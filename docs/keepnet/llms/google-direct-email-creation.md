# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/3.-email-deliverability/google-workspace/google-direct-email-creation.md

# Google: Direct Email Creation

## **Direct Email Creation** <a href="#direct-email-creation" id="direct-email-creation"></a>

**Direct Email Creation (DEC)** is a feature that connects to your O365 with a few required API permissions. This feature creates the phishing simulation email directly in the user’s inbox instead of sending the emails over SMTP protocol.**Key Benefits:**

1. Remove false positives that allow listing tools cause when analyzing links.
2. Eradicate maintenance and challenges of allow listing for the purpose of email delivery (you may need to allow list in your URL protection solutions such as Defender or ZScaler)
3. Very simple and quick setup (can be completed in a couple of minutes!)

This page explains how to use the **Direct** **Email** **Creation** feature in **Google** **Workspace**. Please follow the steps below to set up DEC settings within your Google Workspace.

{% hint style="info" %}
The Google Workspace settings section requires global administrator privileges.
{% endhint %}

## First Settings on Platform

Please follow the steps below to make the necessary settings on the platform for the Direct Email Creation feature to be connected within your Google Workspace.

* Log in to the platform
* Go to **Company > Company Settings >** **Direct Email Creation** page.
* Click the **+ NEW** button and select **Google** **Workspace**.
* Fill in the following fields.
  * **Configuration Name:** Give a name for your DEC settings.
  * **Client ID:** Copy the Client ID ( 102720780747216042586 ).
* Select your **domain(s)** under the **Domains** field.
  * **IMPORTANT:** The selected domain(s) must be **Verified** on the **Allowed** **Domains** page and must be used in your **Google** **Workspace**. Otherwise, the selected domain will not work with this DEC configuration.
* Do not close this tab. The **Save** button will remain disabled until the configuration works. Please proceed to the following section.

## Seconds Settings on Google Workspace

Please follow the steps below to make the necessary settings for the Direct Email Creation feature to be connected to your Google Workspace.

* Log in to <https://admin.google.com/> your Google Workspace admin panel.
* On the left-hand side, go to **Security > Access and Data Control > API Controls.**
* From the **API** **Controls** page, click on the **"Manage Domain-wide Delegation"** button under the **"Domain-wide Delegation"** field.
* Click on the **Add** **New** button.
* Enter the **Client** **ID** ( 102720780747216042586 ) into the **Client** **ID** field.
* Enter the following URLs into the **OAuth** **Scopes** field.
  * <https://mail.google.com>
  * <https://www.googleapis.com/auth/gmail.insert>
  * <https://www.googleapis.com/auth/gmail.modify>
* Click on the **Authorize** button.

## Complete Final Settings and Test Email Direct Creation Feature

Now, we will complete the process in this section, test the connection between Google Workspace and the Direct Email Creation feature, and see if we can successfully create an email in the user's inbox.

* Go to your **Company > Company Settings >** **Direct Email Creation** settings page.
* Click on the **"Send Test Email"** button to test the email creation.
  * **To:** Enter the recipient's email address who will receive the test email in their inbox.
    * The **email** **domain** must be the domain that was selected previously in the **Domains** field.
  * **From:** Enter an email as a from address.
  * **Sender Name:** Enter a sender name.
  * **Message:** Enter a message for test purposes.
* Click on the **Send** button to create the email in the user's inbox. If successful, please click the **Save** button to complete the configuration.

If the test is not successful, please see the **Troubleshoot** section.

## How to Launch Phishing Campaign by DEC Settings

Go to **Phishing Simulator > Campaign Manager** from the main menu. Click on **+ NEW** to create a phishing campaign and launch it to your target users.

* Please complete the first, second, and third sections step by step. For more information about how to use each menu, see [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-manager).
* When you get to the **Delivery** **Settings** page, inside of the **Email** **Delivery** field, select your **DEC** **settings.**
* Set up the rest of the settings as you wish, and then click on **Next** to go to the last page.
* Review all of your settings and click the **Launch** button to create phishing simulation emails in the selected target user's inbox.

✅ **You have now ensured your target users will receive emails through Keepnet. Now you need to** [**Whitelist Domains**](https://doc.keepnetlabs.com/next-generation-product/getting-started/recommended-add-domains-to-url-protection) **so your target users can successfully open Keepnet email links ➡️**

## Video Tutorial

This video tutorial explains how to configure direct email creation settings and launch a campaign with these settings to create phishing emails directly in the user's inbox instead of launching with the SMTP option.

{% embed url="<https://youtu.be/cEHtNP0-UcQ>" %}

## Troubleshoot

If you test the DEC configuration and the test is not successful, please try the following options.

* Please make sure the domain you selected in DEC settings is **Verified** in **the Allowed Domains** page. If it is not, please verify it.
* Please ensure the domain you selected in DEC settings is used in the employee's email address as main domain in Google Workspace.
* Please try to launch a phishing campaign to the test emails with DEC settings via Campaign Manager. Then, go inside the campaign report and go to the **Sending** **Report** menu. You can see more technical information if you hover your mouse over the delivery **Error** status.

If the options above are not resolved, please [contact the support team](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk) for further assistance.
