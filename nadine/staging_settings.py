import os
import datetime
import dj_database_url

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

PRODUCTION = False
DEBUG = True
ALLOWED_HOSTS = [
  '*',
  'runway-nadine.herokuapp.com'
]


# Admins
ADMINS = (
    ('YOU', 'you@yourdomain.com'),
)

DATABASES = {
  'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}

# Site Information
SITE_NAME = "Runway"
SITE_DOMAIN = "runway.is"
SITE_PROTO = "https"

# Email Settings
EMAIL_ADDRESS = "joe@runway.is"
EMAIL_HOST = "smtp.example.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_HOST_USER = "username"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = "[COWORKING] "  # or None if you want no subject prefix
BILLING_EMAIL_ADDRESS = "billing@example.com"

# Team Settings
TEAM_EMAIL_ADDRESS = "team@officenomads.com"
TEAM_MEMBERSHIP_PLAN = "ON Team"

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = "fgPUDJgpjsll0NCtfHliNQpvsmWOTS5nYdqHCLT2KXUwy1SThHKoQQwdOOAk2kD"

# List of possible public calendar designations and the color for display
CALENDAR_DICT = {'Public':'red', 'Member Only': 'RGBA(71, 159, 198, 1)' }

# Google Settngs
#GOOGLE_ANALYTICS_ID = "YOUR-GOOGLE-CODE"
#GOOGLE_CALENDAR_ID = "YOUR-GOOGLE-CALENDAR-ID"
#GOOGLE_API_KEY = "YOUR-API-KEY"

# Mailgun Settings
#MAILGUN_API_KEY = "YOUR-MAILGUN-API-KEY"
#MAILGUN_DOMAIN = "YOUR-MAILGUN-DOMAIN"
#MAILGUN_DEBUG = False

# USAePay Settings
# Use API Doc/Literal WSDL
# USA_EPAY_GATE = "https://www.usaepay.com/gate.php"
# USA_EPAY_FORM = "https://www.usaepay.com/interface/epayform/"
# Used for adding billing profiles
# USA_EPAY_FORM_KEY="YOUR_KEY"
# USA_EPAY_SOAP_1_2 = "https://www.usaepay.com/soap/gate/YOUR_CODE/usaepay.wsdl"
# USA_EPAY_SOAP_1_4 = "https://www.usaepay.com/soap/gate/YOUR_CODE/usaepay.wsdl"
# USA_EPAY_SOAP_KEY = "YOUR_KEY"
# USA_EPAY_SOAP_PIN = "YOUR_PIN"

# Mailchimp Settings
#MAILCHIMP_API_KEY = "goMonkeygo"
#MAILCHIMP_NEWSLETTER_KEY = "melikekey"
#MAILCHIMP_WEBHOOK_KEY = "hookedonhooks"

# Xero Integration Settings
# Generate an RSA key and register it with Xero as a private application.
# openssl genrsa -out privatekey.pem 1024
# openssl req -new -x509 -key privatekey.pem -out publickey.cer -days 1825
# openssl pkcs12 -export -out public_privatekey.pfx -inkey privatekey.pem -in publickey.cer
#XERO_CONSUMER_KEY = "secretkey"
#XERO_PRIVATE_KEY = "/keys/privatekey.pem"

# Slack Settings
SLACK_API_TOKEN = "xoxp-2331654072-3448119480-50994654198-e742ef6f97"
SLACK_TEAM_URL = "https://runway.slack.com/"

# Arp Settings
ARPWATCH_SNMP_SERVER = '192.168.1.1'
ARPWATCH_SNMP_COMMUNITY = 'yourcommunitystring'
ARPWATCH_NETWORK_PREFIX = '192.168.'

# HID Door System
# Encryption Key must be a URL-safe base64-encoded 32-byte key.
# https://cryptography.io/en/latest/fernet/
#HID_ENCRYPTION_KEY = "YOUR-HID-ENCRYPTION-KEY"
#HID_KEYMASTER_URL = "http://127.0.0.1:8000/doors/keymaster/"
#HID_POLL_DELAY_SEC = 60

# Other Settings
BILLING_START_DATE = datetime.date(2009, 11, 17)
NEW_MEMBER_DEPOSIT = 500
NON_MEMBER_DROPIN_FEE = 25

# Settings Generated by ./manage.py setup
COUNTRY = "US"
TIME_ZONE = "America/Los_Angeles"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
