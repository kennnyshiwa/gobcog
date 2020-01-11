import json

from pprint import pprint
from sys import argv

BLANK_STATS = {
        "att": 0,
        "cha": 0,
        "int": 0,
        "dex": 0,
        "luck": 0,
        }

def convert_list_to_json(file_name, default_value):
    word_input = open(file_name, "r")
    word_stats = {}
    for word in word_input:
        word_stats[word.strip()] = default_value

    with open('blank.json', 'w') as output:
        json.dump(word_stats, output, indent=2)

def convert_md_to_json(file_name):
    md_input = open(file_name, "r")
    prefix_stats = {}
    for prefix in prefix_input:
        prefix_stats[prefix.strip()] = {
                "att": 0,
                "cha": 0,
                "int": 0,
                "dex": 0,
                "luck": 0,
                }

    with open('prefixes-blank.json', 'w') as prefix_output:
        json.dump(prefix_stats, prefix_output, indent=2)

if __name__ == "__main__":
    pprint(json.load(open(argv[1], 'r')))
    #  blank_stats_cp = BLANK_STATS.copy()
    #  blank_stats_cp['the'] = False
    #  convert_list_to_json(argv[1], blank_stats_cp)
