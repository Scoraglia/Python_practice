file = open("spider.txt")
#print(file.readline())
#print(file.readline())
print(file.read())
file.close()
#with open("spider.txt") as file:
#    print(file.readline())

#Iterate in the file, line by line, but will read the last hidden jump line character \n
with open("spider.txt") as file:
    for line in file:
        print(line.upper())
        
#Using strip() to avoid whitespaces lines
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())
        

#readlines() save each line in a list
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
        

