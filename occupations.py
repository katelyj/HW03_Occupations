from flask import Flask, render_template
import random, csv

taco = Flask(__name__)

@taco.route("/")
def home():
    return render_template("main.html")

@taco.route("/occupations")
def occ():
    return render_template("occupations.html", #html file
                           dict=dictCSV(), #dictionary
                           occ=randOcc(dictCSV())) #random occupation

def dictCSV():
    d = {}
    with open('occupations.csv') as data:
        reader = csv.DictReader(data)
        for row in reader:
            occ = row['Job Class']
            percent = float(row['Percentage'])
            d[occ] = percent
        del d['Total']
    return d

def randOcc(d):
    randVal = random.random()*99.8
    ctr = 0.0
    for job in d:
        percent = d[job]
        if randVal < ctr + percent:
            return job
        else:
            ctr += percent

if __name__ == '__main__':
    taco.debug = True
    taco.run()
