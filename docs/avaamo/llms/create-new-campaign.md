# Source: https://docs.avaamo.com/user-guide/outreach/campaigns/create-new-campaign.md

# Create new campaign

Avaamo Platform allows you to create multiple campaigns each with different schedules in just a few clicks. This section walks you through the steps of quickly creating a campaign in the Avaamo Platform.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* See [Quick start](https://docs.avaamo.com/user-guide/outreach/quick-start), for a quick article on creating your first outreach program.
* Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new campaign.
  {% endhint %}

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Campaign** tab, and click **Create new campaign -> {{Delivery channel}} .**  Supported channels - SMS, C-IVR, MS Teams, and Custom channel.

{% hint style="info" %}
**Notes**:&#x20;

* C-IVR, MS Teams, and Custom channel delivery channel for outreach campaign is available only when it is enabled for the account. Contact Avaamo Support for further assistance.
* For quick start, refer to the following topics
  * [Campaign in SMS channel](https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-sms-channel)
  * [Campaign in C-IVR channel](https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-c-ivr-channel)
  * [Campaign in MS Teams channel](https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-ms-teams-channel)
  * [Campaign in Custom channel](https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-custom-channel)
    {% endhint %}

A campaign consists of three sections:

1. [Configure](#configure): In this section, you start by specifying the campaign name, and description, and pick a list of recipients for your campaign. Based on your requirements, you can configure a campaign with just one-way outbound calls or with two-way communication where the campaign recipients can communicate back to the campaign by responding to the same campaign message.&#x20;
2. [Add Message](#add-message): In this section, you specify the actual message that is sent to the recipients.
3. [Activate](#activate): This section is where you specify when to send the message to the recipients. You can send it immediately after activating the campaign or you can schedule it for a later time based on your business requirements.

## Configure

{% hint style="success" %}
**Pre-requisite:** You must create a recipient list before creating a new campaign. See [Create new recipient list](https://docs.avaamo.com/user-guide/outreach/recipient-lists), for more information.
{% endhint %}

In this section, you start by specifying the campaign name and description, pick a list of recipients for whom the campaign is intended, and select a delivery channel for your campaign. Specify the following details and click **Next**:

<table><thead><tr><th width="147.44475920679886">Parameters</th><th width="422.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Campaign name</td><td>Indicates the name of the campaign. </td><td align="center">50 characters</td></tr><tr><td>Campaign description</td><td>Indicates the description of the campaign. Use this to specify the purpose of the campaign. </td><td align="center">200 characters</td></tr><tr><td>Select recipient list </td><td><p>Indicates the list of the recipients for whom the campaign is intended. Pick a recipient list from the dropdown. </p><ul><li>Note that only those recipient lists that are not marked for testing are available in the dropdown. </li><li>See <a href="../recipient-lists">Create new recipient list</a>, for more information on how to create a recipient list.   </li></ul></td><td align="center">NA</td></tr></tbody></table>

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNdcT0CGj8QPDgKy3eCTH%2F6.4-outreach-sms-campaign.png?alt=media&#x26;token=171c9fc0-c237-4337-b695-bcece4e82ec5" alt=""><figcaption></figcaption></figure>

### Phone: One-way communication&#x20;

**Applicable for**: SMS and C-IVR channels

One-way campaigns are only outbound messages to the recipients. With this option, you can only send campaign messages to the recipients. There is no action performed when a recipient sends messages back to the campaign message.

In the **Create campaign -> Configure** section, select the **Phone** option. Provide a phone number for making the outbound calls. This is the number used to send the campaign message to the recipient. Phone number is a pre-loaded list for your company. Contact Avaamo Support for more information, if required. &#x20;

### Link to Avaamo agent: Two-way communication

**Applicable for**: SMS, C-IVR, MS Teams, and Custom channels

In two-way communication, a campaign message is sent to the recipients and the campaign recipients can communicate back to the campaign by responding to the same campaign message. This is a very useful feature to make the campaign conversational and proactively enables users to quickly accomplish a wide variety of tasks.&#x20;

For example, consider that you have sent a reminder to all the recipients of an upcoming vaccination drive. A recipient reads the reminder message but now wishes to reschedule the appointment due to some personal reasons. With two-way communication, the recipient can now send an SMS message back to the campaign asking for rescheduling.&#x20;

{% hint style="success" %}
**Pre-requisite**: Depending on the delivery channel for your campaign, you must have an agent with the corresponding channel enabled. Based on your requirement, you can design this agent to handle specific use cases, say, for example, rescheduling an appointment flow. See [Channels](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy), for more information.
{% endhint %}

In the **Create campaign -> Configure** section, select the **Link to Avaamo agent** option. Based on the delivery channel selected, all the agents where the corresponding channel is enabled and you have at least [View permission](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions) on the agent are listed in the dropdown.&#x20;

Each agent is displayed using the following nomenclature - `<<Agent stage>> <<Agent name>>::<<channel name>>.` This helps users easily identify the right channel to select since the agent with the same name can exist in multiple stages.&#x20;

Pick the agent from the list as per your requirement and click **Next**.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fwz4ttaMAvXn7UDbBt8j8%2F6.4-campaign-line-to-agent.png?alt=media&#x26;token=c7235cd6-13ac-4ab9-9206-2c0b1e58eab6" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**: When you link the campaign to an Avaamo agent, all the campaign conversations are also available in the Conversation history of the agent. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history), for more information.&#x20;
{% endhint %}

## Add Message

In this section, you specify the actual message that is sent to the recipients and click **Next** to proceed to the [Activate](#activate) section. Based on the selected delivery channel, you can either specify an SMS message, Voice message, or MS Teams message in this section.

### **Language-specific messages**

You can add customized campaign messages in all the different languages supported by the Avaamo Platform. See [Languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-supported-languages), for more information on the list of supported languages in the Avaamo Conversational AI Platform.

* The default supported language is en-US.
* In the **Add message** section, click the + icon and select the language in which you wish to add the message.&#x20;
  * When you add a language, the response is automatically translated and displayed in the message area. All the other fields such as the response name, phone header, and country code as applicable are copied as-is in the new language tab.
  * By default, the translation only gets added when adding a new language and is not a continuous process, which implies that if you have added a message in English and later update it, the translation is not updated for the other languages and remains the same as it was at the time of adding the new language. You can further customize the response as required.&#x20;
* You can also add and load language-specific templates. See [Create new template](https://docs.avaamo.com/user-guide/templates#create-new-template), for more information.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjqZS0Zb1iMoZWIoYoxXg%2Fimage.png?alt=media&#x26;token=17651543-1cbe-4003-bdc4-cef19dff8982" alt=""><figcaption></figcaption></figure>

### Response sets

You can add multiple responses for the same language and then apply different filters for each response in the response set. See [Filters](#filters-optional), for more information.

Click **Add** in the **Responses** section to add another response for the same language. For each response, you can enter the response name that helps you to identify the response.

{% hint style="info" %}
**Note**: If you add multiple responses for a language without any filter, then the system picks a random response from the set of multiple responses and displays it to the user.
{% endhint %}

You can add up to 50 responses to the same language.&#x20;

### Multiple campaign messages

**Supported channels**: SMS, MS Teams, Custom Channel

This feature allows you to trigger multiple messages to the same recipient using the same campaign configuration at the same time. It saves the time and effort of configuring the campaign from scratch and hence promotes the reusability of campaigns.

To configure multiple campaign messages, in the **Add message** tab, specify each message separated by `<avm-break-line/>` tag.  You can add any number of messages, there is no restriction on the number of messages that can be configured using `<avm-break-line/>` tag.

Here, for this example, when a campaign is triggered, two SMS messages are sent to the user. Though a part of the same campaign, each message is delivered independently, which implies that each message can have its delivery status and failure reasons, if any.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F19Y2ouJVE5AETjLyWEUq%2Fimage.png?alt=media&#x26;token=42ab8f1d-6a68-4a3f-89d7-40cff22b6b73" alt=""><figcaption></figcaption></figure>

Another example can be a healthcare campaign, where you have a set of SMS messages (instructions) that you wish to send to the patients before a procedure. You can configure multiple SMS messages using a simple  `<avm-break-line/>` tag.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3MSO41Tj3HZq2SMN26o5%2Fimage.png?alt=media&#x26;token=191be10e-2544-42fa-ac4c-4f35e446fcb8" alt=""><figcaption></figcaption></figure>

Once the campaign is triggered, you can view the complete status in the `Campaign statistics` page.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQjOh9ivoEhsd5hIDfNs4%2Fimage.png?alt=media&#x26;token=19af3155-ff34-489a-a224-18956e0a8d59" alt=""><figcaption></figcaption></figure>

Click the help icon in the `Text Sent` column to view more details on the message delivery:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FCLwn0CrNtPRAmgDX87sJ%2Fimage.png?alt=media&#x26;token=43da45d9-62f8-40ef-882f-49e050bf96cc" alt=""><figcaption></figcaption></figure>

In the `Campaign statistics` page, you can also download reports for further analysis. Each message in a multi-message campaign sent to a recipient can be identified using a `recipient_uuid.` The `recipient_uuid` remains the same for each message in the multi-message list when multiple messages are sent to the same recipient. See [Campaign statistics](https://docs.avaamo.com/user-guide/outreach/campaign-statistics), for more information.

{% hint style="info" %}
**Notes**:

* There is no option to add a delay between messages.&#x20;
* The order is which the campaign messages are sent to the recipient is dependent on the carrier provider.
* If you have a use case, to trigger different messages at different times, then the best option is to configure and schedule a different campaign.
* `recipient_uuid` is also available in the Outreach insights API. See [Outreach insights API](https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/outreach-insights-api), for more information.
  {% endhint %}

### Phone header

**Applicable for C-IVR and SMS Delivery Channel**&#x20;

You can [create a recipient list](https://docs.avaamo.com/user-guide/outreach/recipient-lists) in either Avaamo format or any custom format according to your business requirements. When you wish to trigger a campaign in the C-IVR or SMS channel, all that is required is a phone number to which the campaign message must be sent. Phone numbers in the recipient CSV can be in multiple columns and are based on the use case, say as Phone number, Preferred Phone number, Home number.&#x20;

In the **Select phone header** dropdown, a list of all the column headers from the selected recipient list is populated. Pick the appropriate column header containing the phone number of the recipients to which the campaign message must be sent. If the recipient list is in Avaamo format, then by default **phone** column header is selected in the dropdown.&#x20;

### Email header

**Applicable for MS Teams Channel**

You can [create a recipient list](https://docs.avaamo.com/user-guide/outreach/recipient-lists) in either Avaamo format or any custom format according to your business requirements. When you wish to trigger a campaign in the Microsoft Teams channel, all that is required is an email to which the campaign message must be sent.&#x20;

In the **Select email header** dropdown, a list of all the column headers from the selected recipient list is populated. Pick the appropriate column header containing the email of the recipients to which the campaign message must be sent. If the recipient list is in Avaamo format, then by default **email** column header is selected in the dropdown.&#x20;

### **Primary header**

**Applicable for Custom Channel**

You can [create a recipient list](https://docs.avaamo.com/user-guide/outreach/recipient-lists) in either Avaamo format or any custom format according to your business requirements. When you wish to trigger a campaign in the Custom channel, all that is required is the primary header to which the campaign recipient is bound.&#x20;

The field selected in the primary header is the `client_uuid` in the custom channel outgoing payload. A campaign triggered to a recipient is hence identified by the combination of `channel_uuid and client_uuid` in the Avaamo Conversational AI Platform. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#payload-details), for more information on the outgoing message payload format.

### **Country code - Optional**

**Applicable for SMS and C-IVR Channel**

This field is optional and allows you to specify the country code for the recipients. If a country code is specified, then all the recipient phone numbers are automatically prefixed with the designated code.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbiRMGz9g8bHcrqXHKZ1v%2Fimage.png?alt=media&#x26;token=6f3febec-0381-4ec5-b9d4-6800115ec7b9" alt=""><figcaption></figcaption></figure>

Given the mandatory requirement for recipient phone numbers to be in the E.164 format, which necessitates a country code, this feature proves valuable when working with recipient files that lack country codes.&#x20;

### **Filters - Optional**

For each language, you can add multiple messages and for each message, you can associate filters. This allows you to reuse the same campaign configuration and tailor the messages to different sets of recipients as per the requirement. Adding filters is optional.

Note that if you add multiple responses without any filter, then when the campaign is triggered, a random message from the set of messages is picked and delivered to the recipient. See [Filters](https://docs.avaamo.com/user-guide/outreach/filters), for more information.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fu8VEPI0VtrADmNSerXMN%2Fimage.png?alt=media&#x26;token=3aa77c41-66e4-4199-aad2-23ec3bd5aac7" alt=""><figcaption></figcaption></figure>

### SMS Message

* **Delivery Channel**: SMS
* **Maximum length**: Each SMS message can be a maximum of 1600 characters. It is recommended to specify an SMS Message with less than 320 characters for better delivery of the message.

Indicates the actual text message sent to the user in the SMS channel. You can create a customized message using the column headers from your recipient list CSV. This helps you to make the message personal and reachable to users. See [Examples](https://docs.avaamo.com/user-guide/templates#examples), for a few sample message templates.

Alternatively, if you already have a template, then click the **Load Message Template** link to reuse and select a pre-existing message.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* You can add customized campaign messages in all the different languages supported by the Avaamo Platform. See [Language-specific messages](#language-specific-messages), for more information.
* For each language, you can add multiple messages and for each message, you can associate filters to target a specific set of recipients. See [Filters](https://docs.avaamo.com/user-guide/outreach/filters), for more information.&#x20;
  {% endhint %}

### MS Teams message

**Delivery Channel**: [MS Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams)

Indicates the actual message sent to the user in the MS Teams channel. You can create a customized message using the column headers from your recipient list CSV. This helps you to make the message personal and reachable to users. See [Examples](https://docs.avaamo.com/user-guide/templates#examples), for a few sample message templates.

Alternatively, if you already have a template, then click the **Load Message Template** link to reuse and select a pre-existing message.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* You can add customized campaign messages in all the different languages supported by the Avaamo Platform. See [Language-specific messages](#language-specific-messages), for more information.
* For each language, you can add multiple messages and for each message, you can associate filters to target a specific set of recipients. See [Filters](https://docs.avaamo.com/user-guide/outreach/filters), for more information.&#x20;
  {% endhint %}

### Voice Message

**Delivery Channel**: C-IVR

Indicates the actual voice message sent to the user in the C-IVR channel. You can create a customized message using the column headers and SSML tags from your recipient list CSV. This helps you to make the message personal and reachable to users. See [Examples](https://docs.avaamo.com/user-guide/templates#examples), for a few sample voice message templates. Alternatively, if you already have a template, then click the **Load Message Template** link to reuse and select a pre-existing message.&#x20;

{% hint style="success" %}
**Key Points**:

* For each language, you can add multiple messages and for each message, you can associate filters to target a specific set of recipients. See [Filters](https://docs.avaamo.com/user-guide/outreach/filters), for more information.&#x20;
* You can add customized campaign messages in all the different languages supported by the Avaamo Platform. See [Language-specific messages](#language-specific-messages), for more information.
  {% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FampHwCbWYIxPzker3fFs%2Fimage.png?alt=media&#x26;token=117b5708-69b8-4c1f-8c4b-300333bbc33d" alt=""><figcaption></figcaption></figure>

* Click the SSML tags at the bottom of the message box to add the corresponding tag in the Message box area. You can use this to quickly construct messages using SSML tags. see [Supported SSML tags](https://docs.avaamo.com/user-guide/ref/speech-synthesis-markup-language-ssml), for more information and examples on SSML tags.
* Click the **Play** button below the message box to preview the voice message. This reads out the message in the selected voice persona and you can use this feature to alter the voice message as required.
* **Voice persona**: If you have specified one-way communication (using Phone in the Configure section) then, you can pick the voice persona from the list of available personas in the Voice message section. Alternatively, if you are using a two-way communication by linking to an existing Avaamo agent, then the persona as configured in the C-IVR channel of the Avaamo agent is selected and displayed.

### Custom channel Message

**Delivery Channel**: Custom Channel

Indicates the actual message sent to the user in the Custom channel. You can create a customized message using the column headers from your recipient list CSV. This helps you to make the message personal and reachable to users. See [Examples](https://docs.avaamo.com/user-guide/templates#examples), for a few sample message templates.

Alternatively, if you already have a template, then click the **Load Message Template** link to reuse and select a pre-existing message.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* You can add customized campaign messages in all the different languages supported by the Avaamo Platform. See [Language-specific messages](#language-specific-messages), for more information.
* For each language, you can add multiple messages and for each message, you can associate filters to target a specific set of recipients. See [Filters](https://docs.avaamo.com/user-guide/outreach/filters), for more information.&#x20;
  {% endhint %}

## Activate&#x20;

This section is where you specify when to send the message to the recipients. You can send it immediately after activating the campaign or you can schedule it for a later time based on your business requirements. Specify the activation method for your campaign and **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FWrqXRy9snSKt057QuZXl%2FScreenshot%202023-03-13%20at%203.55.33%20PM.png?alt=media&#x26;token=8233f385-1ca6-4303-8fcc-a490c9337f0b" alt=""><figcaption></figcaption></figure>

### Send on activate

Enable this toggle if you wish to send the campaign message to the recipients immediately after activation. &#x20;

### **Schedule campaign**

Enable this toggle if you wish to set a specific time and date for sending the campaign message to the list of recipients.

* Time: The time when the scheduled campaign message is sent.
* Date: The date when the scheduled campaign message is sent. The scheduled date must be less than one year from the current date.
* Timezone: The timezone of the selected time for the scheduled campaign.

### **Recurring campaign**

Enable this toggle if you wish to periodically send the campaign message to the list of recipients.

* Timezone: The timezone of the selected time for the recurring campaign.
* Start time: The time when the recurring campaign message is sent.
* Repeat: Pick the frequency of the recurring campaign.
* Ends: The date when the recurring campaign ends. The end date must be less than one year from the start date.
* After: Number of occurrences after which the recurring campaign ends. Occurrences must be between 1 to 100.

### **Campaign failures**&#x20;

Specify the email Ids of the users to receive campaign error notifications.

* These errors are related to campaign configuration errors such as (SFTP file uploaded errors or Teams configuration errors) that result in a complete campaign failure.
* These are not related to the errors in the [Campaign Statistics](https://docs.avaamo.com/user-guide/outreach/campaign-statistics) page.
* It is sent only for activated campaigns per campaign run. If you have a recurring campaign, then each time the campaign is executed and until the error is resolved, the error notification is sent to the emails configured in the **Campaign failures** section.

{% hint style="info" %}
**Note**: You can enable all the toggles and accordingly the campaign message is sent on activation, also at the set specific time and date, and recurring as required. Ensure that the date and times in the scheduled campaign and recurring campaign are non-overlapping for a better user experience.
{% endhint %}

## Campaign summary details

After creating the campaign, a **Campaign summary** details pop-up is displayed.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2Na3RLDMGnijouqAM4G0%2Foutreach-campaign-details.png?alt=media&#x26;token=a9de383b-eb23-40a6-93ac-27a0ac2b8d5d" alt=""><figcaption></figcaption></figure>

* You can quickly glance at all the details before actually activating or testing the campaign. Scroll to the right to view all the messages.&#x20;
* Click **View filter details** to view the list of recipients filtered for each language and response set to whom the campaign message is sent.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzQgPVzHbZiwyDCcFM5Sb%2Foutreach-campaign-filters.png?alt=media&#x26;token=9f5324e5-f1e9-449c-afe4-0b0635f3f90c" alt=""><figcaption></figcaption></figure>

* Click **Download CSV** to download the recipient list CSV. In this CSV, you can view&#x20;
  * The list of recipients and the filters applied against each recipient to whom the campaign message is triggered.&#x20;
  * The failed reason for all those recipients to whom the campaign message is not triggered.
* Click **Test campaign**, if you wish to test your campaign with a selected set of test recipients before activating the campaign. See [Test campaign](https://docs.avaamo.com/user-guide/outreach/campaigns/test-campaign), for more information.
* Click **Activate** to activate your campaign. Based on the option selected in the **Campaign** -> **Activate** section, the SMS message is either sent immediately after activation or at a scheduled date.&#x20;
