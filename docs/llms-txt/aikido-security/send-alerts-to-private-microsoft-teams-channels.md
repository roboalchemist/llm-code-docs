# Source: https://help.aikido.dev/getting-started/chat-and-alerts/send-alerts-to-private-microsoft-teams-channels.md

# Send Alerts to Private Microsoft Teams Channels

Because Microsoft Teams apps can't be member of a private Teams channel, additional setup is required to send alerts to a private channel. The reason for this is a technical limitation in Microsoft Teams that exists since several years and was not solved until now. In some cases it might be easier to create a new MS Team instead, and only allow authorized people access to this team. Please note that alerts in private channels will be send as the user who has performed the setup steps and not as Aikido.

***

Follow these steps to send alerts to a private Microsoft Teams channel:

{% stepper %}
{% step %}

### Install the Aikido app

If not already done, follow the steps described on this page: [ms-teams-notifications](https://help.aikido.dev/getting-started/chat-and-alerts/ms-teams-notifications "mention")
{% endstep %}

{% step %}

### Create the Workflow

Select the private channel that should receive the alerts, click on "More Options" (the three dots) and select "Workflows".

Select **"Send webhook alerts to a channel"**. After that enter a name for the workflow and click on "Next".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FBJrk33HQ5uvMY3fwVHeb%2Fevents%2C%20alerts%2C%20or%20custom%20triggers--%20withous.png?alt=media&#x26;token=3341bb54-da0f-489b-80b5-39e649beb6cd" alt="" width="563"><figcaption><p>Create a new Workflow</p></figcaption></figure>

Select the Microsoft Team and the private channel where the alerts should be sent. Finish the creation by clicking on "Add workflow".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FXsY4czeXgYXVAhr2CTuu%2Fevents%2C%20alerts%20or%20custom%20triggers--%20withous.png?alt=media&#x26;token=c51b40be-65cc-4e65-9f45-3d731cecd4fa" alt="" width="563"><figcaption><p>Select Microsoft Team and private channel</p></figcaption></figure>

Copy and save the workflow URL using the copy button. You need this URL later. Do **not** click on "Done".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FflYY0yMq7e8eERyWu3LX%2FPasted%20Graphic%203.png?alt=media&#x26;token=b0c52521-f23b-4964-9094-776141d703f4" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Edit the Workflow

The workflow is configured to send messages as the Power Automate bot, but this bot cannot send messages to private channels either.

Click on "Manage your workflow" in the left bottom corner of the dialog and then on "Edit" on the top left. Expand the "Attachment is null" section by clicking on it. Modify the "Post card in a chat or channel" action and select "User" for the "Post as" setting as shown in the following screenshot. Make sure to save your changes after that.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FSYRMkpBhYBPaN3zTDjCe%2FScreenshot%202026-01-28%20at%2013.18.23.png?alt=media&#x26;token=5fac63fc-886e-445f-ba85-bf482d79dfe8" alt=""><figcaption><p>Modify Workflow</p></figcaption></figure>
{% endstep %}

{% step %}

### Finish setup

Open the Microsoft Teams integration page and click on "New alert". Inside the channel select input, click on "Link a different private channel". After that the following dialog is opened. Select the Microsoft Team and enter the channel name and  the workflow URL. Click on "Add Channel" to finish the setup.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Ff2amCF4FsfMQbEMwArHz%2Fimage.png?alt=media&#x26;token=1c575c72-e9d2-4868-935f-be4f2db58269" alt="" width="563"><figcaption><p>Finish the connection</p></figcaption></figure>
{% endstep %}

{% step %}

### Confirm successful setup

After clicking on "Add Channel", you should receive the message "This channel has been successfully added to Aikido." in your private Microsoft Teams channel.
{% endstep %}
{% endstepper %}
