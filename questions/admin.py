from django.contrib import admin
from questions.models import Question, Response, User

admin.site.register(Question)
admin.site.register(Response)
admin.site.register(User)
