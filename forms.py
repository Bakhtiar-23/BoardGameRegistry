# boardgames/forms.py
from django import forms
from .models import BoardGame, Loan

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['title', 'description']  # Add other fields as needed

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['returned_at']  # Add other fields as needed
