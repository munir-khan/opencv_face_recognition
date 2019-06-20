# # myitems = [[1,"Item1",100,0],[2,"Item2",150,0],[3,"Item3",75,0],[4,"Item4",20,0],[5,"Item5",15,0]]
# # tempList = []
# #
# # def printall():
# #     for x in myitems:
# #         print (x)
# #
# #
# #
# # def new():
# #
# #     userinput = int(input("Please enter a number:"))
# #     tempList.append(userinput)
# #
# #     userinput = input("Please enter a name:")
# #     tempList.append(userinput)
# #
# #     # myitems.append(tempList[:])
# #     # myitems.append(list(tempList))
# #     # tempList.clear()
# #
# # new()
# # new()
# # new()
# # printall()
#
# import numpy as np
#
# myitems = [[1, "Item1", 100, 0], [2, "Item2", 150, 0], [3, "Item3", 75, 0], [4, "Item4", 20, 0], [5, "Item5", 15, 0]]
# tempList = []
#
#
# # Function print_all
#
# def printall():
#     for x in myitems:
#         print(*x)
#
#     # Function new()
#
#
# def new():
#     userinput = int(input("Please enter a number:"))
#     tempList.append(userinput)
#
#     userinput = input("Please enter a name:")
#     tempList.append(userinput)
#
#     myitems.append(tempList[:])
#     tempList.clear()
#     printall()
#
#
# # Calling the function
# # new()
#
# # def urandom(n): # real signature unknown; restored from __doc__
# #     """
# #     urandom(n) -> str
# #
# #     Return n random bytes suitable for cryptographic use.
# #     """
# #     return ""
# #
# #
# # from os import urandom
# # letters = "ABCDEFGHJKLMNPRSTUVWXYZ"
# # password = "".join(letters[c % len(letters)] for c in urandom(6))
# # print(password)
# import re
#
# # import random
# #
# # board = [1,2,3,4,5,6,7,8,9]
# #
# # # *#display the board*
# #
# # def display():
# #   print(board[0], " | ", board[1], " | ", board[2])
# #   print("-------------")
# #   print(board[3], " | ", board[4], " | ", board[5])
# #   print("-------------")
# #   print(board[6], " | ", board[7], " | ", board[8])
# #   print(" ")
# #
# # display()
# #
# # # *# checks for winner*
# #
# # def winner(char, spot1, spot2, spot3):
# #   if board[spot1] == char and board[spot2] == char and board[spot3] == char:
# #     return True
# #
# # def checkAll(char):
# #   if winner(char,0,1,2):
# #     return True
# #   elif winner(char,3,4,5):
# #     return True
# #   elif winner(char,6,7,8):
# #     return True
# #   elif winner(char,0,3,6):
# #     return True
# #   elif winner(char,1,4,7):
# #     return True
# #   elif winner(char,2,5,8):
# #     return True
# #   elif winner(char,0,4,8):
# #     return True
# #   elif winner(char,2,4,6):
# #     return True
# #
# # game = True
# # while game:
# #   user_input = int(input("Enter a no between 1-9: "))
# #
# #   if board[user_input - 1] != "X" and board[user_input - 1] != "O":
# #     board[user_input - 1] = "X"
# #
# #     # *# checks if user wins*
# #
# #     if checkAll("X") == True:
# #       print("-- X wins ---")
# #       break
# #
# #     finding = True
# #
# #    # *# if user inputs that is already taken*
# #
# #   else:
# #     print(" ")
# #     print("Input is already taken")
# #     print(" ")
# #     finding = False
# #
# #
# #
# #   while finding:
# #     comp_input = random.randint(1, 9)
# #     if board[comp_input-1] != "X" and board[comp_input-1] != "O":
# #       board[comp_input - 1] = "O"
# #
# #       # *# checks if comp wins*
# #
# #       if checkAll("O") == True:
# #         print("-- O wins ---")
# #         break
# #       display()
# #       finding = False
#
#
# # logFile = "list.txt"
# #
# # with open(logFile) as f:
# #     content = f.readlines()
# #
# # # you may also want to remove empty lines
# # content = [l.strip() for l in content if l.strip()]
# #
# # # flag
# # nextLine = False
# #
# # # list to save the lines
# # textList = []
# #
# # for line in content:
# #     find_TC = line.find('TC')
# #
# #     if find_TC > 0:
# #         nextLine = not nextLine
# #     else:
# #         if nextLine:
# #             pass
# #         else:
# #             textList.append(line)
# #
# # print('\n')
# # print('Text list ..')
# # print(textList)
# #
# # j = 0
# # for i in range(j, len(textList)):
# #     if j < len(textList):
# #         print(textList[j], textList[j + 1])
# #         j = j + 2
#
# points_dictionary = {
#         'A': 1, 'B': 3, 'C': 3,
#         'D': 2, 'E': 1, 'F': 4, 'G': 2,
#         'H': 4, 'I': 1, 'J': 8, 'K': 5,
#         'L': 1, 'M': 3, 'N': 1, 'O': 1,
#         'P': 3, 'Q': 10, 'R': 1, 'S': 1,
#         'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
#         'Y': 4, 'Z': 10, '#': 0, '0':3
#     }
#
# currwords = ['PEARS', 'MANGO', 'ORANGE']
# sumsOfwords = []
# sum = 0
# i = -1
# for words in currwords:
#     for word in words:
#         if words == currwords[i + 1]:
#             sum = sum + points_dictionary[word]
#         else:
#             sumsOfwords.append(sum)
#             sum = 0
#             sum = sum + points_dictionary[word]
#             i = i + 1
#
# sumsOfwords.append(sum)
# # print(sumsOfwords)
# #
# #
# # dictionary = list(zip(currwords, sumsOfwords))
# # print(dictionary)
#
# # Num = int(input("Enter a large number: "))
# #
# # if Num == 9:
# #    print("Invalid Input")
# #    exit()
# # else:
# #     Num2 = Num + 10
# #     print("If I added 10 to your number it would be:", Num2)
# #     print("The new number times 2 would be ", Num2 * 2)
# #     count = 0
# #     number = Num
# #     while (number > 1):
# #         number = number // 10
# #         count = count + 1
# #         i = 1
# #         for i in range(1, count + 1):
# #             Num = Num + 1 * (10 ** i)
# #         i = i + 1
# #     print("adding one to every digit on your first number would be: ", Num + 1)
# import sys
#
# # string = '[[Date1,Date2,Number1,Number2],[28Dec2018,29Dec2018,1.24,5]]'
# # print(string)
# #
# # st = string.strip("[]").replace("[", "").replace("]", "").split(",")
# # listA = []
# # listB = []
# #
# # c = 0
# # for s in st:
# #     c = c + 1
# #     if c <= 4:
# #         if s.isdigit():
# #           listA.append(int(s))
# #         elif re.match("^\d+?\.\d+?$", s):
# #             listA.append(float(s))
# #         else:
# #             listA.append(s)
# #     else:
# #         if s.isdigit():
# #             listB.append(int(s))
# #         elif re.match("^\d+?\.\d+?$", s):
# #             listB.append(float(s))
# #         else:
# #             listB.append(s)
# #
# # print(([listA, listB]))
# #
# # # print(str(string.strip("[]").split(",")))
# # import yaml
# # # print(yaml.load(string))
# #
# # # searchString = 'Anday Wala Burger'
# # #
# # # with open('list.txt') as input:
# # #     try:
# # #         for line in input:
# # #             if searchString in line:
# # #                print(next(input), end='')
# # #     except StopIteration:
# # #             pass
# #
# #
# # searchString = 'Anday Wala Burger'
# #
# # logFile = "list.txt"
# #
# # with open(logFile) as f:
# #     content = f.readlines()
# #
# # # you may also want to remove empty lines
# # content = [l.strip() for l in content if l.strip()]
# #
# # # flag
# # nextLine = False
# #
# # # list to save the lines
# # textList = []
# #
# # for line in content:
# #
# #     if searchString in line:
# #         nextLine = not nextLine
# #     else:
# #         if nextLine:
# #             print(line)
# #             nextLine = not nextLine
# #         else:
# #             pass
#
# # import pandas as pd
# #
# # initial_data1 = []
# # initial_data2 = []
# # initial_data3 = []
# #
# # line_num = 1
# # with open ("list.txt") as f:
# #     content = f.readlines()
# #     for line in content:
# #         if line_num == 1:
# #             initial_data1.append(line.split(","))
# #         elif line_num == 2:
# #             initial_data2.append(line.split(","))
# #         elif line_num == 3:
# #             initial_data3.append(line.split(","))
# #
# #         line_num = line_num + 1
# #
# # print(initial_data1)
# # print(initial_data2)
# # print(initial_data3)
# #
# #
# #
# # df = pd.read_csv("data.csv")
# # heads = ['head1','head2','head3','head4','head5','head6','head7','head8','head9','head10']
# #
# # appending_line = 0
# # for index, row in df.iterrows():
# #         if appending_line == 0:
# #             initial_data = initial_data1
# #         elif appending_line == 1:
# #             initial_data = initial_data2
# #         elif appending_line == 2:
# #             initial_data = initial_data3
# #         j = 0
# #         k = 0
# #         appending_line += 1
# #         for i in range(0, len(heads)):   # for the number of heads
# #                 if str(row[heads[i]]) == " ":
# #                     print("FOUND EMPTY COLUMN: ", heads[i])
# #                     print("APPENDING VALUE: ", initial_data[j][k])
# #                     row[heads[i]] = initial_data[j][k]
# #                     k += 1
# #         df.to_csv("tem.csv")
#
#
#
# import re
# pattern = r'([a-z]*[A-Z]+[a-z]*){4}.*'
# function_string = "text text text, more text -- Some More Texty Text Text better manage their online privacy needs  -- Another line of Text in foster programs  LONDON, UK. January 28, 2019-- More example of text, lots of text, Text text. Imagine this is a long article... blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah."
#
# print(re.findall(pattern, function_string))
#
#

# #
# # exit()
#
# # find the repeating numbers for lis1
# # dict_ = {x:lis1.count(x) for x in lis1}
# #
# # for key, val in dict_.items():
# #     if val > 1:
# #         print(key, "repeating for ", val, " times")
# #         # check difference
# #
# #         # find the index of repeating elements
# #         for i in range(0, val):
# #             print(lis1.index(key))
# #             # comparing
# #             # if lis2[lis1.index(key)] < lis2[lis1.index()]
#

# startHour = ''
# startMinute = ''
#



#list of unique columns

from itertools import groupby, chain

# logFile = "tem.csv"
# array = []
# import csv
#
# with open("tem.csv", "r+") as fin:
#     for row in csv.reader(fin):
#         array.append(row[1:])
#
# dd = {k: 0 for k in dict(array).keys()}
# for x in array: dd[x[0]] += int(x[1])
# print(dd)
#
#
# print([[k,v] for k,v in  dd.items()])
# new_dict = {}
# for e in array:
#     print(e[1])

# cost = [[]]*len(car_t)
#
# k = 0
# s = 0
# for ind in range(len(car_t)):
#     print("Matching:", car_t[k])
#     for car_type in array:
#             if car_type[1] == car_t[k]:
#                 # cost.append(row2[2])
#                 print(car_t[k], "matched")
#                 s = s + int(car_type[2])
#                 print(s)
#             else:
#                 print("not matched")
#     k = k + 1
# print(s)

