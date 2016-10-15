from __future__ import unicode_literals

from datetime import datetime
from fitness import myFields

from django.db import models


WORKOUT_TYPE = (('Chest', 'Chest'),
                ('Back', 'Back'),
                ('Shoulders', 'Shoulders'),
                ('Abs', 'Abs'),
                ('Legs', 'Legs'),
                ('Arms', 'Arms'),
                ('Cardio', 'Cardio'))

DAYS_OF_WEEK = (('Sunday', 'Sunday'),
                 ('Monday', 'Monday'),
                 ('Tuesday', 'Tuesday'),
                 ('Wednesday', 'Wednesday'),
                 ('Thursday', 'Thursday'),
                 ('Friday', 'Friday'),
                 ('Saturday', 'Saturday'))


#class UserProfile(models.Model):



class UserBMIProfile(models.Model):
    human_weight = models.FloatField(help_text='Enter weight in pounds')
    human_height_ft = models.IntegerField(help_text='Enter height in feet')
    human_height_in = models.IntegerField(help_text='Enter height in inches')

    def __unicode__(self):
        return 'User BMI - %s' % self.body_mass_calc()

    #function to calculate body mass
    def body_mass_calc(self):
        weight = self.human_weight        #human weight in pounds
        weight_in_kg = float(weight / 2.2)      #converts human weight from pounds to kilograms
        height_ft = self.human_height_ft        #human height in feet
        height_in = self.human_height_in        #human height in inches
        height_total_in = float((height_ft * 12) + height_in) #converts feet to inches and produces total hight in inches
        height_in_m = float(height_total_in * .0254)         #converts human height from inches to meters
        body_mass = float(weight_in_kg / (height_in_m * 2))    #calculates BMI
        return round(body_mass, 1)

    @property
    def bmi_feedback(self): #Returns/displays BMI results
        bmi_string = "Your BMI is %s. A healthy average is between 18.5 and 25." % self.body_mass_calc()
        if self.body_mass_calc() < 18.5:
            return bmi_string
        elif self.body_mass_calc() >= 18.5 and self.body_mass_calc() < 25:
            return "Your BMI is %s, you are average." % self.body_mass_calc()
        elif self.body_mass_calc() >= 25 and self.body_mass_calc() < 30:
            return bmi_string
        elif self.body_mass_calc() >= 30:
            return bmi_string


#user weight with datetime and form
class UserWeight(models.Model):
    profile = models.ForeignKey(UserBMIProfile)
    weight = models.FloatField()
    weight_create = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'UserWeight -- {} -:- {}'.format(self.profile.body_mass, self.weight_create)

#user selects work out date and time from start to end
class WorkoutType(models.Model):
    muscle_group = models.CharField(max_length=25, choices=WORKOUT_TYPE)
    workout_start = models.DateTimeField(default='01:01:01')
    Workout_end = models.TimeField(default='01:01:01', blank=True, auto_now=False)

    def __unicode__(self):
        return 'Work out {}'.format(self.muscle_group)
