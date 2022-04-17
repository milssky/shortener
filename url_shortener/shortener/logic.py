from hashlib import sha1
from random import choice
import string

from django.conf import settings


def get_short_urlcode():
    code = "".join(
        [choice(string.ascii_lowercase) for _ in range(8)]
    )
    return sha1(code.encode()).hexdigest()[:8]

def make_short_url(slug: str) -> str:
    return f"{settings.SITE_ROOT}{slug}/"