# with open("tem.csv", "r+") as fin:
#     k = 0
#     print(car_t)
#
#     for ind in range(len(car_t)):
#         print("Matching:", car_t[k])
#         for row2 in csv.reader(fin):
#                 if row2[1] == car_t[k]:
#                     # cost.append(row2[2])
#                     print(car_t[k], "matched")
#                     cost = cost + int(row2[2])
#                 else:
#                     print("not matched")
#         k = k + 1
#     print(cost)
#
# import os
# print(os.path.isdir("/home/el"))
# print(os.path.exists("/home/el/myfile.txt"))

# method with two params a key and a  list
import requests
from bs4 import BeautifulSoup
import urllib

# page = requests.get("https://in.udacity.com/courses/all")
# soup = BeautifulSoup(page.content, 'html.parser')
# courses = soup.find_all("a", class_="capitalize")

# from PIL import Image, ImageDraw, ImageFont
#
#
# def getSize(txt, font):
#     testImg = Image.new('RGB', (1, 1))
#     testDraw = ImageDraw.Draw(testImg)
#     return testDraw.textsize(txt, font)
#
# fontname = "Arial"
# fontsize = 400
# text = "Hello World"
#
# colorText = "black"
# colorOutline = "red"
# colorBackground = "white"
#
#
# font = ImageFont.truetype(fontname, fontsize)
# width, height = getSize(text, font)


#
# candidates = ['Donald', 'Barack', 'Hillary', 'Mitt']
# votes = [9, 7, 1, 3]
#
# print(sorted(zip(candidates, votes), reverse=True))

# import requests
# from bs4 import BeautifulSoup
#
# library_list = []
#
# data = {'action' : 'LibSearch', 'termtype' : 'Keyword', 'libstate' : 'NSW', 'dosearch' : 'Search', 'libtype' : 'All', 'chunk' : 100}
#
# page = requests.get("http://www.nla.gov.au/apps/libraries/", params=data)
# soup = BeautifulSoup(page.content, 'html.parser')
#
#
# libraries = soup.find_all("a")
#
#
# for library in libraries[5:]:
#     print(library.text)
#     # library_list.append(library.text)

# from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# account_sid = 'AC914a555abeaaa7f474854e61f78d98a1'
# auth_token = 'cc6b74b7b18d6201642717bdbd72ceb1'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#                               body='Hello BABA YAGA!!',
#                               from_='whatsapp:+14155238886',
#                               to='whatsapp:+60149224421'
#                           )
#
# print(message.sid)

# import re
# logFile = "list.txt"
#
# with open(logFile) as f:
#     content = f.readlines()
#
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
#
# pattern = re.compile(r'\s+')
#
# for line in content:
#     find_person = line.find('person')
#     find_car = line.find('car')
#
#     if find_person > 0:
#         line = line.replace("person", "person\n")
#     if find_car > 0:
#         line = line.replace("car", "car\n")
#
#     print(line)


# logFile = "list.txt"
#
# with open(logFile) as f:
#     content = f.readlines()
#
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
#
# dict_ = {}
# dict_list = []
# for line in content[1:]:
#     l = line.split("{", 1)[1].strip("}")
#     dict_list.append(l)

# print(dict_list)

# print(dict_list[0].split(":", 1)[1].replace('"', " "), end = "")

# print(dict_list[1].split(":", 1)[1].replace('"', " "), end = "")
#
# print(dict_list[2].split(":", 1)[0].replace('"', " "), end="")
#
# print(dict_list[3].split(":", 1)[0].replace('"', " "))

# print("name \t", end="")
# print("cx \t\t", end="")
# print("cy \t\t", end="")
# print("r \t", )
# for elem in dict_list:
#     x = elem.split(",")
#     print(x[0].split(":", 2)[1].replace('"', " "), end = "")
#
#     print(x[1].split(":", 2)[1].replace('"', " "), "\t", end = "")
#
#
#     print(x[2].split(":", 2)[1].replace('"', " "), "\t", end = "")
#
#     print(x[3].split(":", 2)[1].replace('"', " "), "\t")




input_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
index=0

# for n in range(int(len(input_data)/8)):
#         v1=input_data[n+index]
#         x1=input_data[n+1+index]
#         y1=input_data[n+2+index]
#         z1=input_data[n+3+index]
#         v2=input_data[n+4+index]
#         x2=input_data[n+5+index]
#         y2=input_data[n+6+index]
#         z2=input_data[n+7+index]
#         index+=7
#
# start_index = -8
# print(input_data[start_index:])
#
# vars_list = []
# for i in range(start_index, 0):
#     vars_list.append(input_data[i])
#
#
# print(vars_list[0])
# print(vars_list[1])
# print(vars_list[2])
# print(vars_list[3])
# print(vars_list[4])
# print(vars_list[5])
# print(vars_list[6])
# print(vars_list[7])

# test_list = ['1. First Message', '2. Second Message (edited)', '3. Third Message (edited)', '4. Forth Message (edited)', '5. Fifth Message (edited)']

# new_list = []
# for t in test_list:
#     if 'edited' in t:
#         t = t + ' marked'
#         new_list.append(t)
#     else:
#         new_list.append(t)
#
# print(new_list)

# for t in test_list[:]:
#     print(t)
#     if 'edited' in t:
#         test_list.remove(t)
#
# print(test_list)
# print(list(filter(lambda a: a != '(edited)', test_list[:])))

# import requests
# from bs4 import BeautifulSoup
# import urllib
#
# test = '''<div>text_0<ul>
#      <li>text_1</li>
#      <li>text_2</li>
#      <li>text_3</li>
#   </ul>
# </div>'''
#
# soup = BeautifulSoup(test, 'html.parser')
# data = soup.find_all("div")
# # for d in data:
# #     print(d.text)
#
#
# import lxml.html as LH
#
# content = '''<div>text_0<ul>
#      <li>text_1</li>
#      <li>text_2</li>
#      <li>text_3</li>
#   </ul>
# </div>'''
# root = LH.fromstring(content)
# for elem in root.xpath('//div/descendant::text()'):
#     print(elem)


# logFile = "list.txt"
#
# with open(logFile) as f:
#     content = f.readlines()
#
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
#
# zeros = 0
# ones = 0
# for line in content:
#     val = line.split('[', 1)[1].split(']')[0]
#     if val == '0':
#         zeros+= 1
#     elif val == '1':
#         ones += 1
# print("Number of zeros {}".format(zeros))
# print("Number of ones {}".format(ones))


# d = {k**2: v for (k, v) in d.items()}
# from bs4 import BeautifulSoup
#
# test = '''<tr> <td class="date"><nobr>01-Jan-2019</nobr></td>
# <td class="number">10881.70</td>
# <td class="number">10923.60</td>
# <td class="number">10807.10</td>
# <td class="number">10910.10</td>
# <td class="number">159404542</td>
# <td class="number">8688.26</td>
# </tr>'''
#
# soup = BeautifulSoup(test, 'html.parser')
# number = soup.find("nobr")
# data = soup.find_all("td", class_ ="number")
# data_list = []
# for n in number:
#     data_list.append(n)
#     for d in data:
#         data_list.append(d.text)
#
# print(data_list)


# logFile = "list.txt"
#
# with open(logFile, encoding="utf8") as f:
#     content = f.readlines()
#
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
#
#
# # list to save the lines
# conv_list = []
#
# Dear = 'Dear'
# Regards = 'Regards'
#
# for line in content:
#     line = line.split(Dear)[-1].split(Regards)[0]
#     print(line)


# from bs4 import BeautifulSoup
# with open('list_test.xml','r') as f:
#     soup = BeautifulSoup(f.read(), features="lxml")
#     aid = soup.find_all('aid')
#     for s in aid:
#         if s.text == 'sk-log':
#             vn = s.find_next('vn')
#             print("Original Value: {}".format(vn.text))
#             vn.string = 'SomeValue'
#             print("Replaced value: {}".format(vn.text))
#
# with open("list_test.xml", "w") as f_write:
#     f_write.write(soup.prettify())

logFile = "list.txt"

# with open(logFile, "r+") as f:
#     content = f.readlines()
#
#     # you may also want to remove empty lines
#     content = [l.strip() for l in content if l.strip()]
#
#     # list of new Values
#     newVal_list = [23,54,67,19.43,4]
#     i = 0
#     for line in content:
#         find_TC = line.find('=')
#         if find_TC > 0:
#             x = line.split('=', 1)[1]
#             line = line.replace(x,str(newVal_list[i]))
#             print("Old Value: {}, New Value: {}".format(x, newVal_list[i]))
#             i += 1

from gensim.models import word2vec

# def word2vec(word):
#     from collections import Counter
#     from math import sqrt
#
#     # count the characters in word
#     cw = Counter(word)
#     # precomputes a set of the different characters
#     sw = set(cw)
#     # precomputes the "length" of the word vector
#     lw = sqrt(sum(c*c for c in cw.values()))
#
#     # return a tuple
#     return cw, sw, lw
#
# def cosdis(v1, v2):
#     # which characters are common to the two words?
#     common = v1[1].intersection(v2[1])
#     # by definition of cosine distance we have
#     return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]
#
#
# list_of_keywords = ['allergy', 'something']
# Sentence = 'a severe allergic reaction to nuts in the meal she had consumed.'
#
# threshold = 0.80
# for key in list_of_keywords:
#     for word in Sentence.split():
#         try:
#             # print(key)
#             # print(word)
#             res = cosdis(word2vec(word), word2vec(key))
#             # print(res)
#             if res > threshold:
#                 print("Found a word with cosine distance > 80 : {} with original word: {}".format(word, key))
#         except IndexError:
#             pass
# # print([word for word in Sentence if word in list_of_keywords])
#
# print([word for word in Sentence if cosdis(word2vec('allergy'), word2vec(word)) > 0.8])

# students={
# 's1' : {"pup1": "001", "s1": 10, "s2": 20},
#
# 's2' : {"pup2": "124", "s1": 20, "s2": 30},
#
# 's3' : {"pup3": "125", "s1": 30, "s2": 40}
# }
#
# for my_var in students:
#    students[my_var]['s1'] += 5
#    print(my_var, 'corresponds to', students[my_var])


# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return F(n-1)+F(n-2)
#
# print(F(100))

# people = ['Jonas', 'Julio', 'Mike', 'Mez']
# ages = [25, 30, 31, 39]
# nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
# for data in zip(people, ages, nationalities):
#     person, age, nationality = data
#     print(data)
#
#
# urls = ['https://xxxxxxxx.com/getNamesEnc02Motasel2.php?keyword=JOHN&type=2&limit=6000"',
# 'https://xxxxxxxx.com/getNamesEnc02Motasel2.php?keyword=SAM&type=2&limit=9000"',
# 'https://xxxxxxxx.com/getNamesEnc02Motasel2.php?keyword=JOHN&type=2&limit=1000"',
# 'https://xxxxxxxx.com/getNamesEnc02Motasel2.php?keyword=HARRY&type=2&limit=7000"']
#
# for url in urls:
#     r = requests.get(url)
#     cont = json.loads(r.content)
#     print(cont)

