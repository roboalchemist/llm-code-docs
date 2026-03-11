# Source: https://www.courier.com/docs/platform/content/brands/css-classnames.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Template CSS Classes

> Style Courier email templates using standardized CSS class names. Target content blocks, text elements, headers, footers, and other components with custom CSS in your brand templates.

Courier exposes standardized CSS classes on every email template element. Use these to customize the look and feel of your branded email notifications.

## Adding CSS to Your Brand Templates

Courier email templates use inline styles by default. You can add custom CSS in the `<style>` element in the `<head>` section of your brand; this works with both the Designer UI and custom MJML/Handlebars templates.

<Warning>
  You must use `!important` on all custom CSS rules. Courier renders email templates with [MJML](https://mjml.io/), which compiles to inline styles. Inline styles always win over class-based rules unless you add `!important`. Without it, your CSS classes will have no visible effect.
</Warning>

### Brand Designer View

<Frame caption="Brand Designer View">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-designer-view.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=1da14078eaaf2e0a8a37aa4e628a8db8" alt="Brand Designer View" width="669" height="267" data-path="assets/platform/content/brand-designer-view.png" />
</Frame>

### Custom Template View

<Frame caption="Custom Template View">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-custom-template-view.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=0ecbf1990224548ae374f2f5b32f464a" alt="Custom Template View" width="655" height="506" data-path="assets/platform/content/brand-custom-template-view.png" />
</Frame>

## MJML Rendering

Courier renders email templates using [MJML](https://mjml.io/), which compiles your template into nested HTML `<table>` structures. Each Courier block becomes a set of wrapper elements, so your target content is usually nested inside the CSS class rather than directly on it. Use the universal selector (`*`) to reach all child elements:

```css  theme={null}
.c--block-text * {
    color: red;
}
```

<Note>
  Test your CSS changes carefully. Create an email notification with the relevant block types and use the preview tab to verify the results.
</Note>

## Content Block Classes

| Class                | Targets                      |
| -------------------- | ---------------------------- |
| `.c--block-action`   | Action (button/link) blocks  |
| `.c--block-divider`  | Divider blocks               |
| `.c--block-image`    | Image blocks                 |
| `.c--block-list`     | List blocks                  |
| `.c--block-markdown` | Markdown blocks              |
| `.c--block-quote`    | Quote blocks                 |
| `.c--block-template` | Template (Handlebars) blocks |
| `.c--block-text`     | Text blocks                  |

## Text Classes

| Class              | Targets                  |
| ------------------ | ------------------------ |
| `.c--text-text`    | Body text                |
| `.c--text-subtext` | Subtext / secondary text |
| `.c--text-h1`      | Heading 1                |
| `.c--text-h2`      | Heading 2                |
| `.c--text-quote`   | Quote text style         |

## Layout Classes

| Class                  | Targets                    |
| ---------------------- | -------------------------- |
| `.c--email-header`     | Email header section       |
| `.c--email-header img` | Logo image in the header   |
| `.c--email-body`       | Email body section         |
| `.c--email-footer`     | Email footer section       |
| `.c--social`           | Social media links section |

## Example

To change the background color and font of all text blocks:

```css  theme={null}
.c--block-text * {
    font-family: Georgia, serif !important;
    background-color: #f9f9f9 !important;
}

.c--text-h1 * {
    color: #1a1a1a !important;
    font-size: 24px !important;
}
```

<CardGroup cols={2}>
  <Card title="Brand Designer" href="/platform/content/brands/brand-designer" icon="palette">
    Customize brand logos, colors, headers, and footers
  </Card>

  <Card title="Email Safe Formatting" href="/platform/content/email-safe-formatting" icon="envelope">
    HTML and CSS best practices for email clients
  </Card>
</CardGroup>
