###26/07/17###
###Use: Pass cloudant username, password, source databse name, target database name and create target into replicateDatabase.sh and run.
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.replicator import *
from cloudant.database import *
from random import randint
from time import sleep
import sys

def failureCheck(error):
    if error == 1:              #Check if something went wrong
        sys.exit(1)

def connect(user, passw, url):
    global client
    client = Cloudant(user, passw, url=url)
    try:
        client.connect()            #connect to cloudant account
    except:
        print("Could not connect to Cloudant. Check credentials")
        return 1

def checkCreateTarget(createTarget):
    if (str(createTarget) == "false") or (str(createTarget) == "False"):
        createTarget = False
    elif (str(createTarget) == "true") or (str(createTarget) == "True"):
        createTarget = True
    else:
        print("Invalid createTarget")
        return 1

def checkReplication(replId):
    for doc in replicatorObject.follow_replication(replId):        #check if replication happened
        sleep(0.2) #seconds
        try:
            if (str(doc['_replication_state']) == 'completed'):
                print ("Done.")
            elif (str(doc['_replication_state']) == 'error'):
                print("Error in replication. Did not replicate. Reason: " + str(doc['_replication_state_reason']))
                return 1
        except:
            print(doc)

def getCommandLineParameters():
    try:
        global username, password, sourceBase, targetBase, replId, createTarget
        username = sys.argv[1]
        password = sys.argv[2]
        sourceBase = sys.argv[3]
        targetBase = sys.argv[4]                    #Get necessary values from shell script
        replId = sys.argv[5]
        createTarget = sys.argv[6]
    except IndexError:
        print("One or more parameters not specified")
        return 1


failureCheck(getCommandLineParameters())

host = username + ".cloudant.com"
baseURL = "https://" + username + ":" + password + "@" + host
source = "https://" + username + ":" + password + "@" + host + "/" + sourceBase
target = "https://" + username + ":" + password + "@" + host + "/" + targetBase           #define source and target dataases

failureCheck(checkCreateTarget(createTarget)) #Check create_target was correct

failureCheck(connect(username, password, baseURL)) # Connect to Cloudant

replBase = client["_replicator"]                    #connect to _replicator database

replicationDocument = {
  "source" : source,
  "target" : target,                               #create replication document
  "create_target": bool(createTarget),
  "_id" : replId
}

repldoc = replBase.create_document(replicationDocument)        #Post replicationDocument to _replicator database

replicatorObject = Replicator(client)                          #create replication instance

failureCheck(checkReplication(replId))
