# Source: https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-c-ivr-channel.md

# Campaign in C-IVR channel

This article describes how to create an outreach program for a vaccination drive using the C-IVR channel. Setting up an outreach program is just a 2-step process:

1. [Create a new recipient list](#step-1-create-a-new-recipient-list)
2. [Create and test your campaign](#step-2-create-and-test-your-campaign)

{% hint style="info" %}
**Note**: Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new outreach campaign program.
{% endhint %}

### Step 1: Create a new recipient list

The first step in any outreach program is to create a list of recipients for whom the outreach program is intended for. You can quickly set up a recipient list using a simple CSV file and upload it to your campaign.

**To create a new recipient list**:

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Recipients Lists** tab, and click **Create new recipient list**.
* Provide a recipient list name and upload a CSV with the required recipient lists.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* The easiest way to upload a recipient list is to download a sample format of the recipient list, update or make a copy of the same file, rename it as required, and then upload the file.&#x20;
* For `C-IVR` channel, the only CSV column header that is mandatory is the **Phone** column.&#x20;
  * This is the number to which the campaign message is sent.&#x20;
  * The phone number must be a complete phone number including the country code. You can specify different types of phone formats such as +1 (254) 672-6232, +12546726232, or  +12546726232 as per your convenience, and all such formats are supported in the Avaamo Platform for sending campaign messages.
* Since this is your first outreach program and first recipient list, specify only the required details with a test phone number and skip the other details for now. See [Create new recipient list,](https://docs.avaamo.com/user-guide/outreach/recipient-lists) for more detailed information.
  {% endhint %}

### Step 2: Create and test your campaign

The final step in setting up an outreach program is creating a new campaign and testing it out.

**To create and test a new campaign**:

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Campaigns** tab, and click **Create new campaign > C-IVR / Phone Channel**.
* In the **Configure** section, specify the following details:
  * Campaign name, campaign description, pick the recipient list created in [Step 1: Create a new recipient list](#step-1-create-a-new-recipient-list), for more information.
  * Select the phone number for sending the campaign message. This list is a pre-loaded list for your company and click **Next**.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FFV4j4mvJDFtklz3GNEyB%2FScreenshot%202023-03-14%20at%203.28.41%20PM.png?alt=media&#x26;token=a00d07d9-3276-4107-8b03-744b051dee57" alt=""><figcaption></figcaption></figure>

* In the **Add Message** section, specify a simple text message to test out your first campaign and click **Next**. You can also add messages from the predefined templates using [Load message template](https://docs.avaamo.com/user-guide/templates#voice-message).

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FoAuqr7b7HpmDtn72gJDp%2Fimage.png?alt=media&#x26;token=6e340db7-396e-45e6-8630-c60a0a92c0d9" alt=""><figcaption></figcaption></figure>

* In the **Activate** section, pick when you wish to send the outreach program to the users. You can either send it right after activating the campaign or at a specific scheduled time or on a recurring schedule. Since this is your first outreach program, enable **Send on activate** toggle option. See [Activate](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate) section, for more information on scheduling a campaign at a specific time.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXAeSDLWtKd9Gpx6lG7EC%2Fimage.png?alt=media&#x26;token=dcabfc3a-6d3b-4eed-a7e9-f2b5afe0744e" alt=""><figcaption></figcaption></figure>

* Click **Create** to save your first campaign. A summary details pop-up is displayed. You can quickly glance at all the details and click **Activate** to test your campaign. Since you have opted to send the campaign on activation, an IVR message as per the selected template is sent to all the recipients.&#x20;

### Next steps&#x20;

Now that you have successfully created and tested your first outreach program, you can dig deeper and understand:

* [How to schedule a campaign?](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate)
* [How to deactivate a campaign?](https://docs.avaamo.com/user-guide/campaigns/manage-campaigns#deactivate-campaign)
* [How to create customized voice templates for different outreach programs?](https://docs.avaamo.com/user-guide/templates#voice-message)
