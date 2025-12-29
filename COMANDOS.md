### Comandos Gerais

|Comando|Descrição|
|  ---  |   ---   |
|```git remote add origin [URL]```|Linka o repositório do GitHub ao repositório local
|```git clone [URL]```|Clona o repertório da URL 
|```git clone [URL] --branch [branch] --single-branch```|Clona somente a branch **[branch]**
|```git add .```|Adiciona todas as mudanças à área de preparação
|```git commit -m [descrição]```|Cria um commit com o nome **[descrição]**
|```git restore [arquivo/repositório]```|Restaura o arquivo ou repositório para a versão da área de preparação
|```git commit --amend -m [nova_descrição]```|Renomeia o último commit
|```git reset [nome]```|Remove o arquivo/repositório **[nome]** da área de preparação
|```git push -u origin main```|Manda o último commit para o repositório remoto
|```git pull```|"Puxa" o último commit do repositório remoto para o repositório local


### Comandos úteis para trabalhar com branches

|Comando|Descrição|
|---|---|
|```git checkout -b [branch]```|"Desloga" da branch atual e cria uma nova branch com o nome [branch]
|```git checkout [branch]```|Troca para a branch **[branch]**
|```git branch```|Lista todas as branchs existentes no repositório
|```git merge [branch]```|Mescla a branch **[branch]** à branch **main**
|```git branch -d [branch]```|Deleta a branch **[branch]**


### Comandos de Configuração

|Comando|Descrição|
|  ---  |   ---   |
|```git config --global credential.helper store```|Armazena o token de validação permanentemente
|```git config --global credential.helper cache```|Armazena o token de validação temporariamente
|```git config --global user.name```|Altera o nome do usuário
|```git config --global user.email```|Altera o e-mail do usuário
