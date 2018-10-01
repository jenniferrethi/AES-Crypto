Amrutha Sreedarane  :
Jennifer Rethi      :
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


	

