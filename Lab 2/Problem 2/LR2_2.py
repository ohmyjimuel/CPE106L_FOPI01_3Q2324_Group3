def main():
    filename = input("Enter the filename: ")
    with open(filename, 'r') as f:
        lines = f.readlines()

    while True:
        print(f"There are {len(lines)} lines in the file.")
        line_num = int(input("Enter a line number (0 to quit): "))

        if line_num == 0:
            break

        elif 1 <= line_num <= len(lines):
            print(f"Line {line_num}: {lines[line_num - 1]}")

        else:
            print("Invalid line number.")

main()