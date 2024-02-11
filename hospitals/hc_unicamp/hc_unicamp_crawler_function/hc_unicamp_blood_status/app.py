import boto3
import unicamp_blood_center_crawler as unicamp_crawler
import json
from datetime import datetime


UNICAMP_BLOOD_CENTER_URL = 'https://www.hemocentro.unicamp.br/'

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('hospitals_blood_status')
    crawler = unicamp_crawler.UnicampBloodCenterCrawler()

    unicamp_supply = crawler.get_blood_suplies()
    
    table.put_item(
        Item={
            'hospital': 'unicamp',
            'date': datetime.now().isoformat(),
            'a_plus_status': unicamp_supply['A+'],
            'a_minus_status': unicamp_supply['A-'],
            'b_plus_status': unicamp_supply['B+'],
            'b_minus_status': unicamp_supply['B-'],
            'ab_plus_status': unicamp_supply['AB+'],
            'ab_minus_status': unicamp_supply['AB-'],
            'o_plus_status': unicamp_supply['O+'],
            'o_minus_status': unicamp_supply['O-']
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Unicamp blood supply status updated.",
        }),
    }