# from bs4 import BeautifulSoup, SoupStrainer
# import requests
# import json
#
# url = "https://www.lazada.com.my/oldtown-white-coffee/?langFlag=en&q=All-Products&from=wangpu&pageTypeId=2"
#
# page = requests.get(url)
# data = page.text
# soup = BeautifulSoup(data)
#
#
# scripts = soup.find_all('script')
#
# jsonObj = None
# for script in scripts:
#     if 'window.pageData=' in script.text:
#         jsonStr = script.text
#
#         jsonStr = jsonStr.split("window.pageData=")[1]
#         jsonObj = json.loads(jsonStr)
#
#
# products = jsonObj['mods']['listItems']
#
# for item in products:
#     print (item['productUrl'])

# Game = 1
#
# if  Game == "1":
#     username = input("Please enter your username: ")
#     if re.search(r'\bf\b', 'Fof')
#     if username in open("Names.txt").read(): #fix
#             print ("Welcome " + username)
#             password = input("Please enter your password: ")
#             if password in open("Passwords.txt").read():
#                     print ("success!")
#     else:
#                     print("Username incorrect!")

# import re
# if re.search(r'\bf\b', 'Fof')



# import re
#
# def atoi(text):
#     return int(text) if text.isdigit() else text
#
# def natural_keys(text):
#     '''
#     alist.sort(key=natural_keys) sorts in human order
#     http://nedbatchelder.com/blog/200712/human_sorting.html
#     (See Toothy's implementation in the comments)
#     '''
#     return [ atoi(c) for c in re.split(r'(\d+)', text) ]
#
# alist = ['Tree', 'Plant', 'Bird', '7animal', 'Beta', '4qwerty']
#
# alist.sort(key=natural_keys)
# print(alist)

# headers = [('id',), ('attr_1',), ('attr_2',)]
#
# test_tup = [(111, 222, 333), ('aaa', 'bbb', 'ccc'), ('a1', 'b2', 'c3')]
# res = list(zip(*test_tup))
#
# print('; '.join(' '.join(str(x) for x in i) for i in headers))
# print('\n'.join('; '.join(str(x) for x in i) for i in res))


# Matrix_2 = []
#
# for arr in Matrix:
#      # arr=arr.split()
#      arr=[map(lambda x:int(x),arr)]
#      Matrix_2.append(arr)
#
# print(list(map(int,Matrix_2)))

# starting dictionary

# from tkinter import *
# top=Tk()
# t = [("1","2","3","4","5"),("aa","bb","cc","dd","ee"),("!@","%^","&*","@#","@$"),("A","B","C","D","E")]
#
# for x in range(4):
#     for y in range(5):
#             w = Text(top, width=15, height=2)
#             w.grid(row=x,column=y)
#             w.insert(END, t[x][y])
#
# top.state("zoomed")
# top.mainloop()

# ticket_start_time = str(info1[11][11:])
# import dateutil.parser as dparser
# dt_1 = '01-04-2019 11:52:26 GMT 5.0'
# print("Date: {}".format(dparser.parse(dt_1,fuzzy=True).date()))
# print("Time: {}".format(dparser.parse(dt_1,fuzzy=True).time()))


# from bs4 import BeautifulSoup
# import urllib
#
# test = '''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
#     <soap:Body>
#         <LoginResponse xmlns="http://tempuri.org/">
#             <LoginResult>true</LoginResult>
#             <aSessionID>AF-6A-51-FD-E6-8D-C8-12-AB-7E-C1-BD-50-7A-43-D0-AA-27-15-CA</aSessionID>
#         </LoginResponse>
#     </soap:Body>
# </soap:Envelope>'''
#
# soup = BeautifulSoup(test, 'html.parser')
# data = soup.find_all("LoginResult")
#
# for d in data:
#     desired_tag = d.find("aSessionID")
#     print(desired_tag.text)

#
# from xml.dom import minidom
#
# doc = minidom.parse('list_test.xml')
# MasterManifest = doc.getElementsByTagName('MasterManifest')
# print(len(MasterManifest))
# for sess in MasterManifest:
#     print(sess)
#
# for x in MasterManifest.childNodes:
#     if x.nodeType == minidom.ELEMENT_NODE:
#         print(x.tagName, x.childNodes[0].data)


# import xml.dom.minidom as md
#
# root = md.parse('list_test.xml')
# from xml.dom.minidom import Node
# Manifests = root.getElementsByTagName('MasterManifest')
# for elem in Manifests:
#     try:
#         for x in elem.childNodes:
#             if x.nodeType == Node.ELEMENT_NODE:
#                  print(x.tagName, ": ", x.childNodes[0].data)
#         print('\n')
#     except IndexError:
#         pass


# import numpy as np
#
# dst = np.array([[1,2], [3,4]])
#
# print(0.5 * dst.max())
#
# print((dst <= 0.5 * dst.max()))

#
# from xml.etree import ElementTree
# tree = ElementTree.parse('list_test.xml')
# root = tree.getroot()
#
# items = root.findall("LoginResult")
# company = root.findall('.//aSessionID').text
# print(company)
# for elem in items:
#     desired_tag = elem.find("aSessionID")
#     print(desired_tag.text)
#
# import requests
# from bs4 import BeautifulSoup
# import urllib
#
# page = requests.get("https://www.rottentomatoes.com/m/the_lord_of_the_rings_the_return_of_the_king")
# soup = BeautifulSoup(page.content, 'html.parser')
# section = soup.find_all("div", class_ = "mop-ratings-wrap__half")
# tomato_rating = soup.find_all("span", class_="mop-ratings-wrap__percentage")
# mop_rating = soup.find_all("span", class_="mop-ratings-wrap__percentage mop-ratings-wrap__percentage--audience")
#
# for elem in section:
#     tomato_rat = elem.find("span", class_="mop-ratings-wrap__percentage mop-ratings-wrap__percentage--audience")
#     print(tomato_rating)

# print(tomato_rating)
# print(mop_rating)
import collections
# dict_ = [{'distance': 1.9999,
#   'breakEvenDistance': 1.9329,
#   'max': 0.0010342833053929787},
#  {'distance': 1.9251,
#   'breakEvenDistance': 2.0669999999999997,
#   'max': 0.0011183923895419084,
#   'min': 0.0010342833053929787},
#  {'distance': 1.8802,
#   'breakEvenDistance': 1.6758,
#   'max': 0.0011927892918825562,
#   'min': 0.0011183923895419084},
#  {'distance': 1.8802,
#   'breakEvenDistance': 1.5956,
#   'max': 0.0012522046577102665,
#   'min': 0.0011927892918825562}]

# for x in dict_:
#     print(x['max'])
# print([x for x in dict_ if not any(y in x for y in str(x["max"]))])
# print([element for element in dict_ if el])
#

# from ast import literal_eval
# print(np.array(literal_eval(lst)))
# print([list(lst) for lst in literal_eval(lst)])
# from xlrd import open_workbook
# from webcolors import rgb_to_name
#
# wb = open_workbook('cel_lis.xls', formatting_info=True)
# sh = wb.sheet_by_name('Sheet1')
#
#
# def getBGColor(book, sheet, row, col):
#     xfx = sheet.cell_xf_index(row, col)
#     xf = book.xf_list[xfx]
#     bgx = xf.background.pattern_colour_index
#     pattern_colour = book.colour_map[bgx]
#
#     #Actually, despite the name, the background colour is not the background colour.
#     #background_colour_index = xf.background.background_colour_index
#     #background_colour = book.colour_map[background_colour_index]
#
#     return pattern_colour
#
# rgb_Col = getBGColor(wb, sh, 0, 0)
# print("The RGB value of the cell is: {} which is equivalent to {}".format(rgb_Col, rgb_to_name(rgb_Col)))
# import ast
# import pandas as pd
#
# print(pd.DataFrame([ast.literal_eval(line.strip(" ").split(" ")) for line in open("list.txt")]))


# import PyPDF2
#
# path="C:\\Users\\munir.khan\\Documents\\test\\ERP PRoject requirements.pdf"
# text=""
# pdf_file = open(path, 'rb')
# text =""
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# c = read_pdf.numPages
# for i in range(c):
#      page = read_pdf.getPage(i)
#      text+=(page.extractText())

# def Colors(col):
#     if col == 'blue':
#         return 24
#     elif col == 'red':
#         return 18
#     elif col == 'green':
#         return 2
#     elif col == 'teal':
#         return 6
#
# quant = int(input('How many variable inputs do you want? (integer only)\n'))
# value = 1
# trial = 0
# while trial < quant:
#     col = (input('Please enter color for input #' + str(trial+1) + '\n'))
#     trial += 1
#     value *= Colors(col)
# value = value**(1./quant)
# print(value)


# import heapq
#
# heap = []
# a = (321,4)
# b = (258,3)
# heapq.heappush(heap,a)
# heapq.heappush(heap,b)
# print(heap)
#
# if 4 in heap:
#     print("found")
# else:
#     print("not found")


# import heapq
# heap = []
# heapq.heappush(heap, (1, 'A'))
# heapq.heappush(heap, (3, 'C'))
# heapq.heappush(heap, (2, 'B'))
#
# print('A' in [k for v, k in heap])
# import os
# path = 'D:\\test2'
# for filename in os.listdir(path):
#     with open(filename, 'r', encoding="latin-1") as fileObj:
#         print("Row Counted  {} in the csv {}:".format(len(fileObj.readlines()) - 1, filename))   # -1 to exclude the header



from itertools import cycle
import numpy as np
from itertools import zip_longest
from itertools import product
# st1=["a","b","c"]
# st2=["likes","dislikes","loves"]
# st3=["programming","math","bio"]

# print([st1[i]+" "+st2[i]+" "+st3[i] for i in range(len(st1))])



# import requests
# from bs4 import BeautifulSoup
#
# page = requests.get("https://www.ntu.edu.sg/events/Pages/default.aspx")
# soup = BeautifulSoup(page.content, 'html.parser')
#
# events_absAll = soup.find_all("div",{"class": "ntu_event_detail"})
# for events in events_absAll:
#     for a in events.find_all('a'):
#         print(a.text.strip())


# item_no = []
# max = 0
# for i in range(5):
#     itemno = int(input("Enter an item number: "))
#     item_no.append(itemno)
# for i in item_no:
#     if i > max:
#         max = i
# high = item_no.index(max)
# print(high)
# print (item_no[high])

# item_no = [5, 6, 7, 8, 8]
# counter = item_no.count(max(item_no))
# print([max(item_no) for x in range(counter)])
#
# for i in range(counter):
#     print(max(item_no), end = " ")

# import time
# from PIL import ImageGrab
# start = int(time.time())
# while True:
#
#     if int(time.time()) % 2 == 0:
#         img = ImageGrab.grab()
#         saveas = 'screenshot' + str(int(time.time())) + '.png'
#         img.save(saveas)
#
#     elif start + 30 == int(time.time()):
#         break

# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://fs.blog/mental-models/'
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# nList = []
# divTag = soup.find_all("div", {"class": "rte"})
# for tag in divTag:
#     pTags = tag.find_all('p')
#     nList.append(pTags[tag].text)
#     # for tag in pTags[:-2]:  # to trim the last two irrelevant looking lines
#         # print(tag.text)
#
# print(nList)


