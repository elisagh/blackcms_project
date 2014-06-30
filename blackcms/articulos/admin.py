from django.contrib import admin
from articulos.models import Articulo, Categoria


class ArticuloAdmin(admin.ModelAdmin):
	filter_horizontal = ("categoria",)
	prepopulated_fields = {"slug": ("titulo",)}


class CategoriaAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("nombre",)}
	

# Register your models here.
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria, CategoriaAdmin)