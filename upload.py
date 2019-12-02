#!/usr/bin/env python3

# mod with ansible by azabiralov from azabiralov.dellin.local

from minio import Minio
from minio.error import ResponseError

uploader = Minio('192.168.150.201:9001',
                 access_key='EwNdTteymL7',
                 secret_key='dmh3sUf4qbN',
                 secure=False)


try:
       uploader.make_bucket("picture", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise

   
try:
       uploader.fput_object('picture', 'bad.jpg', './bad.jpg')
except ResponseError as err:
       print(err)
