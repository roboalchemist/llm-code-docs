# Source: https://www.courier.com/docs/platform/content/content-blocks/template-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Template

> Template Blocks in Courier enable custom HTML, CSS, and Handlebars for richly styled emails. Supports dynamic content, markdown, and inline HTML rendering. Not compatible with plain text previews.

Template Blocks let you write custom HTML, CSS, and Handlebars directly in your email notifications. Use them for dynamic, richly formatted content that goes beyond what the visual block types offer.

<Warning>
  Plain Text

  Plain text preview is **not supported** for template blocks at this time. Anything created with template blocks will not render as plain text in emails.
</Warning>

<Frame caption="Template Block Boilerplate">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/template-block-standard.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=70f9c23bb7579920ad5ed75e35c109f2" alt="Template Block Boilerplate" width="770" height="327" data-path="assets/platform/content/template-block-standard.png" />
</Frame>

<Info>
  **Email Client Support**

  HTML and CSS support [varies by email client](https://www.campaignmonitor.com/css/).
</Info>

## Handlebars Templating Language

The Template Block supports Handlebars. You can learn about the language syntax from the [Handlebars Language Guide](https://handlebarsjs.com/guide/#language-features).

**Read more:** [Custom Courier Handlebars helpers](/platform/content/template-designer/handlebars-helpers).

## Styling with CSS and Handlebars

Combine CSS and Handlebars for dynamic styling:

<Frame caption="Template Block with CSS and Handlebars">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/template-block-styling.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=63718d61a96eaaf7cd05ecc18f58fbf1" alt="Template Block with CSS and Handlebars" width="770" height="795" data-path="assets/platform/content/template-block-styling.png" />
</Frame>

## Using Markdown in a Template Block

Render markdown between `{{#markdown}}` and `{{/markdown}}` within a template block.

```html  theme={null}
<div>
{{#markdown}}
  # Your Markdown Content

  - List item 1
  - List item 2
{{/markdown}}
</div>
```

## Using Replacement Variables in Handlebars

Insert variables from your JSON event data:

```handlebars  theme={null}
{{var "variable_name"}}
```

## Inserting HTML from Variables

To render HTML stored in a variable, use triple curly braces:

```handlebars  theme={null}
{{{htmlContent}}}
```

## Using Brand Snippets

You can reference [Brand Snippets](/platform/content/brands/brand-snippets) in template blocks using Handlebars partial syntax. This is useful for shared components like footers, disclaimers, or promotional banners:

```handlebars  theme={null}
{{>legal_footer}}
```

<CardGroup cols={2}>
  <Card title="Handlebars Helpers" href="/platform/content/template-designer/handlebars-helpers" icon="code">
    Logic, string, math, and date helpers for templates
  </Card>

  <Card title="Variables" href="/platform/content/variables/inserting-variables" icon="brackets-curly">
    Insert dynamic data into template blocks
  </Card>

  <Card title="Brand Snippets" href="/platform/content/brands/brand-snippets" icon="puzzle-piece">
    Reusable Handlebars components across brands
  </Card>

  <Card title="Content Block Basics" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Adding, reordering, and filtering blocks
  </Card>
</CardGroup>
