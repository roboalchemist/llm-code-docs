# Source: https://docs.avaamo.com/user-guide/outreach/recipient-lists.md

# Recipient lists

A **Recipient list** consists of a list of users to whom the campaign message must be sent. You can quickly create and upload a recipient list on the **Outreach -> Recipient Lists** page.&#x20;

The following are some of the key features of the **Recipient Lists** section:

* Quickly upload a list of recipients in a simple CSV file.
* Flexible CSV format that can be used to create customized message templates.
* Reuse the same list for different campaigns.
* Build a separate list for a test run before launching the outreach program to the actual users.&#x20;

The Recipient list page displays a list of all the recipient lists created for the Outreach program in descending order of created or updated timestamp. Each column contains the following details:

* Recipient list name: Indicates the name of the recipient list provided at the time of creating the recipient list.
* Number of recipients: Indicates the number of recipients in the recipient list CSV.
* Updated on: Indicates the last updated timestamp of the recipient list. For a newly created recipient list, it indicates the created timestamp of the recipient list.
* Action: You can use options in the Actions column to [download](#avaamo-file-format), [delete](#delete-a-recipient-list) or [view the recipient list](#view-a-recipient-list)

## Create a new recipient list&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* See [Quick start](https://docs.avaamo.com/user-guide/outreach/quick-start), for a quick article on creating your first outreach program.
* Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new recipient list.
  {% endhint %}

You can create a recipient list is one of the following ways:

* [Upload file](#upload-file): Use this option, if you wish to directly upload a CSV file with a list of recipients.
* [SFTP](#sftp): Use this option, if you wish to pick the recipient list from an SFTP server of your choice. When a campaign is triggered, the latest file available in the SFTP server location is picked as a list of recipients.

{% hint style="success" %}
**Key point**: The recipient file must be in UTF-8 encoded CSV. See [Export to a UTF-8 encoded CSV](#export-to-a-utf-8-encoded-csv), for a few tips.&#x20;
{% endhint %}

### Upload file&#x20;

You can use the **Upload** **recipient list** option if you wish to directly upload a CSV file with a list of recipients.

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Recipient Lists** tab, and click **Create New Recipient List -> Upload** **recipient list** option. Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZVtA2ZtLPyxPm4dbmFO5%2F6.4-campaign-recipient-list.png?alt=media&#x26;token=2cdab0c0-8317-4c07-a0c7-c5d7ced66f12" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="189.44475920679886">Parameters</th><th width="385.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Recipient list name</td><td>Indicates the name of the recipient list. Provide a name that is easily identifiable to pick when you create a campaign.</td><td align="center">50 characters</td></tr><tr><td>File format</td><td><p>Choose a file format of the recipient CSV file.</p><ul><li>If you are uploading Avaamo-compliant CSV format, then see <a href="#avaamo-file-format">Avaamo file format</a>, for more information.</li><li>You can also select Custom as a file format and upload a CSV file in any custom format, say for example Epic integration system as a recipient list. See <a href="#custom-file-format">Custom file format,</a> for more information.</li></ul></td><td align="center">NA</td></tr><tr><td>Upload recipient list in CSV format</td><td><p>Click <strong>Browse</strong> to browse a CSV file with recipient details.</p><p></p><p>You can also click the <strong>Sample recipient file</strong> to download a sample recipient list file format. See <a href="#avaamo-file-format">Recipient list CSV format</a>, for more information.  </p></td><td align="center">NA</td></tr><tr><td>Test recipient list</td><td><p>Use this if you are creating a recipient list for a test run. </p><p></p><p>The test recipient lists are available in the Recipient list dropdown only when you wish to test the campaign. See <a href="campaigns/test-campaign">Test campaign</a>, for more information. In the </p></td><td align="center">NA</td></tr></tbody></table>

The newly created recipient list is displayed in the **Recipient Lists** tab.&#x20;

* In the Recipient Lists tab, a recipient list marked for testing is indicated with a test tube icon <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmGvSTdrZdzGAEm0QGGMV%2FScreenshot%202023-03-14%20at%205.40.39%20PM.png?alt=media&#x26;token=417d456e-0122-421c-bb62-9ee58b3c9511" alt="" data-size="line">, the recipient list not marked for testing is indicated with <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXLAz6CKU9lIOYLmf5gIa%2FScreenshot%202023-03-15%20at%2011.18.06%20AM.png?alt=media&#x26;token=61660e26-8d9f-47d5-8a5b-f69aca3b79f7" alt="" data-size="line"> icon.
* Click the recipient list to view the configurations specified for creating the recipient list.

### SFTP

{% hint style="success" %}
**Key point**: The SFTP file name must contain only letters and numbers without any spaces or special characters.
{% endhint %}

You can use the **SFTP** **connection** option if you wish to pick the recipient list from an SFTP server of your choice. When a campaign is triggered, the latest file available in the SFTP server location is picked as a list of recipients. This allows you to update the recipient file list continuously and the newest list is picked by the Platform when the campaign is triggered.

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Recipient Lists** tab, and click **Create New Recipient List -> Upload recipient list using SFTP** option. Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5ZrudlYrdtSDfLUFACyU%2F6.4-campaign-recipient-list-SFTP.png?alt=media&#x26;token=d157455c-afc5-4953-91e0-73ec72bd42c9" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="196.44475920679886">Parameters</th><th width="398.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Recipient list name</td><td>Indicates the name of the recipient list. Provide a name that is easily identifiable to pick when you create a campaign.</td><td align="center">50 characters</td></tr><tr><td>File format</td><td><p>Choose a file format of the recipient CSV file.</p><ul><li>If you are uploading Avaamo-compliant CSV format, then see <a href="#avaamo-file-format">Avaamo file format</a>, for more information.</li><li>You can also select Custom as a file format and upload a CSV file in any custom format, say for example Epic integration system as a recipient list. See <a href="#custom-file-format">Custom file format,</a> for more information.</li></ul></td><td align="center">NA</td></tr><tr><td>SFTP Host</td><td>Indicates the URL of the SFTP server.</td><td align="center">NA</td></tr><tr><td>Auth type</td><td><p>Indicates the auth type used by the SFTP server. Following auth types are supported: </p><ul><li>Basic: Specify the username and password for connecting to the SFTP server.</li><li>Keys: Specify the username and required <code>pem</code> key for connecting to the SFTP server. </li></ul></td><td align="center">NA</td></tr><tr><td>Test Connection</td><td>Use this button if you wish to test the connection for the SFTP server.</td><td align="center">NA</td></tr><tr><td>File path</td><td>Indicates the path of the recipient file from the SFTP server. </td><td align="center">NA</td></tr><tr><td>Test recipient list</td><td>Use this if you are creating a recipient list for a test run.</td><td align="center">NA</td></tr></tbody></table>

The newly created recipient list is displayed in the **Recipient Lists** tab.&#x20;

* In the **Recipient Lists** tab, the recipient list uploaded using SFTP is indicated using <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FyFOfjzTF7T8O0cRvn0AY%2FScreenshot%202023-03-15%20at%2011.19.33%20AM.png?alt=media&#x26;token=d4696fc3-c436-4fbf-b8ac-c3321056facf" alt="" data-size="line">icon.
* Click the recipient list to view the configurations specified for creating the recipient list.&#x20;

## Recipient list file format

You can upload a recipient list CSV in one of the following formats - Avaamo or Epic. Each row in the CSV file is a recipient to whom the campaign message is sent. See [Avaamo file format](#avaamo-file-format) and [Epic file format](#epic-file-format), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* The column headings in the recipient list CSV can be used as `${column_name}` to create a customized message. These are placeholder values in the message. When an SMS or voice message is sent to a specific recipient, the placeholders `${column_name}` in the message are replaced with the corresponding column value from the CSV file.&#x20;
* All the special characters in the column heading must be removed and space must be replaced with an underscore character when used in the campaign message. Example: If the CSV column heading has "Appointment Date", then in the message template it must be used as `${appointment_date}`.
  {% endhint %}

### Avaamo file format&#x20;

The following is the Avaamo file format of the recipient list CSV:

| Phone      | email      | <\<user\_info\_1>> | <\<user\_info\_2>> |
| ---------- | ---------- | ------------------ | ------------------ |
| <\<value>> | <\<value>> | <\<value>>         | <\<value>>         |

* Recipient information in the CSV file can contain details such as first name, email, last name, date, or time as per the scenario.&#x20;
* For `C-IVR and SMS delivery channels`, the only CSV column header that is mandatory is the **Phone** column.&#x20;
  * This is the number to which the campaign message is sent.&#x20;
  * For the C-IVR channel, the phone number format must be in the [E.164 format](https://www.itu.int/rec/T-REC-E.164/) (`- [+] [country code] [subscriber number including area code] and can have a maximum of fifteen digits`) in all cases.
  * For the SMS channel, it is recommended to specify the phone number in [E.164 format](https://www.itu.int/rec/T-REC-E.164/), except when the recipient's phone number is a national number. In such cases, only the `Subscriber number` without the country code is sufficient. For example, if the "from"  and "to" number of the campaign is from the US, then the "to" number which is the recipient number can be just the Subscriber number.

<table><thead><tr><th width="179">E.164 Format</th><th width="156">Country Code</th><th width="116">Country</th><th>Subscriber Number</th></tr></thead><tbody><tr><td>+1616555xxxx</td><td>1</td><td>US</td><td>616555xxxx</td></tr><tr><td>+44345183xxxx</td><td>44</td><td>GB</td><td>345183xxxx</td></tr><tr><td>+55115743xxxx</td><td>55</td><td>BR</td><td>115743xxxx</td></tr></tbody></table>

* For the `MS Teams delivery channel`, the only CSV column header that is mandatory is the **email** column.&#x20;
  * Ensure the email in the recipient list CSV is a part of the Azure directory for which the MS Teams channel is configured.&#x20;
  * You can find the details of the Azure directory of the MS Teams channel using the **Directory (Tenant) Id** in the MS Teams channel configuration page. See MS Teams, for more information.

The rest of the column headers in the recipient CSV file can be any user information that you wish to include for each recipient.&#x20;

**Example:**

<table><thead><tr><th width="177">Phone</th><th width="207">email</th><th>First name</th><th>Last name</th></tr></thead><tbody><tr><td>+1556xxxx234</td><td>john@abccorp.com</td><td>John</td><td>Miller</td></tr><tr><td>+1678xxxx234</td><td>mark@abccorp.com</td><td>Mark</td><td>Smith</td></tr></tbody></table>

**Message template**:

{% code overflow="wrap" %}

```markup
Dear ${first_name} ${last_name},

Flu season is back again this time of the year. The Sparsh care center is organizing a free Flu vaccination drive on October 1st and October 2nd from 10 AM to 6 PM. Visit your nearest Sparsh Care Center to get vaccinated. 

Best regards,
Sparsh care center team
```

{% endcode %}

When the message is sent to a recipient number, the placeholder values in the template are replaced with actual values corresponding to the number.

{% code overflow="wrap" %}

```
Dear John Miller,

Flu season is back again this time of the year. The Sparsh care center is organizing a free Flu vaccination drive on October 1st and October 2nd from 10 AM to 6 PM. Visit your nearest Sparsh Care Center to get vaccinated. 

Best regards,
Sparsh care center team
```

{% endcode %}

See [Templates](https://docs.avaamo.com/user-guide/outreach/templates), for more example&#x73;**.**

### **Custom file format**

Avaamo Conversational AI Platform allows you to upload a custom recipient CSV file with customized column headers based on your business requirement. Unlike Avaamos-specific recipient file format where either phone or email column header is mandatory, the custom file format allows you the flexibility to upload CSV from any external system without any mandatory column requirement. Later, the mapping of the column headers from the recipient list CSV to the actual column to be used for delivering the campaign message can be done while configuring the campaign. See [Select phone header](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#select-phone-header) and [Select email header](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#select-email-header), for more information.

For example, A custom recipient CSV file can have the following columns - Name, Email, Official Email, Preferred phone number, Mobile phone number, Home number, DOB, and many other columns. Say that you are using the SMS channel to deliver the campaign and you wish to send an SMS to the number in the `Preferred phone number` column. You can map this header in the [Select phone header ](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#select-phone-header)dropdown while configuring the campaign. When the campaign is executed, the numbers in the `Preferred phone number` column is picked for delivering the campaign message.&#x20;

**Example of the Custom file format: Epic file format**

Epic enables the secure flow of patient data between Epic sites and exchange-capable systems. You can automate Epic integration with the Outreach feature in the Avaamo Platform to consume the patient data and send a campaign message to the list of recipients obtained from the Epic API seamlessly.&#x20;

Epic formats are company specific and can vary. The Avaamo platform provides flexibility to upload any Epic format, however, do note the following points to enable Epic integration with the Outreach feature in the Avaamo platform.

* If `Authorised SMS` column is available, then the value in the `Authorised SMS` column is considered before sharing the campaign message. In such cases, the campaign message is sent only when `Authorised SMS` column is `Yes`. If `Authorised SMS` column is not available, then the campaign message is sent to all the users in the file.
* A suggested way to automate the integration is to build an automated script for extracting patient data from the Epic integration and drop it to an SFTP location periodically.&#x20;
* Configure the SFTP details in the Outreach -> Recipient lists -> SFTP page. See [SFTP](#sftp), for more information.
* You can continue to extract and update the same file from the Epic sites to the SFTP location and the Avaamo Platform picks the latest file when the campaign is triggered.

Epic enables the secure flow of patient data between Epic sites and exchange-capable systems. You can automate Epic integration with the Outreach feature in the Avaamo Platform to consume the patient data and send a campaign message to the list of recipients obtained from the Epic API seamlessly.&#x20;

## **Download recipient list**

* In the **Outreach ->** **Recipient Lists** tab, click three ellipse dots in the **Actions** column of the recipient list to view the extended menu and click **Download.**&#x20;
* A copy of the recipient CSV file is downloaded to your local machine.&#x20;

## **Search recipient list**

In the **Outreach ->** **Recipient Lists** tab, start entering the text in the **Search** text box and press the **Enter** key or click the **Search** icon. The results are filtered and displayed based on the text entered in the **Search** text box.

## **View a recipient list**

In the **Outreach ->** **Recipient Lists** tab, click three ellipse dots in the **Actions** column of the recipient list to view the extended menu, and click **View** to view the recipient list setup details.&#x20;

You can also click the recipient list name to view the recipient list setup details.

## **Delete recipient list**

* In the **Outreach ->** **Recipient Lists** tab, click three ellipse dots in the **Actions** column of the recipient list to view the extended menu and click **Delete.**&#x20;
* Click **OK** in the confirmation message to delete the recipient list.

{% hint style="info" %}
**Note**: You can delete a recipient list only when it is not associated with any campaign.
{% endhint %}
