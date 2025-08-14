def ingresar_calificaciones():
    """
    Guarda las materias juntos a las calificaciones pasadas por el usuario.
    
    Returns:
        tupla: Devuelve una tupla con dos listas:
            · Lista1: Nombre de las materias.
            · Lista2: Puntuación de las materias.
    """
    
    # Listas donde se guardarán los inputs pasados por el usuario
    nombre_materias = []
    puntuacion_materias = []
    
    while True:
        # Pregunta inicial para comprobar si el usuario desea añadir o no materias. En caso negativo se sale del programa.
        continuar = input("¿Desea ingresar una materia? (si/no): ").lower()
        if continuar != "si":
            print("Finalizando el ingreso de materias...")
            break
        
        # Ingreso del nombre de la materia
        materia = input("Ingrese el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue
        # Flujo en el que el usuario desea añadir una materia que ya ha sido ingresada
        elif materia in nombre_materias:
            decision_modificar_nota = input(f"La materia \"{materia}\" ya ha sido añadida. ¿Quiere modificar su nota? (si/no): ").lower()
            if decision_modificar_nota != "si":
                continue
            else:
                # Modificación de la nota de la materia ya ingresada
                modificar_nota(nombre_materias, puntuacion_materias, materia)
                continue
        # Ingreso de la nota de una materia no ingresada  anteriormente
        else:                  
            try:
                calificacion = float(input("Ingrese la calificación (0-10): "))
                if 0 <= calificacion <= 10:
                    nombre_materias.append(materia)
                    puntuacion_materias.append(calificacion)
                else:
                    print("La calificación debe estar entre 0 y 10.")
                    continue
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

    # Retorno de ambas listas generadas
    return nombre_materias, puntuacion_materias


def modificar_nota(nombre_materias, puntuacion_materias, materia):
    """
    Modifica la nota de una materia ya registrada anteriormente.
    
    Args:
        nombre_materias (lista): Lista con los nombres de todas las materias ingresadas por el usuario
        puntuacion_materias (lista): Lista con las calificaciones de todas las materias ingresadas por el usuario
        materia (string): materia que se requiere moficiar su puntuación
    """
    
    # Modificación de la nota de la materia ya ingresada
    try:
        calificacion = float(input("Ingrese la calificación (0-10): "))
        if 0 <= calificacion <= 10:
            indice_materia = nombre_materias.index(materia)
            puntuacion_materias[indice_materia] = calificacion
            print(f"Calificacion de la materia \"{materia}\" modificada con éxito")
        else:
            print("La calificación debe estar entre 0 y 10.")
    except ValueError:
        print("Debe ingresar un número válido.")  


def calcular_promedio(calificaciones):
    """
    Guarda las materias juntos a las calificaciones pasadas por el usuario.
    
    Args:
        calificaciones (lista): Lista con todas las clasificaciones ingresadas por el usuario
    
    Returns:
        promedio: promedio de todas las clasificaciones del input calificaciones
    """
    
    # Validación de datos en la lista
    if not calificaciones:
        return
    
    # Suma de todas las clasificaciones
    suma_total = 0.0
    
    # Calculo del promedio
    for calificacion in calificaciones:
        suma_total = suma_total + calificacion
        
    promedio = suma_total/len(calificaciones)
    
    # Retorno del promedio
    return promedio


def determinar_estado(calificaciones, umbral):
    """
    Determina las califacaciones que han sido aprobadas y devuelve dos listas con los indices de las materias aprobadas y otra con los índices de las reprobadas.
    
    Args:
        calificaciones (lista): Lista con todas las clasificaciones ingresadas por el usuario
        umbral: Nota que determinar si una materia esta aprobada. Por defecto es 5.0
    
    Returns:
        tupla: Devuelve una tupla con dos listas:
            · Lista1: Contiene los indices de las materias aprobadas.
            · Lista2: Contiene los indices de las materias suspendidas.
    """
    
    # Bloque para modificar el umbral por defecto de 5.0 en caso de que el usuario lo requiera
    preguntar_umbral = input("¿Desea utilizar el umbral de clasificacion de materias aprobadas por defecto? (si/no): ").lower()
    if preguntar_umbral != "si":
        try:
            respuesta_umbral = float(input("Ingrese el nuevo umbral a utilizar (0.1-10): "))
            if 0.1 <= respuesta_umbral <= 10:
                umbral = respuesta_umbral
            else:
                print("El umbral debe estar entre 0.1 y 10.")
        except ValueError:
            print("Debe ingresar un número válido.")
    
    # Listas donde se guardarán los indices de las masterias aprobadas y suspendidas
    indices_aprobadas = []
    indices_suspendidas = []
    
    # Bloque de añadido de los indices a las listas
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            indices_aprobadas.append(i)
        else:
            indices_suspendidas.append(i)
    
    # Retorno de ambas listas
    return indices_aprobadas, indices_suspendidas


def encontrar_extremos(calificaciones):
    """
    Determina las califacaciones con puntuación más alta y más baja.
    
    Args:
        calificaciones (lista): Lista con todas las clasificaciones ingresadas por el usuario
    
    Returns:
        tupla: Devuelve una tupla con dos float:
            · Float1: Calificación más alta.
            · Float2: Calificación más baja.
    """
    
    # Retorno de las dos clasificaciones
    return calificaciones.index(max(calificaciones)), calificaciones.index(min(calificaciones))

    
def main():
    """
    Función principal en la que producen las llamadas para obtener los datos que serán mostrados por pantalla.
    """
    
    # Ingreso de calificaciones por parte del usuario
    materias, calificaciones = ingresar_calificaciones()
    
    if not materias:
        print ("No se añadió ninguna materia. Saliendo del programa...")
        return
    
    # Llamada a las funciones para obtener distintos outputs
    promedio = calcular_promedio(calificaciones) 
    indices_aprobadas, indices_suspendidas = determinar_estado(calificaciones, 5.0)
    indice_nota_alta, indice_nota_baja = encontrar_extremos(calificaciones)

    # Printeo de datos
    print("\n--- Resumen ---")
    print("\nListado de materias")
    for materia, nota in zip(materias, calificaciones):
        print(f"{materia}: {nota}")

    print(f"\nPromedio general: {promedio}")
    print("\nMaterias aprobadas:", [materias[i] for i in indices_aprobadas])
    print("Materias reprobadas:", [materias[i] for i in indices_suspendidas])
    print(f"\nMejor materia: {materias[indice_nota_alta]} ({calificaciones[indice_nota_alta]})")
    print(f"Peor materia: {materias[ indice_nota_baja]} ({calificaciones[ indice_nota_baja]})")


if __name__ == "__main__": 
    main()