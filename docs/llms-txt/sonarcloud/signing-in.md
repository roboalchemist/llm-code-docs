# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/signing-in.md

# Signing in to SonarQube Cloud

You may sign in to SonarQube Cloud [via your DevOps platform service](https://www.sonarsource.com/trust-center/#authentication) (GitHub, Bitbucket, GitLab, or Azure DevOps) or, if the Single Sign-On (SSO) authentication is set up in your enterprise, through SSO. There is no such thing as a SonarQube Cloud-only account.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-0101a27595b3eeaa1f6bff3453246157398ed4d7%2F48b9234a75a7e590b02bb72eb21408dc44925c0c.png?alt=media" alt="Sign up to SonarQube Cloud using either your DevOps service or with SSO if SAML authentication is set up for your Enterprise."><figcaption></figcaption></figure></div>

{% hint style="info" %}
SonarQube Cloud doesn’t simultaneously support two accounts with the same email address. If you already have a SonarQube Cloud account and want to sign in to SonarQube Cloud with another DevOps platform account associated with the same email address, SonarQube Cloud will warn you that doing so will dissociate your first account from SonarQube Cloud (Signing in again with this account will re-associate it).
{% endhint %}

{% hint style="info" %}
If you no longer have access to the DevOps platform account or associated e-mail address that was used to sign in to SonarQube Cloud, you will not be able to restore your account and will have to create a new one.
{% endhint %}

### Signing in via your DevOps platform service <a href="#via-devops-platform" id="via-devops-platform"></a>

When you sign in for the first time, your SonarQube Cloud account is created and bound to your account on the DevOps platform.

#### Prerequisites for your DevOps account's email address

To use all the features of SonarQube Cloud, the email address in your DevOps account must be verified. If it’s not the case, you’ll face the inability to join an organization, be assigned issues, receive notifications, or import an organization.

For Azure DevOps users:

* SonarQube Cloud considers an email address as verified if its domain has been verified in Microsoft Entra ID.
* If it’s not the case, a one-time email address verification is required. SonarQube Cloud provides guidance through this email verification process during your initial sign-up.

For other users, check your DevOps platform’s documentation for email verification steps. For GitHub users, see [Verifying your email address](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address#verifying-your-email-address).

#### Signing in

To sign in to SonarQube Cloud via your DevOps platform service:

1. Go to <https://sonarcloud.io/login>. The SonarQube Cloud login page is displayed.
2. Select your DevOps platform. You’re redirected to your DevOps platform login page.
3. Enter your existing credentials on that DevOps platform service.

### Signing in with SSO <a href="#with-sso" id="with-sso"></a>

If single sign-on (SSO) has been set up for your SonarQube Cloud enterprise, you can log in to SonarQube Cloud with SSO. In most cases, your administrator has shared an SSO link with you. If not, you can log in from the main login page, but you need to know the key that identifies your enterprise in SonarQube Cloud. See [setting-up-sso](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-sso "mention") for additional information.

{% hint style="info" %}
In systems using SAML SSO, a one-time email address verification is required. SonarQube Cloud provides guidance through this email verification process during your initial sign-up (or during sign-in if your account existed before this feature implementation).
{% endhint %}

#### With the SSO login link <a href="#with-the-sso-login-link" id="with-the-sso-login-link"></a>

1. Select the SSO login link sent to you by your administrator. The **Log in with SSO** page is displayed and your organization key is prefilled (the key that identifies your organization in SonarQube Cloud).
2. Bookmark the link for future logins.
3. Select **Log in**.

#### From the main login page <a href="#from-the-main-login-page" id="from-the-main-login-page"></a>

1. Go to <https://sonarcloud.io/login>. The SonarQube Cloud login page is displayed.
2. Select **Log in with SSO**. The **Log in with SSO** dialog is displayed
3. Enter your enterprise key and select the **Log in** button.

### Signing out <a href="#signing-out" id="signing-out"></a>

To sign out from SonarQube Cloud:

1. Select your account menu in the top right corner of the SonarQube Cloud interface.
2. In the menu, select **Log out**.
