# Source: https://www.courier.com/docs/platform/content/content-blocks/content-block-basics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Content Block Overview

> Courier Content Blocks are reusable, drag-and-drop components for building cross-channel notifications. They support variables, conditional logic, custom styling, and include types like text, image, markdown, list, and more.

Content Blocks are the building blocks of your notifications in Courier. They are reusable, drag-and-drop components that allow you to build notification content across multiple channels. Key features include:

* Responsive and cross-channel by default
* Reusable across different notification channels
* Support for [variables](/platform/content/variables/inserting-variables) and [conditional filtering](/platform/content/template-settings/send-conditions#for-content-blocks)

## Type of Content Blocks

* Text Blocks
* Image Blocks
* Action Blocks
* Divider Blocks
* Markdown Blocks
* Quote Blocks
* Template Blocks
* List Blocks
* Jsonnet Blocks

Some blocks, like Text and Action Blocks, have channel-specific options or formatting. For example, you can set the color of a text block differently for email and SMS.

## Working with Content Blocks

### Adding Content Blocks

1. Create a new notification and add delivery channels
2. Use the content toolbar to add desired block types
3. Drag and drop blocks to reorder them

<Frame caption="Content Toolbar">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/block-basics-blocks.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=63e2196e6f8fe8633a5faf384daf7792" alt="Content Toolbar" width="771" height="365" data-path="assets/platform/content/block-basics-blocks.png" />
</Frame>

### Using the Content Block Library

The Block Library stores shared channel content:

* Displays blocks not in use by the selected channel
* Marks unused blocks for easy identification
* Allows deletion of unused blocks

<Frame caption="Block Library">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/block-basics-library.gif?s=1e241a27ef9a6b4a35ecf488f97b82e8" alt="Block Library" width="1150" height="767" data-path="assets/platform/content/block-basics-library.gif" />
</Frame>

### Applying Conditional Filters

You can hide or show blocks based on specific conditions:

1. Select a block and click the filter button

<Frame caption="Filter Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/block-basics-conditions.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=726681d90ecc616fc2e14658b74907ca" alt="Filter Settings" width="600" height="223" data-path="assets/platform/content/block-basics-conditions.png" />
</Frame>

2. Set conditions in the modal that appears. You can use values passed in the data object or from the merged recipient profile for the property and values.

<Frame caption="Conditional Modal">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/block-basics-condition-modal.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=087a232a13dfc0246bf99e6307a472ec" alt="Conditional Modal" width="861" height="297" data-path="assets/platform/content/block-basics-condition-modal.png" />
</Frame>

You can use values passed in the data object or from the merged recipient profile for the property and values.
See [Content Block Conditions](/platform/content/template-settings/send-conditions#for-content-blocks) for more information.

### Customizing Block Settings

Each content block has block-specific settings. The available settings are block-dependent but include things like alignment, color, and text formatting.

<Frame caption="Block Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/block-basics-settings.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=e65c594516dbafc4b6e1d2a79c59751b" alt="Block Settings" width="690" height="232" data-path="assets/platform/content/block-basics-settings.png" />
</Frame>

### Removing a Block

Blocks can be removed from a channel by selecting the block and clicking the Remove Block button. This action will send it to the Block Library.

<Frame caption="Remove a Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/block-basics-delete.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=29b2a8f36757b99f7ca96f863e2f661a" alt="Remove a Block" width="683" height="201" data-path="assets/platform/content/block-basics-delete.png" />
</Frame>

## Block Types

<CardGroup cols={2}>
  <Card title="Text" href="/platform/content/content-blocks/text-blocks" icon="align-left">
    Rich text with inline conditions, variables, and formatting
  </Card>

  <Card title="Image" href="/platform/content/content-blocks/image-blocks" icon="image">
    Visual content with channel-specific rendering
  </Card>

  <Card title="Action" href="/platform/content/content-blocks/action-blocks" icon="hand-pointer">
    Buttons and links for interactive notifications
  </Card>

  <Card title="List" href="/platform/content/content-blocks/list-blocks" icon="list">
    Dynamic arrays rendered as styled lists
  </Card>

  <Card title="Markdown" href="/platform/content/content-blocks/md-blocks" icon="markdown">
    Formatted content using plain text syntax
  </Card>

  <Card title="Template" href="/platform/content/content-blocks/template-blocks" icon="code">
    Custom HTML, CSS, and Handlebars
  </Card>

  <Card title="Quote" href="/platform/content/content-blocks/quote-blocks" icon="quote-left">
    Highlighted text and citations
  </Card>

  <Card title="Divider" href="/platform/content/content-blocks/divider-blocks" icon="grip-lines">
    Visual separators between content sections
  </Card>
</CardGroup>
