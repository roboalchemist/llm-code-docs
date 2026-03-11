# Source: https://www.courier.com/docs/platform/content/design-studio/custom-code-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# HTML Blocks

> Add HTML markup in Design Studio. Use for advanced layout, tracking, or channel-specific markup.

HTML blocks let you add raw HTML or other markup to your notification content. Use them when you need full control over markup (e.g. tracking pixels, custom layouts, or channel-specific HTML).

## Adding an HTML block

1. In Design Studio, select a channel.
2. Add an **HTML** block from the block sidebar or toolbar.
3. Enter your HTML in the block editor.

<Frame caption="HTML Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-custom-code-new.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=798027ddd2fb31ae86449918046b5a7a" alt="HTML block in Design Studio" width="2294" height="1146" data-path="assets/platform/content/designer-v2/designer-v2-custom-code-new.png" />
</Frame>

## HTML editor

The HTML block offers an inline code editor in the right panel. Enter standard HTML (like `<div>`, `<table>`, or `<img>`) and inline CSS for custom layouts or tracking (e.g., analytics pixels).

<Frame caption="HTML Editor">
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-custom-code-editor.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=b02ddef2391256443e062aeb7478c838" alt="HTML editor in Design Studio" width="1812" height="1294" data-path="assets/platform/content/designer-v2/designer-v2-custom-code-editor.png" />
</Frame>

Changes in the editor appear instantly in the canvas preview. You can see your updates reflected in real time as you type.

<Frame caption="Rendered Example">
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-custom-code-rendered.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=2462dd1bb394c15fddf2dd5f9452aa58" alt="HTML example in Design Studio" width="2740" height="1178" data-path="assets/platform/content/designer-v2/designer-v2-custom-code-rendered.png" />
</Frame>

<Tip>
  Click the expand icon in the top-right corner of the code editor to open a larger editing window.
</Tip>

## Variables and handlebars

HTML blocks support [variables](/platform/content/variables/inserting-variables) using the `{{variable}}` syntax and [handlebars helpers](/platform/content/template-designer/handlebars-helpers) like `{{#if}}` for conditional logic.

<Frame caption="Handlebars Example">
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-custom-code-rendered-handlebars.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=e4a2fb30a4b51268972d3c2d222446de" alt="Handlebars and variables in HTML block" width="2726" height="1630" data-path="assets/platform/content/designer-v2/designer-v2-custom-code-rendered-handlebars.png" />
</Frame>

<Note>
  Variables (`{{variable}}`) and handlebars (`{{#if}}` etc) in HTML blocks only resolve on actual send; during [preview mode](/platform/content/template-designer/how-to-preview-notification), you'll see the raw syntax, not sample values.
</Note>

## Best practices

* Keep markup minimal and test across channels.
* Use variables for dynamic content rather than hardcoding.
* Validate your HTML and CSS to avoid rendering issues in different email clients.

## Related

<CardGroup cols={2}>
  <Card title="Variables" icon="code" href="/platform/content/variables/inserting-variables">
    Dynamic content in code
  </Card>

  <Card title="Email-Safe Formatting" icon="shield" href="/platform/content/email-safe-formatting">
    Tips for reliable HTML and CSS
  </Card>
</CardGroup>
