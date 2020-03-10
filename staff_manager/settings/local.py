from .common import *

environ.Env.read_env(os.path.join(BASE_DIR, '.env_local'))


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DEBUG', default=True)

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INSTALLED_APPS += ('debug_toolbar',)

# DEBUG_TOOLBAR_CONFIG = {
#     'DISABLE_PANELS': [
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#         'debug_toolbar.panels.templates.TemplatesPanel',
#     ],
#     'SHOW_TEMPLATE_CONTEXT': True,
#     'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
# }


# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['example.com'])


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get_value('DB_NAME', default='db'),
        'USER': env.get_value('DB_USER', default='user'),
        'PASSWORD': env.get_value('DB_PASSWORD', default='password'),
        'HOST': env.get_value('DB_HOST', default='localhost'),             # Or an IP Address that your DB is hosted on
        'PORT': env.get_value('DB_PORT', default='3306'),
    }
}

# DATABASES = {
#     # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
#     'default': env.db()
# }
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Email
# ------------------------------------------------------------------------------
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = env('SERVER_EMAIL')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = env.get_value('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# PROJECT CONFIGURATION
# ------------------------------------------------------------------------------

