from django import forms
from .models import *
from django.forms import fields
from users.models import *

class ChooseGroup(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ('group_id',)

class SendedTasksForm(forms.ModelForm):
    class Meta:
        model = SendedTasks
        fields = ('task', 'taskid')
		

class TasksListForm(forms.ModelForm):
	class Meta:
		model = TaskList
		fields = ('taskname','task','group_id')



