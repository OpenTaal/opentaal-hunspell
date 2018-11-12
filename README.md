# hunspell-nl

Dutch language support for Hunspell


# Generation from old database

Go on the server to `/var/www/opentaal.nl/www/htdocs/opentaalbank/spellingcontrole/next_version/genereer`

Run `genereer.sh` which does:
1. set version number and date
2. run `export_dic.pbp` which does:
    1.
    2.
    3.
3. copy `../new.aff.mdl` with replaced date and version number to `new.aff`
4. run `update_aff.pbp` which does:
    1. 
    2.
    3.
5. copy `new.aff` to `..`
6. wait for user to press `Enter`
7. run `export_woordenlijst.php`, which does
    1. 
    2.
    3.
8. run `hunspell` for dictionary `new` and print lines with misspelled words, sort these and store them in `gemist.txt`
9. list the words from `gemist.txt`
10. wait for user to press `Enter`


# Important tables in database

## words_list

Most important table is `opentaal.words_list` holding the words. It has fields:
* `word` for the actual word
* `ebg` for entry in old *elektronisch groene boekje*
* `2_10` for classification for version 2.10 (the latest version)
* `next_version` for classification for version 2.20 (the upcomming version)
* `opm_publicatie` for publication remarks such as registered trademark, see also `aantekeningen`
* `woordtype` for free/unmanaged word type
* `shorttage` for tags such as:
    * `` (~991923) for *none*
    * `---` (~1518) for 
    * `NN1d` (~1320) for 
    * `NN1h` (~342) for 
    * `NN1r` (~116) for 
    * `NN2` (~432) for 
    * `NN2r` (~180) for 
* `base_word` for base word such as:
    * `` (~956024) for *none*
    * `aflossen` (~8)
    * `afstevenen` (~6)
    * ...
    * mostly (~1)
* `alternatief` for alternative word and correction such as:
    * `` (~889210) for *none*
    * `-` (~5902) for spelling errors (`next_version` == `1`) that do not have a correction
    * `zó` (~13)
    * `geïnteresseerd` (~7)
    * ...
    * mostly (~1)
* `aantekeningen` for editor remarks such as rules, see also `opm_publicatie`
* `exclude_spell_checker` for words that should not be used in spell checking, often with an alternative (this was previously *verwarrend*) such as:
    * `handenschudden`
    * `puisje`
    * `daggen`
    * `gebeiden`
    * `win-win`
    * ...


## word_status

Description of all values that may be used in `2_10` and `next_version`. Useful. Used to be used by web interfaces.


## hunspell_rep

Replacements for Hunspell. Still in use. ~


## hunspell_dic and hunspell_dic_210G_20110926`

Words with flags for Hunspell. Still in use. ~173578 entries


# Less-important tables in database


## admin_*

Tables for users, groups and keeping payments done by sponsors.


## words

Table only for optimization. Has only `word` and `id`. Not sure if still up to date. Better not edit or use this table.


## words_counting and words_frequencies

Old tables with word frequency from sources, Google, etc. Not updated for a while. Better not use this anymore.


## words_meaning* and meaning*

Tables for the thesaurus. Many are outdated. Better not use these but to process them when moving to new thesaurus.


## woordtypes

POS tags (part-of-speech tags) used in web interfaces.


## woordsuggesties

Crowd sourced corrections for harvested sentences. Has a lot of noise. Better not use this anymore.


## synset_types

Synsets for old thesaurus. Are identical to top-level POS tags. Do not edit this table.


## stats_thesaurus

Statistics on usage of old thesaurus. Do not edit, do not use.


## statistics

Statistics on words found in harvested sentences but also pages processed by the harvester. Do not edit, do not use.


## RFC and RFC_test

Tables used for user feedback. Keep this. Important for historical decisions. Still in use. Should move to GitHub issues.


## LT_rules and language_tools_*

Rules for LanguageTool. Do not edit or use anymore. All rules are currently in XML files in LanguageTool repository.
