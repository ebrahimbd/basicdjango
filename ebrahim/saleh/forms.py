from django import forms


from .models  import bookproduct
class ProductForm(forms.ModelForm):
    class Meta:
        model = bookproduct
        fields = [
            'title',
            'description',
            'price'
        ]
