def moda(datos):

    frecuencias = {}
    
    # Contar la frecuencia de cada elemento
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1
    
    # Encontrar la frecuencia máxima
    max_frecuencia = max(frecuencias.values())
    
    # Obtener los valores con la frecuencia máxima
    modas = [key for key, value in frecuencias.items() if value == max_frecuencia]
    
    return modas

def prom(x):
    return sum(x)/len(x)

def mediana(datos):
    # Ordenar los datos
    datos_ordenados = sorted(datos)
    
    n = len(datos_ordenados)
    
    if n % 2 != 0:
        mediana = datos_ordenados[n // 2]
    else:
        mediana = (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2
    
    return mediana
    
def mad(data):

    def mediana(data):
        data = sorted(data)
        i = len(data) // 2
        if len(data) % 2 == 0:
            return (data[i] + data[i-1]) / 2
        else:
            return data[i]

    med = mediana(data)
    deviations = sorted(abs(xi - med) for xi in data)
    return mediana(deviations)
    
    
def std(datos, ddof=0):
    media = sum(datos)/len(datos)
    cuadrados = sum((x- media)**2 for x in datos)
    
    varianza = cuadrados/(len(datos)-ddof)
    
    return varianza**(1/2)

def cuartil(datos, pos):
    datos_ordenados = sorted(datos)
    posicion = int(len(datos_ordenados)*pos)

    if posicion >= len(datos_ordenados):
        posicion = len(datos_ordenados) - 1

    # Obtener el valor en esa posición
    valor = datos_ordenados[posicion]
    
    return valor

def cof_re(x, y):
    # Verificar que las listas tengan la misma longitud
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")
    
    # Calcular las medias de x y y
    media_x = sum(x) / len(x)
    media_y = sum(y) / len(y)
    
    # Calcular las sumas de productos de las desviaciones de cada variable
    suma_producto = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
    
    # Calcular las sumas de los cuadrados de las desviaciones de cada variable
    suma_cuadrado_x = sum((xi - media_x) ** 2 for xi in x)
    suma_cuadrado_y = sum((yi - media_y) ** 2 for yi in y)
    
    # Calcular el coeficiente de correlación
    r = suma_producto / ( (suma_cuadrado_x * suma_cuadrado_y) ** 0.5 )
    
    return r
