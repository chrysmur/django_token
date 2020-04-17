from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {
            'message': "Response one"
        }
        return Response(content, status=status.HTTP_200_OK)