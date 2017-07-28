

# databaseReplicate.py
Replicates cloudant databases from a script, and waits until the replication is complete.

## Software pre-requisites 
- python 3
- python 'boto3' module 
  run: ```pip install boto3```

## Syntax
```
python checkBucketSize.py 
--accessKey {AWS-secret-access-key} --keyId {AWS-Access-Key-Id} --endpoint {endpoint-url} --bucketName {name} 
--sizeLimit {size-limit} 
```
### Parameters
`--accessKey` : your AWS secret access key

`--keyId` : your AWS access key id

`--endpoint` : cos endpoint url

`--bucketName` : name of bucket to check size of

`--sizeLimit` : size (in bytes) the bucket shouldn't exceed

```
