# Source: https://docs.beefree.io/beefree-sdk/visual-builders/ai-driven-design-creation.md

# AI-assisted Content Creation

{% hint style="info" %}
**Simple Schema Features by Plan Type:**

* **Superpowers & Enterprise Plans:** Access to Simple Schema for [Custom AddOns](#custom-addons) and [Custom Rows](https://docs.beefree.io/beefree-sdk/rows/reusable-content/create/pre-build/implement-custom-rows).
* **All Paid Plans:** Access the [Simple Schema API](https://docs.beefree.io/beefree-sdk/apis/content-services-api/convert#simple-to-full-json) through the [Content Services API](https://docs.beefree.io/beefree-sdk/apis/content-services-api) (CSAPI).
  {% endhint %}

## Overview

Saving your end users time when creating designs is more important than ever—especially as AI continues to reshape expectations. Today’s users want to move fast, and increasingly expect to generate polished, on-brand designs with just a prompt or a click. [Simple Schema](https://docs.beefree.io/beefree-sdk/data-structures/simple-schema) is built to meet that demand. It provides you with the building blocks you need to construct an AI-assisted content creation experience for your end users. This provides them with a faster, more flexible way to build emails, landing pages, and popups instantly inside your application.

[Simple Schema](https://docs.beefree.io/beefree-sdk/data-structures/simple-schema) empowers your team to unlock AI-assisted content creation and headless template generation—making it easier than ever to build designs programmatically, and 100% outside of Beefree SDK's visual builders. Whether you're building emails, landing pages, or popups, you can leverage Simple Schema as a lightweight, intuitive format that AI models can easily understand and generate.

## Headless Template Creation with AI

[Simple Schema](https://docs.beefree.io/beefree-sdk/data-structures/simple-schema) is designed for flexibility, making it ideal for AI-assisted and headless workflows. Imagine a tool where users describe the design they want in plain language, and submit that description to an AI agent. On the backend:

* An AI model receives the description and generates a Simple Schema-compatible template.
* This template is passed to the `/v1/conversion/simple-to-full-json` [API endpoint](https://docs.beefree.io/beefree-sdk/apis/content-services-api/convert#simple-to-full-json).
* The API returns the complete Beefree JSON for the entire template.
* The template is loaded in the builder, and the end user can start applying edits in a no-code environment.

The following GIF displays an example UI with a basic AI Email Design Assistant that connects to Simple Schema on the backend. By building your own UI and AI agent, you can leverage Simple Schema on the backend to programmatically build templates and load them in the Beefree SDK builder for your end users to use. The programmatically-created email template is loaded within the Beefree SDK builder, and ready for editing.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FCJUjdyNs14BoVGvin4ZJ%2FCleanShot%202025-08-01%20at%2020.26.55.gif?alt=media&#x26;token=8a8f010f-e864-4dce-b7b6-9d36dc079a1a" alt=""><figcaption></figcaption></figure>

Navigate to the [Simple Schema GitHub repository](https://github.com/BeefreeSDK/beefree-sdk-simple-schema/tree/main) to run the code for this demo locally on your machine and experiment with [Claude AI and Simple Schema](https://docs.beefree.io/beefree-sdk/resources/cookbook/create-ai-generated-emails-in-beefree-sdk-with-claude-ai).

## Benefits

Using [Simple Schema](https://docs.beefree.io/beefree-sdk/data-structures/simple-schema) for AI-driven design creation offers the following benefits:

* **AI-ready**: A simplified format perfect for machine-generated layouts.
* **Headless by default**: Build and deploy templates entirely outside the visual builder.
* **Production-ready**: Easily convert to Beefree JSON with a single API call.
* **Efficient**: Reduced payload size and faster AI generation.

## Simple to Full JSON API Endpoint

This endpoint is essential for converting AI-generated or manually assembled Simple Schema templates into full, builder-compatible Beefree JSON. Learn more about how to use this endpoint in the [Content Services API Reference](https://docs.beefree.io/beefree-sdk/apis/content-services-api).
