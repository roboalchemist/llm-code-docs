# Source: https://docs.bugbug.io/collaboration/alerts/sending-slack-message.md

# Sending Slack message

Sending Slack messages to your project channel or directly to people is the best way to keep your team updated on the status of test/suite/schedule runs.

{% hint style="warning" %}
Keep in mind that the "Alerts" feature is only available on paid plans.\
So any related features, such as Slack alerts, will not be available on the free plan.

More information about pricing can be found here: <https://bugbug.io/pricing/>
{% endhint %}

Before proceeding to the first step, remember to [integrate your Slack workspace with BugBug](https://docs.bugbug.io/integrations/slack#connect-your-slack-workspace-with-bugbug).\
If you haven't done so yet, don't worry - BugBug will prompt you for permissions when you start creating an alert.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUUB3iGJGE3hRxH44y4yk%2FScreenshot%20at%20Oct%2024%2015-21-10.png?alt=media&#x26;token=ea65ed99-17cc-4d43-9b81-bc416ea9bcf2" alt=""><figcaption></figcaption></figure>

Already connected? Great! Follow the steps below.

### Set Slack message type&#x20;

In the first field, you need to specify the messaging method. We currently support two different ways to send a Slack message:

* Channel message *(most common)*&#x20;
* Direct message

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQkrz4I82vV1n37meUuQ5%2FZrzut%20ekranu%202023-10-23%20o%2015.45.52.png?alt=media&#x26;token=00b64f6f-a950-4ae0-b88f-855d585d61fd" alt=""><figcaption></figcaption></figure>

### Choose a recipient/channel

In the next box, you need to select a channel or person to receive the messages.\
BugBug will provide you with a list of all available Slack members.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZRvIaEUUPlEUZRNuT4dM%2FZrzut%20ekranu%202023-10-24%20o%2015.09.05.png?alt=media&#x26;token=1f2a666c-a216-411b-817e-d20077a0233f" alt=""><figcaption></figcaption></figure>

### Testing a Slack alert

Before creating a new Slack alert, it's possible to check how it works by clicking on the **"Trigger Alert"** button.

{% hint style="info" %}
The Slack message template is predefined for all users.\
If you need to customize the message, [create a webhook alert instead](https://docs.bugbug.io/collaboration/alerts/sending-webhook).
{% endhint %}
