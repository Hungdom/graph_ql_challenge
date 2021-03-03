from neo4j import GraphDatabase
import csv
import os
import shutil
import datetime



class Seeker:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()


    @staticmethod
    def get_seeker(tx):
        seekers = []
        result = tx.run("MATCH (n:Seeker) RETURN n._id as ID, n.sid as SID")
        for record in result:
            seekers.append({'id':record["ID"], 'sid': record["SID"]})
        return seekers

    def get_results(self):
        with self.driver.session() as session:
            seekers = session.read_transaction(self.get_seeker)
            
            return seekers


    def merge_seeker(self, _sid, _name, _email, _phone):
        with self.driver.session() as session:
            session.write_transaction(self._create_one_seeker, _sid, _name, _email, _phone)
            
    @staticmethod
    def _create_one_seeker(tx, _sid, _name, _email, _phone):

        tx.run("MERGE (a:Seeker {sid:$sid, name:$name, email: $email, phone:$phone}) "
                "ON CREATE SET a._id = id(a); ", sid=_sid, name=_name, email=_email, phone=_phone)

        tx.run("MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) "
                "and a.sid = $sid and b.sid <> $sid "
                "SET a._id = b._id "
                "MERGE (a)-[r:link]->(b) ", sid=_sid)

def exec_with_csv_data(executor:Seeker, path_input):
    header = None
    with open(path_input) as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_data:
            if line_count == 0:
                print(f'Column names are :{", ".join(row)}')
                header = row
                line_count += 1
            else:
                print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
                executor.merge_seeker(row[0],row[1],row[2],row[3])
                line_count += 1
        print(f'Processed {line_count} lines.')

    # backup data
    shutil.move('/mnt/d/Projects/github/graph_ql_challenge/Input/sample_input.csv', '/mnt/d/Projects/github/graph_ql_challenge/Input/bk/sample_input.csv')

    # Write back to sample_input.csv



if __name__ == "__main__":
    executor = Seeker("bolt://localhost:7687", "neo4j", "dominic")

    exec_with_csv_data(executor, '/mnt/d/Projects/github/graph_ql_challenge/Input/sample_input.csv')

    seekers = executor.get_results()
    
    

    executor.close()