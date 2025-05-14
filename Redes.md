Aqui está um exemplo visual de como seria um pacote de dados em uma rede, usando a linguagem Markdown para ilustrar as camadas desde a aplicação até a camada física:

# Exemplo de Pacote Completo de Dados em uma Rede

O pacote de dados percorre as camadas do modelo OSI antes de ser enviado pela rede. Abaixo está o fluxo de como as informações são empacotadas em cada camada.

## 1. Camada de Aplicação (Application Layer)
- **Dados**: A informação gerada pela aplicação (como uma requisição HTTP, e-mail, etc).

Exemplo de dados: "GET /index.html HTTP/1.1"


## 2. Camada de Transporte (Transport Layer)
- **Protocolo**: TCP/UDP (se for TCP, inclui informações de controle como número de sequência, controle de fluxo).

Cabeçalho TCP: \[Número de Sequência: 12345] \[Número de Confirmação: 67890] \[Porta de Origem: 5000] \[Porta de Destino: 80]
Dados: "GET /index.html HTTP/1.1"


## 3. Camada de Rede (Network Layer)
- **Protocolo**: IP (Endereços IP de origem e destino, fragmentação).

Cabeçalho IP: \[Endereço IP de Origem: 192.168.1.1] \[Endereço IP de Destino: 203.0.113.5] \[Tipo de Protocolo: TCP]
Dados: "GET /index.html HTTP/1.1"


## 4. Camada de Enlace de Dados (Data Link Layer)
- **Protocolo**: Ethernet, PPP (endereços MAC, controle de erro e sincronização de dados).

Cabeçalho Ethernet: \[Endereço MAC de Origem: 00:14:22:01:23:45] \[Endereço MAC de Destino: 00:14:22:67:89\:AB] \[Tipo: IP]
Dados: "GET /index.html HTTP/1.1"

## 5. Camada Física (Physical Layer)
- **Transmissão**: O pacote de dados é convertido em sinais elétricos, ópticos ou rádio para ser enviado pela rede.
- **Exemplo**: sinais elétricos enviados através de um cabo Ethernet ou ondas de rádio para uma conexão sem fio.
- Representação Física: 

  Sinal elétrico/óptico/radiofrequência: "0101010100110110"

### Fluxo Completo:
1. **Aplicação**: "GET /index.html HTTP/1.1"
2. **Transporte**: Cabeçalho TCP + Dados
3. **Rede**: Cabeçalho IP + Dados
4. **Enlace de Dados**: Cabeçalho Ethernet + Dados
5. **Física**: Sinal elétrico/rádio

Cada camada acrescenta suas próprias informações ao pacote, encapsulando os dados originais e garantindo que possam ser enviados e recebidos de maneira eficiente e sem erros pela rede.

Esse exemplo demonstra o processo de encapsulamento dos dados em cada camada de rede, desde a camada de aplicação até a transmissão física.

## Tabela representativa do modelo OSI:

| **Camada OSI**  | **Número** | **Função Principal**                         | **Nome da PDU** | **Informações Adicionadas (Encapsulamento)**      |
| --------------- | ---------- | -------------------------------------------- | --------------- | ------------------------------------------------- |
| Aplicação       | 7          | Interface com o usuário e geração dos dados  | Dados           | Nenhuma                                           |
| Apresentação    | 6          | Codificação, compressão, criptografia        | Dados           | Pode aplicar formatação ou criptografia           |
| Sessão          | 5          | Controle de sessão (início, fim, manutenção) | Dados           | Controle de sessão                                |
| Transporte      | 4          | Segmentação e controle de fluxo (TCP/UDP)    | Segmento        | Portas de origem e destino                        |
| Rede            | 3          | Roteamento e endereçamento lógico (IP)       | Pacote          | Endereços IP de origem e destino                  |
| Enlace de Dados | 2          | Endereçamento físico (MAC), acesso ao meio   | Quadro (Frame)  | Endereços MAC + Detecção de erro (FCS)            |
| Física          | 1          | Transmissão de bits no meio físico           | Bits            | Conversão para sinais (elétricos, ópticos, rádio) |
