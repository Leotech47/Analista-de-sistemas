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
