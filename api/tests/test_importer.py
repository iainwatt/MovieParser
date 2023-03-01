import pytest
from importer import WikiImporter
import os
from config import env_config
import json

SCRIPT_DIR = os.path.dirname(__file__)

def test_mapping_function():
    "Verify the output of `calc_addition` function"
    example = json.loads(open(os.path.join(SCRIPT_DIR, 'examples/гулять.json')).read())

    # can we get the envars correctly some other way
    env = os.getenv("FLASK_ENV", 'testing')
    config = {
        'username': 'root',
        'password': 'root0000',
        'host': '127.0.0.1',
        'database': 'lingswap_test'
    }

    output = WikiImporter(language='russian', en_vars=config).map_word_entry(word_entry=example)
    assert list(output) == ['word_type', 'definition', 'etymology', 'related_words', 'verb_conjugation', 'pronunciations']
    assert isinstance(output['definition'], str)
    assert isinstance(output['etymology'], str)
    assert isinstance(output['related_words'], str)
    assert isinstance(output['verb_conjugation'], dict)
    assert isinstance(output['pronunciations'], dict)


def test_word_table_schema():

    # write to this file each time the program runs to update the db schema
    # word_table_schema = json.loads(open(os.path.join(SCRIPT_DIR, 'examples/word_table.json')).read())
    word_table_schema = {}
    word_table_cols = ['word_type', 'definition', 'etymology', 'related_words', 'verb_conjugation', 'pronunciations']

    assert isinstance(word_table_schema, dict)
