from django.conf import settings
from django.core.files.base import ContentFile

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import permissions

from core.utils.crypto import aes_decrypt, image_to_file

# Create your views here.

# class UserCreateDeactivateAPIView(RegisterView):
#     def perform_create(self, serializer):
#         user = serializer.save(self.request):

#         self.access_token, self.refresh_token = jwt_encode(user)
#         complete_signup(
#             self.request._request, user,
#             allauth_settings.EMAIL_VERIFICATION,
#             None,
#         )
#         return user

class CreateSensitiveInfoAPIView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request: Request):
        data = request.data

        enc_pdf = data.get("pdf", None)

        # de_b64_pdf = base64.b64decode(b64_pdf.encode('utf-8'))
        aes_de_pdf = aes_decrypt(enc_pdf)

        # in_memory = BytesIO(b64_de_pdf)

        to_obj = ContentFile(content=aes_de_pdf)        

        response = Response(to_obj, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="a.pdf"'
        return response






