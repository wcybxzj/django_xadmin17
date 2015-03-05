<<<<<<< HEAD
# -*- coding: utf-8 -*-
import xadmin
=======
>>>>>>> 876e8a2b99035bf5d5faae56fda480bf4112a089
from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


<<<<<<< HEAD
class EntryAdmin(object):
=======
class EntryAdmin(MarkdownModelAdmin):
>>>>>>> 876e8a2b99035bf5d5faae56fda480bf4112a089
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

<<<<<<< HEAD
xadmin.site.register(models.Entry, EntryAdmin)
xadmin.site.register(models.Tag)
=======
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
>>>>>>> 876e8a2b99035bf5d5faae56fda480bf4112a089
