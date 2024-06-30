from django.contrib import admin
from .models import Hero,Education,Skill,contact,skill_list
# Register your models here.
admin.site.register(Hero)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(contact)
admin.site.register(skill_list)
