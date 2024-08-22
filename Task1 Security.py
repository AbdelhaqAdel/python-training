# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 23:10:41 2023

@author: Alfy
"""

def encryption(decryptText, key):

  result = ""
  for ch in decryptText:
    if ch.isupper():
      result += chr((ord(ch) - 65 + key) % 26 + 65)
    elif ch.islower():
      result += chr((ord(ch) - 97 + key) % 26 + 97)
    else:
      result += ch
  return result


encryptedText = encryption("test TEXT", 4)
print('encrypted text : '+ encryptedText)



def decryption(encryptText, key):
  return encryption(encryptText, -key)

decryptedText = decryption("XIWX xibx", 4)
print('decrypted text : '+ decryptedText)



