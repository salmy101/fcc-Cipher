message = "Hello, World!"
shift = 6

#result placeholder
encrypted_message = " "
#Go through each letter on the message using a for loop
for char in message:
  #if a charcter is NOt a letter in the alphabet then just ignore it
  if char.isalpha():
    #convert the character into its ASCII code
    char_code = ord(char)

    #new leter after shifting
    encrypted_code = char_code + shift

    #conver the new number into a strg
    encrypted_char = chr(encrypted_code)

    #add each new charcater to one another
    encrypted_message = encrypted_message + encrypted_char
  
print(encrypted_message)


