def div(func):
    def wrapper(*args, **kwargs):
        print('<div>', end='')
        print(func(*args, **kwargs), end='')
        print('</div>')
    return wrapper


def article(func):
    def wrapper(*args, **kwargs):
        print('<article>', end='')
        print(func(*args, **kwargs), end='')
        print('</article>')
    return wrapper    


def p(func):
    def wrapper(*args, **kwargs):
        print('<p>', end='')
        print(func(*args, **kwargs), end='')
        print('</p>')
    return wrapper  


# Here you must apply the decorators, uncomment this later
@div
def saludo1(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'

@article    
def saludo2(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'

@p
def saludo3(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    saludo1('Jorge')
    saludo2('Jorge')
    saludo3('Jorge')

if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
