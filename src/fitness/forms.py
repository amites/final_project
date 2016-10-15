from django.forms import ModelForm
from django import forms

from fitness.models import UserBMIProfile, UserWeight, WorkoutType


class BMIForm(ModelForm):
    class Meta:
        model = UserBMIProfile
        fields = ('human_weight', 'human_height_ft', 'human_height_in', )

class BMIDateForm(ModelForm):
    class Meta:
        model = UserWeight
        fields = ('weight', )

class WorkoutForm(ModelForm):
    class Meta:
        model = WorkoutType
        fields = ('muscle_group', 'workout_start', )


"""
class WorkoutForm(ModelForm):
    muscle_group = forms.ModelMultipleChoiceField(
        queryset=muscle_group.objects.all(),
        widgets=forms.CheckboxSelectMultiple
"""