# logFile = "list.txt"
#
# with open(logFile) as f:
#     content = f.readlines()
#
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
# dict_ = {}
# line_num = 1
# for line in content:
#     dict_[line_num] = line
#     line_num += 1
# print(dict_)

# sum = 0
# for e in dict_:
#     sum += float(dict_[e].split(",")[0])
#     print(float(dict_[e].split(",")[0]))
#
# print(sum)
#
# dict_ = {1: ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'], 2: ['4.9', '3.0', '1.4', '0.2', 'Iris-setosa'], 3: ['4.7', '3.2', '1.3', '0.2', 'Iris-setosa'], 4: ['4.6', '3.1', '1.5', '0.2', 'Iris-setosa'], 5: ['5.0', '3.6', '1.4', '0.2', 'Iris-setosa'], 6: ['5.4', '3.9', '1.7', '0.4', 'Iris-setosa'], 7: ['4.6', '3.4', '1.4', '0.3', 'Iris-setosa']}
#
#
# print(sum([float(dict_[e][0]) for e in dict_]))


# print(sum([float(dict_[k][0]) for k in dict_]))



# import os
# import shutil
# folder = "C:/Users/munir.khan/Documents/test"
# # for filename in glob.iglob(os.path.join(folder, '*.')):
# for filename in os.listdir(folder):
#     print(filename.split(".")[1])
#     # os.rename(os.path.join(folder,filename), filename[:-4] + '.txt')
#
# import os
# [os.rename(x, x.replace(filename.split(".")[1], 'txt')) for x in os.listdir(folder)]

# import requests
# from bs4 import BeautifulSoup
#
# page = requests.get("https://www.ntu.edu.sg/events/Pages/default.aspx")
# soup = BeautifulSoup(page.content, 'html.parser')
#
# events_absAll = soup.find_all("div",{"class": "ntu_event_detail"})


# import requests
# from bs4 import BeautifulSoup
#
# page = requests.get("https://en.wikipedia.org/wiki/List_of_companies_of_Indonesia")
# soup = BeautifulSoup(page.content, 'html.parser')
# ta = soup.find_all('table',class_="wikitable")
#
# for e in ta:
#     print(e)


dir_score = [('../dir_a/1.png', 5.14),
 ('../dir_a/2.png', 5.15),
 ('../dir_b/3.png', 4.19),
 ('../dir_b/4.png', 3.81)]


import os, itertools
# print([list(g) for _, g in itertools.groupby(dir_score, lambda x: x[0][0].split('/')[1])])


# import itertools
# import operator
#
# L = [('grape', 100), ('grape', 3), ('apple', 15), ('apple', 10),
#      ('apple', 4), ('banana', 3)]
#
# def accumulate(l):
#     it = itertools.groupby(l, operator.itemgetter(0))
#     for key, subiter in it:
#        yield key, sum(item[1] for item in subiter)


#
# from bs4 import BeautifulSoup
# a = "images src <img src=\"http://aa/6.png\" /> <img src=\"http://aa/7.png\" /> "
# soup = BeautifulSoup(a, 'html.parser')
# images = soup.findAll('img')
# src_list = []
# for image in images:
#     src_list.append(image['src'])
#     print(image)
#
# import re
# matches = re.search('src="([^"]+)"',a)
# print(matches[0])


#
# from bs4 import BeautifulSoup
#
#
# data = {}
# a = "images src <img src=\"http://aa/6.png\" /> <img src=\"http://aa/7.png\" /> "
# soup = BeautifulSoup(a, 'html.parser')
# page_images = [image["src"] for image in soup.findAll("img")]
#
# content = a.split("<")[0]
# data['content'] = content
# data['src'] = page_images
#
# print(data)

# import re
#
# data = {}
# a = "images src <img src=\"http://aa/6.png\" /> <img src=\"http://aa/7.png\" /> "
# content = a.split("<")[0]
#
# data['content'] = content
# if re.search('src="([^"]+)"',a):
#   data['src'] = re.findall ( 'src="(.*?)"', a, re.DOTALL)
#
# print(data)


#
# order_response = {
# "orders": [
#     {
#         "id": "450789469",
#         "email": "bob.norman@hostmail.com",
#         "location_id": 487838322,
#         "order_value": [
#             {
#                 "id": 123,
#                 "asd": "asd"
#             }, {
#                 "id": 234,
#                 "asd": "sd"
#             }
#         ],
#         "line_items": [
#             {
#                 "id": 466157049,
#                 "variant_id": 39072856,
#                 "title": "IPod Nano - 8gb",
#                 "product_id": 632910392,
#             }, {
#                 "id": 466157050,
#                 "variant_id": 39072856,
#                 "title": "IPod Nano - 8gb",
#                 "product_id": 632910392,
#             }
#         ]
#     }, {
#         "id": "450789469",
#         "email": "bob.norman@hostmail.com",
#         "location_id": 487838323.00,
#         "order_value": {
#             "id": 123,
#             "asd": "asd"
#         },
#         "line_items": {
#             "id": 466157052,
#             "variant_id": 39072856,
#             "title": "IPod Nano - 8gb",
#             "product_id": 632910392,
#         }
#     }, {
#         "id": "450789469",
#         "email": "bob.norman@hostmail.com",
#         "location_id": float('nan'),
#         "order_value": {
#             "id": 123,
#             "asd": "asd"
#         },
#         "line_items": {
#             "id": 466157052,
#             "variant_id": 39072856,
#             "title": "IPod Nano - 8gb",
#             "product_id": 632910392,
#         }
#     },
# ]
# }
# # import pandas as pd
# # order_df = pd.DataFrame(order_response["orders"])
# # print (order_df)
# #
# # cols_to_flatten = []
# # for col in order_df.columns:
# #     if isinstance(order_df[col].any(), list):
# #         cols_to_flatten.append(col)
# #
# # print (cols_to_flatten)
#
#
# def removeZeros(ip):
#     # splits the ip by "."
#     # converts the words to integeres to remove leading removeZeros
#     # convert back the integer to string and join them back to a string
#     new_ip = ".".join([str(int(i)) for i in ip.split(".")])
#     return new_ip
#
# logFile = "list.txt"
# with open(logFile) as f:
#     content = f.readlines()
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
# ipList = []
# stList = []
# for line in content:
#     stList.append(line[1:].split(" ")[1])
#     line = line[1:].split(" ")[0]
#     print(line)
#     line =  removeZeros(line).replace(removeZeros(line).split(".", 2)[1],removeZeros(line).split(".", 2)[1][:-2] + ".0")
#     ipList.append(line)
#     print(line)
#
#
# print(stList)
# print(ipList)
# zipList = zip(ipList, stList)
#
# with open(logFile, "w") as f:
#     for index in range(len(ipList)):
#         f.write(str(ipList[index]) + " " + str(stList[index]) + "\n")

# import urllib.request
# x = urllib.request.urlopen('https://www.google.com/')
# print(x.read())
#
# import requests
# page = requests.get("https://www.google.com/")
# print(page.content)

# logFile = "list.txt"
# with open(logFile) as f:
#     content = f.readlines()
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
#
# searchStr = 'Commit message'
# commitMsg = ''
# for line in content:
#     if searchStr in line:
#         print(line.replace('"', '')[:-1])
#         commitMsg = line.replace('"', '').split(": ")[1][:-1]
#
# print(commitMsg)


# words = ['Bien', '*', 'venue', 'pour', 'les','engage', '*', 'ment','trop', 'de', 'YIELD', 'peut','être','contre', '*', 'productif' ]
#
# option= int(input("option: "))
# iplist=['192.168.1.1', '192.168.1.2', '192.168.1.254']

import random

from bs4 import BeautifulSoup
import urllib
#
# list_I = [123, 453, 444, 555, 123, 444]
#
# list_II = ['A', 'A', 'B', 'C', 'A', 'B']
#
# res = {}
#
# for elem, elem2 in zip(list_I, list_II):
#     res[elem] = elem2
#
# print(res)
#
# print([k for k,v in res.items()])
# print([v for k,v in res.items()])

import copy

# j_data = {
#     "persons":
#         {
#             "city": "Seattle",
#             "name": "Brian"
#         },
#     "cars":
#         {
#             "car1": "Tesla",
#             "car2": "Toyota"
#         }
# }
#
# for elem in j_data:
#     j_data[elem] = [j_data[elem]]
#
#
# import pprint
# pprint.pprint(j_data)
from stringcase import camelcase

# message = ['Hey There', 'Just a List', 'Passing by', 'random', 2]
#
# dict_ = {1: 'random', 2: 'Hello', 3: 'World'}
#
# for key, value in dict_.items():
#     if value in message:
#         print(dict_[key])
#
# print([v for k,v in dict_.items() if v in message])
#
# print({elem : dict_[elem] for elem in message if elem in dict_})


# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
#
# maxCount = 0
# for lst in tableData:
#     for elem in lst:
#         if len(elem) > maxCount:
#             maxCount = len(elem)
#
# print(maxCount)
#
# print([max(len(x) for sublist in tableData for x in sublist)])
    # tableData = [['apples', 'oranges', 'cherries', 'banana'],
    #              ['Alice', 'Bob', 'Carol', 'David'],
    #              ['dogs', 'cats', 'moose', 'goose']]
    #
    # maxCount = 0
    # for lst in tableData:
    #     for elem in lst:
    #         maxCount = max(maxCount, len(elem))
    #
    # print(maxCount)



#
# import pandas as pd
#
#
# def f(row):
#     for elem in currency:
#         if elem in row['Currency']:
#              return elem
#
# currency = ['SGD', 'GBP', 'USD', 'EUR']
# data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Currency':['RANDOM_SGD_2017', 'TEST_EUR_1381', 'FORFUN GBP', 'NAs']}
#
# df = pd.DataFrame(data)
# df['Currency_Updated'] = df.apply(f, axis=1)
#
# print(df)


#
# logFile = "list.txt"
#
# with open(logFile) as f:
#     content = f.readlines()
#
# # you may also want to remove empty lines
# content = [l.strip() for l in content if l.strip()]
#
# for line in content:
#     if line.startswith("o"):
#         if str(content[-1]).strip("[']").split()[0] == 'o':
#             print("File is good.")
#         else:
#             print("File is bad.")
#         break
#     else:
#         print("File is bad.")
#         break

#
# import re
# def GetTheSentences(infile):
#      with open(infile) as fp:
#          red = fp.read()
#          count = 1
#          for result in re.findall('o (.*?)o ', red, re.S):
#              print("Response Packet: {}".format(count))
#              print("\n".join(result.split("\n")[1:]))
#              count +=1
#
# GetTheSentences('list.txt')


# def extract_lines(file):
#     scrubbed = [x.strip('\n') for x in open(file, 'r')]
#     return [x for x in scrubbed if x not in ('o','o')]


# print(extract_lines(logFile))

# import re
# def GetTheResponse(file):
#     start_rx = re.compile('o')
#     end_rx = re.compile('o')
#
#     start = False
#     output = []
#     with open(file,) as datafile:
#          for line in datafile.readlines():
#              if re.match(start_rx, line):
#                  start = True
#                  print("Response Packet")
#              elif re.match(end_rx, line):
#                  start = False
#              if start:
#                   if line.startswith('o'):
#                       pass
#                   else:
#                       print(line)
#                       output.append(line)
#
#     return output

