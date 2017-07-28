#!/bin/bash

function testReturnCodeWhenContentsSmallerThanHugeBucketLimit() {
  python checkBucketSize.py --endpoint --bucketName --accessKey --keyId --sizeLimit 99999999999999999999999999999999999999999999999999
  local rc=$?
  local expected=0
  if [[ $rc -ne expected ]]; then
    echo "failed"
    failedTests=$failedTests+1
  fi
}

function testMessagesWhenContentsSmallerThanHugeBucketLimit() {
  local messages_got=$(python checkBucketSize.py --endpoint --bucketName --accessKey --keyId --sizeLimit 999999999999999999999999999999999999999999999)
  local messages_expected="Bucket acceptable size"
  if [[ ! "$messages_got" == "$messages_expected" ]]; then
    echo "failed"
    failedTests=$failedTests+1
  fi
}

function testReturnCodeWhenContentsBiggerThanBucketLimit() {
  python checkBucketSize.py --endpoint --bucketName --accessKey --keyId --sizeLimit 1
  local rc=$?
  local expected=1
  if [[ $rc -ne expected ]]; then
    echo "failed"
    failedTests=$failedTests+1
  fi
}

function testMessagesWhenContentsBiggerThanBucketLimit() {
  local messages_got=$(python checkBucketSize.py --endpoint --bucketName --accessKey --keyId  --sizeLimit 1)
  local messages_expected="Bucket size too big"
  if [[ ! "$messages_got" == "$messages_expected" ]]; then
    echo "failed"
    failedTests=$failedTests+1
  fi
}

testReturnCodeWhenContentsSmallerThanHugeBucketLimit
testMessagesWhenContentsSmallerThanHugeBucketLimit
testMessagesWhenContentsBiggerThanBucketLimit
testReturnCodeWhenContentsBiggerThanBucketLimit

echo "Tests failed: ${failedTests}"
