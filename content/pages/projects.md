Title: Projects

In my free time I love to write pet projects, some useful, some less so, which I
publish on Github. Here are some of them.

---

## Toot

A commandline tool for interacting with [Mastodon](https://joinmastodon.org/)
instances, including a curses-based UI.

![Toot Example]({static}/images/toot.png)

<a href="https://github.com/ihabunek/toot"><i class="fa fa-github"></i> github.com/ihabunek/toot</a>

---

## hnbex-cli

A commandline tool which displays exchange rates for Croatian Kuna (HRK).

![hnbex-cli]({static}/images/hnbex.png)

<a href="https://github.com/ihabunek/hnbex-cli"><i class="fa fa-github"></i> github.com/ihabunek/hnbex-cli</a>

---

## PDF417 barcode generator

Generator for PDF417 2D barcodes in Python and PHP.

![Barcode Example]({static}/images/barcode.png)

<a href="https://github.com/ihabunek/pdf417-py"><i class="fa fa-github"></i> github.com/ihabunek/pdf417-py</a><br />
<a href="https://github.com/ihabunek/pdf417-php"><i class="fa fa-github"></i> github.com/ihabunek/pdf417-php</a>

---

## HUB3 Barcode API

An API for generating 2D barcodes according to the HUB-3 standard, as defined by the Croatian National Bank.

![Payment slip]({static}/images/uplatnica.png)

<a href="https://hub3.bigfish.software/"><i class="fa fa-globe"></i> hub3.bigfish.software/</a><br />
<a href="https://github.com/ihabunek/hub3-api"><i class="fa fa-github"></i> github.com/ihabunek/hub3-api</a>

---

## GitHub Vanity

Write to your GitHub activity chart.

![Github Vanity Example]({static}/images/vanity.jpg)

<a href="https://github.com/ihabunek/github-vanity"><i class="fa fa-github"></i> github.com/ihabunek/github-vanity</a><br />

---

## Phormium

 A minimal ORM for PHP, written because none of the popular ones worked well
 with Informix.

```php
<?php
$persons = Person::objects()
    ->filter('salary', '>', 10000)
    ->filter('birthday', 'between', ['2000-01-01', '2001-01-01'])
    ->orderBy('name', 'desc')
    ->limit(100)
    ->fetch();
```

<a href="https://github.com/ihabunek/phormium/"><i class="fa fa-github"></i> github.com/ihabunek/phormium/</a><br />

---

## Radio scraper

A web site for collecting radio playlists and showing some statistics,
implemented in Python/Django.

![Radio scraper screenshot]({static}/images/radioscraper.png)

<a href="https://radio.bezdomni.net/"><i class="fa fa-globe"></i> radio.bezdomni.net</a><br />
<a href="https://github.com/ihabunek/radioscraper"><i class="fa fa-github"></i> github.com/ihabunek/radioscraper</a><br />
