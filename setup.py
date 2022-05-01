import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UzTransliterator",
    version="0.0.24",
    author="Ulugbek Salaev, Elmurod Kuriyozov",
    author_email="ulugbek0302@gmail.com, e.kuriyozov@udc.es",
    description="UzTransliterator | Transliteration tool for Uzbek language - Cyrillic<>Latin<>NewLatin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UlugbekSalaev/UzTransliterator",
    project_urls={
        "Bug Tracker": "https://github.com/UlugbekSalaev/UzTransliterator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['python', 'transliteration', 'uzbek-language', 'cyrillic', 'latin'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
    python_requires=">=3.6",
    include_package_data=True,
    package_data={"": ["*.csv"]},
    #package_data={"": ["cyr_exwords.csv", "lat_exwords.csv"],},
)