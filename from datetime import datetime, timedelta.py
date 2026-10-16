from datetime import datetime, timedelta
import random

# ==========================================
# ESTRUCTURAS DE DATOS INICIALES
# ==========================================

inventario = [
    {"nombre": "Carne de Res", "categoria": "Carne", "cantidad": 12, "unidad": "kg", "caducidad": "2026-10-25"},
    {"nombre": "Pechuga de Pollo", "categoria": "Carne", "cantidad": 4, "unidad": "kg", "caducidad": "2026-10-17"},
    {"nombre": "Lechuga", "categoria": "Verdura", "cantidad": 2, "unidad": "unidades", "caducidad": "2026-10-16"},
    {"nombre": "Tomate", "categoria": "Verdura", "cantidad": 8, "unidad": "kg", "caducidad": "2026-10-22"},
    {"nombre": "Crema de Aji Artesanal", "categoria": "Crema", "cantidad": 3, "unidad": "frascos", "caducidad": "2026-10-18"},
    {"nombre": "Mayonesa Casera", "categoria": "Crema", "cantidad": 1, "unidad": "frascos", "caducidad": "2026-10-16"}
]

platos = [
    {"nombre": "Sopa Crema de Verduras", "tipo": "entrada"},
    {"nombre": "Papa a la Huancaina", "tipo": "entrada"},
    {"nombre": "Causa Limena", "tipo": "entrada"},
    {"nombre": "Lomo Saltado", "tipo": "principal"},
    {"nombre": "Seco de Res con Frijoles", "tipo": "principal"},
    {"nombre": "Pollo a la Plancha con Verduras", "tipo": "principal"}
]

# ==========================================
# FUNCIONES DEL SISTEMA
# ==========================================

def mostrar_alertas():
    print("\n" + "="*40)
    print("ALERTAS DEL ALMACEN")
    print("="*40)
    
    hoy = datetime.now().date()
    limite_vencimiento = hoy + timedelta(days=3)
    
    print("\nProductos con Stock Bajo (< 5 unidades/kg):")
    stock_bajo = [p for p in inventario if p["cantidad"] < 5]
    if stock_bajo:
        for p in stock_bajo:
            print(f" - {p['nombre']} ({p['categoria']}): Solo quedan {p['cantidad']} {p['unidad']}")
    else:
        print(" No hay productos con stock bajo.")

    print("\nProximos a Vencer (o vencidos):")
    vencimiento_cercano = False
    for p in inventario:
        try:
            fecha_cad = datetime.strptime(p["caducidad"], "%Y-%m-%d").date()
            if fecha_cad <= limite_vencimiento:
                vencimiento_cercano = True
                estado = "VENCIDO" if fecha_cad < hoy else "Vence pronto"
                print(f" - {p['nombre']} ({p['caducidad']}): {estado}")
        except ValueError:
            pass
            
    if not vencimiento_cercano:
        print(" Ningun producto esta proximo a vencer.")
    print("="*40)

def ver_inventario():
    print("\n" + "="*45)
    print("INVENTARIO GENERAL DEL ALMACEN")
    print("="*45)
    print(f"{'PRODUCTO':<25} | {'CATEGORIA':<10} | {'CANTIDAD':<8} | {'CADUCIDAD'}")
    print("-" * 65)
    for p in inventario:
        print(f"{p['nombre']:<25} | {p['categoria']:<10} | {p['cantidad']:<8} | {p['caducidad']}")
    print("="*45)

def anadir_producto():
    print("\n--- AÑADIR NUEVO PRODUCTO AL ALMACEN ---")
    nombre = input("Nombre del producto (ej. Crema de Rocoto, Carne, Tomate): ")
    categoria = input("Categoria (Carne / Verdura / Crema): ")
    try:
        cantidad = float(input("Cantidad numerica: "))
    except ValueError:
        print("Error: La cantidad debe ser un numero.")
        return
        
    unidad = input("Unidad de medida (ej. kg, litros, frascos, unidades): ")
    caducidad = input("Fecha de caducidad (Formato AAAA-MM-DD): ")
    
    try:
        datetime.strptime(caducidad, "%Y-%m-%d")
    except ValueError:
        print("Error: Formato de fecha invalido. Usa AAAA-MM-DD.")
        return

    nuevo = {
        "nombre": nombre,
        "categoria": categoria.capitalize(),
        "cantidad": cantidad,
        "unidad": unidad,
        "caducidad": caducidad
    }
    inventario.append(nuevo)
    print(f"El producto {nombre} ha sido añadido exitosamente al almacen.")

def anadir_plato():
    print("\n--- AÑADIR NUEVO PLATO ---")
    nombre = input("Nombre del plato: ")
    tipo = input("Tipo de plato (entrada / principal): ").lower()
    
    if tipo not in ["entrada", "principal"]:
        print("Error: El tipo debe ser estrictamente 'entrada' o 'principal'.")
        return
        
    platos.append({"nombre": nombre, "tipo": tipo})
    print(f"El plato '{nombre}' ha sido agregado a la lista de opciones.")

def ver_platos():
    print("\n" + "="*30)
    print("LISTA DE PLATOS REGISTRADOS")
    print("="*30)
    entradas = [p["nombre"] for p in platos if p["tipo"] == "entrada"]
    principales = [p["nombre"] for p in platos if p["tipo"] == "principal"]
    
    print("\nEntradas:")
    for e in entradas:
        print(f" - {e}")
        
    print("\nPlatos Principales:")
    for pr in principales:
        print(f" - {pr}")
    print("="*30)

def generar_menu_diario():
    entradas = [p for p in platos if p["tipo"] == "entrada"]
    principales = [p for p in platos if p["tipo"] == "principal"]
    
    if not entradas or not principales:
        print("Error: Faltan platos registrados (necesitas al menos una entrada y un principal).")
        return
        
    menu_entrada = random.choice(entradas)
    menu_principal = random.choice(principales)
    
    print("\n" + "*"*40)
    print("MENU DIARIO SUGERIDO (AL AZAR)")
    print("*"*40)
    print(f" Entrada:           {menu_entrada['nombre']}")
    print(f" Plato Principal:   {menu_principal['nombre']}")
    print("*"*40)

# ==========================================
# BUCLE PRINCIPAL DEL PROGRAMA
# ==========================================

def main():
    while True:
        print("\n--- SISTEMA DE GESTION PARA RESTAURANTE ---")
        print("1. Ver Almacen (Inventario y Alertas)")
        print("2. Añadir nuevo producto al almacen")
        print("3. Ver lista de platos")
        print("4. Añadir nuevo plato")
        print("5. Generar Menu Diario al azar (Entrada + Principal)")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opcion (1-6): ")
        
        if opcion == "1":
            mostrar_alertas()
            ver_inventario()
        elif opcion == "2":
            anadir_producto()
        elif opcion == "3":
            ver_platos()
        elif opcion == "4":
            anadir_plato()
        elif opcion == "5":
            generar_menu_diario()
        elif opcion == "6":
            print("\nGracias por usar el sistema del restaurante. Hasta luego.")
            break
        else:
            print("Opcion no valida. Por favor, elige un numero entre 1 y 6.")

if __name__ == "__main__":
    main()