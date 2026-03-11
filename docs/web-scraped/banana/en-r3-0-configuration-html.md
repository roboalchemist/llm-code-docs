# Source: https://banana.readthedocs.io/en/r3.0/configuration.html

Title: Configuration — Banana 2.0 documentation

URL Source: https://banana.readthedocs.io/en/r3.0/configuration.html

Markdown Content:
Configuration — Banana 2.0 documentation
===============

[Banana](https://banana.readthedocs.io/en/r3.0/index.html)

 r3.0 

*   [Introduction](https://banana.readthedocs.io/en/r3.0/introduction.html)
*   [Installation](https://banana.readthedocs.io/en/r3.0/installation.html)
*   [Configuration](https://banana.readthedocs.io/en/r3.0/configuration.html)
*   [Project Layout](https://banana.readthedocs.io/en/r3.0/layout.html)
*   [Models](https://banana.readthedocs.io/en/r3.0/models.html)
*   [Testing](https://banana.readthedocs.io/en/r3.0/testing.html)
*   [Banana specific Django View Mixins](https://banana.readthedocs.io/en/r3.0/mixins.html)
*   [Banana and multiple databases](https://banana.readthedocs.io/en/r3.0/multidb.html)

[Banana](https://banana.readthedocs.io/en/r3.0/index.html)

*   [Docs](https://banana.readthedocs.io/en/r3.0/index.html) »
*   Configuration
*   [Edit on GitHub](https://github.com/transientskp/banana/blob/r3.0/doc/configuration.rst)

* * *

Configuration[¶](https://banana.readthedocs.io/en/r3.0/configuration.html#configuration "Permalink to this headline")
=====================================================================================================================

All settings are defined in the python module `project.settings`. banana first loads `project.settings.base` followed by `project.settings.local`. When you start using banana for the firs time, there will be no **local** file. You should copy `project.settings.local_example` to `project.settings.local` and adjust it to your environment. The **base** should contains all settings which are required by Banana and you should not modify this file. You should override, append or define new settings variables in **local**.

[**Still Using Cursor?**Fix bugs faster with Augment's full-codebase context.**Install Now**](https://server.ethicalads.io/proxy/click/10134/019cdf30-9b2e-7500-9c09-1211fc92e988/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

[Next](https://banana.readthedocs.io/en/r3.0/layout.html "Project Layout")[Previous](https://banana.readthedocs.io/en/r3.0/installation.html "Installation")

* * *

© Copyright 2014, Gijs Molenaar, John Swinbank, Tim Staley.  Revision `8d09b0d5`.

 Built with [Sphinx](http://sphinx-doc.org/) using a [theme](https://github.com/snide/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
