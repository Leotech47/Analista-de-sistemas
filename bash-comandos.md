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


Aqui está um **exemplo prático** usando os comandos e atalhos do Bash apresentados, em **formato Markdown**, simulando um fluxo de trabalho real em terminal Linux:

````markdown
# 🛠️ Exemplo Prático: Gerenciamento de Diretório e Arquivos com Bash

## 🎯 Objetivo:
Organizar arquivos de relatórios, compactá-los e enviá-los para um servidor remoto.

---

## 🔧 Passo a Passo com Comandos Bash

### 1. Acessar o terminal e navegar até o diretório de trabalho:
```bash
cd ~/Documentos/relatorios
pwd
````

### 2. Criar uma nova pasta para armazenar os relatórios do mês:

```bash
mkdir relatorios_maio
cd relatorios_maio
```

### 3. Criar arquivos de relatório vazios:

```bash
touch relatorio1.txt relatorio2.txt relatorio3.txt
ls
```

### 4. Preencher um arquivo com conteúdo de exemplo:

```bash
echo "Relatório de vendas - Maio 2025" > relatorio1.txt
cat relatorio1.txt
```

### 5. Copiar os arquivos para backup:

```bash
cp relatorio*.txt ../backup/
```

### 6. Renomear um relatório:

```bash
mv relatorio2.txt relatorio_final.txt
```

### 7. Exibir o conteúdo de um arquivo de forma paginada:

```bash
less relatorio_final.txt
```

### 8. Buscar por uma palavra no arquivo:

```bash
grep "vendas" relatorio1.txt
```

### 9. Verificar o espaço ocupado pelos arquivos:

```bash
du -sh .
```

### 10. Compactar os relatórios:

```bash
cd ..
tar -czf relatorios_maio.tar.gz relatorios_maio/
ls -lh relatorios_maio.tar.gz
```

### 11. Enviar para servidor (exemplo com `scp`):

```bash
scp relatorios_maio.tar.gz usuario@servidor:/home/usuario/relatorios/
```

---

## ⌨️ Utilização de Atalhos no Processo

| **Ação**                                | **Atalho**               |
| --------------------------------------- | ------------------------ |
| Voltar ao início da linha para corrigir | `Ctrl + A`               |
| Ir ao fim para adicionar algo           | `Ctrl + E`               |
| Cancelar um comando digitado por engano | `Ctrl + C`               |
| Limpar a tela                           | `Ctrl + L`               |
| Buscar um comando anterior (ex: `scp`)  | `Ctrl + R`, digite `scp` |
| Repetir o último comando executado      | `!!`                     |
| Apagar até o início da linha            | `Ctrl + U`               |
| Autocompletar nomes de arquivos         | `Tab`                    |

---

## 🧹 Limpeza final (opcional)

```bash
rm -r relatorios_maio
rm relatorios_maio.tar.gz
```

---

## ✅ Resultado

* Relatórios organizados e compactados
* Arquivos enviados com segurança
* Histórico de comandos disponível com `history`

```

Se quiser, posso gerar este exemplo em **PDF**, **HTML**, ou como script `.sh` executável. Deseja algum desses formatos?
```
Aqui está o conteúdo anterior convertido em um **script `.sh` executável**. Esse script automatiza o processo descrito no exemplo:

```bash
#!/bin/bash

# Script: organizar_relatorios.sh
# Descrição: Organiza relatórios do mês, compacta e envia para servidor remoto
# Autor: Seu Nome
# Data: $(date +"%d/%m/%Y")

echo "📁 Acessando diretório de trabalho..."
cd ~/Documentos/relatorios || exit
pwd

echo "📁 Criando pasta para relatórios de maio..."
mkdir -p relatorios_maio
cd relatorios_maio || exit

echo "📄 Criando arquivos de relatório..."
touch relatorio1.txt relatorio2.txt relatorio3.txt
echo "Relatório de vendas - Maio 2025" > relatorio1.txt

echo "🗂️ Fazendo backup dos arquivos..."
mkdir -p ../backup
cp relatorio*.txt ../backup/

echo "✏️ Renomeando arquivo..."
mv relatorio2.txt relatorio_final.txt

echo "🔍 Buscando palavra 'vendas' no relatorio1.txt"
grep "vendas" relatorio1.txt

echo "📦 Compactando relatórios..."
cd ..
tar -czf relatorios_maio.tar.gz relatorios_maio/

echo "📤 Enviando para servidor remoto..."
# Substitua os dados abaixo com os seus dados reais
# Exemplo: scp relatorios_maio.tar.gz usuario@192.168.0.100:/home/usuario/relatorios/
scp relatorios_maio.tar.gz usuario@servidor:/home/usuario/relatorios/

echo "✅ Processo concluído com sucesso!"
```

### 🔧 Instruções para uso:

1. **Salvar o script**:
   Salve o conteúdo acima em um arquivo chamado, por exemplo: `organizar_relatorios.sh`

2. **Tornar executável**:
   No terminal, execute:

   ```bash
   chmod +x organizar_relatorios.sh
   ```

3. **Executar o script**:

   ```bash
   ./organizar_relatorios.sh
   ```

⚠️ **Importante**: Edite a linha do `scp` com os dados do seu servidor remoto antes de executar.

Se quiser, posso gerar esse script em arquivo `.sh` para download. Deseja isso?
