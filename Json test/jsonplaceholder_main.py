import Servicios.ConsumirAPI

def menu():
    """Menú interactivo para utilizar las funciones"""
    while True:
        print("""
Menú de Jsonplaceholder
1. Consultar Post
2. Crear Post
3. Salir
""")
        try: option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
        
        if option == 1:
            post_id = int(input("Ingrese el ID del post que desea leer: "))
            post = Servicios.ConsumirAPI.leer_post_por_id(post_id)
            if post:
                print(f"Post ID: {post.id}\nTítulo: {post.title}\nCuerpo: {post.body}")
            
        elif option == 2:    
            Servicios.ConsumirAPI.crear_post()
        elif option == 3:
            print("Saliendo del programa")
            break

#Ejecuar menú
menu()
