import requests
from Clases.Post import Post

URL_Post = "https://jsonplaceholder.typicode.com/posts"
URL_Todo = "https://jsonplaceholder.typicode.com/todos"


def consultar_api_post():
    posts = [Post()]
    ans = requests.get(URL_Post)
    ans.raise_for_status()

    try:
        if ans.status_code == 200:
            for post in ans.json():
                nuevo_post = Post()
                nuevo_post.id = post['id']
                nuevo_post.title = post['title']
                nuevo_post.body = post['body']
                posts.append(nuevo_post)
            print(posts)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def crear_post():
    nuevo_post = Post()
    nuevo_post.title = input("Ingrese el título del post: ")
    nuevo_post.body = input("Ingrese el cuerpo del post: ")
    nuevo_post.userId = input("Ingrese el id del usuario: ")
    nuevo_post.id = input("Ingrese el id del post: ")
    nuevo_post.completed = input("Ingrese el estado del post: ")
    print(nuevo_post.__dict__)
    ans = requests.post(URL_Post, json=nuevo_post.__dict__)
    ans.raise_for_status()
    print(ans.json())

    