Desafio Técnico - Sistema de Gestão
-----------------------------------------------------------------------------------------------------------
Este repositório contém a solução para um desafio técnico de desenvolvimento de sistemas. O projeto consiste em um script Python que simula um sistema de gestão com três funcionalidades principais: cálculo de comissões, controle de estoque e calculadora de juros.
-----------------------------------------------------------------------------------------------------------
Funcionalidades

O sistema é executado via terminal e oferece um menu interativo com as seguintes opções:

Relatório de Comissões:

Processa uma lista de vendas (JSON).

Calcula a comissão de cada vendedor baseada em regras de negócio (1% para vendas < R$500, 5% para vendas >= R$500).

Exibe o total a receber por vendedor.

-----------------------------------------------------------------------------------------------------------
Controle de Estoque:

Exibe o saldo atual dos produtos.

Permite lançar movimentações de Entrada ou Saída.

Gera um ID único para cada transação e atualiza o saldo em tempo real (na memória).

-----------------------------------------------------------------------------------------------------------
Calculadora de Juros:

Calcula juros simples de 2.5% ao dia para boletos vencidos.

Recebe valor e data de vencimento, retornando o valor corrigido e os dias de atraso.

-----------------------------------------------------------------------------------------------------------
Como Executar

Pré-requisitos

Python 3.14 instalado.

-----------------------------------------------------------------------------------------------------------
Passo a passo

Clone este repositório:

git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)


Acesse a pasta do projeto:

cd NOME-DO-REPO


Execute o script:

python desafio.py


-----------------------------------------------------------------------------------------------------------
Tecnologias Utilizadas

Python 3

Biblioteca json (para manipulação de dados)

Biblioteca datetime (para cálculos de datas)

Biblioteca uuid (para geração de IDs únicos)

Estrutura do Código

O código foi estruturado em uma classe única SistemaDesafio para manter o estado da aplicação durante a execução, simulando um banco de dados em memória através das variáveis JSON_VENDAS e JSON_ESTOQUE.

Desenvolvido como parte de um teste técnico para vaga de Desenvolvimento de Sistemas Jr.


