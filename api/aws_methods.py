import boto3
import base64
import re
import io
import uuid
from PIL import Image

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

aws_region = 'eu-central-1'
bucket_name = 'harold-portfolio-api-bucket'

def list_resources():
  for bucket in s3.buckets.all():
    print(bucket.name)

def put_image(name, source_data, file_ext):
  response = s3.Bucket(bucket_name).put_object(Key = f"testing2/{name}.{file_ext}", Body = source_data)
  name = "+".join(name.split())
  image_url = f'https//{bucket_name}.s3.{aws_region}.amazonaws.com/{name}'
  return image_url

def upload_file_to_folder(dir_name, base64_image):
  def generate_object_name():
    # The generated bucket name must be between 3 and 63 chars long
    return '/'.join(["", str(uuid.uuid4())]) + ".jpg"

  image_data = re.sub('^data:image/.+;base64,', '', base64_image)
  decoded = base64.b64decode(image_data)
  image = Image.open(io.BytesIO(decoded))

  obj_name = generate_object_name()
  file_name = dir_name + obj_name


  response = s3_client.upload_fileobj(io.BytesIO(decoded), bucket_name, file_name)

  dir_name = "+".join(dir_name.split())
  image_url = f'https://{bucket_name}.s3.{aws_region}.amazonaws.com/{dir_name+obj_name}'

  return image_url
  

