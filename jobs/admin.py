from django.contrib import admin

# Register your models
# if you want to show this model in the admin page
from .models import job
admin.site.register(job)
