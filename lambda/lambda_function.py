import io
import os

import boto3
from PIL import Image

s3 = boto3.resource('s3')

bucket_name = os.environ.get('BUCKET_NAME_TEMPLATE', None)
if not bucket_name:
    raise Exception('Env variable BUCKET_NAME_TEMPLATE does not provided!')


def lambda_handler(event, context):
    key = event['Records'][0]['s3']['object']['key']
    img_name = os.path.splitext(key)[0]

    jpg_file = io.BytesIO()
    obj = s3.Object(bucket_name.format('jpeg'), key)
    obj.download_fileobj(jpg_file)
    img = Image.open(jpg_file)

    for file_format in ['bmp', 'png', 'gif']:
        file_obj = io.BytesIO()
        img.save(file_obj, file_format.upper())
        file_obj.seek(0)
        s3.Bucket(bucket_name.format(file_format)).put_object(
            Key=f'{img_name}.{file_format}',
            Body=file_obj)
