# Source: https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-ms-teams-channel.md

# Campaign in MS Teams channel

Avaamo Conversational AI Platform allows you to trigger an outreach campaign and send messages to all the MS Teams App users via the MS Teams channel. This article describes how to create an outreach program for a course or academy drive using the MS Teams channel.&#x20;

Setting up an outreach program is just a 3-step process:

1. [Create an agent and deploy in MS Teams Channel](#step-1-create-an-agent-and-deploy-in-ms-teams-channel)
2. [Create a new recipient list](#step-2-create-a-new-recipient-list)
3. [Create and test your campaign](#step-3-create-and-test-your-campaign)

{% hint style="info" %}
**Note**: Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new outreach campaign program.
{% endhint %}

### Step 1: Create an agent and deploy in MS Teams Channel

The first step to trigger an outreach campaign via the MS Teams channel is to create an agent and then deploy the agent in the MS Teams channel. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.

* While you are deploying the agent in the MS Teams channel, if you wish to use the same agent to link to a campaign, then ensure that the corresponding Azure bot in the Azure Portal has been granted the `TeamsAppInstallation.ReadWriteSelfForUser.All` API Permissions. See [Channel Settings in Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams#outreach), for more information.
* In the MS Teams channel settings, in addition to the other settings, you must specify the Directory (Tenant ID) and Team's App ID for sending campaign messages using this agent. You can trigger the outreach campaign only to the users of the specified Azure directory. See [Step 2: Create a new recipient list](#step-2-create-a-new-recipient-list), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FiGf6NbJfHjhLbWI9tvo9%2F6.4.0-ms-teams.png?alt=media&#x26;token=d9d7b7dc-f2f4-46b3-9688-4b1098924db0" alt=""><figcaption></figcaption></figure>

### Step 2: Create a new recipient list

The next step in any outreach program is to create a list of recipients for whom the outreach program is intended for. You can quickly set up a recipient list using a simple CSV file and upload it to your campaign.&#x20;

**To create a new recipient list**:

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Recipients Lists** tab, and click **Create new recipient list.**
* Provide a recipient list name and upload a CSV with the required recipient lists.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* The easiest way to upload a recipient list is to download a sample format of the recipient list, update or make a copy of the same file, rename it as required, and then upload the file.&#x20;
* To trigger a campaign via `MS Teams` channel,&#x20;
  * The recipient list must be from the users of the Azure directory specified in the Channel settings. See [Channel Settings in Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams#deploy-your-agent-to-microsoft-teams-channel), for more information.&#x20;
  * The recipient list CSV must contain an **email** column. This is the email receiving the campaign message.&#x20;
  * Ensure the email in the recipient list CSV is a part of the Azure directory for which the MS Teams channel is configured. See [Step 1: Setup the MS Teams channel](#step-1-setup-the-ms-teams-channel), for more information.
* Since this is your first outreach program and first recipient list, specify only the required details with a test email and skip the other details for now. See [Create new recipient list,](https://docs.avaamo.com/user-guide/outreach/recipient-lists) for more detailed information.
  {% endhint %}

### Step 3: Create and test your campaign

The final step in setting up an outreach program is creating a new campaign and testing it out.

**To create and test a new campaign**:

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Campaigns** tab, and click **Create new campaign -> Microsoft Teams**..
* In the **Configure** section,&#x20;
  * Campaign name, campaign description, pick the recipient list created in [Step 1: Create a new recipient list](#step-1-create-a-new-recipient-list)
  * Select a channel from an existing agent to make your campaign conversational. Pick the agent deployed on the MS Teams channel with all the prerequisites and channel settings for triggering the campaign message. See [Step 1: Setup the MS Teams channel](#step-1-setup-the-ms-teams-channel), for more information.
  * Click **Next** to proceed with the next step.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8XHjcSN7LJcIorK6hDRo%2FScreenshot%202023-03-14%20at%203.41.05%20PM.png?alt=media&#x26;token=ce59772b-2277-4601-80e6-c9b0a4633450" alt=""><figcaption></figcaption></figure>

* In the **Add Message** section, specify a simple text message to test out your first campaign and click **Next**. You can also add messages from the predefined templates using [Load message template](https://docs.avaamo.com/user-guide/templates#ms-teams-message).

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJ5hg7voOptFPE4mRBEMG%2FScreenshot%202023-03-14%20at%203.42.33%20PM.png?alt=media&#x26;token=5a65429b-86be-4a57-bf33-7583eb40d72b" alt=""><figcaption></figcaption></figure>

* In the **Activate** section, pick when you wish to send the outreach program to the users. You can either send it right after activating the campaign or at a specific scheduled time. Since this is your first outreach program, enable **Send on activate** toggle option. See [Activate](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate) section, for more information on scheduling a campaign at a specific time.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fu1gWTQkqs8Xmiobqije0%2Fimage.png?alt=media&#x26;token=aefb2d56-3602-49d3-874a-ace080c97bdb" alt=""><figcaption></figcaption></figure>

* Click **Create** to save your first campaign. A summary details pop-up is displayed. You can quickly glance at all the details and click **Activate** to test your campaign. Since you have opted to send the campaign on activation, a message in the Teams bot is sent to all the recipients.&#x20;

### Next steps&#x20;

Now that you have successfully created and tested your first outreach program, you can dig deeper and understand:

* [How to schedule a campaign?](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate)
* [How to deactivate a campaign?](https://docs.avaamo.com/user-guide/campaigns/manage-campaigns#deactivate-campaign)
* [How to create customized MS Teams templates for different outreach programs?](https://docs.avaamo.com/user-guide/templates#ms-teams-message)
