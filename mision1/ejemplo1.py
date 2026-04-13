import pandas as pd
# crear datos (simulación estudiantes)
datos={
  "nombre":["Ana","Gelen","Carlos","Sofia","Pedro"],
  "Edad":[30,70,18,21,22],
  "Nota":[3.5,4.2,2.8,4.8,3.0]
}
df =pd.DataFrame(datos)
print(df)
#promedio de notas
print("Promedio:",df["Nota"].mean())
#promedio de Edades
print("Promedio:",df["Edad"].mean())
