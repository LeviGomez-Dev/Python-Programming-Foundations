# main.py
import rrhh  # Importamos tu módulo de lógica

def iniciar_sistema():
    print("🏢 BIENVENIDO AL SISTEMA DE GESTIÓN DE PERSONAL (v1.0)")
    
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Contratar nuevo empleado")
        print("2. Ver toda la plantilla")
        print("3. Calcular gasto de nóminas (Reporte)")
        print("4. Despedir empleado")
        print("5. Salir")
        
        opcion = input(">> Elige una opción: ")

        if opcion == "1":
            # Pedimos los datos y nos aseguramos que el salario y ID sean números
            try:
                uid = int(input("ID del empleado (ej. 101): "))
                
                # --- VALIDACIÓN DE NOMBRE ---
                while True:
                    nom = input("Nombre: ").strip()
                    # 1. Quitamos espacios vacíos al principio/final (.strip)
                    # 2. Quitamos espacios intermedios (.replace) para verificar si es letra
                    if len(nom) > 1 and nom.replace(" ", "").isalpha():
                        break # ¡Es válido! Salimos del bucle
                    else:
                        print("⚠️ El nombre solo debe contener letras y no estar vacío.")

                # --- VALIDACIÓN DE PUESTO ---
                while True:
                    rol = input("Puesto (ej. Desarrollador): ").strip()
                    # Aquí permitimos letras y espacios. 
                    # Si quieres permitir números (ej: "Agente 007"), quita el .isalpha()
                    # y deja solo la validación de longitud len() > 1
                    if len(rol) > 1 and not rol.isdigit():
                        break
                    else:
                        print("⚠️ El puesto debe ser texto válido.")

                sal = float(input("Salario Mensual: "))
                
                # Llamamos a la función final
                rrhh.crear_empleado(uid, nom, rol, sal)

            except ValueError:
                print("⛔ Error: El ID y el Salario deben ser números.")

        elif opcion == "2":
            rrhh.ver_plantilla()

        elif opcion == "3":
            rrhh.calcular_nomina_total()

        elif opcion == "4":
            try:
                uid = int(input("ID del empleado a despedir: "))
                
                # Pedimos confirmación
                confirmacion = input(f"¿Seguro que quieres borrar al ID {uid}? (s/n): ")
                if confirmacion.lower() == 's':
                    rrhh.despedir_empleado(uid)
                elif confirmacion == 'n':
                    print("🚫 Operación cancelada. El empleado sigue en la empresa.")
                
                else:
                    # Aquí atrapamos el "ss", "x", "si", etc.
                    print("⚠️ Respuesta no válida (debe ser 's' o 'n'). Cancelado por seguridad.")

            except ValueError:
                print("⛔ Error: ID inválido.")

        elif opcion == "5":
            print("👋 Cerrando sesión. ¡Buen trabajo!")
            break
        
        else:
            print("Opción no reconocida.")

# Ejecutar programa
if __name__ == "__main__":
    iniciar_sistema()