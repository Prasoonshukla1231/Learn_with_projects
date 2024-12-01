from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        
        lable={
            "title": "Title",
            "description": "Description",
        } 
        
        widgets={
            "title": forms.TextInput(attrs={"placeholders":"Buy Groceries"}),
            "description": forms.TextInput(attrs={"placeholders":"Visit super market and  buy some groceries"}),
        }