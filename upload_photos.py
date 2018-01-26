
from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers

appid = '##############'
secret_id = '###################'
secret_key = '####################'
bucket = '#################'

client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)

print (client.face_newperson('1', ['group2',], CIFile('1刘德华.jpeg')))
print (client.face_setinfo('1', '刘德华'))
