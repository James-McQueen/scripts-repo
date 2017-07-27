databaseReplicate.py:

Replicates cloudant databases from a script.

Called by: python databaseReplicate.py --sourceUser --sourcePass --sourceHost --targetUser --targetPass --targetHost --sourceBase --targetBase --createTarget --id
  --sourceUser : source database's cloudant username 
  --sourcePass : source database's cloudant password
  --sourceHost : source database's cloudant host
  --targetUser : Cloudant username for target database. Ignore if same as source
  --targetPass : Cloudant password for target database. Ignore if same as source
  --targetHost : Cloudant host for target database. Ignore if same as source
  --sourceBase : Name of source database
  --targetBase : Name of target database
  --createTarget : Create target database - True/False
  --id : Replication id
