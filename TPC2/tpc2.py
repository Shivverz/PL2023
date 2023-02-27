import sys


def get_numbers(line):
    numbers = []
    current = ''

    for letter in line:
        if letter.isdigit():
            current += letter
        elif current:
            numbers.append(int(current))
            current = ''

    if current:
        numbers.append(int(current))

    return numbers


def suminator():
    total = 0
    isOn = True

    for line in sys.stdin:

        line = line.strip()

        if line.lower() == "off":
            isOn = False
        elif line.lower() == "on":
            isOn = True
        else:
            if isOn:
                numbers = get_numbers(line)
                total += sum(numbers)
            if '=' in line:
                print(total)
                total = 0


suminator()
