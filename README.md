<div id="top"></div>

<!-- PROJECT SHIELDS -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">UzTransliterator | State-of-the-art machine transliteration tool for Uzbek language, Cyrillic<>Latin<>NewLatin</h3>
  <p align="center">
    The main goal of this paper is to present a state-of-the-art machine transliteration tool between three common scripts used in low-resource Uzbek language: old Cyrillic, currently official Latin, and newly announced New-Latin alphabets, which was created using a combination of rule-based and statistical approaches. The created tool is available as an open-source Python package, as well as a web-based application including a public API
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="https://github.com/UlugbekSalaev/UzTransliterator/blob/main/src/web-uinterface.png?raw=true" width = "600" Alt = "Web-interface of the tool">
</div>


Feel free to use the tool presented in this project, and if you find it useful, plese make sure to cite the paper [here](...) (coming soon...)
Demo of the web-based transliteration tool can be seen [here](https://nlp.urdu.uz/?menu=translit).


In this paper, we presented a Python code, a web tool, and an API created for the Uzbek language that performs machine transliteration between two popularly used Cyrillic and Latin alphabets, as well as a newly reformed version of the Latin alphabet, which, according to the governmental decree, all legal texts will have been completely adapted to by year 2023.

<p align="right">(<a href="#top">back to top</a>)</p>

## Installation
### Python
<code>pip install UzTransliterator</code>
<br><br><b>Source:</b> https://pypi.org/project/UzTransliterator/
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
 https://nlp.urdu.uz/?menu=translit
    
### API
<b>URL:</b> https://uz-translit.herokuapp.com/translit
<br><br><b>Methods:</b> GET, POST<br><br><b>Parametres:</b> <code>text:str</code>, <code>from_:str</code>, <code>to:str</code>
<br><br><b>Example Request:</b> https://uz-translit.herokuapp.com/translit?text=мактаб&from_=cyr&to=lat

## Note
New latin alphabet has some difference than Latin. Main changing is presented in following as format Latin - New Latin:
<br>“G‘, g‘” — “Ḡ, ḡ”
<br>“O‘, o‘” — “Ō, ō”
<br>“Sh, sh” — “Ş, ş”
<br>“Ch, ch” — “Ç ç”

### Built With

Programming language used:

* [Python](https://www.python.org/)

These are the major libraries used inside Python:

* [scikit-learn : A set of python modules for machine learning](https://scikit-learn.org/stable/)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
