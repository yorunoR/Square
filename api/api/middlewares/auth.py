import os

import jwt
import requests
from cryptography import x509
from django.core.cache import cache

from account.models import User

audience = os.environ["FIREBASE_PROJECT_ID"]


def decode_jwt(token):
    try:
        unverified_decoded = jwt.get_unverified_header(token)
        kid_claim = unverified_decoded["kid"]

        cert = cache.get(kid_claim)
        if cert is None:
            response = requests.get("https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com")
            certs = response.json()
            cert = certs[kid_claim].encode("utf-8")

            public_key = x509.load_pem_x509_certificate(cert).public_key()
            payload = jwt.decode(token, public_key, ["RS256"], options=None, audience=audience)
            cache.set(kid_claim, cert, payload.get("exp"))
        else:
            public_key = x509.load_pem_x509_certificate(cert).public_key()
            payload = jwt.decode(token, public_key, ["RS256"], options=None, audience=audience)

        return {"uid": payload.get("user_id"), "email": payload.get("email"), "name": payload.get("name")}
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None
    except Exception:
        return None


class JWTAuthenticationMiddleware:
    def resolve(self, next, root, info, **kwargs):
        token = info.context.headers.get("Authorization", "").split("Bearer ")[-1]
        if token:
            payload = decode_jwt(token)
            user = User.objects.filter(uid=payload["uid"]).first()
            info.context.user = user
            info.context.uid = payload["uid"]
            info.context.email = payload["email"]
            info.context.name = payload["name"]
        else:
            info.context.user = None
        return next(root, info, **kwargs)
