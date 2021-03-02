import json 

def get_sid():
    with open('d:\workspace\graph_ql_challenge\Input\config.json') as f:
        data = json.load(f)
    f.close()
    return data["latest_sid"]

def set_sid(new_sid)
    f = open("d:\workspace\graph_ql_challenge\Input\config.json", "w")
    f.write("{\"latest_sid\":{new_sid}}")
    f.close()

def auto_gen_email():
    pass

def auto_gen_phone_number():
    pass

if __name__ == "__main__":
    # seekers: { sid, name, email, phone }

    pass