num = int(input("Enter a number : "));
total = 0;
for i in range(num):
    print(i);
    total = total+ i ;

print("Total is ",total);





start = int(input("Enter start value : "));
end = int(input("Enter end value : "));

for a in range(start , end):
    print(a,end=",");
