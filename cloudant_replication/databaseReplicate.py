###26/07/17###
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.replicator import *
from cloudant.database import *
from random import randint
from time import sleep
import sys
import argparse

syntaxString = "\n Give --sourceHost --sourcePass --sourceHost --targetUser --targetPass --targetHost --sourceBase --targetBase --createTarget --id   when running. \n--createTarget is given as 'true' or 'false'."

def failureCheck(error):
    if error == 1:              #Check if something went wrong
        sys.exit(1)

def connect(user, passw, url):
    global client
    client = Cloudant(user, passw, url=url)
    try:
        client.connect()            #connect to cloudant account
    except:
        print("Error: Could not connect to Cloudant. Check credentials")
        return 1

def checkCreateTarget(createTarget):
    if (str(createTarget).upper() == "FALSE"):
        createTarget = False
    elif (str(createTarget).upper() == "TRUE"):
        createTarget = True
    else:
        print("Error: Invalid createTarget: must be 'true' or 'false'" + syntaxString)
        return 1

def checkReplication(replId):
    for doc in replicatorObject.follow_replication(replId):        #check if replication happened
        sleep(1) #seconds
        try:
            if (str(doc['_replication_state']) == 'completed'):
                print ("Done.")
            elif (str(doc['_replication_state']) == 'error'):
                print("Error in replication. Did not replicate. Reason: " + str(doc['_replication_state_reason']))
                return 1
        except:
            None

def getCommandLineParameters():
    parser = argparse.ArgumentParser(description="Take cloudant information")
    parser.add_argument('--sourceUser', action="store", dest="sourceUser", help="Cloudant username for source database")
    parser.add_argument('--sourcePass', action="store", dest="sourcePass", help="Cloudant password for source database")
    parser.add_argument('--sourceHost', action="store", dest="sourceHost", help="Cloudant host for source database")
    parser.add_argument('--targetUser', action="store", dest="targetUser", help="Cloudant username for target database. Ignore if same as source")
    parser.add_argument('--targetPass', action="store", dest="targetPass", help="Cloudant password for target database. Ignore if same as source")
    parser.add_argument('--targetHost', action="store", dest="targetHost", help="Cloudant host for target database. Ignore if same as source")
    parser.add_argument('--sourceBase', action="store", dest="sourceBase", help="Name of source database")
    parser.add_argument('--targetBase', action="store", dest="targetBase", help="Name of target database")
    parser.add_argument('--createTarget', action="store", dest="createTarget", help="True/False create the target database")
    parser.add_argument('--id', action="store", dest="id", help="Replication id")
    cloudantDetails = parser.parse_args()

    global sourceUsername, sourcePassword, sourceHost, targetUsername, targetPassword, targetHost, sourceBase, targetBase, createTarget, replId
    sourceUsername = cloudantDetails.sourceUser
    sourcePassword = cloudantDetails.sourcePass
    sourceHost = cloudantDetails.sourceHost

    if cloudantDetails.targetUser == None:
        targetUsername = sourceUsername
    else:
        targetUsername = cloudantDetails.targetUser

    if cloudantDetails.targetPass == None:
        targetPassword = sourcePassword
    else:
        targetUsername = cloudantDetails.targetUser

    if cloudantDetails.targetHost == None:
        targetHost = sourceHost
    else:
        targetHost = cloudantDetails.targetHost

    sourceBase = cloudantDetails.sourceBase
    targetBase = cloudantDetails.targetBase
    createTarget = cloudantDetails.createTarget
    replId = cloudantDetails.id

def buildURL():
    try:
        global baseURL, source, target
        baseURL = "https://" + targetUsername + ":" + targetPassword + "@" + targetHost
        source = "https://" + sourceUsername + ":" + sourcePassword + "@" + sourceHost + "/" + sourceBase
        target = "https://" + targetUsername + ":" + targetPassword + "@" + targetHost + "/" + targetBase           #define source and target dataases
    except TypeError:
        print("Error: Credentials, source, or target database not given.")
        return 1

def main():
    getCommandLineParameters()

    failureCheck(buildURL())

    failureCheck(checkCreateTarget(createTarget)) #Check create_target was correct

    failureCheck(connect(targetUsername, targetPassword, baseURL)) # Connect to Cloudant

    replBase = client["_replicator"]                    #connect to _replicator database

    replicationDocument = {
        "source" : source,
        "target" : target,                               #create replication document
        "create_target": bool(createTarget),
        "_id" : replId
    }

    repldoc = replBase.create_document(replicationDocument)        #Post replicationDocument to _replicator database

    global replicatorObject
    replicatorObject = Replicator(client)                          #create replication instance

    failureCheck(checkReplication(replId))                         #Check if replication was successful

main()
