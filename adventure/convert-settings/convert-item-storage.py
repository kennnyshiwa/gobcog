#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from pprint import pprint
from sys import argv

def convert_item(item_name, item_dict):
    new_name = item_name
    del item_dict['name']
    if item_dict["rarity"] == "legendary":
        new_name = item_name.replace("{Legendary:'", "").replace("'}", "")
    if item_dict["rarity"] == "epic":
        new_name = item_name.replace( "[", "").replace("]", "")
    if item_dict["rarity"] == "rare":
        new_name = item_name.replace( "_", " ").replace(".", "")
    return new_name, item_dict

def convert_settings(settings_file):
    settings = json.load(open(settings_file, 'r'))
    for server in list(settings.keys()):
        server_user_settings = settings[server]["USER"]
        for user in list(server_user_settings.keys()):
            new_backpack = {}
            user_equipped_items = server_user_settings[user]["items"]
            for slot in list(user_equipped_items.keys()):
                if user_equipped_items[slot]:
                    for slot_item_name, slot_item in list(
                            user_equipped_items[slot].items())[:1]:
                        # update slot item if item equipped
                        new_name, slot_item = convert_item(slot_item_name, slot_item)
                        server_user_settings[user]["items"][slot] = { new_name: slot_item}

            # update backpack items
            for backpack_item_name, backpack_item in list(server_user_settings[user]["backpack"].items()):
                new_name, backpack_item = convert_item(backpack_item_name, backpack_item)
                new_backpack[new_name] = backpack_item
            server_user_settings[user]["backpack"] = new_backpack

    with open('settings-new.json', 'w') as new_settings:
        json.dump(settings, new_settings, indent=2)

if __name__ == "__main__":
    convert_settings(argv[1])
