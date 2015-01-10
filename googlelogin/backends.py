from django.conf import settings
from django.contrib.auth import get_user_model

from django.core.urlresolvers import reverse
from googleapiclient.discovery import build
import httplib2
from oauth2client.client import OAuth2WebServerFlow

__author__ = 'gautam'
User = get_user_model()


class GoogleAuthBackend(object):
    @staticmethod
    def get_flow(redirect_uri):
        flow = OAuth2WebServerFlow(
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET,
            scope=settings.GOOGLE_SCOPE,
            redirect_uri=redirect_uri,
            access_type='online',
            state=''
        )
        return flow


    @staticmethod
    def get_auth_redirect(request):
        flow = GoogleAuthBackend.get_flow(request.build_absolute_uri(reverse('oauth2redirect')))
        return flow.step1_get_authorize_url()

    def get_user_info(self, credential):
        http = httplib2.Http()
        http = credential.authorize(http)
        service = build('oauth2', 'v2', http=http)

        # this call gets us email info. however, decrypting the ID_TOKEN would have done it too
        user = service.userinfo().get().execute()
        return user

    @staticmethod
    def update_user(user, user_info):
        user.first_name = user_info.get('given_name')
        user.last_name = user_info.get('family_name')
        user.email = user_info.get('email')
        user.profile_picture = user_info.get('picture')
        user.save()

    def authenticate(self, code=None, request=None):
        if code:
            flow = GoogleAuthBackend.get_flow(request.build_absolute_uri(reverse('oauth2redirect')))
            credential = flow.step2_exchange(code)
            email = credential.id_token.get("email")
            user_info = self.get_user_info(credential)
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                user = User(username=email)
            GoogleAuthBackend.update_user(user, user_info)
            return user
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
