from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_caching import Cache
import aiohttp
import asyncio
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Função para criar a conexão com o MySQL
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         # Seu nome de usuário
            password='123456',   # Sua senha
            database='TESTEFABIANO'  # Nome do seu banco de dados
        )
        print("Conexão com o MySQL bem-sucedida")
    except Error as e:
        print(f"Erro '{e}' ocorreu")
    return connection

SWAPI_BASE_URLS = {
    'people': 'https://swapi.dev/api/people/',
    'films': 'https://swapi.dev/api/films/',
    'starships': 'https://swapi.dev/api/starships/',
}

async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            raise ValueError(f"Erro ao acessar {url}: {response.status}")
        return await response.json()

async def fetch_all_data(session, urls):
    tasks = [fetch_data(session, url) for url in urls]
    return await asyncio.gather(*tasks)

async def get_character_data(session, character_index):
    data = await fetch_all_data(session, [SWAPI_BASE_URLS['people']])
    characters = data[0]['results']
    if character_index < 1 or character_index > len(characters):
        return None, 'Character not found'
    
    character_data = characters[character_index - 1]
    species_names = []

    for species_url in character_data.get('species', []):
        species_data = await fetch_data(session, species_url)
        species_names.append(species_data.get('name', 'não identificado'))

    character_data['species'] = ', '.join(species_names) if species_names else 'não identificado'
    return character_data, None

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.route('/characters', methods=['GET'])
@cache.cached(timeout=120)  # Cache por 120 segundos
async def get_characters():
    async with aiohttp.ClientSession() as session:
        data = await fetch_all_data(session, [SWAPI_BASE_URLS['people']])
        characters = data[0]['results']
        return render_template('characters.html', characters=characters)

@app.route('/characters/<int:character_index>', methods=['GET'])
async def get_character(character_index):
    async with aiohttp.ClientSession() as session:
        character_data, error = await get_character_data(session, character_index)
        if error:
            return jsonify({'error': error}), 404
        return render_template('character_detail.html', character=character_data, character_index=character_index)


@app.route('/films', methods=['GET'])
@cache.cached(timeout=120)  # Cache por 120 segundos
async def get_films():
    async with aiohttp.ClientSession() as session:
        data = await fetch_all_data(session, [SWAPI_BASE_URLS['films']])
        return render_template('films.html', films=data[0]['results'])

@app.route('/films/<int:film_index>', methods=['GET'])
@cache.cached(timeout=60)  # Cache por 60 segundos
async def get_film(film_index):
    async with aiohttp.ClientSession() as session:
        data = await fetch_all_data(session, [SWAPI_BASE_URLS['films']])
        films = data[0]['results']

        if film_index < 1 or film_index > len(films):
            return jsonify({'error': 'Film not found'}), 404

        film_data = films[film_index - 1]
        character_urls = film_data['characters']
        all_urls = character_urls
        all_data = await fetch_all_data(session, all_urls)

        characters = all_data[:len(character_urls)]
        
        # Passar o índice do filme para o template
        return render_template('film_detail.html', film=film_data, characters=characters, film_index=film_index)

if __name__ == '__main__':
    app.run(debug=True)
