#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:14:26 2017
"""
# Movie class to store title, youtube trailer url and poster image url
class Movies:
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
    