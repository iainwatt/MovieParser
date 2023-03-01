#### To run locally
* cd /api
* export FLASK_APP=app.py
* export FLASK_ENV=development
* flask run
* to test: python3 -m pytest -rP

#### To deploy to Heroku
* pip3 freeze > requirements.txt
* git push heroku master

#### Planned improvements
* Add authentication
* Improve testing
* Add flask-sqlachemy
* Look into Flask-migrate or alembic for reading DB migrations (https://pypi.org/project/alembic/)
* Auto detect DB changes https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect
* Add Swagger docs
* Re-organize the app with Flask restful (https://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/)


#### Useful links
* [WiktionaryParser](https://github.com/Suyash458/WiktionaryParser)
* [SQL Alchemy](https://www.sqlalchemy.org/)


### Wiktionary Parser (Embedded within the Flask api wrapper)

A python project which downloads words from English Wiktionary ([en.wiktionary.org](https://en.wiktionary.org)) and parses articles' content in an easy to use JSON format. Right now, it parses etymologies, definitions, pronunciations, examples, audio links and related words.


#### JSON structure

```json
[{
    "pronunciations": {
        "text": ["pronunciation text"],
        "audio": ["pronunciation audio"]
    },
    "definitions": [{
        "relatedWords": [{
            "relationshipType": "word relationship type",
            "words": ["list of related words"]
        }],
        "text": ["list of definitions"],
        "partOfSpeech": "part of speech",
        "examples": ["list of examples"]
    }],
    "etymology": "etymology text",
}]
```



#### Usage

 - Import the WiktionaryParser class.
 - Initialize an object and use the `fetch("word", "language")` method.
 - The default language is English, it can be changed using the `set_default_language method`.
 - Include/exclude parts of speech to be parsed using `include_part_of_speech(part_of_speech)` and `exclude_part_of_speech(part_of_speech)`
 - Include/exclude relations to be parsed using `include_relation(relation)` and `exclude_relation(relation)`

#### Examples

```python
>>> from wiktionaryparser import WiktionaryParser
>>> parser = WiktionaryParser()
>>> word = parser.fetch('test')
>>> another_word = parser.fetch('test', 'french')
>>> parser.set_default_language('french')
>>> parser.exclude_part_of_speech('noun')
>>> parser.include_relation('alternative forms')
```

#### Requirements

 - requests==2.20.0
 - beautifulsoup4==4.4.0
