import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('your_table_name')

    hospital = event['queryStringParameters']['hospital']
    
    limit = int(event['queryStringParameters'].get('limit', 10))  # default to 10 if not provided
    if limit < 1 or limit > 100:
        return {
            'statusCode': 400,
            'body': 'Limit must be between 1 and 100'
        }

    response = table.query(
        KeyConditionExpression=Key('hospital').eq(hospital),
        Limit=limit,
        ScanIndexForward=False
    )

    items = response['Items']

    return {
        'statusCode': 200,
        'body': items
    }