from django import forms

from todo_list.models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ("title",)

    title = forms.CharField(max_length=250)
