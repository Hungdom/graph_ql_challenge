# graph_ql_challenge
Challenge for my quick learn and productivity


## Ideas
input:
```
sid, name, email, phone
1, aaa, aaa@g.com, 12345
2, aab, aaa@g.com, 12333
3, abb, aaa@g.com, 12222
4, ddd, ddd@g.com, 12222
5, daa, bcd@g.com, 12222
6, eee, eee@g.com, 55555
7, eff, eee@g.com, 56666
```
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

## Process insert data:

### 1. Create node

    create (n:Seeker);
    create (n:Seeker {sid:1, name:"aaa", email: "aaa", phone:1234});
    create (n:Seeker {sid:2, name:"aab", email: "aaa", phone:1235});

    create (n:Seeker {sid:1, name:"aaa", email: "aaa@g.com", phone:12345});
    create (n:Seeker {sid:2, name:"aab", email: "aaa@g.com", phone:12333});
    create (n:Seeker {sid:3, name:"abb", email: "aaa@g.com", phone:12222});
    create (n:Seeker {sid:4, name:"ddd", email: "ddd@g.com", phone:12222});
    create (n:Seeker {sid:5, name:"eee", email: "eee@g.com", phone:56666});
    create (n:Seeker {sid:6, name:"eff", email: "eee@g.com", phone:55555});
### 2. Create relationship

    MATCH (a:Seeker), (b:Seeker)
    WHERE a.email = b.email 
    CREATE (a)-[:email_link]->(b)
    RETURN a,b;

    MATCH (a:Seeker), (b:Seeker)
    WHERE a.phone = b.phone 
    CREATE (a)-[:phone_link]->(b)
    RETURN a,b;


### 3. Merge and add relation ship.
    ```
    MERGE (a:Seeker {sid:1, name:"aaa", email: "aaa@g.com", phone:12345, id:1})
    ON CREATE SET a._id = id(a)

    MERGE (a:Seeker {sid:2, name:"aab", email: "aaa@g.com", phone:12333})
    ON CREATE SET a._id = id(a)

    MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone )
    and a.sid <> b.sid and id(a) <> b._id
    SET a._id = id(b)
    MERGE (a)-[r:link]->(b)
    RETURN a._id, a.sid


    MERGE (a:Seeker {sid:3, name:"abb", email: "aaa@g.com", phone:12222})
    ON CREATE SET a.id = id(a)

    MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone )
    and a.sid = 3 and b.sid <> 3
        SET a.id = b.id
    MERGE (a)-[r:link]->(b);

    MERGE (a:Seeker {sid:4, name:"ddd", email: "ddd@g.com", phone:12222})
    ON CREATE SET a.id = id(a)

    MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone )
    and a.sid = 4 and b.sid <> 4
        SET a.id = b.id
    MERGE (a)-[r:link]->(b);

    MERGE (a:Seeker {sid:5, name:"eee", email: "eee@g.com", phone:56666})
    ON CREATE SET a.id = id(a);

    MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone ) 
    and a.sid = 5 and b.sid <> 5
        SET a.id = b.id
    MERGE (a)-[r:link]->(b);

    MERGE (a:Seeker {sid:6, name:"eff", email: "eee@g.com", phone:55555})
    ON CREATE SET a.id = id(a);

    MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone ) 
    and a.sid = 6 and b.sid <> 6
        SET a.id = b.id
    MERGE (a)-[r:link]->(b);
    ```

### 4. Delete node and relationship:

    MATCH (n) DETACH DELETE n

### 5. Create UNIQUE:

    CREATE CONSTRAINT ON (n:Seeker) ASSERT n.sid IS UNIQUE;

### 6. Loop to get output

    MATCH (n:Seeker) RETURN n._id, n.sid

## output:
```
id, sid
1, 1
1, 2
1, 3
1, 4
1, 5
2, 6
2, 7
```



MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone ) 
AND a.sid <> b.sid AND a._id <> 0
SET a._id = 0
MERGE (a)-[r:link]->(b)
RETURN a._id, a.sid


MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) AND a.sid ="2"
AND a.sid <> b.sid
SET a._id = 0
MERGE (a)-[r:link]->(b)


MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) AND a.sid ="7"
AND a.sid <> b.sid AND b._id <> 0
SET a._id = 0
MERGE (a)-[r:link]->(b)


MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone)
AND a.sid <> b.sid AND b._id <> a._id
SET b._id = a._id
MERGE (a)-[r:link]->(b)
RETURN b._id, b.sid


MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone)
AND a.sid <> b.sid AND b._id <> a._id
SET b._id = a._id
MERGE (a)-[r:link]->(b)
RETURN b._id, b.sid

MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone)
AND a.sid <> b.sid AND b._id <> a._id
SET b._id = a._id
MERGE (a)-[r:link]->(b)
RETURN b._id, b.sid

MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone)
AND a.sid <> b.sid AND b._id <> a._id
SET b._id = a._id
MERGE (a)-[r:link]->(b)
RETURN b._id, b.sid


MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone)
AND a.sid <> b.sid AND b._id <> a._id
SET b._id = a._id
MERGE (a)-[r:link]-(b)
RETURN a._id, a.sid