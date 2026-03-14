# Source: https://docs.startree.ai/corecapabilities/security/idp/azure.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Entra ID

> Configure Microsoft Entra ID as your Identity Provider (IdP) with StarTree. Microsoft Entra ID enables centralized authentication, enhanced security, and streamlined user management, simplifying access to StarTree.

## Prerequisites

1. Admin access to the [Azure portal](https://portal.azure.com/).
2. Access to a StarTree environment.
3. Obtain the redirect URI from StarTree.

## Steps

### Register the StarTree App

1. Navigate to the Microsoft Azure portal.
2. Select **Microsoft Entra ID** from the portal menu.

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/security/images/azure-entra-id.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=6c053d587341a1cf91e7d05f527b1ce6" alt="idp-azure-entra-id.png" title="idp-azure-entra-id.png" style={{ width:"21%" }} className="mx-auto" width="488" height="794" data-path="corecapabilities/security/images/azure-entra-id.png" />

1. Click on **Add** and select **App registration** to register a new app.
2. Specify a name for the application and select the supported account types option that fits your needs.
3. Under **Redirect URI**, select **Web** as the platform, and enter the URL that was provided by StarTree.

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/security/images/azure-register-application.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=89ae34f5d0eaa7220b895884206de6b4" alt="idp-azure-register-application.png" className="mx-auto" style={{ width:"77%" }} title="" width="2076" height="1572" data-path="corecapabilities/security/images/azure-register-application.png" />

1. **Register** the application.
2. Copy the **Application (client) ID** and the **Directory (tenant) ID**. You will need to provide these to StarTree.
3. Click **Add a certificate or secret** and create a new client secret. Save the client secret **Value**. You will need to provide this to StarTree.
4. Make sure the users have the email address field populated.

### Provide the following details to StarTree

* Application (client) ID.
* Directory (tenant) ID.
* Client secret.
* Issuer URL: [https://login.microsoftonline.com//v2.0](https://login.microsoftonline.com/\{tenantid}/v2.0) (replace the tenant ID with the actual value).

### \[Optional] Enable Groups Claim

To enable groups claim for an application in Azure AD for OpenID Connect, complete the following steps:

1. Select **Azure Active Directory** from the left navigation menu.
2. Select **App registrations**.
3. Select the application you just created.
4. Select **Token configuration** from the left navigation menu

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/security/images/azure-token-config.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=9617da92fec46e8398221a93e1bfe36b" alt="idp-azure-token-config.png" title="idp-azure-token-config.png" style={{ width:"40%" }} className="mx-auto" width="1226" height="1118" data-path="corecapabilities/security/images/azure-token-config.png" />

1. Click the **+ Add groups claim** button and select the types of groups you want to include in the claim.
2. Once you save the groups claim, click **API permissions**.

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/security/images/azure-api-permissions.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=b17c26940a42635b3ab8dc6706ba93e2" alt="idp-azure-api-permissions.png" title="idp-azure-api-permissions.png" style={{ width:"33%" }} className="mx-auto" width="928" height="1200" data-path="corecapabilities/security/images/azure-api-permissions.png" />

1. Click on **+ Add a permission.**
2. Select **Microsoft Graph** and then **Delegated permissions.**
3. Scroll down to the **Directory** category, expand it, then check **Directory.Read.All**

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/security/images/azure-api-permission-1.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=74bcff10700a1b92fbb92171ed63096c" alt="idp-azure-api-permission-1.png" style={{ width:"75%" }} title="" className="mx-auto" width="1634" height="772" data-path="corecapabilities/security/images/azure-api-permission-1.png" />

1. Click **Add permissions.**
2. When prompted, click **Yes** to grant admin consent.

### Granting User and Group Access to StarTree

1. Use the Azure portal search bar to search for **Enterprise applications.**
2. Select the application you created.
3. In the left navigation menu, expand the **Manage** menu and click on **Users and Groups.**

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/security/images/azure-users-and-groups.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=b2c844f4c0e8d85e95526826abdc1fe1" alt="idp-azure-users-and-groups.png" title="idp-azure-users-and-groups.png" style={{ width:"28%" }} className="mx-auto" width="850" height="980" data-path="corecapabilities/security/images/azure-users-and-groups.png" />

1. Click **+ Add user/group** and add the users and groups that you want provide access to StarTree.
2. Click on **Assign.**

Built with [Mintlify](https://mintlify.com).
