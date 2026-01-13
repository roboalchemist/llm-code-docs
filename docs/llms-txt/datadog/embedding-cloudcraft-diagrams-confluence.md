# Source: https://docs.datadoghq.com/cloudcraft/getting-started/embedding-cloudcraft-diagrams-confluence.md

---
title: Embedding Cloudcraft Diagrams with the Confluence App
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Getting started > Embedding Cloudcraft
  Diagrams with the Confluence App
source_url: >-
  https://docs.datadoghq.com/getting-started/embedding-cloudcraft-diagrams-confluence/index.html
---

# Embedding Cloudcraft Diagrams with the Confluence App

In this article, we'll walk you through the process of seamlessly integrating your current Cloudcraft diagrams into a Confluence page by using Cloudcraft's Confluence app.

This process allows you to grant access to diagrams for authorized users without requiring them to have individual Cloudcraft subscriptions, while also granting you a centralized and up-to-date version of your infrastructure documentation.

## Installing the app{% #installing-the-app %}

To install Cloudcraft's Confluence application, log in to Confluence as an admin, navigate to [the Cloudcraft marketplace listing](https://marketplace.atlassian.com/apps/1233281/cloudcraft-aws-and-azure-cloud-diagrams-for-confluence?hosting=cloud&tab=overview), and then click **Get it now**.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/embedding-cloudcraft-diagrams-confluence/marketplace-listing.1cd8b38acc4f8cb887293a34c99b5b85.png?auto=format"
   alt="Cloudcraft's app on the Atlassian Marketplace." /%}

## Using the app{% #using-the-app %}

With a Confluence page open, type **/cloudcraft**, and then click the application command that appears.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/embedding-cloudcraft-diagrams-confluence/embed-command.46a6826a0a75bc94e119776334aa1fdd.png?auto=format"
   alt="The Cloudcraft integration tool for embedding diagrams in a Confluence document." /%}

Next, click **Sign in** to log in to your Cloudcraft account.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/embedding-cloudcraft-diagrams-confluence/signin-or-signup.d3e01e9d380c6988a9f3bfac38a49c4e.png?auto=format"
   alt="The Cloudcraft login page for the Confluence integration with options to sign in with Datadog, Google, or email." /%}

Once you're logged in, the diagram picker appears. Select the diagram you want to embed from the list.

{% alert level="info" %}
You can also search, filter, and sort diagrams in the diagram picker.
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/embedding-cloudcraft-diagrams-confluence/blueprint-picker.2dc948a52a204d9aa047a2828bb9cfd6.png?auto=format"
   alt="The Cloudcraft Confluence app showing options to insert cloud architecture blueprints into a Confluence page with labeled diagrams for staging and production environments." /%}

After selecting a diagram, a preview of the embedded diagram appears in your Confluence page. At this point, you can also select from the window size menu to resize the width of the diagram, or click the pencil icon to reopen the diagram picker.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/embedding-cloudcraft-diagrams-confluence/window-size-menu.54830fb244fcde9e28c31952fd4d1380.png?auto=format"
   alt="An isometric view of a cloud infrastructure layout in Cloudcraft featuring EC2 instances, load balancers, and RDS databases embedded in a Confluence page." /%}

When publishing or previewing the Confluence page, your Cloudcraft diagram will be fully embedded on the page.

Embedded diagrams are only viewable by Confluence user accounts, and are not visible when accessing the public URL of a Confluence page.
