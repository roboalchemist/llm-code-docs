# Source: https://www.courier.com/docs/platform/content/elemental/elements/image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image

> Embed images in your Elemental notifications with support for alignment, sizing, links, and alt text. Images work across all channels with channel-specific rendering.

## Overview

The image element allows you to embed images into your notifications. Images can be aligned, sized, linked, and include alt text for accessibility.

**When to use:**

* Display logos, product images, or illustrations
* Add visual elements to enhance notifications
* Create clickable image banners
* Include user avatars or profile pictures

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "image",
    "src": "https://example.com/logo.png"
  }
  ```

  ```javascript Node.js icon="node-js" lines theme={null}
  const { CourierClient } = require("@trycourier/courier");

  const courier = new CourierClient({
    authorizationToken: process.env.COURIER_AUTH_TOKEN,
  });

  await courier.send({
    message: {
      to: { email: "user@example.com" },
      content: {
        version: "2022-01-01",
        elements: [
          {
            type: "image",
            src: "https://example.com/logo.png",
            alt_text: "Company Logo",
          },
        ],
      },
    },
  });
  ```

  ```python Python icon="python" lines theme={null}
  import os
  from trycourier import Courier

  client = Courier(auth_token=os.environ["COURIER_AUTH_TOKEN"])

  client.send_message(
      message={
          "to": {"email": "user@example.com"},
          "content": {
              "version": "2022-01-01",
              "elements": [
                  {
                      "type": "image",
                      "src": "https://example.com/logo.png",
                      "alt_text": "Company Logo",
                  }
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For image elements, this value must be `"image"`.
</ParamField>

<ParamField path="src" type="string" required>
  The source URL of the image. Must be a publicly accessible URL.
</ParamField>

<ParamField path="alt_text" type="string">
  Alternate text for the image. Used by screen readers and displayed when the image cannot be loaded. Important for accessibility.
</ParamField>

<ParamField path="href" type="string">
  A URL to link to when the image is clicked. Makes the image clickable.
</ParamField>

<ParamField path="width" type="string">
  CSS width properties to apply to the image. Can be:

  * Fixed: `"200px"`, `"300px"`
  * Percentage: `"50%"`, `"100%"`
  * Auto: `"auto"`
</ParamField>

<ParamField path="align" type="string">
  The alignment of the image. One of `"center"`, `"left"`, `"right"`, or `"full"`. Defaults to `"center"`.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization. Can localize `src` (image URL) and `href` (link URL). See the [Locales documentation](/platform/content/elemental/locales) for more details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The image will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Examples & Variants

### Basic Image

Simple image with alt text:

```json  theme={null}
{
  "type": "image",
  "src": "https://example.com/logo.png",
  "alt_text": "Company Logo"
}
```

### Clickable Image

Image that links to a URL:

```json  theme={null}
{
  "type": "image",
  "src": "https://example.com/banner.jpg",
  "alt_text": "Special Offer",
  "href": "https://example.com/sale",
  "width": "100%"
}
```

### Sized and Aligned Image

Control image size and alignment:

```json  theme={null}
{
  "type": "image",
  "src": "https://example.com/product.png",
  "alt_text": "Product Image",
  "width": "200px",
  "align": "center"
}
```

### Localized Image

Use different images for different locales:

```json  theme={null}
{
  "type": "image",
  "src": "https://example.com/welcome-en.png",
  "alt_text": "Welcome",
  "href": "https://example.com/dashboard",
  "locales": {
    "es": {
      "src": "https://example.com/welcome-es.png",
      "href": "https://example.com/es/dashboard"
    },
    "fr": {
      "src": "https://example.com/welcome-fr.png",
      "href": "https://example.com/fr/dashboard"
    }
  }
}
```

### Channel-Specific Image

Show different images per channel:

```json  theme={null}
{
  "type": "image",
  "channels": ["email"],
  "src": "https://example.com/email-banner.jpg",
  "alt_text": "Email Banner",
  "width": "100%"
},
{
  "type": "image",
  "channels": ["push"],
  "src": "https://example.com/push-icon.png",
  "alt_text": "Notification Icon"
}
```

### Full-Width Banner

Full-width banner image:

```json  theme={null}
{
  "type": "image",
  "src": "https://example.com/banner.jpg",
  "alt_text": "Promotional Banner",
  "href": "https://example.com/promo",
  "width": "100%",
  "align": "full"
}
```

## Best Practices

* **Always include alt text**: Essential for accessibility and when images fail to load
* **Use appropriate sizes**: Optimize images for email (typically max 600px width)
* **Use HTTPS URLs**: Ensure image URLs use HTTPS for security
* **Consider channel differences**: Images may render differently in email vs push notifications
* **Optimize file sizes**: Large images can slow down email loading
* **Test image loading**: Verify images are publicly accessible and load correctly

## Channel Support

* **Email**: ✅ Full support with alignment, sizing, and linking
* **Push**: ✅ Supported (typically as notification icon or banner)
* **SMS**: ❌ Not supported (text-only channel)
* **Inbox**: ✅ Full support

## Related Elements

* [Action Element](/platform/content/elemental/elements/action) - For clickable buttons and links
* [Text Element](/platform/content/elemental/elements/text) - For text content alongside images
* [Columns Element](/platform/content/elemental/elements/columns) - For layouts with images and text side-by-side
* [Locales](/platform/content/elemental/locales) - For localizing image URLs and links
