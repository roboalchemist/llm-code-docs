# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/direct-email-creation/direct-email-creation-for-microsoft-365.md

# Direct Email Creation for Microsoft 365

This page explains how to use the **Direct** **Email** **Creation** feature in **Microsoft 365**. Please follow the steps below to set up DEC settings within your Microsoft 365.

{% hint style="info" %}
The Microsoft 365 settings section requires global administrator privileges.
{% endhint %}

## Connect Your O365 with the DEC App

Please follow the steps below to make the necessary settings on the platform for the Direct Email Creation feature to be connected to your Microsoft 365.

* Log in to the platform
* Go to **Company > Company Settings >** **Direct Email Creation** page.
* Click the **+ NEW** button and select **Microsoft 365.**
* Click on the **Connect Account** button to connect your O365 with the Direct Email Creation (DEC) application to create a configuration.
* If required permissions are established successfully, you can configure the following DEC settings.
  * **Name:** Set a name for DEC settings.
  * **Domains:** Select email domains that you will send phishing simulation emails.
  * **Test Email:** Test if the configuration works successfully.
    * **Send Test Email To:** Enter the business email address.
    * **Sender Email Address:** Enter any from the address.
    * **Sender Name:** Enter a sender name.
    * **Message:** Enter a message.
  * Click the **SAVE** button to create configuration settings.

{% hint style="info" %}
The configuration will be created if the requested permissions are established successfully. If it fails, the admin can see why it fails from the same page of the configuration.
{% endhint %}

## How to Launch Phishing Campaign by DEC Settings

Go to **Phishing Simulator > Campaign Manager** from the main menu. Click on **+ NEW** to create a phishing campaign and launch it to your target users.

* Please complete the first, second, and third sections step by step. For more information about how to use each menu, see [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-manager).
* When you get to the **Delivery** **Settings** page, inside of the **Email** **Delivery** field, select your **DEC** **settings.**
* Set up the rest of the settings as you wish, and then click on **Next** to go to the last page.
* Review all of your settings and click the **Launch** button to create phishing simulation emails in the selected target user's inbox.

## About Required API Permissions

