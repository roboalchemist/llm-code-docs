# Source: https://docs.datadoghq.com/cloudcraft/getting-started/generate-api-key.md

---
title: Generate an API Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Getting started > Generate an API Key
---

# Generate an API Key

Cloudcraft offers a [developer API](https://docs.datadoghq.com/cloudcraft/api/) that provides programmatic access and remote rendering of your architecture diagrams. The API also provides fully automated visualization of AWS and Azure accounts that are linked with your Cloudcraft account, either as ready-to-use images or as JSON data.

Authentication is required to use this API. This guide describes how to create an API key through the web interface.

{% alert level="info" %}
The ability to use Cloudcraft's developer API is available only to Pro subscribers. See [Cloudcraft's pricing page](https://www.cloudcraft.co/pricing) for more information about subscription plans.
{% /alert %}

## Prerequisites{% #prerequisites %}

This guide assumes you have:

- A Cloudcraft user with either the [Owner or Administrator role](https://docs.datadoghq.com/cloudcraft/account-management/roles-and-permissions/).
- An active [Cloudcraft Pro subscription](https://www.cloudcraft.co/pricing).

## Create an API key{% #create-an-api-key %}

To create an API key for automation, go to **User** > **API keys** and click **Create API key**.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/generate-api-key/create-api-key-button.6e070ad71f755a1e6d068d2c40d6cba3.png?auto=format"
   alt="Screenshot of Cloudcraft's user interface for managing API keys with a focus on the 'Create API key' button." /%}

Name the key to describe its purpose, for example, 'Automation Key,' and assign the appropriate permissions. Select the permission that best fits this key, but try to follow the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). The same principle applies when giving teams access to this key.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/generate-api-key/create-api-key-window.36da83c5779ecc652ac90a01bece44d1.png?auto=format"
   alt="Screenshot of Cloudcraft's API key creation interface with fields for naming and setting permissions." /%}

When you're done, click **Save key** to create a new API key. Make sure to write down the key in a secure location so you can use it later.

If you have any questions or issues with creating an API key, [contact Cloudcraft's support team through the in-app beacon](https://app.cloudcraft.co/support).
