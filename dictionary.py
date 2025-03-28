#counting the skills through dictionary
dict={
    "name":"sandhya",
    "student":"true",
    "skills":["python","java","javascript","html"],
    "languages":["telugu","english","urdu"]}

print(len(dict["skills"]))

#program to print list of prime and non prime numbers separately in given list
numbers=[1,2,3,4,5,6,7,8,9,11]
prime_numbers=[]
non_prime_numbers=[]
for num in numbers:
    if num<2:
        non_prime_numbers.append(num)
    else:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
               is_prime=False
               break
        if is_prime:
         prime_numbers.append(num)
        else:    
          non_prime_numbers.append(num)
print("prime numbers:",prime_numbers)
print("non-prime numbers:",non_prime_numbers)