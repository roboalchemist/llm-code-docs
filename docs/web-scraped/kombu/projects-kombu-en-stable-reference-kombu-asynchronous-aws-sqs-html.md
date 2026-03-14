# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.html

Title: Async Amazon SQS Client - kombu.asynchronous.aws.sqs — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.html

Markdown Content:
Async Amazon SQS Client - kombu.asynchronous.aws.sqs — Kombu 5.6.2 documentation
===============

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.connection.html "SQS Connection - kombu.asynchronous.aws.sqs.connection") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html "Amazon AWS Connection - kombu.asynchronous.aws.connection") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html) »
*   [Async Amazon SQS Client - `kombu.asynchronous.aws.sqs`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.html)

This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.asynchronous.aws.sqs.html).

Async Amazon SQS Client - `kombu.asynchronous.aws.sqs`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.html#async-amazon-sqs-client-kombu-asynchronous-aws-sqs "Link to this heading")
================================================================================================================================================================================================================================

[![Image 1: Logo of Kombu](https://docs.celeryq.dev/projects/kombu/en/stable/_static/kombusmall.jpg)](https://docs.celeryq.dev/projects/kombu/en/stable/index.html)

**Donations welcome:**![Image 2](https://www.paypalobjects.com/en_US/i/scr/pixel.gif)

#### Previous topic

[Amazon AWS Connection - `kombu.asynchronous.aws.connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html "previous chapter")

#### Next topic

[SQS Connection - `kombu.asynchronous.aws.sqs.connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.connection.html "next chapter")

### This Page

*   [Show Source](https://docs.celeryq.dev/projects/kombu/en/stable/_sources/reference/kombu.asynchronous.aws.sqs.rst.txt)

### Quick search

[![Image 3: Sponsored: Augment](https://media.ethicalads.io/media/images/2026/01/cropped_BYZ33XI.png)](https://server.ethicalads.io/proxy/click/10130/019cdcaf-74be-7b61-ba5a-e37237089585/)

[**Augment Code Review**Outperforms Cursor by 20% on Code Review**Install Now**](https://server.ethicalads.io/proxy/click/10130/019cdcaf-74be-7b61-ba5a-e37237089585/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=rtd-sidebar-buy-ads)

![Image 4](https://server.ethicalads.io/proxy/view/10130/019cdcaf-74be-7b61-ba5a-e37237089585/)

### Navigation

*   [index](https://docs.celeryq.dev/projects/kombu/en/stable/genindex.html "General Index")
*   [modules](https://docs.celeryq.dev/projects/kombu/en/stable/py-modindex.html "Python Module Index") |
*   [next](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.connection.html "SQS Connection - kombu.asynchronous.aws.sqs.connection") |
*   [previous](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html "Amazon AWS Connection - kombu.asynchronous.aws.connection") |
*   [Kombu 5.6.2 documentation](https://docs.celeryq.dev/projects/kombu/en/stable/index.html) »
*   [API Reference](https://docs.celeryq.dev/projects/kombu/en/stable/reference/index.html) »
*   [Async Amazon SQS Client - `kombu.asynchronous.aws.sqs`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.sqs.html)

 © Copyright 2009-2019, Ask Solem & contributors.
