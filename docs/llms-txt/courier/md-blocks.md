# Source: https://www.courier.com/docs/platform/content/content-blocks/md-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Markdown

> Markdown Blocks enable cross-channel rich content using standard Markdown syntax. Support dynamic variables, personalization, and conditional rendering—ideal for scalable, consistent notifications in email, SMS, push, and more.

Markdown Blocks let you write formatted content using plain text syntax that renders across all notification channels.

<Frame caption="New Markdown Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/md-block-new.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=cdbc1553cdc878d9afac08283217642e" alt="New Markdown Block" width="1300" height="614" data-path="assets/platform/content/md-block-new.png" />
</Frame>

## Key Features

* Cross-channel compatibility: Create content once and deliver it consistently across email, push, SMS and other channels.
* Rich formatting: Use Markdown syntax to add headings, lists, links, emphasis and more.
* Variable support: Insert dynamic user data and personalize content.
* Conditional rendering: Show or hide Markdown Blocks based on conditions.

## Working with Markdown Blocks

### Adding a Markdown Block

1. In the Courier designer, click the "+" icon to add a new block
2. Select "Markdown" from the block options
3. Enter your Markdown content in the editor

### Markdown Syntax

Courier supports standard Markdown syntax, including:

* Headings (# H1, ## H2, etc)
* Lists (bulleted and numbered)
* Links Link text
* Emphasis (italic, bold)
* And more

For a complete reference, see the [Markdown syntax guide](https://daringfireball.net/projects/markdown/syntax).

### Inserting Variables

To insert a variable into your Markdown, use double curly braces: `{{variable_name}}`. The variable will be replaced with actual data when the notification is sent.

<CardGroup cols={2}>
  <Card title="Content Block Basics" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Adding, reordering, and filtering blocks
  </Card>

  <Card title="Template Blocks" href="/platform/content/content-blocks/template-blocks" icon="code">
    Full HTML/Handlebars for advanced formatting
  </Card>

  <Card title="Variables" href="/platform/content/variables/inserting-variables" icon="brackets-curly">
    Insert dynamic data into markdown content
  </Card>

  <Card title="Text Blocks" href="/platform/content/content-blocks/text-blocks" icon="align-left">
    Rich text with inline conditions
  </Card>
</CardGroup>
