# Source: https://docs.mailtrap.io/email-api-smtp/help/troubleshooting/unauthorized-401-error.md

# 401 Unauthorized Error

If you're getting an "Unauthorised" error (401 code) when trying to send emails, there are several possible causes and solutions.

### Common Causes

**1. Sending from Unverified Domain**

Make sure you're sending from the domain that you've set up and verified in Mailtrap. Using any other domain will result in this error.

{% hint style="danger" %}
If you verified `example.com`, you can only send from `*@example.com` addresses. Attempting to send from `otherdomain.com` will fail with a 401 error.
{% endhint %}

**2. API Token Permissions**

If you've configured a custom API token for your domain, make sure it has proper permissions to send emails.

Check your [API tokens](https://mailtrap.io/api-tokens) and verify the token has:

* Email sending permissions
* Access to the correct domain
* Valid expiration date (if applicable)

**3. Incorrect Credentials**

Make sure you're using the correct SMTP/API credentials provided in the Integration tab of your domain.

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-2caae3c1dba9c159c8b60f02ce10b2620f155f8d%2Ftroubleshoot-sending-credentials-both-streams.png?alt=media" alt="Integration tab showing SMTP and API credentials for both Transactional Stream and Bulk Stream in Mailtrap"><figcaption><p>SMTP and API credentials in Integration tab</p></figcaption></figure></div>

### How to Fix

{% stepper %}
{% step %}
**Verify Your Domain**

1. Go to [Sending Domains](https://mailtrap.io/sending/domains)
2. Ensure your domain shows the **Verified** badge
3. If not verified, complete the DNS record setup
   {% endstep %}

{% step %}
**Check API Token (if using custom tokens)**

1. Go to [API Tokens](https://mailtrap.io/api-tokens)
2. Verify the token has **Send Email** permissions
3. Ensure it's assigned to the correct domain
4. Check that the token hasn't expired
   {% endstep %}

{% step %}
**Verify Credentials**

Navigate to: **Sending Domains > Integration > Integrate** (under Transactional or Bulk Stream)

Copy the exact credentials shown there:

* For SMTP: Username and Password
* For API: API Token

Replace your current credentials with these values.
{% endstep %}

{% step %}
**Test with cURL**

Use the cURL code example to test if the error persists:

1. Go to **Sending Domains > Integration > Integrate**
2. Select your stream (Transactional or Bulk)
3. Go to **Code Samples > cURL**
4. Copy and run the cURL command

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b7c7048f01d78409e4c08a9306434233329e62ef%2Ftroubleshoot-sending-code-samples.png?alt=media" alt="Code Samples section in Mailtrap showing cURL integration example" width="563"><figcaption><p>Code Samples section with cURL example</p></figcaption></figure></div>

If the cURL test succeeds but your application fails, the issue is with your application's configuration.
{% endstep %}
{% endstepper %}

### Still Having Issues?

If you've verified all the above and still getting 401 errors:

* Double-check that your FROM address domain matches your verified domain
* Ensure there are no extra spaces or special characters in your credentials
* Contact support at <support@mailtrap.io> with:
  * Your domain name
  * The exact error message
  * A code sample showing how you're attempting to send

### Related Articles

* [Sending Domain Setup](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain)
* [API Integration](https://docs.mailtrap.io/email-api-smtp/setup/api-integration)
* [SMTP Integration](https://docs.mailtrap.io/email-api-smtp/setup/smtp-integration)
* [Sending from Domain Not Allowed](https://docs.mailtrap.io/email-api-smtp/help/troubleshooting/sending-from-domain-not-allowed)
