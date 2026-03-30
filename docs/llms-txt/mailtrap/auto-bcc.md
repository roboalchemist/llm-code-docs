# Source: https://docs.mailtrap.io/email-api-smtp/advanced/auto-bcc.md

# Auto BCC

### How to set up Auto BCC

{% stepper %}
{% step %}
Go to **Sending Domains** and choose the domain you want to set up Auto BCC for.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-05532a096d2941cef62f874aa17ed1ec5bbedb9f%2Fauto-bcc-sending-domains-list.png?alt=media" alt="Sending Domains page showing list of verified domains with domains highlighted" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Navigate to the **Auto BCC** tab.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-85aed464b5ab611501e8a37b20e0b1f3263eac6d%2Fauto-bcc-tab.png?alt=media" alt="Domain page showing Auto BCC tab highlighted by red arrow" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Enter an email address that will be included as BCC in all the emails you send from this domain and click **Add Email**.

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-241fd324619c429bd0bf5813f7ef921f44ce186d%2Fauto-bcc-add-email.png?alt=media" alt="Auto BCC page with email input field and Add Email button highlighted by red arrow" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Optionally, specify a custom X-header that will be included in emails to BCC recipients. Enter the Name and Value, and click **Add Header**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4231db79febbaa273437142bd8578c3193f4d12c%2Fauto-bcc-add-header.png?alt=media" alt="Custom Headers section with Name and Value fields and Add Header button highlighted by red arrow" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
To delete the email address or a custom header, click the trash bin icon and confirm the action by clicking **Delete**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-060445e232eb255ee8bf63ecb2bcaa59e9b16486%2Fauto-bcc-delete-confirmation.png?alt=media" alt="Auto BCC page showing email with trash icon and delete confirmation dialog with Delete button highlighted" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Important notes

* You can add multiple BCC email addresses, and all of them will receive email copies;
* You can’t use Auto BCC with a demo domain;
* Using this feature will increase your usage. Each email copy sent will count against your quota or overage calculation.
