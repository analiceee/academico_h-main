from django.contrib import admin
from .models import *

# Inlines
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Cursos
    extra = 1

class DisciplinaCursoInline(admin.TabularInline):
    model = DiciplinaCurso
    extra = 1

class DisciplinaInline(admin.TabularInline):
    model = Disciplinas
    extra = 1

# Admins
@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    inlines = [PessoaInline]

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'site', 'telefone', 'cidade']
    search_fields = ['nome']
    inlines = [CursoInline]

@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'area_saber', 'instituicao']
    search_fields = ['nome']
    list_filter = ['area_saber', 'instituicao']
    inlines = [DisciplinaCursoInline]

@admin.register(Disciplinas)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'area_saber']
    search_fields = ['nome']
    list_filter = ['area_saber']

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'cidade', 'ocupacao']
    search_fields = ['nome', 'cpf']
    list_filter = ['cidade', 'ocupacao']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'instituicao', 'data_inicio', 'data_prev_termino']
    search_fields = ['pessoa__nome', 'curso__nome']
    list_filter = ['curso', 'instituicao']

@admin.register(Avaliacoes)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'curso', 'disciplina']
    search_fields = ['descricao']
    list_filter = ['curso', 'disciplina']

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'disciplina', 'numero_faltas']
    search_fields = ['pessoa__nome']
    list_filter = ['curso', 'disciplina']

@admin.register(Turmas)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'periodo']
    search_fields = ['nome']
    list_filter = ['periodo']

@admin.register(Ocorrencias)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'data', 'pessoa', 'curso', 'disciplina']
    search_fields = ['descricao']
    list_filter = ['curso', 'disciplina', 'data']

@admin.register(DiciplinaCurso)
class DisciplinaCursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'carga_horaria', 'periodo', 'curso']
    search_fields = ['nome']
    list_filter = ['curso', 'periodo']

@admin.register(TipoAvaliacao)
class TipoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

# Registros diretos
admin.site.register(Cidade)
admin.site.register(AreaSaber)
admin.site.register(PeriodoCurso)
