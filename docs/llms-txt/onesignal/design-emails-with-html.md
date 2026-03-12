# Source: https://documentation.onesignal.com/docs/en/design-emails-with-html.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Design emails with HTML

> Create custom HTML emails in OneSignal using the HTML Editor. Learn supported HTML rules, unsubscribe handling, image requirements, dark mode behavior, and email client limitations.

## Overview

The HTML Editor lets you send fully custom, branded emails using your own HTML.

You should use the HTML Editor when you:

* Need complete control over layout, spacing, and styling
* Already have production-ready HTML email templates
* Are comfortable working within email client limitations

<Info>
  HTML emails are not the same as web pages. Many HTML and CSS features are unsupported or inconsistently rendered across email clients.
</Info>

### Prerequisites

Before using the HTML Editor, make sure you:

* Have experience building responsive HTML emails
* Host all images on publicly accessible URLs (your site, CDN, S3, etc.)

#### Expected outcome

After setup, your email:

* Renders consistently across major clients (Gmail, Outlook, Apple Mail)
* Tracks link clicks correctly
* Includes a working unsubscribe mechanism
* Passes spam and deliverability checks

### Import your own templates

If you already have HTML email templates, you can add them to OneSignal in any of the following ways:

1. Use [Email Template forwarding](./email-template-forwarding)
2. Create templates programmatically using the [Create Template API](/reference/create-template)
3. Copy-paste your HTML into the HTML Editor

<Info> We recommend starting with a proven template rather than writing HTML from scratch. </Info>

***

## Use the HTML Editor

When creating an email message, select **HTML Editor** as the editor type.

1. Paste or write your HTML in the editor.
2. Use **Send Test Email** to preview rendering across clients and devices.
3. Fix layout issues before scheduling or sending.

<Frame caption="HTML editor with code input and live preview">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/966f520-html-editor-preheader.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=ceece56a7c1c52b3a51badea42685768" alt="HTML editor with code input and live preview" width="1300" height="1238" data-path="images/docs/966f520-html-editor-preheader.png" />
</Frame>

### Links & tracking

Link tracking is enabled by default for HTML emails.

* Multi-link tracking is supported
* Clicks appear in message reports

See:

* [Links](./links#email)
* [Deep Linking](./deep-linking)

#### Unsubscribe links

All marketing emails should include an unsubscribe link.

Emails without a valid unsubscribe option are more likely to:

* Be marked as spam
* Hurt sender reputation
* Be blocked by inbox providers

<Tabs>
  <Tab title="OneSignal's default unsubscribe link">
    Include the following placeholder anywhere in your HTML (usually in the footer):

    ```html HTML theme={null}
    <a href="[unsubscribe_url]">Unsubscribe</a>
    ```

    When clicked, this link unsubscribes the user's email [Subscription](./subscriptions) in OneSignal.
  </Tab>

  <Tab title="Use a custom unsubscribe page (optional)">
    You can link to your own unsubscribe page, but you must:

    * Capture the unsubscribe action
    * Update the user’s email Subscription status

    See [Create a custom unsubscribe page](./create-custom-unsubscribe-page) for more details.

    <Warning> If you use a custom unsubscribe URL and do not update the Subscription, users will continue receiving emails. </Warning>
  </Tab>
</Tabs>

***

## HTML email best practices

### Always use inline CSS

Most email clients strip `<style>` blocks and external stylesheets.

Try this tool: [Responsive Email CSS Inliner](https://htmlemail.io/inline/)

### Dark mode styling

Many email clients apply automatic color inversion when a user has dark mode enabled. This behavior can cause unpredictable results, such as buttons appearing with a black background and black text. To ensure consistent rendering, we recommend explicitly defining how your email should look in both light and dark modes.

Best practices:

* **Define base styles inline.** Always set background and text colors directly on elements instead of relying on defaults or transparency.
* **Use media queries for dark mode.** Clients like Apple Mail and Outlook on iOS support `@media (prefers-color-scheme: dark)` where you can override styles for dark mode.
* **Apply `!important` sparingly.** Adding `!important` to dark mode overrides helps prevent inboxes from stacking inversion rules on top of your custom styles.
* **Signal theme support.** Include the following meta tags in your HTML head to reduce auto-inversion:

```html  theme={null}
  <meta name="color-scheme" content="light dark">
  <meta name="supported-color-schemes" content="light dark">
```

<Note>
  Test across clients. Gmail (iOS, Android, web), Outlook, and Apple Mail all behave differently. Testing helps catch issues early.
</Note>

### Recommended image sizes for email

**Aspect Ratios:**

* Header/Banner images: `3:1` or `4:1` (e.g., `600×200` or `600×150`)
* Hero images: `16:9` or `2:1` (e.g., `600×338` or `600×300`)
* Square images: `1:1` (e.g., `300×300`) — good for product grids
* Thumbnails: `1:1` or `4:3`
* Max width: `600–700px` is standard (most email clients)
* Design at `2x` for retina displays (e.g., `1200px` wide, displayed at `600px`)

**File Size:**

* Keep individual images under `100–200KB`
* Total email size (including images) under `1MB`
* Smaller = faster load times and better deliverability

**File Formats:**

* JPG: Best for photos
* PNG: Best for graphics, logos, transparency
* GIF: For simple animations (keep file size small)
* WebP: Not widely supported in email yet — avoid

**Other Tips:**

* Always include alt text for accessibility and when images don't load
* Use inline CSS for styling (many clients strip `<style>` tags)
* Avoid background images (inconsistent support)
* Test across clients (Gmail, Outlook, Apple Mail all render differently)
  * Outlook often ignores image dimensions, so set both width and height attributes in HTML

### Add alt tags to images

Alt text improves accessibility and ensures information is conveyed even if images are blocked or fail to load.

| Email Client | Blocks Images? | Shows Alt Text | Styles Alt Text |
| ------------ | -------------- | -------------- | --------------- |
| AOL          | Yes            | Yes            | Yes             |
| Gmail        | Yes            | Yes            | Yes             |
| Yahoo        | Yes            | Yes            | Yes             |
| Outlook      | Sometimes      | Yes            | Yes             |

Source: [Litmus Email Client Support](https://litmus.com/community/learning/12-alt-text-in-html-email)

### Name and format your HTML

Use semantic HTML and meaningful tag naming for accessibility. This helps screen readers interpret your content more accurately.

Also, use standard color formats and proper indentation for maintainability.

### Check for broken links

Broken links reduce deliverability and can flag your emails as spam. Test all links thoroughly before sending.

### Use supported HTML only

Email clients **do not** support:

* JavaScript
* `<iframe>`
* HTML forms
* Embedded audio or video
* Flash
* CSS positioning or layering tricks

Use links to external pages instead.

### Validate before sending

Before sending, validate your email by:

* Testing all links
* Verifying unsubscribe behavior
* Sending test emails to Gmail, Outlook, and Apple Mail
* Checking dark mode rendering

<Check> If your email renders correctly in major clients and unsubscribe works, it is ready to send. </Check>

***

## FAQ

### Can I reuse my existing email templates?

See above [Import your own templates](#import-your-own-templates) for details.

### Can I use custom fonts?

## Yes, but support varies. Unsupported fonts fall back to system defaults, especially in Outlook

Built with [Mintlify](https://mintlify.com).
