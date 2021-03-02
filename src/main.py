from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_greeting(self, ):
        with self.driver.session() as session:
            greeting = session.write_transaction(
                self._create_one_seeker, _sid, _name, _email, _phone)

    @staticmethod
    def _create_one_seeker(tx, _sid, _name, _email, _phone):
        result = tx.run("CREATE (n:Seeker) "
                        "SET a.sid = $sid "
                        "RETURN a.message + ', from node ' + id(a)", sid=_sid)
        return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "dominic")
    greeter.print_greeting("hello, world")
    greeter.close()