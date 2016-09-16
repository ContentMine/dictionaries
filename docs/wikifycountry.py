
import json

def enrich(termlist, facetname):
    """
    Iterate over a list of terms and add an enumerating identifier.
    """
    return [reformat(d, i, facetname) for i,d in enumerate(termlist) \
                                      if not digit_present(d.get("termLabel"))]

def digit_present(s):
    """
    Returns true for entities that have no common/scientific name in wikidata
    and get assigned something like 't307596644'.
    """
    return any(i.isdigit() for i in s)

def reformat(d, i, facetname):
    """
    Reformats the dictionaries into facets.
    """
    new = {}
    new["term"] = d.get("termLabel")
    new["name"] = d.get("termLabel")
    new["identifiers"] = {}
    # "https://www.wikidata.org/wiki/Q4661045" -> "Q4661045"
    new["identifiers"]["wikidata"] = d.get("term").split("/")[-1]
    new["identifiers"]["contentmine"] = "CM."+facetname+str(i)
    return new

def make_facet(wikidatajsonpath, facetname):
    """
    Reads downloaded JSON from a wikidata query,
    builds structure around a list of terms,
    returns facet.
    """
    with open(wikidatajsonpath) as infile:
        raw = json.load(infile)
        entries = enrich(raw, facetname)
        
        facet= {}
        facet["id"] = "CM."+facetname
        facet["name"] = facetname
        facet["entries"] = entries
        return facet

print ("transforming dictionaries")

facetname = "wikidatacountry" # give an appropriate one, e.g. "endangered"
new_facet = make_facet("/Users/pm286/workspace/dictionaries/json/wikidatacountry.raw.json", facetname)

with open("{0}.json".format(facetname), "w") as outfile:
    json.dump(new_facet, outfile, indent=4)

