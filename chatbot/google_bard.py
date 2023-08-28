import google.generativeai as palm
from django.conf import settings


def get_response(prompt):
    response = palm.chat(messages=prompt)
    print(response)
    return response.last