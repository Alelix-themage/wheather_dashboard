import streamlit as st
import requests
from API import API
import pandas as pd

def weather_informations(data):
    '''Extrai e retorna a temperatura a partir dos dados do clima.'''
    temp = data['main']['temp']
    icon = data['weather'][0]['icon']
    return temp, icon


def more_informations(data):
    umidade = data['main']['humidity']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressao = data['main']['pressure']
    visibilidade = data['visibility']
    pais = data['sys']['country']
    
    st.text("Informações adicionais:")
    st.code("Umidade: " + str(umidade))
    st.code("Temperatura Mínima: " + str(temp_min))
    st.code("Temperatura Máxima: " + str(temp_max))
    st.code("Pressão: " + str(pressao))
    st.code("Visibilidade: " + str(visibilidade) )
    st.code("País: "+ pais)


st.title('Dashboard de Temperaturas')
st.code('print("Welcome, this is my dashboard!")')

# Input de cidade
city = st.text_input("Digite o nome da cidade:", "São Paulo")


url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

# Fazendo a requisição HTTP para a API
response = requests.get(url)


# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    print('\n')
    print(data)
    
    
    # Usando a função para obter a temperatura e o ícone
    temperature, icon = weather_informations(data)
    
   
    
    # Mostrando a temperatura com um ícone
    st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
    st.metric(label="Temperatura Atual", value=f"{temperature}°C")
   
    #função de informações adicionais
    more_info = more_informations(data)
       
else:
    st.write("Essa cidade não existe".format(response.status_code))


