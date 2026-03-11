# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html

Title: API Reference — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html

Markdown Content:
API Reference — Kombu 5.6.2 documentation
===============

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html "Kombu - kombu") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/faq.html "Frequently Asked Questions") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html)

This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/index.html).

API Reference[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html#api-reference "Link to this heading")
=============================================================================================================================

Release:
5.6

Date:
Dec 29, 2025

Kombu Core[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html#kombu-core "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

*   [Kombu - `kombu`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html)
*   [Common Utilities - `kombu.common`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html)
*   [Pattern matching registry - `kombu.matcher`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.matcher.html)
*   [Mixin Classes - `kombu.mixins`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html)
*   [Simple Messaging API - `kombu.simple`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html)
*   [Logical Clocks and Synchronization - `kombu.clocks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html)
*   [Carrot Compatibility - `kombu.compat`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html)
*   [Pidbox - `kombu.pidbox`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html)
*   [Exceptions - `kombu.exceptions`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html)
*   [Logging - `kombu.log`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.log.html)
*   [Connection - `kombu.connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html)
*   [Message Objects - `kombu.message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html)
*   [Message Compression - `kombu.compression`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html)
*   [Connection/Producer Pools - `kombu.pools`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html)
*   [Abstract Classes - `kombu.abstract`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html)
*   [Resource Management - `kombu.resource`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html)
*   [Message Serialization - `kombu.serialization`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html)

Kombu Transports[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html#kombu-transports "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

*   [Built-in Transports - `kombu.transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html)
*   [Transport Base Class - `kombu.transport.base`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html)
*   [Virtual Transport Base Class - `kombu.transport.virtual`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html)
*   [Virtual AMQ Exchange Implementation - `kombu.transport.virtual.exchange`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html)
*   [Azure Storage Queues Transport - `kombu.transport.azurestoragequeues`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html)
*   [Azure Service Bus Transport - `kombu.transport.azureservicebus`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html)
*   [Pure-python AMQP Transport - `kombu.transport.pyamqp`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html)
*   [librabbitmq AMQP transport - `kombu.transport.librabbitmq`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.librabbitmq.html)
*   [Apache QPid Transport - `kombu.transport.qpid`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html)
*   [In-memory Transport - `kombu.transport.memory`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html)
*   [Redis Transport - `kombu.transport.redis`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html)
*   [MongoDB Transport - `kombu.transport.mongodb`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html)
*   [Consul Transport - `kombu.transport.consul`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html)
*   [Etcd Transport - `kombu.transport.etcd`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html)
*   [Zookeeper Transport - `kombu.transport.zookeeper`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html)
*   [File-system Transport - `kombu.transport.filesystem`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html)
*   [SQLAlchemy Transport Model - `kombu.transport.sqlalchemy`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html)
*   [Amazon SQS Transport - `kombu.transport.SQS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html)
*   [SLMQ Transport - `kombu.transport.SLMQ`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html)
*   [Pyro Transport - `kombu.transport.pyro`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html)

Kombu Asynchronous[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html#kombu-asynchronous "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

*   [Event Loop - `kombu.asynchronous`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.html)
*   [Event Loop Implementation - `kombu.asynchronous.hub`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.hub.html)
*   [Semaphores - `kombu.asynchronous.semaphore`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html)
*   [Timer - `kombu.asynchronous.timer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.timer.html)
*   [Event Loop Debugging Utils - `kombu.asynchronous.debug`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html)
*   [Async HTTP Client - `kombu.asynchronous.http`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.html)
*   [Async HTTP Client Interface - `kombu.asynchronous.http.base`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html)
*   [Async pyCurl HTTP Client - `kombu.asynchronous.http.curl`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html)
*   [Async Amazon AWS Client - `kombu.asynchronous.aws`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.html)
*   [Amazon AWS Connection - `kombu.asynchronous.aws.connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html)
*   [Async Amazon SQS Client - `kombu.asynchronous.aws.sqs`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.html)
*   [SQS Connection - `kombu.asynchronous.aws.sqs.connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.connection.html)
*   [SQS Messages - `kombu.asynchronous.aws.sqs.message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.message.html)
*   [SQS Queues - `kombu.asynchronous.aws.sqs.queue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.queue.html)

Kombu utils[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html#kombu-utils "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

*   [Generic RabbitMQ manager - `kombu.utils.amq_manager`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.amq_manager.html)
*   [Custom Collections - `kombu.utils.collections`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.collections.html)
*   [Python Compatibility - `kombu.utils.compat`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html)
*   [Debugging Utilities - `kombu.utils.debug`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.debug.html)
*   [Div Utilities - `kombu.utils.div`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.div.html)
*   [String Encoding Utilities - `kombu.utils.encoding`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html)
*   [Async I/O Selectors - `kombu.utils.eventio`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.eventio.html)
*   [Functional-style Utilities - `kombu.utils.functional`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html)
*   [Module Importing Utilities - `kombu.utils.imports`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.imports.html)
*   [JSON Utilities - `kombu.utils.json`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html)
*   [Rate limiting - `kombu.utils.limits`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.limits.html)
*   [Object/Property Utilities - `kombu.utils.objects`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.objects.html)
*   [Consumer Scheduling - `kombu.utils.scheduling`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html)
*   [Text utilitites - `kombu.utils.text`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.text.html)
*   [Time Utilities - `kombu.utils.time`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.time.html)
*   [URL Utilities - `kombu.utils.url`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html)
*   [UUID Utilities - `kombu.utils.uuid`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.uuid.html)

[![Image 1: Logo of Kombu](https://docs.celeryq.dev/projects/kombu/en/stable/_static/kombusmall.jpg)](https://docs.celeryq.dev/projects/kombu/en/stable/index.html)

**Donations welcome:**![Image 2](https://www.paypalobjects.com/en_US/i/scr/pixel.gif)

#### Previous topic

[Frequently Asked Questions](https://docs.celeryq.dev/projects/kombu/en/stable/faq.html "previous chapter")

#### Next topic

[Kombu - `kombu`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html "next chapter")

### This Page

*   [Show Source](https://docs.celeryq.dev/projects/kombu/en/stable/_sources/reference/index.rst.txt)

### Quick search

[![Image 3: Sponsored: Augment](https://media.ethicalads.io/media/images/2026/01/cropped_EBRxlX2.png)](https://server.ethicalads.io/proxy/click/10131/019cdcaa-d4ed-7132-8ca5-1c9e0cb2626a/)

[**Augment Code Review**Benchmarked #1 Against Cursor, Copilot, Claude**Install Now**](https://server.ethicalads.io/proxy/click/10131/019cdcaa-d4ed-7132-8ca5-1c9e0cb2626a/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=rtd-sidebar-buy-ads)

![Image 4](https://server.ethicalads.io/proxy/view/10131/019cdcaa-d4ed-7132-8ca5-1c9e0cb2626a/)

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html "Kombu - kombu") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/faq.html "Frequently Asked Questions") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html)

 © Copyright 2009-2019, Ask Solem & contributors.
