from django import forms
from stack.models import Post, Tags, Category

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    title = forms.CharField()
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget = forms.CheckboxSelectMultiple
        )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget = forms.CheckboxSelectMultiple
        )
