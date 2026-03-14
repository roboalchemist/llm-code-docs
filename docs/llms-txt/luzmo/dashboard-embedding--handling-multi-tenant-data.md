# Source: https://developer.cumul.io/guide/dashboard-embedding--handling-multi-tenant-data.md

---
title: Handling multi-tenant data
description: Configure Luzmo for multi-tenant data setups with dynamic row-level filtering using parameterized filters and connection overrides for secure data access.
url: https://developer.luzmo.com/guide/dashboard-embedding--handling-multi-tenant-data
type: guide
---

# Handling multi-tenant data

Luzmo can be used for all sorts of multi-tenant data configurations, from one single database with multi-tenant data to multiple single-tenant databases. In this section you'll find more details on the different solutions and how to easily set them up.


## Section Index

This reference is split into separate files. **For LLM agents**: Match the user's question to the headers below and read only the relevant sub-file(s).

### [Introduction](https://developer.luzmo.com/guide/dashboard-embedding--handling-multi-tenant-data--introduction.md)


### [Parameter filtering](https://developer.luzmo.com/guide/dashboard-embedding--handling-multi-tenant-data--parameter-filtering.md)

- Add a parameter filter
  - Define a parameter filter on the dataset level using an embed filter group
  - Define a parameter filter on a dashboard
- Override the parameter in the authorization request

### [Connection overrides](https://developer.luzmo.com/guide/dashboard-embedding--handling-multi-tenant-data--connection-overrides.md)

- Connection overrides for a standard Luzmo connection
- Connection overrides for a plugin connection


---

## Related Pages

- [Generating an Embed token](https://developer.luzmo.com/guide/dashboard-embedding--generating-an-authorization-token.md): Learn to securely authorize end-users by generating short-living Embed Authorization tokens server-side using an API key-token pair.
- [Embedding dashboards](https://developer.luzmo.com/guide/dashboard-embedding--embed-into-application.md): Learn to securely embed Luzmo dashboards into your application using Embed Authorization tokens with Web, React, Angular, Vue, and React Native components.
- [Embedding the dashboard editor](https://developer.luzmo.com/guide/dashboard-embedding--embedded-dashboard-editor.md): Empower users to create and alter dashboards within your application by embedding the Luzmo dashboard editor with 'designer' or 'owner' roles.
- [Embedding AI Assistant](https://developer.luzmo.com/guide/iq--introduction.md): Luzmo IQ enables AI-powered answers to data questions. Embed a chat component for interactive queries or an answer component to display AI responses.
- [Code-first visualizations](https://developer.luzmo.com/guide/flex--introduction.md): Luzmo Flex SDK allows you to create customizable visualizations entirely from code for building powerful, hyper-personalized data analytics products.


---

## Sitemap

- [Official best practices and implementation guidelines](https://developer.luzmo.com/AGENTS.md)
- [Overview of all docs pages](https://developer.luzmo.com/llms.txt)
