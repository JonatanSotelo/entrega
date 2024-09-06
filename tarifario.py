# Definimos las tarifas base
BASE_FEE = 5.00  # Tarifa base por pedido
FEE_PER_KG = 1.00  # Tarifa por kilogramo
FEE_PER_KM = 0.10  # Tarifa por kilómetro

# Tarifas adicionales según el tipo de servicio
SERVICE_TYPES = {
    "standard": 1.0,  # Sin tarifa adicional
    "express": 1.5,  # 50% adicional
    "overnight": 2.0  # 100% adicional
}

def calculate_shipping_cost(weight_kg, distance_km, service_type="standard"):
    """
    Calcula el costo total de envío basado en el peso, distancia y tipo de servicio.
    
    Args:
    weight_kg (float): Peso del paquete en kilogramos.
    distance_km (float): Distancia de envío en kilómetros.
    service_type (str): Tipo de servicio de envío (standard, express, overnight).
    
    Returns:
    float: Costo total de envío.
    """
    
    # Validamos que el tipo de servicio sea válido
    if service_type not in SERVICE_TYPES:
        raise ValueError("Tipo de servicio no válido. Debe ser 'standard', 'express' o 'overnight'.")

    # Cálculo de las tarifas de envío
    weight_fee = FEE_PER_KG * weight_kg
    distance_fee = FEE_PER_KM * distance_km
    service_multiplier = SERVICE_TYPES[service_type]

    # Costo total
    total_cost = (BASE_FEE + weight_fee + distance_fee) * service_multiplier
    
    return round(total_cost, 2)

# Ejemplo de uso
weight = 10.5  # en kilogramos
distance = 120  # en kilómetros
service = "express"  # Tipo de servicio

cost = calculate_shipping_cost(weight, distance, service)
print(f"El costo total de envío es: ${cost}")
