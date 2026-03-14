# Source: https://docs.djangoproject.com/en/6.0/topics/testing/

Title: Testing in Django | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/topics/testing/

Markdown Content:
Testing in Django | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/6.0/topics/testing/#main-content)

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
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/topics/testing/)
*   [sv](https://docs.djangoproject.com/sv/6.0/topics/testing/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/topics/testing/)
*   [pl](https://docs.djangoproject.com/pl/6.0/topics/testing/)
*   [ko](https://docs.djangoproject.com/ko/6.0/topics/testing/)
*   [ja](https://docs.djangoproject.com/ja/6.0/topics/testing/)
*   [it](https://docs.djangoproject.com/it/6.0/topics/testing/)
*   [id](https://docs.djangoproject.com/id/6.0/topics/testing/)
*   [fr](https://docs.djangoproject.com/fr/6.0/topics/testing/)
*   [es](https://docs.djangoproject.com/es/6.0/topics/testing/)
*   [el](https://docs.djangoproject.com/el/6.0/topics/testing/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/topics/testing/)
*   [5.2](https://docs.djangoproject.com/en/5.2/topics/testing/)
*   [5.1](https://docs.djangoproject.com/en/5.1/topics/testing/)
*   [5.0](https://docs.djangoproject.com/en/5.0/topics/testing/)
*   [4.2](https://docs.djangoproject.com/en/4.2/topics/testing/)
*   [4.1](https://docs.djangoproject.com/en/4.1/topics/testing/)
*   [4.0](https://docs.djangoproject.com/en/4.0/topics/testing/)
*   [3.2](https://docs.djangoproject.com/en/3.2/topics/testing/)
*   [3.1](https://docs.djangoproject.com/en/3.1/topics/testing/)
*   [3.0](https://docs.djangoproject.com/en/3.0/topics/testing/)
*   [2.2](https://docs.djangoproject.com/en/2.2/topics/testing/)
*   [2.1](https://docs.djangoproject.com/en/2.1/topics/testing/)
*   [2.0](https://docs.djangoproject.com/en/2.0/topics/testing/)
*   [1.11](https://docs.djangoproject.com/en/1.11/topics/testing/)
*   [1.10](https://docs.djangoproject.com/en/1.10/topics/testing/)
*   [1.8](https://docs.djangoproject.com/en/1.8/topics/testing/)

*   [](https://docs.djangoproject.com/en/6.0/topics/testing/#top)

Testing in Django[¶](https://docs.djangoproject.com/en/6.0/topics/testing/#testing-in-django "Link to this heading")
====================================================================================================================

Automated testing is an extremely useful bug-killing tool for the modern web developer. You can use a collection of tests – a **test suite** – to solve, or avoid, a number of problems:

*   When you’re writing new code, you can use tests to validate your code works as expected.

*   When you’re refactoring or modifying old code, you can use tests to ensure your changes haven’t affected your application’s behavior unexpectedly.

Testing a web application is a complex task, because a web application is made of several layers of logic – from HTTP-level request handling, to form validation and processing, to template rendering. With Django’s test-execution framework and assorted utilities, you can simulate requests, insert test data, inspect your application’s output and generally verify your code is doing what it should be doing.

The preferred way to write tests in Django is using the [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "(in Python v3.14)") module built-in to the Python standard library. This is covered in detail in the [Writing and running tests](https://docs.djangoproject.com/en/6.0/topics/testing/overview/) document.

You can also use any _other_ Python test framework; Django provides an API and tools for that kind of integration. They are described in the [Using different testing frameworks](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/#other-testing-frameworks) section of [Advanced testing topics](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/).

*   [Writing and running tests](https://docs.djangoproject.com/en/6.0/topics/testing/overview/)
*   [Testing tools](https://docs.djangoproject.com/en/6.0/topics/testing/tools/)
*   [Advanced testing topics](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/)

Previous page and next page

[Managing files](https://docs.djangoproject.com/en/6.0/topics/files/)

[Writing and running tests](https://docs.djangoproject.com/en/6.0/topics/testing/overview/)

[Back to Top](https://docs.djangoproject.com/en/6.0/topics/testing/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [Leukeleu donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [Testing in Django](https://docs.djangoproject.com/en/6.0/topics/testing/#)

### Browse

*   Prev: [Managing files](https://docs.djangoproject.com/en/6.0/topics/files/)
*   Next: [Writing and running tests](https://docs.djangoproject.com/en/6.0/topics/testing/overview/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [Using Django](https://docs.djangoproject.com/en/6.0/topics/)
        *   Testing in Django

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
