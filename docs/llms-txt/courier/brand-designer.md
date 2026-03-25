# Source: https://www.courier.com/docs/platform/create/brand-designer.md

# Source: https://www.courier.com/docs/platform/content/brands/brand-designer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Brand Designer

> Customize brand appearance with logos, colors, headers, footers, and custom templates using the Brand Designer.

The Brand Designer lets you customize every aspect of your brand's visual appearance. Configure standard templates with simple settings, or use custom MJML/Handlebars for full control.

<Frame caption="Brand Designer">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-designer.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=9bd3e38e32a298c28ea99e11a192b0c5" alt="Brand Designer" width="2568" height="1096" data-path="assets/platform/content/brand-designer.png" />
</Frame>

## Standard Template

Customize Standard Template Brands with:

* Name
* Logo
* Brand colors (Primary, Secondary, Tertiary)
* Brand Header color
* Brand Footer Social URLs

<Note>
  **Logo Requirements**

  * Format: JPEG, PNG, or GIF
  * Width: 140px (height is flexible)
  * Maximum file size: 5MB
</Note>

## Custom MJML/Handlebars Template

Use a Custom MJML/Handlebars Template to fully customize the header, footer, and background using HTML, [MJML](https://mjml.io/), or [Handlebars](https://handlebarsjs.com/).

<Frame caption="Brand Custom Template">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-custom-template.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=94b5755591a656ec752c6f62d75d4533" alt="Brand Custom Template" style={{width: 500}} width="1520" height="1190" data-path="assets/platform/content/brand-custom-template.png" />
</Frame>

A custom template has four configurable fields:

### Head

The **Head** field injects content into the `<head>` element of the compiled email. Use it for `<style>` blocks, MSO conditional CSS for Outlook, and custom font imports. This is also where you apply [CSS Classnames](/platform/content/brands/css-classnames) to style Courier blocks.

```html  theme={null}
<style>
  /* Custom styles applied to all emails using this brand */
  .courier-text-block { font-family: Georgia, serif; }
  .courier-action-block a { background-color: #7d2f9a !important; }

  /* Outlook-specific overrides */
  <!--[if mso]>
  <style>
    td { font-family: Arial, sans-serif !important; }
  </style>
  <![endif]-->
</style>
```

<Warning>
  Courier's MJML compiler generates inline styles that take precedence over class-based rules. Add `!important` to your custom CSS class selectors to ensure they apply. See [CSS Classnames](/platform/content/brands/css-classnames) for details.
</Warning>

### Header

The **Header** field renders MJML or HTML content **above** your template's content blocks. Use it for branded banners, navigation bars, or promotional strips that appear at the top of every email.

```mjml  theme={null}
<mj-section background-color="#7d2f9a" padding="12px 24px">
  <mj-column>
    <mj-text color="#ffffff" font-size="14px" align="center">
      Free shipping on orders over $50
    </mj-text>
  </mj-column>
</mj-section>
```

### Footer

The **Footer** field renders MJML or HTML content **below** your template's content blocks. Use it for legal disclaimers, unsubscribe links, social media icons, or company address.

```mjml  theme={null}
<mj-section padding="24px">
  <mj-column>
    <mj-text font-size="12px" color="#999999" align="center">
      © 2026 Your Company · 123 Main St · <a href="{{{unsubscribe_url}}}">Unsubscribe</a>
    </mj-text>
  </mj-column>
</mj-section>
```

<Tip>
  For Outlook-compatible footers, wrap table-based HTML in `<mj-raw>` with MSO conditional comments. See [Email Safe Formatting](/platform/content/email-safe-formatting#formatting-mjml-for-outlook-compatibility) for the pattern.
</Tip>

### Background Colors and Layout

Both the **Custom MJML/Handlebars** and **Handlebars** template types expose a **Background Color** field and a **Width** field. The **Handlebars** type also exposes additional layout controls:

| Field                        | Custom MJML/Handlebars | Handlebars | Description                                                         |
| ---------------------------- | :--------------------: | :--------: | ------------------------------------------------------------------- |
| **Background Color**         |           Yes          |     Yes    | Overall email background color (behind the entire email)            |
| **Width**                    |           Yes          |     Yes    | Email container width (default `600px`)                             |
| **Content Background Color** |           No           |     Yes    | Background color for the content area (behind your template blocks) |
| **Footer Background Color**  |           No           |     Yes    | Background color for the footer section only                        |
| **Full Width Footer**        |           No           |     Yes    | Whether the footer background extends to the full email width       |

In Custom MJML/Handlebars mode, control content and footer backgrounds directly in your MJML code using `background-color` attributes on `<mj-section>` and `<mj-wrapper>` elements.

These fields can also be set via the [Brands API](/api-reference/brands/create-a-new-brand) on `settings.email.templateOverride`.

***

## Reusing Styles Across Brands

### Inheriting from the Default Brand

Use the **Inherit from Default Brand** toggle to inherit the `Head`, `Header`, or `Footer` from the Default brand. Both brands must use the standard brand type.

<Frame caption="Inherit from Default Brand">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-inherit-toggle.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=532bd4eea25f8300c0caeacffbb732c1" alt="Inherit from Default Brand" style={{width: 500}} width="1128" height="592" data-path="assets/platform/content/brand-inherit-toggle.png" />
</Frame>

### Using Brand Snippets

[Brand Snippets](/platform/content/brands/brand-snippets) let you share custom styles between standard and custom brand templates (Handlebars & MJML).

1. Create a snippet in your default brand with reusable CSS styling. You can use [CSS Classnames](/platform/content/brands/css-classnames) to style Courier blocks.

<Frame caption="CSS Snippet">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-style-snippet.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=539a57aaa6a3c79b77ad3977a87944b5" alt="CSS Snippet" style={{width: 500}} width="1126" height="372" data-path="assets/platform/content/brand-style-snippet.png" />
</Frame>

2. Reference the snippet in a custom brand's `Head` section:

```html  theme={null}
<style>
    {{>css-snippet-1}}
</style>
```

<Note>
  Snippets in your Default brand can be referenced in custom brands as long as the snippet name is unique.
</Note>

***

## Previewing Brands

To preview how your notification looks with different brands:

1. Open the template in the designer
2. Open **Preview**
3. Select a brand from **Preview Details > Brand**

<Frame caption="Notification Preview Details">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-preview-details.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=b36ec9dc770c48cbb3936239cd2f1471" alt="Notification Preview Details" style={{width: 250}} width="558" height="912" data-path="assets/platform/content/brand-preview-details.png" />
</Frame>

***

## Brand Variables Reference

Reference brand attributes in templates using the `var` helper with the `brand` prefix.

### Available Variables

| Variable                        | Description            |
| ------------------------------- | ---------------------- |
| `brand.id`                      | Brand identifier       |
| `brand.colors.primary`          | Primary brand color    |
| `brand.colors.secondary`        | Secondary brand color  |
| `brand.colors.tertiary`         | Tertiary brand color   |
| `brand.email.header.barColor`   | Email header bar color |
| `brand.email.header.logo.href`  | Logo click-through URL |
| `brand.email.header.logo.image` | Logo image URL         |
| `brand.social.facebook`         | Facebook profile URL   |
| `brand.social.instagram`        | Instagram profile URL  |
| `brand.social.linkedin`         | LinkedIn profile URL   |
| `brand.social.medium`           | Medium profile URL     |
| `brand.social.twitter`          | Twitter/X profile URL  |

### Examples

**Using brand colors for inline styling:**

```handlebars  theme={null}
<div style="background-color: {{var "brand.colors.primary"}};">
  Welcome to our platform!
</div>
```

**Adding social links in a footer:**

```handlebars  theme={null}
{{#if (var "brand.social.twitter")}}
  <a href="{{var "brand.social.twitter"}}">Follow us on Twitter</a>
{{/if}}
```

**Referencing the brand logo:**

```handlebars  theme={null}
<img src="{{var "brand.email.header.logo.image"}}" alt="Logo" />
```
