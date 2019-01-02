import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Workshop3')

response = table.query(
    KeyConditionExpression=Key('Age').eq(35)
)


print("User Database")

for i in response['Items']:
    print("Name", ":", i['AGE'])
