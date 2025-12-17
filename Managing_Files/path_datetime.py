import datetime
import os

#Managing_Files\spider.txt

#This code will provide the file size

os.path.getsize("spider.txt")

#This code will provide the date and time for the file in an 
#easy-to-understand format

timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)

#This code takes the file name and turns it into an absolute path

os.path.abspath("spider.txt")