# rrhh.py

# Diccionario para guardar empleados. 
# La CLAVE será el ID del empleado, el VALOR sus datos.
empleados = {}

def crear_empleado(id_emp, nombre, puesto, salario):
    """Registra un nuevo empleado en el sistema"""
    if id_emp in empleados:
        print(f"⚠️ Error: El ID {id_emp} ya existe (pertenece a {empleados[id_emp]['nombre']}).")
        return False
    else:
        empleados[id_emp] = {
            "nombre": nombre,
            "puesto": puesto,
            "salario": salario
        }
        print(f"✅ {nombre} contratado/a como {puesto}.")
        return True

def ver_plantilla():
    """Muestra una tabla con todos los empleados"""
    if not empleados:
        print("📂 La empresa no tiene empleados registrados.")
        return

    print("\n--- PLANTILLA ACTUAL ---")
    print(f"{'ID':<5} {'NOMBRE':<20} {'PUESTO':<20} {'SALARIO ($)':<15}")
    print("-" * 65)
    for id_emp, datos in empleados.items():
        print(f"{id_emp:<5} {datos['nombre']:<20} {datos['puesto']:<20} {datos['salario']:<15}")
    print("-" * 65)

def calcular_nomina_total():
    """Suma todos los salarios para ver el gasto mensual"""
    total = 0
    cantidad_empleados = len(empleados)
    
    for datos in empleados.values():
        total += datos['salario']
        
    print(f"\n💰 DATOS FINANCIEROS:")
    print(f"Total empleados: {cantidad_empleados}")
    print(f"Gasto mensual en nóminas: ${total}")
    # Un toque extra: calcular promedio
    if cantidad_empleados > 0:
        promedio = total / cantidad_empleados
        print(f"Salario promedio: ${promedio:.2f}")

def despedir_empleado(id_emp):
    """Elimina un empleado del sistema"""
    if id_emp in empleados:
        nombre = empleados[id_emp]['nombre']
        del empleados[id_emp]
        print(f"❌ El empleado {nombre} (ID: {id_emp}) ha sido dado de baja.")
    else:
        print("⚠️ No se encontró ningún empleado con ese ID.")