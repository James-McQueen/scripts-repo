#!/bin/bash
CLOUDANT_USER="username" #
CLOUDANT_PASSWORD="password" #
SOURCE_DB="source_database" #
TARGET_DB="target_database" #
REPLICATE_ID="id" #
CREATE_TARGET="False" #
#
python databaseReplicate.py ${CLOUDANT_USER} ${CLOUDANT_PASSWORD} ${SOURCE_DB} ${TARGET_DB} ${REPLICATE_ID} ${CREATE_TARGET}  #
#if [[ $? -ne 0 ]]; then
#  echo "Failed"
#else
#  echo "OK"
#fi
