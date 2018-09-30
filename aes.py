import sys

sbox = (
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
            )
sbox_inverse = (
            0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
            )

rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36,
            0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97,
            0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72,
            0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66,
            0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
            0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d,
            0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
            0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61,
            0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
            0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
            0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc,
            0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5,
            0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a,
            0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d,
            0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c,
            0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
            0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4,
            0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
            0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08,
            0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
            0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d,
            0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2,
            0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74,
            0xe8, 0xcb]


gm = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]
gm_inv = [[14, 11, 13, 9], [9, 14, 11, 13], [13, 9, 14, 11], [11, 13, 9, 14]]


def expand_key(key, num_rounds, Nk, Nb):
    key_size = len(key)

    # container for expanded key
    expandedKey = [] # should be 11 keys -> for rounds -> each key is 128 bits

    # first part of expanded key is the original key
    for i in range(Nk) :
        list_byte = list(key[i*4 : (i*4) + 4])
        expandedKey.append(list_byte)

    i = Nk

    temp = [0, 0, 0, 0]
    print(Nb)
    print(num_rounds)
    print(Nb * (num_rounds + 1))
    while i < Nb * (num_rounds + 1):

        temp = expandedKey[i-1]

        if i % Nk == 0:
            temp = rot_and_sub(temp, i)

        elif i % Nk == 4:
            for j in range(4):
                temp[j] = sbox[i]

        new_list = []
        for j in range(4):
            new_list.append(expandedKey[i-Nk][j] ^ temp[j])
        expandedKey.append(new_list)
        i = i + 1

    print(expandedKey)
    return expandedKey


def rot_and_sub(word, index):
    #rotate
    word = word[1:] + word[0:1]
    #sub
    for i in range(4):
        word[i] = sbox[word[i]]
    word[0] = word[0] ^ rcon[index/4]
    return word


def sub_bytes(arr):
      for i in range(4):
            for j in range(4):
                  val = sbox[arr[i][j]]
                  arr[i][j] = val
      return arr


def sub_bytes_inv(arr):
    for i in range(4):
          for j in range(4):
                val = sbox_inverse[arr[i][j]]
                arr[i][j] = val
    return arr


def shift(i, row):
      first_elems = row[0 : i]
      the_rest = row[i : len(row)]
      new_arr = the_rest + first_elems
      return new_arr

def shift_row(arr):
      for i in range(4):
            arr[i] = shift(i, arr[i])
      return arr;


def shift_inv(i, row):
    last_elems = row[i : len(row)]
    first_elems = row[0 : i]
    new_arr = last_elems + first_elems
    return new_arr

def shift_row_inv(arr):
    for i in range(4):
          arr[i] = shift_inv(i, arr[i])
    return arr;


