import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = "xgboost-2020-10-17-12-22-23-769"
runtime= boto3.client('runtime.sagemaker')
sns = boto3.client('sns')
def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    payload = data['data']
    print(payload)
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    print(response)
    result = json.loads(response['Body'].read().decode())

    if result> 0.5:
        sns.publish(TopicArn = 'arn:aws:sns:us-east-1:208552737735:samplesns' , Message = 'Your result is positive .Please consider your doctor asap')
        return('malignant')
    else :
        return('benign')
    return (result)

   
