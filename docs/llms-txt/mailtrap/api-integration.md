# Source: https://docs.mailtrap.io/email-api-smtp/setup/api-integration.md

# API Integration

Use API credentials to integrate Mailtrap with your project.

{% stepper %}
{% step %}
Go to the **Sending Domains** tab and choose the domain you want to send emails from. Remember that you'll be able to start sending emails once the domain is verified.
{% endstep %}

{% step %}
Navigate to the **Integration** tab for your selected domain.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c770f21d61dc676fb576e19fabf81671cb5b5a8c%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click the **Integrate** button under **Transactional Stream** or **Bulk Stream**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-bb2ed533ad8282eddc4bfd9aa9d575249205e9ac%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

**Transactional Stream** is used to send automated, non-promotional application emails triggered by the specific user action.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-eef39a1323370d004e69c4c9686f291f06ca942f%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

**Bulk Stream** is used to send a single marketing campaign to a large group of recipients in bulk.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4deee87f494c19629c1f76a859bb83eb47a66c27%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Toggle the switch to **API**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e5bc6fe628c677dfb1012313d9f2232f6564d4a5%2Fapi-integration-credentials-streams.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Build the authenticated HTTP request in your programming language or framework and configure it with **Mailtrap Host** and **API Token**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-277ed4a03452a3091f2067afa8e3078df3030ed6%2Fapi-integration-credentials-transactional.png?alt=media" alt="Transactional Stream API credentials showing Host and API Token" width="563"><figcaption><p>Transactional Stream API credentials</p></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-60ba1ceace0286cee9131e3d55845680d4d5e20e%2Fapi-integration-credentials-bulk.png?alt=media" alt="Bulk Stream API credentials showing Host and API Token" width="563"><figcaption><p>Bulk Stream API credentials</p></figcaption></figure></div>

Alternatively, choose the programming language or framework from the menu under **Code Samples** and copy the sample configuration already containing your credentials. In this menu, you'll find official SDKs for [PHP](https://github.com/railsware/mailtrap-php), [Python](https://github.com/railsware/mailtrap-python), [Ruby](https://github.com/railsware/mailtrap-ruby), and [Node.js](https://github.com/railsware/mailtrap-nodejs).

{% hint style="info" %}
Note: For now, only Ruby, PHP (Laravel + Symfony), and Node.js SDKs support Bulk Stream, but others are in development. Request and response examples are also available [here](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/67f1d70aeb62c-send-email-including-templates).
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a39d965f764098a681859256d7e0f8967b9f60a6%2Fapi-integration-code-samples-transactional.png?alt=media" alt="Code Samples dropdown showing programming languages including cURL, C++, C#, Go, Java, Node.js, Ruby, Python, and PHP" width="563"><figcaption><p>Transactional Stream code samples</p></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b415435c884d7847b7cd3079864ce33fdf1d75e7%2Fapi-integration-code-samples-bulk.png?alt=media" alt="Code Samples dropdown for Bulk Stream showing available programming languages and frameworks" width="563"><figcaption><p>Bulk Stream code samples</p></figcaption></figure></div>
{% endstep %}

{% step %}
Complete your script and run it. If you did everything correctly, you should find the sent email in the inbox of the email address you indicated in the script. The email will also appear in **Email Logs** in Mailtrap.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d64cbccae97e40d1548f8f93468528e98d31d9f7%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

Remember that each domain has different API tokens that you can always access by clicking on the desired domain and going to the **Integration** tab.

You can also create additional API tokens by going to **Settings** → **API Tokens** and clicking **Add Token**.

<a href="api-tokens" class="button primary" data-icon="magnifying-glass">Learn more about API Tokens</a>

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>

Mailtrap Email Sending API supports:

* attachments
* [email templates](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-sandbox/email-marketing/email-templates.md)
* [custom variables](https://docs.mailtrap.io/email-api-smtp/advanced/custom-variables)
* [email categories](https://docs.mailtrap.io/email-api-smtp/analytics/categories)

{% hint style="info" %}
If you need any help with API integration, please, contact our support team at <support@mailtrap.io>.
{% endhint %}