# GetTheResponse('list.txt')

# parentDiv = soup.find_all("div", class_="_5rgt _5nk5 _5msi")
# for elem in parentDiv:
#     para = elem.find("p")

# html = '''<div class="_5rgt _5nk5 _5msi" style data-gt="{"tn":"*s"}" data-ft="{"tn":"*s"}"> == $0
#  <span>
#    <p>
#      "Sample paragraph"
#    </p>'''
#
# soup = BeautifulSoup(html, 'html.parser')
# parentDiv = soup.find_all("div", class_="_5rgt _5nk5 _5msi")
# for elem in parentDiv:
#     para = elem.find("p").text
#     print(para.strip())

# d1 = {'primary_key': '01/01/20185511', 'Fecha': '01/01/2018', 'linea': '551', 'Sentido': '1', 'trayecto': '3', 'SA_A_': '0', 'SA_B1': '1', '': '2', 'SA_B3': '3'}
# d2 = {'primary_key': '01/01/20185511', 'Fecha': '01/01/2018', 'linea': '551', 'Sentido': '1', 'trayecto': '4', 'SA_A_': '1', 'SA_B1': '1', 'SA_B2': '2', 'SA_B3': '3'}
# # d3 = {}
#
# select_list = ['SA_A_', 'SA_B1','SA_B2','SA_B3']
# for (k,v), (k2,v2) in zip(d1.items(),d2.items()):
#     if k2 in select_list:
#         # d3[k2] = int(v) + int(v2)
#         print({k2: int(v) + int(v2)})


# print({k2: int(v) + int(v2) for (k,v), (k2,v2) in zip(d1.items(),d2.items()) if k2 in select_list})
# print(d3)


# lst = [["4040", ["4040", "1.04862754", 4]], ["4040.1", ["4040.1", "0.25906621", 1]], ["4040.2", ["4040.2", "0.954", 1]]]
#
# # print({k[0]: k[1:] for k in lst })
#
# # print(dict(lst))
#
# print([{k:v} for k, v in lst])




# def replace_all(text, dic):
#     for i, j in dic.items():
#         text = text.replace(i, j)
#     return text
#
# d = { ":": "_", "(+):": "_+__"}
# mySentence = "name1_22:3-3(+):Pos_bos"
#
# print(replace_all(mySentence, d))

# repls = (':', '_'), ('(+):', '_+__')

# s =  "name1_22:3-3(+):Pos_bos"
# replaceList =  [(":", "_"), ("(", "_"), (")", "__")]
#
# repList = [':','(',')']   # list of all the chars to replace
# rChar = '_'               # the char to replace with
# for elem in repList:
#     s = s.replace(elem, rChar)
# print(s)



# word= input("Enter your string please: ")
# words = ''.join(c if c.isalnum() else ' ' for c in word).split()
# print("Total words: {}".format(len(words)))
#
# print("Total words: {}".format(len(word.split())))
# print("Total Characters: {}".format(len(word)))


# word = input("Enter your string please: ")
#
# print("Total words: {}".format(len(word.split())))
# print("Total Characters: {}".format(len(word)))



#
# tableData = [['red apples', 'apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David', 'Elon'],
#              ['dogs', 'cats', 'moose', 'goose']]
#
#
# print(list(zip(*tableData)))
#
# print(list(zip_longest(*tableData)))


# def dedup(lst):
#     return lst[::-1]   # just to return a reversed lst
#
# listA = [1,2,3]
# listB = [4,5,6]
# listC = [7,8,9]
#
# cList = [listA,listB,listC]
# listA, listB, listC = [dedup(lst) for lst in cList]

# def dedup2(cList):
#     temp = []
#     for e in cList:
#         temp.append(e[::-1])
#     return temp
#
#
#
# def dedup2(cList):
#     # temp = []
#     # for e in cList:
#         # temp.append(e[::-1])
#     # return temp
#
#     return [t[::-1] for t in cList]
#
# listA, listB, listC = dedup2(cList)
# print(listA)
# print(listB)
# print(listC)

# import pandas as pd
#
# data = {'col1':['1', '1', '2', '2', '3', '1','3'], 'col2':['A', 'D', 'R', 'D', 'T', 'R','R'], 'col3':['B', 'R', 'P', 'F', 'G', 'S','S']}
# df = pd.DataFrame(data)
# df = df.drop_duplicates()
#
# print(df)
#
# from bs4 import BeautifulSoup
# import urllib.request as urllib2
# import re
#
# html_page = urllib2.urlopen('https://www.boletinoficial.gob.ar/')
# soup = BeautifulSoup(html_page, "html.parser")

# for td in soup.findAll("div", class_="itemsection"):
#     for h3 in soup.findAll("h3"):
#         for a in h3.findAll("a", href=True):
#             print(a)

# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# url = "https://www.boletinoficial.gob.ar/"
# browser = webdriver.Chrome("C:/Users/michael/Downloads/chromedriver_win32/chromedriver.exe")
# browser.get(url)
# html = browser.page_source
# soup = BeautifulSoup(html, 'lxml')
# a = soup.find('a')
# print(a)


# def chkList(lst):
#     return True if lst in list_of_lists else False
#
# list_of_lists = [[2,2,2,3],[2,3,4],[2,2,6]]
# print(chkList([2,2,6]))



# lol = [['0',1,2,3], [4,5,6,7], [8,9,10,11]]
# print([item for sublist in lol for item in sublist])
#
#
# flattened = []
# for sublist in lol:
#     for item in sublist:
#         flattened.append(item)
#
# print(flattened)
#
# from functools import reduce
# print(reduce(lambda x, y: x + y, lol))
# from iteration_utilities import deepflatten
#
# print(list(deepflatten(lol, depth=2)))
#
# import numpy as np
# print (np.concatenate(lol))

# import num2words as n2w
#
# s = '154,342,231'
# s = s.replace(",", "")
# print(s)
# print(n2w.num2words(s))
#
#
# import humanize
# print(humanize.intword(s))

# date = "200601"
#
# import datetime, calendar
# num_days = calendar.monthrange(int(date[:-2]), int(date[4:]))[1]
# print([datetime.date(int(date[:-2]), int(date[4:]), day).strftime("%Y%d") for day in range(1, num_days+1)])




# def GetNumbersInBetween(lst, l_Bound, u_Bound):
#     n_List = []
#
#     lowerBound = min(l_Bound, u_Bound)
#     upperBound = max(l_Bound, u_Bound)
#
#     for x in lst:
#         if x >= lowerBound and x <= upperBound:
#             n_List.append(x)
#     return n_List
#
# lst = [9, 10, 11, 15, 19, 20, 21]
#
# lowerBound = 20
# upperBound = 10
#
# print(GetNumbersInBetween(lst, lowerBound, upperBound))
#
# print([x for x in lst if min(lowerBound, upperBound) <= x <= max(lowerBound, upperBound)])

# def isOrdered(t):
#     """
#     t: list
#     return True if the list is ordered in a growing sense
#     """
#     res = sorted(t)
#
#     if res:
#         if len(t) == len(set(t)):
#             return True
#         else:
#             return False
#     else:
#         return False
#
# print(isOrdered([1, 2, 3, 4, 5, 1]))
# print(isOrdered([1, 1, 2, 3, 4, 5]))
# print(isOrdered([1, 3, 2, 4, 2]))
# print(isOrdered([1, 2, 3, 4, 5, 1]))


# inventory = {'apple':(3, 133), 'banana':(9, 407), 'pear':(17, 205), 'orange':(1, 91)}
#
# maxVal = 0
# for k,v in inventory.items():
#     maxVal = max(maxVal, v[1])
#
# for k,v in inventory.items():
#     if v[1] == maxVal:
#         print(k, v)
#
#
# print(max(inventory.items(), key=lambda x: x[1][1]))

from jellyfish import soundex
#
# print(soundex("two"))
# print(soundex("to"))
#
# print(soundex("accept"))
# print(soundex("except"))
#
# # import fuzzy
# # soundex = fuzzy.Soundex(4)
# #
# # print(soundex("to"))
# # print(soundex("two"))
#

# from itertools import groupby
# def getSoundexList(dList):
#     return sorted([soundex(x) for x in dList])
#
# from operator import itemgetter
#
# def getSoundexDict(dList):
#     # print(sorted(dict_.items(), key=itemgetter(1)))
#     return sorted(dict_.items(), key=itemgetter(1))
#
# dataList = ['two','fourth','forth','dessert','to','desert']
# res = [soundex(x) for x in dataList]
# dict_ = dict(list(zip(dataList, res)))
#
# print([list(g) for _, g in groupby(getSoundexDict(dataList), lambda x: x)])



# import dateutil.parser as dparser
# dt_1 = "birthday on 20/12/2018 and wedding aniversry on 04/01/1997 and dob is on 09/07/1897"
# print("Date: {}".format(dparser.parse(dt_1,fuzzy=True).date()))

# from cStringIO import StringIO
# for item in timesplit(StringIO(a)):
#   print "Found:", item
#   print "Parsed:", p.parse(StringIO(item))


# from dateutil.parser import parse
#
# for s in s.split():
#     try:
#         print(parse(s))
#     except ValueError:
#         pass
#
# result = {"provision":"provision section 1",
#        "subsets": [
#            {"item":"milk"},
#            {"payments": [{"price": "170 usd"}]},
#            {"item":"sugar"},
#            {"payments": [{"price": "70 usd"}]},
#            {"item":"tea"},
#            {"payments": [{"price": "90 usd"}]}
#        ]
#           }
#
#
# print(result.get('subsets')[0].values())
# print(''.join(reversed("ANURAG")))
# print(result.get('subsets')[1].values())

# def swap(x, y):
#     return y,x
#
# def even_odd(x, y, c):
#     if y % 2 == 0:
#         return x,y
#     else:
#         return x, aList[c - 1]
#
#
# aList = [1,2,3,4,5,6,7,8,9,10]
#
#
#
# for i, elem in enumerate(aList):
#     for j in range(len(aList)-1, len(aList)):
#         print("Current item", aList[i])
#         if aList[i] % 2 == 0:
#             print("Curre list", aList)
#             break
#         else:
#             aList[i], aList[j] = aList[j], aList[i]
#             print("After Inter-Changed", aList[i], aList[j])
#             if aList[i] % 2 == 1:
#                 aList[i], aList[j-1] = swap(aList[i], aList[j-1])
#                 print("aglaa", aList[i], aList[j-1])
#                 continue
#             else:
#                 j -=1
#
# print(aList)

# lst = [ [[1,2],[2,3]], [[3,4],[5,6]], [[3,4], [5,6]] ]
#
# from toolz import unique
#
# flat_list = [item for sublist in lst for item in sublist]
# res = list(map(list, unique(map(tuple, flat_list))))
#
#
# print([res[i:i+2] for i in range(0, len(res), 2)])


# fset = set(frozenset(x) for x in lst)
# print([list(x) for x in fset])


# text='<>one</>this should be displayed<>two</>this too<>three</>and this<>four</>'
#
# import re
#
# text='<>one</>this should be displayed<>two</>this too<>three</>and this<>four</>'
# print(re.findall('\/>(.+?)<',text))

