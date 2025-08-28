alunos = []

def gerar_matricula(curso):
    sigla = curso.strip().upper()
    return f"{sigla}{sum(a['curso'] == sigla for a in alunos) + 1}"

def cadastrar_aluno():
    nome = input("Digite o nome do(a) aluno(a): ")
    email = input("Digite o e-mail do(a) aluno(a): ")
    curso = input("Digite o curso do(a) aluno(a) (use a sigla, ex: GES): ").strip().upper()

    matricula = gerar_matricula(curso)
    alunos.append({"nome": nome, "email": email, "curso": curso, "matricula": matricula})
    print(f"Aluno(a) {nome} cadastrado(a) com sucesso! Matrícula: {matricula}")

def listar_alunos():
    if not alunos:
        print("Nenhum(a) aluno(a) cadastrado(a).")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}, Matrícula: {aluno['matricula']}")

def atualizar_aluno():
    nome = input("Digite o nome do(a) aluno(a) a ser atualizado(a): ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            novo_email = input("Digite o novo e-mail (ou deixe em branco para manter): ").strip()
            novo_curso = input("Digite o novo curso (sigla) (ou deixe em branco para manter): ").strip().upper()

            if novo_email:
                aluno["email"] = novo_email
            if novo_curso:
                if novo_curso != aluno["curso"]:
                    aluno["curso"] = novo_curso
                    aluno["matricula"] = gerar_matricula(novo_curso)

            print("Aluno(a) atualizado(a) com sucesso!")
            return
    print("Aluno(a) não encontrado(a).")

def remover_aluno():
    nome = input("Digite o nome do(a) aluno(a) a ser removido(a): ")
    idx = next((i for i, a in enumerate(alunos) if a["nome"] == nome), None)
    if idx is not None:
        alunos.pop(idx)
        print("Aluno(a) removido(a) com sucesso!")
    else:
        print("Aluno(a) não encontrado(a).")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Aluno(a)")
        print("2. Listar Alunos(as)")
        print("3. Atualizar Aluno(a)")
        print("4. Remover Aluno(a)")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
