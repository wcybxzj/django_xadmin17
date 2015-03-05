from django.contrib import admin
from models import JieSpider

class JieSpiderAdmin(admin.ModelAdmin):
    pass

admin.site.register(JieSpider, JieSpiderAdmin)

