# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/publishing-documentation/authenticated-access/setting-up-okta.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/authenticated-access/setting-up-okta.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/authenticated-access/setting-up-okta.md

# Source: https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-okta.md

# Setting up Okta

{% hint style="warning" %}
This guide takes you through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through the process of [enabling authenticated access](https://gitbook.com/docs/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

To setup your GitBook site with authenticated access using Okta, the process looks as follows:

{% stepper %}
{% step %}
**Create a new Okta application**

Create an Okta application from your Okta dashboard.
{% endstep %}

{% step %}
**Install and configure the Okta integration**

Install the Okta integration and add the required configuration.
{% endstep %}

{% step %}
**Configure Okta for adaptive content (optional)**

Configure Okta to work with adaptive content in GitBook.
{% endstep %}
{% endstepper %}

### Create a new Okta application

First, sign in to Okta platform (the admin version) and create a new app integration (or use an existing one) by clicking the Applications button in the left sidebar.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8roQ3QDR5zsyFh2FoQS4%2FScreen%20Shot%202023-10-30%20at%201.32.55%20PM.png?alt=media&#x26;token=dc46f9f6-ec54-456f-ba7b-397477089e1a" alt="An Okta screenshot showing the create app integration screen"><figcaption></figcaption></figure>

Click Create App Integration and select OIDC - OpenID Connect as the Sign-In method. And then select Web Application as the application type.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FqgFHYo6HOUGF8dUTFEJM%2FScreen%20Shot%202023-10-30%20at%201.39.15%20PM.png?alt=media&#x26;token=0ac8e337-6082-4a28-b3df-33fa4e33dc0d" alt="An Okta screenshot showing the integration setup"><figcaption></figcaption></figure>

Name it appropriately and don't edit any other setting on that page. For assignments, choose the appropriate checkbox. Click Save.

On the next screen, copy Client ID and Client Secret. Copy the Okta Domain right below your email address by clicking the dropdown in the top right.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FJQWvrITuUlno737DbQKM%2FScreen%20Shot%202023-10-30%20at%204.52.14%20PM.png?alt=media&#x26;token=82a63cfd-a1e6-4666-b132-30fc98e95c22" alt="An Okta screenshot showing where to copy client credentials"><figcaption></figcaption></figure>

We will need these values to configure the Okta Integration.

### Install and configure the Okta integration

Navigate to the Integrations tab in the site you want to publish and locate the Okta integration.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FeFArORtsvAcvgwbDZNce%2FScreen%20Shot%202024-12-13%20at%203.21.30%20PM.png?alt=media&#x26;token=199acbf6-3100-49af-886e-d2d09445f978" alt="A GitBook screenshot showing the site settings page"><figcaption></figcaption></figure>

Install the integration on your site.

Upon installation on site, you will see a screen asking you enter the Client ID, Okta Domain, and Client Secret.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHrwQ0ASv1tD6kTZPVLMY%2FScreen%20Shot%202024-12-13%20at%203.34.37%20PM.png?alt=media&#x26;token=0844c1db-14b8-415c-8d51-33d4618e900e" alt="A GitBook screenshot showing the Okta credentials modal"><figcaption></figcaption></figure>

For Client ID, Okta Domain (remove `https://`prefix, if any) and Client Secret, paste in the value you copied from Okta Dashboard.

Click Save.

Copy the URL displayed in the modal and enter it as a Sign-In redirect URI in Okta (as shown in the below screenshot). Hit Save.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FpPZlqJlE6koyHrWhSp8i%2FScreen%20Shot%202024-01-14%20at%207.55.08%20PM.png?alt=media&#x26;token=99abc690-c82b-4974-9b5a-7ba6fbd11ed2" alt="An Okta screenshot showing the sign-in redirect URI configuration"><figcaption></figcaption></figure>

Now, in GitBook, close the integrations modal and click on the Manage site button. Navigate to **Audience**, select **Authenticated access**, and choose Okta as the backend. Then, click **Update audience**. Go to the site’s screen and click **Publish**.\
\
The site is now published behind authenticated access controlled by your Auth0 application. To try it out, click on Visit. You will be asked to sign in with Okta, which confirms that your site is published behind authenticated access using Auth0.

### Configure Okta for adaptive content (optional)

To enable Adaptive Content in your GitBook site with authenticated access, you’ll need to configure your Okta application to include relevant user data as claims in the authentication token.

Claims are key-value pairs embedded in the token sent to GitBook. These claims can be used to dynamically tailor documentation based on the user’s role, plan, location, or any other identifying attribute.

Okta supports multiple types of claims:

* **Standard Claims**\
  These are common claims (like `email`, `name`, or `groups`) that may be included by default but often need to be explicitly added to your token configuration for consistent availability.
* **Custom Claims**\
  You can define custom claims in Okta using [custom user attributes](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-add-custom-user-attributes.htm) or expression-based logic. These allow you to pass highly specific values—like plan tier, account ID, or internal team flags.
* **Groups as Claims**\
  You can also pass Okta groups as claims, which is especially useful when defining audience segments like “enterprise users” or “beta testers.” These can be filtered and mapped in your authorization server’s claim configuration.

To add or customize claims in Okta:

1. Open your Okta Admin Console.
2. Navigate to **Security > API > Authorization Servers**.
3. Edit the authorization server used for your GitBook site.
4. Under the **Claims** tab, add rules to include the desired claims in the token.
5. Make sure your GitBook site is reading and mapping those claims correctly.

Once claims are being passed into GitBook, follow the steps in [Adapting your content](https://gitbook.com/docs/publishing-documentation/adaptive-content/adapting-your-content) to define what content should be shown to whom.
