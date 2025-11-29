import json
from datetime import datetime
import uuid
import os

# Dados iniciais (Simulando banco de dados)
JSON_VENDAS = '''
{
 "vendas": [
 { "vendedor": "João Silva", "valor": 1200.50 },
 { "vendedor": "João Silva", "valor": 950.75 },
 { "vendedor": "João Silva", "valor": 1800.00 },
 { "vendedor": "João Silva", "valor": 1400.30 },
 { "vendedor": "João Silva", "valor": 1100.90 },
 { "vendedor": "João Silva", "valor": 1550.00 },
 { "vendedor": "João Silva", "valor": 1700.80 },
 { "vendedor": "João Silva", "valor": 250.30 },
 { "vendedor": "João Silva", "valor": 480.75 },
 { "vendedor": "João Silva", "valor": 320.40 },
 { "vendedor": "Maria Souza", "valor": 2100.40 },
 { "vendedor": "Maria Souza", "valor": 1350.60 },
 { "vendedor": "Maria Souza", "valor": 950.20 },
 { "vendedor": "Maria Souza", "valor": 1600.75 },
 { "vendedor": "Maria Souza", "valor": 1750.00 },
 { "vendedor": "Maria Souza", "valor": 1450.90 },
 { "vendedor": "Maria Souza", "valor": 400.50 },
 { "vendedor": "Maria Souza", "valor": 180.20 },
 { "vendedor": "Maria Souza", "valor": 90.75 },
 { "vendedor": "Carlos Oliveira", "valor": 800.50 },
 { "vendedor": "Carlos Oliveira", "valor": 1200.00 },
 { "vendedor": "Carlos Oliveira", "valor": 1950.30 },
 { "vendedor": "Carlos Oliveira", "valor": 1750.80 },
 { "vendedor": "Carlos Oliveira", "valor": 1300.60 },
 { "vendedor": "Carlos Oliveira", "valor": 300.40 },
 { "vendedor": "Carlos Oliveira", "valor": 500.00 },
 { "vendedor": "Carlos Oliveira", "valor": 125.75 },
 { "vendedor": "Ana Lima", "valor": 1000.00 },
 { "vendedor": "Ana Lima", "valor": 1100.50 },
 { "vendedor": "Ana Lima", "valor": 1250.75 },
 { "vendedor": "Ana Lima", "valor": 1400.20 },
 { "vendedor": "Ana Lima", "valor": 1550.90 },
 { "vendedor": "Ana Lima", "valor": 1650.00 },
 { "vendedor": "Ana Lima", "valor": 75.30 },
 { "vendedor": "Ana Lima", "valor": 420.90 },
 { "vendedor": "Ana Lima", "valor": 315.40 }
 ]
}
'''

JSON_ESTOQUE = '''
{
"estoque":
[
 { "codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150 },
 { "codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75 },
 { "codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200 },
 { "codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320 },
 { "codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90 }
]
}
'''

# ==============================================================================
# LÓGICA DO SISTEMA
# ==============================================================================

class SistemaDesafio:
    def __init__(self):
        self.estoque_data = json.loads(JSON_ESTOQUE)
        self.vendas_data = json.loads(JSON_VENDAS)

    def desafio_1_comissoes(self):
        print("\n--- RELATÓRIO DE COMISSÕES ---")
        resumo_vendedores = {}

        for venda in self.vendas_data['vendas']:
            vendedor = venda['vendedor']
            valor = venda['valor']
            comissao = 0

            if valor >= 500:
                comissao = valor * 0.05
            elif valor >= 100:
                comissao = valor * 0.01
            
            if vendedor not in resumo_vendedores:
                resumo_vendedores[vendedor] = 0
            resumo_vendedores[vendedor] += comissao

        for nome, total in resumo_vendedores.items():
            print(f"Vendedor: {nome:<20} | Total Comissão: R$ {total:.2f}")
        input("\nPressione Enter para voltar...")

    def desafio_2_estoque(self):
        while True:
            print("\n--- CONTROLE DE ESTOQUE ---")
            print(f"{'CÓD':<5} | {'PRODUTO':<30} | {'QTD':<5}")
            print("-" * 45)
            for p in self.estoque_data['estoque']:
                print(f"{p['codigoProduto']:<5} | {p['descricaoProduto']:<30} | {p['estoque']:<5}")
            
            print("\n[1] Movimentar Estoque")
            print("[0] Voltar ao Menu Principal")
            opcao = input("Escolha: ")

            if opcao == '0':
                break
            elif opcao == '1':
                try:
                    cod = int(input("Digite o Código do Produto: "))
                    produto = next((p for p in self.estoque_data['estoque'] if p['codigoProduto'] == cod), None)
                    
                    if not produto:
                        print(">> ERRO: Produto não encontrado!")
                        continue

                    tipo = input("Tipo (E para Entrada / S para Saída): ").upper()
                    qtd = int(input("Quantidade: "))
                    desc = input("Descrição da movimentação: ")

                    if tipo == 'S':
                        qtd = qtd * -1 # Transforma em negativo

                    # Atualiza
                    produto['estoque'] += qtd
                    id_mov = str(uuid.uuid4())[:8]
                    
                    print(f"\n>> SUCESSO! Movimentação {id_mov} registrada.")
                    print(f"Produto: {produto['descricaoProduto']}")
                    print(f"Novo Saldo: {produto['estoque']}")
                    input("Enter para continuar...")

                except ValueError:
                    print(">> ERRO: Digite apenas números para código e quantidade.")
            else:
                print("Opção inválida.")

    def desafio_3_juros(self):
        print("\n--- CÁLCULO DE JUROS ---")
        try:
            valor = float(input("Digite o valor do boleto (ex: 1000.50): "))
            data_str = input("Digite a data de vencimento (DD/MM/AAAA): ")
            
            data_vencimento = datetime.strptime(data_str, "%d/%m/%Y")
            hoje = datetime.now()
            
            diferenca = hoje - data_vencimento
            dias_atraso = diferenca.days

            if dias_atraso <= 0:
                print(f"\n>> Boleto em dia! Nenhum juros a cobrar.")
            else:
                taxa_diaria = 0.025 # 2.5%
                valor_juros = valor * (taxa_diaria * dias_atraso)
                valor_total = valor + valor_juros

                print(f"\n>> RESULTADO DO CÁLCULO:")
                print(f"Dias de atraso: {dias_atraso}")
                print(f"Juros totais (2.5% a.d): R$ {valor_juros:.2f}")
                print(f"Valor Final Atualizado:  R$ {valor_total:.2f}")
            
        except ValueError:
            print(">> ERRO: Formato de data ou valor inválido.")
        
        input("\nPressione Enter para voltar...")

    def menu_principal(self):
        while True:
            # Limpa tela (opcional, funciona melhor em terminal local)
            print("\n" + "="*30)
            print(" SISTEMA DE GESTÃO - TESTE TÉCNICO")
            print("="*30)
            print("1. Relatório de Comissões")
            print("2. Controle de Estoque")
            print("3. Calculadora de Juros")
            print("0. Sair")
            
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.desafio_1_comissoes()
            elif opcao == '2':
                self.desafio_2_estoque()
            elif opcao == '3':
                self.desafio_3_juros()
            elif opcao == '0':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = SistemaDesafio()
    app.menu_principal()