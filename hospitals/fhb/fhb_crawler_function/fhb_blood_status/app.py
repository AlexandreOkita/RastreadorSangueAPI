import datetime
import json
import boto3
import fhb_website_crawler
import fhb_image_parser

FHB_URL = 'https://www.hemocentro.df.gov.br/estoque-de-sangue/'

def lambda_handler(event, context):
    image = fhb_website_crawler.fetch_blood_status_image(FHB_URL)
    bloodStatus = fhb_image_parser.retrieve_blood_status_from_image(image)

    # TODO: Extract this logic to a common `createBloodStatusEntry(hospitalName, bloodStatus)`
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('hospitals_blood_status')
    table.put_item(
        Item={
            'hospital': 'fundacao_hemocentro_brasilia', # Full name?
            'date': datetime.now().isoformat(),
            **bloodStatus.toDynamoData()
        }
    )

    # TODO: Check how exceptions are handled. Should I rescue here and build a failed response? Or just let it bubble up?
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "FHB blood supply status updated.",
        }),
    }

if __name__ == '__main__':
    image = fhb_website_crawler.fetch_blood_status_image(FHB_URL)
    bloodStatus = fhb_image_parser.retrieve_blood_status_from_image(image)

    print(bloodStatus)