cris = 'eeeee'

def calculadora():
    """
    Calculadora básica que recibe dos números y permite seleccionar
    entre sumar, restar, multiplicar o dividir
    """
    print("=== CALCULADORA BÁSICA ===")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        try:
            # Solicitar los dos números
            num1 = float(input("\nIngrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            # Mostrar opciones de operación
            print("\nSeleccione la operación:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            
            opcion = input("Ingrese su opción (1-5): ")
            
            if opcion == "1":
                resultado = num1 + num2
                print(f"\n{num1} + {num2} = {resultado}")
                
            elif opcion == "2":
                resultado = num1 - num2
                print(f"\n{num1} - {num2} = {resultado}")
                
            elif opcion == "3":
                resultado = num1 * num2
                print(f"\n{num1} × {num2} = {resultado}")
                
            elif opcion == "4":
                if num2 == 0:
                    print("\nError: No se puede dividir por cero")
                else:
                    resultado = num1 / num2
                    print(f"\n{num1} ÷ {num2} = {resultado}")
                    
            elif opcion == "5":
                print("\n¡Gracias por usar la calculadora!")
                break
                
            else:
                print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")
                
        except ValueError:
            print("\nError: Por favor, ingrese números válidos.")
        except Exception as e:
            print(f"\nError inesperado: {e}")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            print("\n¡Gracias por usar la calculadora de Ctorres!")
            break

#if __name__ == "__main__":
 #
calculadora()