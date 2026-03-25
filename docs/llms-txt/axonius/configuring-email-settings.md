# Source: https://docs.axonius.com/docs/configuring-email-settings.md

# Configuring Email Settings

You can configure an email server so that you can send an email notification as part of an enforcement set or send a report by email.

**To configure Email settings:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **External Integrations**, and select **Email**.

   * **Send emails** *(required, default: switched off)* - Toggle on to use an Email server. A configured Email server is a prerequisite before you can configure an email notification as part of a [configured Enforcement Set](/docs/creating-new-enforcement-sets) or [configuring a report to be sent via mail](/docs/report-configuration-screen).
   * SMTP gateway - Select the Gateway to use for SMTP.
     * Define the **Email host** name and **Port**.
     * **SMTP Authentication Type**  -   Select the SMTP Authentication type:
     * **Password Authentication**
     * **Azure Authentication**
     * **OAuth2 Authentication**

### Password Authentication

When you choose **Password Authentication**, you can configure a  **User name** and **Password**  (optional).

### Azure Authentication

#### Required Permissions

The user needs to have the following application-level permissions: Mail.Send or Mail.Send.Shared.

Select **Azure Authentication** to send email using MS Graph API, and configure the following settings:

* **Client ID** - The client ID from the Azure application.

* **Client secret** - The client secret from the Azure application.

* **Tenant ID** -  The Tenant ID from the Azure application.

* **Sender address**  - Enter  a sender address from which the mail will be sent. The Sender address  needs to have an *Exchange Online* license for *Microsoft 365* to be able to send emails.

  ### OAuth2 Authentication

  When you choose **OAuth2 Authentication**, set the following:

* **OAuth authentication email** - The email for which the OAuth token was created.

* **OAuth client ID** - Standard OAuth parameter

* **OAuth client secret** - Standard OAuth parameter

* **OAuth refresh token** - The derived value of creating active tokens from Client ID and Secret ID (procedure is standard)

* **OAuth URL** - The URL to authenticate with and which generates the Access tokens, for example:
  * [Microsoft AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow):

` https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`

* [Google](https://developers.google.com/identity/protocols/oauth2):

`https://accounts.google.com/o/oauth2/token`

**Microsoft Entra ID (Azure AD) Permissions**
You need to grant the following permissions
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OAUTHPErmissinons.png)

<Callout icon="📘" theme="info">
  Note

  Microsoft has deprecated the Outlook REST APIs; it is recommended to use the Graph API (Azure Authentication)
</Callout>

### General Email Configuration

* **Use SSL for connection** - Configure the connection to be **Unencrypted**, **Verified**, or **Unverified**.
  * When you select the **Verified** or **Unverified** options, you need to provide the SSL **CA file**, **Certificate file**, and **Private key file**.
  * When you select the **Unencrypted** option, the system attempts using TLS when sending emails (the default; no TLS configuration required). If TLS fails and the connection is active (if lost, the system first reestablishes the connection), the system proceeds to send emails without TLS.
* Define the **Sender address** for all emails sent by Axonius. If empty, the sender address is '[system@axonius.com](mailto:system@axonius.com)'.
* **Compress email attachments** *(default, false)* - Select this option to compress email attachments. This affects email attachments sent from [reports](/docs/report-configuration-page) and those sent as part of the [*Send email* Enforcement Set](/docs/send-email) action.
  * When this feature is activated, email attachments are sent as one compressed attachment in zip format.
  * When this feature is not activated, all email attachments are not compressed, and are sent as separate files.

<Callout icon="📘" theme="info">
  Note

  If attachments are larger than 10 Megabytes, the system notifies you that the email is 'big' (as some systems have a limitation on the size of emails that they can handle).
</Callout>

<br />

<br />