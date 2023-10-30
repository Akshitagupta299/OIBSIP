import random

lower = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
upper = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_-[]"

string = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(string , length))

print("YOUR NEW PASSWORD IS : "+ password)