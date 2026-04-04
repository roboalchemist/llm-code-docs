# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/multi-factor-authentication-mfa-settings.md

# Multi-Factor Authentication (MFA) Settings

This article covers how system users can enable Multi-Factor Authentication to log in to the platform more securely.

## What is Multi-Factor Authentication

Multi-factor Authentication (MFA) is an authentication method that requires the user to provide two or more verification factors to gain access to the platform. Even if the user account has been compromised, logins performed without validating the Multi-Factor Authentication code will be rejected, and the account would be inaccessible.

## Supported Authentication Applications for MFA

When logging onto the platform, Multi-Factor Authentication is required. The system user must configure MFA within 15 days of the user account being created. It is possible to log in without utilizing MFA at that date range.

{% hint style="info" %}
For the first 15 days after your account is activated, you can select the Continue without MFA option to proceed without activating Multi-Factor Authentication.
{% endhint %}

Recommended list of applications including, but not limited to:

* Microsoft Authenticator
* Google Authenticator
* Authy
* Duo Mobile
* LastPass Authenticator
* Symantec VIP Access

## How to activate Multi-Factor Authentication?

If you see a reminder for MFA when you log in to the platform, follow the steps below to activate it.

1. After login into the platform, go to the left menu and click on the company name or company logo above the menu.
2. Click **Security** on the pop-up menu.
3. Click **Enable** next to the Multi-Factor Authentication heading.
4. Follow the instructions in the Setup Multi-factor Authentication window.
5. Scan the **QR code** with the related application on your mobile device.
6. Enter the **MFA code** given on the application and click **Confirm** to complete the process.

{% hint style="info" %}
If you are unable to use the Multi-Factor Authentication application for a reason, the platform can send you a code through SMS so that you can regain your account.
{% endhint %}

To resync your MFA settings, follow the instructions below.

1. After login into the platform, go to the left menu and click on the company name or company logo above the menu.
2. Click **Security** on the pop-up menu.
3. Click **Resync** next to the Multi-Factor Authentication heading.
4. Follow the instructions in the Setup Multi-factor Authentication window.
5. Scan the **QR code** with the related application on your mobile device.
6. Enter the **MFA code** given on the application and click Confirm to complete the process.

{% hint style="info" %}
For companies using SSO via SAML, MFA is disabled by default.
{% endhint %}

## Video Tutorial

This tutorial covers how system users can enable Multi-Factor Authentication to log in to the platform more securely.

{% embed url="<https://youtu.be/1hvKBFxVIc0>" %}

## FAQ

### Q: I can’t access my phone. I'm unable to use the MFA app. What can I do to regain access to the platform?

A: You can receive the MFA code via SMS alternatively, and after logging into the platform, you can reconfigure your MFA settings.

### Q: My phone number has changed, and the SMS code for MFA cannot be delivered to reset the configuration. What can I do?

A: If there are other system users in the same company, you can request them to update your mobile number on your profile. If you are the only one system user, please request assistance from the support team.

### Q: What can I do if the MFA application I'm using isn't supported by the system?

A: You can contact the support team to request an integration for the MFA application. The support team will review the inquiry and response soon.

### Q: I am unable to use the MFA application. I have requested an SMS code for MFA and have not received it yet. What options do I have?

A: If there are other system users in the same company, you can request them to double check your mobile number settings. If you are the only system user, please request assistance from the support team.

### Q: I want to disable MFA permanently. Is it possible?

A: MFA is mandatory by default, and it cannot be disabled. For companies using SSO via SAML, it is disabled by default. In that case, please refer to the link.

### Q: I log into the platform using SSO via SAML; do I still need to configure MFA?

A: No, the platform will disable MFA by default in that case.

### Q: How long does platform remember me if I click the "Don't ask again on this computer" option?

A: If you select "Don't ask again on this computer" while login to the platform, the platform will remember your browser and will not ask you to enter MFA code each time you login until 14 days.
