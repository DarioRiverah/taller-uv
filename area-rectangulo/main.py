def main():
    print("=== Área de un rectángulo ===")
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    area = base * altura

    print(f"\nBase: {base:g}")
    print(f"Altura: {altura:g}")
    print(f"Área: {area:g}")


if __name__ == "__main__":
    main()