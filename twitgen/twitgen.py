import os
import jinja2
import csv
import datetime
import email.utils

templateLoader = jinja2.FileSystemLoader(searchpath=os.getcwd())
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)

class Tweet:
    text = None
    handle = None
    date = None
    media = None
    def __init__(self, row):
        self.media = [m for m in row[0].split(',') if m.strip() != ""]

        date = datetime.datetime.strptime(row[1], '%a %b %d %H:%M:%S %z %Y')
        self.date = email.utils.format_datetime(date)
        self.handle = row[3]
        self.text = row[4]

f = open('data.csv', 'r')

tweets = []

with f:
    reader = csv.reader(f)

    for row in reader:
        tweets.append(Tweet(row))



template = templateEnv.get_template("tweets.html")

output = template.render(tweets=[t for t in tweets if t.handle == "pir_at" and  not t.text.startswith("RT")])

print(output)


