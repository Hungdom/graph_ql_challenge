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


    MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) 
    AND a.sid <> b.sid AND a.flag=1
    SET b._id = a._id, a.flag=0
    MERGE (a)-[r:link]->(b) 
    WITH a, r, b
    CALL{
        MATCH 
    }
    RETURN DISTINCT a; 


Using unwind:
OPTIONAL MATCH (a: Article {URL: event.URL})

 UNWIND case when a is  null then [1] else [] end AS ignoreMe
 CREATE (a: Article {URL: event.URL})
 UNWIND CASE WHEN event.article.nlp_relations is not null then event.article.nlp_relations else [] end AS relation
match (a)-[:HAS_NLP_TAG]->(t_from) where (t_from:Tag or t_from:Entity) and t_from.value = relation.from.value
match (a)-[:HAS_NLP_TAG]->(t_to) where (t_to:Tag or t_to:Entity) and t_to.value = relation.to.value
call apoc.create.relationship(t_from,relation.type , {}, t_to)


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
CREATE(a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
CREATE(a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
WITH a
MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) 
and a.sid = b.sid and b.sid <> a.sid 
SET a._id = b._id 
WITH a, b
MERGE (a)-[r:link]->(b) 
RETURN DISTINCT a._id as ID, a.sid as SID ;          


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
MERGE(a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
WITH a
MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) 
and a.sid = b.sid and b.sid <> a.sid 
SET a._id = b._id 
WITH a, b
MERGE (a)-[r:link]->(b) 
RETURN DISTINCT a._id as ID, a.sid as SID ;          


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
MERGE(a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
ON CREATE SET a._id = id(a)
ON MATCH SET a._id = id(a) 


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
CREATE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
WITH a
MATCH (a:Seeker), (b:Seeker) 
WHERE (a.email = b.email OR a.phone = b.phone) AND b.sid <> a.sid
MERGE (a)-[r:link]->(b) 



LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
CREATE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
WITH a
MATCH (a:Seeker), (b:Seeker) 
  WHERE (a.email = b.email OR a.phone = b.phone) AND b.sid <> a.sid
MERGE (a)-[r:link]->(b) 
WITH a, b
MATCH p=(a)-[r:link]->(b)
FOREACH (n IN nodes(p) | 
	
    SET n._id = true
    )


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
CREATE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
WITH aMATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) AND b.sid <> a.sid
MERGE (a)-[r:link]->(b) WITH a, b 
MATCH p=(a)-[r:link]->(b)
FOREACH (n IN nodes(p) | 
    MATCH (a:Seeker)-[r:link]->(b:Seeker)
    SET b.`_id` = a.`_id`
    )
    

LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
CREATE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
WITH a MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) AND b.sid <> a.sid
MERGE (a)-[r:link]->(b) WITH a, b 
MATCH p=(a)-[r:link]->(b)
FOREACH (n IN nodes(p) | 
    SET n.`_id` = a.`_id`
    )


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
MERGE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
ON CREATE SET a._id = id(a), a.flag = false
ON MATCH SET a._id = id(a), a.flag = false
WITH a
MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) 
AND b.sid <> a.sid 
MERGE (a)-[r:link]->(b) 
WITH a, b, r
MATCH p=(a)-[r]->(b) WHERE a._id <> b._id and b.flag = false
FOREACH (n IN nodes(p) | 
    SET n.`_id` = a.`_id` , b.flag = true
    )


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
MERGE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
ON CREATE SET a._id = id(a), a.flag = false
ON MATCH SET a._id = id(a), a.flag = false
WITH  COLLECT(a) AS nodesList
UNWIND nodesList as a_node
  MATCH (a:Seeker), (b:Seeker) 
    WHERE a.sid = a_node.sids
      AND (a.email = b.email OR a.phone = b.phone) 
      AND b.sid <> a.sid AND b.flag = false
    SET b._id = a._id, b.flag = true
  MERGE (a)-[r:link]->(b)




LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
MERGE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
ON CREATE SET a._id = id(a), a.flag = false
ON MATCH SET a._id = id(a), a.flag = false
WITH  COLLECT(a) AS nodesList
UNWIND nodesList as a_node
  MATCH (a:Seeker), (b:Seeker) 
    WHERE a.sid = a_node.sid
      AND (a.email = b.email OR a.phone = b.phone) 
      AND b.sid <> a.sid AND b.flag = false
    SET b._id = a._id, b.flag = true
  MERGE (a)-[r:link]->(b)


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvLine
MERGE (a:Seeker {sid:csvLine.sid, name:csvLine.name, email:csvLine.email, phone:csvLine.phone})
ON CREATE SET a._id = id(a), a.flag = false
ON MATCH SET a._id = id(a), a.flag = false
WITH  COLLECT(a) AS nodesList
foreach (i in range(0,length(nodesList)-1) |
	MERGE (u:User {id: (user[i]).id, name: (user[i]).name,year:(user[i]).year})
MERGE (y:W {id: (w[i]).id, name: (w[i]).name,year:(w[i]).year})
MERGE (u)-[:SHARE]->(y))


LOAD CSV WITH HEADERS FROM "file:///seekers.csv" AS csvline
WITH  COLLECT(csvline) AS lines
FOREACH (line in lines |
	MERGE (a:Seeker {sid:line.sid, name:line.name, email:line.email, phone:line.phone})
        ON CREATE SET a._id = id(a), a.flag = false
        ON MATCH SET a._id = id(a), a.flag = false
    
    MATCH (a:Seeker), (b:Seeker) WHERE (a.email = b.email OR a.phone = b.phone) AND b.sid <> a.sid
    )