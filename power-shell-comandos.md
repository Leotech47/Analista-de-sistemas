# 📘 Resumo de Comandos do PowerShell (CLI)

| **Comando**                 | **Descrição**                                                                 |
|----------------------------|------------------------------------------------------------------------------|
| `Get-Help`                 | Exibe ajuda sobre comandos (`Get-Help Get-Process`)                          |
| `Get-Command`              | Lista todos os comandos disponíveis                                          |
| `Get-Process`              | Mostra os processos em execução                                              |
| `Stop-Process -Name nome`  | Encerra um processo específico                                               |
| `Get-Service`              | Lista todos os serviços do sistema                                           |
| `Start-Service nome`       | Inicia um serviço                                                            |
| `Stop-Service nome`        | Para um serviço                                                              |
| `Set-ExecutionPolicy`      | Define política de execução de scripts (ex: `RemoteSigned`)                 |
| `Get-ChildItem` (`ls`)     | Lista arquivos e diretórios                                                  |
| `Set-Location` (`cd`)      | Altera o diretório atual                                                     |
| `Copy-Item` (`cp`)         | Copia arquivos ou pastas                                                     |
| `Move-Item` (`mv`)         | Move ou renomeia arquivos/pastas                                             |
| `Remove-Item` (`rm`)       | Exclui arquivos ou pastas                                                    |
| `New-Item`                 | Cria um novo arquivo ou diretório                                            |
| `Clear-Host` (`cls`)       | Limpa a tela                                                                 |
| `Get-Content` (`cat`, `type`) | Exibe o conteúdo de um arquivo                                              |
| `Out-File`                 | Redireciona saída para um arquivo (`comando \| Out-File arquivo.txt`)        |
| `Get-History`              | Mostra o histórico de comandos                                               |
| `Start-Job`, `Get-Job`     | Executa tarefas em segundo plano                                            |
| `Import-Module`            | Carrega módulos adicionais no ambiente                                       |



Abaixo está um **exemplo prático em PowerShell**, simulando um fluxo de trabalho real, com comentários e comandos explicados, em **formato Markdown**:

````markdown
# 🛠️ Exemplo Prático: Gerenciamento de Arquivos e Processos com PowerShell

## 🎯 Objetivo:
Criar diretórios, manipular arquivos, visualizar processos e salvar saídas em um relatório.

---

## 🔧 Passo a Passo com Comandos PowerShell

### 1. Criar uma nova pasta de trabalho
```powershell
New-Item -Path "C:\Relatorios" -ItemType Directory
Set-Location "C:\Relatorios"
````

### 2. Criar arquivos de texto

```powershell
New-Item -Name "relatorio1.txt" -ItemType File
New-Item -Name "relatorio2.txt" -ItemType File
```

### 3. Adicionar conteúdo a um arquivo

```powershell
"Relatório de atividades - Maio 2025" | Out-File relatorio1.txt
Get-Content relatorio1.txt
```

### 4. Copiar e renomear arquivos

```powershell
Copy-Item relatorio1.txt relatorio_backup.txt
Rename-Item relatorio2.txt relatorio_final.txt
```

### 5. Verificar processos ativos e salvar em arquivo

```powershell
Get-Process | Out-File processos.txt
```

### 6. Filtrar serviços em execução

```powershell
Get-Service | Where-Object {$_.Status -eq "Running"}
```

### 7. Parar e iniciar um serviço (Exemplo: Spooler de impressão)

```powershell
Stop-Service -Name Spooler
Start-Service -Name Spooler
```

### 8. Exibir histórico de comandos

```powershell
Get-History
```

### 9. Limpar a tela

```powershell
Clear-Host
```

---

## ⌨️ Dicas de uso com PowerShell

| **Ação**                             | **Comando / Tecla**         |
| ------------------------------------ | --------------------------- |
| Buscar ajuda de um comando           | `Get-Help NomeDoComando`    |
| Listar todos os comandos             | `Get-Command`               |
| Executar comandos como administrador | Abrir PowerShell como Admin |
| Visualizar histórico                 | `Get-History`               |
| Autocompletar                        | `Tab`                       |
| Cancelar execução                    | `Ctrl + C`                  |
| Limpar tela                          | `Clear-Host`                |

---

## ✅ Resultado Final:

* Diretório `C:\Relatorios` com 3 arquivos manipulados
* Processos salvos em `processos.txt`
* Serviços gerenciados com segurança
* Histórico acessível para revisão

```

