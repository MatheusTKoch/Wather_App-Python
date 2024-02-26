# Weather App

## Descrição

O Weather App é uma aplicação Python que fornece informações sobre o clima atual com base no nome da cidade. Ele também pode aceitar códigos de estado e códigos de país opcionalmente, caso necessário. A aplicação utiliza a API do Open Weather para obter os dados meteorológicos.

## Requisitos

- Python 3.x
- Módulo os
- Módulo dotenv
- Módulo requests

## Instalação

1.Clone este repositório para o seu computador:

```bash
git clone https://github.com/seu-usuario/weather-app.git
```

2.Navegue até o diretório do projeto:

```bash
cd weather-app
```

3.Instale as dependências usando o pip:

```bash
pip install -r requirements.txt
```

4.Crie um arquivo .env na raiz do projeto e adicione sua chave de API do Open Weather:

API_KEY='SuaChaveDeAPIAqui'

## Uso

Execute o aplicativo usando o Python:

```bash
python weather_app.py
```

O aplicativo solicitará que você insira o nome da cidade, o código do estado (opcional) e o código do país (opcional). Em seguida, ele retornará informações sobre o clima atual para a cidade especificada.