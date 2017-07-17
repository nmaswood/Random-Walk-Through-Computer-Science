NUMBER_OF_LETTERS = 26
A_IN_PYTHON = 97

def casear_cipher(n):

    encrypt = {}

    for i in range(NUMBER_OF_LETTERS + 1):

        original_letter = i + A_IN_PYTHON
        shift = i + n

        letter = chr(original_letter)
        other_letter = chr((shift % NUMBER_OF_LETTERS) + A_IN_PYTHON)

        encrypt[letter] = other_letter

    return encrypt

e = casear_cipher(1)

def hash_function(string):

     x = 37

     for char in string:
        x = x * ord(char)

    return x


from random import randint


def create_mapping(msg):

    d = {}

    for i in range(len(msg)):

        random_shift_forward = randint(0,26)

        d[i] = random_shift_forward

    return d

randint(0,)




