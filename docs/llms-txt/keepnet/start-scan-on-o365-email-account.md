# Source: https://doc.keepnetlabs.com/next-generation-product/platform/email-threat-simulator/start-scan-on-o365-email-account.md

# Start Scan on O365 Email Account

This document will provide information on how to start the Email Threat Simulator scan to the email inbox by using the **“Continue with Microsoft Office 365”** feature.

Microsoft O365 requires extra configuration steps in order to use the Email Threat Simulator with an O365 email account.

## Create Microsoft Azure Application

Follow the steps to create and configure the application on Microsoft Azure.

* Login to [Microsoft Azure](https://portal.azure.com/#home).
* From the **Home** page, go to the **App** **Registrations** menu from the **Azure** **Services** page
* Create a new application by clicking on the **+New Registration** button.
* Fill in the following fields on the **Register** **an** **Application** page and then click the **Register** button.
  * **Name:** Enter a name for your application.
  * **Supported account types:** Select the **“Accounts in this organizational directory only (Single tenant)”** option.
  * **Redirect URI:** Leave this field blank.
* After creating the application, copy the **“Application (client) ID”** and **“Directory (tenant) ID”** from the **Overview** page to use it in the platform later.

Follow the steps to assign the required **permission** to the application that has been created on Microsoft Azure.

* To assign **EWS.AccessAsUser.All** permission;
  * Click **API** **Permissions** from the left menu and click the **+Add a permission** button.
  * Click **APIs** **my** **organization** **users** title on the **Request** **API** **Permissions** page.
  * Select **Delegated** **permissions** option on the **Office** **365** **Exchange** **Online** page.
  * Enable the **EWS.AccessAsUser.All** permission in the **EWS** field and then click **Add** **Permission** button.
* To assign **Mail.Read** permission;
  * Click **API** **Permissions** from the left menu and click the **+Add a permission** button.
  * The **Microsoft** **APIs** field will appear by default on the **Request** **API Permission** page.
  * Click on **Microsoft** **Graph** and select **Delegated** **Permissions** option.
  * Enable the **Mail.Read** permission in the **Mail** field and after that click **Add** **Permission** button.

{% hint style="danger" %}
Click the **Grant admin consent for “CompanyName”** button to successfully grant these permissions to the application.
{% endhint %}

Follow the steps to configure **Authentication** configuration in order to start a simulation from the platform.

Set permissions on the Web Applications field from the Authentication menu;

* Click on the **Authentication** from the left menu and then click on the **+Add a platform** button from the **Platform** **Configurations** page.
* From **Configure** **Platforms** page, under the **Web** **Applications** title, click on the **Single-page Application** button.
* Under the **Configure** **Single-page Application** title, find **Redirect** **URLs** and **Front-Channel Logout URL** and then write **<https://ets-api.keepnetlabs.com/>** to both fields.
* Under the **Implicit Grant** and **Hybrid** **Flows** title, enable the **Access** **tokens** **(used for implicit flows)** and **ID tokens (used for implicit and hybrid flows)** options.
* Click on **Configure** button to finish this configuration steps.

Set permissions on the **Mobile and Desktop Applications** field from the **Authentication** menu;

* Click on the **+Add a platform** button from the **Platform** **Configurations** page.
* From **Configure** **Platforms** page, under the **Mobile and Desktop Applications** title, click on the **Mobile and Desktop Applications** button.
* Under the **Configure** **Desktop** **+ Devices** title, find **Redirect** **URLs** and then select the **“<https://login.microsoftonline.com/common/oauth2/nativeclient”>** address.
* Click on **Configure** button to finish this configuration steps.

Set permissions on the **Advanced** **Settings** field from the **Authentication** menu;

* From the **Authentication** menu, under the **Advanced** **Settings** title, find **Allow Public Client Flows** field and activate the **“Enable the following mobile and desktop flows:”** option.
* Click the **Save** button to finish this configuration steps.

{% hint style="danger" %}
Please make sure that the 2FA authentication is disabled on the email account before starting a simulation on the platform.
{% endhint %}

{% hint style="danger" %}
Azure might need approximately 30-60 minutes to apply the changes on their side. If you see an error while starting a simulation, please wait a few hours and then try again.
{% endhint %}

## How to start the simulation with the “Continue with Microsoft Office 365“ feature?

Follow the following steps to start the simulation from the platform.

* Go to **Email Threat Simulator > Scans** page from the left menu on the platform.
* Click on the **+NEW** button to start a new simulation.
* Read the warning message and then click the **“I Understand”** button.
* Follow the steps in the following table for further steps to start a simulation.

You can find more information about the **Email** **Threat** **Simulator** [here](https://doc.keepnetlabs.com/next-generation-product/platform/email-threat-simulator/start-scan).

<table><thead><tr><th width="174.5"></th><th></th></tr></thead><tbody><tr><td>Test Email Address</td><td>The email address that the simulation will be started on.</td></tr><tr><td>Choose an Option</td><td>Select the “Continue with Microsoft Office 365” option.</td></tr><tr><td>Password</td><td>The password of the email address that will be used in the simulation</td></tr><tr><td>Application (Client) ID</td><td>The Application (Client) ID information that is visible in the application that is created in the Azure platform.</td></tr><tr><td>Directory (Tenant) ID</td><td>The Directory (Tenant) ID information that is visible in the application that is created in the Azure platform.</td></tr></tbody></table>

Click on the **Next** button to go to the next page and customize the options as wished on “the **“Scan and Delivery Settings”** page and then go to the last page to agree on the **“User Agreement”** to start the simulation.

## Troubleshoot

If you’re unable to start an ETS scan on an O365 email account, follow these steps to troubleshoot:

1. **Check Sign-In Logs**: Navigate to the **User Sign-In** logs for the email account used for the ETS scan. Review the logs to identify any technical issues preventing Keepnet from connecting to the account.
2. **Verify MFA/2FA Settings**: Ensure that Multi-Factor Authentication (MFA) or Two-Factor Authentication (2FA) is disabled for the email account used for the ETS scan.
3. **Allow Time for Settings to Apply**: After configuring the account settings according to the documentation, wait at least 60 minutes before initiating the ETS scan. Microsoft may require some time to apply the changes across your organization.

If you still can't start an ETS scan on the email account, please [contact the support team](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk) for further assistance.
