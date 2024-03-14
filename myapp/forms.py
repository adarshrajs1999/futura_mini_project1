from django import forms
from myapp.models import Todo


class todoform(forms.ModelForm):
    class Meta:
        model=Todo
        # fields=('subject','data','date')
        fields = ('__all__')


# In django,a meta class is a class used to define the behavior of other classes.
# Here the meta class is used to define the model and fields of the todoform class's
# instances by Todo model and 'subject','data' and 'date' fields respectively.