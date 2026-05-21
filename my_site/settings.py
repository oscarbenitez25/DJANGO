from pathlib import Path

# Camí base del projecte (BASE_DIR)
BASE_DIR = Path(__file__).resolve().parent.parent

# CLAU SECRETA: canvia-la en producció per a seguretat-xyz123
SECRET_KEY = "django-insecure-change-me-in-production-xyz123"

# MUNTATGE DE DEPURACIÓ: Activat per a desenvolupament
DEBUG = True

# HOSTS PERMESOS: "*" permet qualsevol connexió en desenvolupament
ALLOWED_HOSTS = ["*"]

# APLICACIONS INSTAL·LADES
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
    "blog",
]

# LOGICIAL INTERMEDIARI (MIDDLEWARE)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CONFIGURACIÓ DE LES ENRUTADORES DE L'ARREL URL
ROOT_URLCONF = "my_site.urls"

# PLANTILLES DE DISSENY (TEMPLATES)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# APLICACIÓ INTERFÍCIE DE SERVIDOR WEB (WSGI)
WSGI_APPLICATION = "my_site.wsgi.application"

# BASES DE DADES
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# VALIDATORS DE CONTRASENYA D'USUARI
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# CONFIGURACIÓ INTERNACIONAL I HORÀRIA
LANGUAGE_CODE = "ca"
TIME_ZONE = "Europe/Madrid"
USE_I18N = True
USE_TZ = True

# ARXIUS ESTÀTICS (CSS, JavaScript, Imatges de disseny)
STATIC_URL = "/static/"
STATICFILES_DIRS = []

# ARXIUS MULTIMÈDIA (Arxius pujats pels usuaris)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# TIPUS DE CAMP AUTOINCREMENTAL PER DEFECTE
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"