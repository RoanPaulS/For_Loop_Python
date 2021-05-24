word = input("Enter any word : ");
reverse = word[::-1];  # <----- using step operator function

print("Word = ",word);
print("Reverse = ",reverse);


if(word ==  reverse):
    print("Given word",word," is a Palindrome");
else:
    print("Given word",word," is not a Palindrome");