def galois_multiply(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256


def matrix_multiplication(column):
      col = column
      mult = galois_multiply
      new_col = []
      new_col.append(mult(col[0], gm[0][0]) ^ mult(col[1], gm[0][1]) ^ mult(col[2], gm[0][2]) ^ mult(col[3], gm[0][3]))
      new_col.append(mult(col[0], gm[1][0]) ^ mult(col[1], gm[1][1]) ^ mult(col[2], gm[1][2]) ^ mult(col[3], gm[1][3]))
      new_col.append(mult(col[0], gm[2][0]) ^ mult(col[1], gm[2][1]) ^ mult(col[2], gm[2][2]) ^ mult(col[3], gm[2][3]))
      new_col.append(mult(col[0], gm[3][0]) ^ mult(col[1], gm[3][1]) ^ mult(col[2], gm[3][2]) ^ mult(col[3], gm[3][3]))

      return new_col


def mix_columns(arr):
      col = 0
      mixed_columns = []

      for col in range(4):
            column = []
            mixed_col = []
            for row in range(4):
                  column.append(arr[row][col])

            mixed_columns.append(matrix_multiplication(column))

      return map(list, zip(*mixed_columns))

def matrix_multiplication_inv(column):

      col = column
      mult = galois_multiply
      new_col = []
      new_col.append(mult(col[0], gm_inv[0][0]) ^ mult(col[1], gm_inv[0][1]) ^ mult(col[2], gm_inv[0][2]) ^ mult(col[3], gm_inv[0][3]))
      new_col.append(mult(col[0], gm_inv[1][0]) ^ mult(col[1], gm_inv[1][1]) ^ mult(col[2], gm_inv[1][2]) ^ mult(col[3], gm_inv[1][3]))
      new_col.append(mult(col[0], gm_inv[2][0]) ^ mult(col[1], gm_inv[2][1]) ^ mult(col[2], gm_inv[2][2]) ^ mult(col[3], gm_inv[2][3]))
      new_col.append(mult(col[0], gm_inv[3][0]) ^ mult(col[1], gm_inv[3][1]) ^ mult(col[2], gm_inv[3][2]) ^ mult(col[3], gm_inv[3][3]))

      return new_col

def mix_columns_inv(arr):
      col = 0
      mixed_columns = []

      for col in range(4):
            column = []
            mixed_col = []
            for row in range(4):
                  column.append(arr[row][col])
            mixed_columns.append(matrix_multiplication_inv(column))

      return map(list, zip(*mixed_columns))

def get_round_key(expandedKey, round_num):
    key = expandedKey[round_num]
    print(key)
    return expandedKey[round_num * 4: round_num * 4 + 4]

def add_round_key(arr, round_key):
    print(round_key)
    count = 0
    for i in range(4):
        for j in range(4):
          arr[i][j] = arr[i][j] ^ round_key[i][j]
          count += 1
    return arr

def aes_encrypt(arr, key, Nk, Nr, Nb):
    b = bytearray()
    b.extend(map(ord, key))
    print(b)
    num_rounds = Nr
    expanded_key = expand_key(b, num_rounds, Nk, Nb)
    encrypt_main(arr, expanded_key, num_rounds)
    return arr

def encrypt_main(arr, expanded_key, num_rounds):
    round_key_og = get_round_key(expanded_key, 0)
    add_round_key(arr, round_key_og)
    for i in range(1, num_rounds):
        round_key = get_round_key(expanded_key, i)
        sub_bytes(arr)
        shift_row(arr)
        mix_columns(arr)
        add_round_key(arr, round_key)

    # final round don't do mix_columns
    round_key = get_round_key(expanded_key, num_rounds)
    sub_bytes(arr)
    shift_row(arr)
    add_round_key(arr, round_key)

def aes_decrypt(arr, key, Nk, Nr, Nb):
    b = bytearray()
    b.extend(key.encode())
    num_rounds = Nr
    expanded_key = expand_key(b, num_rounds, Nk, Nb)
    decrypt_main(arr, expanded_key, num_rounds)
    return arr

def decrypt_main(arr, expanded_key, num_rounds):
    round_key_og = get_round_key(expanded_key, num_rounds)
    add_round_key(arr, round_key_og)
    shift_row_inv(arr)
    sub_bytes_inv(arr)
    for i in range(num_rounds - 1, 0, -1):
        round_key = get_round_key(expanded_key, i)
        add_round_key(arr, round_key)
        mix_columns_inv(arr)
        shift_row_inv(arr)
        sub_bytes_inv(arr)
    round_key = get_round_key(expanded_key, 0)
    add_round_key(arr, round_key)

def addPadding(plaintext):
    length_to_pad = 16 - (len(plaintext) % 16)
    padding = (chr(length_to_pad) * length_to_pad)
    return plaintext + padding

def main():

    # get command line arguments
    key_size = sys.argv[2]
    key_file = sys.argv[4]
    input_file = sys.argv[6]
    output_file = sys.argv[8]
    mode = sys.argv[10]

    # read from input and key file to get key and plaintext
    f = open(key_file, "r")
    key = f.read()
    f = open(input_file, "r")
    plaintext = addPadding(f.read())

    b = bytearray()
    b.extend(map(ord, plaintext))

    # put plaintext into 4x4 matrix
    arr = [[0 for x in range(4)] for y in range(4)]
    count = 0
    for i in range(4):
        for j in range(4):
            arr[i][j] = b[count]
            count+=1
    print(key_size)

    if key_size == '128':
        Nk = 4
        Nr = 10
        Nb = 4
    else:
        Nk = 8
        Nr = 14
        Nb = 4

    print("Original", arr)
    print("Original key", key)
    print("")

    if mode == 'e':
        arr = aes_encrypt(arr, key, Nk, Nr, Nb)
    elif mode == 'd':
        arr = aes_decrypt(arr, key, Nk, Nr, Nb)
    else:
        arr = aes_encrypt(arr, key, Nk, Nr, Nb)
        arr = aes_decrypt(arr, key, Nk, Nr, Nb)


    print(arr)

    # put resulting state into string
    result = ""
    for i in range(4):
        for j in range(4):
            result = result + chr(arr[i][j])

    # write to file
    f = open(output_file, "w")
    f.write(result)

if __name__ == '__main__':
    main()
