# Source: https://www.elastic.co/docs/extend/elasticsearch

﻿---
title: Create Elasticsearch plugins
description: Elasticsearch plugins are modular bits of code that add functionality to Elasticsearch. Plugins are written in Java and implement Java interfaces that...
url: https://www.elastic.co/docs/extend/elasticsearch
products:
  - Elasticsearch
---

# Create Elasticsearch plugins
Elasticsearch plugins are modular bits of code that add functionality to Elasticsearch. Plugins are written in Java and implement Java interfaces that are defined in the source code. Plugins are composed of JAR files and metadata files, compressed in a single zip file.
There are two ways to create a plugin:
<definitions>
  <definition term="Creating text analysis plugins with the stable plugin API">
    Text analysis plugins can be developed against the stable plugin API to provide Elasticsearch with custom Lucene analyzers, token filters, character filters, and tokenizers.
  </definition>
  <definition term="Creating classic plugins">
    Other plugins can be developed against the classic plugin API to provide custom authentication, authorization, or scoring mechanisms, and more.
  </definition>
</definitions>