# Source: https://www.courier.com/docs/platform/content/brands/brand-snippets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Brand Snippets

> Courier Brand Snippets are reusable Handlebars components. Create them under any brand, use them in templates via the snippet name, customize with variables, and extend default snippets in custom brands.

## What are Brand Snippets?

Snippets are reusable pieces of [Handlebars](https://handlebarsjs.com/) code that you can include in your email templates. Use snippets for content that appears across multiple templates, like:

* Standard legal disclaimers or footer text
* Social media links
* Promotional banners or CTAs
* Support contact information

Snippets are defined at the brand level and can be referenced by name in any template that uses that brand.

<Frame caption="Brand Snippet">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-snippet.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=a069a749570b3910062bb61877091f6c" alt="Brand Snippet" width="2118" height="650" data-path="assets/platform/content/brand-snippet.png" />
</Frame>

## Creating a Brand Snippet

To create a Snippet:

1. Navigate to the **Brands** tab in Courier
2. Select the brand you want to add the snippet to
3. Click the **Snippets** tab
4. Click **Add Snippet**
5. Give your snippet a name (this is how you'll reference it in templates)
6. Add your Handlebars content

## Using Brand Snippets in Templates

Reference snippets in a **Template Block** using Handlebars partial syntax:

```handlebars  theme={null}
{{>snippet_name}}
```

For example, if you created a snippet named `legal_footer`:

```handlebars  theme={null}
{{>legal_footer}}
```

<Frame caption="Brand Snippet Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-snippet-block.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=0f1c0a04f0b19f7f6f9766bca6391eca" alt="Brand Snippet Block" width="1540" height="558" data-path="assets/platform/content/brand-snippet-block.png" />
</Frame>

Using the notification preview allows you to see the snippet rendered:

<Frame caption="Brand Snippet Preview">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-snippet-preview.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=9bf29515ad05bb7bd9ea060a6d16b02f" alt="Brand Snippet Preview" width="1540" height="464" data-path="assets/platform/content/brand-snippet-preview.png" />
</Frame>

## Customizing Snippets with Variables

Snippets can include variables that get populated from data passed in the Send API call. Use standard Handlebars variable syntax within your snippet:

```handlebars  theme={null}
<p>Thanks for being a customer since {{profile.member_since}}!</p>
<p>Your current plan: {{data.plan_name}}</p>
```

Variables in snippets have access to the same data context as the rest of your template, including `profile`, `data`, and `brand` variables.

<Frame caption="Brand Snippet Variables">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-snippet-variables.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=c8b2a99e5c5f43eb819ea6f470ff45fd" alt="Brand Snippet Variables" width="942" height="422" data-path="assets/platform/content/brand-snippet-variables.png" />
</Frame>

## Snippet Inheritance from the Default Brand

Custom brands **extend** the default brand's snippets. This means:

* Snippets defined in the default brand are automatically available in all custom brands
* If a custom brand defines a snippet with the same name, it overrides the default brand's snippet
* Custom brands can have their own additional snippets alongside inherited ones

**Example**:

* Default brand has snippets: `footer`, `social_links`, `legal_text`
* Custom brand "Acme" has snippet: `footer` (custom version)
* When using Acme brand: `footer` uses Acme's version, `social_links` and `legal_text` use the default brand's versions

This inheritance model lets you:

* Define common snippets once in the default brand
* Override specific snippets per brand when needed
* Avoid duplicating content across brands

## Related Resources

<CardGroup cols={2}>
  <Card title="Brands Overview" href="/platform/content/brands/brands-overview" icon="palette">
    Learn how to configure and use brands
  </Card>

  <Card title="Handlebars Helpers" href="/platform/content/template-designer/handlebars-helpers" icon="code">
    Formatting and logic helpers for snippets
  </Card>
</CardGroup>
