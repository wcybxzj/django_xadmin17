# -*- coding: utf-8 -*-
import xadmin
from polls.models import Choice, Question, Post

#通过父类别设置不同的内容页choice效果
class ChoiceInline(object):
#class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 #每次打开question 增加显示3个choice

class QuestionAdmin(object):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information',#前缀
         {
             'fields': ['pub_date'],    #model字段
             'classes': ['collapse']    #样式可以折叠
         }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently') #列表页多显示几个内容
    list_filter = ['pub_date'] #列表页右侧filter
    search_fields = ['question_text']

class PostAdmin(object):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(Post, PostAdmin)
