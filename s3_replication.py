#!/usr/bin/env python
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    copy_source = {
          'Bucket': 'sagar111',
          'Key': event['Records'][0]['s3']['object']['key']
        }
    bucket = s3.Bucket('sagar1111')
    bucket.copy(copy_source, event['Records'][0]['s3']['object']['key'])
    return 'Object copied'


