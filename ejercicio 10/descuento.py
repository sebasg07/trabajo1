calcular_precio_con_decuento(precio_base, porcentaje_descuento)
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    retunr precio_final

precio_base = float("Ingrese el precio base del producto: ")
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
