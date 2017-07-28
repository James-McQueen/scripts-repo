import boto3
import sys
import argparse

syntaxString = "\n Give --endpoint --accessKey --keyId --bucketName --sizeLimit when running."


def getCommandLineParameters():

    parser = argparse.ArgumentParser(description="Take COS information")
    parser.add_argument('--endpoint', action="store", dest="endpoint", help="COS endpoint url")
    parser.add_argument('--accessKey', action="store", dest="accessKey", help="AWS secret access key")
    parser.add_argument('--keyId', action="store", dest="keyId", help="AWS access key id")                      #Get necessray information when script is called
    parser.add_argument('--bucketName', action="store", dest="bucketName", help="COS bucket name")
    parser.add_argument('--sizeLimit', action="store", dest="sizeLimit", help="Specify COS bucket size limit in bytes")
    parameters = parser.parse_args()

    check = [parameters.endpoint, parameters.accessKey, parameters.keyId, parameters.bucketName, parameters.sizeLimit]
    for parameter in check:
        try:
            if parameter.type() == None:
                None
        except AttributeError:                                                 #check all parameters are given
            print("Error: One or more parameters not set." + syntaxString)
            sys.exit()

    global endpoint, bucketName, sizeLimit, keyId, accessKey
    endpoint = parameters.endpoint
    bucketName = parameters.bucketName
    try:
        sizeLimit = int(parameters.sizeLimit)                                   #Check a size limit was given
    except TypeError:
        print("Error: Bucket size limit not given" + syntaxString )
        sys.exit()
    keyId = parameters.keyId
    accessKey = parameters.accessKey

def connectToCOS():
    global cos
    cos = boto3.resource(
        's3',                                       #Set credentials to access cloud object storage
        endpoint_url=endpoint,
        aws_access_key_id=keyId,
        aws_secret_access_key=accessKey
        )

def checkBucketSize():
    size = 0

    getCommandLineParameters()
    connectToCOS()

    try:
        for obj in cos.Bucket(bucketName).objects.all():  #Iterate over all objects in given bucket
            size = size + obj.size                        #Add up total size of given bucket
    except ValueError:
        print("Error: Name of bucket not provided")       #Check bucket name was given
        sys.exit()

    ########print("Bucket size is: " + str(size))
    if (size > sizeLimit):
        print("Bucket size too big")
        sys.exit(1)                                        #Evaluate if bucket is bigger than specified limit
    else:
        print("Bucket acceptable size")
        sys.exit(0)

checkBucketSize()
