from django.conf import settings # import the settings file

def website_info(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
            'WEBSITE_NAME': settings.WEBSITE_NAME,
            'PHONE_NUMBER': settings.PHONE_NUMBER,
            'EMAIL':       settings.EMAIL,
            'ADDRESS':      settings.ADDRESS,

            'FACEBOOK': settings.FACEBOOK,
            'LINKEDIN': settings.LINKEDIN,
            'TWITTER': settings.TWITTER,
            'RSS': settings.RSS,
            'PINTEREST': settings.PINTEREST,
            'WHATSAPP': settings.WHATSAPP,
            }