# Source: https://docs.djangoproject.com/en/6.0/ref/models/indexes/

Title: Model index reference | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/models/indexes/

Markdown Content:
Model index reference | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#main-content)

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
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/models/indexes/)
*   [sv](https://docs.djangoproject.com/sv/6.0/ref/models/indexes/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/models/indexes/)
*   [pl](https://docs.djangoproject.com/pl/6.0/ref/models/indexes/)
*   [ko](https://docs.djangoproject.com/ko/6.0/ref/models/indexes/)
*   [ja](https://docs.djangoproject.com/ja/6.0/ref/models/indexes/)
*   [it](https://docs.djangoproject.com/it/6.0/ref/models/indexes/)
*   [id](https://docs.djangoproject.com/id/6.0/ref/models/indexes/)
*   [fr](https://docs.djangoproject.com/fr/6.0/ref/models/indexes/)
*   [es](https://docs.djangoproject.com/es/6.0/ref/models/indexes/)
*   [el](https://docs.djangoproject.com/el/6.0/ref/models/indexes/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/ref/models/indexes/)
*   [5.2](https://docs.djangoproject.com/en/5.2/ref/models/indexes/)
*   [5.1](https://docs.djangoproject.com/en/5.1/ref/models/indexes/)
*   [5.0](https://docs.djangoproject.com/en/5.0/ref/models/indexes/)
*   [4.2](https://docs.djangoproject.com/en/4.2/ref/models/indexes/)
*   [4.1](https://docs.djangoproject.com/en/4.1/ref/models/indexes/)
*   [4.0](https://docs.djangoproject.com/en/4.0/ref/models/indexes/)
*   [3.2](https://docs.djangoproject.com/en/3.2/ref/models/indexes/)
*   [3.1](https://docs.djangoproject.com/en/3.1/ref/models/indexes/)
*   [3.0](https://docs.djangoproject.com/en/3.0/ref/models/indexes/)
*   [2.2](https://docs.djangoproject.com/en/2.2/ref/models/indexes/)
*   [2.1](https://docs.djangoproject.com/en/2.1/ref/models/indexes/)
*   [2.0](https://docs.djangoproject.com/en/2.0/ref/models/indexes/)
*   [1.11](https://docs.djangoproject.com/en/1.11/ref/models/indexes/)

*   [](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#top)

Model index reference[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#module-django.db.models.indexes "Link to this heading")
==========================================================================================================================================

Index classes ease creating database indexes. They can be added using the [`Meta.indexes`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.indexes "django.db.models.Options.indexes") option. This document explains the API references of [`Index`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index "django.db.models.Index") which includes the [index options](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#index-options).

Referencing built-in indexes

Indexes are defined in `django.db.models.indexes`, but for convenience they’re imported into [`django.db.models`](https://docs.djangoproject.com/en/6.0/topics/db/models/#module-django.db.models "django.db.models"). The standard convention is to use `from django.db import models` and refer to the indexes as `models.<IndexClass>`.

`Index` options[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#index-options "Link to this heading")
------------------------------------------------------------------------------------------------------------------

_class_ Index(_*expressions_, _fields=()_, _name=None_, _db\_tablespace=None_, _opclasses=()_, _condition=None_, _include=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/indexes.py#L14)[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index "Link to this definition")
Creates an index (B-Tree) in the database.

### `expressions`[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#expressions "Link to this heading")

Index.expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.expressions "Link to this definition")
Positional argument `*expressions` allows creating functional indexes on expressions and database functions.

For example:

Index(Lower("title").desc(), "pub_date", name="lower_title_date_idx")

creates an index on the lowercased value of the `title` field in descending order and the `pub_date` field in the default ascending order.

Another example:

Index(F("height") * F("weight"), Round("weight"), name="calc_idx")

creates an index on the result of multiplying fields `height` and `weight` and the `weight` rounded to the nearest integer.

[`Index.name`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.name "django.db.models.Index.name") is required when using `*expressions`.

Restrictions on Oracle

Oracle requires functions referenced in an index to be marked as `DETERMINISTIC`. Django doesn’t validate this but Oracle will error. This means that functions such as [`Random()`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Random "django.db.models.functions.Random") aren’t accepted.

Restrictions on PostgreSQL

PostgreSQL requires functions and operators referenced in an index to be marked as `IMMUTABLE`. Django doesn’t validate this but PostgreSQL will error. This means that functions such as [`Concat()`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Concat "django.db.models.functions.Concat") aren’t accepted.

MySQL and MariaDB

Functional indexes are ignored with MySQL < 8.0.13 and MariaDB as neither supports them.

### `fields`[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#fields "Link to this heading")

Index.fields[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.fields "Link to this definition")
A list or tuple of the name of the fields on which the index is desired.

By default, indexes are created with an ascending order for each column. To define an index with a descending order for a column, add a hyphen before the field’s name.

For example `Index(fields=['headline', '-pub_date'])` would create SQL with `(headline, pub_date DESC)`.

MariaDB

Index ordering isn’t supported on MariaDB < 10.8. In that case, a descending index is created as a normal index.

### `name`[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#name "Link to this heading")

Index.name[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.name "Link to this definition")
The name of the index. If `name` isn’t provided Django will auto-generate a name. For compatibility with different databases, index names cannot be longer than 30 characters and shouldn’t start with a number (0-9) or underscore (_).

Partial indexes in abstract base classes

You must always specify a unique name for an index. As such, you cannot normally specify a partial index on an abstract base class, since the [`Meta.indexes`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.indexes "django.db.models.Options.indexes") option is inherited by subclasses, with exactly the same values for the attributes (including `name`) each time. To work around name collisions, part of the name may contain `'%(app_label)s'` and `'%(class)s'`, which are replaced, respectively, by the lowercased app label and class name of the concrete model. For example 
```
Index(fields=['title'],
name='%(app_label)s_%(class)s_title_index')
```
.

### `db_tablespace`[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#db-tablespace "Link to this heading")

Index.db_tablespace[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.db_tablespace "Link to this definition")
The name of the [database tablespace](https://docs.djangoproject.com/en/6.0/topics/db/tablespaces/) to use for this index. For single field indexes, if `db_tablespace` isn’t provided, the index is created in the `db_tablespace` of the field.

If [`Field.db_tablespace`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_tablespace "django.db.models.Field.db_tablespace") isn’t specified (or if the index uses multiple fields), the index is created in tablespace specified in the [`db_tablespace`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.db_tablespace "django.db.models.Options.db_tablespace") option inside the model’s `class Meta`. If neither of those tablespaces are set, the index is created in the same tablespace as the table.

See also

For a list of PostgreSQL-specific indexes, see [`django.contrib.postgres.indexes`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#module-django.contrib.postgres.indexes "django.contrib.postgres.indexes").

### `opclasses`[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#opclasses "Link to this heading")

Index.opclasses[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.opclasses "Link to this definition")
The names of the [PostgreSQL operator classes](https://www.postgresql.org/docs/current/indexes-opclass.html) to use for this index. If you require a custom operator class, you must provide one for each field in the index.

For example, 
```
GinIndex(name='json_index', fields=['jsonfield'],
opclasses=['jsonb_path_ops'])
```
 creates a gin index on `jsonfield` using `jsonb_path_ops`.

`opclasses` are ignored for databases besides PostgreSQL.

[`Index.name`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.name "django.db.models.Index.name") is required when using `opclasses`.

### `condition`[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#condition "Link to this heading")

Index.condition[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.condition "Link to this definition")
If the table is very large and your queries mostly target a subset of rows, it may be useful to restrict an index to that subset. Specify a condition as a [`Q`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q"). For example, `condition=Q(pages__gt=400)` indexes records with more than 400 pages.

[`Index.name`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.name "django.db.models.Index.name") is required when using `condition`.

Restrictions on PostgreSQL

PostgreSQL requires functions referenced in the condition to be marked as IMMUTABLE. Django doesn’t validate this but PostgreSQL will error. This means that functions such as [Date functions](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#date-functions) and [`Concat`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Concat "django.db.models.functions.Concat") aren’t accepted. If you store dates in [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField"), comparison to [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") objects may require the `tzinfo` argument to be provided because otherwise the comparison could result in a mutable function due to the casting Django does for [lookups](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#field-lookups).

Restrictions on SQLite

SQLite [imposes restrictions](https://www.sqlite.org/partialindex.html) on how a partial index can be constructed.

Oracle

Oracle does not support partial indexes. Instead, partial indexes can be emulated by using functional indexes together with [`Case`](https://docs.djangoproject.com/en/6.0/ref/models/conditional-expressions/#django.db.models.expressions.Case "django.db.models.expressions.Case") expressions.

MySQL and MariaDB

The `condition` argument is ignored with MySQL and MariaDB as neither supports conditional indexes.

### `include`[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#include "Link to this heading")

Index.include[¶](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.include "Link to this definition")
A list or tuple of the names of the fields to be included in the covering index as non-key columns. This allows index-only scans to be used for queries that select only included fields ([`include`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.include "django.db.models.Index.include")) and filter only by indexed fields ([`fields`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.fields "django.db.models.Index.fields")).

For example:

Index(name="covering_index", fields=["headline"], include=["pub_date"])

will allow filtering on `headline`, also selecting `pub_date`, while fetching data only from the index.

Using `include` will produce a smaller index than using a multiple column index but with the drawback that non-key columns can not be used for sorting or filtering.

`include` is ignored for databases besides PostgreSQL.

[`Index.name`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index.name "django.db.models.Index.name") is required when using `include`.

See the PostgreSQL documentation for more details about [covering indexes](https://www.postgresql.org/docs/current/indexes-index-only-scans.html).

Restrictions on PostgreSQL

PostgreSQL supports covering B-Tree and [`GiST indexes`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#django.contrib.postgres.indexes.GistIndex "django.contrib.postgres.indexes.GistIndex"). PostgreSQL 14+ also supports covering [`SP-GiST indexes`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#django.contrib.postgres.indexes.SpGistIndex "django.contrib.postgres.indexes.SpGistIndex").

Previous page and next page

[Model field reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/)

[Constraints reference](https://docs.djangoproject.com/en/6.0/ref/models/constraints/)

[Back to Top](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [DjangoTricks - Aidas Bendoraitis donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [Model index reference](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#)
    *   [`Index` options](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#index-options)
        *   [`expressions`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#expressions)
        *   [`fields`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#fields)
        *   [`name`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#name)
        *   [`db_tablespace`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#db-tablespace)
        *   [`opclasses`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#opclasses)
        *   [`condition`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#condition)
        *   [`include`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#include)

### Browse

*   Prev: [Model field reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/)
*   Next: [Constraints reference](https://docs.djangoproject.com/en/6.0/ref/models/constraints/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
        *   [Models](https://docs.djangoproject.com/en/6.0/ref/models/)
            *   Model index reference

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
