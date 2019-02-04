# Making dictionaries

There are several ways to make dictionaries quickly. HOWEVER always make sure that the results make sense and edit out any false positives. 

## edit by hand
The editor can use a JSON (or XML) editor to create the dictionary by hand. However these are not constrained by schems so it is easy 
to make mistakes. It is useful to have a JSON editor such as https://jsoneditoronline.org/ .

## use ami-dictionary
The `ami-dictionary` command can generate dictionaries from a variety of inputs. Wherever possible the terms should be linked to 
Wikipedia or Wikidata. You must have the `ami20190204` (or later) release in http://github.com/petermr/ami-jars. To run, 
use:
```
ami-dictionary [options]
```
where options  are defined below. Note that lines are broken `\` for readability but the command can be put on a single line.

## List of terms

The editor selects a set of terms and copied them into the command:
```
ami-dictionaries create \
	    --dictionary plantvirusesA \
	    --directory /Users/pm286/ContentMine/dictionaries/testvirus \
      --out
		--terms \
Alfamovirus,Allexivirus,Alphacryptovirus,Ampelovirus,Anulavirus,Apscaviroid,Aureusvirus,Avenavirus,Avsunviroid,Badnavirus,Begomovirus,Benyvirus,\
Betacryptovirus,Betaflexiviridae,Bromovirus,Bymovirus,Capillovirus,Carlavirus,Carmovirus,Caulimovirus,Cavemovirus,Cheravirus,Closterovirus,\
Cocadviroid,Coleviroid,Comovirus,Crinivirus,Cucumovirus,Curtovirus,Cytorhabdovirus,Dianthovirus,Enamovirus,Fabavirus,Fijivirus,Furovirus,\
Hordeivirus,Hostuviroid,Idaeovirus,Ilarvirus,Ipomovirus,Luteoviridae,Machlomovirus,Macluravirus,Marafivirus,Mastrevirus,Nanovirus,Necrovirus,\
Nepovirus,Nucleorhabdovirus,Oleavirus,Ophiovirus,Oryzavirus,Panicovirus,Pecluvirus,Petuvirus,Phytoreovirus,Polerovirus,Pomovirus,Pospiviroid,\
Potexvirus,Potyviridae,Potyvirus,Reoviridae,Rhabdoviridae,Rymovirus,Sadwavirus,Sequivirus,Sobemovirus,Tenuivirus,Tobamovirus,Tobravirus,\
Tombusviridae,Tombusvirus,Topocuvirus,Tospovirus,Trichovirus,Tritimovirus,Tungrovirus,Tymovirus,Umbravirus,Unassigned,Varicosavirus,Vitivirus,Waikavirus	
```
This creates a dictionary `plantvirusesA.xml` (default format) in directory `/Users/pm286/ContentMine/dictionaries/testvirus` containing ca 84 entries.
(Please check this). 

## create from Wikipedia List
This is one of the best approaches. Many pages are labelled "List_of_xxx" and `ami-dictionary` can extract this automatically. It's normally a table
(so use `wikitable`) and pick the column (`namecol`). Sometimes there is another column with links and you can add `--linkcol` to add this.
Note the use of `outformats`. The HTML is not directly usable but is very readable and a good way of making sure the dictionary makes sense - 
it even has pictures.
The rest is similar to the previous.
```
ami-dictionaries create\
 --hreftext \
	 --input  https://en.wikipedia.org/wiki/List_of_Indian_spices \
	 --informat  wikitable \
	 --namecol 'Standard English'\
	 --dictionary spices\
	 --outformats  xml,json,html \
	 --directory testdir/
```

## create from Wikipedia Category

This is also very useful if you can find it as it is guaranteed that most of the entries will be relevant and homogeneous
```
ami-dictionaries create\
 --hreftext \
	 --input  https://en.wikipedia.org/wiki/Category:Monoterpenes \
	 --informat  wikicategory \
	 --dictionary monoterpenes\
	 --outformats  xml,json,html \
	 --directory testdir/
```
## create from Wikipedia page
This picks all the Wikipedia links from the page. There will certainly be false positives and page will require editing
```
ami-dictionaries create\
 --hreftext \
 --input https://en.wikipedia.org/wiki/Plant_virus\
 --informat wikipage\
 --dictionary plantvirusesB \
 --outformats xml
 ```
 
