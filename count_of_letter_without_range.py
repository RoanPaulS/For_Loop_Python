### 1.Without Range

##word = input("Enter any word : ");
##count = 0;
##for letter in word:
##    print(letter,end=",");
##    count = count+1;
##
##print("");
##print("Total number of letter is : ",count);


# 2.With Range

word2 = input("Enter any word : ");
length = len(word2);
count = 0;

print("letter2 is : ");
for letter2 in range(length):
    print(letter2,end=" ");


print("");
print("");

print("word2[letter2] is : ");
for letter2 in range(length):
    print(word2[letter2],end=" ");
    count = count+1;

print("");
print("Total number of letter is : ",count);
