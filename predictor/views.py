from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import predict_health_risks

class PredictAPI(APIView):
    def get(self, request):
        return Response('Method \"GET\" not allowed. Use \"POST\" Method')
    def post(self, request):
        try:
            data = request.data
            prediction = predict_health_risks(data)
            return Response(prediction)
        except Exception as e:
            return Response(e)