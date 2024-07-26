# Projeto de Ponto Eletrônico

Este é um projeto desenvolvido em Python utilizando o framework FastAPI e o banco de dados SQLite. O objetivo é criar um sistema de ponto eletrônico que possa ser embarcado em um Raspberry Pi e utilize um sensor RFID para identificação dos usuários.

## Funcionalidades

- Registro de entrada e saída dos usuários através do sensor RFID
- Armazenamento dos registros no banco de dados SQLite

## Configuração

1. Clone o repositório para o seu Raspberry Pi
2. Instale as dependências necessárias executando o comando `pip install -r requirements.txt`
3. Configure o banco de dados SQLite
4. Conecte o sensor RFID ao Raspberry Pi
5. Execute o aplicativo utilizando o comando `python main.py`