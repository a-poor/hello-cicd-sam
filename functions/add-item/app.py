import os
import json
import uuid
import boto3


def lambda_handler(event, context):
    TABLE_NAME = os.environ["TABLE_NAME"]

    item_info = event["queryStringParameters"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    item_id = uuid.uuid4().hex

    table.put_item(Item={
        "ItemId": item_id,
        "Name": item_info.get("name"),
        "IsCool": bool(item_info.get("cool", False))
    })

    return {
        "statusCode": 200,
        "body": json.dumps({
            "success": True,
            "ItemId": item_id
        })
    }
