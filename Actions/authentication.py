from rest_framework import authentication, exceptions
from Actions.models import User
import jwt
from TrackActions.settings import SECRET_KEY


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return None
        try:
            payload = self.decode_token(token)
            user = User.objects.get(email=payload["email"])
            return (user, payload)
        except Exception:
            raise exceptions.AuthenticationFailed("User doesnt exist")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY)
        except Exception:
            raise exceptions.AuthenticationFailed("The token is invalid")

        return payload
