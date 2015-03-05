import xadmin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class EntryAdmin(object):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

xadmin.site.register(models.Entry, EntryAdmin)
xadmin.site.register(models.Tag)
