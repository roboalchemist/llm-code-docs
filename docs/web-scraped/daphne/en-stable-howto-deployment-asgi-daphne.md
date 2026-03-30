# Source: https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/

Title: How to use Django with Daphne | Django documentation

URL Source: https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/

Markdown Content:
How to use Django with Daphne | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#main-content)

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
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/howto/deployment/asgi/daphne/)
*   [sv](https://docs.djangoproject.com/sv/6.0/howto/deployment/asgi/daphne/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/howto/deployment/asgi/daphne/)
*   [pl](https://docs.djangoproject.com/pl/6.0/howto/deployment/asgi/daphne/)
*   [ko](https://docs.djangoproject.com/ko/6.0/howto/deployment/asgi/daphne/)
*   [ja](https://docs.djangoproject.com/ja/6.0/howto/deployment/asgi/daphne/)
*   [it](https://docs.djangoproject.com/it/6.0/howto/deployment/asgi/daphne/)
*   [id](https://docs.djangoproject.com/id/6.0/howto/deployment/asgi/daphne/)
*   [fr](https://docs.djangoproject.com/fr/6.0/howto/deployment/asgi/daphne/)
*   [es](https://docs.djangoproject.com/es/6.0/howto/deployment/asgi/daphne/)
*   [el](https://docs.djangoproject.com/el/6.0/howto/deployment/asgi/daphne/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/howto/deployment/asgi/daphne/)
*   [5.2](https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/daphne/)
*   [5.1](https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/daphne/)
*   [5.0](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/daphne/)
*   [4.2](https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/daphne/)
*   [4.1](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/daphne/)
*   [4.0](https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/daphne/)
*   [3.2](https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/daphne/)
*   [3.1](https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/daphne/)
*   [3.0](https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/daphne/)

*   [](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#top)

How to use Django with Daphne[¶](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#how-to-use-django-with-daphne "Link to this heading")
=============================================================================================================================================================

[Daphne](https://pypi.org/project/daphne/) is a pure-Python ASGI server for UNIX, maintained by members of the Django project. It acts as the reference server for ASGI.

Installing Daphne[¶](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#installing-daphne "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

You can install Daphne with `pip`:

python -m pip install daphne

Running Django in Daphne[¶](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#running-django-in-daphne "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

When Daphne is installed, a `daphne` command is available which starts the Daphne server process. At its simplest, Daphne needs to be called with the location of a module containing an ASGI application object, followed by what the application is called (separated by a colon).

For a typical Django project, invoking Daphne would look like:

daphne myproject.asgi:application

This will start one process listening on `127.0.0.1:8000`. It requires that your project be on the Python path; to ensure that run this command from the same directory as your `manage.py` file.

Integration with `runserver`[¶](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#integration-with-runserver "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Daphne provides a [`runserver`](https://docs.djangoproject.com/en/stable/ref/django-admin/#django-admin-runserver) command to serve your site under ASGI during development.

This can be enabled by adding `daphne` to the start of your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/stable/ref/settings/#std-setting-INSTALLED_APPS) and adding an `ASGI_APPLICATION` setting pointing to your ASGI application object:

INSTALLED_APPS = [
    "daphne",
    ...,
]

ASGI_APPLICATION = "myproject.asgi.application"

Previous page and next page

[How to deploy with ASGI](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/)

[How to use Django with Hypercorn](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/hypercorn/)

[Back to Top](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [Manu Ganji donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [How to use Django with Daphne](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#)
    *   [Installing Daphne](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#installing-daphne)
    *   [Running Django in Daphne](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#running-django-in-daphne)
    *   [Integration with `runserver`](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/#integration-with-runserver)

### Browse

*   Prev: [How to deploy with ASGI](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/)
*   Next: [How to use Django with Hypercorn](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/hypercorn/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [How-to guides](https://docs.djangoproject.com/en/stable/howto/)
        *   [How to deploy Django](https://docs.djangoproject.com/en/stable/howto/deployment/)
            *   [How to deploy with ASGI](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/)
                *   How to use Django with Daphne

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
