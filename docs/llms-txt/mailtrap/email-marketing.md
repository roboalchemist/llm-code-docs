# Source: https://docs.mailtrap.io/getting-started/email-marketing.md

# Email Marketing

Make sure you've added and [verified a domain](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain), or you won't be able to send a campaign.

### How to set up and send a campaign

{% stepper %}
{% step %}
Go to **Email Marketing** and click **Create New Campaign**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e78333259c0895cb79f8191c0ee30ff6a54e96d1%2Fmarketing-campaign-create-button.png?alt=media" alt="Email Marketing page with Create New Campaign button" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Fill out the form with your company details, such as name, address, city, zip code, and country. Optionally, enter your company's phone number and link to the website. Click **Continue**.

{% hint style="info" %}
This information will be added to email footers to ensure compliance with existing regulations. You'll only have to complete this step once when creating your first campaign.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fe2f916144c632bbca566ba05fd0e30e9b041ac6%2Fmarketing-campaign-company-details.png?alt=media" alt="Company details form for campaign compliance" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Choose a domain from the **Select domain** dropdown, then set the **Campaign name**, **Subject**, and **From** email address. Optionally, set the From name, Reply-To name, and Reply-To email. If you have only one domain, no need to choose anything, it's selected for you by default. Click **Continue**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-7438e739ed4d440af44bdd34f4db7be4c157acc4%2Fmarketing-campaign-settings.png?alt=media" alt="Campaign details form with domain, name, subject, and email settings" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
You'll be taken to the Design step, where you can choose between Drag & Drop and HTML editors. If you have templates stored, you'll see them here. You can use them in your campaigns. Read more about creating templates [here](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-templates.md).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a39b2f1f77325f288af5dd1d98e02701be96b2ef%2Ftemplate-design-selection.png?alt=media" alt="Template selection page with Drag &#x26; Drop and HTML editors" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Create your campaign design, click **Save**, and then **Continue**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c8be19e87f8d68f7965da6b5b11e176692580cf6%2Fmarketing-campaign-design-editor.png?alt=media" alt="Drag and drop email editor interface" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Instead of continuing to the next step, you can click **Send Test** to send a test to one email address to check the design in your email client or click **Finish Later** to return to the campaign **Details**, where you can change any of the parameters you set in previous steps.
{% endhint %}
{% endstep %}

{% step %}
If you've already imported your contacts, select your audience by including or excluding specific lists. Then, click **Confirm Audience**.

{% hint style="success" %}
With **Including** and **Excluding** features, you can easily send campaigns to specific audience groups only.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5e05b425a2dbc0bc7fa105c60b3a02004dd3ecc0%2Fgetting-started-audience-selection.png?alt=media" alt="Audience selection with including and excluding lists" width="563"><figcaption></figcaption></figure></div>

{% hint style="warning" %}
If you didn't upload your contacts before creating a campaign, you'll be prompted to import contacts at this stage. Simply click **Import Contacts** and follow the steps ([refer to this section](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/contacts.md#how-to-upload-contacts-nag8y) in our Contacts guide for more details). **Important**: you should create Fields beforehand to be able to assign variables to the fields (map fields) when importing contacts.
{% endhint %}
{% endstep %}

{% step %}
At this point, you can click **Send Test** to send a test email to one email address, choose **Send now** to send the campaign immediately, or select **Schedule campaign** to send it at a specific date and time.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ad90c58a55bc9f563f5d29c31c02bbb1d6b4bf3e%2Fmarketing-campaign-send-options.png?alt=media" alt="Send and schedule campaign options" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
To schedule the campaign, click **Schedule Campaign**, select the date, and choose the time. Then, confirm the action by clicking **Schedule Sending**.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9c32b4843af03eee725633fa8eeeabc38f45fbb1%2Fmarketing-campaign-schedule-form.png?alt=media" alt="Schedule campaign form with date and time picker" width="375"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### What's next?

Once your campaign has been sent, you can check the campaign deliverability data and stats. Here's how to do it:

{% stepper %}
{% step %}
Click **Email Marketing** in the left navigation panel and you'll have a quick preview of all the campaign data. If we're still collecting the data, you'll be notified accordingly.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-96be0e0862d333dd58e722c7c64504714e9c596c%2Fmarketing-campaign-list-view.png?alt=media" alt="Campaign sent confirmation messages" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
If you want more details for a particular campaign, click the campaign name, then select the **Reports** tab where you'll see the full [Statistics report](https://docs.mailtrap.io/email-marketing/campaigns/statistics).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-56ae57c22ff2e41fd60d52b78f5af2a4e444a81b%2Fmarketing-campaign-statistics.png?alt=media" alt="Campaign statistics report showing delivery rates, opens, clicks, and mailbox provider breakdown" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}
