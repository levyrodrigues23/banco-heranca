from cursos import GerenciadorCursos

class CampusLista:
    
    
    def __init__(self):
        self.campus = {}
        
        fortaleza = GerenciadorCursos()
        fortaleza.cursos = [
            "administração (diurno)",
            "administração (noturno)",
            "agronomia",
            "arquitetura e urbanismo",
            "biotecnologia",
            "ciência da computação",
            "ciência de dados",
            "ciências biológicas (licenciatura)",
            "estatística",
            "física",
            "geografia",
            "geologia",
            "matemática (bacharelado)",
            "matemática (licenciatura)",
            "química (licenciatura)",
            "química (bacharelado)",
            "economia ecológica",
            "engenharia de alimentos",
            "engenharia de pesca",
            "gestão de políticas públicas",
            "zootecnia",
            "biblioteconomia",
            "ciências sociais",
            "história",
            "letras – português",
            "letras – inglês",
            "letras – espanhol",
            "letras – português e francês",
            "letras – português e italiano",
            "psicologia",
            "engenharia ambiental e sanitária",
            "engenharia civil",
            "engenharia de computação",
            "engenharia de energias renováveis",
            "engenharia de telecomunicações",
            "ciências contábeis",
            "ciências econômicas",
            "finanças",
            "secretariado executivo",
            "enfermagem",
            "farmácia",
            "odontologia",
            "cinema e audiovisual",
            "publicidade e propaganda",
            "dança",
            "design",
            "design – moda",
            "filosofia",
            "jornalismo",
            "música",
            "teatro",
            "educação física",
            "sistemas e mídias digitais",
            "ciências ambientais",
            "oceanografia"
        ]
        
        crateus = GerenciadorCursos()
        crateus.cursos = [
            "ciência da computação",
            "engenharia ambiental e sanitária",
            "engenharia civil",
            "engenharia de minas",
            "sistemas de informação"
        ]
        
        itapaje = GerenciadorCursos()
        itapaje.cursos = [
            "análise e desenvolvimento de sistemas",
            "ciência de dados",
            "segurança da informação"
        ]
        
        quixada = GerenciadorCursos()
        quixada.cursos = [
            "ciência da computação",
            "design digital",
            "engenharia de computação",
            "engenharia de software",
            "redes de computadores",
            "sistemas de informação"
        ]
        
        russas = GerenciadorCursos()
        russas.cursos = [
            "ciência da computação",
            "engenharia civil",
            "engenharia de produção",
            "engenharia de software",
            "engenharia mecânica"
        ]
        
        sobral = GerenciadorCursos()
        sobral.cursos = [
            "ciências econômicas",
            "engenharia de computação",
            "engenharia elétrica",
            "finanças",
            "medicina",
            "música",
            "odontologia",
            "psicologia"
        ]
        
        self.campus["fortaleza"] = fortaleza
        self.campus["crateús"] = crateus
        self.campus["itapajé"] = itapaje
        self.campus["quixadá"] = quixada
        self.campus["russas"] = russas
        self.campus["sobral"] = sobral
    
    def cadastrar_campus(self, nome_campus: str):
        nome_campus = nome_campus.lower()
        
        if nome_campus in self.campus:
            print(f"O campus '{nome_campus}' já está cadastrado.\n")
            return False
        
        self.campus[nome_campus] = GerenciadorCursos()
        print(f"O campus '{nome_campus}' foi adicionado.\n")
        self._mostrar_campus()
        return True
    
    def cadastrar_curso_campus(self, nome_campus: str, curso_novo: str):
        nome_campus = nome_campus.lower()
        
        if nome_campus not in self.campus:
            print("Esse campus não foi cadastrado ainda.")
            return False
        
        resultado = self.campus[nome_campus].adicionar_curso(curso_novo)
        self._mostrar_campus()
        return resultado
    
    def verificar_os_campus(self):
        if not self.campus:
            print("Nenhum campus foi cadastrado ainda.")
            return
        
        print("\n" + "="*70)
        print(" CAMPUS DA UFC ".center(70))
        print("="*70)
        
        for i, (nome, gerenciador) in enumerate(self.campus.items()):
            cursos = gerenciador.listar_cursos()
            quantidade = gerenciador.quantidade_cursos()
            
            print(f"\n{i+1}. Campus: {nome.title()}")
            print(f"   Quantidade de Cursos: {quantidade}")
            
            if cursos:
                cursos_formatados = [curso.title() for curso in cursos]
                print(f"   Cursos: {', '.join(cursos_formatados)}")
            else:
                print(f"   Cursos: (nenhum)")
        
        print("\n" + "="*70 + "\n")
    
    def remover_campus(self, nome_campus: str):
        nome_campus = nome_campus.lower()
        
        if nome_campus not in self.campus:
            print("Esse campus não foi cadastrado ainda.")
            return False
        
        gerenciador_removido = self.campus.pop(nome_campus)
        cursos = gerenciador_removido.listar_cursos()
        
        print(f"O campus '{nome_campus}' foi removido.")
        print(f"Cursos que estavam nele: {cursos if cursos else '(nenhum)'}")
        self._mostrar_campus()
        return True
    
    def remover_curso_campus(self, nome_curso: str, nome_campus: str):
        nome_campus = nome_campus.lower()
        
        if nome_campus not in self.campus:
            print("Esse campus não foi cadastrado ainda.")
            return False
        
        resultado = self.campus[nome_campus].remover_curso(nome_curso)
        
        if resultado:
            print(f"Curso removido do campus '{nome_campus}'.")
        
        return resultado
    
    def atualizar_campus(self, campus_antigo: str, novo_nome_campus: str):
        campus_antigo = campus_antigo.lower()
        novo_nome_campus = novo_nome_campus.lower()
        
        if campus_antigo not in self.campus:
            print("Esse campus não foi cadastrado ainda.")
            return False
        
        self.campus[novo_nome_campus] = self.campus.pop(campus_antigo)
        print(f"Campus '{campus_antigo}' atualizado para '{novo_nome_campus}'.")
        return True
    
    def atualizar_curso_campus(self, curso: str, nome_campus: str, novo_nome_curso: str):
        nome_campus = nome_campus.lower()
        
        if nome_campus not in self.campus:
            print("Esse campus não foi cadastrado ainda.")
            return False
        
        resultado = self.campus[nome_campus].atualizar_curso(curso, novo_nome_curso)
        
        if resultado:
            print(f"Curso atualizado no campus '{nome_campus}'.")
        
        return resultado
    
    def _mostrar_campus(self):
        estrutura = {}
        for nome, gerenciador in self.campus.items():
            estrutura[nome] = gerenciador.listar_cursos()
        print(estrutura)