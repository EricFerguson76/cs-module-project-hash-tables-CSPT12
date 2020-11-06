# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}


def build_table():
    for key, value in encode_table.items():
        decode_table[value] = key


def encode(s):
    new_string = ''

    for letter in s:
        if letter in encode_table:
            new_string += encode_table[letter]
        else:
            new_string += letter

    return new_string


def decode(s):
    new_string = ''

    for letter in s:
        if letter in decode_table:
            new_string += decode_table[letter]
        else:
            new_string += letter

    return new_string


build_table()

print(encode("HELLO, WORLD!"))

print(decode("DOGGE, BEUGW!"))
