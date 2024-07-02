## Bleatrix Trotter

This project solves the Bleatrix Trotter problem, where a sheep counts multiples of a number to fall asleep. The project is structured in Python and uses unit tests to verify the correct implementation.

### Project Description

Bleatrix Trotter has a strategy to fall asleep faster. She picks a number N and starts naming N, 2 × N, 3 × N, and so on. She thinks about all the digits in those numbers and keeps track of the digits 0 through 9 she has seen at least once. Once she has seen all ten digits, she falls asleep.

The objective is to determine the last number she will name before falling asleep. If she cannot see all the digits, the program should return "INSOMNIA".

### Project Structure

- winclap_ex2/
  - bleatrix_trotter.py
  - c-input.in
  - test_bleatrix_trotter.py
  - c-input_test.in    

where:

bleatrix_trotter.py :Contains the main logic to solve the Bleatrix Trotter problem 

c-input.in: Input file that contains the test cases

test_bleatrix_trotter.py: Unit tests

c-input_test.in: Input file for unit tests


### How to Run


1. Run the `bleatrix_trotter` script:
    ```
    python .\bleatrix_trotter.py <your_input_file>
    ```
    If no input file is specified, it defaults to c-input.in 

2. Run the tests:
    ```
    python .\test_bleatrix_trotter.py
    ```

### Example Usage

Make sure that your input file contains the test cases. The file format should be:
    
    
    T
    N1
    N2
    ...
    NT

with

LIMITS
```
1 ≤ T ≤ 100
```

DATASET
```
0 ≤ Ni ≤ 200
```

For example:
```
4
0
1
2
11
```
When you run the bleatrix_trotter.py script for the example input above, it is going to produce the output:

```
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
```
