def read_unique_integers():
    try:
        numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

        unique_numbers = []

        for num in numbers:
            if num in unique_numbers:
                raise ValueError("Duplicate value found:", num)

            unique_numbers.append(num)

        print("All numbers are unique.")

    except ValueError as e:
        print("Error:", e)



read_unique_integers()
