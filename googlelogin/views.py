from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponse

from googlelogin.backends import GoogleAuthBackend


__author__ = 'gautam'

@login_required
def home(request):
    return HttpResponse()

def login(request):
    if not request.user.is_authenticated():
        redirect_uri = GoogleAuthBackend.get_auth_redirect(request)
        return redirect(redirect_uri)


def oauth2redirect(request):
    code = request.GET.get('code')
    error = request.GET.get('error')
    if code:
        user = auth.authenticate(code=code, request=request)
        auth.login(request, user)
        return redirect(reverse('home'))
    elif error:
        return HttpResponse(str(error))
