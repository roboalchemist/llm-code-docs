# Source: https://docs.mailtrap.io/email-api-smtp/email-templates/integration.md

# Integration

### Overview

Once you've created and customized your email template, you can integrate it with your application using the Email API or SMTP. This guide shows you how to get the necessary credentials and code samples to send emails using your templates.

### Integration steps

{% stepper %}
{% step %}
Navigate to Templates in the menu on the left.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d4b58986a09646ee33096aceec07e1af772c471a%2Ftemplate-menu-nav.png?alt=media" alt="Mailtrap sidebar menu with Templates menu item highlighted by red arrow" width="375"><figcaption><p>Templates in navigation menu</p></figcaption></figure></div>
{% endstep %}

{% step %}
Click the template you want to call using the API.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8e27873c5eca3dc3ff209d4d535f0f20a9f73e9a%2Ftemplate-list-view.png?alt=media" alt="Templates list showing Newsletter template highlighted by red arrow" width="563"><figcaption><p>Select template from list</p></figcaption></figure></div>
{% endstep %}

{% step %}
Open the Integration tab.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-297f15ee561555c6f584050e24c7d81749233721%2Ftemplate-integration-tab.png?alt=media" alt="Template page showing Details and Integration tabs with Integration tab highlighted by red arrow" width="563"><figcaption><p>Open Integration tab</p></figcaption></figure></div>
{% endstep %}

{% step %}
With Email API/SMTP toggled on, click Integrate under Transactional Stream or Bulk Stream.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-de8c7136039e15eb13f39177eac503126e90dee7%2Ftemplate-stream-options.png?alt=media" alt="Integration page showing Transactional Stream and Bulk Stream options with Integrate buttons highlighted by red arrows" width="375"><figcaption><p>Choose stream type and click Integrate</p></figcaption></figure></div>
{% endstep %}

{% step %}
Copy the necessary credentials such as Host, API Token, and Template UUID.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-277ed4a03452a3091f2067afa8e3078df3030ed6%2Fapi-integration-credentials-transactional.png?alt=media" alt="Transactional Stream API credentials box showing Host, API Token, and Template UUID" width="375"><figcaption><p>Transactional Stream API credentials</p></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-60ba1ceace0286cee9131e3d55845680d4d5e20e%2Fapi-integration-credentials-bulk.png?alt=media" alt="Bulk Stream API credentials box showing Host, API Token, and Template UUID" width="375"><figcaption><p>Bulk Stream API credentials</p></figcaption></figure></div>
{% endstep %}

{% step %}
Alternatively, under Code Samples, choose the desired language and copy the sample configuration already containing the necessary credentials. Mailtrap's official SDKs ([Node.js](https://github.com/railsware/mailtrap-nodejs), [Python](https://github.com/railsware/mailtrap-python), [PHP](https://github.com/railsware/mailtrap-php), and [Ruby](https://github.com/railsware/mailtrap-ruby)) also support the templates feature.
{% endstep %}

{% step %}
Paste the code into your project and customize it if needed. Then, run the code to send an email to the email address you indicated in your script.

For more details, [open the API docs](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/5tjdeg9545058-mailtrap-api) and go to Email Sending API → Emails → Send email (including template) for transactional stream and Bulk Sending API → Emails → Send email (including template) for bulk stream. Under Body, click the dropdown menu, and choose `EmailFromTemplate`.
{% endstep %}
{% endstepper %}
