import csv
import itertools
file_object=open("/Users/joelleeverett/Desktop/github/inst326testGH/klaverns_all_sans_sources.csv")
info=csv.DictReader(file_object)
info,info2=itertools.tee(info,n=2)
state=input("Enter a state: " ) 
for line in info:
    min=1916
    if line["founded by"]==min:
        line.move_to_end
        min+=1
for row in info2:
    row["founded by"] = int(row["founded by"])
    if row["klavern name"]=="Not Named":
        row["klavern name"] = "(Not Named)"
    if row["state"]==state:
        print("The klavern "+row["klavern name"]+" was founded in "+row["city"]+" in "+str(row["founded by"]))

