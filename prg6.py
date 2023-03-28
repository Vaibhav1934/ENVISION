word = 'hello'

reversed_word = ""

for i in range(len(word) -1, -1):
    reversed_word += word[i] 

print("The word in reverse is:")
print(reversed_word, end="")