# line = '<meta content=\"Allrecipes\" property=\"og:site_name\"/>'
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(line, 'lxml')
# print("Content: {}".format(soup.meta["content"]))
# print("Property: {}".format(soup.meta["property"]))
#
# def func():
#     return np.random.randint(0, 10), np.random.randint(10, 20)
#
# masterLst = []
#
# for i in range(5):
#     masterLst.append(func())
#
# l1,l2 = zip(*masterLst)
#
# print(list(l1))
# print(list(l2))
# import fileinput as fp
#
# def inplace_change(filename, old_string_new):
#
#     return "Le stringhe sono vuote", None
#     for old_val, new_val in old_string_new:
#         with fp.FileInput(filename, inplace=True, backup='.bak') as file:
#             for line in file:
#                 print(line.replace(old_val, new_val), end='')
#
#
# old_string_new  = [('old1', 'new1'), ('old2', 'new2'), ('old3', 'new3')]
# print(inplace_change('list.txt', old_string_new))


#
#
# items=[["mouse,10,50"],["pen,20,50"],["pencil,30,30"],["sharpner,40,40"],["ruler,50,10"]]
#
#
# import math
# maxPrice = 0
# lowQty = math.inf
# for elem in items:
#         maxPrice = max(maxPrice, int(elem[0].split(",")[1]))
#         lowQty = min(lowQty, int(elem[0].split(",")[2]))
#
#
#
# print("max_price: {}".format(max([int(elem[0].split(",")[1]) for elem in items])))
# print("lowest_qty: {}".format(min([int(elem[0].split(",")[2]) for elem in items])))



# n = 2
# m = 23
#
# data = [(i,j,i*2) for i in range(n) for j in range(m)]
# data = [', '.join(map(str, x)) for x in data]
#
# lat = np.arange(33.8916,34.0426,0.0033)
# long = np.arange(78.0136,78.1036,0.002)
#
# res = list(zip_longest(lat,long,data))
#
# logFile = "list.txt"
#
# print(len(data))
# print(len(lat))
# print(len(long))
#
#
# with open(logFile, "w") as f:
#     for data in res:
#         f.write("%s, %s, %s" % data + "\n")

# MIN_PASSWORD_LENGTH = 6
# MAX_PASSWORD_LENGTH = 14
# import datetime
#
# ps_week = "WEEK"
# ps_strong = "STRONG"
#
# ps_week_a = "Your password is weak! It only contains letters."
# ps_week_b = "Your password is weak! It only contains number."
# ps_strong_a = "Your password is strong! It contains letters and numbers."
#
#
# def writeTofile(fileObj, p_strength, p_text):
#     fileObj.write("Date: {}".format(datetime.datetime.today()) + "\n")
#     fileObj.write("Password: {}".format(p_inp + "\n"))
#     fileObj.write("Password strength: {}".format(p_strength) + "\n")
#     fileObj.write("Prompt: {}".format(p_text) + "\n")
#
# def p_validate(p_inp, fileObj):
#     if p_inp.isalpha():
#         writeTofile(fileObj, ps_week, ps_week_a)
#     elif p_inp.isnumeric():
#         writeTofile(fileObj, ps_week, ps_week_b)
#     else:
#         writeTofile(fileObj, ps_strong, ps_strong_a)
#
# while True:
#     p_inp = input("Enter your password OR Press N to quit")
#     if p_inp.lower() == 'n':
#         exit()
#     with open('list.txt', 'a+') as fileObj:
#         p_validate(p_inp, fileObj)


# line = '''<tr>
# <td><a href="http://sdb.admin.uw.edu/timeschd/UWNetID/sln.asp?QTRYR=SPR+2019&amp;SLN=15308">15308</a></td>
# <td nowrap="">INFO   101  </td>
# <td>A </td>
# <td align="CENTER">LC</td>
# <td>SOCIAL NETWORKING   </td>
# <td align="CENTER"> 150</td>
# <td align="CENTER"> 150</td>
# <td align="CENTER"> 250</td>
# <th align="CENTER">  0</th><td align="CENTER"> 229</td>
# <td></td>
# </tr>
# <tr><td><a href="http://sdb.admin.uw.edu/timeschd/UWNetID/sln.asp?QTRYR=SPR+2019&amp;SLN=15309">15309</a></td>
# <td nowrap="">INFO   101  </td>
# <td>AA</td>
# <td align="CENTER">LB</td>
# <td>SOCIAL NETWORKING   </td>
# <td align="CENTER">  25</td>
# <td align="CENTER">  25</td>
# <td align="CENTER">  26</td>
# <th align="CENTER" style="">  2</th><td align="CENTER">  21</td>
# <td></td>
# </tr>'''
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(line, 'html.parser')
#
# trElems = soup.find_all('tr')
# toFind = '15308'
#
# for tr in trElems:
#     val = tr.select('td a')[0].text
#     if toFind == val:
#         xpathTh = tr.find_all('td')[7]
#         print("For the value: {}, The result is {}".format(toFind, xpathTh.find_next('th').text.strip()))

# from bs4 import BeautifulSoup
#
# xml = '''\
# <root>
# <name search = "read TTT: write">
#     <version id = "1.0.0">
#         <value>myVal</value>
#         <method>myMethod</method>
#     </version>
# </name>
#
# <name search = "read TTT: write">
#     <version id = "2.0.0">
#         <value>myVal_2</value>
#         <method>myMethod_2</method>
#     </version>
# </name>
# </root>'''
#
#
# soup = BeautifulSoup(xml, 'lxml')
# newVal = "NewValue"
#
# for elem in soup.find_all("name"):
#     elem['search'] = elem['search'].replace(str(elem['search']).split(" ")[0], newVal)
#     print(elem)

# from xml.dom import minidom
# xmldoc = minidom.parse('list_test.xml')
#
# tags = xmldoc.getElementsByTagName("name")
#
# for item in tags:
#     item.attributes["search"].value = item.attributes["search"].value.replace(
#         'select ARG', 'selected ARG')
#     print(item.content)

# from bs4.dammit import EncodingDetector
#
# headers = {
#         'Connection': 'close',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
#     }
#
# def get_url_soup(url):
#         url_request = requests.get(url, headers=headers, allow_redirects=True)
#         http_encoding = url_request.encoding if 'charset' in url_request.headers.get('content-type', '').lower() else None
#         html_encoding = EncodingDetector.find_declared_encoding(url_request.content, is_html=True)
#         encoding = html_encoding or http_encoding
#         soup = BeautifulSoup(url_request.content, 'lxml', from_encoding=encoding)
#         return soup
#
# soup = get_url_soup('https://www.onlinekhabar.com/2019/03/753522')
# title_card = soup.find('div', {'class': 'nws__title--card'})
#
# print(title_card.text.strip())



# import requests
# from bs4 import BeautifulSoup
#
# html = '''<h5>
#     <a id="user-content-q-can-i-use-multilingual-bert-model-provided-by-google" class="anchor" aria-hidden="true" href="#q-can-i-use-multilingual-bert-model-provided-by-google">
#     <svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
#     <path fill-rule="evenodd" d="M4 9h1v1H4c"></path>
#     </svg>
#     </a>
#     <strong>Q:</strong> Can I use multilingual BERT model provided by Google?
# </h5>
# <p><strong>A:</strong> Yes.</p>'''
#
# soup = BeautifulSoup(html, "html.parser")
# results = soup.find("h5")
#
# print(str(results.contents[len(results.contents)-1]).strip())


#
# from bs4 import BeautifulSoup as bs
#
# res = requests.get('https://www.flipkart.com/samsung-mobile-store?otracker=nmenu_sub_Electronics_0_Samsung')
# soup = bs(res.content, 'html.parser')
#
# names = soup.find_all('a', class_ ='Zhf2z-')
# ratings = soup.find_all('div', class_ ='hGSR34')
#
# for nm, rat in zip(names, ratings):
#     print("Device: {}, Link: {}, Rating: {}".format(nm.get('title', 'no title avialable'), nm.get('href', 'href not available'), rat.text))


# with open("people.csv") as f:
#     contents = f.read()
#     occurences = contents.count("bike")
#
# print(occurences)
#
# print([sum(line.count("bike") for line in open('people.csv'))][0])

# import pandas as pd
# df = pd.DataFrame({"Sex": ['male','male','female','male','female']})
#
# df['Sex'] = df['Sex'].apply({'male':0, 'female':1}.get)
# print(df)

# import datetime as dt
# timestamp = [1545730073,1645733473]   # or timestamp = ['1545730073','1645733473']
#
# for indx, ts in enumerate(timestamp):
#     timestamp[indx] = dt.datetime.fromtimestamp(int(ts)).date()
#     print(timestamp[indx])
#
# print(timestamp)
# print([dt.datetime.fromtimestamp(int(ts)).date() for ts in timestamp])

# import datetime as dt
# timestamp = [1545730073,1645733473]   # or timestamp = ['1545730073','1645733473']
#
# for indx, ts in enumerate(timestamp):
#     timestamp[indx] = dt.datetime.fromtimestamp(int(ts)).date()
#
# print(timestamp)
#
# dt_object = list(map(dt.date.fromtimestamp, timestamp[0]))


# import sys
# import time
# for i in range(10):
#     sys.stdout.write('\r' + str(i))
#     time.sleep(1)

#
# strings = ["Mayo", "Nice May", "nice May comes", "nice Mayo", "nice Mayo comes"]
# substring = "May"
# for x in strings:
#     if substring in x.split():print(x)
#
# print([x for x in strings if substring in x.split()])

# content = ['Sports', 'Nature', 'Football']
# path = 'list.txt'
# with open(path) as auto:
#         print([[x.lower() for x in content if x.lower() in line.lower()]for line in auto for y in content if y in line])


# parse = ['a ', ' ', ' b', 'c', '', 'd ']

# print(list(map(str.strip, filter(str.strip, parse))))

# s = [11.117643101389094, 14.439701045971955, 1.0, 4.459431618637297, 7.794415866350106, 11.117643101389094, 1.0, 4.459431618637297, 7.794415866350106]
#
# # print(list(filter(lambda x: x.is_integer(), s)))
#
# import time
#
# start = time.time()
# # print(list(filter(lambda x: x.is_integer(), s)))
# ints = [i for i in s if i.is_integer()]
# end = time.time()
# print(end - start)


# def read_anchors(anchors_path):
#  with open(anchors_path) as f:
#   anchors = f.readline()
#   anchors = [float(x) for x in anchors.split(',')]
#   anchors = np.array(anchors).reshape(-1, 2)
#  return anchors
#
#
# print(read_anchors("list.txt"))

# s = [1.5, 1.0, 2.5, 3.54, 1.0]
#
# # print([int(x) if x.is_integer() else x for x in s])
#
#
#
# print(list(filter(lambda x: int(x) if x.is_integer() else x, s)))

# from datetime import datetime, timedelta
# print(datetime.today() - timedelta(minutes=4

# dt_1 = "2019-04-03 05:10:35+03:00"
# # print("Date: {}".format(dparser.parse(dt_1,fuzzy=True)))
#
# import datetime
# print(datetime.datetime.strptime("2019-04-03T05:10:35+03:00", "%Y-%m-%dT%H:%M:%S%z"))

