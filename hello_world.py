words = "It's thanksgiving day. It's my birthday, too!"
print words
print words.find('day')
print words.replace("day", "month")
print words

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]

print y[0]
print y[len(y)-1]

new_y = [y[0], y[len(y) - 1]]
print new_y

list_2 = [19,2,54,-2,7,12,98,32,10,-3,6]
print list_2
list_2.sort()

print list_2

half_length = len(list_2)/2

lst = []

for ele in list_2 [:5]:
    lst.append(int(ele))

list_2.insert(5, lst)
print list_2[5:]
