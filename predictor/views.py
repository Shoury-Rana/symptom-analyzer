from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import predict_health_risks

class PredictAPI(APIView):
    def post(self, request):
        data = request.data
        prediction = predict_health_risks(data)
        return Response(prediction)