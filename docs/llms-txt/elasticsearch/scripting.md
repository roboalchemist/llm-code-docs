# Source: https://www.elastic.co/docs/explore-analyze/scripting

﻿---
title: Scripting
description: With scripting, you can evaluate custom expressions in Elasticsearch. For example, you can use a script to return a computed value as a field or evaluate...
url: https://www.elastic.co/docs/explore-analyze/scripting
products:
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Scripting
With scripting, you can evaluate custom expressions in Elasticsearch. For example, you can use a script to return a computed value as a field or evaluate a custom score for a query.
The default scripting language is [Painless](https://www.elastic.co/docs/explore-analyze/scripting/modules-scripting-painless). Additional `lang` plugins are available to run scripts written in other languages. You can specify the language of the script anywhere that scripts run.

## Available scripting languages

Painless is purpose-built for Elasticsearch, can be used for any purpose in the scripting APIs, and provides the most flexibility. The other languages are less flexible, but can be useful for specific purposes.

| Language                                                                                           | Sandboxed                                                         | Required plugin | Purpose                         |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|-----------------|---------------------------------|
| [`painless`](https://www.elastic.co/docs/explore-analyze/scripting/modules-scripting-painless)     | ![Yes](https://doc-icons.s3.us-east-2.amazonaws.com/icon-yes.png) | Built-in        | Purpose-built for Elasticsearch |
| [`expression`](https://www.elastic.co/docs/explore-analyze/scripting/modules-scripting-expression) | ![Yes](https://doc-icons.s3.us-east-2.amazonaws.com/icon-yes.png) | Built-in        | Fast custom ranking and sorting |
| [`mustache`](https://www.elastic.co/docs/solutions/search/search-templates)                        | ![Yes](https://doc-icons.s3.us-east-2.amazonaws.com/icon-yes.png) | Built-in        | Templates                       |
| [`java`](https://www.elastic.co/docs/explore-analyze/scripting/modules-scripting-engine)           | ![No](https://doc-icons.s3.us-east-2.amazonaws.com/icon-no.png)   | Not available   | Expert API                      |