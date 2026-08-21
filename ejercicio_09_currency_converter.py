import requests

def get_exchange_rates():
    # URL de una API pública de tasas de cambio (base USD)
    url = "https://open.er-api.com/v6/latest/USD"
    
    try:
        # Hacemos la petición GET al servidor
        response = requests.get(url)
        
        # El código 200 significa "Petición exitosa" (OK)
        if response.status_code == 200:
            data = response.json() # Convertimos la respuesta de texto a diccionario Python
            rates = data["rates"] # Extraemos solo el diccionario de tasas
            return rates
        else:
            print(f"❌ Error HTTP: Status {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

def main():
    print("=== CONSULTOR DE DIVISAS EN TIEMPO REAL ===")
    print("Conectando con el servidor web...\n")
    
    rates = get_exchange_rates()
    
    if rates:
        # Mostramos algunas divisas de ejemplo
        print(f"💵 1 USD = {rates.get('EUR'):.2f} EUR (Euros)")
        print(f"💵 1 USD = {rates.get('COP'):.2f} COP (Pesos Colombianos)")
        print(f"💵 1 USD = {rates.get('MXN'):.2f} MXN (Pesos Mexicanos)")
        
        print("\n--- CONVERTIDOR DE USD ---")
        try:
            usd_amount = float(input("Ingresa un monto en USD ($): "))
            eur_total = usd_amount * rates.get('EUR', 0)
            cop_total = usd_amount * rates.get('COP', 0)
            
            print(f"\nResultados para ${usd_amount:.2f} USD:")
            print(f"-> Euros: {eur_total:.2f} EUR")
            print(f"-> Pesos Colombianos: {cop_total:,.2f} COP")
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar un número.")

if __name__ == "__main__":
    main()
  
