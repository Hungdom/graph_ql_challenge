# graph_ql_challenge
Challenge for my quick learn and productivity

## Setup for local dev
In local dev, this project build on WSL Ubuntu and Docker on Window desktop.
### 1. Setup docker for neo4j graph database 
```
docker-compose up -d
```

### 2. Python env
```
pip3 install -p requirements.txt
```

### 3. Setup path

Change variable work_space in src/main.py:
```
work_space = '/place/to/graph_ql_challenge'
```

Cchange variable work_space in Input/.py:
```
work_space = '/place/to/graph_ql_challenge/Input'
```

neo4j://18.140.2.236:7687


http://18.140.2.236:7474/browser/