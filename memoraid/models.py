import datetime

from django.db import models
from django.utils import timezone

import validators

# You can find an example class diagram for the Model at
# http://yuml.me/edit/53759046
# You'll notice that the Model class provided by Django is 
# elided (it doesn't have the attributes or methods listed.

class Memoraid(models.Model):
    memoraid_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',validators=[validators.not_future])
    def __unicode__(self):
        return self.memoraid_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    memoraid = models.ForeignKey(Memoraid)
    choice_text = models.CharField(max_length=200,validators=[validators.not_unauthorized_word])
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
		
class Course(models.Model):
	course_tag = models.CharField(max_length=5)
	course_description = models.CharField(max_length=80)
	relation_to = models.CharField(max_length=30)
	relation_description = models.CharField(max_length=80)
	def __unicode__(self):
		return self.course_tag, self.course_description, self.relation_to, self.relation_description
	
class Lists(models.Model):
	courses = models.ForeignKey(Course)
	lists_name = models.CharField(max_length=20)
	lists_description = models.CharField(max_length=80)
	relation_to = models.CharField(max_length=30)
	relation_description = models.CharField(max_length=80)	
	def __unicode__(self):
		return self.lists_name, self.lists_description, self.relation_to, self.relation_description
	
class Element(models.Model):
	lists = models.ForeignKey(Lists)
	element_name = models.CharField(max_length=20)
	element_description = models.CharField(max_length=80)
	relation_to = models.CharField(max_length=30)
	relation_description = models.CharField(max_length=80)	
	def __unicode__(self):
		return self.element_name, self.element_description, self.relation_to, self.relation_description