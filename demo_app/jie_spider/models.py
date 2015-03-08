# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class JieSpider(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created_at = models.DateTimeField()
    mid = models.BigIntegerField()
    text = models.TextField()
    image0 = models.CharField(max_length=200, blank=True)
    image1 = models.CharField(max_length=200)
    image2 = models.CharField(max_length=200, blank=True)
    image3 = models.CharField(max_length=200, blank=True)
    video_url = models.CharField(max_length=250, blank=True)
    images = models.CharField(max_length=200, blank=True)
    screen_name = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=200)
    uid = models.CharField(max_length=30)
    reposts_count = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=250)
    width = models.IntegerField()
    height = models.IntegerField()
    size = models.IntegerField()
    addtime = models.DateTimeField()
    passtime = models.DateTimeField()
    weight = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    md5 = models.CharField(max_length=50)
    type = models.IntegerField()
    flash = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    remark = models.CharField(max_length=255)
    category = models.CharField(max_length=10)
    tag = models.CharField(max_length=200)
    win = models.IntegerField()
    fail = models.IntegerField()
    hot = models.DecimalField(max_digits=2, decimal_places=1)
    top_day = models.IntegerField()
    top_week = models.IntegerField()
    top_month = models.IntegerField()
    top_all = models.IntegerField()
    love = models.IntegerField()
    favourite = models.IntegerField()
    follower = models.IntegerField()
    repost = models.IntegerField()
    comment = models.IntegerField()
    ding = models.IntegerField()
    cai = models.IntegerField()
    user_id = models.IntegerField()
    is_gif = models.IntegerField()
    is_http = models.IntegerField()
    modifytime = models.DateTimeField()
    image_md5 = models.CharField(max_length=32)
    like_id = models.BigIntegerField(blank=True, null=True)
    is_modify = models.IntegerField()
    jie_mid = models.BigIntegerField(blank=True, null=True)
    image_hash = models.CharField(max_length=90)
    text_uniq_status = models.IntegerField(blank=True, null=True)
    sameid = models.IntegerField(blank=True, null=True)
    samepercent = models.IntegerField(blank=True, null=True)
    samefrom = models.IntegerField(blank=True, null=True)
    original_image = models.CharField(max_length=200)
    user_type = models.IntegerField(blank=True, null=True)
    external_link = models.CharField(max_length=512)
    foreign_type = models.IntegerField()
    foreign_id = models.IntegerField()
    labels = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=512, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jie_spider'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
