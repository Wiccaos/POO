import requests
from Clases.Post import Post
import Auxiliares.Variables_fijas 

def leer_post_por_id(post_id):
    """Función para leer un post desde JSON Placeholder según el id"""
    try:
        ans = requests.get(f"{Auxiliares.Variables_fijas.URL_Post}/{post_id}")
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        post_data = ans.json()
        
        # Crear una instancia de Post y asignar los valores
        post = Post()
        post.userId = post_data['userId']
        post.id = post_data['id']
        post.title = post_data['title']
        post.body = post_data['body']
        
        return post
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El post no fue encontrado.")
    

def crear_post():
    """Función para crear un nuevo post en JSON Placeholder"""
    nuevo_post = Post()
    
    # Solicitar datos del usuario
    nuevo_post.title = input("Ingrese el título del post: ")
    nuevo_post.body = input("Ingrese el cuerpo del post: ")
    
    # Validar que el ID del usuario sea un número
    while True:
        user_id = input("Ingrese el id del usuario (número): ")
        if user_id.isdigit():
            nuevo_post.userId = int(user_id)
            break
        else:
            print("Por favor, ingrese un número válido para el ID del usuario.")
    
    try:
        # Realizar la solicitud POST
        ans = requests.post(Auxiliares.Variables_fijas.URL_Post, json=nuevo_post.__dict__)
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        
        # Crear una instancia de Post con la respuesta
        created_post_data = ans.json()
        nuevo_post.id = created_post_data['id']  # Asignar el ID del post creado
        return nuevo_post  # Retornar el post creado
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
