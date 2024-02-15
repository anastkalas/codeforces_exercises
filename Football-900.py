def is_dangerous(situation):
    dangerous_substrings = ["0000000", "1111111"]
    for substring in dangerous_substrings:
        if substring in situation:
            return "YES"
    return "NO"
 
def main():
    input_string = input().strip()
    result = is_dangerous(input_string)
    print(result)
 
if __name__ == "__main__":
    main()