
| **Camada OSI**  | **Número** | **Função Principal**                         | **Nome da PDU** | **Informações Adicionadas (Encapsulamento)**      |
| --------------- | ---------- | -------------------------------------------- | --------------- | ------------------------------------------------- |
| Aplicação       | 7          | Interface com o usuário e geração dos dados  | Dados           | Nenhuma                                           |
| Apresentação    | 6          | Codificação, compressão, criptografia        | Dados           | Pode aplicar formatação ou criptografia           |
| Sessão          | 5          | Controle de sessão (início, fim, manutenção) | Dados           | Controle de sessão                                |
| Transporte      | 4          | Segmentação e controle de fluxo (TCP/UDP)    | Segmento        | Portas de origem e destino                        |
| Rede            | 3          | Roteamento e endereçamento lógico (IP)       | Pacote          | Endereços IP de origem e destino                  |
| Enlace de Dados | 2          | Endereçamento físico (MAC), acesso ao meio   | Quadro (Frame)  | Endereços MAC + Detecção de erro (FCS)            |
| Física          | 1          | Transmissão de bits no meio físico           | Bits            | Conversão para sinais (elétricos, ópticos, rádio) |
| --------------- | ---------- | -------------------------------------------- | --------------- | ------------------------------------------------- |
