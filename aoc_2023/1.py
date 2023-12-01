import fileinput

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# create a list of lines (strings) from the input file
lines = list(fileinput.input())

def part1():
    count = 0
    for line in lines:
        calibration = ''
        # Find first
        for c in line:
            if c.isdigit():
                calibration = calibration + c
                break
        # Find last
        for c in reversed(line):
            if c.isdigit():
                calibration = calibration + c
                break
        count = count + int(calibration)
    return count

def part2():
    count = 0
    for line in lines:
        # Replace words for digits as digits
        line = ''.join([x if (x := ''.join([v for k, v in digits.items() if line[i:].startswith(k)])) else line[i] for i in range(len(line))])
        calibration = ''
        # Find first
        for c in line:
            if c.isdigit():
                calibration = calibration + c
                break
        # Find last
        for c in reversed(line):
            if c.isdigit():
                calibration = calibration + c
                break
        count = count + int(calibration)
    return count

print(part1())
print(part2())
