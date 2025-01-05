
MAX_CHAR_CODE = 90
MIN_CHAR_CODE = 65
CHAR_RANGE = 26


#lets make this into a function
def caesar_shift(message, shift):

  #result placeholder
  encrypted_message = " "

#Go through each letter on the message using a for loop
  for char in message.upper():
    if char.isalpha():   #if a charcter is NO a letter in the alphabet then just ignore it
      char_code = ord(char)     #convert the character into its ASCII code

      encrypted_code = char_code + shift     #new leter after shifting

      if char_code > MAX_CHAR_CODE:
        char_code -= CHAR_RANGE
        
      if char_code < MIN_CHAR_CODE:
        char_code += CHAR_RANGE

      encrypted_char = chr(encrypted_code)     #conver the new number into a strg
      encrypted_message += encrypted_char    #add each new charcater to one another

    else:
      encrypted_message += char     #adding the non-alpheabetical character as they are
  print(encrypted_message)



user_message = input("What message would you like to encrypt: ") 
user_shift = int(input("By what number would you like to shift your message by?: "))

caesar_shift(user_message, user_shift)
