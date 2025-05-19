# 📘 Resumo de Comandos do Bash (CLI)

## 🔹 Comandos básicos

| **Comando**                | **Descrição**                                                                 |
|---------------------------|------------------------------------------------------------------------------|
| `ls`                      | Lista arquivos e diretórios                                                   |
| `cd`                      | Altera o diretório atual (`cd /home/user`)                                   |
| `pwd`                     | Mostra o caminho do diretório atual                                           |
| `mkdir nome`              | Cria um novo diretório                                                        |
| `touch nome.txt`          | Cria um novo arquivo vazio                                                    |
| `cp origem destino`       | Copia arquivos ou diretórios                                                  |
| `mv origem destino`       | Move ou renomeia arquivos ou diretórios                                       |
| `rm arquivo`              | Remove arquivos                                                               |
| `rm -r pasta`             | Remove diretórios e seu conteúdo                                              |
| `cat arquivo`             | Exibe o conteúdo de um arquivo                                                |
| `less arquivo`            | Visualiza o conteúdo de arquivos paginados                                    |
| `echo "texto"`            | Imprime uma mensagem na tela                                                  |
| `man comando`             | Mostra o manual de uso de um comando                                          |
| `history`                 | Lista o histórico de comandos                                                 |
| `clear`                   | Limpa a tela do terminal                                                      |
| `sudo comando`            | Executa comando com permissões de superusuário                               |
| `chmod`                   | Altera permissões de arquivos e diretórios                                    |
| `chown`                   | Altera o dono de arquivos e diretórios                                        |
| `ps`                      | Mostra processos em execução                                                  |
| `kill PID`                | Encerra um processo com o ID informado                                        |
| `top` / `htop`            | Monitora processos em tempo real                                              |
| `df -h`                   | Mostra uso de espaço em disco                                                 |
| `du -sh pasta/`           | Mostra tamanho de uma pasta                                                   |
| `grep "termo" arquivo`    | Busca por padrões de texto em arquivos                                        |
| `find . -name "*.txt"`    | Busca arquivos por nome                                                       |
| `tar -czf arq.tar.gz pasta/` | Compacta uma pasta em tar.gz                                              |
| `unzip arq.zip`           | Descompacta arquivos `.zip`                                                   |
| `curl URL` / `wget URL`   | Faz download de arquivos pela internet                                        |

---

## ⌨️ Atalhos de Teclado no Bash

| **Atalho**        | **Função**                                                   |
|-------------------|---------------------------------------------------------------|
| `Ctrl + A`        | Vai para o início da linha                                    |
| `Ctrl + E`        | Vai para o final da linha                                     |
| `Ctrl + U`        | Apaga do cursor até o início da linha                         |
| `Ctrl + K`        | Apaga do cursor até o final da linha                          |
| `Ctrl + W`        | Apaga a palavra anterior                                      |
| `Ctrl + L`        | Limpa a tela (como `clear`)                                   |
| `Ctrl + C`        | Interrompe o comando atual                                    |
| `Ctrl + D`        | Encerra o terminal (se a linha estiver vazia)                |
| `Ctrl + R`        | Busca reversa no histórico de comandos                        |
| `↑ / ↓`           | Navega pelos comandos anteriores/seguintes                    |
| `Tab`             | Autocompleta comandos ou nomes de arquivos                    |
| `!!`              | Repete o último comando executado                             |
| `!palavra`        | Executa o último comando que começa com "palavra"             |

---
