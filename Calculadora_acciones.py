print("Calculadora de Rendimiento de Acciones")
def calcular_rendimiento(precio_compra, precio_venta):
  try:
      precio_compra = float(precio_compra)
      precio_venta = float(precio_venta)
      rendimiento = ((precio_venta - precio_compra) / precio_compra) * 100
      return rendimiento
  except ZeroDivisionError:
      print("Por favor, ingrese valores numéricos válidos.")

precio_compra = input("Ingrese el precio de compra de las acciones: ")
precio_venta = input("Ingrese el precio de venta de las acciones: ")

rendimiento = calcular_rendimiento(precio_compra, precio_venta)

if rendimiento is not None:
  print(f"\nEl rendimiento de las acciones es: {rendimiento:.2f}%")
