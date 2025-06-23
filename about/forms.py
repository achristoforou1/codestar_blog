"""
Forms for the about app.
Includes the collaboration request form.
"""
from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    Form for submitting a collaboration request.

    **Fields:**
    - ``name``: Name of the requester.
    - ``email``: Email address of the requester.
    - ``message``: Message content from the requester.

    Uses :model:`about.CollaborateRequest`.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')