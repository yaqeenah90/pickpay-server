"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pickpayapi.models import Job, Parent


class JobView(ViewSet):
    """Pick Your Pay Job view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single job"""
        job = Job.objects.get(pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
        #Returns Response -- JSON serialized job""



    def list(self, request):
        """"Handle GET request to get all jobs"""
        jobs = []
        if request.auth.user.parent:
            jobs = Job.objects.all()

        if "completed" in request.query_params:
            if request.query_params['completed'] == "completed":
                jobs = jobs.filter(completed__isnull=False)

        else:
            jobs = Job.objects.filter(child__user=request.auth.user)

        serialized = JobSerializer(jobs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


    def create(self, request):
        """Handle POST requests for jobs

        Returns:
            Response: JSON serialized representation of newly created service ticket
        """
        new_job = Job()
        new_job.parent = Parent.objects.get(user=request.auth.user)
        new_job.description = request.data['description']
        new_job.title = request.data['title']
        new_job.rate = request.data['rate']
        new_job.assigned_to = request.data['assigned_to']
        new_job.save()

        serialized = JobSerializer(new_job)

        return Response(serialized.data, status=status.HTTP_201_CREATED)



class JobSerializer(serializers.ModelSerializer):
    """JSON serializer for jobs
    """
    class Meta:
        model = Job
        fields = ('id', 'title', 'assigned_to', 'description', 'rate')