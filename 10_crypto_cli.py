import requests

def obtener_precio_crypto(crypto_id):
    """Consulta la API de CoinGecko para obtener el precio de una crypto."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Si la crypto existe en la respuesta, retornamos el precio
            if crypto_id in datos:
                return datos[crypto_id]["usd"]
            else:
                return None
        else:
            print(f"\n⚠️ Error de servidor (Código HTTP: {respuesta.status_code})")
            return None
    except requests.exceptions.RequestException:
        print("\n❌ Error de conexión a internet.")
        return None

def mostrar_menu():
    print("\n" + "="*35)
    print(" 🚀 CONSULTOR CRYPTO EN TIEMPO REAL")
    print("="*35)
    print("1. Consultar Bitcoin (BTC)")
    print("2. Consultar Ethereum (ETH)")
    print("3. Consultar Solana (SOL)")
    print("4. Buscar otra criptomoneda")
    print("5. Salir")
    print("="*35)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            precio = obtener_precio_crypto("bitcoin")
            if precio:
                print(f"\n💵 Bitcoin (BTC): ${precio:,.2f} USD")
        elif opcion == "2":
            precio = obtener_precio_crypto("ethereum")
            if precio:
                print(f"\n💵 Ethereum (ETH): ${precio:,.2f} USD")
        elif opcion == "3":
            precio = obtener_precio_crypto("solana")
            if precio:
                print(f"\n💵 Solana (SOL): ${precio:,.2f} USD")
        elif opcion == "4":
            nombre_crypto = input("Ingresa el ID de la crypto (ej. cardano, dogecoin): ").strip().lower()
            precio = obtener_precio_crypto(nombre_crypto)
            if precio:
                print(f"\n💵 {nombre_crypto.capitalize()}: ${precio:,.2f} USD")
            else:
                print(f"\n⚠️ No se encontró la criptomoneda '{nombre_crypto}'.")
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Hasta luego, hermano. 👋")
            break
        else:
            print("\n❌ Opción inválida. Intenta del 1 al 5.")

if __name__ == "__main__":
    main()
              
