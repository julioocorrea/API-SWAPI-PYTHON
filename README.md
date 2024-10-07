# Passo a Passo
 1. Certifique-se de que o Python 3.7 ou superior está instalado. Você pode verificar isso com o comando: python --version
    
 2. Certifique-se de que o MySQL está instalado e em execução.
 
 3. Criar Banco de Dados:Acesse o MySQL e crie o banco de dados chamado SWAPIPYTHON: "CREATE DATABASE SWAPIPYTHON;"
    
 4. Crie uma tabela favorites:

    USE SWAPIPYTHON;

    CREATE TABLE favorites (
        id INT AUTO_INCREMENT PRIMARY KEY,
        item_index INT NOT NULL,
        item_type VARCHAR(255) NOT NULL
    );


5. Instale as dependências necessárias com o pip: "pip install Flask flask-caching aiohttp mysql-connector-python"
   
6. A estrutura de pastas da sua aplicação deve ser assim:

/sua_aplicacao/
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
