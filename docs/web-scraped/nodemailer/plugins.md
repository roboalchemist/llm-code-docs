# Source: https://nodemailer.com/plugins

Title: Plugins | Nodemailer

URL Source: https://nodemailer.com/plugins

Markdown Content:
Nodemailer is designed to be **extensible**. You can inject custom logic at three well-defined phases of a message's lifecycle:

| Phase | Keyword | When it runs | Typical uses |
| --- | --- | --- | --- |
| **Pre-processing** | `compile` | After the message object is created but _before_ the MIME source is generated | Templating, automatic plain-text alternatives, address validation |
| **Processing** | `stream` | After MIME compilation, while the message stream is being prepared for sending | Inlining images, transforming HTML content |
| **Sending** | `transport` | When the message is ready to be delivered | [SMTP](https://nodemailer.com/smtp), [SES](https://nodemailer.com/transports/ses), SparkPost, custom HTTP APIs |

tip

Use _compile_ and _stream_ plugins when you want your plugin to work with any transport. Transport plugins are only needed when you want to define a completely custom delivery mechanism.

Writing a plugin[​](https://nodemailer.com/plugins#writing-a-plugin "Direct link to Writing a plugin")
------------------------------------------------------------------------------------------------------

A plugin is a function that receives a mail object and a callback. Here is an example that automatically generates a plain-text version of your email when only HTML is provided:

`// CommonJS module formatmodule.exports = function myCompilePlugin(mail, callback) {  // The mail object contains a`data`property with your message options  // You can read and modify these properties before the message is compiled  if (!mail.data.text && mail.data.html) {    // Generate plain-text from HTML using the html-to-text package    mail.data.text = require("html-to-text").htmlToText(mail.data.html);  }  // Always call the callback when done  // Pass no arguments for success, or pass an Error to abort sending  callback();};`

To use the plugin, register it on a transport instance with the `use()` method:

`const nodemailer = require("nodemailer");const transport = nodemailer.createTransport({ sendmail: true });// Register a compile plugin - it will run before MIME generationtransport.use("compile", require("./myCompilePlugin"));`

### Error handling[​](https://nodemailer.com/plugins#error-handling "Direct link to Error handling")

If your plugin encounters a problem that should prevent the message from being sent, pass an `Error` object to the callback:

`callback(new Error("Template not found"));`

When you pass an error, the message will **not** be sent. The error will be returned to the caller through the `sendMail()` callback or rejected promise.

Public plugins[​](https://nodemailer.com/plugins#public-plugins "Direct link to Public plugins")
------------------------------------------------------------------------------------------------

Here are some popular community-maintained plugins you can use:

* **express-handlebars** - Render Handlebars templates using your Express application's views directory. [https://github.com/yads/nodemailer-express-handlebars](https://github.com/yads/nodemailer-express-handlebars)
* **inline-base64** - Automatically convert inline base64-encoded images in your HTML to proper CID attachments. [https://github.com/mixmaxhq/nodemailer-plugin-inline-base64](https://github.com/mixmaxhq/nodemailer-plugin-inline-base64)
* **html-to-text** - Automatically generate a plain-text version of your email when only HTML content is provided. [https://github.com/andris9/nodemailer-html-to-text](https://github.com/andris9/nodemailer-html-to-text)

Looking for something else? Try [searching npm for "nodemailer plugin"](https://www.npmjs.com/search?q=keywords:nodemailer%20plugin).

* * *

Need more control? See **[Creating plugins](https://nodemailer.com/plugins/create)** for a detailed guide on the plugin API.
