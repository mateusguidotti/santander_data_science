livros = [
    ["percy jackson e o ladrão de raios", "rick riordan", 512],
    ["vinte mil léguas submarinas", "júlio verne", 321]
]
def mostrar_livros(livros):
    if len(livros) == 0:
        print("Nenhum livro no momento!")
        return
    
    for livro in livros:
        titulo = livro[0].title()
        autor = livro[1].title()
        paginas = livro[2]

        print(f"======== Livro {livros.index(livro)+1} ========")
        print(f"Título: {titulo}\nAutor: {autor}\nPáginas: {paginas}\n")
    return

def inserir_livros(livros):
    titulo = input("Insira o nome do livro: ").lower()

    if verifica_duplicados(titulo, livros):
        print("O livro já existe!")
    else:
        autor = input("Insira o autor do livro: ").lower()
        paginas = int(input("Insira o número de páginas do livro: "))
        livros.append([titulo, autor, paginas])
        print("Livro adicionado com sucesso!")
        
    return livros

def procurar_livro(livros):
    titulo = input("Insira o nome do livro que procura: ").lower()

    for livro in livros:
        if livro[0] == titulo:
            indice = livros.index(livro)
            mostrar_livros(livros[indice:indice+1])
            return

    print("Não achei!")

def procurar_autor(livros):
    autor = input("Insira o nome do autor: ").lower()
    livros_autor = []

    for livro in livros:
        if livro[1] == autor:
            livros_autor.append(livro)
    
    if(len(livros_autor) == 0):
        print("Nenhum livro encontrado!\n")
        return
    else:
        print("")
        mostrar_livros(livros_autor)
        return

def verifica_duplicados(titulo, livros):
    for livro in livros:
        if livro[0] == titulo:
            return livro
    return False

def deletar_livro(livros):
    titulo = input("Insira o nome do livro que deseja deletar: ").lower()
    livro_existe = verifica_duplicados(titulo, livros)

    if(livro_existe):
        livros.remove(livro_existe)
        print("Livro deletado com sucesso!")
    else:
        print(f"O livro {titulo} não encontrado!")

    return livros
        

def editar_livro(livros):
    titulo = input("Insira o nome do livro que deseja editar: ").lower()
    livro_existe = verifica_duplicados(titulo, livros)

    if(livro_existe):
        indice = livros.index(livro_existe)
        livros[indice][0] = input("Digite o novo nome do livro: ")
        livros[indice][1] = input("Digite o novo autor do livro: ")
        livros[indice][2] = int(input("Digite o novo número de páginas do livro: "))
        print("\nAlteração realizada com sucesso!\n")
    else:
        print("Livro não encontrado!")
    
    return livros

def menu(qtd_opcoes) :
    print("""
    ========== MENU ==========
            
    1 - Inserir Livro
    2 - Listar Livros
    3 - Procurar Livro
    4 - Procurar Livros De Um Autor
    5 - Deletar Livro
    6 - Editar Livro
    7 - Sair
            
    ==========================
    """)

    while(True):
        escolha = int(input("Insira a opção desejada: "))

        if(escolha <= 0 or escolha > qtd_opcoes):
            print("Escolha inválida\n")
        else:
            print("")
            return escolha

# função principal

while True:
    escolha = menu(7)

    match escolha:
        case 1:
            livros = inserir_livros(livros)
        case 2:
            mostrar_livros(livros)
        case 3:
            procurar_livro(livros)
        case 4:
            procurar_autor(livros)
        case 5:
            livros = deletar_livro(livros)
        case 6:
            livros = editar_livro(livros)
        case 7:
            print("Saindo...")
            break