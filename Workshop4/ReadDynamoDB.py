#!/usr/bin/env python

import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Workshop4')

response = table.query(
    KeyConditionExpression=Key('CustomerID').eq("5c2c6f3cd4db1d94ea747444")
)


print("User Database")

for i in response['Items']:
    print("Name", ":", i['Name'])
