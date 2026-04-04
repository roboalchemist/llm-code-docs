# Source: https://www.courier.com/docs/platform/content/design-studio/image-blocks.md

# Source: https://www.courier.com/docs/platform/content/content-blocks/image-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image

> Courier Image Blocks let you add visuals to notifications across email, SMS, push, and direct message channels. They support conditional display, channel-specific behavior, and best practices like alt text.

# Image Blocks

Image Blocks allow you to enhance your notifications with visual content across various channels.
Image Blocks can improve the engagement and effectiveness of your notifications by providing visual context or appeal.

<Frame caption="New Image Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/image-block-new.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=fcc1ba3dcf97048ee730fc627941a438" alt="New Image Block" width="1300" height="614" data-path="assets/platform/content/image-block-new.png" />
</Frame>

## Channel-Specific Behaviors

### Email

In email notifications, Image Blocks display as embedded images, allowing for rich visual content.

### SMS, Push

For SMS and push notifications:

* Image Blocks appear as URLs
* The rendering of these URLs depends on the integrated channel provider

### Direct Message

For supported direct message integrations:

* Images are displayed in real-time within the Courier editor
* No preview links are shown

<Frame caption="Image Block Rendering">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/image-block-fb.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=8a735018c58b6978fb90bb8fe8605c32" alt="Image Block Rendering" width="1057" height="667" data-path="assets/platform/content/image-block-fb.png" />
</Frame>

## Advanced Usage

### Conditional Display

Like other content blocks, you can dynamically show or hide Image Blocks using [conditional filters](/platform/content/template-settings/send-conditions#for-content-blocks).

<Frame caption="Setting up an Image Block Filter">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/image-block-filter.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=4cbafecffe71733c037289995070103d" alt="Setting up an Image Block filter" width="773" height="369" data-path="assets/platform/content/image-block-filter.png" />
</Frame>

<Frame caption="Configuring Image Block Conditions">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/image-block-condition.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=34dac9da5e98c3368366db75601587cb" alt="Configuring Image Block conditions" width="836" height="341" data-path="assets/platform/content/image-block-condition.png" />
</Frame>

## Best Practices

1. **Optimize for mobile**: Ensure images are responsive and look good on various device sizes
2. **File size**: Keep image file sizes small to improve loading times, especially for email
3. **Relevance**: Use images that are relevant to your message content
4. **Accessibility**: Always include descriptive alt text for screen readers
5. **Fallback**: Provide text alternatives for channels that may not support images

<CardGroup cols={2}>
  <Card title="Content Block Basics" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Adding, reordering, and filtering blocks
  </Card>

  <Card title="Text Blocks" href="/platform/content/content-blocks/text-blocks" icon="align-left">
    Add formatted text with inline images
  </Card>

  <Card title="Action Blocks" href="/platform/content/content-blocks/action-blocks" icon="hand-pointer">
    Add buttons and links alongside images
  </Card>

  <Card title="Send Conditions" href="/platform/content/template-settings/send-conditions" icon="filter">
    Conditionally show or hide image blocks
  </Card>
</CardGroup>
