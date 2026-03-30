# Source: https://documentation.onesignal.com/docs/en/design-emails-with-drag-and-drop.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Design emails with drag-and-drop

> Create responsive emails using OneSignal’s Drag and Drop Email Builder. Learn the recommended build flow, global settings, rows, content blocks, personalization, unsubscribe handling, and common design guardrails.

## Overview

The OneSignal Drag and Drop Email Builder lets you visually design responsive emails exactly as they will appear in your users’ inboxes—without writing full HTML.

You build emails using three core components:

* **Settings** – global styles and layout applied across the entire email
* **Rows** – horizontal layout containers that control structure and responsiveness
* **Content** – individual blocks such as text, images, buttons, and HTML

This guide walks you through each component and shows the recommended way to build an email from start to finish.

<Note>
  Use the Drag and Drop Email Builder if you want to:

* Design emails visually without managing full HTML (HTML blocks are available)
* Reuse rows or templates across campaigns
* Allow non-technical teammates to safely edit content

  If you need full HTML control, custom fonts everywhere, or advanced dark mode logic, use the [HTML Editor](./design-emails-with-html) instead.
</Note>

### Recommended build flow (default)

Follow this order for the best results and fewer rendering issues:

1. Configure global styles in **Settings**
2. Add layout structure using **Rows**
3. Insert **Content** blocks
4. Add personalization and links
5. Add an unsubscribe link (for marketing emails)
6. Save as a template or send

<Check>
  When finished, your email should:

* Be no wider than 600px
* Render cleanly on mobile and desktop
* Include required compliance links
</Check>

### Import your own templates

If you already have HTML email templates, you can add them to OneSignal using:

1. [Email Template forwarding](./email-template-forwarding)
2. [Create Template API](/reference/create-template)
3. Copy-paste HTML into the [HTML Editor](./design-emails-with-html)

***

## Settings

Settings define the foundational layout and styles for your email. These values cascade down to rows and content blocks unless explicitly overridden.

<Frame caption="Image shows settings for the builder">
  <img src="https://mintcdn.com/onesignal/RBBmVfkQbMT-0tMb/images/email/email-drag-and-drop-settings.png?fit=max&auto=format&n=RBBmVfkQbMT-0tMb&q=85&s=0a857f7754c6b1031926f2e62b6dde15" alt="Settings for the builder" width="2418" height="1652" data-path="images/email/email-drag-and-drop-settings.png" />
</Frame>

| Design Setting                | Description                                                            |
| ----------------------------- | ---------------------------------------------------------------------- |
| Content area width            | Width of the email in pixels. **Recommended:** `600px`.                |
| Content area alignment        | Align content left or center.                                          |
| Background color              | Color behind the content area.                                         |
| Content area background color | Color inside the content area.                                         |
| Default font                  | Applied to all text unless overridden. Custom fonts require HTML.      |
| Link color                    | Default color for all links.                                           |
| Language                      | Sets the HTML `lang` attribute for accessibility. Defaults to English. |

<Note>
  **Recommended default:** Configure as much styling as possible in Settings to ensure consistency and reduce per-block overrides.
</Note>

***

## Rows

Rows define the horizontal layout of your email. Each row can contain one or more columns, and each column can contain content blocks.

Drag and drop rows into the editor to build your structure.

<Frame caption="Adding rows to structure an email">
  <img src="https://mintcdn.com/onesignal/RBBmVfkQbMT-0tMb/images/email/email-drag-and-drop-rows.png?fit=max&auto=format&n=RBBmVfkQbMT-0tMb&q=85&s=77120964b859903fc5b9b14ae94f1c44" alt="Adding rows to structure an email" width="2418" height="1652" data-path="images/email/email-drag-and-drop-rows.png" />
</Frame>

<Note>
  Use rows to control layout and spacing. Avoid relying on individual content blocks for major layout decisions.
</Note>

### Delete & duplicate rows

Select the row and use the **delete** and **duplicate** icons.

