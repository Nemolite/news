import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *

# class PostModel:
#    def __init__(self,title,content):
#        self.title = title
#        self.content = content

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_crate = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    cat_id = serializers.IntegerField()


# def encode():
#     model = PostModel('ttt','qwrwer')
#     model_sr = NewsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json =JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"ttt","content":"qwrwer"}')
#     data = JSONParser.parse(stream)
#     serializer = NewsSerializer(data = data)
#     serializer.is_valid()
#     print(serializer.validated_data)