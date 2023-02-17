#import library for random function
from random import shuffle
from fastapi import FastAPI

#global vars to store audit log
api_call = []
query = []
payload = []

#function to add api calls to audit log file
def add_audit(called_api, query_string, result):

    #format audit log for readability
    audit_log = '{"api_call": ' + '"' + called_api + '"' + ', ' + '"query": ' + '"' + query_string + '"' + ', ' + '"payload": ' + '"' + result + '"' + '}'
        
    audit_file = open("audit.log", "a") 
    audit_file.write(audit_log)
    audit_file.write("\n")
    audit_file.close()

app = FastAPI()

@app.get("/", tags = ['ROOT'])
async def root():
    add_audit("Get api-instructions", "N/A", "N/A")

    return {"message": "Welcome to the Jumble Word API. To jumble a word visit the /jumble-word path with your query word. For example /jumble-word?word=hello"}

@app.get("/jumble-word", tags = ['jumble-word'])
#funciton to scramble a word
async def jumble_word(word):

    temp_list = list(word)
    shuffle(temp_list)
    shuffled_word = ''.join(temp_list)
    
    #add api call to audit log
    add_audit("Get jumble-word", word, shuffled_word)
    
    return shuffled_word

@app.get("/audit", tags=["audit-api"])
async def get_audit():
    
    #add audit api call to log
    add_audit("Get audit-log", "N/A", "N/A")
    
    audit_log = []

    with open("audit.log", "r") as file:
        audit_log = file.readlines()
        audit_log.reverse()

        if len(audit_log) <= 10:
            return audit_log

        else:
            audit_log = audit_log[:10]
            return audit_log