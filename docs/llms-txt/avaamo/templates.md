# Source: https://docs.avaamo.com/user-guide/outreach/templates.md

# Templates

A **Template** is where you provide a customized message that is sent to recipients of your campaign. You can quickly create a template specific to your campaign in the **Outreach -> Templates** page.&#x20;

The following are some of the key features of the **Templates** section:

* Create a customized template by using the column headings in the recipient list CSV
* Reuse the same template for different campaigns.

## Create new template

{% hint style="info" %}
**Notes**:&#x20;

* See [Quick start](https://docs.avaamo.com/user-guide/outreach/quick-start), for a quick article on creating your first outreach program.
* Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new recipient list.
  {% endhint %}

Based on the [delivery channel ](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#configure)of your campaign, you can create&#x20;

* [Text message template for an SMS channel ](#text-message)
* [Voice message template for the C-IVR channel](#voice-message)
* [MS Teams message template for the MS Teams channel](#ms-teams-message)
* [Custom message template for the Custom channel](#custom-message)

### **Text message**

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Templates** tab, and click **Create new template -> Text Message** to create an SMS message template.  Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfOrTZTGqqo7CEf0dQ7vw%2Foutreach-create-new-text-template.png?alt=media&#x26;token=8052c67c-9a5c-4556-b9b5-b80cff821a5a" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="166.44475920679886">Parameters</th><th width="381.798167959476">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Template name</td><td><p>Indicates the name of the template. </p><p></p><p>Provide a name that is easily identifiable to pick when you create a campaign.</p></td><td>50 characters</td></tr><tr><td>Template description</td><td>Indicates the description of the template. Use this to specify the purpose of the template. </td><td>200 characters</td></tr><tr><td>Language</td><td><p>Indicates the language in which you wish to create templates. </p><ul><li>You can create templates in all the languages supported by the Avaamo Platform. See <a href="../how-to/build-agents/configure-agents/deploy/web-supported-languages">Languages</a>, for more information on the list of supported languages in the Avaamo Conversational AI Platform. </li><li>The corresponding language template is displayed in the <strong>Add message</strong> section when you load the message template. See <a href="../campaigns/create-new-campaign#add-message">Add message</a>, for more information.</li><li>The default language is en-US.</li><li>Click <strong>Change</strong> add select the required language in which you wish to create the template.</li></ul></td><td>N/A</td></tr><tr><td>SMS template</td><td><p>Indicates the SMS message sent to the recipients. </p><p></p><p>To configure multiple campaign messages, specify each message separated by <code>&#x3C;avm-break-line/></code> tag. See <a href="../campaigns/create-new-campaign#multiple-campaign-messages">Multiple campaign messages</a>, for more information.</p><p></p><p>You can create customized messages specific to your campaign using the column headers in the recipient lists CSV file. See <a href="../recipient-lists#recipient-list-file-format">Recipient list CSV format</a>, for more information.</p></td><td><p>Each SMS message can be a maximum of 1600 characters </p><p></p><p>It is recommended to specify an SMS Message with less than 320 characters for better delivery of the message.</p></td></tr></tbody></table>

The newly created template is displayed in the **Templates** tab.&#x20;

### **Voice message**

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Templates** tab, and click **Create new template -> Voice Message** to create a voice message template.  Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FsnaVI3OH1EXuxgLow28S%2FScreenshot%202025-10-13%20at%2012.39.45%E2%80%AFPM.png?alt=media&#x26;token=7fb8848b-dd4a-476d-9dd7-48099122c785" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="166.44475920679886">Parameters</th><th width="388.798167959476">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Template name</td><td><p>Indicates the name of the template. </p><p></p><p>Provide a name that is easily identifiable to pick when you create a campaign.</p></td><td>50 characters</td></tr><tr><td>Template description</td><td>Indicates the description of the template. Use this to specify the purpose of the template. </td><td>200 characters</td></tr><tr><td>Language</td><td><p>Indicates the language in which you wish to create templates. </p><ul><li>You can create templates in all the voice-supported languages of the Avaamo Platform. See <a href="../../how-to/build-agents/configure-agents/deploy/voice-supported-languages#supported-languages">Languages</a>, for more information on the list of supported languages in the Avaamo Conversational AI Platform. </li><li>The corresponding language template is displayed in the <strong>Add message</strong> section when you load the message template. See <a href="../campaigns/create-new-campaign#add-message">Add message</a>, for more information.</li><li>The default language is en-US.</li><li>Click <strong>Change</strong> add select the required language in which you wish to create the template.</li></ul></td><td>N/A</td></tr><tr><td>Agent Type</td><td>Indicates the type of agent the template is designed for. You can select whether the template is intended for an <a href="../ai-agent">AI Agent</a> or a <a href="../how-to/build-agents/add-skills">Classic Agent</a>.</td><td>N/A</td></tr><tr><td>Voice template</td><td><p>Indicates the voice message sent to the recipients. </p><p></p><p>You can create a customized message using the column headers and SSML tags from your recipient list CSV.  See <a href="../recipient-lists#recipient-list-file-format">Recipient list CSV format</a>, for more information. </p><p></p><p>See <a href="../ref/speech-synthesis-markup-language-ssml">Supported SSML tags</a>, for more information and examples on SSML tags. </p><p></p><p>Configuring multiple campaign messages for the C-IVR channel is not supported. </p></td><td>It is recommeded to keep the voice message short and succint so that user's can understand it clearly.</td></tr></tbody></table>

{% hint style="success" %}
**Key points**: Note the following key points about the voice message template:

* You can click the SSML tags at the bottom of the message box to add the corresponding tag in the Message box area. You can use this to quickly construct messages using SSML tags. See [Supported SSML tags](https://docs.avaamo.com/user-guide/ref/speech-synthesis-markup-language-ssml), for more information and examples on SSML tags.
* To preview the message, click the **Play** button below the message box to preview the voice message. This reads out the message in the selected voice persona and you can use this feature to alter the voice message as required.
* Pick the voice persona from the list of available personas in the Voice message section. This is the persona used to render the voice template
  {% endhint %}

### MS Teams message

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Templates** tab, and click **Create new template > Teams Message** to create an MS Teams message template.  Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fk3IYw4fGt570AMvMiyvZ%2Foutreach-create-new-teams-template.png?alt=media&#x26;token=098b7b27-8f89-40cc-827e-ac907e53d601" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="166.44475920679886">Parameters</th><th width="381.798167959476">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Template name</td><td><p>Indicates the name of the template. </p><p></p><p>Provide a name that is easily identifiable to pick when you create a campaign.</p></td><td>50 characters</td></tr><tr><td>Template description</td><td>Indicates the description of the template. Use this to specify the purpose of the template. </td><td>200 characters</td></tr><tr><td>Language</td><td><p>Indicates the language in which you wish to create templates. </p><ul><li>You can create templates in all the languages supported by the Avaamo Platform. See <a href="../how-to/build-agents/configure-agents/deploy/web-supported-languages">Languages</a>, for more information on the list of supported languages in the Avaamo Conversational AI Platform. </li><li>The corresponding language template is displayed in the <strong>Add message</strong> section when you load the message template. See <a href="../campaigns/create-new-campaign#add-message">Add message</a>, for more information.</li><li>The default language is en-US.</li><li>Click <strong>Change</strong> add select the required language in which you wish to create the template.</li></ul></td><td>N/A</td></tr><tr><td>Teams Message template </td><td><p>Indicates the message sent to the recipients via the MS Teams channel. </p><p></p><p>You can create customized messages specific to your campaign using the column headers in the recipient lists CSV file. See <a href="../recipient-lists#recipient-list-file-format">Recipient list CSV format</a>, for more information. </p><p></p><p>In the Teams Message template, you can use:</p><ul><li>Simple text messages</li><li>Any custom card Teams messages can be wrapped in a <code>CustomTeamsMessage</code> object and used as-is. See <a href="#custom-card-ms-teams-message">Custom card Teams message</a>, for an example.</li></ul><p>To configure multiple campaign messages, specify each message separated by <code>&#x3C;avm-break-line/></code> tag. See <a href="../campaigns/create-new-campaign#multiple-campaign-messages">Multiple campaign messages</a>, for more information.</p></td><td><p>It is recommeded to keep the campaign message short and succint so that user's can understand it clearly.</p><p></p></td></tr></tbody></table>

The newly created template is displayed in the **Templates** tab.&#x20;

### **Custom message**

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Templates** tab, and click **Create new template -> Custom message** to create a message template for a custom channel. Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXlnqdR2zs88r790NKfC2%2Fimage.png?alt=media&#x26;token=848ae18f-0fe0-47ec-ad68-e9188af7a1db" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="166.44475920679886">Parameters</th><th width="381.798167959476">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Template name</td><td><p>Indicates the name of the template. </p><p></p><p>Provide a name that is easily identifiable to pick when you create a campaign.</p></td><td>50 characters</td></tr><tr><td>Template description</td><td>Indicates the description of the template. Use this to specify the purpose of the template. </td><td>200 characters</td></tr><tr><td>Language</td><td><p>Indicates the language in which you wish to create templates. </p><ul><li>You can create templates in all the languages supported by the Avaamo Platform. See <a href="../how-to/build-agents/configure-agents/deploy/web-supported-languages">Languages</a>, for more information on the list of supported languages in the Avaamo Conversational AI Platform. </li><li>The corresponding language template is displayed in the <strong>Add message</strong> section when you load the message template. See <a href="../campaigns/create-new-campaign#add-message">Add message</a>, for more information.</li><li>The default language is en-US.</li><li>Click <strong>Change</strong> add select the required language in which you wish to create the template.</li></ul></td><td>N/A</td></tr><tr><td>Custom Message template </td><td><p>Indicates the message sent to the recipients via the Custom channel. </p><p></p><p>You can create customized messages specific to your campaign using the column headers in the recipient lists CSV file. See <a href="../recipient-lists#recipient-list-file-format">Recipient list CSV format</a>, for more information. </p><p></p><p>Note that currently, only text messages are supported in the Custom Message template. </p><p></p><p>To configure multiple campaign messages, specify each message separated by <code>&#x3C;avm-break-line/></code> tag. See <a href="../campaigns/create-new-campaign#multiple-campaign-messages">Multiple campaign messages</a>, for more information.</p></td><td><p>It is recommeded to keep the campaign message short and succint so that user's can understand it clearly.</p><p></p></td></tr></tbody></table>

The newly created template is displayed in the **Templates** tab.&#x20;

## **Search template**

In the **Outreach -> Templates** tab, start entering the text in the **Search** text box and press the **Enter** key or click the **Search** icon. The results are filtered and displayed based on the text entered in the **Search** text box.

## **Edit template**

You can edit a template from the **Outreach -> Templates** tab. Click on any template in the **Templates** page to open the template in edit mode. Edit the required details and click **Update**.

## **Delete template**

* In the **Outreach -> Templates** tab, click three ellipse dots in the **Actions** column of the template to view the extended menu and click **Delete.**&#x20;
* Click **OK** in the confirmation message to delete the template.

{% hint style="info" %}
**Note**: You can delete a template only when it is not associated with any campaign.
{% endhint %}

## Examples

This section lists a few sample templates that you can refer to and customize for your use case. Consider the following CSV file:

<table><thead><tr><th width="206">email</th><th width="118">First name</th><th width="119">Last name</th><th>Date</th><th>Time</th></tr></thead><tbody><tr><td>john@abccorp.com</td><td>John</td><td>Miller</td><td>20 Dec 2022</td><td>10:00 AM</td></tr><tr><td>mark@abccorp.com</td><td>Mark</td><td>Smith</td><td>23 Dec 2022</td><td>4:00 PM</td></tr></tbody></table>

{% hint style="info" %}
**Note**: All the placeholder values in the template must be column names in the recipient CSV file.
{% endhint %}

### Vaccination drive

<mark style="color:blue;">`SMS message / MS Teams message / Custom message`</mark>

{% code overflow="wrap" %}

```
Dear ${first_name} ${last_name},

Flu season is back again this time of the year. The Sparsh care center is organizing a free Flu vaccination drive on October 1st and October 2nd from 10 AM to 6 PM. Visit your nearest Sparsh Care Center to get vaccinated. 

Best regards,
Sparsh care center team
```

{% endcode %}

<mark style="color:blue;">`Voice message`</mark>

{% code overflow="wrap" %}

```json
<speak>
Dear ${first_name} ${last_name},

Flu season is back again this time of the year. The Sparsh care center is organizing a free Flu vaccination drive on October 1st and October 2nd from 10 AM to 6 PM. Visit your nearest Sparsh Care Center to get vaccinated. 

Best regards,
Sparsh care center team
</speak>
```

{% endcode %}

### Appointment confirmation

<mark style="color:blue;">`SMS message / MS Teams message / Custom message`</mark>

<pre data-overflow="wrap"><code><strong>Hi ${first_name} ${last_name}, 
</strong><strong>
</strong><strong>We have your appointment confirmed on ${date} at ${time} in our Sparsh Care Center.
</strong>
Best regards,
Sparsh care center team
</code></pre>

<mark style="color:blue;">`Voice message`</mark>

{% code overflow="wrap" %}

```
<speak>
Hi ${first_name} ${last_name},

We have your appointment confirmed on <emphasis level="strong"> ${date} at ${time} </emphasis> in our Sparsh Care Center.

Best regards,
Sparsh care center team
</speak>
```

{% endcode %}

### Reschedule appointment as the clinic is closed

<mark style="color:blue;">`SMS message / MS Teams message / Custom message`</mark>

{% code overflow="wrap" %}

```
Hi ${first_name},

This is to inform you that the Sparsh care center clinic is closed on Friday, 16th September 2022. Your appointment is rescheduled. Please call 999-887-9388 if you have any questions.

Best regards,
Sparsh care center team
```

{% endcode %}

<mark style="color:blue;">`Voice message`</mark>

{% code overflow="wrap" %}

```
<speak>
Hi ${first_name},

This is to inform you that the Sparsh care center clinic is closed on Friday, 16th September 2022. Your appointment is rescheduled. Please call <emphasis level="strong"> 999-887-9388 </emphasis> if you have any questions.

Best regards,
Sparsh care center team
</speak>
```

{% endcode %}

### Custom card MS Teams message&#x20;

The following is an example of an Adaptive card message that can be used in an Outreach campaign via MS Teams channel:

{% code overflow="wrap" %}

```json
{
  "CustomTeamsMessage": {
    "type": "message",
    "attachments": [
      {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
          "type": "AdaptiveCard",
          "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
          "version": "1.5",
          "body": [
            {
              "type": "TextBlock",
              "text": "Hello John, Hope you are doing well.",
              "wrap": true
            },
            {
              "type": "TextBlock",
              "text": "You have 10 pending approvals awaiting your decision for the past 2 days. Would you like to approve them?",
              "wrap": true
            },
            {
              "type": "ActionSet",
              "actions": [
                {
                  "type": "Action.Submit",
                  "title": "Show",
                  "data": {
                    "msteams": {
                      "type": "messageBack",
                      "title": "Show",
                      "displayText": "Show",
                      "value": "##reminders-###approvals-show 2",
                      "text": "##reminders-###approvals-show 9"
                    }
                  }
                },
                {
                  "type": "Action.Submit",
                  "title": "Approve Later",
                  "data": {
                    "msteams": {
                      "type": "messageBack",
                      "title": "Approve Later",
                      "displayText": "Approve Later",
                      "value": "##reminders-###approvals-approve-later",
                      "text": "##reminders-###approvals-approve-later"
                    }
                  }
                }
              ]
            }
          ],
          "msteams": {
            "width": "Full"
          }
        }
      }
    ]
  }
}
```

{% endcode %}
