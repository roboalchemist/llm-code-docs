# Source: https://nodemailer.com/transports/stream

Title: Stream transport | Nodemailer

URL Source: https://nodemailer.com/transports/stream

Markdown Content:
Stream transport is **not** a real SMTP transport. Instead of delivering your message to a remote mail server, it _generates_ the complete RFC 822 formatted email and returns it to you. This makes it ideal for:

* **[Testing](https://nodemailer.com/smtp/testing)** - Examine the exact bytes that would be sent over the wire, create snapshot tests, or forward the output to another system for validation.
* **Custom delivery pipelines** - Apply Nodemailer plugins (such as DKIM signing or list headers) to your message, then handle delivery yourself through an internal API, archive messages for audit logging, or process them in any custom way.

For an overview of all available transports, see the [transports documentation](https://nodemailer.com/transports).

* * *

Enabling Stream transport[​](https://nodemailer.com/transports/stream#enabling-stream-transport "Direct link to Enabling Stream transport")
-------------------------------------------------------------------------------------------------------------------------------------------

To use Stream transport, create a transporter with `streamTransport: true` in the options object:

`const nodemailer = require("nodemailer");const transporter = nodemailer.createTransport({  streamTransport: true,  // See additional options below});`

### Options[​](https://nodemailer.com/transports/stream#options "Direct link to Options")

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `streamTransport` | `boolean` | **required** | Set to `true` to enable Stream transport. |
| `buffer` | `boolean` | `false` | When `true`, returns the generated message as a `Buffer` instead of a `Readable` stream. |
| `newline` | `'windows' | 'unix'` | `'unix'` | Line ending style for the generated message. Use `'windows'` for CRLF (`\r\n`) or `'unix'` for LF (`\n`). |

JSON Transport

A separate **JSON transport** is also available. Enable it by setting `jsonTransport: true` (instead of `streamTransport`). JSON transport returns a serialized JSON representation of the message rather than the raw RFC 822 format. See the [JSON transport section](https://nodemailer.com/transports/stream#json-transport) below for details.

### `sendMail()` callback signature[​](https://nodemailer.com/transports/stream#sendmail-callback-signature "Direct link to sendmail-callback-signature")

The `sendMail()` callback receives two arguments: `(err, info)`. On success, the `info` object contains:

* **`envelope`** - The SMTP envelope object with `from` (string) and `to` (array of strings) properties.
* **`messageId`** - The generated _Message-ID_ header value for this email.
* **`message`** - The generated email content. By default this is a Node.js `Readable` stream. If you set `buffer: true`, it will be a `Buffer`. For JSON transport, it will be a JSON string (or a plain object if `skipEncoding: true`).

For details on configuring the message object passed to `sendMail()`, see the [message configuration](https://nodemailer.com/message) documentation. To parse the generated RFC 822 stream output, you can use [MailParser](https://nodemailer.com/extras/mailparser).

* * *

Examples[​](https://nodemailer.com/transports/stream#examples "Direct link to Examples")
----------------------------------------------------------------------------------------

### 1. Stream a message with Windows-style line endings[​](https://nodemailer.com/transports/stream#1-stream-a-message-with-windows-style-line-endings "Direct link to 1. Stream a message with Windows-style line endings")

This example generates an email as a readable stream using Windows-style CRLF line endings. The stream can be piped to any writable destination.

`const nodemailer = require("nodemailer");const transporter = nodemailer.createTransport({  streamTransport: true,  newline: "windows", // Use CRLF (\r\n) line endings});transporter.sendMail(  {    from: "sender@example.com",    to: "recipient@example.com",    subject: "Streamed message",    text: "This message is streamed using CRLF line endings.",  },  (err, info) => {    if (err) throw err;    console.log(info.envelope);   // { from: '...', to: ['...'] }    console.log(info.messageId);  // '<unique-id@example.com>'    // Pipe the raw RFC 822 message to stdout    info.message.pipe(process.stdout);  });`

### 2. Return a Buffer with Unix-style line endings[​](https://nodemailer.com/transports/stream#2-return-a-buffer-with-unix-style-line-endings "Direct link to 2. Return a Buffer with Unix-style line endings")

When you need the entire message in memory at once, set `buffer: true`. This example also explicitly uses Unix-style LF line endings (the default).

`const nodemailer = require("nodemailer");const transporter = nodemailer.createTransport({  streamTransport: true,  buffer: true,    // Return a Buffer instead of a stream  newline: "unix", // Use LF (\n) line endings (this is the default)});transporter.sendMail(  {    from: "sender@example.com",    to: "recipient@example.com",    subject: "Buffered message",    text: "This message is buffered using LF line endings.",  },  (err, info) => {    if (err) throw err;    console.log(info.envelope);    console.log(info.messageId);    // The complete message is available as a Buffer    console.log(info.message.toString());  });`

### 3. Generate a JSON-encoded message object (>= v3.1.0)[​](https://nodemailer.com/transports/stream#json-transport "Direct link to 3. Generate a JSON-encoded message object (>= v3.1.0)")

**JSON transport** is a separate transport type, not an option of Stream transport. To use it, set `jsonTransport: true` instead of `streamTransport`. The resulting `info.message` will be a JSON string representing the message structure. This format is useful for storing messages, inspecting them in tests, or passing them to other systems. Binary data such as attachments is automatically base64-encoded.

If you prefer to work with a JavaScript object rather than a JSON string, set `skipEncoding: true` to receive the raw data object directly.

`const nodemailer = require("nodemailer");const transporter = nodemailer.createTransport({  jsonTransport: true,});transporter.sendMail(  {    from: "sender@example.com",    to: "recipient@example.com",    subject: "JSON message",    text: "I hope this message gets JSON-ified!",  },  (err, info) => {    if (err) throw err;    console.log(info.envelope);    console.log(info.messageId);    console.log(info.message); // JSON string  });`

Here is an example of what the JSON output looks like:

`{  "from": { "address": "sender@example.com", "name": "" },  "to": [{ "address": "recipient@example.com", "name": "" }],  "subject": "JSON message",  "text": "I hope this message gets JSON-ified!",  "headers": {},  "messageId": "<77a3458f-8070-339d-095f-85bb73f3db8e@example.com>"}`

* * *

When to choose Stream vs. JSON transport[​](https://nodemailer.com/transports/stream#when-to-choose-stream-vs-json-transport "Direct link to When to choose Stream vs. JSON transport")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the following table to help decide which transport best fits your needs:

| Use case | Recommended transport |
| --- | --- |
| Inspect or pipe raw RFC 822 SMTP content | `streamTransport` (Stream or Buffer) |
| Store structured message data for later replay | `jsonTransport` |
| Apply Nodemailer plugins (DKIM, headers, etc.) | Either (plugins run before output) |
| Need access to the `_raw` property (see [custom source](https://nodemailer.com/message/custom-source)) | **Stream transport only** |
