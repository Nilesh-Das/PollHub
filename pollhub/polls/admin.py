from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = "PollHub Admin"
admin.site.site_title = "PollHub Admin Panel"
admin.site.index_header = "PollHub Admin"

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_text']}),
				('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),]
	inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)