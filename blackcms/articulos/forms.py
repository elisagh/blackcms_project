from django.forms import ModelForm
from articulos.models import Articulo

# Create the form class.
class ArticuloForm(ModelForm):
     class Meta:
         model = Articulo
         exclude = ('autor',)
