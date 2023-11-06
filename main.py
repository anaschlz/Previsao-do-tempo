import requests
import datetime

ufs_brasil = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MS", "MA", "MT",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
}


def get_weather_data(uf):
    key = "c77b469f"

    if uf in ufs_brasil:
        url = f"https://api.hgbrasil.com/weather?key={key}&city_name={uf}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'results' not in data:
                print(f"Erro: Não foi possível encontrar informações para o estado {uf}.")
                return

            weather = data['results']

            temperature = weather['temp']
            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            description = weather['description']
            condition = weather['condition_slug']
            humidity = weather['humidity']
            wind_speed = weather['wind_speedy']
            sunrise = weather['sunrise']
            sunset = weather['sunset']

            print("Previsão do tempo para", uf)
            print("Temperatura atual:", temperature, "ºC")
            print("Data e Hora da consulta:", current_time)
            print("Descrição do tempo atual:", description)
            print("Condição de tempo atual:", condition)
            print("Umidade:", humidity)
            print("Velocidade do vento:", wind_speed)
            print("Nascer do sol:", sunrise)
            print("Pôr do sol:", sunset)

            forecast = weather['forecast'][0]
            max_temp = forecast['max']
            min_temp = forecast['min']

            print("Médias das temperaturas máxima e mínima semanal:")
            print("Temperatura máxima:", max_temp)
            print("Temperatura mínima:", min_temp)
        else:
            print("Erro ao buscar os dados do tempo. Por favor, verifique se a UF está correta.")
    else:
        print(f"Erro: UF não encontrada na lista de estados do Brasil.")


while True:
    uf = input("Digite a UF para buscar a previsão do tempo: ").upper()
    get_weather_data(uf)
