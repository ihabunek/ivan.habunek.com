#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ivan Habunek'
SITENAME = 'Ivan Habunek'
SITEURL = 'https://ivan.habunek.com'

PATH = 'content'

TIMEZONE = 'Europe/Zagreb'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'

MENUITEMS = (
    ('Home', '/'),
    ('Talks', '/talks/'),
)

DISPLAY_PAGES_ON_MENU = True

# USE_FOLDER_AS_CATEGORY = True

# Clean URLs
ARTICLE_URL = '{category}/{date:%Y-%m-%d}-{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y-%m-%d}-{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

# Copy slides to output, but don't process them
STATIC_PATHS = ['slides']
PAGE_EXCLUDES = ['slides']
ARTICLE_EXCLUDES = ['slides']
