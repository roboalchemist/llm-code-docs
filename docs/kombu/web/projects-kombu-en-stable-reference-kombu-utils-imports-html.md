# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.imports.html

Title: Module Importing Utilities - kombu.utils.imports — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.imports.html

Markdown Content:
Module Importing Utilities - kombu.utils.imports — Kombu 5.6.2 documentation
===============

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html "JSON Utilities - kombu.utils.json") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html "Functional-style Utilities - kombu.utils.functional") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html) »
*   [Module Importing Utilities - `kombu.utils.imports`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.imports.html)

This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.imports.html).

Module Importing Utilities - `kombu.utils.imports`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.imports.html#module-importing-utilities-kombu-utils-imports "Link to this heading")
=================================================================================================================================================================================================================

Import related utilities.

kombu.utils.imports.symbol_by_name(_name_, _aliases=None_, _imp=None_, _package=None_, _sep='.'_, _default=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/imports.html#symbol_by_name)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.imports.html#kombu.utils.imports.symbol_by_name "Link to this definition")
Get symbol by qualified name.

The name should be the full dot-separated path to the class:

modulename.ClassName

Example:

celery.concurrency.processes.TaskPool
                            ^- class name

or using ‘:’ to separate module and symbol:

celery.concurrency.processes:TaskPool

If aliases is provided, a dict containing short name/long name mappings, the name is looked up in the aliases first.

Examples

>>> symbol_by_name('celery.concurrency.processes.TaskPool')
<class 'celery.concurrency.processes.TaskPool'>

>>> symbol_by_name('default', {
...     'default': 'celery.concurrency.processes.TaskPool'})
<class 'celery.concurrency.processes.TaskPool'>

# Does not try to look up non-string names. >>> from celery.concurrency.processes import TaskPool >>> symbol_by_name(TaskPool) is TaskPool True

[![Image 1: Logo of Kombu](https://docs.celeryq.dev/projects/kombu/en/stable/_static/kombusmall.jpg)](https://docs.celeryq.dev/projects/kombu/en/stable/index.html)

**Donations welcome:**![Image 2](https://www.paypalobjects.com/en_US/i/scr/pixel.gif)

#### Previous topic

[Functional-style Utilities - `kombu.utils.functional`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html "previous chapter")

#### Next topic

[JSON Utilities - `kombu.utils.json`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html "next chapter")

### This Page

*   [Show Source](https://docs.celeryq.dev/projects/kombu/en/stable/_sources/reference/kombu.utils.imports.rst.txt)

### Quick search

[![Image 3: Sponsored: Augment](https://media.ethicalads.io/media/images/2026/01/cropped_HCpyCwC.png)](https://server.ethicalads.io/proxy/click/10129/019cdcb0-a9a1-7e42-b42c-459b719f59e1/)

[**Augment Code Review**Beats Copilot, Cursor & Claude on Code Review**Install Now**](https://server.ethicalads.io/proxy/click/10129/019cdcb0-a9a1-7e42-b42c-459b719f59e1/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=rtd-sidebar-buy-ads)

![Image 4](https://server.ethicalads.io/proxy/view/10129/019cdcb0-a9a1-7e42-b42c-459b719f59e1/)

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html "JSON Utilities - kombu.utils.json") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html "Functional-style Utilities - kombu.utils.functional") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html) »
*   [Module Importing Utilities - `kombu.utils.imports`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.imports.html)

 © Copyright 2009-2019, Ask Solem & contributors.
