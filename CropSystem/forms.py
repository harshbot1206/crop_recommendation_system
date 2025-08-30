from django import forms

class CropForm(forms.Form):
    location = forms.CharField(
        label='Location', 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter city name (e.g., Mumbai, Delhi)',
            'class': 'form-control'
        }),
        required=True
    )
    
    # Soil parameters (will be auto-filled but can be manually adjusted)
    N = forms.FloatField(
        label='Nitrogen (N)', 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
    P = forms.FloatField(
        label='Phosphorus (P)', 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
    K = forms.FloatField(
        label='Potassium (K)', 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
    ph = forms.FloatField(
        label='pH', 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'step': '0.1'})
    )
    
    # Weather parameters (will be auto-filled)
    temperature = forms.FloatField(
        label='Temperature (°C)', 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'step': '0.1'})
    )
    humidity = forms.FloatField(
        label='Humidity (%)', 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'step': '0.1'})
    )
    rainfall = forms.FloatField(
        label='Rainfall (mm)', 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'step': '0.1'})
    )
    
    def clean(self):
        cleaned_data = super().clean()
        # Ensure at least one set of parameters is provided
        if not any([cleaned_data.get('N'), cleaned_data.get('P'), cleaned_data.get('K'), 
                   cleaned_data.get('ph'), cleaned_data.get('temperature'), 
                   cleaned_data.get('humidity'), cleaned_data.get('rainfall')]):
            raise forms.ValidationError("Please enter a location to auto-fill parameters or manually enter values.")
        return cleaned_data
