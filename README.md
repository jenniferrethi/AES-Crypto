Amrutha Sreedarane  : as57286
Jennifer Rethi      : jlr5452
Ruchira Shekar      : rs48939


HOW TO RUN:
- To add plaintext, input bytes into input_file.txt
- To add key, add bytes to key
- To see output, view output_file.txt

ex:
python aes.py --keysize 128 --keyfile key --inputfile input_file.txt --outputfile output_file.txt --mode "e"


sub_bytes:
	This method takes each value in your 16 byte 4x4 state and subs it out with the corresponding value in the Sbox matrix. We got this matrix from the internet.

sub_bytes_inv:
	This is the inverse of the sub_bytes method - to be used during decyrption. This method takes each value in your 16 byte 4x4 state and subs it with the corresponding value in the inverse Sbox matrix.

shift_row:
	This method takes your 4x4 state and does a column order shift on each column. For the 0th column, no shift is done. For the 1 index column, the column is shifted left by 1. The 2nd index column is shifted left by 2 and the 3rd shifted left by 3. We added a helper method called shift which does the actual shifting. 

	We performed the shift by taking each column in the state and performing the shift on it. Then we transposed the state back to row order, since this is how we are handling the state in the rest of the code.

shift_row_inv:
	This method is performed the same way as shift_row however the columns are shifted to the right to perform decyrption.

mix_columns: 
	This method goes through the columns and then calls the matrix_multiplication method to perform the multiplication.

matrix_multiplication:
	This method calls the galois_multiply fuction on the column.

galois_multiply:
	This method performs the exact galois multiplication on the column. We watched a few videos that helped us understand the galois field and how to perform the bit shifts and multiply with the galois field. 

get_round_key:
	This method returns the round key (the arrays inside the expanded key array) at the necessary indices depending on which round we're on.

add_round_key:
	This method performs the xoring of each value in the array with the round key values in the expanded key array

aes_encrypt:
	This method calls the expand key function to build the expanded key array to get the round keys. The function then calls encrypt_main which performs the rounds.

encrypt_main:
	This method performs the rounds of encryption by calling the sub_bytes, shift_rows, mix_columns, add_round_key functions through the num rounds and then the final round.

aes_decrypt:
	This method calls the expand key function to build the expanded key array to get the round keys. The function then calls decrypt_main which performs the rounds for decryption.

decrypt_main:
	This method performs the rounds of decryption by calling the sub_bytes, shift_rows, mix_columns, add_round_key functions through the num rounds and then the final round.

addPadding:
	This method adds padding so that we are dealing with a length of 16 input at all times. 

main:
	This method reads from the input files, sets the number of rounds, the size of the input, and number of words values for the expand key function. The method calls the padding functions, and then handles calling the encrypt and decrypt functions. The function also writes to the file.

print_in_hex:
	This method returns the input array in hex.

print_in_hex:
	This method returns the expand key in hex.

expand_key:
	This method creates the expanded key for this key to perform the add round key function. This was explained in the attachment to the project description.

rot_and_sub:
	This method rotates the word to perform the expand key function and then substitutes it by subbing the byte of the first bit in the word with the Rcon matrix value.
