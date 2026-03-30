# Source: https://www.courier.com/docs/tutorials/content/how-to-design-your-first-notification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Design and Send Your First Notification

> Create a notification template in Courier's Template Designer, configure a provider, add content and variables, preview with test data, publish, and send a test notification.

Walk through the full lifecycle of a Courier notification: configure a provider, design a template with content blocks and variables, preview it with test data, publish, and send a test message. By the end, you'll have a working notification ready to integrate into your codebase.

## Prerequisites

* A [Courier account](https://app.courier.com/)
* Credentials for at least one provider (e.g. SendGrid API key, Twilio SID). Courier also provides a built-in test email provider you can use to get started without external credentials.

## Step 1: Configure a Provider

Before you can send anything, your Courier workspace needs at least one integrated provider. If you've already configured a provider, skip to Step 2.

<Steps>
  <Step title="Open the Integrations page">
    Navigate to the [Integrations tab](https://app.courier.com/integrations) in the left sidebar.
  </Step>

  <Step title="Choose a provider">
    Search for your provider (e.g. SendGrid, Twilio, Firebase) and click it. Fill in the required credentials from your provider's dashboard and click **Install**.

    <Frame caption="Configuring a provider in the Integrations tab">
      <img src="https://mintcdn.com/courier-4f1f25dc/CSwPAtKFYYOP9EdP/assets/tutorials/content/integration-selector.png?fit=max&auto=format&n=CSwPAtKFYYOP9EdP&q=85&s=29b319a8e2990f5ceab4b2161f58123e" width="1976" height="1260" data-path="assets/tutorials/content/integration-selector.png" />
    </Frame>
  </Step>

  <Step title="Verify installation">
    Your newly configured provider appears in the **Installed** section. You can now use it in any notification template.
  </Step>
</Steps>

<Tip>
  You can also configure providers inline while designing a template. If you add a channel that has no provider, Courier will prompt you to configure one in the channel settings.
</Tip>

## Step 2: Create a Notification Template

<Steps>
  <Step title="Create a new template">
    Navigate to [Templates](https://app.courier.com/assets/templates) and click **+ New** > **Message Template**. Give it a name (e.g. "Welcome Email"), then click **Create Template**.
  </Step>

  <Step title="Add a channel">
    Under **Add Notification Channels**, select **Email**. In the left sidebar under **Channels**, hover over **Email** and click the cog icon to open channel settings. Choose the provider you configured in Step 1.

    <Frame caption="Selecting an email provider for the channel">
      <img src="https://mintcdn.com/courier-4f1f25dc/fzDzb8rXw-5hGi1q/assets/tutorials/sending/select-integration.jpeg?fit=max&auto=format&n=fzDzb8rXw-5hGi1q&q=85&s=e49e180ca152d3cc63fcf9c959cfb996" width="3456" height="1804" data-path="assets/tutorials/sending/select-integration.jpeg" />
    </Frame>

    <Note>
      Providers you've already configured appear under "Configured" in the integrations list. You can add multiple providers per channel and set [priority rules](/platform/sending/channel-priority) to control failover.
    </Note>
  </Step>
</Steps>

## Step 3: Add Content

Click on the email channel to open the content editor. Use the content toolbar to build your notification with blocks.

<Steps>
  <Step title="Add a text block">
    Click the **T** icon in the toolbar to add a text block. Replace the placeholder text with your message, e.g. `Hello, {profile.name}!`

    <Frame caption="Adding a text block with a variable">
      <img src="https://mintcdn.com/courier-4f1f25dc/fzDzb8rXw-5hGi1q/assets/tutorials/sending/new-text-block.png?fit=max&auto=format&n=fzDzb8rXw-5hGi1q&q=85&s=646243eec484876d6bec8587b481e644" width="1492" height="600" data-path="assets/tutorials/sending/new-text-block.png" />
    </Frame>
  </Step>

  <Step title="Add an action block">
    Click the button icon to add an action block. This renders as a clickable button (CTA) in email. You can set the button text and URL; use a variable like `{invite_url}` for dynamic links.

    <Frame caption="Text and action blocks in the editor">
      <img src="https://mintcdn.com/courier-4f1f25dc/fzDzb8rXw-5hGi1q/assets/tutorials/sending/text-and-action-result.png?fit=max&auto=format&n=fzDzb8rXw-5hGi1q&q=85&s=a45906a81d652e59942d36eaabd53477" width="1514" height="760" data-path="assets/tutorials/sending/text-and-action-result.png" />
    </Frame>
  </Step>

  <Step title="Add more blocks as needed">
    Add images, dividers, markdown, or template blocks. Courier auto-saves and adapts your blocks for all channels. See [Content Blocks](/platform/content/content-blocks/content-block-basics) for the full list.
  </Step>
</Steps>

### Variables for Dynamic Data

Use curly-brace placeholders to insert dynamic data from the send request:

* **`{profile.name}`** - Recipient's name from their Courier profile
* **`{data.invite_url}`** or **`{invite_url}`** - Custom data passed in the send request
* **`{urls.preferences}`** - Link to the user's preference page
* **`{urls.unsubscribe}`** - One-click unsubscribe link

See [Variables](/platform/content/variables/inserting-variables) for the full syntax and available built-in variables.

### Multi-Channel Content

Once you've built content in one channel, open another channel and pull in the same blocks from the content library. Courier dynamically adjusts blocks to match each channel's format (e.g. stripping images for SMS).

## Step 4: Preview with Test Data

<Steps>
  <Step title="Open the Preview tab">
    Click **Preview** at the top of the editor, then click **Create Test Event**.
  </Step>

  <Step title="Add test data">
    Replace the `data` and `profile` objects with values that match your variables:

    ```json  theme={null}
    {
      "data": {
        "invite_url": "https://www.example.com"
      },
      "profile": {
        "email": "you@example.com",
        "name": "Test User"
      }
    }
    ```
  </Step>

  <Step title="Verify the preview">
    Your variables should render with the test data. If any show as raw `{variable}` text, check that the key names match between your template and test event JSON.

    <Frame caption="Preview with test data rendered">
      <img src="https://mintcdn.com/courier-4f1f25dc/dpfmS7sFlMZo7Z91/assets/tutorials/content/preview-email.png?fit=max&auto=format&n=dpfmS7sFlMZo7Z91&q=85&s=fdac683e4c6c720af52447ff419e3d8f" width="3456" height="1804" data-path="assets/tutorials/content/preview-email.png" />
    </Frame>
  </Step>
</Steps>

For more on test events (including creating them from message logs), see [How to Use Test Events](/tutorials/content/how-to-preview-notification).

## Step 5: Configure Branding (Optional)

[Brands](/platform/content/brands/brands-overview) let you apply consistent logos, colors, headers, and footers across notifications. If no brand is configured, Courier uses simple default styling.

To apply a brand, open **Template Settings** and select a brand from the dropdown. See [How to Create and Use Brands](/tutorials/content/how-to-create-and-use-brands) for a full walkthrough.

## Step 6: Publish

Click **Publish Changes** to save your notification template. Unpublished changes are only visible in draft mode; your live notifications won't update until you publish.

<Tip>
  You can roll back to any previously published version in **Template Settings > Publish History**.
</Tip>

## Step 7: Send a Test Notification

<Steps>
  <Step title="Open the Send tab">
    Click the **Send** tab at the top of the editor.

    <Frame caption="The Send tab in the Template Designer">
      <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/send-notification-tab.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=804509fb636ead6f591de925d00eaff5" width="1662" height="212" data-path="assets/platform/content/send-notification-tab.png" />
    </Frame>
  </Step>

  <Step title="Configure the code snippet">
    Select your programming language, confirm the notification event, and set the recipient ID. Courier generates a ready-to-use code snippet.

    <Frame caption="Generated code snippet for your stack">
      <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/send-notification-code.jpeg?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=c97e610149ba8201ffb834525c3a9e65" width="2868" height="1538" data-path="assets/platform/content/send-notification-code.jpeg" />
    </Frame>
  </Step>

  <Step title="Send a test">
    Select a test event (from Step 4), optionally choose a brand, and click **Send Notification**. Check the [Message Logs](/platform/analytics/message-logs) to verify delivery.
  </Step>

  <Step title="Integrate into your codebase">
    Copy the code snippet and integrate it into your application. You can also use the [Send API](/api-reference/send/send-a-message) directly or any of the [Courier SDKs](https://github.com/trycourier).
  </Step>
</Steps>

## What's Next

<CardGroup cols={2}>
  <Card title="Content Blocks" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Explore all available block types for building notification content
  </Card>

  <Card title="Multi-Channel Routing" href="/tutorials/sending/how-to-configure-multi-channel-routing" icon="list-tree">
    Configure channel priority and failover rules
  </Card>

  <Card title="Brands" href="/tutorials/content/how-to-create-and-use-brands" icon="copyright">
    Apply consistent branding to your notifications
  </Card>

  <Card title="Send API Reference" href="/api-reference/send/send-a-message" icon="code">
    Full API reference for sending notifications
  </Card>
</CardGroup>
