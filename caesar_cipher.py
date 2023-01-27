import sys

def encode_char(letter): #This function contains the algorithm that encodes a character using the provided shift key from the user
    if ord(letter) > (90-int(sys.argv[1])): #This makes accommodation for when the letter reaches the end of the alphabet and the corresponding letter is at the start of the alphabet
        return chr(ord(letter)+int(sys.argv[1])-26)
    else:
        return chr(ord(letter)+int(sys.argv[1]))

for line in sys.stdin: #Gets the message from the user in a different way than using the input() function
    message = line
    break
count = 0 #This is used to ensure that the encoded letters are group in blocks of 5.
num_of_blocks = 0 #This is used to ensure that there are 10 blocks of letters per line.
msg_encoded = ""
msg_decoded = ""

for char in message: #This loops through each character in the message, to remove any non-alphabetic character, converts them to uppercase
    if char.isalpha():
        msg_decoded += char.upper()

for character in msg_decoded: #This loops through all the letters in the redefined message that contains only letters.
    if num_of_blocks == 10: #This makes use of the earlier defined variable to ensure that there are a maximum of 10 blocks of letter per line.
        msg_encoded.strip()
        msg_encoded += "\n"
        num_of_blocks = 0
    count += 1
    msg_encoded += encode_char(character) #Uses the earlier defined function to concatenate the encrypted character to the new string containign the entire encrypted message.
    if count == 5: #This ensures that there 5 letters in each block
        msg_encoded += " "
        count = 0
        num_of_blocks += 1

print(msg_encoded)

