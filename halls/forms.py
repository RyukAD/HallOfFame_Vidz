# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 00:32:45 2020

@author: dubey
"""

from .models import Video
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        
        model = Video
        fields = ['url']
        labels = {'url': 'YouTube URL'}
        
        
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos ')