from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Who)
admin.site.register(Term)
admin.site.register(Plan)
admin.site.register(Subscription)

# Register your models here.
