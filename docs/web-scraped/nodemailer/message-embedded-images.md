# Source: https://nodemailer.com/message/embedded-images

Title: Embedded images | Nodemailer

URL Source: https://nodemailer.com/message/embedded-images

Published Time: Sat, 07 Feb 2026 09:05:49 GMT

Markdown Content:
Embedded images are images that display directly in the email body rather than appearing as downloadable attachments. You can embed images in your HTML emails by including them in the [attachments](https://nodemailer.com/message/attachments) array and referencing them using the `cid:` (Content-ID) URL scheme.

Here is how to embed an image in three steps:

1. Add the image to the [attachments](https://nodemailer.com/message/attachments) array in your message options.
2. Assign a unique [`cid`](https://nodemailer.com/message/attachments) (Content-ID) value to the attachment.
3. Reference the image in your HTML using `src="cid:your-cid-value"`.

Why use embedded images?

Many email clients block external images by default for privacy and security reasons. Embedded images bypass this restriction because the image data travels inside the message itself, so the recipient sees the image immediately without needing to click "load images."

Choosing a unique cid

The **cid** value must be unique within the message. A recommended pattern is to use an email-like format with a domain you control, such as `logo@example.com` or `header-image@mycompany.com`. This format helps ensure uniqueness and follows email standards.

#### Basic example[​](https://nodemailer.com/message/embedded-images#basic-example "Direct link to Basic example")

This example shows how to embed a single image from a file path. The `cid` value in the attachment must match the value used in the HTML `src` attribute (without the `cid:` prefix).

`const message = {  from: "Alice <alice@example.com>",  to: "Bob <bob@example.com>",  subject: "Inline image test",  html: 'Embedded image: <img src="cid:logo@example.com" alt="Company logo"/>',  attachments: [    {      filename: "logo.png",      path: "/path/to/logo.png",      cid: "logo@example.com", // matches the cid in the img src attribute    },  ],};`

#### Using a Buffer instead of a file[​](https://nodemailer.com/message/embedded-images#using-a-buffer-instead-of-a-file "Direct link to Using a Buffer instead of a file")

Instead of specifying a file path, you can provide the image data directly as a Buffer. This is useful when the image is generated dynamically or already loaded in memory.

`const fs = require("fs");const message = {  from: "Alice <alice@example.com>",  to: "Bob <bob@example.com>",  subject: "Screenshot attached",  html: '<img src="cid:screenshot@example.com" alt="Screenshot"/>',  attachments: [    {      filename: "screenshot.png",      content: fs.readFileSync("/tmp/screenshot.png"), // Buffer containing the image data      cid: "screenshot@example.com",    },  ],};`

#### Embedding multiple images[​](https://nodemailer.com/message/embedded-images#embedding-multiple-images "Direct link to Embedding multiple images")

You can embed multiple images in the same email. Each image needs its own unique `cid` value, and each must be listed as a separate entry in the `attachments` array.

`const message = {  from: "Reports <reports@example.com>",  to: "Team <team@example.com>",  subject: "Monthly report",  html:`    <h1>Monthly Report</h1>    <p>Here are this month's results:</p>    <img src="cid:chart@example.com" alt="Sales chart"/>    <img src="cid:badge@example.com" alt="Achievement badge"/>  `,  attachments: [    { filename: "chart.png", path: "./chart.png", cid: "chart@example.com" },    { filename: "badge.png", path: "./badge.png", cid: "badge@example.com" },  ],};`
