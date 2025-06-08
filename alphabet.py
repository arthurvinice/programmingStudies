alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_all_letters_number(number):
    if number < 1 or number > 26:
        return "Number must be between 1 and 26"
    result = []
    for i in range(number):
        result.append(alpha[i])
    return result
    

def main():
    print(get_all_letters_number(5))