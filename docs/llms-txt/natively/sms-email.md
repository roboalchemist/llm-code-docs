# Source: https://docs.buildnatively.com/guides/integration/sms-email.md

# SMS/Email

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-c42fbf4cfd0d7bd6033dae358800553c40bb447f%2Fimage.png?alt=media)

### 🧋 Bubble.io Plugin

#### \[Element] Natively - SMS/Email

#### Events:

* **SMS action is not allowed \[iOS]** - Get called when user restricted sending SMS for other apps
* **SMS sent \[iOS]** - successfully sent an SMS
* **SMS sending failed \[iOS]**
* **SMS sending cancelled \[iOS]** - Sending SMS screen was closed
* **Email action is not allowed \[iOS]** - Get called when user restricted sending email for other apps
* **Email sent \[iOS]** - successfully sent an Email
* **Email sending failed \[iOS]**
* **Email saved \[iOS]**
* **Email sending cancelled \[iOS]** - Sending Email screen was closed

#### Actions:

* **Send SMS** - Displays native MessageComposeViewController
  * Subject
  * Recipient
  * Body
* **Send Email** - Display native MailComposeViewController
  * Subject
  * Recipient
  * Body

### 🛠 JavaScript SDK

#### NativelyMessage

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const message = new NativelyMessage()
const send_sms_callback = function (resp) {
    console.log(resp.status); // SENT/CANCELLED/FAILED/NOT_ALLOWED (Works only on iOS)
};
const send_email_callback = function (resp) {
    console.log(resp.status); // SENT/CANCELLED/FAILED/NOT_ALLOWED/SAVED (Works only on iOS)
};
message.sendSMS(body, recipient, send_sms_callback);
message.sendEmail(subject, body, recipient, send_email_callback);
```

{% endcode %}
