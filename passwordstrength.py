LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

PUNCTUATION = "!£^&*(){}[]:@~;'#<>?"

PASSWORD_DESCRIPTIONS = ["dangerously insecure", 
                         "insecure", "weak", 
                         "medium", "strong",
                         "secure", "unbreakable"]


password = ""
passwordStrength = 0



def containsAnyOf(pPassword, pCharacters):
  found = False
  for character in pCharacters:
    for index in range(len(pPassword)):
      if character == pPassword[index]:
        found = True
  return found

def calcPasswordStrength(pPassword):
  strength = 0
  if containsAnyOf(pPassword, LETTERS):
    strength += 1
  if containsAnyOf(pPassword, LETTERS.lower()):
    strength += 1
  if containsAnyOf(pPassword, NUMBERS):
    strength += 1
  if containsAnyOf(pPassword, PUNCTUATION):
    strength += 1
  if len(pPassword) > 5:
    strength += 1
  

  return (strength)


password = input("Please enter a password")

passwordStrength = calcPasswordStrength(password)

print("Your password is " + PASSWORD_DESCRIPTIONS[passwordStrength])
