

from django.db import connection
from core.models import Curso

class GerenciadorBanco():

    def __init__(self):
        pass

    def select(self):

        cursor = connection.cursor()

        try:
            query = 'SELECT * FROM core_curso'

            # atribuir query
            cursor.execute(query)

            # retornar todos
            rows = cursor.fetchall()

            # lista inicial
            cursos = []

            # interar sobre todos as linhas
            for row in rows:

                # obtem cada coluna
                sigla = row[1]
                nome = row[2]
                tipo = row[3]
                carga_horaria = row[4]
                ativo = [5]

                # abre intancia do objeto e atribuir dados a suas propriedades
                curso = Curso()
                curso.nome = nome
                curso.tipo = tipo
                curso.sigla = nome
                curso.carga_horaria = carga_horaria
                curso.ativo = ativo

                # insere na lista
                cursos.append(curso)


        finally:

            # fechar conexao com o banco
            cursor.close()

        return cursos
