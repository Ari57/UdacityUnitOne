# print(3)
# print(1 + 1)
# print(52 * 3 + 12 * 9)
# print((52 * 3) + (12 * 9))
# print(52 * (3 + 12) * 9)
# print(365 * 24 * 60 * 60)
#  above prints the number of seconds in a year
#  there are 10080 minutes in a week
# print(10080 * 7)
#  could have also done:
#  7 * 7 - number of days
#  7 * 7 * 24 - number of hours
#  7 * 7 * 24 * 60 - number of minutes in a week

# speed_of_light = 299792458  # metres per second
# print(speed_of_light)
# nanostick = speed_of_light * 1000000000 * 100
#
# cyclesPerSecond = 2700000000 # 2.7 ghz
#
# print(speed_of_light/cyclesPerSecond)
#
# cyclesPerSecond = 2600000000
#
# age = 18
#
# print(365*age + 105)

# Strings
# string = "I am a string"
# print(string)

name = "Nathan"

# String concatenation
# print("Hello " + name + "!!!")
# # Indexing Strings
# print(name[1])
# print(name[-3])
# # minus index starts from the back
# # name = name + name
# # print(name)
# # name = "Nathan"
# # print(name[-1])
# # print(name+name[-1])
#
# print(name[1:3])
# it stops just before position 3
# print (name[:]) (give the whole word)

s = "audacity"

# print("U" + s[2:8])

# ss [0:0] - should print nothing or could print out first letter
# abcd [0:-1] - abc

# t = "Hi"
# print t[:3] + t[3:]
# above prints out 'Hi'
# String.find(string) – the position in the string where that sub-string is found

# sentence = "Hello this is a sentence, and this is another sentence"
# print(sentence.find("sentence"))
# # above prints 16 as 'sentence' starts on the 16th position
# print(sentence.find("hello)"))
# # it's also case sensitive

# s.find(s) will always be 0 as it's the first position no matter what
# You can use find to locate multiple occurrences

# test = "Hello. Hello again, this is a test"
# print(test.find('Hello'))
# print(test.find("Hello",0)) # first occurrence of 'Hello' is found at position 0
# print(test.find("Hello",3)) # start from position 3, the first occurrence of 'Hello' is found at position 7
# print(test.find("Hello",10)) # it will return -1 if it can't find anything


# print(s[0:].find("hello,0"))
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find("<a href=")
start_quote = page.find('"',start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1: end_quote]
print(url)


