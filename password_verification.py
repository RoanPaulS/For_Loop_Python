word = input("Enter any word : ");
length = len(word);
count_of_alpha = 0;
count_of_number = 0;
count_of_spchar = 0;


if length>=8:
    for letter in range(length):
        # if(word[letter].isalpha()):
        if((word[letter]>="A" and word[letter]<="Z") or
           (word[letter]>="a" and word[letter]<="z")):
                count_of_alpha = count_of_alpha + 1;
                
        # if(word[letter].isdigit()):
        elif(word[letter]>="0" and word[letter]<="9"):
            count_of_number = count_of_number+1;

        else:
            count_of_spchar = count_of_spchar+1;

    print("Number of Alphabets = ",count_of_alpha);
    print("Number of Numerics = ",count_of_number);
    print("Number of Special Characters = ",count_of_spchar);

else:
    print("Please enter 8 or above characters");



