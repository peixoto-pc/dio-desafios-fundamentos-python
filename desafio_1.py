PLANO_50 = "Plano Essencial Fibra - 50Mbps"
PLANO_100 = "Plano Prata Fibra - 100Mbps"
PLANO_300 = "Plano Premium Fibra - 300Mbps"

def recomendar_plano(consumo):
    plano_recomendado = ""
    if(consumo > 0 and consumo <= 10):
        plano_recomendado = PLANO_50
    
    elif(consumo > 10 and consumo <= 20):
        plano_recomendado = PLANO_100

    elif(consumo > 20):
        plano_recomendado = PLANO_300
    
    return plano_recomendado



#Solicita ao usuário que insira o consumo médio mensal de dados    
consumo = float(input("Por favor, informe o seu consumo médio mensal de internet: \n"))

if(consumo):
    print(recomendar_plano(consumo))

elif(consumo == 0):
    print("Parece que você não possui internet ainda!")