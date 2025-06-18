import sys

def printArt(input, font_data):
    output = []
    inputLines = input.split('\\n')

    for inputLine in inputLines:
        artRows = ["", "", "", "", "", "", "", ""]

        for char in inputLine:
            charArt = font_data[char]
                
            for i in range(8):
                artRows[i] += charArt[i]

        for row in artRows:
            output.append(row)

    return "\n".join(output)

def main():
    input = sys.argv[1]
    file = "standard.txt"
    font = {}

    with open(file, 'r') as file:
        lines = file.readlines()

    current_char_code = 32
    lineI = 0

    while lineI < len(lines):
        charLines = []
        for i in range(1, 9):
            artLine = lines[lineI + i].rstrip('\n')
            charLines.append(artLine)
                
        font[chr(current_char_code)] = charLines
        current_char_code += 1
        lineI += 9

    print(printArt(input, font))

if __name__ == "__main__":
    main()