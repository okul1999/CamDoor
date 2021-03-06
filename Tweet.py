from twython import Twython
import time, os

#http://www.mieni.nl/

APP_KEY = "184zUq2bFNsVkLJNALmvKImVR"
APP_SECRET = "PannWHgUEmXCPcergzBbIjkA6AZICDgB6CSXuhYF0yFiwoOFBI"

with open("pic/config", "r") as f:
    if not f.read() == "":
        f.seek(0)
        if f.readline()[0] == "#":
            f.seek(0)
            OAUTH_TOKEN = f.readline()[1:-1]
            OAUTH_TOKEN_SECRET = f.readline()[1:-1]
            twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
            print "successfully opened twitter"

while True:
    f = open("pic/tweet", "r")
    lines = f.readlines()
    f.close()

    f = open("pic/tweet", "w")
    for line in lines:
        if line[0] == "$":
            print "tweeted file: " + line[1:]
            fn = os.path.abspath("pic/" + line[1:-1])
            print fn
            try:
                photo = open(fn, "rb")
                twitter.update_status_with_media(status="Someone walked through the door at " + line[1:], media=photo)
                os.remove("pic/" + line[1:-1])
                photo.close()
            except OSError, Twython.TwythonError:
                print "file to tweet not found"
                f.write(line)
            else:
                f.write(line[1:])
            f.flush()
            os.fsync(f.fileno())
    f.close()