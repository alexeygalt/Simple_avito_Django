from django.contrib import admin

from ads.models import Ad

from ads.models import Comment

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

admin.site.register(Ad)
admin.site.register(Comment)