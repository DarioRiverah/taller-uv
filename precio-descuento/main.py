PORCENTAJE_DESCUENTO = 0.10


def main():
    print("=== Precio con descuento ===")
    precio = float(input("Ingrese el precio del producto: "))

    descuento = precio * PORCENTAJE_DESCUENTO
    precio_final = precio - descuento

    print(f"\nPrecio original: {precio:.0f}")
    print(f"Descuento (10%): {descuento:.0f}")
    print(f"Precio final: {precio_final:.0f}")


if __name__ == "__main__":
    main()