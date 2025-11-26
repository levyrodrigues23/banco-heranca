class GerenciadorCursos:
    
    def __init__(self):
        self.cursos = []
    
    def adicionar_curso(self, curso: str):
        curso = curso.lower()
        
        if curso in self.cursos:
            print(f"O curso '{curso}' já está cadastrado neste campus.")
            return False
        
        self.cursos.append(curso)
        print(f"Curso '{curso}' adicionado com sucesso!")
        return True
    
    def remover_curso(self, curso: str):
        curso = curso.lower()
        
        if curso not in self.cursos:
            print("Esse curso não foi cadastrado neste campus!")
            return False
        
        self.cursos.remove(curso)
        print(f"O curso '{curso}' foi removido.")
        return True
    
    def atualizar_curso(self, curso: str, nome_atualizado: str):
        curso = curso.lower()
        nome_atualizado = nome_atualizado.lower()
        
        if curso not in self.cursos:
            print("O curso não foi cadastrado ainda.")
            return False
        
        indice = self.cursos.index(curso)
        self.cursos[indice] = nome_atualizado
        print(f"Curso '{curso}' atualizado para '{nome_atualizado}'.")
        return True
    
    def verificar_curso(self, curso: str):
        curso = curso.lower()
        return curso in self.cursos
    
    def listar_cursos(self):
        return self.cursos.copy()
    
    def quantidade_cursos(self):
        return len(self.cursos)