from rest_framework.response import Response
import datetime

def BaseResponse(data):
    return Response({'result': data, 'timeIn': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})