def main():
    print("=== Edad futura ===")
    nombre = input("Ingrese su nombre: ")
    edad_actual = int(input("Ingrese su edad actual: "))

    edad_futura = edad_actual + 5

    print(f"{nombre}, actualmente tienes {edad_actual} años "
          f"y dentro de cinco años tendrás {edad_futura} años.")


if __name__ == "__main__":
    main()