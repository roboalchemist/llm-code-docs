# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html

Title: kombu.utils.collections — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html

Markdown Content:
Custom Collections - kombu.utils.collections — Kombu 5.6.2 documentation
===============

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html "Python Compatibility - kombu.utils.compat") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.amq_manager.html "Generic RabbitMQ manager - kombu.utils.amq_manager") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html) »
*   [Custom Collections - `kombu.utils.collections`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html)

This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.collections.html).

Custom Collections - `kombu.utils.collections`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html#custom-collections-kombu-utils-collections "Link to this heading")
=============================================================================================================================================================================================================

Custom maps, sequences, etc.

_class_ kombu.utils.collections.EqualityDict[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/collections.html#EqualityDict)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html#kombu.utils.collections.EqualityDict "Link to this definition")
Dict using the eq operator for keying.

_class_ kombu.utils.collections.HashedSeq(_*seq_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/collections.html#HashedSeq)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html#kombu.utils.collections.HashedSeq "Link to this definition")
Hashed Sequence.

Type used for hash() to make sure the hash is not generated multiple times.

hashvalue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html#kombu.utils.collections.HashedSeq.hashvalue "Link to this definition")kombu.utils.collections.eqhash(_o_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/collections.html#eqhash)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html#kombu.utils.collections.eqhash "Link to this definition")
Call `obj.__eqhash__`.

[![Image 1: Logo of Kombu](https://docs.celeryq.dev/projects/kombu/en/stable/_static/kombusmall.jpg)](https://docs.celeryq.dev/projects/kombu/en/stable/index.html)

**Donations welcome:**![Image 2](https://www.paypalobjects.com/en_US/i/scr/pixel.gif)

#### Previous topic

[Generic RabbitMQ manager - `kombu.utils.amq_manager`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.amq_manager.html "previous chapter")

#### Next topic

[Python Compatibility - `kombu.utils.compat`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html "next chapter")

### This Page

*   [Show Source](https://docs.celeryq.dev/projects/kombu/en/stable/_sources/reference/kombu.utils.collections.rst.txt)

### Quick search

[![Image 3: Sponsored: ClickSend](https://media.ethicalads.io/media/images/2025/05/Messaging_as_fast_as_hello_world_240x180.png)](https://server.ethicalads.io/proxy/click/10198/019cdcaf-ea32-7e21-88f2-8b46f7ac3cd6/)

[**The Messenger API for devs.**Simple setup, strong support, and global delivery with one API.**Send now.**](https://server.ethicalads.io/proxy/click/10198/019cdcaf-ea32-7e21-88f2-8b46f7ac3cd6/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=rtd-sidebar-buy-ads)

![Image 4](https://server.ethicalads.io/proxy/view/10198/019cdcaf-ea32-7e21-88f2-8b46f7ac3cd6/)

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html "Python Compatibility - kombu.utils.compat") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.amq_manager.html "Generic RabbitMQ manager - kombu.utils.amq_manager") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html) »
*   [Custom Collections - `kombu.utils.collections`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html)

 © Copyright 2009-2019, Ask Solem & contributors.
