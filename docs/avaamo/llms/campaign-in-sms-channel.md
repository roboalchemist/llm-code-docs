# Source: https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-sms-channel.md

# Campaign in SMS channel

This article describes how to create an outreach program for a vaccination drive using the SMS channel. Setting up an outreach program is just a 2-step process:

1. [Create a new recipient list](#step-1-create-a-new-recipient-list)
2. [Create and test your campaign](#step-2-create-and-test-your-campaign)

{% hint style="info" %}
**Note**: Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new outreach campaign program.
{% endhint %}

### Step 1: Create a new recipient list

The first step in any outreach program is to create a list of recipients for whom the outreach program is intended for. You can quickly set up a recipient list using a simple CSV file and upload it to your campaign.

**To create a new recipient list**:

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Recipients Lists** tab, and click **Create new recipient list -> Upload** **recipient list** option.
* Provide a recipient list name and upload a CSV with the required recipient lists. Since this is your first campaign, keep the file format as **Avaamo**.

{% hint style="success" %}
**Key points**:&#x20;

* The easiest way to upload a recipient list is to download a sample format of the recipient list, update or make a copy of the same file, rename it as required, and then upload the file.&#x20;
* For `SMS` channel, the only CSV column header that is mandatory is the **Phone** column.&#x20;
  * This is the number to which the campaign message is sent.&#x20;
  * The phone number must be a complete phone number including the country code. You can specify different types of phone formats such as +1 (25x) 67x-62xx, +125x67x62xx, or  +125x67x62xx as per your convenience, and all such formats are supported in the Avaamo Platform for sending campaign messages.
* Since this is your first outreach program and first recipient list, specify only the required details with a test phone number and skip the other details for now. See [Create new recipient list,](https://docs.avaamo.com/user-guide/outreach/recipient-lists) for more detailed information.
  {% endhint %}

### Step 2: Create and test your campaign

The final step in setting up an outreach program is creating a new campaign and testing it out.

**To create and test a new campaign**:

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Campaigns** tab, and click **Create new campaign -> SMS**.
* In the **Configure** section, specify the following details:

  * Campaign name, campaign description, pick the recipient list created in [Step 1: Create a new recipient list](#step-1-create-a-new-recipient-list),&#x20;
  * Select the phone number for sending the campaign message. This list is a pre-loaded list for your company and click **Next**.

  <figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNdcT0CGj8QPDgKy3eCTH%2F6.4-outreach-sms-campaign.png?alt=media&#x26;token=171c9fc0-c237-4337-b695-bcece4e82ec5" alt=""><figcaption></figcaption></figure>
* In the **Add Message** section, specify a simple text message to test out your first campaign and click **Next**.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8V3DBwM0dYbMWU9aF30j%2Fimage.png?alt=media&#x26;token=cc208b60-1733-4279-8049-81e65afd635d" alt=""><figcaption></figcaption></figure>

* In the **Activate** section, pick when you wish to send the outreach program to the users. You can either send it right after activating the campaign or at a specific scheduled time or on a recurring schedule. Since this is your first outreach program, enable **Send on activate** toggle option. See [Activate](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate) section, for more information on scheduling a campaign at a specific time.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKJijFIdkYzSo1Y8yBuf7%2Fimage.png?alt=media&#x26;token=a6606d69-0384-42b1-a4fe-2e0b8555312a" alt=""><figcaption></figcaption></figure>

* Click **Create** to save your first campaign. A summary details pop-up is displayed. You can quickly glance at all the details and click **Activate** to test your campaign. Since you have opted to send the campaign on activation, an SMS message as per the selected template is sent to all the recipients.&#x20;

### Next steps&#x20;

Now that you have successfully created and tested your first outreach program, you can dig deeper and understand:

* [How to schedule a campaign?](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate)
* [How to deactivate a campaign?](https://docs.avaamo.com/user-guide/campaigns/manage-campaigns#deactivate-campaign)
* [How to create customized SMS templates for different outreach programs?](https://docs.avaamo.com/user-guide/outreach/templates)
