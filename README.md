# graph_ql_challenge
This git have branch:
- main: for master dev
- release: for release code on AWS EC2 and connect with Neo4j database on AWS

Focus:
- For the Idea and Study process you can see the detail on README in path: src/README.md
- Challenge for my quick learn and productivity.
- For setup and re-implement please follow 3.Setup for local dev.
- All the Process you can see on the Images_Implement_Process folder.

# Connect to the viewer on Browser:
Please send me your public IP first then I'll add you can connect to DB IP.
IP: http://18.140.2.236:7474/browser/

To access database you need to fill some info:
- url bolt: neo4j://18.140.2.236:7687
- account: neo4j
- pass: hungle

## 1. Create input data:
All the input data be create in folder Input:

- Script auto gen inputdata:
```
auto_gen_seekers.py
```
## 2. Main Source
Follow up main step: 
- Read input data in path: Input/seekers.csv
- Merge data into Neo4j graph database.
    - each row -> store node.
    - Create relation ship betwen them.
- Move the input file into backup folder: Input/bk/seekers.csv_<time moving in bk>
- Move the old output in to backup folder: Output/bk/seekers_master.csv_<time moving in bk>
- Return output in path: Output/seeker_master.csv

## 3.Setup for local dev
In local dev, this project build on WSL Ubuntu and Docker on Window desktop.
### a. Setup docker for neo4j graph database 
```
docker-compose up -d
```

### b. Python env
```
pip3 install -p requirements.txt
```

### c. Setup path

Change variable work_space in src/main.py:
```
work_space = '/place/to/graph_ql_challenge'
```

Cchange variable work_space in Input/.py:
```
work_space = '/place/to/graph_ql_challenge/Input'
```

### d. Setup IP, account, pass
connect to query: neo4j://18.140.2.236:7687

Connect to see on the browser: http://18.140.2.236:7474/browser/