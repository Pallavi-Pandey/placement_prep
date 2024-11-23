# Write a Python program to find the longest word in the sentence.

sentence = "The quick brown fox jumps over the lazy dogggggggggg"
words = sentence.split()
print (max(words, key=len))