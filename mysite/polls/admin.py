# -*- coding:utf-8 -*-
from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	list_display = ('questions', 'pub_date',)
	list_filter = ['pub_date']
	search_fields = ['questions']
	date_hierarchy = 'pub_date'
	fieldsets = [
		(None, {'fields': ['questions']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
## admin.site.register(Choice)
