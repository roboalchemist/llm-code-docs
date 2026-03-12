# Source: https://docs.mailtrap.io/account-and-organization/privacy-and-security/activity-log.md

# User audit Logs

User Audit Log automatically tracks the activities and actions performed by users within your account. It's a stream of events, logging actions taken and indicating who performed them, which is used for security purposes.

{% hint style="warning" %}
This feature is available to Enterprise plan users only.
{% endhint %}

## How to view User Audit Log

To view the Audit Log:

1. Log in to your Mailtrap account.
2. Click on **Settings** in the left-side menu and select **Audit Log**.

Once you're on the Audit Log page, you'll be able to see the activities performed by users:

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-1e47ccb62c63c5d0bc9b07fc26166ddfeee277ac%2Factivity-log-page.png?alt=media" alt="Mailtrap Activity Log page showing user actions with Actor, Description, Resource and Date columns" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Events start saving the moment you upgrade to Enterprise plan.
{% endhint %}

## User Audit Log event examples

In the Audit Log, you can see events such as:

* John Doe added a domain.
* John Doe created the field First Name.
* John Doe deleted a sandbox QA.
* John Doe invited the user <email@example.com> to the account.
* Someone attempted to log in to the user John Doe using GitHub.
* John Doe removed the webhook Logging from Transactional.

## Why should you use the User Audit Log?

Some of the reasons you should use the Audit Log include:

* **Security** – With events being tracked automatically, you can easily debug and investigate security incidents.
* **Transparency** – See what's happening in your account in real time by having a transparent overview of actions performed by users.
* **User management** – Monitor how your team members are interacting with Mailtrap services.

## Using User Audit Log with Mailtrap Webhooks

You can also pair the Audit Log with Mailtrap Webhooks and build an integration to monitor activities live.

Here's what you need to do:

1. Navigate to **Settings** → **Webhooks** and click on **Create New Webhook**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-455f6d42219c0da196d59c9834b3540664f61add%2Fwebhooks-create-new.png?alt=media" alt="Mailtrap Webhooks settings page with Create New Webhook button highlighted" width="563"><figcaption></figcaption></figure></div>

2. Enter your unique webhook URL, choose the Payload format, and select Audit Log.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b1449c2ca04e5b90b4628481994f20bdf4801d3f%2Fwebhook-activity-log-config.png?alt=media" alt="Add new webhook form with Activity Log selection and JSON payload example" width="563"><figcaption></figcaption></figure></div>

Now you can build an integration to monitor activities live, increasing your security measures.

Here's an example of a webhook payload:

{% code title="Audit Log webhook payload" %}

```json
{
  "events": [
    {
      "event": "activity_log.user.updated",
      "description": "updated the user profile",
      "actor": {
        "id": 783,
        "type": "user",
        "name": "Jane Doe"
      },
      "resource": {
        "id": "783",
        "type": "user",
        "name": "Jane Doe"
      },
      "changes": {
        "name": {
          "to": "[FILTERED]",
          "from": "[FILTERED]"
        }
      },
      "timestamp": 1733739084
    }
  ]
}
```

{% endcode %}
