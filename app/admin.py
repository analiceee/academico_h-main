from django.contrib import admin
from .models import *

# Inline de disciplinas na área do saber
class DisciplinaInline(admin.TabularInline):
    model = Disciplinas
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [DisciplinaInline]

# Não precisa fazer unregister
admin.site.register(AreaSaber, AreaSaberAdmin)

# Outros registros
admin.site.register(Cidade)
admin.site.register(Instituicao)
admin.site.register(Ocupacao)
admin.site.register(Pessoas)
admin.site.register(Cursos)
admin.site.register(PeriodoCurso)
admin.site.register(Disciplinas)
admin.site.register(Matricula)
admin.site.register(Avaliacoes)
admin.site.register(Frequencia)
admin.site.register(Turmas)
admin.site.register(Ocorrencias)
admin.site.register(DiciplinaCurso)
admin.site.register(TipoAvaliacao)
