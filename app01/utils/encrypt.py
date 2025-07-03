from django.conf import settings
import hashlib


def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()

# import hashlib
#
# SECRET_KEY = 'django-insecure-hkrj5qe6)4-oe)g&+s-_)90r8$$fk_*a1w33=2wikt4!^4_h6c'
#
# def md5(data_string):
#     obj = hashlib.md5(SECRET_KEY.encode('utf-8'))
#     obj.update(data_string.encode('utf-8'))
#     return obj.hexdigest()
#
# str = "yuanqing"
# print(md5(str))
