#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script used to convert raw word lists to JSON for random item generation.

import json

from pprint import pprint
from sys import argv

BLANK_STATS = { "att": 0, "cha": 0, "int": 0, "dex": 0, "luck": 0 }

def convert_list_to_json(file_name, default_value):
    """Convert list of words to JSON and write to blank.json.

    :default_value: Default value in the JSON for each word in the
        list.
    """
    word_input = open(file_name, "r")
    word_stats = {}
    for word in word_input:
        word_stats[word.strip()] = default_value

    with open('blank.json', 'w') as output:
        json.dump(word_stats, output, indent=2, sort_keys=True)

def convert_md_to_json(file_name, default_value):
    """Convert Markdown to JSON and write to blank.json. Each header
    will be used a top-level key, and each word below the header will
    be added to a dict nested within the top-level key.

    :default_value: Default value in the JSON for each word in the
        list.
    """
    md_input = open(file_name, "r")
    categories = {}

    category_name = ""
    category_stats = {}
    for line in md_input:
        stripped_line = line.strip()
        if stripped_line.startswith("#"):
            category_name = stripped_line.replace("# ", "")
        elif stripped_line == "":
            categories[category_name] = category_stats
            category_stats = {}
        else:
            category_stats[stripped_line] = default_value

    with open('blank.json', 'w') as output:
        json.dump(categories, output, indent=2, sort_keys=True)

def sort_json(file_name):
    """Sort the keys of the JSON passed in and write to sorted.json."""
    with open('sorted.json', 'w') as output:
        json.dump(json.load(open(argv[2], 'r')), output, indent=2, sort_keys=True)

if __name__ == "__main__":
    if argv[1] == 'list':
        convert_list_to_json(argv[2], BLANK_STATS)
    elif argv[1] == 'md':
        convert_md_to_json(argv[2], BLANK_STATS)
    elif argv[1] == 'sort':
        sort_json(argv[2])
