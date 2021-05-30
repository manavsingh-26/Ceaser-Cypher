alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt_decrypt(text,shift,direction):
  letters = ""
  for i in text:
    ind = alphabet.index(i)
    if direction == 'encode':
        ind +=shift
        
    elif direction == 'decode':
        ind -=shift
        
    else:
        print("Wrong choice")
        return
    ind%=26
    a =alphabet[ind]
    letters += a 
  print(f"The {direction}d text is "+ letters)

encrypt_decrypt(text,shift,direction)
