def is_armstrong_number(number):
    power = len(str(number))
    result = 0
    for character in str(number):
        result += int(character)**power
    return result == number