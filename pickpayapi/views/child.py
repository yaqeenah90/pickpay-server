"""View module for handling requests for customer data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pickpayapi.models import Child


class ChildView(ViewSet):
    """Pick Your Pay API child view"""

    def list(self, request):
        """Handle GET requests to get all children

        Returns:
            Response -- JSON serialized list of children
        """

        children = Child.objects.all()
        serialized = ChildSerializer(children, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single child

        Returns:
            Response -- JSON serialized child record
        """

        child = Child.objects.get(pk=pk)
        serialized = ChildSerializer(child)
        return Response(serialized.data, status=status.HTTP_200_OK)


class ChildSerializer(serializers.ModelSerializer):
    """JSON serializer for children"""
    class Meta:
        model = Child
        fields = ('id', 'full_name', 'financial_goal')