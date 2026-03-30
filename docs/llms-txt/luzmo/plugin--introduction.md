# Source: https://developer.cumul.io/guide/plugin--introduction.md

---
title: Introduction
url: https://developer.luzmo.com/guide/plugin--introduction
type: guide
---

# Plugin API

With Luzmo's Plugin API, you can connect arbitrary data sources, private or public APIs or open data sources for which Luzmo does not offer a native connector (yet). Plugins are connectors in Luzmo that your user(s) can use to create (authenticated) connections to, import dataset(s) from, and retrieve data from those dataset(s).

Each Plugin is a small RESTful API that acts as an **adapter** between Luzmo and a source system. It consists of [2 mandatory and 2 optional endpoints](/guide/plugin--endpoints.md), and can optionally call webhooks to notify Luzmo of events.

Example Plugin implementations are available:

- [Citybik.es plugin](https://github.com/luzmo-official/cumul.io-plugin/tree/master/open/citybikes) (using authentication type `none`)
- [MongoDB plugin](https://github.com/luzmo-official/cumul.io-plugin/tree/master/token/mongodb) (using authentication type `token`)
- [Asana plugin](https://github.com/luzmo-official/cumul.io-plugin/tree/master/oauth2/asana) (using authentication type `oauth2`)
- [SQL based plugins](https://github.com/luzmo-official/cumul.io-plugin/tree/master/sql) for MySQL, Postgres and SQL Server using `host`, `key`, `token` authentication.

During development of a new Plugin, you might want to use a service like [ngrok](https://ngrok.com) to tunnel HTTPS requests to your local environment. We also strongly recommend taking a look at the interactive Plugin checklist in [this Academy article](https://academy.luzmo.com/article/dds1ul5m), which provides several important checks to ensure your plugin is secure and adheres to the specifications!

---

## Related Pages

- [Registering a plugin](https://developer.luzmo.com/guide/plugin--registering-a-plugin.md)
- [Plugin endpoints](https://developer.luzmo.com/guide/plugin--endpoints.md)
- [Version history](https://developer.luzmo.com/guide/plugin--version-history.md)
- [Webhooks](https://developer.luzmo.com/guide/plugin--webhooks.md)


---

## Sitemap

- [Official best practices and implementation guidelines](https://developer.luzmo.com/AGENTS.md)
- [Overview of all docs pages](https://developer.luzmo.com/llms.txt)
