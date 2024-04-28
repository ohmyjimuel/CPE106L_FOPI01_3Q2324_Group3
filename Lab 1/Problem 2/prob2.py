def obtain_file(filename):
    try:
        with open(filename, 'r') as readfile:
            lines = readfile.readlines()
            return lines
    except FileNotFoundError:
        print("File not found.")
        return None
    
def file_navigation():
    filename = input("Enter file name:")
    
    lines = obtain_file(filename)
    

    if not lines:
        return
    
    numLines = len(lines)

    while True:
        print("The number of lines in the file, ", filename, " is: ", numLines)
        whatLineNum = input(f"Enter the line number from 1 to {numLines} or 0 to quit: ")
        if whatLineNum == '0':
            print("Exiting the program.")
            break
        if not whatLineNum.isdigit() or int(whatLineNum) < 0 or int(whatLineNum) > numLines:
            print(f"Invalid input. Please enter a number between 1 and {numLines} or 0 to quit.")
            continue

        whatLineNum = int(whatLineNum)

        print("Line ", whatLineNum, ": ")
        print(lines[whatLineNum - 1])

file_navigation()
