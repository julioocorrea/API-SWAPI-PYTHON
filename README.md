# Resumo da Aplicação
Esta aplicação é um sistema web construído com Flask que permite aos usuários explorar dados do universo Star Wars. Os usuários podem visualizar informações sobre personagens, filmes, naves, veículos, espécies e planetas, além de adicionar itens a uma lista de favoritos, que é armazenada em um banco de dados MySQL. A aplicação utiliza caching para melhorar o desempenho, reduzindo a carga nas requisições repetidas.

# Tecnologias Utilizadas
Flask: Um framework web em Python que facilita o desenvolvimento de aplicações web.
Flask-Caching: Extensão para Flask que fornece suporte ao cache, melhorando a eficiência da aplicação.
aiohttp: Biblioteca para realizar requisições HTTP assíncronas, permitindo a busca eficiente de dados da API Star Wars.
asyncio: Módulo para programação assíncrona em Python, utilizado para gerenciar chamadas assíncronas.
mysql-connector-python: Biblioteca para conectar e interagir com bancos de dados MySQL.
HTML/CSS: Para criar as interfaces de usuário e renderizar as páginas web.

# Passo a Passo para ultilizar o sistema:
 1. Certifique-se de que o Python 3.7 ou superior está instalado. Você pode verificar isso com o comando: python --version
    
 2. Certifique-se de que o MySQL está instalado e em execução.
 
 3. Criar Banco de Dados:Acesse o MySQL e crie o banco de dados chamado SWAPIPYTHON: "CREATE DATABASE SWAPIPYTHON;"
    
 4. Crie uma tabela favorites:

Código:

    USE SWAPIPYTHON;

    CREATE TABLE favorites (
        id INT AUTO_INCREMENT PRIMARY KEY,
        item_index INT NOT NULL,
        item_type VARCHAR(255) NOT NULL
    );


6. Instale as dependências necessárias com o pip:

Dependencias:

    pip install Flask
    pip install Flask-Caching
    pip install aiohttp
    pip install mysql-connector-python
   
8. A estrutura de pastas da sua aplicação deve ser assim:

Estrutura:

    app.py 
    /templates/
        home.html
        characters.html
        character_detail.html
        films.html
        film_detail.html
        starships.html
        starship_detail.html
        vehicles.html
        vehicle_detail.html
        species.html
        species_detail.html
        planets.html
        planet_detail.html
        favorites.html
    /static/
        /imagens/
            fundo.png
        /videos/
            videoAbertura.mp4
            

7. Rodar a Aplicação: "python app.py"
   
8. A aplicação deve estar rodando em http://127.0.0.1:5000/. Você pode acessar essa URL no seu navegador.
