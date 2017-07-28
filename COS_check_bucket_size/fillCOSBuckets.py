import boto3
import sys
import argparse

parser = argparse.ArgumentParser(description="Take COS information")
parser.add_argument('--endpoint', action="store", dest="endpoint", help="COS endpoint url")
parser.add_argument('--accessKey', action="store", dest="accessKey", help="AWS secret access key")
parser.add_argument('--keyId', action="store", dest="keyId", help="AWS access key id")
parser.add_argument('--bucketName', action="store", dest="bucketName", help="COS bucket name")
parameters = parser.parse_args()

endpoint = parameters.endpoint
bucketName = parameters.bucketName
keyId = parameters.keyId
accessKey = parameters.accessKey

cos = boto3.resource(
    's3',
    endpoint_url=endpoint,
    aws_access_key_id=keyId,
    aws_secret_access_key=accessKey
    )


offset = 1001
print("connected")
sys.stdout.flush()
for i in range(0,100):
    offset = offset + 1
    key = "test" + str(offset) + ".jpg"
    data = open('test.jpg', 'rb')
    cos.Bucket(bucketName).put_object(Key=key, Body=data)
    print(i)
    sys.stdout.flush()
