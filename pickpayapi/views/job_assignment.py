"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pickpayapi.models import JobAssignment


class JobAssignmentView(ViewSet):
    """Pick your Pay job assignment view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type"""
        job_assignment = JobAssignment.objects.get(pk=pk)
        serializer = JobAssignmentSerializer(job_assignment)
        return Response(serializer.data)
        #Returns Response -- JSON serialized game type""



    def list(self, request):
        """Handle GET requests to get all game types"""
        job_assignments = JobAssignment.objects.all()
        serializer = JobAssignmentSerializer(job_assignments, many=True)
        return Response(serializer.data)
        #Returns Response -- JSON serialized list of game types"""

class JobAssignmentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = JobAssignment
        fields = ('id', 'job', 'child', 'completed')

