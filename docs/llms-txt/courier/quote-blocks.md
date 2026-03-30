# Source: https://www.courier.com/docs/platform/content/content-blocks/quote-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quote

> Quote Blocks in Courier emphasize key text with distinct formatting per channel—indentation for email and Slack, quotes for SMS. Ideal for highlighting citations or testimonials. Supports conditional visibility.

Quote Blocks highlight important text or citations in your notifications. They're useful for emphasizing key points, displaying testimonials, or citing sources.

## Working with Quote Blocks

### Adding a Quote Block

1. In the Courier designer, click the "+" icon to add a new block
2. Select "Quote" from the block options
3. Enter the text you want to appear in the quote

### Cross-Channel Behaviors

Quote Blocks adapt their appearance based on the delivery channel:

#### Email

Creates an indented quote block with distinctive styling.

<Frame caption="Quote Block Appearance in Email">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/quote-block-email.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=c0f573abf164a9e17469ff492b4aa4c5" alt="Quote Block appearance in email" width="970" height="180" data-path="assets/platform/content/quote-block-email.png" />
</Frame>

#### Slack

Text is indented and italicized to match Slack's quote formatting.

<Frame caption="Quote Block Appearance in Slack">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/quote-block-slack.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=f407b8b95d7e1e73f1459486e9a17e82" alt="Quote Block appearance in Slack" width="970" height="180" data-path="assets/platform/content/quote-block-slack.png" />
</Frame>

#### SMS / Direct Message

Automatically wraps the text in quotation marks.

<Frame caption="Quote Block Appearance in SMS/DM">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/quote-block-sms.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=cc4687ffaac0096373dab6303f9d1435" alt="Quote Block appearance in SMS/DM" width="542" height="222" data-path="assets/platform/content/quote-block-sms.png" />
</Frame>

## Conditional Rendering

Like with any content block, Quote Blocks can be hidden using a [conditions filter](/platform/content/template-settings/send-conditions#for-content-blocks).

<CardGroup cols={2}>
  <Card title="Content Block Basics" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Adding, reordering, and filtering blocks
  </Card>

  <Card title="Text Blocks" href="/platform/content/content-blocks/text-blocks" icon="align-left">
    Rich text with inline conditions and formatting
  </Card>
</CardGroup>
