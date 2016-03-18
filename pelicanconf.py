#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'destop'
SITENAME = u'The Far Star'
SITEURL = 'albanatita.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

PAGE_PATHS = ['./pages/']
ARTICLE_PATHS = ['./articles/']
STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css']
PLUGIN_PATHS = ["./plugins/"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# RENDERING
TYPOGRIFY = True
THEME = "./theme/pelican-bootstrap3/"
BOOTSTRAP_THEME = 'flatly'
DEFAULT_PAGINATION = 5
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'search', 'archives')

# BANNER
BANNER = 'images/banner.png'
BANNER_SUBTITLE = 'Reach the stars and bring them back on Earth.'
BANNER_ALL_PAGES = False

# ABOUT ME
ABOUT_ME = "Plasma physicist. Munich, Germany."
#AVATAR = 'images/avatar.png'

# PLUGINS
PLUGINS = ["render_math"]

# Do not work = 'liquid_tags.notebook',

# Feed
FEED_ALL_RSS = None
FEED_ALL_ATOM = None

# Social widget
LINKS = None
SOCIAL = (('Twitter', 'https://twitter.com/destop'),
          ('Github', 'https://github.com/albanatita'),)
GOOGLE_ANALYTICS="UA-75277621-1"

# ARTICLE INFO
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED =  True
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
