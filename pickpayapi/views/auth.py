from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from pickpayapi.models import Parent, Child


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
    request -- The full HTTP request object
    '''
    email = request.data['email']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(email=email, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)

        data = {
            'valid': True,
            'token': token.key,
            'parent': authenticated_user.is_parent
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
    request -- The full HTTP request object
    '''
    account_type = request.data.get('account_type', None)
    email = request.data.get('email', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)

    if account_type is not None \
        and email is not None\
        and first_name is not None \
        and last_name is not None \
        and password is not None:

        if account_type == 'parent':
            parent_user = request.data.get('parent_user', None)
            if parent_user is None:
                return Response(
                    {'message': 'You must provide username for a parent'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        elif account_type == 'child':
            child_user = request.data.get('child_user', None)
            if child_user is None:
                return Response(
                    {'message': 'You must provide a username m for a child'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {'message': 'Invalid account type. Valid values are \'parent\' or \'child\''},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Create a new user by invoking the `create_user` helper method
            # on Django's built-in User model
            new_user = User.objects.create_user(
                username=request.data['email'],
                email=request.data['email'],
                password=request.data['password'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name']
            )
        except IntegrityError:
            return Response(
                {'message': 'An account with that email address already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        account = None
        is_parent = False 
            #
        if account_type == 'child':
            account = Child.objects.create(
                financial_goal=request.data['financial_goal'],
                user= new_user
            )
        elif account_type == 'parent':
            
            is_parent = True
            new_user.save()
            account = Parent.objects.create(
                monthly_budget=request.data['monthly_budget'],
                user= new_user
            )
            # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=account.user)
                # Return the token to the client
                
        data = { 'token': token.key, 'parent':is_parent  }
        return Response(data)
    