# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/microsoft-page-view-phishing-reporter.md

# Microsoft Page View Phishing Reporter

The **Microsoft** **Page View Phishing Reporter** is a Microsoft Outlook add-in developed by Keepnet that enables your users to quickly and securely report suspicious emails with a single click—directly from their email view pane. This helps your organization detect threats early and respond to phishing attempts more effectively.

### Which Outlook Platforms and Browsers Are Supported?

The **Microsoft** **Page View Phishing Reporter** is built using the Microsoft Graph API and is designed to provide a seamless, modern experience across **all major Outlook platforms**. Unlike the traditional [Microsoft Ribbon Phishing Reporter](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/microsoft-ribbon-phishing-reporter) that appears in the toolbar, the Page View version is **embedded directly within the email view pane**, providing a more integrated user interface.

[Click here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/..#comparison-ribbon-vs-page-view-vs-msi-outlook-phishing-reporter-microsoft-365) to view the list of compatible Outlook platforms that support the Microsoft Page View Phishing Reporter.

This cross-platform and cross-browser support ensures that your users can report suspicious emails **consistently and securely on Outlook platforms**, regardless of the device or environment they’re using.

## Where Are Reported Emails Sent?

When a user clicks the **Phishing Reporter** button, **the** **reported suspicious email** **is sent** to one or more destinations, depending on your organization's needs:

* 📌 **Microsoft 365 Defender portal**\
  Emails can be submitted directly to Microsoft for further analysis and contribution to spam/phishing intelligence (optional setup). Please refer to [this document](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/integrating-microsoft-defender-with-keepnet-phishing-reporter) for setup.
* 📌 **SOC or IT team's inbox**\
  The reported email can be forwarded to your designated inbox for internal analysis and response (optional setup). Please [visit here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter-customization#email-settings) for more information.
* 📌 **Keepnet Incident Responder** *(if licensed)*\
  If your organization uses [Keepnet’s Incident Responder](https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder), the reported email is also logged in the portal for case management, automated response, and automated analysis.

This flexible approach allows your organization to respond quickly to threats using your preferred tools and workflows.

## What Happens When Users Report Simulated Emails?

If you are running simulated phishing campaigns such as [**Phishing Simulator**](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator), [Callback Simulator](https://doc.keepnetlabs.com/next-generation-product/platform/callback-simulator), [Quishing Simulator ](https://doc.keepnetlabs.com/next-generation-product/platform/quishing-simulator)through Keepnet, the **Phishing Reporter** can automatically detect and log when a user reports a simulated phishing emails.

This allows you to:

* Track individual user performance,
* Identify who successfully recognized phishing simulation campaign emails, and
* Generate behavior-based metrics for awareness training.

This feature helps improve your organization’s overall security posture by providing **real-time insight into user vigilance**. Please see the following hint for the **'real-time insights into user vigilance'** explanation.

{% hint style="info" %}
If the **"Turn off email forwarding for reported Phishing Simulation Emails"** option is enabled by the admin while customizing the phishing reporter button, a pop-up message will appear thanking the user for their awareness each time they report simulation emails, reinforcing positive behavior. Please [see here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter-customization#add-in-settings) for more information about this option.
{% endhint %}

## What Happens When an Employee Reports an Email

When an employee uses the **Page View Phishing Reporter Add-in** to report a suspicious email, the reported email will be sent with a detailed report directly to your designated SOC or IT email address.

{% hint style="info" %}
If you purchased the [Keepnet Incident Responder](https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder) product, the email will also be sent for automated analysis, automated response, and case management.
{% endhint %}

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F6HP58fPdwtIebx2KVA8w%2FScreenshot%202025-05-22%20at%2017.38.50.png?alt=media&#x26;token=b1537690-4f78-40d1-9804-42c8753b0e76" alt="Example of reported email content sent to SOC/IT — attachment and report structure."><figcaption><p>Example of reported email content sent to SOC/IT — attachment and report structure.</p></figcaption></figure>

The email that is sent to the SOC/IT team inbox includes:

* The attached **original email** as an `.eml or .msg` file
* The attached **full message header of the original reported email** as a `headers.txt` file
* The **reporting reason** selected by the employee (e.g., spam, phishing, unsure)
* Any **additional comments** the employee entered in the message box

This structured report helps your security team quickly understand the context and take action, without needing to follow up with the reporting user.

## Microsoft Page View Phishing Reporter User Experience

Here is an example view of the **Microsoft Page View Phishing Reporter** button on the **New Outlook Desktop**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FTGheYyTBL4XJ0RAhqJFP%2F1%20(1).png?alt=media&#x26;token=67f3dce9-e038-4e58-832b-f62d348d3291" alt="View of Microsoft Page View Phishing Reporter button on New Outlook Desktop App."><figcaption><p>Picture 1: View of Microsoft Page View Phishing Reporter button on New Outlook Desktop App</p></figcaption></figure>

* When using the **Phishing** **Reporter** **button**, clicking the report button **opens a side panel** instead of the pop-up window.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fwwv2QSoRJP6nC12jB7SW%2F2%20(1).png?alt=media&#x26;token=7349d9d3-2d61-4fec-8d85-757b4d522dba" alt="Reporting side panel of Microsoft Page View Phishing Reporter on New Outlook Desktop App."><figcaption><p>Picture 2: Reporting side panel of Microsoft Page View Phishing Reporter Button on New Outlook Desktop App</p></figcaption></figure>

{% hint style="info" %}
**User Principal Name (UPN) and primary email:** For the Phishing Reporter add-in to work, each user's **Microsoft Entra ID (Azure AD) User Principal Name** must match their **primary email address** in Outlook. If they differ, the add-in may not work for those users. Identification steps and resolution are described in the Troubleshooting section below.
{% endhint %}

### How to Install the Microsoft Page View Phishing Reporter

1. Before deploying the button, we recommend customizing it. This can be done in the **Add-In Settings** tab under the [Phishing Reporter](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization) menu on the Keepnet platform.
2. Once customization is complete, stay on the **Settings** tab. Scroll down to the bottom and click **Manage and Download**. A pop-up will appear — select **Authorize** for **Delegated** **Access** to proceed.

{% hint style="warning" %}
Suggested to authorize **Application-Level Access** only for organizations using Conditional Access or Advanced Identity Policies, since managed device or policy restrictions may cause token acquisition to fail when using delegated permissions. Please click [here](#troubleshooting-microsoft-graph-authentication-error-aadsts530004) for more information.
{% endhint %}

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fl8Rs9Z5fueJkJgupkP46%2FScreenshot%202025-10-21%20at%2010.17.18.png?alt=media&#x26;token=1f246445-6a8c-4632-b911-babec0054ce9" alt="Download Button panel on Phishing Reporter page." width="563"><figcaption><p>Picture 3: Download Button panel on Phishing Reporter page</p></figcaption></figure>

3. Log in to your [Microsoft 365](https://admin.microsoft.com/) account using your **global admin credentials**.
4. Once you log in, the **Permissions** **requested** pop-up window will display. Read the permissions, then click **Accept**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FGExVj1BUxLZdAH77V7p5%2FScreenshot%202025-05-28%20at%2011.34.26.png?alt=media&#x26;token=b8c424ad-fd01-4586-90f0-6d4801af3575" alt="Required Graph API permissions for Microsoft Page View Phishing Reporter button." width="375"><figcaption><p>Picture 4: Required Graph API Permissions for<br>Microsoft Page View Phishing Reporter button</p></figcaption></figure>

#### Understanding Required Microsoft Graph API Permissions

The **Microsoft Page View Phishing Reporter** requires specific Microsoft Graph API permissions to function effectively within an organization’s Microsoft 365 environment. These permissions allow the application to interact with users’ emails, retrieve necessary details for reporting phishing attempts, and ensure smooth integration with the email infrastructure.

Below is a breakdown of the permissions required and their purpose:

**1. Mail Permissions**

* **Mail.Read**: Allows the Phishing Reporter to read the user’s email to retrieve necessary email details such as headers, attachments, and content.
* **Mail.Read.Shared**: Extends read access to shared mailboxes, ensuring that the application can retrieve phishing emails reported from shared accounts.
* **Mail.ReadWrite**: Provides both read and write access to the user’s mailbox, enabling modifications or tagging of emails as needed.
* **Mail.ReadWrite.Shared**: Extends read and write permissions to shared mailboxes for better handling of phishing reports.
* **Mail.Send**: Enables the application to send emails, which may be necessary when forwarding reported phishing emails.
* **Mail.Send.Shared**: Allows the application to send emails from shared mailboxes when the user has the appropriate permissions.

**2. User Profile Permissions**

* **profile**: Allows the Microsoft Page View Phishing Reporter to retrieve basic user profile information, ensuring accurate reporting and tracking.

5. Once you accept the permissions, the **GRAPH Authorization Successful** window will display.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F1wZx7as1uCzdJut3aG7i%2FScreenshot%202025-10-21%20at%2010.31.25.png?alt=media&#x26;token=652d8dc1-5b81-407e-bcaf-beddb7657111" alt="Graph Authorization Successful message on Phishing Reporter page." width="563"><figcaption><p>Picture 5: Graph Authorization Successfull message on Phishing Reporter page</p></figcaption></figure>

6. Click the **Download** button for the **Page** **View** button under the **Microsoft** **365** to download the **Microsoft365PhishingReporterAddin.xml** file.
7. In a new tab of your browser, log in to your [**Microsoft 365 admin center**](https://admin.microsoft.com/).

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FCeuisG2BuMfl5yZSrCYi%2Fimage12.png?alt=media&#x26;token=f3d58e14-9f1b-4919-b7c6-4816d38dca6e" alt="Microsoft 365 Admin Center."><figcaption><p>Picture 6: Microsoft 365 Admin Center</p></figcaption></figure>

8. From the menu on the left side of the page, click **Settings**.
9. From the **Settings** drop-down menu, select **Integrated** **apps**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FzNYBX9DlN38dcQko6fKD%2Fimage6.png?alt=media&#x26;token=0cebab9a-9194-4ff9-ac45-6afce7b0bc31" alt="Integrated Apps on Microsoft 365 Admin Center."><figcaption><p>Picture 6: Integrated Apps on Microsoft 365 Admin Center</p></figcaption></figure>

10. Click **Add-ins** at the top-right corner of the page.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F0MTodUqALA567GmHxBOu%2Fimage7.png?alt=media&#x26;token=84b20411-6108-41bf-b596-5d649e7c8b2a" alt="Add-ins button access on Integrated Apps page."><figcaption><p>Picture 7: Add-Ins button access on Integrated Apps page</p></figcaption></figure>

11. On the add-ins page, click **Deploy** **Add-In**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FPAIXRsdi77j918JJwZPd%2Fimage5.png?alt=media&#x26;token=2c293344-6b1a-480d-8c39-3f5826707c88" alt="Click deploy add-in button."><figcaption><p>Picture 8: Click deploy add-In button</p></figcaption></figure>

12. In the pop-up window, click **Next**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FuQcX0GaDSaRiv485gl4D%2FScreenshot%202025-03-03%20at%2018.10.27.png?alt=media&#x26;token=2400fd84-ece4-49b0-84b7-7d5bcab0e607" alt="Deploy a new add-in pop-up message."><figcaption><p>Picture 9: Deploy a new add-in pop-up message.</p></figcaption></figure>

13. Click the **Upload** **custom** **apps** button.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FGnNIH0oB6AhE3rScjUxO%2Fimage3.png?alt=media&#x26;token=2c143488-3c20-41e8-ba29-faaec1db2a17" alt="Deploy a custom add-in page."><figcaption><p>Picture 10: Deploy a custom add-in page</p></figcaption></figure>

14. Select the '**I have the manifest file (.xml) on this device'** option. Then, click **Choose** **File** and select the **Microsoft365PhishingReporterAddin.xml** file that you downloaded in step 6.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fmz8cDo8qA8OuoRNP6csg%2Fimage14.png?alt=media&#x26;token=dcef820b-ee00-4ce5-bea1-d861ae930463" alt="Uploading XML file to deploy the Microsoft Page View Phishing Reporter add-in."><figcaption><p>Picture 11: Uploading XML file to deploy the Microsoft Page View Phishing Reporter add-in</p></figcaption></figure>

15. Click **Upload** to install the **Microsoft** **Page** **View** **Phishing** **Reporter** add-in.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FxRmdeV6dIaUyT0FzzgKH%2FScreenshot%202025-03-03%20at%2018.11.21.png?alt=media&#x26;token=80ae9cca-780b-4141-9495-06d3a70a54c6" alt="Deployment Settings for Microsoft Page View Phishing Reporter add-in."><figcaption><p>Picture 12: Deployment Settings for Microsoft Page View Phishing Reporter add-in</p></figcaption></figure>

16. From the pop-up window, select **which users will have access to the Microsoft Page View Phishing Reporter** and **which method** you would like to use to deploy the Phishing Reporter.

{% hint style="info" %}
We recommend that you **allow all users** to access the Phishing Reporter. We also recommend that you use the '**Fixed' deployment method**.
{% endhint %}

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FZPtlZRcxOPN53CAEfBYd%2FScreenshot%202025-05-21%20at%2014.44.50.png?alt=media&#x26;token=56f1b5ff-37b4-4b87-8d27-bd7d498cc529" alt="List of permissions used by the Microsoft Page View Phishing Reporter add-in."><figcaption><p>Picture 13: The list of permissions that are used by the Microsoft Page View Phishing Reporter add-in</p></figcaption></figure>

17. Click **Next**, and additional app permissions will display.
18. Once you have read the permissions, click **Save**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fk0sx28wijx9epjQ539Uv%2FScreenshot%202025-03-03%20at%2018.11.29.png?alt=media&#x26;token=81657f66-c080-485a-a74f-26f38fc68599" alt="Successful deployment message for Microsoft Page View Phishing Reporter add-in."><figcaption><p>Picture 14: Successful deployment message of Microsoft Page View Phishing Reporter add-in</p></figcaption></figure>

{% hint style="warning" %}
The expected timeframe for the Phishing Reporter to deploy is 12 hours, but timeframes can vary. For more information about deploying add-ins, see Microsoft's [Deploy add-ins in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide#deploy-an-office-add-in-using-the-admin-center) article.
{% endhint %}

19. Once the pop-up window displays a confirmation that the add-in has been successfully deployed, click **Next**. The **Announce** **add-in** pop-up window will open and display a message about announcement recommendations from Microsoft.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FKjh7jzBSTLNqrOQvog1K%2FScreenshot%202025-03-03%20at%2018.15.27.png?alt=media&#x26;token=d8fd555a-7b75-4800-8fb8-1a11b87b789e" alt="Default announcement message from Microsoft to inform employees."><figcaption><p>Picture 15: Default announcement message provided by Microsoft to inform employees</p></figcaption></figure>

{% hint style="info" %}
After you install and deploy the Phishing Reporter, you might receive an email from your mail service provider that contains information you can use to help you announce the Phishing Reporter add-in to your users. Keepnet does not send the email about the Phishing Reporter’s intended usage and benefits.
{% endhint %}

20. Click **Close** to close the pop-up window.

## Troubleshooting

### Microsoft Graph Authentication Error (AADSTS530004)

The following issue occurs because **Microsoft Conditional Access** requires devices or sessions to be compliant before granting access to protected resources. When the **Keepnet Phishing Reporter** **add-in** attempts to connect via **Delegated Access** (i.e., on behalf of a signed-in user), the organization’s Conditional Access policies may block the request if it does not originate from a compliant or trusted device.

This is common when:

* The organization enforces device compliance via Intune or Azure AD.
* The user accessing the Phishing Reporter add-in is considered an external identity.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F7PNUifMJuKhkDfUCTnwU%2Fimage%20(2).png?alt=media&#x26;token=d982af03-a042-45c4-bf81-1e4cc60c52ea" alt="Screenshot reference of the error:" width="375"><figcaption><p>Error or troubleshooting screenshot for Page View Phishing Reporter (e.g. AADSTS530004).</p></figcaption></figure>

#### What Is Application-Level Access?

**Application-level permissions** allow the **Keepnet Phishing Reporter add-in** to access Microsoft 365 mailboxes and perform phishing reporting tasks **without requiring a signed-in user**. The add-in authenticates using its own identity instead of a user’s.

When enabled, the Phishing Reporter add-in acts as a **trusted service** with organization-wide permissions granted by an administrator. This ensures that Keepnet can operate under Conditional Access, perform automated operations, and maintain consistent behavior even when users are not logged in.

#### Delegated vs Application-Level Access

<table><thead><tr><th width="151.91796875">Access Type</th><th width="202.17578125">Description</th><th width="119.875">Scope</th><th>Typical Use Case</th></tr></thead><tbody><tr><td>Delegated Access</td><td>Add-in acts on behalf of a user, limited by that user’s permissions.</td><td>User-based</td><td>When a user reports a phishing email from Outlook.</td></tr><tr><td>Application-Level Access</td><td>Add-in acts as itself, using admin-granted permissions.</td><td>Tenant-wide</td><td>When the Phishing Reporter add-in performs identity mapping, mailbox scans, or Conditional Access operations.</td></tr></tbody></table>

#### Why Application-Level Access Is Required

If your organization enforces **Conditional Access**, **device compliance**, or **automated identity** **checks**, Delegated Access will fail because it depends on the user’s compliance state.

**Application-Level Access** ensures:

* **Uninterrupted operation** of the Phishing Reporter add-in across all mailboxes.
* **Centralized and consistent access** across departments and tenants.
* **Secure authentication** compatible with Conditional Access requirements.

#### When to Use Application-Level Access

Use Application-Level Access if:

* You require organization-wide authentication for all users.
* Conditional Access or advanced identity enforcement is active.
* Consistency across departments/regions is needed.

#### Security Notes

* **Admin Consent Required:** Only global administrators can grant Application-Level permissions.
* **Least Privilege Principle:** Assign only the permissions needed for the Phishing Reporter add-in to operate.
* **Governance:** Regularly audit app-only permissions to ensure compliance.

#### Keepnet Recommendation

Use **Application-Level Access** for:

* Reliable, organization-wide authentication and identity mapping.
* Compatibility with Conditional Access and advanced identity controls.

Keep **Delegated Access** for:

* End-user actions like phishing report submission from the Outlook ribbon.

#### Additional References

* [Microsoft Docs: Conditional Access and Compliant Devices](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-compliance)
* [Microsoft Docs: On-Behalf-Of Flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow)

#### Summary

This error (AADSTS530004) indicates that your Microsoft 365 tenant blocks delegated access under Conditional Access rules.

To resolve it, configure Application-Level Access (App-only) for the Keepnet Phishing Reporter add-in and reauthorize the application with admin consent

### Microsoft Graph Authentication Error (AADSTS50076)

The following issue occurs because **Microsoft Conditional Access** or another security policy now requires **multi-factor authentication (MFA)** to access Microsoft Graph. When the **Keepnet Phishing Reporter add-in** attempts to authenticate using the **On-Behalf-Of (OBO)** flow, the request fails with the following error:

> Unknown error: {"data":{},"status":"FAILED",\
> "message":"OnBehalfOfCredential authentication failed: ||\
> **AADSTS50076**: Due to a configuration change made by your administrator,\
> or because you moved to a new location, you must use multi-factor\
> authentication to access '00000003-0000-0000-c000-000000000000'.\
> Trace ID: Correlation ID: Timestamp: . The returned error contains a claims challenge."}

#### Why This Happens

This is common when:

* The organization has recently **enabled or updated Conditional Access** policies that enforce MFA for Microsoft Graph or specific applications.
* The **signed-in user has not yet completed MFA** on the current device/session.
* The **claims challenge returned by Azure AD** is not handled by the application during the On-Behalf-Of flow.

#### How to Resolve

Ask your Azure AD / M365 administrator to:

1. **Confirm MFA and Conditional Access requirements**
   1. Review the Conditional Access policies that apply to the Keepnet Phishing Reporter add-in and Microsoft Graph.
2. **Ensure the user satisfies MFA**
   1. Have the affected user sign in to Microsoft 365 or Outlook and complete the required multi-factor authentication (e.g., Authenticator app, SMS, FIDO key).
   2. After successfully completing MFA, retry using the Phishing Reporter add-in.
3. **Review claims challenge handling (for advanced configurations)**
   1. If you are using custom integration or the Microsoft Authentication Library (MSAL) with the OBO flow, make sure that claims challenges are correctly handled as described in Microsoft’s documentation:
   2. Handling MFA and Conditional Access claims: <https://aka.ms/msal-conditional-access-claims>
   3. Handling claims in On-Behalf-Of flow: <https://aka.ms/msal-conditional-access-claims-obo>

If the error persists after the user has completed MFA and policies have been verified, share the Trace ID, Correlation ID, and Timestamp from the error message with your Azure AD administrator for further investigation.

### Reporter button not working for some users — UPN and primary email mismatch

The Keepnet Phishing Reporter add-in may fail for **some users** when their **Microsoft Entra ID (formerly Azure AD) User Principal Name (UPN)** does not match their **primary email address** used in Outlook. Typically only a subset of users in the organization are affected.

#### Why This Happens

* The add-in identifies the user by **primary email address** (e.g. SMTP/mailbox address). Sign-in uses **UPN**. If UPN and primary email differ, the add-in cannot match the signed-in identity to the correct user in Entra ID.
* **Symptoms:** The Phishing Reporter button does not appear, is greyed out, or does not respond for certain users; other users in the same tenant can use it. The user can open Outlook and use email normally, but reporting fails when they click the Reporter button.

#### How to Resolve

Ask your Microsoft Entra ID / M365 administrator to:

1. **Identify affected users:** In Microsoft Entra ID, open the user’s profile and compare **User principal name** with **primary email address** (Mail/Primary SMTP). If they differ, the user is affected.
2. **Update UPN:** In [Microsoft 365 admin center](https://admin.microsoft.com/) or [Azure portal](https://portal.azure.com/), go to **Users** → **Active users**, open the user, edit **User principal name** to match their **primary email address**, and save. See [Add or update a user's profile information in Azure AD](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info) for details and constraints.
3. **Verify:** Have the user sign out and sign in again, then try the Phishing Reporter button.

#### Best practice

Ensure UPN matches primary email for all users who will use the add-in, and include this in your Phishing Reporter deployment checklist.

## How Microsoft Page View Phishing Reporter Buttons Look on Outlook Platforms

The **Microsoft Page View Phishing Reporter** button enables users to report suspicious emails quickly and efficiently across various Outlook environments. This guide visually demonstrates how the Phishing Reporter button appears and can be accessed in different Outlook platforms: **New Outlook**, **Classic Outlook**, **Outlook Web App (OWA)**, **Outlook for Mac**, and **Outlook Mobile (iOS/Android)**.

### New Outlook

In the redesigned **New Outlook** interface, the **Phishing** **Reporter** button is located in the **right-hand apps panel** while viewing an email.

1. Go to your **Inbox**.
2. Select the suspicious email.
3. Click the **Apps icon** (grid icon) on the right-hand side panel.
4. Choose **Phishing** **Reporter** from the list.

<div align="center" data-full-width="false"><figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FHx1kJPB9IeY2AYLiSia5%2Fs5.png?alt=media&#x26;token=7547d3e4-f440-4f7f-92f4-6ea9dba526a8" alt="Page View Phishing Reporter — New Outlook, Apps panel and Phishing Reporter option." width="563"><figcaption><p>Page View Phishing Reporter — New Outlook, Apps panel and Phishing Reporter option.</p></figcaption></figure></div>

### Classic Outlook

In the **Classic** **Outlook** interface, the button is integrated into the **ribbon toolbar** at the top.

1. Navigate to your **Inbox**.
2. Open the email you want to report.
3. Click the **Phishing Reporter** button on the ribbon at the top of the message window.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FGosTJLJtU64TLDeE368P%2Fs4.png?alt=media&#x26;token=f53286bc-481f-408a-82c0-e09552a38f23" alt="Page View Phishing Reporter — Classic Outlook, ribbon toolbar." width="563"><figcaption><p>Page View Phishing Reporter — Classic Outlook, ribbon toolbar.</p></figcaption></figure>

### Outlook Web App (OWA)

For users accessing **Outlook via a web browser**:

1. Open your **Inbox** in Outlook on the web.
2. Select the suspicious email.
3. Click the **Apps icon** (grid icon) located in the message view panel.
4. Click on **Phishing Reporter**.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FN0wQLGTfV8YEFAR8MLmb%2Fs1.png?alt=media&#x26;token=d26fe3de-6914-42a0-9c90-a7afca22347f" alt="Page View Phishing Reporter — Outlook Web App (OWA), Apps icon and Phishing Reporter." width="563"><figcaption><p>Page View Phishing Reporter — Outlook Web App (OWA), Apps icon and Phishing Reporter.</p></figcaption></figure>

### Outlook for Mac

In **macOS** versions of Outlook, the button is accessible through the top toolbar options.

1. Go to your **Inbox** and select the suspicious email.
2. Click the **three-dot icon (•••)** in the top-right corner.
3. Select **Phishing Reporter** from the dropdown menu.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F7WCrWvqOXRSrabwTMbRA%2Fs3.png?alt=media&#x26;token=98126f5f-e26c-4e76-acac-087c55f77ee9" alt="Page View Phishing Reporter — Outlook for Mac, three-dot menu and Phishing Reporter." width="563"><figcaption><p>Page View Phishing Reporter — Outlook for Mac, three-dot menu and Phishing Reporter.</p></figcaption></figure>

### Outlook Mobile (iOS / Android)

On mobile devices, the reporting option is available via the message action menu:

1. While viewing the suspicious email, tap the **three-dot menu (•••)** in the top-right corner.
2. Tap on the **Phishing Reporter** icon from the list of options.

<div data-full-width="true"><figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F0iZ3XfOlaHNIzB3C0oyN%2Fs2.png?alt=media&#x26;token=e53207f4-9e00-4c27-80f4-a17066106dff" alt="Page View Phishing Reporter — Outlook Mobile, three-dot menu and Phishing Reporter icon." width="188"><figcaption><p>Page View Phishing Reporter — Outlook Mobile, three-dot menu and Phishing Reporter icon.</p></figcaption></figure></div>

## Why Do Some Users See a Popup or Redirection?

When using Keepnet’s Phishing Reporter, most users can report phishing emails with a single click — seamlessly and silently. However, some users may occasionally see a popup window or get redirected briefly to Microsoft’s login screen.

This behavior is expected, safe, and part of Microsoft’s secure authentication process.

#### What Is Supposed to Happen?

Keepnet’s Phishing Reporter is designed to authenticate users automatically in the background. In most cases, if the user is already signed into Microsoft 365, the system can confirm their identity silently without any additional steps.

#### So Why Is There Sometimes a Pop-up or Redirection?

A small number of users may see a sign-in prompt because:

* **They haven’t used the add-in before,** and the system needs their permission
* **Their Microsoft 365 session has expired,** and reauthentication is required
* **Their browser or security settings block silent sign-in,** which is common in private/incognito mode or stricter corporate environments
* **Microsoft requires additional verification,** such as multi-factor authentication
* **They’re on a new device or browser** that Microsoft doesn’t recognize

In any of these cases, the system must briefly show a popup or redirect them to sign in securely before proceeding.

#### Will This Happen Every Time?

No. Once a user has signed in and given the necessary permissions, their session is remembered. They typically won’t be asked to sign in again unless:

* Their session expires (after days or weeks)
* Company policy or security tools clear their session
* New permissions are requested

#### Bottom Line

Popups or redirections are not errors — they’re part of Microsoft’s secure identity verification process. They ensure that only authorized users can access sensitive data and perform actions like reporting emails.

Keepnet follows Microsoft’s best practices to provide the most seamless experience possible, while maintaining strict security and compliance.

## Frequently Asked Questions (FAQs)

### Q: Can I show a confirmation prompt before deleting a reported email?

**A:** Yes. To enable a confirmation prompt, go to the **Phishing Reporter** menu and select the **Settings** tab. Within the tab, scroll down to the **Dialog Box Settings** section. Locate the **Delete Reported Emails** option, and select **With Confirmation** from the dropdown menu.

### Q: Does the Microsoft Page View Phishing Reporter work on Outlook Mobile for iPhone or Android?

A: Yes, it works. Please visit [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/..#comparison-ribbon-vs-page-view-vs-msi-outlook-phishing-reporter-microsoft-365) to view the supported Outlook environments.

### Q: Can I customize the Microsoft Page View Phishing Reporter side panel message, such as setting a fixed width and height?

A: No, Microsoft does not allow customization of the size of the side panel. Its size is automatically adjusted.

### Q: Can users choose their preferred language for the Phishing Reporter button pop-up messages?

**A:** Yes, you can add multiple languages from the [**Phishing Reporter customization page**](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization). When an employee reports an email, the reporting side panel will appear, and they will be able to select their preferred language from the available language options before proceeding with the reporting.

### Q: If we set the Phishing Reporter button to delete reported emails automatically, can the email be recovered?

A: Yes, if you use the **'Delete reported emails'** option with **'Automatically**'**,** the reported email will be deleted automatically. The email will be sent to the **Trash** folder, where you can visit the folder and restore the deleted email.

### Q: Does the Microsoft Page View Phishing Reporter button work on the native Mail client of Apple on IOS mobile?

A: No, it is not supported.

## Tutorial Video

This video tutorial shows the documentation steps for deploying the Microsoft Page View Phishing Reporter add-in on M365.

{% embed url="<https://www.youtube.com/watch?v=PhBu-3p7TB4>" %}
