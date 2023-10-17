#la puntuación del examen
examen = float(input("cual fue la puntuación del examen (0-100): "))

# asignaciones completadas
asignaciones_completadas = int(input("me puedes decir  el número de asignaciones completadas (0-10): "))

# Obtener la participación (Sí/No)
participacion = input("¿Hubo participación? (Sí/No): ").lower()

# Verificar los criterios para aprobar
if examen >= 70 and asignaciones_completadas >= 5:
    print("El estudiante ha aprobado.")
elif examen < 70 and participacion == "sí":
    print("El estudiante ha aprobado.")
else:
    print("El estudiante no ha aprobado.")
