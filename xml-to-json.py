import xmltodict
import pprint
import json

f = open("person.json","w+")

with open('person.xml') as fd:
    doc = xmltodict.parse(fd.read())

f.write(json.dumps(doc))

f.close()
