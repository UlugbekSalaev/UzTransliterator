<div id="top"></div>

<br />
<div align="center">
  <h2 align="center">UzTransliterator</h2>
  <h4 align="center">State-of-the-art Machine Transliteration Tool for Uzbek Language (Cyrillic ↔ Latin ↔ New Latin)</h4>
  <p align="center">
    UzTransliterator is an open-source Python package that provides high-accuracy, rule-based machine transliteration between the three writing scripts of the Uzbek language: <b>Cyrillic</b>, <b>Latin</b>, and <b>New Latin</b>.
  </p>
</div>

---

##  Features

- **Transliteration Between 3 Uzbek Scripts**: Full support for bidirectional transliteration between all 3 writing scripts used in Uzbek: `cyr` (Cyrillic), `lat` (Latin), and `nlt` (New Latin).
- **Rule-based & Statistical Engine**: Correctly handles context-sensitive rules (such as `Е/е`, `Ц/ц`, `Ё/Ю/Я`, Roman numerals, dates, hyphenation, and exception words).
- **Lightweight & Fast**: Direct Python library execution without external API dependencies.

---

## Installation

Install the package via PyPI:

```bash
pip install UzTransliterator
```

---

## Usage

```python
from UzTransliterator import UzTransliterator

# Initialize transliterator object
obj = UzTransliterator()

# Transliterate from Cyrillic to Latin
latin_text = obj.transliterate("мактаб", from_="cyr", to="lat")
print(latin_text)  # Output: maktab

# Transliterate from Cyrillic to New Latin (Yangi Lotin)
new_latin_text = obj.transliterate("Ўзбекистон шаҳарлари va g‘azal", from_="cyr", to="nlt")
print(new_latin_text)  # Output: Özbekiston şaharlari va g‘azal

# Transliterate from Latin to New Latin
nlt_text = obj.transliterate("O‘zbekiston, g‘alaba, shahar, chelak", from_="lat", to="nlt")
print(nlt_text)  # Output: Özbekiston, ğalaba, şahar, çelak

# Transliterate from New Latin to Cyrillic
cyr_text = obj.transliterate("Özbekiston şaharlari", from_="nlt", to="cyr")
print(cyr_text)  # Output: Ўзбекистон шаҳарлари
```

### Script Direction Options (`from_` and `to`)

Supported script codes:

- `cyr` — Cyrillic (Кирилл)
- `lat` — Latin (Lotin)
- `nlt` — New Latin (Yangi Lotin)

Available direction pairs:

- `from_='cyr', to='lat'`
- `from_='cyr', to='nlt'`
- `from_='lat', to='cyr'`
- `from_='lat', to='nlt'`
- `from_='nlt', to='cyr'`
- `from_='nlt', to='lat'`

---

## Web Interface

**[https://uzmorph.uz/models/uztranslit](https://uzmorph.uz/models/uztranslit)**

---

## New Latin Alphabet Reform (Yangi Lotin)

According to the reformed Uzbek Latin alphabet legislation, character mappings are updated as follows:

|      Latin      |   New Latin   | Cyrillic Equivalent |
| :--------------: | :------------: | :-----------------: |
| `G‘`, `g‘` | `Ğ`, `ğ` |   `Ғ`, `ғ`   |
| `O‘`, `o‘` | `Ö`, `ö` |   `Ў`, `ў`   |
|  `Sh`, `sh`  | `Ş`, `ş` |   `Ш`, `ш`   |
|  `Ch`, `ch`  | `Ç`, `ç` |   `Ч`, `ч`   |

---

## Scopus Publication & Citation

If you use `UzTransliterator` in your academic research or projects, please cite our Scopus-indexed research paper:

> **Salaev, U., Kuriyozov, E., & Gómez-Rodríguez, C.** (2022). *A Machine Transliteration Tool Between Uzbek Alphabets*. CEUR Workshop Proceedings, Vol-3315, pp. 42–50.

📄 **Scopus Link**: [https://www.scopus.com/inward/record.uri?eid=2-s2.0-85146119140&amp;partnerID=40&amp;md5=be670d829670d883b2f8326559ce954a](https://www.scopus.com/inward/record.uri?eid=2-s2.0-85146119140&partnerID=40&md5=be670d829670d883b2f8326559ce954a)

```bibtex
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

---

## License

Distributed under the MIT License. See `LICENSE` for details.

<p align="right">(<a href="#top">back to top</a>)</p>
