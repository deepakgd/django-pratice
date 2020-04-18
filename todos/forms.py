from django import forms
from .models import Todos

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        # to show all input field in form use this
        fields = "__all__" 

        # to show selected field in form
        # fields = ["title", "description", "status"]
    
    # validation for title field
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if len(title) < 4:
            raise forms.ValidationError("Title must be greater than 3 characters")
        else:
            return title