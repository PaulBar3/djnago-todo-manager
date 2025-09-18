from django import forms

from todo_list.models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ("title",)

        widgets = {
            "title": forms.Textarea(attrs={"cols": 30, "rows": 5})
            }
