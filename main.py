#!/usr/bin/env python
#coding:utf-8

import const
import requests
from bs4 import BeautifulSoup as BeautifulSoup
from bs4 import NavigableString, Tag

if __name__ == '__main__':
    
    response = requests.get(const.URL)

    if response.status_code != 200:
        print('Error: {}'.format(response.status_code))
        exit()

    page = BeautifulSoup(response.text, 'html.parser')
    games_list_div = page.find(id="game-lists")
    
    currentlyPlaying = []
    for game in games_list_div:
        if isinstance(game, NavigableString):
            continue
        if isinstance(game, Tag):
            # game name
            game_name = game.find("div", {"class": "game-text-centered"})
            currentlyPlaying.append(game_name.text)

            # game cover
            # game_cover = game.find("div", {"class": "game-cover"})
            # game_cover_link = game_cover.find("a")
            # print(game_cover_link.get("href"))

            # image tag
            # img_tag = game.find("img")
            # print(img_tag)
            
    print(currentlyPlaying)