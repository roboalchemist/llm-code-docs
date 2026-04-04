# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-g-suite.md

# SAML Support- G Suite

G Suite is a package of cloud-based services that can provide your company or school with a whole new way to work together online—not just using email and chat, but over video conferences, social media, real-time document collaboration, and more.

\
A user can use their G Suite credentials to sign in to enterprise cloud applications via Single Sign-On (SSO). An identity and access management (IAM) service provide its administrators with a single place to manage all users and cloud applications. You don't have to manage individual user IDs and passwords tied to individual cloud applications for each of your users. An IAM service provides your users with a unified sign-on across all their enterprise cloud applications.

This page describes how to add Avaamo dashboard to G Suite and configure SSO-support with SAML 2.0.

{% hint style="info" %}
**Note**: This page reflects a 3rd party’s application which may change. If the steps described here do not match what you see in your G Suite account, you can use the generic Avaamo dashboard SAML documentation, along with the IdP’s documentation.
{% endhint %}

### Setup G Suite Account

To setup, your G Suite account for SAML support, follow the steps below:

* Login to your admin.google.com account using your G Suite account credentials.
* Select Apps on the main page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LygnlpHVHiRiJW5_6P0%2F-Lygsuirq1TZ4WpcC0Bt%2Fgsuite-sso-1.png?alt=media\&token=ec481b88-55eb-4481-a597-c3fe46f6bbdc)

* Select SAML apps

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh-W6nEgPm7YE-z8EB%2Fgsuite-sso-2.png?alt=media\&token=335ccac0-fb4e-4d59-895f-d2fe10abc842)

* Create a new application. Click on the “+” button or “ SETUP MY OWN CUSTOM APP”.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh-b6thD52vLQxLCl7%2Fgsuite-sso-3.png?alt=media&#x26;token=a0600780-f545-4eee-8e73-83def9528ec7" alt=""></div>

* Download Certificate or IDP Metadata, save SSO URL.\
  Use notepad to open certificate or Metadata file, save lines starting from -----BEGIN CERTIFICATE----- to -----END CERTIFICATE-----.This information will be used for the Avaamo dashboard SAML configuration.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh0-HOmMWaxxbRgS9Y%2Fgsuite-sso-4.png?alt=media&#x26;token=2df4746a-fbfa-4705-8dfe-98eef8f0a07e" alt=""></div>

* Enter the Application Name. For example, the Avaamo dashboard.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh05SumiTRU_Rg9hif%2Fgsuite-sso-5.png?alt=media&#x26;token=5199d2c0-e190-4894-be6d-13b9357a5aba" alt=""></div>

* Enter the details for:

  ```
   ACS URL  - *https://cXX.avaamo.com/dashboard_user/users/saml/sign_in*
   Entity ID -     <*clients G-suite Entity ID*> 
  ```

  Enable Signed Response, select Name ID Format

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh0EuBqtpuz12CgEii%2Fgsuite-sso-6.png?alt=media&#x26;token=1734c64b-48da-45c4-8f89-25445b98152b" alt=""></div>

* Add new mapping for User.email.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh0KGzr8q5b27eAvkt%2Fgsuite-sso-7.png?alt=media&#x26;token=88c22548-e5d7-4d07-8871-5a99f4100777" alt=""></div>

* Click on Finish. And OK on the popup window.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh0PcIJ2eqZBGKp3eY%2Fgsuite-sso-8.png?alt=media&#x26;token=86b444b1-52dc-4771-994c-bf19fbf1a36a" alt=""></div>

* Enable Avaamo Dashboard application for All users.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh-SMY_O7NwfZ3eBKa%2F-Lyh0Wm5Gu48-TAPT4Ho%2Fgsuite-sso-9.png?alt=media&#x26;token=6d263de2-4f3b-4b24-8dd4-09b164cf9113" alt=""></div>

* Users with access to any of the web pages on your Avaamo Dashboard server will be redirected to Google G Suite authentication.

### Avaamo Admin SAML Integration

* Open a new Chrome browser window, and enter cx.avaamo.com(cx is the platform assigned to you).
* Login with your admin credentials. On the Avaamo dashboard, click on the action over the button (the three dots) for the menu bar. Select Settings.
* On the settings page click on **Identity Providers** and click on the Add New button.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LygnlpHVHiRiJW5_6P0%2F-LygqeWXPqZ1i06G9st-%2Fgsuite-sso.png?alt=media&#x26;token=3101fef4-f12d-4cbc-a8e4-1b9473a47be5" alt=""></div>

* On the New Identity Provider popup window, set the value of **Authentication Identity Provider** (Optional) to ‘G-suite’ and submit to save your configuration.
  * **Identity Provider Name:** A unique identity provider name for your identification. This name will be displayed in the drop-down list when you are selecting an identity provider for your dashboard users while either creating a new user or editing an existing one. For example, Microsoft Azure, G-Suite, Okta, etc..
  * **App Id / Entity Id**: This Id must exactly match the Entity Id that you have used while configuring single sign-on with your application in the Basic SAML Configuration section on G Suite.
  * **Single Sign-On URL**: Copy the Login URL from SAML Signing Certificate Section from your application configuration on G Suite and paste it in this section.
  * **Certificate Signature:** Download the raw certificate from ​SAML Signing Certificate ​Section from your app configuration on G Suite and upload it here.

Now the ‘G-suite’ configured user tries to login to [https://cXX.avaamo.com/#/](https://cxx.avaamo.com/#/) with client email and the user will not be prompted for an OTP.
