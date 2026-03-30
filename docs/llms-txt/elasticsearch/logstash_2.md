# Source: https://www.elastic.co/docs/extend/logstash

﻿---
title: Contribute to Logstash
description: You can add your own input, codec, filter, or output plugins to Logstash. Start with the end in mind. These guidelines and best practices can help you...
url: https://www.elastic.co/docs/extend/logstash
products:
  - Logstash
---

# Contribute to Logstash
You can add your own input, codec, filter, or output plugins to Logstash.

### Acceptance guidelines

Start with the end in mind. These guidelines and best practices can help you build a better plugin, even if you choose not to share it with the world.
- **Consistency.** Your plugin must be consistent in quality and naming conventions used by other plugins. The plugin name must be unique and in this format: `logstash-plugintype-pluginname`. If the plugin name is more than one word, separate words after plugin type with underscores. Example: *logstash-output-elastic_app_search*
- **Documentation.** Documentation is a required component of your plugin. If we list your plugin in the Logstash Reference, we point to your documentation—a readme.md, docs/index.asciidoc, or both—in your plugin repo.
- **Code Review.** Your plugin must be reviewed by members of the community for coherence, quality, readability, stability and security.
- **Tests.** Your plugin must contain tests to be accepted. You can refer to [http://betterspecs.org/](http://betterspecs.org/) for examples.
  - Step 1. Enable travis on your account
- Step 2. Import our standard travis.yml [[https://github.com/logstash-plugins/.ci/blob/1.x/travis/travis.yml](https://github.com/logstash-plugins/.ci/blob/1.x/travis/travis.yml)](https://github.com/logstash-plugins/.ci/blob/1.x/travis/travis.yml), as shown in the [fingerprint filter example](https://github.com/logstash-plugins/logstash-filter-fingerprint/blob/main/.travis.yml).
- Step 3. Have specs in the spec folder.


## Add a plugin

Plugins can be developed and deployed independently of the Logstash core. Here are some documents to guide you through the process of coding, deploying, and sharing your plugin:
- Write a new plugin
  - [How to write a Logstash input plugin](https://www.elastic.co/docs/extend/logstash/input-new-plugin)
- [How to write a Logstash codec plugin](https://www.elastic.co/docs/extend/logstash/codec-new-plugin)
- [How to write a Logstash filter plugin](https://www.elastic.co/docs/extend/logstash/filter-new-plugin)
- [How to write a Logstash output plugin](https://www.elastic.co/docs/extend/logstash/output-new-plugin)
- [Community Maintainer’s Guide](https://www.elastic.co/docs/extend/logstash/community-maintainer)
- [Document your plugin](https://www.elastic.co/docs/extend/logstash/plugin-doc)
- [Publish your plugin to RubyGems.org](https://www.elastic.co/docs/extend/logstash/publish-plugin)
- [List your plugin](https://www.elastic.co/docs/extend/logstash/plugin-listing)
- Contribute a patch
  - [Contributing a patch to a Logstash plugin](https://www.elastic.co/docs/extend/logstash/contributing-patch-plugin)
- [Extending Logstash core](https://www.elastic.co/docs/extend/logstash/contribute-to-core)


#### Plugin Shutdown APIs

You have three options for shutting down a plugin: `stop`, `stop?`, and `close`.
- Call the `stop` method from outside the plugin thread. This method signals the plugin to stop.
- The `stop?` method returns `true` when the `stop` method has already been called for that plugin.
- The `close` method performs final bookkeeping and cleanup after the plugin’s `run` method and the plugin’s thread both exit. The `close` method is a a new name for the method known as `teardown` in previous versions of Logstash.

The `shutdown`, `finished`, `finished?`, `running?`, and `terminating?` methods are redundant and no longer present in the Plugin Base class.
Sample code for the plugin shutdown APIs is [available](https://github.com/logstash-plugins/logstash-input-example/blob/main/lib/logstash/inputs/example.rb).