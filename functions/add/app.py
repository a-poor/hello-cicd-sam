import os
import json
import boto3


def lambda_handler(event, context):
    TABLE_NAME = os.environ["TABLE_NAME"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    table.put_item(Item={})


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        })
    }
