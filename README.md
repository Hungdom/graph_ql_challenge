# graph_ql_challenge
Challenge for my quick learn and productivity


## Ideas
input:
sid, name, email, phone
1, aaa, aaa@g.com, 12345
2, aab, aaa@g.com, 12333
3, abb, aaa@g.com, 12222
4, ddd, ddd@g.com, 12222
5, daa, bcd@g.com, 12222
6, eee, eee@g.com, 55555
7, eff, eee@g.com, 56666

 
- row -> 
    how to create node?
    node: key->value pairs
    node name
    - properties: sid, name

- relations: connect 2 nodes 
    - how to create relations.
    - email, phone
- labels: set of nodes or relationships. A node or relationship can contain one or more labels.
- data browser:


##
Process insert data:
1. Create node
    create (n:Seeker);
    create (n:Seeker {sid:1, name:"aaa", email: "aaa", phone:1234});
    create (n:Seeker {sid:2, name:"aab", email: "aaa", phone:1235})
2. Create relationship
    MATCH (a:Seeker), (b:Seeker)
    WHERE a.email = b.email 
    CREATE (a)-[:email_link]->(b)
    RETURN a,b;

3. Delete node and relationship:
    MATCH (n) DETACH DELETE n


output:
id, sid
1, 1
1, 2
1, 3
1, 4
1, 5
2, 6
2, 7