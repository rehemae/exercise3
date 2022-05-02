house="yellow"
house_copy="yellow"
print(house==house_copy)

my_string = "0123456789"
print(my_string[-2: -6: -2])

#On your interpreter capitalize the first letter of each word in the string 
x="python is an awesome language"
print(x.title())



#On your Interpreter, replace all the occurrences of letter i with letter e in the following string 
#I love Akirachix
school="I love Akirachix"
print (school.replace("e","i"))


 #Given the list x = ["a", "b", 1, 42, True, False], on your interpreter, reverse the list. Paste your code and output below
x = ["a", "b", 1, 42, True, False]
print(x.reverse())



#On your interpreter, create the dictionary country_codes = {"Kenya":254, "Uganda":256, "Rwanda": 250}
#Add Burundi with a code of 257
#Remove Uganda from the dictionary

codes = {"Kenya":254, "Uganda":256, "Rwanda": 250}
codes["burundi"]=257
print(codes)

print(codes.pop("Uganda"))
print(codes)

#Given the list a = [150, 250, 350, 450, 550], use a list comprehension to create a new list b where each number in a is divided by 9
a = [150, 250, 350, 450, 550]
b= [n/9 for n in a]
print(b)

#Given the tuple y = (10,20,30,40,50), on your interpreter use a for loop to print the remainder of each number divided by 3. Paste your code and output it below
y = (10,20,30,40,50)
x=[n%3 for n in y]
print(x)




