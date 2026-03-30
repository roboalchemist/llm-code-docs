# Source: https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/

Title: django.contrib.postgres | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/

Markdown Content:
django.contrib.postgres | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/#main-content)

[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.

Menu Main navigation
*   [Overview](https://www.djangoproject.com/start/overview/)
*   [Download](https://www.djangoproject.com/download/)
*   [Documentation](https://docs.djangoproject.com/)
*   [News](https://www.djangoproject.com/weblog/)
*   [Code](https://github.com/django/django)
*   [Issues](https://code.djangoproject.com/)
*   [Community](https://www.djangoproject.com/community/)
*   [Foundation](https://www.djangoproject.com/foundation/)
*   [♥ Donate](https://www.djangoproject.com/fundraising/)

Search Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

*   [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

*   Language: **en**
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/contrib/postgres/)
*   [sv](https://docs.djangoproject.com/sv/6.0/ref/contrib/postgres/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/contrib/postgres/)
*   [pl](https://docs.djangoproject.com/pl/6.0/ref/contrib/postgres/)
*   [ko](https://docs.djangoproject.com/ko/6.0/ref/contrib/postgres/)
*   [ja](https://docs.djangoproject.com/ja/6.0/ref/contrib/postgres/)
*   [it](https://docs.djangoproject.com/it/6.0/ref/contrib/postgres/)
*   [id](https://docs.djangoproject.com/id/6.0/ref/contrib/postgres/)
*   [fr](https://docs.djangoproject.com/fr/6.0/ref/contrib/postgres/)
*   [es](https://docs.djangoproject.com/es/6.0/ref/contrib/postgres/)
*   [el](https://docs.djangoproject.com/el/6.0/ref/contrib/postgres/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/ref/contrib/postgres/)
*   [5.2](https://docs.djangoproject.com/en/5.2/ref/contrib/postgres/)
*   [5.1](https://docs.djangoproject.com/en/5.1/ref/contrib/postgres/)
*   [5.0](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/)
*   [4.2](https://docs.djangoproject.com/en/4.2/ref/contrib/postgres/)
*   [4.1](https://docs.djangoproject.com/en/4.1/ref/contrib/postgres/)
*   [4.0](https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/)
*   [3.2](https://docs.djangoproject.com/en/3.2/ref/contrib/postgres/)
*   [3.1](https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/)
*   [3.0](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/)
*   [2.2](https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/)
*   [2.1](https://docs.djangoproject.com/en/2.1/ref/contrib/postgres/)
*   [2.0](https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/)
*   [1.11](https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/)
*   [1.10](https://docs.djangoproject.com/en/1.10/ref/contrib/postgres/)
*   [1.8](https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/)

*   [](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/#top)

`django.contrib.postgres`[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/#module-django.contrib.postgres "Link to this heading")
===============================================================================================================================================

PostgreSQL has a number of features which are not shared by the other databases Django supports. This optional module contains model fields and form fields for a number of PostgreSQL specific data types.

Note

Django is, and will continue to be, a database-agnostic web framework. We would encourage those writing reusable applications for the Django community to write database-agnostic code where practical. However, we recognize that real world projects written using Django need not be database-agnostic. In fact, once a project reaches a given size changing the underlying data store is already a significant challenge and is likely to require changing the code base in some ways to handle differences between the data stores.

Django provides support for a number of data types which will only work with PostgreSQL. There is no fundamental reason why (for example) a `contrib.mysql` module does not exist, except that PostgreSQL has the richest feature set of the supported databases so its users have the most to gain.

*   [PostgreSQL specific aggregation functions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/aggregates/)
    *   [General-purpose aggregation functions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/aggregates/#general-purpose-aggregation-functions)
    *   [Aggregate functions for statistics](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/aggregates/#aggregate-functions-for-statistics)
    *   [Usage examples](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/aggregates/#usage-examples)

*   [PostgreSQL specific database constraints](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/constraints/)
    *   [`ExclusionConstraint`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/constraints/#exclusionconstraint)

*   [PostgreSQL specific query expressions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/expressions/)
    *   [`ArraySubquery()` expressions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/expressions/#arraysubquery-expressions)

*   [PostgreSQL specific model fields](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/fields/)
    *   [Indexing these fields](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/fields/#indexing-these-fields)
    *   [`ArrayField`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/fields/#arrayfield)
    *   [`HStoreField`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/fields/#hstorefield)
    *   [Range Fields](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/fields/#range-fields)

*   [PostgreSQL specific form fields and widgets](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/forms/)
    *   [Fields](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/forms/#fields)
    *   [Widgets](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/forms/#widgets)

*   [PostgreSQL specific database functions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/functions/)
    *   [`RandomUUID`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/functions/#randomuuid)
    *   [`TransactionNow`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/functions/#transactionnow)

*   [PostgreSQL specific model indexes](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/)
    *   [`BloomIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#bloomindex)
    *   [`BrinIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#brinindex)
    *   [`BTreeIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#btreeindex)
    *   [`GinIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#ginindex)
    *   [`GistIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#gistindex)
    *   [`HashIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#hashindex)
    *   [`SpGistIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#spgistindex)
    *   [`OpClass()` expressions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#opclass-expressions)

*   [PostgreSQL specific lookups](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/lookups/)
    *   [Trigram similarity](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/lookups/#trigram-similarity)
    *   [`Unaccent`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/lookups/#unaccent)

*   [Database migration operations](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/)
    *   [Creating extension using migrations](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#creating-extension-using-migrations)
    *   [`CreateExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#createextension)
    *   [`BloomExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#bloomextension)
    *   [`BtreeGinExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#btreeginextension)
    *   [`BtreeGistExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#btreegistextension)
    *   [`CITextExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#citextextension)
    *   [`CryptoExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#cryptoextension)
    *   [`HStoreExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#hstoreextension)
    *   [`TrigramExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#trigramextension)
    *   [`UnaccentExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#unaccentextension)
    *   [Managing collations using migrations](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#managing-collations-using-migrations)
    *   [Concurrent index operations](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#concurrent-index-operations)
    *   [Adding constraints without enforcing validation](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#adding-constraints-without-enforcing-validation)

*   [Full text search](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/)
    *   [The `search` lookup](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#the-search-lookup)
    *   [`SearchVector`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#searchvector)
    *   [`SearchQuery`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#searchquery)
    *   [`SearchRank`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#searchrank)
    *   [`SearchHeadline`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#searchheadline)
    *   [Changing the search configuration](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#changing-the-search-configuration)
    *   [Weighting queries](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#weighting-queries)
    *   [`Lexeme`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#lexeme)
    *   [Performance](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#performance)
    *   [Trigram similarity](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/search/#trigram-similarity)

*   [Validators](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/validators/)
    *   [`KeysValidator`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/validators/#keysvalidator)
    *   [Range validators](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/validators/#range-validators)

Previous page and next page

[The messages framework](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/)

[PostgreSQL specific aggregation functions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/aggregates/)

[Back to Top](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [gitaarik donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [`django.contrib.postgres`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/#)

### Browse

*   Prev: [The messages framework](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/)
*   Next: [PostgreSQL specific aggregation functions](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/aggregates/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
        *   [`contrib` packages](https://docs.djangoproject.com/en/6.0/ref/contrib/)
            *   `django.contrib.postgres`

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)Try the FAQ — it's got answers to many common questions.[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)Handy when looking for specific information.[Django Discord Server](https://chat.djangoproject.com/)Join the Django Discord Community.[Official Django Forum](https://forum.djangoproject.com/)Join the community on the Django Forum.[Ticket tracker](https://code.djangoproject.com/)Report bugs with Django or Django documentation in our ticket tracker.
### Download:

Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) | [PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) | [ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)

 Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Image 2: JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

*   **JetBrains**
*   [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")

[![Image 3: Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

*   **Sentry**
*   [Monitor your Django Code Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![Image 4: Kraken Tech](https://media.djangoproject.com/cache/71/4b/714b3473ed0cf3665f6b894d3be9491e.png)](https://kraken.tech/ "Kraken Tech")

*   **Kraken Tech**
*   [Kraken is the most-loved operating system for energy. Powered by our Utility-Grade AI™ and deep industry know-how, we help utilities transform their technology and operations so they can lead the energy transition. Delivering better outcomes from generation through distribution to supply, Kraken powers 70+ million accounts worldwide, and is on a mission to make a big, green dent in the universe.](https://kraken.tech/ "Kraken Tech")

Django Links
------------

### Learn More

*   [About Django](https://www.djangoproject.com/start/overview/)
*   [Getting Started with Django](https://www.djangoproject.com/start/)
*   [Team Organization](https://www.djangoproject.com/foundation/teams/)
*   [Django Software Foundation](https://www.djangoproject.com/foundation/)
*   [Code of Conduct](https://www.djangoproject.com/conduct/)
*   [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

*   [Join a Group](https://www.djangoproject.com/community/)
*   [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
*   [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
*   [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
*   [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

*   [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
*   [Django Discord](https://chat.djangoproject.com/)
*   [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

*   [GitHub](https://github.com/django)
*   [X](https://x.com/djangoproject)
*   [Fediverse (Mastodon)](https://fosstodon.org/@django)
*   [Bluesky](https://bsky.app/profile/djangoproject.com)
*   [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
*   [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

*   [Sponsor Django](https://www.djangoproject.com/fundraising/)
*   [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
*   [Official merchandise store](https://django.threadless.com/)
*   [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

*   Hosting by[In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
*   Design by[Threespot](https://www.threespot.com/)&[andrevv](http://andrevv.com/)

© 2005-2026 [Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
