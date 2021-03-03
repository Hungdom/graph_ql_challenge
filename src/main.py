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
    backup_input_data('/mnt/d/Projects/github/graph_ql_challenge/Input/')

def backup_input_data(src_dir):
    import datetime
    now = str(datetime.datetime.now())[:19]
    now = now.replace(":","_").replace(" ", "")
    shutil.move(src_dir + 'seekers.csv', 
        src_dir + 'bk/seekers.csv_' + str(now))

def backup_output_data(src_dir):
    import datetime
    now = str(datetime.datetime.now())[:19]
    now = now.replace(":","_").replace(" ", "")
    shutil.move(src_dir + 'seeker_master.csv', 
        src_dir + 'bk/seeker_master.csv_' + str(now))

def write_output_csv(seeker_master_output, src_dir):
    toCSV = seeker_master_output
    with open(src_dir+ '/Output/seeker_master.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, 
                        fieldnames=toCSV[0].keys())
        fc.writeheader()
        fc.writerows(toCSV)

if __name__ == "__main__":
    executor = Seeker("bolt://18.140.2.236:7687", "neo4j", "hungle")
    work_space = '/mnt/d/Projects/github/graph_ql_challenge'

    exec_with_csv_data(executor, work_space + '/Input/seekers.csv')
    seekers = executor.get_results()
    backup_output_data(work_space + '/Output/')
    write_output_csv(seekers, work_space)
    
    print(seekers)

    executor.close()