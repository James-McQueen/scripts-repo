from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.replicator import *
from cloudant.database import *
from random import randint
from time import sleep
import sys

username = sys.argv[1]
password = sys.argv[2]
sourceBase = sys.argv[3]
targetBase = sys.argv[4]
replId = sys.argv[5]

createTarget = sys.argv[6]
if (str(createTarget) == "false") or (str(createTarget) == "False"):
    createTarget = False
else:
    createTarget = True

host = username + ".cloudant.com"
baseURL = "https://" + username + ":" + password + "@" + host


client = Cloudant(username, password, url=baseURL)
client.connect()                                    #connect to cloudant account

replBase = client["_replicator"]                    #connect to _replicator database

print(replId)

source = "https://" + username + ":" + password + "@" + host + "/" + sourceBase
target = "https://" + username + ":" + password + "@" + host + "/" + targetBase           #define source and target dataases

replicationDocument = {
  "source" : source,
  "target" : target,                               #create replication document
  "create_target": createTarget,
  "_id" : replId
}

repldoc = replBase.create_document(replicationDocument)        #Post replicationDocument to _replicator database

replicatorObject = Replicator(client)                          #create replication instance

for doc in replicatorObject.follow_replication(replId):        #check if replication happened
    sleep(0.1)
    try:
        if (str(doc['_replication_state']) == 'completed'):
            print ("done")
    except:
        print("Waiting")
