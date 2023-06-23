"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pickpayapi.models import JobAssignment, Child, Job


class JobAssignmentView(ViewSet):
    """Pick your Pay job assignment view"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single job assignment

        Returns:
            Response -- JSON serialized parent record
        """

        assignment = JobAssignment.objects.get(pk=pk)
        serialized = JobAssignmentSerializer(assignment)
        return Response(serialized.data, status=status.HTTP_200_OK)
    


    def create(self, request):
        """Handle POST operations
        Returns
        Response -- JSON serialized job instance
        """

        new_assignment = JobAssignment()
        
        new_assignment.child = Child.objects.get(user=request.auth.user)
        new_assignment.completed = request.data['completed']
        new_assignment.job = Job.objects.get(pk=request.data["job"])
        new_assignment.save()
        
        serializer = JobAssignmentSerializer(new_assignment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """Handles PUT request for single assignment"""
        # Select the targeted assignment using pk
        assignment = JobAssignment.objects.get(pk=pk)

        # Get the completed instance the client request
        is_completed = request.data.get('completed', False)

        # Assign that completed instance to variable.
        assignment.completed = is_completed

        # Save the updated assignment
        assignment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def list(self, request):
        """Handle GET requests to get all job assignments"""
        job_assignments = JobAssignment.objects.all()
        serializer = JobAssignmentSerializer(job_assignments, many=True)
        return Response(serializer.data)
        #Returns Response -- JSON serialized list of game types"""

    def destroy(self, request, pk=None):
        """Handle DELETE requests for job assignments

        Returns:
            Response -- None with 204 status code
        """
        assignment = JobAssignment.objects.get(pk=pk)
        assignment.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class JobAssignmentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = JobAssignment
        fields = ('id', 'job', 'child', 'completed')

