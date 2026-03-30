# Source: https://www.courier.com/docs/platform/content/content-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What are Templates?

> Templates define the content and structure of your notifications across all channels.

## Overview

Courier notifications are powered by flexible templates that allow you to define what your message says, how it looks, and how it behaves across channels.

Create a template once and send it across email, SMS, push, chat, and in-app channels. With Courier templates, you can design modular content blocks, configure routing and failover logic, and apply customized branding and variables across the appropriate channels.

## Two ways to build templates

Courier offers two main ways to create templates: a UI-based Designer for visual editing, and an API-based Elemental format for programmatic control. Most teams start with the UI Template Designer, which is accessible to both technical and non-technical users:

### **[Template Designer](/platform/content/template-designer/template-designer-overview)**

A powerful visual editor for building notifications with drag-and-drop blocks. Best for teams that want to create and iterate on templates without writing code. The designer provides real-time previews, test data injection, version history, and side-by-side channel editing.

<Frame caption="Template Designer">
  <img src="https://mintcdn.com/courier-4f1f25dc/t6vOhTOKkehrbARm/assets/platform/content/template-editor.png?fit=max&auto=format&n=t6vOhTOKkehrbARm&q=85&s=a0bc88a13b68befb14ba50920317f1f9" alt="Template Designer showing drag-and-drop blocks" width="3456" height="1924" data-path="assets/platform/content/template-editor.png" />
</Frame>

### **[Elemental](/platform/content/elemental/elemental-overview)**

A JSON format for creating and editing templates programmatically. Best for templates that live in your codebase, require complex logic, or need version control through Git. Elemental templates can be generated dynamically, tested in CI pipelines, and managed alongside your application code.

***

## What you can do with templates

### [Dynamic content](/platform/content/variables/inserting-variables)

Personalize notifications with variables from multiple data sources. Pull in user profile data, event payloads, tenant information, and brand settings to create contextual, relevant messages for each recipient.

### [Branding](/platform/content/brands/brands-overview)

Maintain visual consistency across all notifications. Configure logos, colors, fonts, and layouts that automatically apply to templates. Support white-labeling for multi-tenant applications where you send on behalf of customers.

### [Conditional logic](/platform/content/template-settings/send-conditions)

Control what content appears based on user data, preferences, or custom business rules. Show premium features to paid users, hide irrelevant sections, or adapt messaging based on account status or location.

### [Preview and testing](/platform/content/template-designer/how-to-preview-notification)

Validate templates before they go live. Inject test data to see exactly how notifications will render, preview across different brands, and send test emails to verify delivery and formatting.

### [Version control](/platform/content/template-designer/history-compare-mode)

Track every change to your templates with full version history. Compare versions side-by-side, see who made changes and when, and roll back to previous iterations if needed.

## Key Concepts

<CardGroup cols={2}>
  <Card title="Brands" href="/platform/content/brands/brands-overview" icon="palette">
    Apply consistent styles to notifications; assign brands per template as needed
  </Card>

  <Card title="Settings" href="/platform/content/template-settings/general-settings" icon="gear">
    Configure send conditions, channels, and approval workflows
  </Card>

  <Card title="Handlebars Helpers" href="/platform/content/template-designer/handlebars-helpers" icon="bicycle">
    Use Handlebars helpers for logic, formatting, and dynamic content
  </Card>

  <Card title="Localization" href="/platform/content/elemental/locales" icon="globe">
    Serve content in multiple languages based on user locale
  </Card>

  <Card title="Blocks" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Add text, images, buttons, and other content components
  </Card>

  <Card title="Elements" href="/platform/content/elemental/elements/index" icon="code">
    Add and configure building blocks in JSON; Elements map to the same content types as blocks
  </Card>
</CardGroup>
