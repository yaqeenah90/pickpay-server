"""View module for handling requests for customer data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pickpayapi.models import Parent

class ParentView(ViewSet):
    """Pick Your Pay API parent view"""

    def list(self, request):
        """Handle GET requests to get all parents

        Returns:
            Response -- JSON serialized list of parents
        """

        parents = Parent.objects.all()
        serialized = ParentSerializer(parents, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single parent

        Returns:
            Response -- JSON serialized parent record
        """

        parent = Parent.objects.get(pk=pk)
        serialized = ParentSerializer(parent)
        return Response(serialized.data, status=status.HTTP_200_OK)


class ParentSerializer(serializers.ModelSerializer):
    """JSON serializer for parents"""
    class Meta:
        model = Parent
        fields = ('id', 'full_name', 'monthly_budget')