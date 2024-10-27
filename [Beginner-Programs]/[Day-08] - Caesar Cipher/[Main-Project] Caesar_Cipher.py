import time

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def loading_sign (duration = 3, delay=0.5):
    print ("Exiting", end="")
    for _ in range (duration):
        print (".", end="", flush=True)
        time.sleep(delay)
    print()
    
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

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher (text, shift, direction)

    while True:
        another_input = input ("Do you want to use the program again? Y or N. ").upper()

        if another_input == "Y":   
            break
        elif another_input == "N":
            print ("Thank you for using our program.")
            loading_sign()
        else:
            ("Invalid. Please type only Y or N.")
