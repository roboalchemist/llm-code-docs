# Source: https://www.courier.com/docs/platform/content/content-blocks/action-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Action

> Action Blocks let you add buttons or links to Courier notifications. Configure text, URL actions, alignment, and styling. Behavior and appearance vary by channel, with limited support in SMS/chat.

Action Blocks add interactive buttons or links to your notifications, letting recipients take action directly from the message. They render as buttons in email and as plain URLs in SMS and chat channels.

<Frame caption="New Action Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/action-block-new.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=243a2e4d05af1410a515b6a00fdfcbf6" alt="New Action Block" width="1300" height="614" data-path="assets/platform/content/action-block-new.png" />
</Frame>

## Configuring Action Blocks

When you select an action block, you are presented with a toolbar with the following formatting options depending on the notification channel.

<Frame caption="Action Block Options">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/action-block-options.gif?s=f8d1dd957a14e54ec38581c5c132d8f0" alt="New Action Block" width="914" height="490" data-path="assets/platform/content/action-block-options.gif" />
</Frame>

### Text and Link

* Click the Edit icon to set the `Friendly Text` and `Action`. For most channels, the action is a URL. For Slack, you can opt to use a webhook.

### Button Type

* Select between different button styles, as well as a text-only link option

<Info>
  Action buttons are not available across all channels. For SMS and chat, the button renders as a URL.
</Info>

### Alignment

* Align the content of the block left, center or right.

### Color (Action Buttons Only)

* Select the button color. You can use a color from the palette or enter the hex value for a custom color, or select from pre-defined brand template colors. This option is only available for action buttons.

<CardGroup cols={2}>
  <Card title="Content Block Basics" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Adding, reordering, and filtering blocks
  </Card>

  <Card title="Text Blocks" href="/platform/content/content-blocks/text-blocks" icon="align-left">
    Add hyperlinks inline within text content
  </Card>

  <Card title="Send Conditions" href="/platform/content/template-settings/send-conditions" icon="filter">
    Conditionally show or hide action blocks
  </Card>

  <Card title="Variables" href="/platform/content/variables/inserting-variables" icon="code">
    Use dynamic URLs and button text
  </Card>
</CardGroup>
