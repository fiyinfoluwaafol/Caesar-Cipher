import sys

def encode_char(letter):
    if letter == "Y" or letter == "Z":
        return chr(ord(letter)+int(sys.argv[1])-26)
    else:
        return chr(ord(letter)+int(sys.argv[1]))

for line in sys.stdin:
    message = line
    break
count = 0
num_of_blocks = 0
msg_encoded = ""
msg_decoded = ""

for char in message:
    if char.isalpha():
        msg_decoded += char.upper()

for character in msg_decoded:
    if num_of_blocks == 10:
        msg_encoded.strip()
        msg_encoded += "\n"
        num_of_blocks = 0
    count += 1
    msg_encoded += encode_char(character)
    if count == 5:
        msg_encoded += " "
        count = 0
        num_of_blocks += 1

print(msg_encoded)

