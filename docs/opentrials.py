import json, csv

def reformat(rows, facetname):
    entries = []
    i=0
    headers = next(rows, None)
    for row in rows:
        #print(row)
        new = {}
        identifiers = json.loads(row[2])
        for id_source, id in identifiers.items():
            new["name"] = id
            new["identifiers"] = {}
            new["identifiers"]["opentrials"] = row[1]
            new["identifiers"]["contentmine"] = "CM."+facetname+str(i)
            entries.append(new)
            i+=1
    return entries

def make_facet(csvpath, facetname):
    with open(csvpath, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        entries = reformat(reader, facetname)
        facet= {}
        facet["id"] = "CM."+facetname
        facet["name"] = facetname
        facet["entries"] = entries
        return facet

facetname = "OpenTrialsOnlyTrialIDs" # give an appropriate one, e.g. "endangered"
new_facet = make_facet("/home/tom/Downloads/New_Query_2016_10_10.csv", facetname)

with open("{0}.json".format(facetname), "w") as outfile:
    json.dump(new_facet, outfile, indent=4)
