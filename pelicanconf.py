#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matt Cooper'
SITENAME = u'Computer Science + Beer'
SITESUBTITLE = u'Delicious alone, better together'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

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
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#OUTPUT_RETENTION = (".git",)
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

THEME = "/Users/mattc/Projects/blog.vtbassmatt.com/crowsfoot"

# Crowsfoot Theme Settings
EMAIL_ADDRESS = "vtbassmatt@gmail.com"
GITHUB_ADDRESS = "https://github.com/vtbassmatt"
SO_ADDRESS = "http://stackoverflow.com/users/481231/matt-cooper"
TWITTER_ADDRESS = "https://twitter.com/vtbassmatt"
SHOW_ARTICLE_AUTHOR = False
LICENSE_URL = "http://creativecommons.org/licenses/by-sa/4.0/"
LICENSE_NAME = "CC BY-SA 4.0"
#PROFILE_IMAGE_URL = "http://blog.vtbassmatt.com/images/mattandt.jpg"
