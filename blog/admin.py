from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Posts)
class PostAdmin(admin.ModelAdmin):
    list_display =['id','title','date_posted']

admin.site.register(models.Comments)