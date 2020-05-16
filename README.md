**DO NOT USE THIS, THIS IS UNDER HEAVY DEVELOPMENT!**

_for English, please see below_


# Nederlandse spellingcontrole

Dit is de Nederlandse spellingcontrole van
[Stichting OpenTaal](https://www.opentaal.org). Mits aan volledige
bronvermelding wordt gedaan en de licenties worden gerespecteerd, is deze lijst
vrij te gebruiken. De exacte voorwaarden zijn te vinden in het bestand
[LICENSE](LICENSE). Lees deze goed door.

![logo Stichting OpenTaal](images/logo-shape-white-640x360.png?raw=true)

Deze spellingcontrole is samengesteld door ontelbare individuele bijdragen,
specifieke delen uit bronnen zonder auteursrecht en intensieve eindredactie. De
spellingcontrole heeft van de [Taalunie](http://taalunie.org) het
[Keurmerk Spelling](http://taalunieversum.org/inhoud/spelling-meer-hulpmiddelen/keurmerk)
gekregen. Dit betekent dat de woorden in deze spellingcontrole voldoen aan de
officiële spelling.

![logo Keurmerk Spelling](images/keurmerk.png?raw=true)

Het Keurmerk Spelling voor deze spellingcontrole is van medio 2017, 2018. Sinds
eind 2018 wordt dit keurmerk niet meer uitgegeven en zal bij volgende versies
van deze spellingcontrole niet meer van toepassing zijn.


## Inhoud

TODO


## Scripts en directories

In de directorie `scripts` zijn een aantal scripts te vinden voor het
analyseren en ontwikkelen van een nieuwe spellingcontrole. Deze scripts moeten
vanuit die directorie worden gerunt.

Het script `1-download.sh` haalt de laatste exports van de database op en slaat
die op in de directorie `downloads`. Daar komen ook de spellingcontrole en de
woordenlijst van versie 2.1 te staan.

In de directorie `parts` staan de bestanden die samen met inhoud van de
bestanden in de directorie `input` staan door het script `2-combine.sh` worden
gecombineerd tot de bestanden `nl.dic` en `nl.aff` die in de hoogste directorie.
Dat is de versie 2.2.

Een vergelijking kan gemaakt worden met het script `3-compare.sh`, die output
daarvan wordt opgeslagen in de directory `comparison`. Om makkelijk de
verschillen te bekijken worden beide versies eerst van commentaar en witruimte
gestript.

    sudo apt-get install npm
    sudo npm install -g diff2html-cli

TODO



Romeinse cijfers zitten in de collectie maar zijn aangemerkt met uitsluiten van
spellingcontrole omdat het affix bestand deze direct ondersteunt.

TODO Ook Romeinse cijfers in kleine letters aan collectie toevoegen?


TODO

# Dutch spell checker

This is the Dutch spell checker by [Stichting OpenTaal](https://www.opentaal.org).
As long as full attribution is provided and the licenses are being respected,
this spell checker can be used freely. The exact conditions can be found in the
file [LICENSE.txt](LICENSE.txt). Please, read these carefully.

![logo Stichting OpenTaal](images/logo-shape-white-640x360.png?raw=true)

This spell checker has been compiled from countless individual contributions,
specific parts from sources without copyright and intense final editing. This
spell checker has received from the Dutch Language Union
([Taalunie](http://taalunie.org)) the Quality Mark Spelling
([Keurmerk Spelling](http://taalunieversum.org/inhoud/spelling-meer-hulpmiddelen/keurmerk)).
This means that the words in this spell checker are according to the official spelling.

![logo Keurmerk Spelling](images/keurmerk.png?raw=true)

The Quality Mark Spelling for this spell checker has been given in 2017/2018.
This quality mark has stopped since the end of 2018 and will not apply to future
releases of this spell checker.


## Contents

_Please, see the relevant section in Dutch_





**Ignore rest of this file!!**

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

* `flags`:
    * `` (~71520) for *none*
    * `P`
        * `PN` (~16878) for poper noun such as Aagje, Aalbers, Zwols, Zweverink
    * `F`
        * `Fw` (~10515) for ? such as woonzorgterrein, brandweer, Mexico-stad, luisterend, woonzorgservices, wereldhockeybond. Words labelled in `aantekeingen` with `onzinsuggestie` such as 3-koorts, pre-pais, 3D-speler, vervuilringen, wonderdekking, VLO-, Elite-, -0, -1, -9-regeling, -A4, A-oever. (no idea if this is relevant)
    * `Z`
        * `Za` (~15992) for compounds? such as 's-Gravenhagenaar, 06-nummer, AOW'er, à-la-carterestaurant, zwerfvuilactie, zwerfster

### `Zb` (~13058) meervoud kruisproductsuffix `en`, `ën`, `en-` of `ën-`

`tuin` → `tuinen`

### `Zd` (~411) meervoud `heid` met vervangende kruisproductsuffix `heden` of `heden-`

`schoonheid` → `schoonheden`



        * `Ze` (~4080) for
        * `Zf` (~1697) for
        * `Zc` (~1491) for
        * `Zh` (~1463) for
        * `Zj` (~35) for nouns of which pluras get `n` added? such as IJsheilige, alleenstaande, dakloze, weersdeskundige, werktuigboukundige
        * `Zu` (~13) for ? such as dialecticus, gnosticus, ssytematicus (plural gets `ca` removed and `i` added?)
    * `V`
        * `Vi` (~7732) for
        * `Ve` (~3546) for
        * `V3` (~) for stam?
        * `Vq` (~) for (lot of double VqVq, what to do with those?)
        * `Vp` (~) for  
        * `Ve` (~) for voltooid deelwoord?
        * `Vi` (~) for infinitief?
    * `C`
        * `CA` (~) for
        * `CB` (~) for
        * `C0` (~) for
        * `Cl` (~) for *initiaalwoorden* starting with upper case character such as Vwo, Lpg, H5N1, E and Bh.
    * `Y`
        * `Yb` (~) for

### `A` Adjectief (bijvoeglijk naamwoord)

`ts:AJn` stellende trap is de stam, alle regels staan kruisproduct toe

#### `Aa` (~6676) verbogen stellende trap `ts:AJe`

1. `viezig` → `viezigE`
2. `moE` → `moeË`

#### `Ab` (~2350) vergrotende trap `ts:AJcn`

1. `lelijk` → `lelijkER`
2. `raaR` → `raarDER`

#### `Ac` (~764) verbogen vergrotende trap `ts:AJce`

1. `lelijk` → `lelijkERE`
2. `doR` → `dorDERE`

#### `Ad` (~1229) overtreffende trap `ts:AJsn`

1. `lelijk` → `lelijkST`
2. `zinlooS` → `zinloosT`

#### `Ae` (~1238) verbogen overtreffende trap `ts:AJse`

1. `lelijk` → `lelijkSTE`
2. `zinlooS` → `zinloosTE`

#### `A0` continuation class voor `Ad` en `Ae` let op `ts:` wordt uitgesteld 1x

`Ad`: `lelijkst` → `ALLERlelijkst`
`zinloost` → `ALLERzinloost`

`Ae`: `lelijkste` → `ALLERlelijkste` maar geen gebruik flag in dictionary voor `allerzinlooste`

#### `Ai` (~531) s-vorm `ts:i`

1. `lelijk` → `lelijks`

#### `Al` (~1863) verbogen stellende trap `ts:AJe`

1. `aerOOB` → `aeroBE`
2. `kwAAD` → `kwaDE`
3. `brEED` → `breDE`
4. `rOOD` → `roDE`
5. `brAAF` → `braVE` (f->v)
6. `dOOF` → `doVE` (f->v)
7. `trAAG` → `traGE`
8. `lEEG` → `leGE`
9. `hOOG` → `hoGE`
10. `rAAK` → `raKE`
11. `wEEK` → `weKE`
12. `*OOK` → niet gebruikt
13. `vAAL` → `vaLE`
14. `gEEL` → `geLE`
15. `anabOOL` → `anaboLE`
16. `eenzAAM` → `eenzaME`
17. `slOOM` → `sloME`
18. `postUUM` → `postuME`
19. `urbAAN` → `urbaNE`
20. `autogEEN` → `autogeNE`
21. `ultrasOON` → `ultrasoNE`
22. `vloeibAAR` → `vloeibaRE`
23. `gOOR` → `goRE`
24. `hEES` → `heSE` (let op: niet heze)
25. `kordAAT` → `kordaTE`
26. `hEET` → `heTE`
27. `grOOT` → `groTE`
28. `vOOS` → `voZE` (s->z)
29. `confUUS` → `confuSE`

#### `Am` (~69) verbogen stellende trap `ts:AJe`

1. `industrIEEL` → `industriËLE`

#### `An` (~301) verbogen stellende trap `ts:AJe`

1. `glaD` → `gladDE`
2. `doF` → `dofFE`
3. `stuG` → `stugGE`
4. `druK` → `drukKE`
5. `boL` → `bolLE`
6. `laM` → `lamME`
7. `miN` → `minNE`
8. `neP` → `nepPE`
9. `doR` → `dorRE`
10. `roS` → `rosSE`
11. `zoT` → `zotTE`

#### `Ao` (~138) vergrotende trap `ts:AJc`

1. `glaD` → `gladDER`
3. `maF` → `mafFER`
3. `stuG` → `stugGER`
4. `vlaK` → `vlakKER`
5. `zinvoL` → `zinvolLER`
6. `doM` → `domMER`
7. `duN` → `dunNER`
8. `raP` → `rapPER`
9. `.*R` → `rRER` geen gebruik
10. `loS` → `losSER`
11. `zaT` → `zatTER`

#### `Ap` (~47) verbogen vergrotende trap `ts:AJce`

1. `glaD` → `gladDERE`
2. `maF` → `mafFERE`
3. `stuG` → `stugGERE`
4. `vlaK` → `vlakKERE`
5. `zinvoL` → `zinvolLERE`
6. `doM` → `domMERE`
7. `duN` → `dunNERE`
8. `raP` → `rapPERE`
9. `.*R` → `rRERE` geen gebruik
10. `loS` → `losSERE`
11. `zaT` → `zatTERE`

#### `Aq` vergrotende trap `ts:AJcn`

1. `aerOOB` → `aeroBER`
2. `kwAAD` → `kwaDER`
3. `brEED` → `breDER`
4. `rOOD` → `roDER`
5. `brAAF` → `braVER` (f->v)
6. `dOOF` → `doVER` (f->v)
7. `trAAG` → `traGER`
8. `lEEG` → `leGER`
9. `hOOG` → `hoGER`
10. `rAAK` → `raKER`
11. `wEEK` → `weKER`
12. `*OOK` → niet gebruikt
13. `vAAL` → `vaLER`
14. `gEEL` → `geLER`
15. `anabOOL` → `anaboLER`
16. `eenzAAM` → `eenzaMER`
17. `slOOM` → `sloMER`
18. `postUUM` → `postuMER`
19. `urbAAN` → `urbaNER`
20. `autogEEN` → `autogeNER`
21. `ultrasOON` → `ultrasoNER`
22. `hEES` → `heSE` (let op: niet heze)
23. `kordAAT` → `kordaTE`
24. `hEET` → `heTE`
25. `grOOT` → `groTE`
26. `vOOS` → `voZE` (s->z)
27. `confUUS` → `confuSE`

#22. `vloeibAAR` → `vloeibaarDER`
#23. `gOOR` → `goorDER`

#### `Ar`

#### `As`

#### `At`

#### `Au`

#### `Av`

#### `Aw`

#### `Ax`

    * `N` numbers
        `N7` (~18) rangtelwoord, ordinale, EN ordinal number such as eerste, tweede, derde, ..., negentiende

# Less-important tables in database


## admin_*

Tables for users, groups and keeping payments done by sponsors.


## words

Table only for optimization. Has only `word` and `id`. Not sure if still up to date. Better not edit or use this table.


## freqTotal, words_counting and words_frequencies

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


## domains

List of domain names harvested. Not very relevant anymore.


## base_jargon and base_status

Probably once intended to be used in LanguageTool.
