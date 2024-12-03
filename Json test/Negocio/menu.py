import Servicios.ConsumirAPI

def menu():
    """Menú interactivo para utilizar las funciones"""
    while True:
        print(""" 
Menú de JSONplaceholder
1. Consultar Post
2. Crear Post
3. Salir
""")
        try: 
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            continue  # Volver al inicio del bucle
        
        if option == 1:
            post_id = int(input("Ingrese el ID del post que desea leer: "))
            post = Servicios.ConsumirAPI.leer_post_por_id(post_id)
            if post:
                print(f"\nPost ID: {post.id}\nUserID: {post.userId}\nTítulo: {post.title}\nCuerpo: {post.body}")
            
        elif option == 2:    
            created_post = Servicios.ConsumirAPI.crear_post()
            if created_post:
                print(f"\nPost creado exitosamente: \nUser ID: {created_post.userId}\nPost ID: {created_post.id}\nTítulo: {created_post.title}\nCuerpo: {created_post.body}")
        
        elif option == 3:
            print("Saliendo del programa...")
            break