Keepnet follows [Microsoft's secure design principles](https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview?WT.mc_id=Portal-Microsoft_AAD_RegisteredApps) for third-party applications and has received approval from Microsoft. The app uses permissions solely to create simulated phishing emails in users' inboxes. It does not include permission to read, send email or access other mailbox functionalities.

The following permissions are required for customers using the **Microsoft** **365** email server.

<table data-header-hidden><thead><tr><th width="189"></th><th></th></tr></thead><tbody><tr><td>Read domains</td><td>It is used to fetch the domains that the customer owns in Microsoft 365 and allows the customer to select the relevant domains so the platform can create simulation emails in the user's inbox under the selected domains.</td></tr><tr><td>Read and write mail in all mailboxes</td><td>It is used to create a simulation email in the user's inbox. Please see following screenshot for more information about this permission</td></tr><tr><td>Read all users' full profiles</td><td>It is used to read the user's profile information, retrieve email account details (e.g., email address), and switch to the user's profile to create simulation emails in their inbox.</td></tr><tr><td>Sign in and read user profile<br></td><td>It is used to read basic company information of the signed-in user who grants permission.</td></tr></tbody></table>

Microsoft bundles permissions together. The following Microsoft screenshot shows a '**Mail**' permission group. There's no separate **Write** permission — only the **Mail.ReadWrite** permission, which handles **Write** **actions**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FoqlWQlHAwFpEmzdYXdXJ%2Fmail.readwrite.png?alt=media&#x26;token=b768c380-9017-4b04-b837-70dd7d48eb2f" alt="Microsoft permission group — Mail.ReadWrite for DEC."><figcaption><p>Microsoft permission group — Mail.ReadWrite for DEC.</p></figcaption></figure>

The following permissions are required for customers using the **Microsoft** **Exchange** **Online** email server.

<table data-header-hidden><thead><tr><th width="180"></th><th></th></tr></thead><tbody><tr><td>Access mailboxes as the signed-in user via Exchange Web Services</td><td>It is used to access user's mailbox in order to create simulation email in the inbox.</td></tr><tr><td>Use Exchange Web Services with full access to all mailboxes</td><td>It is used to create a simulation email in the user's inbox without using a sign-in account.</td></tr><tr><td>Manage Exchange As Application</td><td>It is used to allow the app to manage the organization's Exchange environment without any user interaction.</td></tr></tbody></table>

In summary, customers only need to share the necessary permissions based on their specific environment, whether they use **Microsoft** **365**, **Microsoft** **Exchange** **Online**, or a **hybrid of both**. Keepnet requests these permissions to create simulation emails in the user's inbox across **any of these environments**.

For example, if you use just only **Microsoft** **Exchange** **Online**, then Keepnet only uses the related permission groups for **Exchange** **Online**, other permissions are not used.

{% hint style="info" %}
**Read and write all applications**: This permission is used only when the customer uses a custom domain instead of dash.keepnetlabs.com to access the platform. This ensures that the customer can successfully configure the DEC settings on the platform while using the custom whitelabeled domain.
{% endhint %}

## **How to Provide Proof of DEC App Activity for Compliance and Security**

To view the activity of the DEC application created by the platform and confirm that it is only creating simulation emails (and not reading any emails), please follow these steps:

1. **Log in** to the [Microsoft Compliance Portal](https://compliance.microsoft.com/).
2. Navigate to the **Audit** menu.
3. If not already enabled, click to **Enable Audit Logging**.
4. **Set up the DEC configuration** successfully on the platform, and send a test email using the DEC settings to generate activity logs.
5. Go back to the **Audit menu** and search for logs related to the user who sent the test email with DEC settings. Also, you may copy the **Application** **ID** of the DEC application and paste it under the Keyword Search field to search logs.

In the logs, you should see activities such as **"Created mailbox item"**, confirming the application's behavior. For example:

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FVCntvGflRgwdK9yvFsBa%2Funnamed.png?alt=media&#x26;token=6a31106a-8380-40aa-906a-667cd689d159" alt="Microsoft Compliance Portal — audit log showing Created mailbox item for DEC app."><figcaption><p>Microsoft Compliance Portal — audit log showing "Created mailbox item" for DEC app.</p></figcaption></figure>

This log indicates that the application is only creating mailbox items and not accessing or reading mailboxes.

## Video Tutorial

This video tutorial explains how to configure direct email creation settings and launch a campaign with these settings to create phishing emails directly in the user's inbox instead of launching with the SMTP option.

{% embed url="<https://www.youtube.com/watch?v=qBnJFVtqz_c>" %}

## FAQ

### Q: Which permissions does the DEC feature work with?

A: Click [here](#about-required-api-permissions) for more information.

### Q: Can I launch a campaign with DEC settings using the Fast Launch option?

A: No, you can only launch a campaign with DEC settings using Campaign Manager. If you launch a campaign with Fast Launch, the campaign will be started with default SMTP settings.

### Q: Do I need to allow list if I use the DEC feature?

A: No, you don't need to [Allow List](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing) if you are using the DEC feature for the [Phishing Simulator](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator) or the [Awareness Educator](https://doc.keepnetlabs.com/next-generation-product/platform/awareness-educator) product.

### Q: Can I resend the campaign email to the users whose status shows Error in the Sending Report menu in the campaign report?

A: No, the users whose status shows Error means the destination email user account hasn’t been found in the O365, or there might be another problem for these users' email accounts which platform will show you as a tooltip if you hover your mouse over the error status.

### Q: What action should I take for users whose status shows an error ("domain.com" is not in the allowed domain list) in the Sending Report menu after the launch campaign?

A: You can check and make sure you selected the related domain addresses in the DEC configuration, and then you can try to resend the campaign to these users from the Sending Report menu in the campaign report.

### Q: What are the security risks if we authorize the DEC feature on the O365 server?

A: Authorizing the DEC feature on the O365 server doesn’t involve any potential security considerations. Keepnet Labs provides encryption to secure data and prevent unauthorized access to keep your data safe.

First, we encrypt data and apply it to our [cryptography policy](https://doc.keepnetlabs.com/resources/compliance#cryptography-policy) and [data protection policy](https://doc.keepnetlabs.com/resources/compliance#data-protection-policy) to make data secure and prevent potential vulnerabilities.

Furthermore, we have a strict access policy and do not allow unauthorized gain access to sensitive data; please see our access policy [here](https://doc.keepnetlabs.com/resources/compliance#access-management-procedure).

Keepnet does its best to maintain rigorous security protocols such as regular audits of access rights, continuous monitoring for abnormal activities, and thorough vulnerability assessments.

You can see other data security measures on our [platform security page](https://doc.keepnetlabs.com/resources/compliance).
