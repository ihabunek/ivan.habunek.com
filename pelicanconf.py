AUTHOR = 'Ivan Habunek'
SITENAME = 'Ivan Habunek'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Zagreb'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'

MENUITEMS = (
    ('About', '/'),
    ('Talks', '/talks/'),
    ('Projects', '/projects/'),
)

DISPLAY_PAGES_ON_MENU = True

# Clean URLs
ARTICLE_URL = '{category}/{date:%Y-%m-%d}-{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y-%m-%d}-{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

# Copy slides to output, but don't process them
STATIC_PATHS = ['images', 'slides', 'keybase.txt']
PAGE_EXCLUDES = ['slides']
ARTICLE_EXCLUDES = ['slides']
