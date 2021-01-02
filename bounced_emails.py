import json
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('EmailList')


def lambda_handler(event, context):
    print("starting")
    email = extractEmailAddress(event)
    print("Deleting " + email + " from the EmailList table")
    table.delete_item(
        Key={
            "Email": email
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps(email + ' was deleted from the EmailList table')
    }


def extractEmailAddress(event):
    return "ralamo33@gmail.com";
