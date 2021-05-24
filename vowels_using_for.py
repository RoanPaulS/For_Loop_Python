word = "God is AGreat";
total = 0;
print("Vowels in given word '",word,"' are : "); 


for letter in word:
    if (letter in  ['a','e','i','o','u']) or (letter in ['A','E','I','O','U']) :
        print(letter,end=",");
        total = total+1;

print("");
print("Total vowel is ",total);


"""

Find Vowels using While Loop

word = input("Enter Your Name : ");
index = 0;
total = 0;
while(index < len(word)):
    #if(word[index] == 'a' or word[index] == 'e' or word[index] == 'i' or word[index] == 'o' or word[index] == 'u'):
    if word[index] in (['a','e','i','o','u'] or ['A','E','I','O','U']):
        print(word[index]);
        total = total+1;
    index = index+1;
print("Total number of vowels in given word",word,"is",total);

"""
