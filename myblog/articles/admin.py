from django.contrib import admin
from .models import Articles, Category,Comments

# Register your models here.
admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Comments)
