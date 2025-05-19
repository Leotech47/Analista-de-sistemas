# Criar o arquivo .sh com o conteúdo do script
script_content = """#!/bin/bash

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
"""

file_path = "/mnt/data/organizar_relatorios.sh"
with open(file_path, "w") as file:
    file.write(script_content)

file_path
