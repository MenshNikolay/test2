from django.utils import timezone
import uuid



def define_exp_date():
    return (timezone.now() + timezone.timedelta(days=30)).date()


def refresh_token():
    return str(uuid.uuid4())