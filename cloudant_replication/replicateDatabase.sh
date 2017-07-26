#!/bin/bash
CLOUDANT_USER="username" #
CLOUDANT_PASSWORD="password" #
SOURCE_DB="source_database" #
TARGET_DB="target_database" #
CREATE_TARGET="true"
REPLICATE_ID=$random #
#
python databaseReplicate.py ${CLOUDANT_USER} ${CLOUDANT_PASSWORD} ${SOURCE_DB} ${TARGET_DB} ${REPLICATE_ID} ${CREATE_TARGET} #
