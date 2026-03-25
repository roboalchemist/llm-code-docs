# Source: https://docs.bugbug.io/collaboration/alerts/sending-webhook.md

# Sending webhook

Outgoing webhooks are a powerful feature for advanced users that can be used to integrate BugBug into your current workflow, such as sending custom notifications to your team's communicator like Slack.

Before proceeding to the next step, remember to first set up a webhook in your external service. You will need the webhook configuration to populate the form fields.

{% hint style="info" %}
**Note**: You can use built-in variables in any field, e.g. **{{testRunId}}**.
{% endhint %}

### Set basic request data

In the first two fields, you need to define the request **method** and the **webhook URL**. Currently, we support the most popular webhook request methods like POST and GET.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F102guqauEIfxPSXUTz93%2FZrzut%20ekranu%202023-09-25%20o%2014.49.29.png?alt=media&#x26;token=969898a0-47f0-4b47-ad1f-83bc0178ff32" alt=""><figcaption><p>Method and Webohook URL fields on the setup screen</p></figcaption></figure>

### Define POST request body message

The **Body** is an optional field that consumes data in JSON format. Its value depends on your needs and the requirements of your external service provider.

If you need to send additional data through the webhook request, it's the best place to do so.

### Testing a webhook alert

Before creating a new webhook alert, it's possible to check how it works by clicking on the **"Trigger Alert"** button.

It's a good practice to do this. It allows you to avoid unexpected errors in the future, for example, invalid credentials or wrong body format.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F88vc4LzDb5ao8ouPU165%2FZrzut%20ekranu%202023-09-25%20o%2015.00.29.png?alt=media&#x26;token=c12b54f6-ab8a-4735-8950-1bd42dd8e47a" alt=""><figcaption><p>Verify alert configuration</p></figcaption></figure>

### Define the POST request body message by using a built-in variable

When it comes to setting up the **Body** of your webhook, you can easily use **only** the built-in variables within BugBug, so the overall configuration will be more intuitive. Knowing this, for instance, you can set an alert that will send the name of the test with the usage of the POST method that contains within its **Body** a variable that reflects the finished test's name, like here:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F5wlYUcFkpNQ0I2NpSx7M%2F2_requestBodyWithVariable.png?alt=media&#x26;token=13b1e733-0bff-4941-9dc6-19819820c456" alt=""><figcaption><p>Request body with a bult-in variable</p></figcaption></figure>

```javascript
{
  "test name of a finished test": "{{testName}}"
}
```

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fl2eLLPIIEVtKf3NCNUpD%2F5_testNameVar.png?alt=media&#x26;token=2705eca2-5402-4c71-a198-95b50f5a7ed3" alt=""><figcaption><p>List of built-in variables</p></figcaption></figure>

&#x20;&#x20;

The `{{testName}}` built-in variable was used here, which resulted in an output of a webhook alert (after the test finished) in the "Raw Content" section in the tested Webhook service:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlzppEeVm5949Z963YGFn%2F3_requestResponse.png?alt=media&#x26;token=1c550c30-76e2-4b0b-9f91-17c917d835a3" alt=""><figcaption><p>Webook alert for the triggered action</p></figcaption></figure>

&#x20;This matches the test's name that exists and was executed:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FLk9nRAc62kCuAKC0G13g%2F4_testsList.png?alt=media&#x26;token=978b098e-1a0a-44e7-ab75-c85432ad9ab0" alt=""><figcaption><p>List of created tests</p></figcaption></figure>
