alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO 1: Create a function called 'encrypt' that takes the 'original_text' and 'shift' as inputs.
# TODO 2: Inside the 'encrypt ()' function, shift each letter of the 'original_text' by the 'shift' amount and print the encrypted text.
# TODO 3: Call the 'encrypt()' function and pass the 'user inputs'. You should be able to test the code and encrypt a message.

def encrypt(original_text, shift):
    encrypted_text = ""

    for letter in original_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position + shift) % 26
            encrypted_text += alphabets[new_position]
        else:
            encrypted_text += letter

    print(f"The encoded text is {encrypted_text}")


if direction == "encode":
    encrypt(text, shift)

# TODO 4: What happens if you try to shift z forwards by 9? Can you fix the code?
