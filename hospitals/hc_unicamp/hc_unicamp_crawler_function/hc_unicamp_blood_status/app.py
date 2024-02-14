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
    print(unicamp_supply)
    table.put_item(
        Item={
            'hospital': 'unicamp',
            'date': datetime.now().isoformat(),
            'a_plus_status': unicamp_supply.get('A+', 'unknown'),
            'a_minus_status': unicamp_supply.get('A-', 'unknown'),
            'b_plus_status': unicamp_supply.get('B+', 'unknown'),
            'b_minus_status': unicamp_supply.get('B-', 'unknown'),
            'ab_plus_status': unicamp_supply.get('AB+', 'unknown'),
            'ab_minus_status': unicamp_supply.get('AB-', 'unknown'),
            'o_plus_status': unicamp_supply.get('O+', 'unknown'),
            'o_minus_status': unicamp_supply.get('O-', 'unknown')
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Unicamp blood supply status updated.",
        }),
    }
