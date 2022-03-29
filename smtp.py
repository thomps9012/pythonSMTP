from __future__ import print_function

import base64
import mimetypes
import os
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import google_auth_oauthlib
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://mail.google.com/']

def gmail_send_message_with_attachment():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('credentials.json', SCOPES)
    try:
        service = build('gmail', 'v1', credentials=flow)
        mime_message = MIMEMultipart()
        mime_message['from'] = 'thompsonsamuel097@gmail.com'
        mime_message['to'] = 'thomps9012@gmail.com'
        mime_message['subject'] = 'sample with attachment'
        text_part = MIMEText('Hi, this is automated mail with attachment.'
                             'Please do not reply.')
        mime_message.attach(text_part)
        pdf_attachment = build_file_part(file='SamuelThompsonCV.pdf')
        mime_message.attach(pdf_attachment)
        # encoded message
        encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()) \
            .decode()

        send_message_request_body = {
            'message': {

                'raw': encoded_message
            }
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId='me', body=send_message_request_body).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


def build_file_part(file):
    """Creates a MIME part for a file.
    Args:
      file: The path to the file to be attached.
    Returns:
      A MIME part that can be attached to a message.
    """
    content_type, encoding = mimetypes.guess_type(file)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        with open(file, 'rb'):
            msg = MIMEText('r', _subtype=sub_type)
    elif main_type == 'image':
        with open(file, 'rb'):
            msg = MIMEImage('r', _subtype=sub_type)
    elif main_type == 'audio':
        with open(file, 'rb'):
            msg = MIMEAudio('r', _subtype=sub_type)
    else:
        with open(file, 'rb'):
            msg = MIMEBase(main_type, sub_type)
            print(file)
            msg.set_payload(file)
    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    return msg


if __name__ == '__main__':
    gmail_send_message_with_attachment()