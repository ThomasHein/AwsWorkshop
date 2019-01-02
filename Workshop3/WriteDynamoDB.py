#!/usr/bin/env python

import boto3
import json
import decimal
import uuid
from boto3.dynamodb.conditions import Key, Attr

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Workshop3')

response = table.put_item(
    Item={
        'CustomerID': str(uuid.uuid4()),
        'Age': 25,
        'Name': "Fritz Meier"
    }
)


print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
