from django.contrib import admin

# Register your models here.

from .models import Categoria
from .models import Comentario
from .models import Detalleespecie
from .models import DetalleespecieCategoria
from .models import Especie
from .models import EspecieComentario

admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Detalleespecie)
admin.site.register(DetalleespecieCategoria)
admin.site.register(Especie)
admin.site.register(EspecieComentario)
