import os
from GetphotoPath import xz
from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers

appid = '##############'
secret_id = '###################'
secret_key = '####################'
bucket = '#################'

client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)

input_photopath=xz()
result = client.face_identify('group2', CIFile(input_photopath))
value_no=80
value_yes=96
person=client.face_getinfo(result['data']['candidates'][0]['person_id'])
person_id=person['data']['person_id']
person_name = person['data']['person_name']
original_photo_name=person_id+person_name+'.jpeg'
this_path = os.getcwd()
original_photopath = this_path+'/'+original_photo_name
print (input_photopath,original_photopath,person_name)
