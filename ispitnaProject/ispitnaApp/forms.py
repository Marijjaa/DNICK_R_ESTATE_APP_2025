from django import forms

from ispitnaApp.models import RealEstate


class RealEstateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RealEstateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ["is_reserved", "is_bought"]:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = RealEstate
        fields = '__all__'
