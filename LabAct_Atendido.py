words = []
length = []

for user in range(10):
    y = input(f"Enter a word {user + 1}: ")
    words.append(y)
    if any(meow.isdigit() for meow in y): 
        print("Error! Please enter a valid word.")
        
letters = int(input("Enter the number of letters:"))
    
for word in words:  
    if len(word) >= letters:
        length.append(word)        
    else:
        continue        
print(f"Here are the words that have {letters} letters: {length}")