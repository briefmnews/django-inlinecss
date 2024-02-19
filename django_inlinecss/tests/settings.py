SECRET_KEY = "dump-secret-key"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["django_inlinecss/tests/templates"],
        "APP_DIRS": True,
    }
]

INSTALLED_APPS = ("django_inlinecss",)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

STATIC_URL = "/static/"
