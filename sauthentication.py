from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse
import json


def json_response(key, value, status):
    return HttpResponse(
        json.dumps({key: value}),
        content_type='application/javascript; charset=utf8',
        status=status
    )


def auth(request):
    if request.method == 'POST':
        # If user is not authenticated we do our thing
        if not request.user.is_authenticated():
            # Really important variables
            data = json.loads(request.body)
            username = data['username']
            password = data['password']

            if username and password:
                # Match the given username and password to our django users
                user = authenticate(username=username, password=password)
                # Check if the user exists...
                if user is not None:
                    # ...and if the user is active...
                    if user.is_active:
                        # ...we login and return a json response
                        login(request, user)
                        return json_response('success', True, 200)
                    # But if the user is inactive we return a bad json response
                    else:
                        return json_response('failed', 'The account you are trying to access is disabled.', status=400)
                # If the user credentials doesnt match we send out a bad json response
                else:
                    return json_response('failed', 'Could not match given username and password.', status=400)
            else:
                # If the some credentials was missed, we send out a bad json response
                return json_response('failed', 'Both the username and password must be provided.', status=400)
        # If user is already authenticated, we also send out a bad json response
        else:
            return json_response('failed', 'Already authenticated.', status=400)
    # If the we receive a GET ?logout=True
    elif request.GET.get('logout') == "True":
        # ... and the user is authenticated, we logout.
        if request.user.is_authenticated():
            logout(request)
            return json_response('success', 'Signed out authenticated user.', status=200)
        # otherwise we return a bad json_response
        else:
            return json_response('failed', 'No user is logged on.', status=400)
    else:
        return json_response('failed', 'Allowed methods: POST and GET=?logout=True', status=405)