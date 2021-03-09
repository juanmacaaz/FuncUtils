# Autor Juan Manuel Camara Diaz
# Email: juanma.caaz@gmail.com

import time

def cost(**a):
    '''
    Calcula el coste de tiempo de la funcion
    Keyword Args:
        loops (int): numero de iteraciopnes que realizara el test
    '''
    if 'loops' not in a:
        a['loops'] = 10000

    def decorator(function):
        def wrapper(*args, **kwargs):
            loops = a['loops']
            timeCost = 0
            for _ in range(loops):
                s = time.time()
                out = function(*args, **kwargs)
                f = time.time()
                timeCost += (f-s)
            print(f'El timepo de ejecucion de {function.__name__} es de: {timeCost} segundos. En {loops} iteraciones.')
            return out
        return wrapper
    return decorator


if __name__ == '__main__':
    
    @cost()
    def mul(a):
        return (120937982*123123/324234)**2/a

    def testCases():
        print(mul(34))

    testCases()