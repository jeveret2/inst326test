import csv
file_object=open("/Users/joelleeverett/Desktop/github/inst326testGH/klaverns_all_sans_sources.csv")
info=csv.DictReader(file_object)
state=input("Enter a state: " ) 
min=1916    
for i in range(1,31):
    for row in info:
        if row["klavern name"]=="Not Named":
            row["klavern name"]="(Not Named)"
        if row["founded by"]==str(min):
            print("The klavern "+row["klavern name"]+" was founded in "+row["city"]+" in "+row["founded by"])
    min+=1
    file_object.seek(0)           