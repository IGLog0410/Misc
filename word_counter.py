"""
 Finished implementing the function to extract words from a text.
"""
import re

# Input a text
context = input()
# Evict ",", "." and so on using ASCII codes
for i in range(33, 64):
    context = context.replace(str(chr(i)), '')
for i in range(91, 96):
    context = context.replace(str(chr(i)), '')
for i in range(123, 127):
    context = context.replace(str(chr(i)), '')

# Replace uppercase letters to lowercase letters.
for i in range(65,90):
    context = context.replace(str(chr(i)), str(chr(i+32)))

# Devide context to words
words = list(context.split())
print(words)

