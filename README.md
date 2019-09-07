# Automatic phonetic transcription of the Czech, Slovak and Polish languages
This repository contains codes of rule-based approach to the phonetics transcription of the Czech, Slovak and Polish languages into the [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) (IPA). Used rules and IPA signs are based on the phonologic, phonetic, and orthoepic studies (listed below) of the mentioned West-Slavic languages.

`CHANGELOG.txt` contains list of changes in each version. Current version is this one (version 1).

## Usage
These scripts can be used both as imported in any project, and as shell scripts. Bellow, three examples how to use them are shown.

**1. Import as the function to your Python3 project.**
```python
from phon_czech import ipa_czech
from phon_slovak import ipa_slovak
from phon_polish import ipa_polish

word1 = ipa_czech('všichni')
text1 = ipa_czech('Všichni lidé rodí se svobodní a sobě rovní co do důstojnosti a práv.')

word2 = ipa_slovak('všetci')
text2 = ipa_slovak('Všetci ľudia sa rodia slobodní a rovní si do dôstojnosti a práv.')

word3 = ipa_polish('wszyscy')
text3 = ipa_polish('Wszyscy ludzie rodzą się wolni i równi pod względem godności i praw.')

print(word1, word2, word3, sep='\n')
print(text1, text2, text3, sep='\n')
```

**2. Read from stdin in the shell pipeline.**
```bash
echo -e 'všichni' | python3 phon_czech.py
echo -e 'Všichni lidé rodí se svobodní a sobě rovní co do důstojnosti a práv.' | python3 phon_czech.py

echo -e 'všetci' | python3 phon_slovak.py
echo -e 'Všetci ľudia sa rodia slobodní a rovní si do dôstojnosti a práv.' | python3 phon_slovak.py

echo -e 'wszyscy' | python3 phon_polish.py
echo -e 'Wszyscy ludzie rodzą się wolni i równi pod względem godności i praw.' | python3 phon_polish.py
```

```bash
cat 'path-to-input-file' | python3 phon_czech.py
cat 'path-to-input-file' | python3 phon_slovak.py
cat 'path-to-input-file' | python3 phon_polish.py
```

**3. Read from file in shell pipeline.**
```bash
python3 phon_czech.py 'path-to-input-file'
python3 phon_slovak.py 'path-to-input-file'
python3 phon_polish.py 'path-to-input-file'
```

## Based on these studies
- BALOWSKI, Mieczysław. 1993. Fonetika a fonologie současné polštiny. Praha: Karolinum. ISBN: 80-7066-793-1.
- DUDÁŠOVÁ-KRIŠŠÁKOVÁ, Júlia. 1999. Fonologický systém spisovnej slovenčiny a poľštiny z typologického hľadiska. Slavica Slovaca. 34(1), 16-24. ISSN: 0037-6787.
- KAJANOVÁ-SCHULZOVÁ, Oľga. 1970. Úvod do fonetiky slovenčiny. Bratislava: Slovenské pedagogické nakladateľstvo.
- KRÁĽ, Ábeľ; SABOL, Ján. 1989. Fonetika a fonológia. Bratislava: Slovenské pedagogické nakladateľstvo. ISBN: 80-08-00036-8.
- KRČMOVÁ, Marie. 2016. Úvod do fonetiky a fonologie pro bohemisty. Ostrava: Universitas Ostraviensis. ISBN: 978-80-7368-636-9.
- KRČMOVÁ, Marie. 2017. TRANSKRIPCE. In: Petr Karlík, Marek Nekula, Jana Pleskalová (eds.), CzechEncy - Nový encyklopedický slovník češtiny.
URL: https://www.czechency.org/slovnik/TRANSKRIPCE.
- KRČMOVÁ, Marie. 2017. ORTOEPIE. In: Petr Karlík, Marek Nekula, Jana Pleskalová (eds.), CzechEncy - Nový encyklopedický slovník češtiny.
URL: https://www.czechency.org/slovnik/ORTOEPIE.
- LIPOWSKI, Jaroslav. 2011. Operatívna fonetika slovenčiny, češtiny a poľštiny. Wrocław: Wydawnictwo Uniwersytetu Wrocławskiego. ISBN: 978-80-7294-511-5.
- LOTKO, Edvard. 1999. Ke konfrontaci příbuzných jazyků. In: Srovnávací a bohemistické studie. Olomouc: Vydavatelství Univerzity Palackého, 9-19. ISBN: 978-80-244-2201-5.
- PALKOVÁ, Zdena. 1994. Fonetika a fonologie češtiny. Praha: Karolinum. ISBN: 80-7066-843-1.
- PAULINY, Eugen. 1979. Slovenská fonológia. Bratislava: Slovenské pedagogické nakladateľstvo.
- ZEMAN, Jiří. 2008. Základy české ortoepie. Hradec Králové: Gaudeamus. ISBN: 978-80-7041-778-2.

- Fonetická transkripce češtiny. Fonetický ústav, Filozofická fakulta, Univerzita Karlova. URL: https://fonetika.ff.cuni.cz/o-fonetice/foneticka-transkripce/o-foneticke-transkripci/.
- International Phonetic Alphabet. URL: https://www.internationalphoneticassociation.org/redirected_home.
