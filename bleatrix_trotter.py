def solve_cases(input_file):
    # Check if the input file exists and is not empty
    import os
    if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
        raise ValueError(f"Input file '{input_file}' does not exist or is empty")

    # Open the file to read the data
    with open(input_file, 'r') as file:
        data = file.read().strip().split()

    T = int(data[0])  # Number of test cases
    cases = [int(data[i]) for i in range(1, T + 1) if 0 <= int(data[i]) <= 200]  # List of cases within limits

    if not (1 <= T <= 100):
        raise ValueError("Number of test cases (T) must be between 1 and 100")

    results = []

    for idx, N in enumerate(cases):
        result = solve_case(N)
        results.append(f"Case #{idx + 1}: {result}")

    for result in results:
        print(result)


def solve_case(N):
    if not (0 <= N <= 200):
        raise ValueError("Value of N must be between 0 and 200")

    if N == 0:
        return "INSOMNIA"

    seen_digits = set()
    iteration = 0

    while len(seen_digits) < 10:
        iteration += 1
        number = N * iteration
        seen_digits.update(str(number))

    return str(N * iteration)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        input_file = 'c-input.in'
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
    else:
        print("Usage: python bleatrix_trotter.py <input_file>")
        sys.exit(1)

    solve_cases(input_file)
