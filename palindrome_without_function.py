word = input("Enter any word : ");
start = -1;
end = len(word)-1;
print(start);
print(end);
reverse = "";
for i in range(end , start , -1):
    reverse = reverse + word[i];
   # print(word[i],end="");

print("Word = ",word);
print("Reverse = ",reverse);


if(word ==  reverse):
    print("Given word",word," is a Palindrome");
else:
    print("Given word",word," is not a Palindrome");


"""
Palindrome Program using Javascript

var word = "malayalam";
var reverse = "";
var start = 0
var end = word.length-1;
console.log(start);
console.log(end);

for(var i=end;i>=start;i--)
{
	reverse = reverse+word[i];
}
document.write(reverse);
if(word == reverse)
{
    document.write("Given word is Palindrome");
}
"""
