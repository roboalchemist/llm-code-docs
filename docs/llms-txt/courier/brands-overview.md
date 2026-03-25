# Source: https://www.courier.com/docs/platform/content/brands/brands-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What are Brands?

> Courier Brands define the visual appearance of your notifications. Customize logos, colors, headers, footers, and templates to ensure consistent styling across all channels.

## Overview

Brands in Courier define the visual appearance of your notifications. A brand includes your logo, colors, headers, footers, and custom styling that automatically apply to templates using that brand. Brands ensure visual consistency across all notifications without manually styling each template.

## When to Use Brands

* **Multi-tenant SaaS (White-labeling)**: Send notifications on behalf of your customers with their branding. Each customer gets their own brand with logo, colors, and styling.
* **Multiple Product Lines**: Maintain distinct visual identities for different products or services within your organization.
* **Regional or Market Variations**: Customize branding for different geographic regions or market segments while keeping template logic consistent.
* **A/B Testing Brand Styles**: Test different visual treatments by creating brand variants and comparing delivery metrics.

***

## Getting Started

### The Default Brand

Every workspace has a default brand that cannot be deleted. Customizing it is important because:

* Every email notification uses the Default Brand unless you manually disable Brands in template settings
* If you enable brands on a notification, the Default Brand is the fallback when no brand is specified in the Send API call

The default brand can be customized and renamed like any other brand.

<Frame caption="Brands list in the Courier dashboard">
  <img src="https://mintcdn.com/courier-4f1f25dc/BELbxySbf5lFIcUH/assets/platform/content/brand-list.png?fit=max&auto=format&n=BELbxySbf5lFIcUH&q=85&s=1665638b3dd335f1dce03ba08cf01e29" alt="Brands list showing brand name, palette, logo, and modified date" width="3456" height="1806" data-path="assets/platform/content/brand-list.png" />
</Frame>

### Creating a New Brand

1. In the sidebar, open the **Content** dropdown and select **Brands**
2. Click the **+ New** button to create a new brand
3. Enter a **name** for your brand (e.g., "Acme Client", "Northern EMEA")
4. Optionally set a `brand_id` for easier API reference

<Frame caption="Set brand name and ID in brand creator modal">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/create-brand.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=516fa786df0cc37e1a209f6bf82a4096" alt="New Brand" style={{width: 400}} width="800" height="504" data-path="assets/platform/content/create-brand.png" />
</Frame>

### Setting a Custom Brand as Default

To set a custom brand as your default, open the brand settings and click **Set As Default**.

***

## Sending Branded Notifications

To send a branded email:

1. Enable **Brand** in the template's settings
2. *(Optional)* Include a Brand ID in the [Send API call](/api-reference/send/send-a-message). If omitted, Courier uses the Default Brand.

<Frame caption="Brand Template Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-notification-settings.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=66fbb1e46f428d1bf8ba53687f5458d7" alt="Brand Template Settings" width="1870" height="1018" data-path="assets/platform/content/brand-notification-settings.png" />
</Frame>

***

## Brands API

Brands are fully API-enabled. Create, update, and delete brands programmatically using the [Brands API](/api-reference/brands/list-brands).

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Brand Designer" href="/platform/content/brands/brand-designer" icon="palette">
    Customize logos, colors, headers, footers, and templates
  </Card>

  <Card title="Brand Snippets" href="/platform/content/brands/brand-snippets" icon="code">
    Create reusable Handlebars components across brands
  </Card>

  <Card title="CSS Classnames" href="/platform/content/brands/css-classnames" icon="paintbrush">
    Style Courier blocks with custom CSS
  </Card>

  <Card title="Domain White Labeling" href="/platform/content/brands/email-domain-white-labeling" icon="envelope">
    Send emails from your own domain
  </Card>
</CardGroup>
