#. 1 Definición de funciones

def convertir_moneda(monto):
    return monto * 0.92
 
def calcular_impuesto(monto, porcentaje):
    return monto * (porcentaje / 100)
    
#. 2 Codigo principal

monto_venta = 200
porcentaje_iva = 16.0

#. 3 Usamos las funciones para calcular los datos

impuesto = calcular_impuesto(monto_venta,  porcentaje_iva)
total_usd = monto_venta + impuesto
total_eur  = convertir_moneda(total_usd)

#. 4 Motrar resultados 

print(f"Subtotal: ${monto_venta} USD")
print(f"Impuesto ({porcentaje_iva}%): ${impuesto} USD")
print(f"Total a pagar: {total_usd} USD")
print(f"Total equivalente: €{total_eur} EUR")
