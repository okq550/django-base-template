# django-base-template

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


configuration_root DIR ---

settings.py

INSTALLED_APPS = [
    .
    .
    .
    'django_project_root.app_1',
]

urls.py

path('', include('django_project_root.app_1.urls',))



app_1 DIR --
apps.py

name = 'django_project_root.app_1'