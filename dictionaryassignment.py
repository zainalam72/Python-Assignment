# Ex : 1
# rivers = {
#     'Nile' : 'Egypt',
#     'Indus' : 'Pakistan',
#     'Niagara' : 'Canada',
#     'Amazon' : 'South America',
#     'Indus' : 'Pakistan'
# }

# for r,l in rivers.items():
#     print(r , 'runs through' , l)
#     print('River - ',r)
#     print('Location - ',l)
    
# Ex : 2a

# per1 = {
#     "first name" : "Zain",
#     "last name" : "Alam",
#     "age" : 22,
#     "city" : "Karachi"
# }
# print(per1)
# per2 = {}
# if per1 == per2:
#     print(per2)


# Ex : 2b

# per1 = {
#     "first name" : "Zain",
#     "last name" : "Alam",
#     "age" : 22,
#     "city" : "Karachi"
# }
# per2 = {
#     "first name" : "Aslam",
#     "last name" : "Khan",
#     "age" : 34,
#     "city" : "Islamabad"
# }
# per3 = {
#     "first name" : "Shehzad",
#     "last name" : "Shaikh",
#     "age" : 46,
#     "city" : "Lahore"
# }
# for i in per1,per2,per3:
#     print(i)


# Ex : 3

# cities = {
#     "Karachi" : {
#         "Country" : "Pakistan",
#         "Approximate Population" : 15741000,
#         "Fact" : "Karachi is among the cheapest city to live in"},

#     "Madrid" : {
#         "Country" :"Spain",
#         "Approximate Population" : 49000000,
#         "Fact" : "Madrid is the fifth largest city in Europe."},

#     "Toronto" : {
#         "Country" : "Canada",
#         "Approximate Population" : 2930000,
#         "Fact" : "Toronto is the most populous city in Canada"}
# }
# for i,j in cities.items():
#     print(i)
#     for k,l in j.items():
#         print(k ,":", l)


# Ex : 4

# dic_1 = {
#     1:10,
#     2:20}

# dic_2 = {
#     3:30,
#     4:40}

# dic_3 = {
#     5:50,
#     6:60}

# dic_1.update(dic_2)
# dic_1.update(dic_3)
# print(dic_1)


# Ex : 5

# String = "Dictionaries"
# dic = {}
# for s in String:
#     a = String.count(s)
#     dic[s] = a
# print(dic)


# Ex : 6

# dct = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#         'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#         'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

# for a in dct.values():
#     print("The Value of 5th Number is : ",a[4])


# Ex : 7a

# prices = {
#     "Banana" : 4,
#     "Apple" : 2,
#     "Orange" : 1.5,
#     "Pear" : 3
# } 

# for a,k in prices.items():
#     print(a)
#     print("The price of",a,"is",k,"$")


# Ex : 7b

# total = 0
# stock = 6
# prices = {
#     "Banana" : 4,
#     "Apple" : 2,
#     "Orange" : 1.5,
#     "Pear" : 3}
# for i,j in prices.items():
#     print(i,j)
#     new = j*stock
#     print("Your price is :",new)
# total += int(new)
# print("Total",total)


# Ex : 8

# word = "MISSISSIPPI"
# dic={}

# for l in word:
#     dic[l] = word.count(l)
# print('\n',dic)


# Ex : 9

# positive = {}
# dict = {'a':1, 'b':-2, 'c':-3, 'd':7, 'e':0}
# for a,b in dict.items():
#     if b >= 0:
#         positive[b] = a
# print(positive)


# EX : 10

dict = {
    1: ["Samuel", 21, "Data Structures"],
    2: ["Richie", 20, "Machine Learning"],
    3: ["Lauren", 21, "OOPS with java"],}


for s,o in dict.items():
    print(s,o)