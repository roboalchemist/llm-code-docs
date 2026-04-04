# Source: https://nodemailer.com/plugins/create

Title: Create plugins | Nodemailer

URL Source: https://nodemailer.com/plugins/create

Markdown Content:
Nodemailer provides three extension points in the email delivery pipeline where you can attach [plugins](https://nodemailer.com/plugins) to customize behavior:

1. **`compile`** - Runs immediately after `sendMail()` is called, before Nodemailer builds the MIME tree. Use this stage to modify `mail.data` (for example, to transform HTML content, add custom headers, or set default values).
2. **`stream`** - Runs after the MIME tree is fully constructed but before the message bytes are streamed out. At this stage you can modify the `mail.message` object directly or insert transform streams to process the raw message data.
3. **Transport** - The final stage where the raw message stream is delivered to its destination. Custom [transports](https://nodemailer.com/transports) implement this stage to define how messages are actually sent.

* * *

Attaching `compile` and `stream` plugins[​](https://nodemailer.com/plugins/create#attaching-compile-and-stream-plugins "Direct link to attaching-compile-and-stream-plugins")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To register a plugin, call the `use()` method on your transporter:

`transporter.use(step, pluginFn);`

| Parameter | Type | Description |
| --- | --- | --- |
| `transporter` | `Object` | A transporter instance created with `nodemailer.createTransport()` |
| `step` | `String` | The pipeline stage: either `'compile'` or `'stream'` |
| `pluginFn` | `Function(mail, done)` | Your plugin function (see the Plugin API section below) |

You can register multiple plugins for the same stage. They will execute in the order they were added.

* * *

Plugin API[​](https://nodemailer.com/plugins/create#plugin-api "Direct link to Plugin API")
-------------------------------------------------------------------------------------------

Every plugin function, including custom transport `send` methods, receives two arguments:

1. **`mail`** - An object containing information about the message being processed (see the table below).
2. **`done`** - A callback function with the signature `function(err)`. You **must** call this when your plugin finishes. Pass an `Error` object to abort the send operation, or call it with no arguments to continue processing.

### The `mail` object[​](https://nodemailer.com/plugins/create#the-mail-object "Direct link to the-mail-object")

| Property | Available at | Description |
| --- | --- | --- |
| `data` | `compile`, `stream`, **transport** | The original options object passed to `sendMail()` |
| `message` | `stream`, **transport** | A [`MimeNode`](https://github.com/nodemailer/nodemailer/blob/master/lib/mime-node/index.js) instance representing the built message (see also [MailComposer](https://nodemailer.com/extras/mailcomposer)) |
| `resolveContent` | `compile`, `stream`, **transport** | A helper method for converting Nodemailer content objects (streams, file paths, URLs) into a `String` or `Buffer` |

### `mail.resolveContent(obj, key, callback)`[​](https://nodemailer.com/plugins/create#mailresolvecontentobj-key-callback "Direct link to mailresolvecontentobj-key-callback")

Use this method to convert any [Nodemailer content type](https://nodemailer.com/message/attachments/#possible-content-types) (file path, URL, Stream, Buffer, etc.) into a plain `String` or `Buffer`. This is useful when you need to read and process content that might come from various sources.

`mail.resolveContent(sourceObject, propertyName, (err, value) => {  if (err) return done(err);  // value is a String or Buffer depending on the input type});`

#### Example: Log the final HTML string[​](https://nodemailer.com/plugins/create#example-log-the-final-html-string "Direct link to Example: Log the final HTML string")

`function plugin(mail, done) {  mail.resolveContent(mail.data, "html", (err, html) => {    if (err) return done(err);    console.log("HTML contents: %s", html.toString());    done();  });}`

* * *

`compile` plugins[​](https://nodemailer.com/plugins/create#compile-plugins "Direct link to compile-plugins")
------------------------------------------------------------------------------------------------------------

At the `compile` stage, only `mail.data` is available. The `mail.message` property does **not** exist yet because the MIME tree has not been built. You can freely modify `mail.data` and then call `done()` when finished. Passing an error to `done(err)` will abort the `sendMail()` operation.

#### Example: Generate plain text from HTML if missing[​](https://nodemailer.com/plugins/create#example-generate-plain-text-from-html-if-missing "Direct link to Example: Generate plain text from HTML if missing")

`transporter.use("compile", (mail, done) => {  if (!mail.data.text && mail.data.html) {    mail.data.text = mail.data.html.replace(/<[^>]*>/g, " ");  }  done();});`

* * *

`stream` plugins[​](https://nodemailer.com/plugins/create#stream-plugins "Direct link to stream-plugins")
---------------------------------------------------------------------------------------------------------

`stream` plugins run **after** the MIME tree is fully built but **before** any bytes are sent to the transport. At this stage you can:

* Modify `mail.message` directly (for example, to add or change headers)
* Pipe the output through additional Transform streams using `mail.message.transform()`

note

Modifying `mail.data` at this stage usually has **no effect** because the MIME tree has already been built from it. The exception is if your custom transport explicitly reads properties from `mail.data`.

### Example: Replace all tabs with spaces in the outgoing stream[​](https://nodemailer.com/plugins/create#example-replace-all-tabs-with-spaces-in-the-outgoing-stream "Direct link to Example: Replace all tabs with spaces in the outgoing stream")

`const { Transform } = require("stream");const tabToSpace = new Transform();tabToSpace._transform = function (chunk, _enc, cb) {  for (let i = 0; i < chunk.length; ++i) {    if (chunk[i] === 0x09) chunk[i] = 0x20; // 0x09 = TAB, 0x20 = space  }  this.push(chunk);  cb();};transporter.use("stream", (mail, done) => {  mail.message.transform(tabToSpace);  done();});`

### Example: Log all address fields[​](https://nodemailer.com/plugins/create#example-log-all-address-fields "Direct link to Example: Log all address fields")

`transporter.use("stream", (mail, done) => {  const a = mail.message.getAddresses();  console.log("From :", JSON.stringify(a.from));  console.log("To   :", JSON.stringify(a.to));  console.log("Cc   :", JSON.stringify(a.cc));  console.log("Bcc  :", JSON.stringify(a.bcc));  done();});`

* * *

### `mail.message.transform(transformStream)`[​](https://nodemailer.com/plugins/create#mailmessagetransformtransformstream "Direct link to mailmessagetransformtransformstream")

Adds a [`stream.Transform`](https://nodejs.org/api/stream.html#class-streamtransform) through which the raw message is piped **before** it reaches the transport. You can also pass a function that returns a Transform stream.

### `mail.message.getAddresses()`[​](https://nodemailer.com/plugins/create#mailmessagegetaddresses "Direct link to mailmessagegetaddresses")

Returns an object containing parsed email addresses from the **From**, **Sender**, **Reply-To**, **To**, **Cc**, and **Bcc** headers. Each property is an **array** of objects with `{ name, address }` structure. If a header is not present in the message, that property will be omitted from the result.

* * *

Writing a custom transport[​](https://nodemailer.com/plugins/create#transports "Direct link to Writing a custom transport")
---------------------------------------------------------------------------------------------------------------------------

A transport is an object that defines how messages are actually delivered. For built-in options, see [SMTP transport](https://nodemailer.com/smtp) and [other transports](https://nodemailer.com/transports). To create your own, implement an object with three properties: **`name`**, **`version`**, and a **`send(mail, done)`** method. Pass this object to `nodemailer.createTransport()` to create a working transporter.

`const nodemailer = require("nodemailer");const transport = {  name: require("./package.json").name, // e.g. "SMTP"  version: require("./package.json").version, // e.g. "1.0.0"  /**   * Sends the message.   * @param {Object} mail - The same`mail` object that plugins receive   * @param {Function} done - Callback with signature `(err, info)` */  send(mail, done) {    const input = mail.message.createReadStream();    const envelope = mail.message.getEnvelope();    const messageId = mail.message.messageId();    // For demonstration, we pipe the message to stdout    input.pipe(process.stdout);    input.on("end", () => {      done(null, {        envelope,        messageId,      });    });  },  /**   * Optional: Clean up resources when the transporter is closed.   * Useful for closing long-lived connections (e.g., pooled SMTP).   */  close() {    // Release resources here  },  /**   * Optional: Report whether the transport is idle.   * Used by connection pooling. Return `true`when the transport   * has capacity to send more messages immediately.   */  isIdle() {    return true;  },};const transporter = nodemailer.createTransport(transport);transporter.sendMail(  {    from: "sender@example.com",    to: "receiver@example.com",    subject: "Hello",    text: "Hello world!",  },  console.log);`

* * *

Summary[​](https://nodemailer.com/plugins/create#summary "Direct link to Summary")
----------------------------------------------------------------------------------

1. Choose the stage (`compile`, `stream`, or custom **transport**) that best fits your needs.
2. Write a plugin function that accepts **`(mail, done)`** and register it with `transporter.use()`, or implement `transport.send()` for a custom transport.
3. Always call `done()` when your plugin completes. Pass an `Error` to abort the send operation.