<Frame caption="Delete and duplicate row controls">
  <img src="https://mintcdn.com/onesignal/RBBmVfkQbMT-0tMb/images/email/email-drag-and-drop-rows-delete-duplicate.png?fit=max&auto=format&n=RBBmVfkQbMT-0tMb&q=85&s=af3c1203c0a94d232214128dba4fef6e" alt="Delete and duplicate row controls" width="2418" height="508" data-path="images/email/email-drag-and-drop-rows-delete-duplicate.png" />
</Frame>

### Saved rows

Saved rows let you reuse headers, footers, or repeated sections across emails and templates.

Click the **save icon** on a row to save it.

<Frame caption="Saving a row for reuse">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f4244e8-save-row.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=d08bbd071e599b38cceb57a093db8837" alt="Saving a row for reuse" width="1056" height="650" data-path="images/docs/f4244e8-save-row.png" />
</Frame>

Access saved rows from **Rows > Saved rows**.

<Frame caption="Selecting a saved row">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/cc85e4fe9192d6917cf8b6e7be2ee3c13473d77cc7719d4bc4e14c26f40e00f8-image.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=534a234a40e10750ae07706628f9fecd" alt="Selecting a saved row" width="419" height="705" data-path="images/docs/cc85e4fe9192d6917cf8b6e7be2ee3c13473d77cc7719d4bc4e14c26f40e00f8-image.png" />
</Frame>

Saved row categories:

* **Empty** – blank row templates
* **My Saved Rows** – rows created by you or your team
* **Sample Rows** – OneSignal examples

### Row properties

Click the outer edge of a row to edit row-level settings.

<Note> If you see **Content** instead of **Row** when hovering, you’ve selected a content block. Click the outer container edge until the label reads **Row**. </Note>

| Row Property | Description                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------- |
| Backgrounds  | Color or image behind the row. **Recommended:** set background color in Settings for consistency. |
| Borders      | Border color, width, and style.                                                                   |
| Layout       | Show or hide rows on mobile or desktop.                                                           |
| Columns      | Add, remove, or resize columns and adjust column padding.                                         |

<Warning> Avoid background images in rows. Email client support is inconsistent. If the row contains only an image, use an **Image block** instead. </Warning>

***

## Content

Content blocks are the actual elements your users see—text, images, buttons, dividers, and HTML.

Drag a content block into a row column. It automatically adapts to the column width.

<Frame caption="Available content blocks">
  <img src="https://mintcdn.com/onesignal/RBBmVfkQbMT-0tMb/images/email/email-drag-and-drop-content.png?fit=max&auto=format&n=RBBmVfkQbMT-0tMb&q=85&s=c4a31c6aa103e112e90519cf6cc0956a" alt="Available content blocks" width="2418" height="1660" data-path="images/email/email-drag-and-drop-content.png" />
</Frame>

<Info>
  **Decision rules for content blocks:**

* Use **Text blocks** for most copy.
* Use **Image blocks** for visuals or custom typography.
* Use **HTML blocks** only when you need advanced styling or behavior.
</Info>

### Custom fonts

The Drag and Drop Editor supports system fonts by default. To use custom fonts, you must use an HTML block.

```html HTML block theme={null}
<!-- Place this into a HTML block at the top of your email -->
<style type="text/css">
  /* Declare Bebas Neue (only loads in clients that support web fonts) */
  @font-face {
    font-family: 'Bebas Neue';
    font-style: normal;
    font-weight: 400;
    src: url('https://fonts.gstatic.com/s/bebasneue/v9/JTUSjIg69CK48gW7PXoo9Wlhzg.ttf') format('truetype');
  }
</style>

<h1 style="font-family:'Bebas Neue', Arial, Helvetica, sans-serif; 
           font-size:36px; line-height:1.2; margin:0; text-transform:uppercase;">
  Welcome!
</h1>
<p style="font-family:Arial, Helvetica, sans-serif; font-size:16px; margin:12px 0 0;">
  Thanks for subscribing.
</p>
```

<Info>
  **Recommended default:** Use system fonts for body text and custom fonts for headlines only.
</Info>

