#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Calculate the total possible combinations of items based on the
# number of current words.

import json

from pprint import pprint
from prettytable import PrettyTable
from sys import argv
from tabulate import tabulate

PREFIXES_FILE = "prefixes.json"
MATERIALS_FILE = "materials.json"
EQUIPMENT_FILE = "equipment.json"
SUFFIXES_FILE = "suffixes.json"

def num_keys(file_name):
    """Get the number of top-level keys from the JSON at file_name."""
    return len(json.load(open(file_name, 'r')).keys())

def get_nested_num(file_name):
    """Get the total number of nested keys from the JSON at file_name."""
    num = 0
    top_level_dict = json.load(open(file_name, 'r'))
    for nested_dict in list(top_level_dict.values()):
        num += len(nested_dict.keys())
    return num

def add_1_word(cur_num_items, cur_num_words):
    """Calculate the new number of items if you add 1 word to the list
    with cur_num_words."""
    return round(cur_num_items / cur_num_words * (cur_num_words + 1))

def add_1_word_row(info_table, word_name, cur_num_items, cur_num_words):
    """Create row for table for word detailing new number of items and
    the difference."""
    new_items = add_1_word(cur_num_items, cur_num_words)
    info_table.add_row([f"Add 1 {word_name}", f"{new_items:,}",
        f"+{new_items - cur_num_items:,}"])

if __name__ == "__main__":
    num_prefixes = num_keys(PREFIXES_FILE)
    num_materials = get_nested_num(MATERIALS_FILE)
    num_equipment = get_nested_num(EQUIPMENT_FILE)
    num_suffixes = num_keys(SUFFIXES_FILE)
    cur_num_items = num_prefixes * num_materials * num_equipment * num_suffixes

    info_table = PrettyTable()
    info_table.field_names = ["Description", "# Items", "Difference"]
    info_table.align["Description"] = "l"
    info_table.align["Difference"] = "l"

    info_table.add_row(["Cur. # of Items", f"{cur_num_items:,}", ""])
    add_1_word_row(info_table, "Prefix", cur_num_items, num_prefixes)
    add_1_word_row(info_table, "Material", cur_num_items, num_materials)
    add_1_word_row(info_table, "Equipment", cur_num_items, num_equipment)
    add_1_word_row(info_table, "Suffix", cur_num_items, num_suffixes)

    print(info_table)
