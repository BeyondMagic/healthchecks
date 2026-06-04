from __future__ import annotations

import json

from django import forms
from hc.front.forms import LaxURLField


class AddGotifyForm(forms.Form):
    error_css_class = "has-error"
    PRIORITY_CHOICES = [(0, "0"), (2, "2"), (5, "5"), (9, "9")]

    token = forms.CharField(max_length=50)
    url = LaxURLField(max_length=1000, assume_scheme="https")
    priority = forms.TypedChoiceField(
        choices=PRIORITY_CHOICES, coerce=int, required=False, initial=5
    )
    priority_up = forms.TypedChoiceField(
        choices=PRIORITY_CHOICES, coerce=int, required=False, initial=5
    )

    def clean_priority(self) -> int:
        value = self.cleaned_data.get("priority")
        return 5 if value is None else value

    def clean_priority_up(self) -> int:
        value = self.cleaned_data.get("priority_up")
        return 5 if value is None else value

    def get_value(self) -> str:
        return json.dumps(dict(self.cleaned_data), sort_keys=True)