<Warning>
  Many email clients (including Gmail and Outlook for Windows) do not load web fonts. Always include fallback fonts or use images for guaranteed typography.

  To "force" a specific font, consider using images with the desired font instead.
</Warning>

### Images & video

You can upload images to the OneSignal dashboard and have them be accessible to your team. Change and apply effects to images like cropping, filtering, and more directly in the editor. You can also use URLs to images and videos. Make sure they are available via the provided URL.

#### Recommended image sizes for email

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

### Links

Link tracking is enabled by default. Multi-link tracking is available. See [Links](./links#email) and [Deep Linking](./deep-linking) for more details.

#### Unsubscribe links

All marketing emails should contain an unsubscribe link. Without an unsubscribe link, your emails will have a higher chance of being marked as spam. See [Unsubscribe links](./unsubscribe-links-email-subscriptions) for more details.

OneSignal provides a default unsubscribe link that when used, will unsubscribe the user's email [Subscription](./subscriptions). You can also include your own custom unsubscribe URL if desired. Just make sure you correctly manage the email Subscription (details in [Create a custom unsubscribe page](./create-custom-unsubscribe-page)).

Add OneSignal's default `[unsubscribe_url]` into your emails via:

* HTML Block: `<a href="[unsubscribe_url]">Unsubscribe</a>`
* Select your text and use the **Special links** option in the editor or set `[unsubscribe_url]` in the URL field

<Frame caption="Adding the unsubscribe link to your email">
  <img src="https://mintcdn.com/onesignal/RBBmVfkQbMT-0tMb/images/email/email-drag-and-drop-unsubscribe-link.png?fit=max&auto=format&n=RBBmVfkQbMT-0tMb&q=85&s=42c785978dc3142feba1b8de65cc9e62" width="1320" height="936" data-path="images/email/email-drag-and-drop-unsubscribe-link.png" />
</Frame>

### HTML blocks

HTML blocks allow custom markup and styling.

* JavaScript is not supported
* Inline CSS is recommended
* Some clients strip classes and IDs

<Info> HTML blocks are the best place for advanced styling such as dark mode overrides. See [Dark mode styling best practices](./design-emails-with-html#dark-mode-styling). </Info>

### Personalization

Use liquid templating to personalize messages. Example: `{{ first_name | default: "there" }}`

<Frame caption="Using Liquid templating to personalize messages">
  <img src="https://mintcdn.com/onesignal/RBBmVfkQbMT-0tMb/images/email/email-drag-and-drop-personalization.png?fit=max&auto=format&n=RBBmVfkQbMT-0tMb&q=85&s=1bf7e704ceb2cdf940ffdfe3939dac44" alt="Using Liquid templating to personalize messages" width="1232" height="670" data-path="images/email/email-drag-and-drop-personalization.png" />
</Frame>

<Note>
  See [Message personalization](./message-personalization) and [Using Liquid syntax](./using-liquid-syntax) for more details.
</Note>

### Emojis

Emojis may render differently across email platforms.

***

## Save your work

You can save your email design as a [**template**](./templates) for future use.

<Frame caption="Save email as a template">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b827bbc-Email-Save_As_Template.jpg?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=042193dfb7e8d814f99deb2b12bb26fa" alt="Save email as a template" width="2250" height="1176" data-path="images/docs/b827bbc-Email-Save_As_Template.jpg" />
</Frame>

***

## FAQ

### How do I handle dark mode?

Most emails render acceptably in dark mode, but always test. For advanced dark mode styling, use HTML blockes and see [Dark mode styling best practices](./design-emails-with-html#dark-mode-styling).

### How do I add a custom unsubscribe link?

See [Create a custom unsubscribe page](./create-custom-unsubscribe-page) for details.

## Related articles

* [Email overview](./email-messaging)
* [Email templates](./templates)
* [Unsubscribe links](./unsubscribe-links-email-subscriptions)
* [Dynamic content](./dynamic-content)
* [AB testing](./ab-testing)
* [Message personalization](./message-personalization)
* [Using Liquid syntax](./using-liquid-syntax)

***

Built with [Mintlify](https://mintlify.com).
