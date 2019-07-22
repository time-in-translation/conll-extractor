# CONLL-extractor

The scripts in this project allow to extract various forms of interest from files in the [CONLL-U (Universal Dependencies) format](https://universaldependencies.org/format.html). The scripts are heavily dependent upon the [pyconll](https://github.com/pyconll/pyconll) library.

## Available scripts

### Indefinites

This script allows to extract noun phrases that start with an indefinite article (e.g. *a dog*, *an hour*).  

### Prepositions

This script allows to extract prepositional phrases, in either uncontracted (*in* ***das*** *Auto*) or contracted form (*in****s*** *Auto*).

## Installation

First, install the requirements via:

    $ pip install -r requirements.txt

Then, create the executable `conll-extract` via:    
 
    $ pip install --editable .

## Examples

### Indefinites

The script to extract indefinites is straightforward:

    $ conll-extract indefinites <filename>.conllu
    
The extracted indefinites can be found in `<filename>.csv`. 

### Prepositions

The script to extract prepositional phrases has some additional parameters:

    $ conll-extract --help
    
    Usage: conll-extract [OPTIONS] [indefinites|prepositions] [FILES]...
    
    Options:
      --contracted  Whether to extract contracted (e.g. ins Auto) or uncontracted
                    (e.g. in das Auto) PPs
      --filter_pps  Whether to filter the PPs based on a list of preposition-noun
                    combinations
      --help        Show this message and exit.

    $ conll-extract prepositions <filename>.conllu
    
The extracted prepositional phrases can be found in `<filename>.csv`.
