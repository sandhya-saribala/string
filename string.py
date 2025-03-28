#string methods

#upper()
name="sandhya"
print(name.upper())

#strip()
name="  sandhya "
print(name.strip())

#replace()
name=("my name is sandhya")
print(name.replace("d","D"))

#starts with()
string="sandhya"
print(string.startswith("d"))

#ends with()
string="sandhya"
print(string.endswith("y"))

#find()
string="sandhya"
print(string.find("s"))

#count()
skills=("html","java","python","css")
print(skills.count("devops"))

#title()
sentence="eat five star do nothing"
print(sentence.title())

#capitalize()
name="my name is sandhya"
print(name.capitalize())

#swapcase()
name="sanDHYA"
print(name.swapcase())

#zfill()
name="sandhya"
print(name.zfill(10))

#isalpha()
name="12344"
print(name.isalpha())

#isalphanum()
name="sandhya1234"
print(name.isalnum())

#isdigit()
num="1234567890"
print(num.isdigit())

#center()
name="sandhya"
print("sandhya".center(10,"*"))

#ord(char)
name="a"
print(ord(name))

#chr(int)
name="120"
print(chr(int(120)))

#split()
string="i am a good girl"
print(string.split(" "))

#join()
string=["hi","sandhya"]
print(" ".join(string))

#take a string it contains both upper case and lower case,print no of vowels and consonants present in the string
name="sanDHYA"
vowels="AEIOUaeiou"
vowel_count=0
consonant_count=0
for char in name:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print("number of vowels:",vowel_count)
print("number of consonants:",consonant_count) # type: ignore