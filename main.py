from campus_lista import CampusLista

def menu(ufc: CampusLista):
    
    while True:
        print("\n" + "="*40)
        print(" --CAMPUS UFC-- ".center(40))
        print("="*40)
        print("1 - Cadastrar Campus")
        print("2 - Cadastrar Curso em Campus")
        print("3 - Verificar os Campus e Cursos")
        print("4 - Remover Campus")
        print("5 - Remover Curso de Campus")
        print("6 - Atualizar Campus")
        print("7 - Atualizar Curso de Campus")
        print("0 - Sair")
        print("="*40)
    
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "0":
            print("\nObrigado por usar o sistema! Tenha um bom dia.")
            break
        
        elif opcao == "1":
            nome_campus = input("\nDigite o nome do campus: ").strip()
            ufc.cadastrar_campus(nome_campus)
        
        elif opcao == "2":
            nome_campus = input("\nDigite o nome do campus: ").strip()
            curso_novo = input("Digite o nome do curso: ").strip()
            ufc.cadastrar_curso_campus(nome_campus, curso_novo)
        
        elif opcao == "3":
            ufc.verificar_os_campus()
        
        elif opcao == "4":
            nome_campus = input("\nDigite o nome do campus a remover: ").strip()
            ufc.remover_campus(nome_campus)
        
        elif opcao == "5":
            nome_campus = input("\nDigite o nome do campus: ").strip()
            nome_curso = input("Digite o nome do curso a remover: ").strip()
            ufc.remover_curso_campus(nome_curso, nome_campus)
        
        elif opcao == "6":
            nome_campus = input("\nDigite o nome do campus atual: ").strip()
            novo_nome = input("Digite o novo nome do campus: ").strip()
            ufc.atualizar_campus(nome_campus, novo_nome)
        
        elif opcao == "7":
            nome_campus = input("\nDigite o nome do campus: ").strip()
            nome_curso = input("Digite o nome do curso atual: ").strip()
            novo_nome = input("Digite o novo nome do curso: ").strip()
            ufc.atualizar_curso_campus(nome_curso, nome_campus, novo_nome)
        
        else:
            print("\nSinto muito, mas tente novamente porque essa opcao é inválida.")


def main():
    print("\n" + "="*50)
    print(" BEM-VINDO AO SISTEMA DE GERENCIAMENTO DA UFC ".center(50))
    print("="*50 + "\n")
    
    ufc = CampusLista()
    menu(ufc)  # Passa o objeto para o menu


if __name__ == "__main__":
    main()