# import ast
#
# sch = "{0= [0, 0.00, 5.59, 8.00, 14.59, 17.00, 0.59], 1= [1, 1.00, 0.59], 2:[2, 1.00, 0.59], 3=[3, 1.00, 5.59, 8.00, 0.59], 4=[4, 1.00, 12.59, 15.00, 0.59], 5=[5, 1.00, 2.59, 5.00, 14.59, 17.00, 0.59], 6=[6, 1.00, 23.59]}"
# sch = ast.literal_eval(sch.replace("=",":"))
#
# print([v for k,v in sch.items()])

#
# s = [1.5, 1.0, 2.5, 3.54, 1.0, 4.4, 2.0]
# # s = [str(x) for x in s]
#
# print([int(x) if x.is_integer() else x for x in s])
#
# # def func(s):
# #     return [int(x) if x == int(x) else x for x in s]
# #
# # print(func(s))
# print(list(map(lambda x: int(x) if x == int(x) else x, s)))
#
# # print(list(map(lambda x: int(x) if int(x) == x else x, s)))
#
# # # print(map(str.strip, filter(str.strip, s)))
# import pandas as pd
#
# df = pd.DataFrame({'order_status': ['delivered', 'shipped', 'canceled', 'invoiced', 'processing']})
#
# # mask = df['order_status'].isin(['delivered'])
# # print(df[~mask])
#
# filter_ = df.groupby('order_status')
# res = filter_.filter(lambda x: x != 'delivered')
# print(res['order_status'].value_counts())
#
# queryColectoras = {'server': 'csv_data','server2': 'csv_data2'}
#
# for key,val in queryColectoras.items():
#       print(key, val)
#
# print({k:v for k,v in queryColectoras.items()})

# import datetime
#
# tempValue = datetime.datetime.strptime("02-05-2019 12:30:43.000", '%Y-%m-%d %H:%M:%S').strftime('%b %d, %Y')

# import dateutil.parser as dparser
# dt_1 = "2000-12-25 17:30:00"
# tempVal = (dparser.parse(dt_1,fuzzy=True).date()).strftime('%d %B %Y')
#
# print("Date: {}".format(tempVal))

# s = 'file.exe.abc.dux'
#
# print(s.rsplit('.', 1))
#
# import re
# print(re.search(r'^.*(?=\.)', s)[0])
#
# print(s[:s.rindex(".")])

# function that prompts the user for a name and returns it


# products = [
#               {'product_name': 'Passion Fruit Flavored Fruit Juice Cocktail Blend',
#               'department_id': '7',
#               'metrics': {'request_count': 289, 'number_of_first_orders': 82}},
#
#               {'product_name': 'Passion Fruit Flavored Fruit Juice Cocktail Blend',
#               'department_id': '7',
#               'metrics': {'request_count': 289, 'number_of_first_orders': 90}}
#            ]
#
#
# for entry in products:
#     number_of_first_orders = entry["metrics"]["number_of_first_orders"]
#     print(number_of_first_orders)


# import wikipedia
#
# ny = wikipedia.page("List of Internet top-level domains", 'html.parser')
#
# print(ny.content)

# import json
# #
# # with open('list.txt', 'r') as file:
# #     content = file.read()
# #     clean = content.replace('][', ',')  # cleanup here
# #     json_data = json.loads(clean)
# #
# # print(json_data)
import timeit



#
# j_data = {"AbandonmentDate": "", "Abstract": "", "Name": "ABC"},{"AbandonmentDate": "", "Abstract": "", "Name": "ABC"}
#
# import json
# with open('j_data_file.json', 'w') as outfile:
#     for elem in j_data:
#         json.dump(elem, outfile)
#         outfile.write('\n')

#
# import json
# results  = ['[{"AbandonmentDate":null,"Abstract":null,"Name":"abc"}\n,{"AbandonmentDate":null,"Abstract":null,"Name":"abc"}\n]']
#
# res1 = results[0].split("\n,")[0]
# res2 = results[0].split("\n,")[1]
#
# r = [res1, res2]
#
# with open('j_data_file.json', 'w') as file:
#     for elem in r:
#         json.dump(elem, file)
#         file.write('\n')

# from ilio import read
#
# contents = read('filename').splitlines()



# with open('list.txt') as fileObj:
#     print(list(fileObj)[-1])
#
#
# from pathlib import Path
# print(Path('list.txt').read_text().splitlines()[-1])

from natsort import natsorted

# fileOne = 'list.txt'
# fileTwo = 'list2.txt'
#
# result = []
# with open (fileOne, 'r') as file1Obj, open(fileTwo, 'r') as file2Obj:
#       result.append(file1Obj.readlines())
#       result.append(file2Obj.readlines())
#
# result = sum(result, [])
# result = [i.split('\n', 1)[0] for i in result]
#
# print(sorted(result, reverse=True, key = lambda x: int(x.split()[2])))



# subject = {'math':  {('Tom', 'A+'), ('Kevin','B+')},
#        'History':  {('Kate', 'C+'),('Eric','C'),('Hannah','A-')},
#        'English':  {('Eli', 'B-')}}
#
# result = {}
# for k, v in subject.items():
#     for name, grade in v:
#         result[grade.rstrip("+-")] += {k : name}
# print(result)

# fileOne = 'list.txt'
# fileTwo = 'list2.txt'
#
# with open (fileOne, 'r') as file1Obj, open(fileTwo, 'r') as file2Obj: result = file1Obj.readlines() + file2Obj.readlines()
#
# print(list(i.split('\n', 1)[0] for i in sorted(result, reverse=True, key = lambda x: int(x.split()[2]))))   # sorting by the view


# messages = []
#
# import ast
# with open("commitJson.json","r", encoding="utf8") as json_file:
#     data = ast.literal_eval(json_file.read())
#
#
# for elem in data['items']:
#     for e in elem['commit']:
#         if 'message' in e:
#             print(elem['commit'][e])
#
# print([elem['commit'][e] for e in elem['commit'] if 'message' in e for elem in data['items']])

# s = ['Received value 126;AOC;H3498XX from 602', 'Received value 101;KYL;0IMMM0432 from 229']
#
# for elem in s:
#     print(elem.replace(elem.split(";",2)[-1].split()[0],''))


# with open('list.txt', 'r') as f:
#     content = f.readlines()
#
# bFlag = False
# for line in content:
#     if line.startswith('Component2'):
#         bFlag = not bFlag
#     if bFlag:
#         if 'Component3' in line:
#             break
#         else:
#             print(line)

a = [{"a":"data1","b":"Nill","c":"data3","d":"Nill"},{"a":"dat1","b":"dat2","c":"dat3","d":"Nill"},{"a":"sa1","b":"sa2","c":"sa3","d":"Nill"}]


# result = {}
# for sub_list in a: # loop through the list
#     for key, val in sub_list.items():
#         result[key] = result.get(key, 0)
#         if val == 'Nill':
#             result[key] += 1
#
# for key, val in result.items():
#     print(key, val)



# from collections import OrderedDict
# counter = OrderedDict()
# for item in a:
#    if 'Nill' in item:
#          counter[item['Nill']] = counter.get(item['Nill'], 0) + 1
#
# print(counter)

# c = Counter()
# for d in a:
#    c.update({k: v == 'Nill' for k, v in d.items()})
# list1 =[(1,2,3),(4,5),(7,8,9),(10,11)]
# #
# for elem in list1:
#     print(f"{', '.join(str(e) for e in elem)}, of size {len(elem)}")

# import re
# s = '1,2,"toto , titi",3"titi ,, tata",4'
#
# print(str(re.findall(r'"([^"]*)"', s)).replace(",", ":"))

# import dateutil.parser as dparser
#
# dt_1 = "2018-11-16 11:32:51.285000+01:00"
# dt_2 = "2019-02-28 17:13:49.492000+01:00"
# dt_3 = "2018-08-29 09:50:51+02:00"
#
#
# print("Date: {}".format(dparser.parse(dt_1,fuzzy=True).date()))
# print("Date: {}".format(dparser.parse(dt_2,fuzzy=True).date()))
# print("Date: {}".format(dparser.parse(dt_3,fuzzy=True).date()))


# itemsList = []
# priceList = []
#
#
# for i in range(1,4):
#     itemStr = "Enter the {} shopping item: ".format(i)
#     itemsList.append(input(itemStr))
#     priceStr = "Enter the price of {}: ".format(itemsList[i-1])
#     priceList.append(int(input(priceStr)))
#
# print("The Total of {}, {}, {} is {} and the average price of the items are {}".format(*itemsList, sum(priceList), sum(priceList) / float(len(priceList))))
#
# print(itemsList)
# print(priceList)

# s = ['', 'value1', '346.897', '', 'value2', '202.306', 'value3', '136.880', 'value4', '7.711', '']
# s = list(filter(None, s))
# print(list(zip(s[0::2], s[1::2])))

# with open("j_data_test.csv", "r") as fileObj, open("j_data_test.csv", "w") as fileObj2:
#         contents = fileObj.read().replace(';',' ').replace('\\', '').replace('"', '')
#
# print(contents)

# with open("j_data_test.csv", "w+") as fileObj2:
#     fileObj2.write(contents)

# import pandas as pd
# df = pd.read_csv(r"j_data_test.csv", delimiter = ";")
# print(df)

# import pandas as pd
#
# rm_quote = lambda x: x.replace('"', '').replace(';',' ').replace('\\', '').replace('"', '')
#
# df = pd.read_csv(r"j_data_test.csv", delimiter = ";", converters={rm_quote})
#
# df = df.rename(columns=rm_quote)
# print(df)

# lst = []
# repetitions = 3
# for elem in range(2):
#     lst  += [elem] * repetitions
#
# print(lst)
# print(sorted([0,1,2]*3))
#
# print([elem for elem in range(3) for _ in range(repetitions)])
#
# print(list(np.repeat(lst,3)))
#
# print([elem for elem in lst for i in range(3)])


# l = list(range(100))
# n = 15
# def chunks(l, n):
#     """Yield successive n-sized chunks from l."""
#     for i in range(0, len(l), n):
#         yield l[i:i + n]
# import pprint
#
# res = (list(chunks(list(range(0, 100)), 10)))
# # print(res)
# lstA, lstB, lstC, lstD, lstE, lstF, lstG, lstE, lstH, lstI = [*res]
# pprint.pprint(lstA)
# pprint.pprint(lstB)

# print(res[0])
# print(res[1])
#
# import requests
# from bs4 import BeautifulSoup
# import dateutil.parser as dparser
# import re
#
# library_list = []
#
# data = {'employeeId' : '201', 'date' : '2019-04-30', 'actionRecorder' : 'viewMy'}
#
# page = requests.post("http://192.168.101.197/intagleo_hrm/symfony/web/index.php/attendance/getRelatedAttendanceRecords", params=data, cookies={'PHPSESSID':'7kgsrcdbg7dhj61smcevk4i3k5','Loggedin':'True'})
# soup = BeautifulSoup(page.content, 'html.parser')
#
# table = soup.find('table', class_ ='table')
# td = table.find_all('td')
#
# date_time = []
# for elem in td[:-5]:
#     elem = elem.text.strip()
#     if elem != '':
#         date_time.append("".join(re.findall(r'\d{2}[-]\d{2}[-]\d{4}\s\d{2}[:]\d{2}[:]\d{2}', elem)))
#
# print(date_time)
#
# # a = datetime.datetime(2019, 4, 1, 11, 52, 26)
# # b = datetime.datetime(2019, 4, 1, 20, 25, 7)
#
# a = dparser.parse(date_time[0])
# b = dparser.parse(date_time[1])
# c = b - a
# print(c)
#
#


