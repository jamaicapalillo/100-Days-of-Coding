alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO 1: Create a function called 'encrypt' that takes the 'original_text' and 'shift' as inputs.
# TODO 2: Inside the 'encrypt ()' function, shift each letter of the 'original_text' by the 'shift' amount and print the encrypted text.
# TODO 3: Call the 'encrypt()' function and pass the 'user inputs'. You should be able to test the code and encrypt a message.

def caesar_cipher (text, shift, direction):
    output_text = ""

    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabets:
            new_position = (alphabets.index(letter)+ shift) % 26
            output_text += alphabets[new_position]
        else:
            output_text += letter
    print(f"The {direction}d text is {output_text}")

caesar_cipher (text, shift, direction)

# def encrypt (original_text, shift):
#     encrypted_text = ""

#     for letter in original_text:
#         if letter in alphabets:
#             new_position = (alphabets.index(letter)+ shift) % 26
#             encrypted_text += alphabets[new_position]
#         else:
#             encrypted_text += letter

#     print(f"The encoded text is {encrypted_text}")

# def decipher (original_text, shift):
#     deciphered_text = ""

#     for letter in original_text:
#         if letter in alphabets:
#             new_position = (alphabets.index(letter) - shift) % 26
#             deciphered_text += alphabets[new_position]
#         else:
#             deciphered_text += letter

#     print(f"The decoded text is {deciphered_text}")

# if direction == "encode":
#     encrypt (text, shift)
# elif direction == "decode":
#     decipher (text, shift)
