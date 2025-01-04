message = "Hello, World!"
shift = 6
MAX_CHAR_COUNT = 90
CHAR_RANGE = 26

#result placeholder
encrypted_message = " "
#Go through each letter on the message using a for loop
for char in message.upper():
  #if a charcter is NOt a letter in the alphabet then just ignore it
  if char.isalpha():
    #convert the character into its ASCII code
    char_code = ord(char)

    #new leter after shifting
    encrypted_code = char_code + shift

    if char_code > MAX_CHAR_COUNT:
      char_code -= CHAR_RANGE  

    #conver the new number into a strg
    encrypted_char = chr(encrypted_code)

    #add each new charcater to one another
    encrypted_message += encrypted_char

  else:
    #adding the non-alpheabetical character as they are
      encrypted_message += char

  
print(encrypted_message)


