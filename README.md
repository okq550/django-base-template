# django-base-template

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py startapp app_2 django_project_root/app_2

This creates the app in the django_project_root/ directory, following your existing pattern.
2. Update the app's apps.py
Edit django_project_root/app_2/apps.py to use the correct Python path:
pythonfrom django.apps import AppConfig


class App2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_project_root.app_2'  # Important: full Python path
3. Add the app to INSTALLED_APPS
In configuration_root/settings.py:
pythonINSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_project_root.app_1',
    'django_project_root.app_2',  # Add this line
]
4. Create URLs for the new app (optional)
Create django_project_root/app_2/urls.py:
pythonfrom django.urls import path
from . import views

urlpatterns = [
    # Your URL patterns here
]
5. Include the app's URLs in the main config (optional)
In configuration_root/urls.py:
pythonfrom django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_project_root.app_1.urls')),
    path('app2/', include('django_project_root.app_2.urls')),  # Add this
]
That's it! The key points to remember are:

Always create apps inside django_project_root/
Update the name in apps.py to include the full path
Use the full path when adding to INSTALLED_APPS