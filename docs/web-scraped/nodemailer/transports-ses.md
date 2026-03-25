# Source: https://nodemailer.com/transports/ses

Title: SES transport | Nodemailer

URL Source: https://nodemailer.com/transports/ses

Markdown Content:
The Nodemailer **SES transport** allows you to send emails through **Amazon Simple Email Service (SES)** using the official AWS SDK v3 package [@aws-sdk/client-sesv2](https://www.npmjs.com/package/@aws-sdk/client-sesv2). It acts as a wrapper around the [`SendEmailCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/sesv2/) while letting you use the familiar `transporter.sendMail()` API you already know from Nodemailer.

For an overview of all available transports, see the [transports documentation](https://nodemailer.com/transports/).

The AWS SES SDK is not included with Nodemailer, so you need to install it separately:

`npm install @aws-sdk/client-sesv2`

Quick start[​](https://nodemailer.com/transports/ses#quick-start "Direct link to Quick start")
----------------------------------------------------------------------------------------------

`const nodemailer = require("nodemailer");const { SESv2Client, SendEmailCommand } = require("@aws-sdk/client-sesv2");// 1. Create an AWS SES client//    If you omit credentials, the SDK uses the default credential chain//    (environment variables, shared credentials file, IAM role, etc.)const sesClient = new SESv2Client({ region: "us-east-1" });// 2. Create a Nodemailer transport configured to use SESconst transporter = nodemailer.createTransport({  SES: { sesClient, SendEmailCommand },});// 3. Send the messageconst info = await transporter.sendMail({  from: "sender@example.com",  to: "recipient@example.com",  subject: "Hello from Nodemailer + SES",  text: "I hope this message gets sent!",  // You can pass additional SES-specific options under the`ses`key:  ses: {    ConfigurationSetName: "my-config-set",    EmailTags: [{ Name: "tag_name", Value: "tag_value" }],  },});console.log(info.envelope); // { from: "sender@example.com", to: ["recipient@example.com"] }console.log(info.messageId); // The SES Message ID`

tip

You can also use the callback style if you prefer: `transporter.sendMail(mailOptions, callback)`.

Transport options[​](https://nodemailer.com/transports/ses#transport-options "Direct link to Transport options")
----------------------------------------------------------------------------------------------------------------

When calling `createTransport()`, pass an object with an `SES` property. This `SES` object must contain the following **required** keys:

| Key | Type | Description |
| --- | --- | --- |
| `sesClient` | `SESv2Client` | An initialized AWS SDK v3 SES client instance |
| `SendEmailCommand` | `SendEmailCommand` | The `SendEmailCommand` class from **@aws-sdk/client-sesv2** |

Property names matter

The property **must** be named exactly `sesClient` (not `client`, `ses`, or any other name). If you store your client in a variable with a different name, use explicit property syntax to rename it:

`const myClient = new SESv2Client({ region: "us-east-1" });const transporter = nodemailer.createTransport({  SES: { sesClient: myClient, SendEmailCommand }, // rename myClient to sesClient});`

Message-level options[​](https://nodemailer.com/transports/ses#message-level-options "Direct link to Message-level options")
----------------------------------------------------------------------------------------------------------------------------

When calling `sendMail()`, you can include an optional **ses** property in your [mail options](https://nodemailer.com/message) object. Any properties you add to this object are passed directly to the AWS `SendEmailCommand`, allowing you to use SES-specific features such as `EmailTags`, `ConfigurationSetName`, `FeedbackForwardingEmailAddress`, and more. See the [AWS SES documentation](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/sesv2/command/SendEmailCommand/) for all available options.

Response object[​](https://nodemailer.com/transports/ses#response-object "Direct link to Response object")
----------------------------------------------------------------------------------------------------------

When the email is sent successfully, the promise resolves (or the callback receives) an object with the following properties:

| Property | Description |
| --- | --- |
| `envelope` | An object containing `from` (string) and `to` (array of strings) representing the email envelope |
| `messageId` | The Message ID returned by SES, formatted as a standard Message-ID header value |
| `response` | The raw Message ID string as returned by SES (without angle brackets or domain suffix) |
| `raw` | A `Buffer` containing the complete raw RFC 822 message that was sent to SES |

Memory usage

The entire message (including attachments) is buffered in memory before being sent to SES. For messages with very large attachments, ensure your application has sufficient memory available.

Rate limiting[​](https://nodemailer.com/transports/ses#rate-limiting "Direct link to Rate limiting")
----------------------------------------------------------------------------------------------------

The SES transport does **not** include built-in rate limiting, queuing, or concurrency controls. Each `sendMail()` call immediately initiates a send operation to AWS.

If you need to send bulk emails, you must implement your own rate limiting to stay within your [SES sending limits](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html). The AWS SDK v3 handles automatic retries with exponential backoff for transient errors.

tip

For high-volume sending, consider using a job queue (such as Bull, Bee-Queue, or AWS SQS) to manage send operations and respect SES rate limits.

DKIM signing[​](https://nodemailer.com/transports/ses#dkim-signing "Direct link to DKIM signing")
-------------------------------------------------------------------------------------------------

When using [DKIM signing](https://nodemailer.com/dkim) with the SES transport, Nodemailer automatically excludes the `Date` and `Message-ID` headers from the DKIM signature. This is necessary because SES may modify these headers, which would otherwise invalidate the signature.

`const transporter = nodemailer.createTransport({  SES: { sesClient, SendEmailCommand },  dkim: {    domainName: "example.com",    keySelector: "mail",    privateKey: fs.readFileSync("dkim-private.pem", "utf8"),  },});`

Troubleshooting[​](https://nodemailer.com/transports/ses#troubleshooting "Direct link to Troubleshooting")
----------------------------------------------------------------------------------------------------------

This error means your AWS credentials lack the required permissions. To resolve it:

1. Verify that the IAM user or role associated with your credentials has the **ses:SendRawEmail** permission. See the [minimal IAM policy example](https://nodemailer.com/transports/ses#example-2) below.
2. Ensure the **From** address (or its entire domain) is verified in the [SES console](https://console.aws.amazon.com/ses/). SES requires sender verification before you can send emails.
3. If your SES account is still in sandbox mode, you must also verify each recipient address. Request production access to remove this restriction.
4. In rare cases, AWS access keys containing special characters have caused authentication failures. If everything else looks correct, try regenerating your access keys.

### "Cannot find module '@aws-sdk/client-sesv2'"[​](https://nodemailer.com/transports/ses#cannot-find-module-aws-sdkclient-sesv2 "Direct link to \"Cannot find module '@aws-sdk/client-sesv2'\"")

The AWS SES SDK is not bundled with Nodemailer. You need to install it as a separate dependency:

`npm install @aws-sdk/client-sesv2`

### Using the verify() method with SES[​](https://nodemailer.com/transports/ses#using-the-verify-method-with-ses "Direct link to Using the verify() method with SES")

The SES transport supports the `transporter.verify()` method to validate your configuration. Unlike [SMTP transports](https://nodemailer.com/smtp), which test the actual connection, the SES verify method works by attempting to send an invalid test message. If SES responds with an `InvalidParameterValue` or `MessageRejected` error, the verification is considered successful because it confirms your credentials and configuration are correct.

`// Verify SES configurationconst isValid = await transporter.verify();console.log("SES configuration is valid:", isValid);`

Examples[​](https://nodemailer.com/transports/ses#examples "Direct link to Examples")
-------------------------------------------------------------------------------------

### 1. Send a message[​](https://nodemailer.com/transports/ses#example-1 "Direct link to 1. Send a message")

This example shows how to send an email using the callback style, which is useful when you are not using async/await:

`const nodemailer = require("nodemailer");const { SESv2Client, SendEmailCommand } = require("@aws-sdk/client-sesv2");// Create the SES client using the AWS_REGION environment variableconst sesClient = new SESv2Client({ region: process.env.AWS_REGION });// Create the Nodemailer transportconst transporter = nodemailer.createTransport({  SES: { sesClient, SendEmailCommand },});// Send the emailtransporter.sendMail(  {    from: "sender@example.com",    to: ["recipient@example.com"],    subject: "Message via SES transport",    text: "I hope this message gets sent!",    ses: {      // Add tags for tracking and analytics      EmailTags: [{ Name: "tag_name", Value: "tag_value" }],    },  },  (err, info) => {    if (err) {      console.error("Failed to send email:", err);      return;    }    console.log("Email sent successfully!");    console.log("Envelope:", info.envelope);    console.log("Message ID:", info.messageId);  });`

### 2. Minimal IAM policy[​](https://nodemailer.com/transports/ses#example-2 "Direct link to 2. Minimal IAM policy")

Your AWS IAM user or role needs permission to call `ses:SendRawEmail`. Here is the minimal IAM policy required:

`{  "Version": "2012-10-17",  "Statement": [    {      "Effect": "Allow",      "Action": "ses:SendRawEmail",      "Resource": "*"    }  ]}`

For production environments, consider restricting the `Resource` to specific verified identities rather than using `"*"`.
