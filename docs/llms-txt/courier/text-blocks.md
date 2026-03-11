# Source: https://www.courier.com/docs/platform/content/design-studio/text-blocks.md

# Source: https://www.courier.com/docs/platform/content/content-blocks/text-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text

> Courier Text Blocks allow rich text formatting, variables, and conditional rendering across channels. Customize appearance, embed links and images, and adapt formatting automatically for email, SMS, and direct messages.

Text Blocks provide a versatile way to add and format text in your notifications.

<Frame caption="New Text Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-new.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=c19d39294fac13e6a5aec8197051e2df" alt="New Text Block" width="1300" height="614" data-path="assets/platform/content/text-block-new.png" />
</Frame>

### Text Block Options

* **Variables**: Customize text across all channels and integrations using variables.
* **Background Color**: Adjust the background color to enhance the text block's appearance.
* **Insert Bulleted List**: For static bulleted lists, use this option. For dynamic content, refer to list blocks.
* **Hyperlink**: Add hyperlinks to text in any channel to create interactive notifications.

<Frame caption="Create a New Variable">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-variable.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=ff9217de6db15e37adacdaddd8da8035" alt="Create a New Variable" width="1506" height="444" data-path="assets/platform/content/text-block-variable.png" />
</Frame>

## Show or Hide Text With Inline Conditions

Conditional text allows you to control the visibility of text within a Text Block across different channels. You can use filters to dynamically show or hide text based on data from the profile or data objects sent with the Send API.

<Frame caption="Conditionally Render Text">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-conditional.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=67c1493a27d4f239b10549219707bbcd" alt="Conditionally Render Text" width="739" height="223" data-path="assets/platform/content/text-block-conditional.png" />
</Frame>

<Frame caption="Choose Your Rendering Conditions">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-conditional-modal.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=78df7b35d694aebf141e679458b9d5ef" alt="Choose Your Rendering Conditions" width="861" height="297" data-path="assets/platform/content/text-block-conditional-modal.png" />
</Frame>

**Common Use Case**: Use inline conditions to provide fallback text when user-specific data is unavailable. For example, highlight the `profile.name` variable in your template and set a condition to hide it when the name property is empty. Then, add fallback text (e.g., "there") with a condition to display when `profile.name` is not present, resulting in a message like "Hi there," instead of "Hi `{profile.name}`,".

## Cross-Channel Formatting Behaviors

Courier automatically adjusts text formatting to suit the limitations of each channel and integration when using text blocks from the shared content library.

### Email

<Frame caption="Email Text Formatting">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-format.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=f731b5d4091d57d4491d993f7b108256" alt="Email Text Formatting" width="1136" height="330" data-path="assets/platform/content/text-block-format.png" />
</Frame>

* Text blocks in emails offer advanced formatting options, such as inline images, bulleted lists, headers (H1, H2), subtext, text color, and alignment. These features are not available in SMS, push notifications, or Slack.
* You can also embed images inline:

<Frame caption="Inline Image">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-image.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=384b7dc7d1ea1ea1748bc5b1ed92f671" alt="Inline Image" width="743" height="184" data-path="assets/platform/content/text-block-image.png" />
</Frame>

* Highlight important text:

<Frame caption="Highlight Text">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-highlight.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=736e849654d0f15755608782766adbbe" alt="Highlight Text" width="743" height="253" data-path="assets/platform/content/text-block-highlight.png" />
</Frame>

* Add static bulleted lists (use list blocks for dynamic content):

<Frame caption="Unordered List">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-bullet.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=83dc8921a71d0df2bde9c89fda04da9c" alt="Unordered List" width="1120" height="366" data-path="assets/platform/content/text-block-bullet.png" />
</Frame>

### Direct Message

* Formatting options such as bold and italic are available in certain direct message text blocks.

<Frame caption="Bold Formatting">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/text-block-bold.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=233719d08dbbd7e7ef1f167ee02376c3" alt="Bold Formatting" width="773" height="213" data-path="assets/platform/content/text-block-bold.png" />
</Frame>

### SMS

* SMS does not support text formatting. Bold, italic, headers, subtext, background colors, and alignment will revert to plain text.
* Hyperlinks formatted as anchor links will appear as URL hyperlinks in SMS.

## Conditional Rendering

Like with any content block, Text Blocks can be hidden using a [conditions filter](/platform/content/template-settings/send-conditions#for-content-blocks).

<CardGroup cols={2}>
  <Card title="Content Block Basics" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Adding, reordering, and filtering blocks
  </Card>

  <Card title="Action Blocks" href="/platform/content/content-blocks/action-blocks" icon="hand-pointer">
    Add buttons and links to your notifications
  </Card>

  <Card title="List Blocks" href="/platform/content/content-blocks/list-blocks" icon="list">
    Render dynamic arrays as styled lists
  </Card>

  <Card title="Variables" href="/platform/content/variables/inserting-variables" icon="code">
    Insert dynamic data into text content
  </Card>
</CardGroup>
