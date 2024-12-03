class Todo:
    """Clase de lista de cosas por hacer 'To Do's'"""
    def __init__(self, userId = 0, Id= 0, title = '', completed = True):
        self.userId = userId
        self.Id = Id
        self.title = title
        self.completed = completed
