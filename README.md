# CONLL-extractor

The scripts in this project allow to extract various forms of interest from files in the [CONLL-U (Universal Dependencies) format](https://universaldependencies.org/format.html). The scripts are heavily dependent upon the [pyconll](https://github.com/pyconll/pyconll) library.

## Available scripts

### Determiner phrases

This script allows to extract noun phrases that start with a definite (e.g. *the dog*, *the ongoing concern*) indefinite article (e.g. *a dog*, *an ongoing concern*).  

### Prepositions

This script allows to extract prepositional phrases, in either uncontracted (*in* ***das*** *Auto*) or contracted form (*in****s*** *Auto*).

## Installation

First, install the requirements via:

    $ pip install -r requirements.txt

Then, create the executable `conll-extract` via:    
 
    $ pip install --editable .

## Examples

### Determiner phrases

The script to extract determiners and their accompanying nouns has one additional parameter (optionally) filter for definite or indefinite noun phrases:

    $ conll-extract determiners <filename>.conllu
    
    Options:
      --definiteness [definite|indefinite]
        If set, limit the definiteness of noun phrases to definite or indefinite

The extracted noun phrases can be found in `<filename>.csv`.

### Nouns

The script to extract noun phrases has two additional parameter (optionally) filter for a specific dependency relation or the number of the noun:

    $ conll-extract nouns <filename>.conllu
    
    Options:
      --deprel TEXT
        If set, filter based on the dependency relation of the noun.
      --number [Coll|Count|Dual|Grpa|Grpl|Inv|Pauc|Plur|Ptan|Sing|Tri]
        If set, filter based on the number of the noun.

The extracted noun phrases can be found in `<filename>.csv`.

### Prepositions

The script to extract prepositional phrases has two additional parameters:

    $ conll-extract prepositions <filename>.conllu
    
    Options:
      --contracted 
        Whether to extract contracted (e.g. ins Auto) or uncontracted (e.g. in das Auto) PPs
      --filter_pps
        Whether to filter the PPs based on a list of preposition-noun combinations
    
The extracted prepositional phrases can be found in `<filename>.csv`.
