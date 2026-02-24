nome_cliente = input("Olá viajante! Seja bem-vindo(a) a Taverna do Dragão Banguelo! Informe o seu nome para continuarmos: ")
idade_cliente = int(input("Perfeito! Agora nos informe a sua idade: "))
acompanhado_por_adulto = input("Você está acompanhado por um adulto? Responda com 'Sim' ou 'Não': ").strip().lower() 
entrada_permitida = (idade_cliente >= 18) or (idade_cliente >= 16 and acompanhado_por_adulto == "sim")

if entrada_permitida:
    print(f"É um prazer recebê-lo(a) em nossa taverna {nome_cliente}! Aproveite a noite!")
else:
    print(f"Sentimos muito, {nome_cliente}, porém você ainda não tem idade para frequentar o nosso estabelecimento. Volte em alguns anos!")