# Source: https://docs.djangoproject.com/en/6.0/intro/install/

Title: Quick install guide | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/intro/install/

Markdown Content:
Quick install guide | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/6.0/intro/install/#main-content)

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
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/intro/install/)
*   [sv](https://docs.djangoproject.com/sv/6.0/intro/install/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/intro/install/)
*   [pl](https://docs.djangoproject.com/pl/6.0/intro/install/)
*   [ko](https://docs.djangoproject.com/ko/6.0/intro/install/)
*   [ja](https://docs.djangoproject.com/ja/6.0/intro/install/)
*   [it](https://docs.djangoproject.com/it/6.0/intro/install/)
*   [id](https://docs.djangoproject.com/id/6.0/intro/install/)
*   [fr](https://docs.djangoproject.com/fr/6.0/intro/install/)
*   [es](https://docs.djangoproject.com/es/6.0/intro/install/)
*   [el](https://docs.djangoproject.com/el/6.0/intro/install/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/intro/install/)
*   [5.2](https://docs.djangoproject.com/en/5.2/intro/install/)
*   [5.1](https://docs.djangoproject.com/en/5.1/intro/install/)
*   [5.0](https://docs.djangoproject.com/en/5.0/intro/install/)
*   [4.2](https://docs.djangoproject.com/en/4.2/intro/install/)
*   [4.1](https://docs.djangoproject.com/en/4.1/intro/install/)
*   [4.0](https://docs.djangoproject.com/en/4.0/intro/install/)
*   [3.2](https://docs.djangoproject.com/en/3.2/intro/install/)
*   [3.1](https://docs.djangoproject.com/en/3.1/intro/install/)
*   [3.0](https://docs.djangoproject.com/en/3.0/intro/install/)
*   [2.2](https://docs.djangoproject.com/en/2.2/intro/install/)
*   [2.1](https://docs.djangoproject.com/en/2.1/intro/install/)
*   [2.0](https://docs.djangoproject.com/en/2.0/intro/install/)
*   [1.11](https://docs.djangoproject.com/en/1.11/intro/install/)
*   [1.10](https://docs.djangoproject.com/en/1.10/intro/install/)
*   [1.8](https://docs.djangoproject.com/en/1.8/intro/install/)

*   [](https://docs.djangoproject.com/en/6.0/intro/install/#top)

Quick install guide[¶](https://docs.djangoproject.com/en/6.0/intro/install/#quick-install-guide "Link to this heading")
=======================================================================================================================

Before you can use Django, you’ll need to get it installed. We have a [complete installation guide](https://docs.djangoproject.com/en/6.0/topics/install/) that covers all the possibilities; this guide will guide you to a minimal installation that’ll work while you walk through the introduction.

Install Python[¶](https://docs.djangoproject.com/en/6.0/intro/install/#install-python "Link to this heading")
-------------------------------------------------------------------------------------------------------------

Being a Python web framework, Django requires Python. See [What Python version can I use with Django?](https://docs.djangoproject.com/en/6.0/faq/install/#faq-python-version-support) for details. Python includes a lightweight database called [SQLite](https://www.sqlite.org/) so you won’t need to set up a database just yet.

Get the latest version of Python at [https://www.python.org/downloads/](https://www.python.org/downloads/) or with your operating system’s package manager.

You can verify that Python is installed by typing `python` from your shell; you should see something like:

Python 3.x.y
[GCC 4.x] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

Set up a database[¶](https://docs.djangoproject.com/en/6.0/intro/install/#set-up-a-database "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

This step is only necessary if you’d like to work with a “large” database engine like PostgreSQL, MariaDB, MySQL, or Oracle. To install such a database, consult the [database installation information](https://docs.djangoproject.com/en/6.0/topics/install/#database-installation).

Install Django[¶](https://docs.djangoproject.com/en/6.0/intro/install/#install-django "Link to this heading")
-------------------------------------------------------------------------------------------------------------

You’ve got three options to install Django:

*   [Install an official release](https://docs.djangoproject.com/en/6.0/topics/install/#installing-official-release). This is the best approach for most users.

*   Install a version of Django [provided by your operating system distribution](https://docs.djangoproject.com/en/6.0/topics/install/#installing-distribution-package).

*   [Install the latest development version](https://docs.djangoproject.com/en/6.0/topics/install/#installing-development-version). This option is for enthusiasts who want the latest-and-greatest features and aren’t afraid of running brand new code. You might encounter new bugs in the development version, but reporting them helps the development of Django. Also, releases of third-party packages are less likely to be compatible with the development version than with the latest stable release.

Always refer to the documentation that corresponds to the version of Django you’re using!

If you do either of the first two steps, keep an eye out for parts of the documentation marked **new in development version**. That phrase flags features that are only available in development versions of Django, and they likely won’t work with an official release.

Verifying[¶](https://docs.djangoproject.com/en/6.0/intro/install/#verifying "Link to this heading")
---------------------------------------------------------------------------------------------------

To verify that Django can be seen by Python, type `python` from your shell. Then at the Python prompt, try to import Django:

>>> import django
>>> print(django.get_version())
6.0
You may have another version of Django installed.

That’s it![¶](https://docs.djangoproject.com/en/6.0/intro/install/#that-s-it "Link to this heading")
----------------------------------------------------------------------------------------------------

That’s it – you can now [move onto the tutorial](https://docs.djangoproject.com/en/6.0/intro/tutorial01/).

Previous page and next page

[Django at a glance](https://docs.djangoproject.com/en/6.0/intro/overview/)

[Writing your first Django app, part 1](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)

[Back to Top](https://docs.djangoproject.com/en/6.0/intro/install/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [Williams Mendez donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [Quick install guide](https://docs.djangoproject.com/en/6.0/intro/install/#)
    *   [Install Python](https://docs.djangoproject.com/en/6.0/intro/install/#install-python)
    *   [Set up a database](https://docs.djangoproject.com/en/6.0/intro/install/#set-up-a-database)
    *   [Install Django](https://docs.djangoproject.com/en/6.0/intro/install/#install-django)
    *   [Verifying](https://docs.djangoproject.com/en/6.0/intro/install/#verifying)
    *   [That’s it!](https://docs.djangoproject.com/en/6.0/intro/install/#that-s-it)

### Browse

*   Prev: [Django at a glance](https://docs.djangoproject.com/en/6.0/intro/overview/)
*   Next: [Writing your first Django app, part 1](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [Getting started](https://docs.djangoproject.com/en/6.0/intro/)
        *   Quick install guide

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
