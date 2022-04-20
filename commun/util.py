from django.core.mail import EmailMessage
import traceback
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from django.core.mail import send_mail
import os
from django.conf import settings
media_root = settings.MEDIA_ROOT

class Util:
    @staticmethod
    def send_email(subject:str,message:str,source:str,to:list,cc:list,attachments:list):
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=source,
            to=to,
            cc=cc,
            #reply_to=['cheng@blah.com'],
            # when the reply or reply all button is clicked, this is the reply to address, normally you don't have to set this if you want the receivers to reply to the from_email address
        )
        email.content_subtype = 'html'  # if the email body contains html tags, set this. Otherwise, omit it
        for file in attachments:
            email.attach_file(os.path.join(media_root,file))
        email.send(fail_silently=False)
