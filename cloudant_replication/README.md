

# databaseReplicate.py
Replicates cloudant databases from a script, and waits until the replication is complete.

## Software pre-requisites 
- python 3
- python 'cloudant' module 
  run: ```pip install cloudant```

## Syntax
```
python databaseReplicate.py 
--sourceUser {user} --sourcePass {password} --sourceHost {host} --sourceBase {database-name} 
[--targetUser {user}] [--targetPass {password}] [--targetHost {host}] --targetBase {database-name} 
--createTarget {true|false} --id {replicatorId}
```
### Parameters
`--sourceUser` : source database's cloudant username 

`--sourcePass` : source database's cloudant password

`--sourceHost` : source database's cloudant host

`--sourceBase` : Name of source cloudant database

`--targetUser` : Cloudant username for target database. Ignore if same as source
Optional. If missing, then a value of --sourceUser is assumed.

`--targetPass` : Cloudant password for target database. Ignore if same as source
Optional. If missing, then a value of --sourcePass is assumed.

`--targetHost` : Cloudant host for target database. Ignore if same as source
Optional. If missing, then a value of --sourceHost is assumed.

`--targetBase` : Name of target database

`--createTarget` : If the database doesn't exist, should it be created ?
  Valid valies: True/False/true/false

`--id` : Replicator id. Must not exist already.

```
