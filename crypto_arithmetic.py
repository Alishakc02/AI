from itertools import permutations
def solve_cryptoarithmetic(equation):
  
    parts = equation.split(' ')
    
    if len(parts) != 5 or parts[3] != '=' or parts[1] != '+':
        print("Invalid equation format. Please use the format: WORD1 + WORD2 = RESULT")
        return

    word1, word2, result = parts[0], parts[2], parts[4]
    letters = set(word1 + word2 + result)
    
    if len(letters) > 10:
        print("Too many distinct letters (max 10 unique letters).")
        return
    for perm in permutations(range(10), len(letters)):
        letter_to_digit = dict(zip(letters, perm))
        word1_value = sum(letter_to_digit[letter] * (10 ** idx) for idx, letter in enumerate(reversed(word1)))
        word2_value = sum(letter_to_digit[letter] * (10 ** idx) for idx, letter in enumerate(reversed(word2)))
        result_value = sum(letter_to_digit[letter] * (10 ** idx) for idx, letter in enumerate(reversed(result)))
        if word1_value + word2_value == result_value:
            print(f"Solution found:")
            print(f"{word1} = {word1_value}, {word2} = {word2_value}, {result} = {result_value}")
            print(f"Digit mapping: {letter_to_digit}")
            return 

    print("No solution found.")

def main():
    equation = input("Enter the cryptoarithmetic equation:")
    solve_cryptoarithmetic(equation)

if __name__ == "__main__":
    main()
