<div id="top"></div>

<!-- PROJECT SHIELDS -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">UzTransliterator | State-of-the-art machine transliteration tool for Uzbek language, Cyrillic<>Latin<>NewLatin</h3>
  <p align="center">
    The main goal of this paper is to present a state-of-the-art machine transliteration tool between three common scripts used in the low-resource Uzbek language: old Cyrillic, currently official Latin, and newly announced New-Latin alphabets (2026), which was created using a combination of rule-based and statistical approaches. The created tool is available as an open-source Python package, as well as a web-based application.
  </p>
</div>

Feel free to use the tools presented in this project; a paper about more details on creation and usage <a href='http://www.grupolys.org/biblioteca/SalKurGom2022b.pdf'>here</a>.<br>
If you find it useful, please make sure to cite the paper:
```
@CONFERENCE{Salaev202242,
	author = {Salaev, Ulugbek and Kuriyozov, Elmurod and Gómez-Rodríguez, Carlos},
	title = {A Machine Transliteration Tool Between Uzbek Alphabets},
	year = {2022},
	journal = {CEUR Workshop Proceedings},
	volume = {3315},
	pages = {42 – 50},
	url = {https://www.scopus.com/inward/record.uri?eid=2-s2.0-85146119140&partnerID=40&md5=be670d829670d883b2f8326559ce954a}
}
```

<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="https://github.com/UlugbekSalaev/UzTransliterator/blob/main/src/web-uinterface.png?raw=true" width = "600" Alt = "Web-interface of the tool">
</div>

In this paper, we present Python code, a web tool created for the Uzbek language that performs machine transliteration between two popularly used Cyrillic and Latin alphabets, as well as a newly reformed version of the Latin alphabet (2026), which, according to the governmental decree, all legal texts will have been completely adapted to by the year 2023.

<p align="right">(<a href="#top">back to top</a>)</p>

## Installation
### Python
<code>pip install UzTransliterator</code>
<br><b>Source:</b> https://pypi.org/project/UzTransliterator/
<br><br><b>Using</b><br>
<code>from UzTransliterator import UzTransliterator</code>
<br><code>obj = UzTransliterator.UzTransliterator()</code>
<br><code>print(obj.transliterate("маткаб", from_="cyr", to="lat"))</code>
<br>Output: <code>maktab</code>

### Options 
<code>from_='cyr', to='lat'</code><br>
<code>from_='cyr', to='nlt'</code><br>
<code>from_='lat', to='cyr'</code><br>
<code>from_='lat', to='nlt'</code><br>
<code>from_='nlt', to='cyr'</code><br>
<code>from_='nlt', to='lat'</code><br>

### Web Interface
https://uzmorph.uz/models/uztranslit
    
## Note
The new Latin alphabet has some differences from Latin. The main changes are presented below in the format Latin - New Latin:
<br>“G‘, g‘” — “Ḡ, ḡ”
<br>“O‘, o‘” — “Ō, ō”
<br>“Sh, sh” — “Ş, ş”
<br>“Ch, ch” — “Ç ç”

### Built With

Programming language used:

* [Python](https://www.python.org/)

These are the major libraries used inside Python:

* [scikit-learn : A set of Python modules for machine learning](https://scikit-learn.org/stable/)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
