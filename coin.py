a = str(input("Enter an amount in dollars and cents: "))
b = a.split(".")
dollars = float(b[0])
cents = float(b[1])

verify = input((f"You have {dollars} dollars and {cents} cents. Continue? (type yes or no): "))

if verify == "yes":
    print(f"{dollars} dollars")

    print(f"{cents} cents")

    if dollars != 0:
        print(dollars//2, "toonies")
        if dollars % 2 != 0:
            loonies = float(1)
            print(loonies, "loonie")
        else:
            print(float(0), "loonies")

    if cents != 0:
        print(cents//25, "quarters")
        q = cents % 25

        print(q // 10, "dimes")
        d = q % 10

        print(d // 5, "nickles")
        n = d % 5

        print(n // 1, "pennies")
elif verify == "no":
    print("Goodbye!")

else:
    print("I don't understand that. Goodbye!")
