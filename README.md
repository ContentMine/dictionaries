# dictionaries
Dictionaries for use with `ami` as well as with `canary`. Provided as xml files and now also JSON.

To contribute simply fork and make a pull request with a new dictionary. Ideally include some external identifier (particularly Wikidata) for each term if possible. For inspiration see this: [blog post](http://discuss.contentmine.org/t/building-a-new-facet-from-wikidata/237). By Chris Kittel about making a dictionary for species from Wikidata.

Either XML or JSON is fine.

Looks something like:
```
<dictionary title="baz">
<entry term="foo" name="bar" id="1234" wikidataId="Q1234" />
</dictionary>
```

id and wikidataId  are not required

A rough description of the contents is as follows
* cochrane - short list of terms that may be of interest to or about Cochrane
* disease - list of diseases, origin currently unknown perhaps wikidata
* epidemic - very short list relating to epidemics
* funders - list of funders provided by CrossRef
* hgnc - list of human genes perhaps from NIH?
* inn - list of generic drug names from ChEBI
* jax - list of mouse genes
~ synbio - list of synthetic biology terms, handwritten
* taxdumpGenus - list of taxonomic genus, source unknown
* tropicalVirus - list of tropical viruses, handwritten
