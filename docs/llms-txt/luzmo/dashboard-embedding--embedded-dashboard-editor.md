# Source: https://developer.cumul.io/guide/dashboard-embedding--embedded-dashboard-editor.md

---
title: Embedding the dashboard editor
description: Empower users to create and alter dashboards within your application by embedding the Luzmo dashboard editor with 'designer' or 'owner' roles.
url: https://developer.luzmo.com/guide/dashboard-embedding--embedded-dashboard-editor
type: guide
---

# Embed the dashboard editor

Empower your users to create and alter dashboards straight from within your application with our embedded dashboard editor. With the embedded dashboard editor, non-technical users can easily create their own insights based on the data they were given access to!

[Video](https://cdn.luzmo.com/academy/embedTheDashboardEditor/introEDE.mp4)

:::info
Before diving into the embedded dashboard editor guide, it might be useful to first understand how to [generate Embed Authorization tokens](guide/dashboard-embedding--generating-an-authorization-token.md) and read through the [Embedding dashboards](guide/dashboard-embedding--embed-into-application.md) guide to understand how to embed dashboards in view mode!
:::

Once you've embedded dashboards in view mode with Embed authorization tokens, it's very easy to further extend this setup to also allow (certain) end-user designers to use the dashboard editor embedded into your application. There are a few topics that are important for the embedded dashboard editor:

- In the Authorization request:
  - Define securable access rights - give at least `use` rights to your dashboards and datasets.
  - Specify the user role - give a `designer` or `owner` role to your user in the authorization request in your backend.
- In your frontend, you can set the `editMode` property of the frontend component to show the dashboard in the desired edit mode.


## Section Index

This reference is split into separate files. **For LLM agents**: Match the user's question to the headers below and read only the relevant sub-file(s).

### [Generate an Embed token with designer role and rights](https://developer.luzmo.com/guide/dashboard-embedding--embedded-dashboard-editor--generate-an-embed-token-with-designer-role-and-rights.md)


### [Embed the dashboard with an edit mode](https://developer.luzmo.com/guide/dashboard-embedding--embedded-dashboard-editor--embed-the-dashboard-with-an-edit-mode.md)


### [Capture events to enhance interactivity](https://developer.luzmo.com/guide/dashboard-embedding--embedded-dashboard-editor--capture-events-to-enhance-interactivity.md)



---

## Related Pages

- [Generating an Embed token](https://developer.luzmo.com/guide/dashboard-embedding--generating-an-authorization-token.md): Learn to securely authorize end-users by generating short-living Embed Authorization tokens server-side using an API key-token pair.
- [Handling multi-tenant data](https://developer.luzmo.com/guide/dashboard-embedding--handling-multi-tenant-data.md): Configure Luzmo for multi-tenant data setups with dynamic row-level filtering using parameterized filters and connection overrides for secure data access.
- [Embedding dashboards](https://developer.luzmo.com/guide/dashboard-embedding--embed-into-application.md): Learn to securely embed Luzmo dashboards into your application using Embed Authorization tokens with Web, React, Angular, Vue, and React Native components.
- [Embedding AI Assistant](https://developer.luzmo.com/guide/iq--introduction.md): Luzmo IQ enables AI-powered answers to data questions. Embed a chat component for interactive queries or an answer component to display AI responses.
- [Code-first visualizations](https://developer.luzmo.com/guide/flex--introduction.md): Luzmo Flex SDK allows you to create customizable visualizations entirely from code for building powerful, hyper-personalized data analytics products.


---

## Sitemap

- [Official best practices and implementation guidelines](https://developer.luzmo.com/AGENTS.md)
- [Overview of all docs pages](https://developer.luzmo.com/llms.txt)
