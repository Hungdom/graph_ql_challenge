import json 
import random
import string
import names
import csv


domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:3] 

def get_one_random_domain(domains):
    return random.choice(domains)

def get_one_random_name(letters):
    return ''.join(random.choice(letters) for i in range(5))

def generate_random_emails():
    return get_one_random_name(letters) + '@' + get_one_random_domain(domains)

def generate_random_phone():
    return random.randint(10000, 99999)

def generate_random_name():
    return names.get_first_name()

def get_sid(work_space):
    f = open(work_space+ '/config.txt', "r")
    sid = f.read()
    f.close()
    return sid

def set_sid(new_sid):
    f = open(work_space+ '/config.txt', "w")
    str_write = str(new_sid)
    f.write(str_write)
    f.close()



if __name__ == "__main__":
    # seekers: { sid, name, email, phone }
    work_space = '/mnt/d/Projects/github/graph_ql_challenge/Input'
    latest_sid = int(get_sid(work_space))

    num_loop = 1000


    with open(work_space + '/seekers.csv', mode='w') as csv_file:
        fieldnames = ['sid', 'name', 'email', 'phone']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for each in range(latest_sid+1, latest_sid+num_loop+1):
            writer.writerow({'sid': each, 'name': generate_random_name(),
             'email': generate_random_emails(), 'phone': generate_random_phone()})
        

    new_sid = latest_sid+num_loop
    set_sid(new_sid)
