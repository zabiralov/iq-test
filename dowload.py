#!/usr/bin/env python3

# mod with ansible by azabiralov from azabiralov.dellin.local

from minio import Minio
from minio.error import ResponseError

downloader = Minio('192.168.150.201:9001',
                 access_key='download',
                 secret_key='PvJK7TNVoxe',
                 secure=False)

try:
    data = downloader.get_partial_object('picture', 'bad.jpg', 1000)
    with open('good.jpg', 'wb') as file_data:
        for d in data:
            file_data.write(d)
except ResponseError as err:
    print(err)
