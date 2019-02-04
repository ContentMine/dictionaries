#! /bin/sh
#	
ami-dictionaries create \
	    --dictionary plantvirusesA \
	    --directory /Users/pm286/ContentMine/dictionaries/testvirus \
		--terms \
Alfamovirus,Allexivirus,Alphacryptovirus,Ampelovirus,Anulavirus,Apscaviroid,Aureusvirus,Avenavirus,Avsunviroid,Badnavirus,Begomovirus,Benyvirus,\
Betacryptovirus,Betaflexiviridae,Bromovirus,Bymovirus,Capillovirus,Carlavirus,Carmovirus,Caulimovirus,Cavemovirus,Cheravirus,Closterovirus,\
Cocadviroid,Coleviroid,Comovirus,Crinivirus,Cucumovirus,Curtovirus,Cytorhabdovirus,Dianthovirus,Enamovirus,Fabavirus,Fijivirus,Furovirus,\
Hordeivirus,Hostuviroid,Idaeovirus,Ilarvirus,Ipomovirus,Luteoviridae,Machlomovirus,Macluravirus,Marafivirus,Mastrevirus,Nanovirus,Necrovirus,\
Nepovirus,Nucleorhabdovirus,Oleavirus,Ophiovirus,Oryzavirus,Panicovirus,Pecluvirus,Petuvirus,Phytoreovirus,Polerovirus,Pomovirus,Pospiviroid,\
Potexvirus,Potyviridae,Potyvirus,Reoviridae,Rhabdoviridae,Rymovirus,Sadwavirus,Sequivirus,Sobemovirus,Tenuivirus,Tobamovirus,Tobravirus,\
Tombusviridae,Tombusvirus,Topocuvirus,Tospovirus,Trichovirus,Tritimovirus,Tungrovirus,Tymovirus,Umbravirus,Unassigned,Varicosavirus,Vitivirus,Waikavirus	

# create from Wikipedia page
ami-dictionaries create\
 --hreftext \
 --input https://en.wikipedia.org/wiki/Plant_virus\
 --informat wikipage\
 --dictionary plantvirusesB \
 --outformats xml

# create from Wikipedia List
ami-dictionaries create\
 --hreftext \
	 --input  https://en.wikipedia.org/wiki/List_of_Indian_spices \
	 --informat  wikitable \
	 --namecol 'Standard English'\
	 --linkcol 'Standard English'\
	 --dictionary spices\
	 --outformats  xml,json,html \
	 --directory testdir/

# create from Wikipedia Category
ami-dictionaries create\
 --hreftext \
	 --input  https://en.wikipedia.org/wiki/Category:Monoterpenes \
	 --informat  wikicategory \
	 --dictionary monoterpenes\
	 --outformats  xml,json,html \
	 --directory testdir/
	
	
