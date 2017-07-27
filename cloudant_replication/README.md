databaseReplicate.py:<br>
Replicates cloudant databases from a script.<br>
<br>
Called by: python databaseReplicate.py --sourceUser --sourcePass --sourceHost --targetUser --targetPass --targetHost --sourceBase --targetBase --createTarget --id <br>
    --sourceUser : source database's cloudant username <br>
    --sourcePass : source database's cloudant password <br>
    --sourceHost : source database's cloudant host <br>
    --targetUser : Cloudant username for target database. Ignore if same as source <br>
    --targetPass : Cloudant password for target database. Ignore if same as source <br>
    --targetHost : Cloudant host for target database. Ignore if same as source <br>
    --sourceBase : Name of source database <br>
    --targetBase : Name of target database <br>
    --createTarget : Create target database - True/False <br>
    --id : Replication id <br>