# import json
# import ast
# with open('commitJson.json', 'r') as fp:
#      print(json.dumps([ast.literal_eval(line.strip()) for line in fp.readlines()], indent = 4))

import random

# numbers = [1, 1, 1, 1, 6, 5, 5, 2, 3]
#
# print(list(dict.fromkeys(numbers).keys()))
#
# import pandas as pd
# print(pd.unique(numbers).tolist())
#
#
# from collections import OrderedDict
# print(list(OrderedDict.fromkeys(numbers)))
#
#
# numbers = [1, 1, 1, 1, 6, 5, 5, 2, 3]
# for x in numbers[:]:
#     if numbers.count(x) >= 2:
#         numbers.remove(x)
# print(numbers)
#
#
# print(list(set(numbers)))
#
# print(list(frozenset(numbers)))
#
# a1 = []

# from  more_itertools import unique_everseen
#
# print(list(unique_everseen(numbers)))
#
# from itertools import groupby
# print([k for k,_ in groupby(numbers)])


# Line='Hello, welcome to python programming '
#
# words=[x for x in Line.split()]
# print(words)
#
# lengths=[len(word) for word in words]
# print(lengths)
#
# x = {words[i]: lengths[i] for i in range(len(words))}
# print('--'*44)
# print (x)
#
# maxWord = max(x, key=x.get)
# minWord = min(x, key=x.get)
#
# print("The maximum word is {} with len {}".format(maxWord, x[maxWord]))
# print("The minimum word is {} with len {}".format(minWord, x[minWord]))
#
#
# s = 'Hello, welcome to python programming '
# maxWord = max(s.split(), key=len)
# maxLen = len(maxWord)
#
# minWord = min(s.split(), key=len)
# minLen = len(maxWord)
#
# print((maxWord, maxLen))
# print((minWord, minLen))
#
# print((((max(s.split(), key=len), len(maxWord)),(min(s.split(), key=len), len(maxWord)))))

# result = [{'T_Project': 'ABC','T_Employee': 'MNK','T_Project1': 'ABC','T_Project2': 'ABC'}]
#
# print(list(map(lambda x: x.values(), result)))
#
# print(list(x.values() for x in result))
#
# from collections import OrderedDict
#
# d = OrderedDict()
# d['T_Project'] = 'ABC'
# d['T_Employee'] = 'MNK'
# d['T_Project1'] = 'ABC'
# d['T_Project2'] = 'ABC'
#
# print(list(d))
# print(list(d.values()))
#
# r = ['T_Dept.ABC', 'T_EMP.NAME', 'T_PRO.ABC', 'T_Mastert.ABC']
#
# print([x.split(".")[1] for x in r])

#
# sentences = ['Hello akk sentence', 'Another one asdfa here', 'and another one']
#
# s = " ".join(sentences)
# repList = ['akk','asdfa']   # list of all the chars to replace
#
# for elem in repList:
#     s = s.replace(elem, '')
# print(s)
#
# print(list(s.replace(elem, '') for elem in repList))
#
# import dateutil.parser as dparser
#
# def from_pendulum_to_tupple(date):
#     print("date: {}".format(date))
#     date = dparser.parse(date,fuzzy=True)
#     year = date.year
#     month = date.month
#     day = date.day
#     hour = date.hour
#     minute = date.minute
#     return (year, month, day, hour, minute)
#
# s = '2019-04-18T14:00:00+00:00'
# print(from_pendulum_to_tupple(s))

# import pandas as pd
# df = pd.DataFrame()
# df['Tag'] = [('unclear', 'JJ'), ('incomplete', 'JJ'), ('instruction', 'NN'), ('given', 'VBN')]
#
# # create 2 separate columns with tags and words
# df['words'] = [i[0] for i in df['Tag']]
# df['tags'] = [i[1] for i in df['Tag']]
#
# # use np.where to find tags with `NN`
# df['Tagged2'] = np.where(df['tags']=='NN', df['words'], np.nan)
#
# df.drop(['words','tags'],1,inplace=True)
# print(df)

# d = [
#    {
#       "task_id":123,
#       "results":[
#          {
#             "url":"site.com",
#             "date":"04.18.2019"
#          },
#          {
#             "url":"another_site.com",
#             "date":"04.18.2019"
#          },
#          {
#             "url":"site1.com",
#             "date":"04.18.2019"
#          }
#       ]
#    },
#    {
#       "task_id":456,
#       "results":[
#          {
#             "url":"site3.com",
#             "date":"04.18.2019"
#          },
#          {
#             "url":"site.com",
#             "date":"04.18.2019"
#          }
#       ]
#    },
#    {
#       "task_id":789,
#       "results":[
#          {
#             "url":"site7.com",
#             "date":"04.18.2019"
#          },
#          {
#             "url":"site9.com",
#             "date":"04.18.2019"
#          },
#          {
#             "url":"site.com",
#             "date":"04.18.2019"
#          }
#       ]
#    }
# ]
# # code to remove duplicates
# keep = set({repr(sorted(value.items())): key
#             for key, value in d.items()}.values())
#
# for key in list(d):
#  if key not in keep:
#     del d[key]
# x = ["The wind, ", "which had hitherto carried us along with amazing rapidity, ", "sank at sunset to a light breeze; ", "the soft air just ruffled the water and ", "caused a pleasant motion among the trees as we approached the shore", "from which it wafted the most delightful scent of flowers and hay."]
#
#
#
# print("".join(x))
#
#
# string1 = "The wind, "
# string2 = "which had hitherto carried us along with amazing rapidity, "
# string3 = "sank at sunset to a light breeze; "
# string4 = "the soft air just ruffled the water and "
# string5 = "caused a pleasant motion among the trees as we approached the shore, "
# string6 = "from which it wafted the most delightful scent of flowers and hay."
#
#
# print("".join([string1, string2, string3, string4, string5, string6]))
#
# message = ''.join([eval('string'+str(i)) for i in range(1,7)])
#
# print(message)
#
# s = [
#     {
#         "a": "1",
#         "b": "2"
#     },
#     {
#         "a": "3",
#         "b": "4"
#     },
#     {
#         "a": "5",
#         "b": "6"
#     }
# ]


# for k,v in s:
#    s[k + '0'] = s.pop(k)
# print(s)

# for dict_item in s:
#     for key in dict_item:
#         print(key)
#         dict_item[key + '0'] = dict_item.pop(key)   # dict_item[key]

# id = [6, 77, 888, 9999]
# print([int(str(x).zfill(4)) for x in id])

# import pandas as pd
#
# df = pd.DataFrame({'un-padded':[6, 77, 888, 9999]})
# df['padded'] = [str(x).zfill(4) for x in df['un-padded']]
# print(df)

# s = [
#      {"filename1": "SPI_121218_SITE2_NDVI_25m_transparent_mosaic_group13918.jpg", 'some': 'data'},
#      {"filename2": "SPI_121218_SITE2_NDVI_25m_transparent_mosaic_group13919.jpg", 'some': 'data'}
#     ]
#
# print({k:v for elem in s for k,v in elem.items() if 'filename' in k})


# string2 = "Hello World;"
# string3 = "Hello World,"
# string4 = "Hello Word."
#
# s = [string4, string3, string2]
#
#
# # print(" ".join([x + x if x.endswith(';') and x.endswith(',') else x for x in s]))
#
# p = [x for x in s if x.endswith(';') or x.endswith(',')]
#
# print(" ".join(p + list(set(s) - set(p))))
#
# string2 = "Hello World;"
# string3 = "Hello World,"
# string4 = "Hello Word."
# import pandas as pd
# a = [['1', 'sam', 'Texas', 'na']]
# df = pd.DataFrame(a, columns=[b'id', b'Name', b'Address', b'Contact'])
# df.columns = [x.decode('utf-8') for x in df.columns]
# print(df)

# import json
# import objectpath
#
# with open('j_data_file.json') as fileObj:
#     s = json.load(fileObj)
#
# t = 0
# for elem in s:
#     if elem['questionnaire'] == t:
#         print(elem['response']['text'])
#         print(elem['response']['guid'])
#         print(elem['response']['options'][t]['optionText'])
#         print(elem['response']['options'][t + 1]['optionText'])
#
#
# g_id = '1b9beed5-fd72-477f-b8b8-126aefd8ffbd'
# opt = 'no'
#
# # return child text, guid and optionText
#
# for elem in s:
#     if elem['response']['guid'] == g_id:
#             if elem['response']['options'][t]['optionText'] == opt:
#                     print(elem['response']['options'][t]['text'])
#                     print(elem['response']['options'][t]['guid'])
#                     print(elem['response']['options'][t]['options'][t]['optionText'])
#                     print(elem['response']['options'][t]['options'][t + 1]['optionText'])
#             elif elem['response']['options'][t + 1]['optionText'] == opt:
#                     print(elem['response']['options'][t + 1]['text'])
#
# food = 'pizza'
# g_id = '7b08ab52-313f-47f6-abcd-d7c5732d5e28'
#
# # return child text, guid and optionText
#
#
# for elem in s:
#     if elem['response']['options'][t]['guid'] == g_id:
#         if elem['response']['options'][t]['options'][t]['optionText'] == food:
#              print(elem['response']['options'][t]['options'][t]['text'])
#              print(elem['response']['options'][t]['options'][t]['guid'])
#              print(elem['response']['options'][t]['options'][t]['options'][t]['optionText'])
#              print(elem['response']['options'][t]['options'][t]['options'][t + 1]['optionText'])
#         elif elem['response']['options'][t]['options'][t + 1]['optionText'] == food:
#              print(elem['response']['options'][t]['options'][t + 1]['text'])
#
#
# opt = 'no'
# g_id = '15b929d1-7436-47cf-9cd1-46b186c51b7e'
#
# # return child text, guid and optionText
#
# for elem in s:
#     if elem['response']['options'][t]['options'][t]['guid'] == g_id:
#         if elem['response']['options'][t]['options'][t]['options'][t]['optionText'] == opt:
#              print(elem['response']['options'][t]['options'][t]['options'][t]['text'])
#         elif elem['response']['options'][t]['options'][t]['options'][t + 1]['optionText'] == opt:
#              print(elem['response']['options'][t]['options'][t]['options'][t + 1]['text'])
#
#

#
# response = [elem for elem in s if elem['questionnaire'] == t]
# # answers = [r['text'] for r in response['options']]
# # print(answers)
# print(response[t]['text'])

#
# def myGen(n):
#     yield n
#     yield n + 1
#
# # g = myGen(6)
# #
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
#
# for n in myGen(6):
#  print(n)

# import array as arr
# a=arr.array('d', [1.1 , 2.1 ,3.1] )
# a.append(3.4)
# print(a)
# a.extend([4.5,6.3,6.8])
# print(a)
# a.insert(2,3.8)
# print(a)
#

# pyramid testing
def pyfunc(r):
 for x in range(r):
  print(' ' * (r - x - 1) + '*' * (2 * x + 1))
pyfunc(9)