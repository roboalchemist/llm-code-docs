# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-ms-azure.md

# SAML Support - MS Azure

The Security Assertion Markup Language (SAML) is an XML standard that facilitates the exchange of user authentication and authorization data across secure domains.

SAML-based SSO services involve communications between the user, an identity provider that maintains a user directory, and a service provider. When a user attempts to access an application from the service provider, the service provider sends a request to the identity provider for authentication. The service provider then verifies the authentication and log the user in. The user does not have to log in again for the rest of his session.

The Avaamo platform supports Single Sign-On (SSO) provided by different Identity Service Providers. In this article, the steps to integrate MS Azure with the Avaamo platform are detailed out:

1. [Before you begin](https://docs.avaamo.com/user-guide/build-agents/configure-agents/deploy/alexa#before-you-begin)
2. [Create SAML SSO application in Azure](#create-saml-sso-application-in-azure)
3. [Configure SAML SSO application in Azure](#configure-saml-sso-application-in-azure)
4. [Integrate MS Azure SSO application in Avaamo Platform](#integrate-ms-azure-sso-application-in-avaamo-platform)
5. [Testing integration](#testing-integration)

Azure Active Directory Seamless Single Sign-On (Azure AD Seamless SSO) automatically signs users in when they are on their corporate devices connected to the network.

## Before you begin

Ensure you meet the following pre-requisites before configuring and integrating the SAML SSO Azure application in the Avaamo Platform:

* Administration login credentials for MS Azure account
* A callback URL must be specified in the MS Azure SSO application. Contact Avaamo support to get the callback URL.
* You have configured the **Settings** roles for your user. Only a user with the **Settings** role can configure Identity providers in the Avaamo Platform. See [Users and Roles](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions), for more information.

## Create SAML SSO Application in Azure

To integrate the Avaamo platform for Single Sign-On, you need to have access to an MS Azure account and Avaamo login credentials. To configure the SSO, follow the steps below:

* Open a browser (Safari, Chrome, Firefox) and enter [https://portal.azure.com​](https://portal.azure.com/).
* Login into the MS Azure account using the Administration login credentials.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh2VavEoIAmsKiGe-7%2F-Lyh3RbBoQzlFufybMSe%2Fazure-sso-1.png?alt=media&#x26;token=5ee4c2d7-46b1-4312-a2c7-34a01a097e31" alt=""></div>

* From the left navigation pane, select **Azure Active Directory**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3K8J9sEerMTfVJ4JJP%2F-M3Kdovy7hwQxR_ljDuy%2Fazure-sso-2.png?alt=media\&token=caf7ca63-169d-4fef-bb78-926ed137abf8)

* In the **Azure Active Directory** page, select **Enterprise applications** from the left navigation menu to create a new application.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3K8J9sEerMTfVJ4JJP%2F-M3KeK07VuFioD9dflie%2Fazure-sso-3.png?alt=media\&token=72bfa4fc-3c68-465b-8aba-4252c0125b50)

* In the **Enterprise applications** page, click **New application**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3Ke_cBPwmGNOujFpR1%2F-M3Kex8vAqydpTL3pRsf%2Fazure-sso-4.png?alt=media\&token=4d662f08-d9f2-492a-9b45-c76e60a9367e)

* In the **Add an application** page, select **Non-gallery application**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3Ke_cBPwmGNOujFpR1%2F-M3KfQvqa6X2VGJkBFLM%2Fazure-sso-5.png?alt=media\&token=ba847f0c-c334-421f-adf3-54008de211b4)

* In the **Add your own application** page, enter a **Name** for your application and click **Add**. **Example**: Avaamo Application.&#x20;
* Select **Single sign-on** from the left navigation pane.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3Ke_cBPwmGNOujFpR1%2F-M3KgQS9vOqFEy4YhzRP%2Fazure-sso-6.png?alt=media\&token=79e73114-734a-4c23-88ef-4a1d5fb25aba)

* Choose **SAML** as your Single sign-on method.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3Ke_cBPwmGNOujFpR1%2F-M3KguQFtlt2elmKLX_W%2Fazure-sso-7.png?alt=media\&token=7b78f0f6-c7ea-4837-847d-2839ee5f2f12)

* In the Avaamo Application-SAML-based sign-on, configure the [Basic SAML Configuration](#basic-saml-configuration), [User Attributes and Claims](#user-attributes-and-claims), [SAML Signing Certificate](#saml-signing-certificate), and [Add Users and Groups](#add-users-and-groups).

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTEX3lgrr5MSV14JToH%2F-MTEi4tecTHDteZxEHnX%2F5.6-saml-groups.png?alt=media\&token=6e9ec5c0-7170-444a-b467-cacf212417e7)

## Configure SAML SSO Application in Azure

After you create a SAML SSO application in MS Azure, you can configure the [Basic SAML Configuration](#basic-saml-configuration), [User Attributes and Claims](#user-attributes-and-claims), [SAML Signing Certificate](#saml-signing-certificate), and [Add Users and Groups.](#add-users-and-groups)

### Basic SAML Configuration

Click edit (pencil icon) in the **Basic SAML Configuration section** and specify the following details:

* **Identifier (Entity ID)**: Enter a unique identifier for your application. Make a note of the Entity ID. You must specify the same when you configure the identity providers in the Avaamo Platform.
* **Reply URL (Assertion Consumer Service URL)**: This is the callback URL of the Avaamo Platform, such as [*https://cx.avaamo.com/dashboard\_user/users/saml/auth*](https://cx.avaamo.com/dashboard_user/users/saml/auth). Contact Avaamo support to get the callback URL.
* **Relay State**: This is usually the URL where you access the SSO. Example: <https://cx.avaamo.com/>.
* Click **Save**.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3L0ey7pfgqmfWxj8K6%2F-M3L2XvaIoejHcC4l4Ef%2Fazure-sso-9.png?alt=media&#x26;token=534e879a-9d7a-4d3d-affd-76c60a648fdc" alt=""></div>

### User Attributes and Claims

Click edit (pencil icon) in the **User Attributes and Claims** section and update the claim name.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTEX3lgrr5MSV14JToH%2F-MTEi4tecTHDteZxEHnX%2F5.6-saml-groups.png?alt=media\&token=6e9ec5c0-7170-444a-b467-cacf212417e7)

* In the **User Attributes & Claims** page, click **Claim name.**

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTEzdhVGousARh_uNuo%2F-MTF3KQmgMVLOAi0p4qw%2F5.6-saml-user-attributes.png?alt=media\&token=48965f26-8e79-42b8-ab42-0c798c2312c5)

* Select **user.mail** in **Source attribute** and click **Save.**

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3LLF6zqLIjqlWqd_7X%2F-M3LVTL4nWpvLxa44G5c%2Fazure-sso-15.png?alt=media\&token=c7e7e4f6-dbcf-42a8-aaac-eb73c808000a)

#### Groups claim policy

* Click claim name associated **user.groups.** The following options are supported:
  * Groups assigned to the application (Recommended): Only those groups that are a part of the application and that the user belongs to is synced with the Avaamo Platform.
  * All groups: All the groups that the user belongs to irrespective of the application is synced with the Avaamo Platform.

### SAML Signing Certificate

Click edit (pencil icon) in the **SAML Signing Certificate** section and verify if the signing algorithm is SHA-256.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3L6i1gjktzFzVazsW9%2F-M3LGt--r8p22Hsir1qd%2Fazure-sso-12.png?alt=media\&token=c1212a05-fd68-46e6-9d9c-5e289fbd3c61)

Download the Certificate (Raw) in your local environment. This certificate must be uploaded to the theAvaamo Admin page under the Single Sign-on URL.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3L6i1gjktzFzVazsW9%2F-M3LI33oFw7SebO4Chew%2Fazure-sso-13.png?alt=media\&token=76a9acc5-3f49-4728-bb58-cf2f17f3c46f)

### Setup Application Roles

Avaamo Platform allows you to create users and associate users to different out-of-the-box roles based on the user's responsibility in the company. See [Roles and Permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.&#x20;

To facilitate seamless user-role management in MS-Azure AD, you must create a few roles in your MS-Azure application and later map these roles to appropriate users and groups. Once mapped, the roles applicable to a user is automatically applied when a user logs in to the Avaamo Platform Dashboard after [MS-Azure SSO integration](#integrate-ms-azure-sso-application-in-avaamo-platform).&#x20;

* Navigate to **App registrations** and click the Application where you wish to add the roles.
* In the selected Application, navigate to **App roles** and create the following roles. Note that the role names are case-sensitive:
  * development
  * testing
  * staging
  * production
  * live\_agent
  * settings
  * broadcast\_read
  * broadcast\_manage
  * broadcast\_send
  * cap\_supervisor

{% hint style="info" %}
**Note**: These roles get mapped to the roles in the Avaamo Platform when you integrate MS-Azure SSO. See [Roles and Permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.&#x20;
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTBi4jsIR2g6a7d7X47%2F-MTEQPZ1U0Wdokk8smQI%2F5.6-saml-app-roles.png?alt=media\&token=914dc174-ff53-4415-82ac-569a4a95a18a)

### Add Users and Groups&#x20;

The next step is to add users and groups to the SSO application.

* Click **Users and Groups** from the left navigation pane.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3LWmaX6rpfCv1tvN-x%2F-M3LZQJq8F4ubdKQUBJ1%2Fazure-sso-16.png?alt=media\&token=54bb09a2-cafb-419d-a5c8-c7e993ba8ec3)

* Search and select for an existing user or group. For creating new users or groups, navigate to **App registrations** and click the **Application** where you wish to add new users or groups.

{% hint style="success" %}
**Key Point**: Instead of managing individual users, you can also create groups with users and assign roles to the groups. If you have added new users, then you can directly assign the users to the group based on their roles and responsibilities.
{% endhint %}

* Select the role you wish to assign to the user or group. Note that you can only select one role at a time. If you wish to assign multiple roles to users or groups, then select user or group again and assign the required role. Repeat the assignment of roles to users or groups as per your requirement. Click **Assign.**

Once you have assigned the user or group, integrate the Azure SAML support on the Avaamo platform.

## Integrate MS Azure SSO application in Avaamo Platform

To integrate the Azure SAML SSO support on Avaamo, follow the steps below:

* Login to Avaamo Platform using credentials with **Settings** role access. Only a user with the **Settings** role can configure the identity provider. See [Roles and Permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
* On the Avaamo dashboard, click the name initials in the top-right corner. Click **Settings**.
* On the **Settings** page, click **Identity Providers** and click **Add New**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LygnlpHVHiRiJW5_6P0%2F-LygqeWXPqZ1i06G9st-%2Fgsuite-sso.png?alt=media\&token=3101fef4-f12d-4cbc-a8e4-1b9473a47be5)

* In the **New Identity Provider** popup window, enter the following details:
  * **Identity Provider Name:** A unique identity provider name for your identification. This name is being displayed in the drop-down list when you are selecting an identity provider for your dashboard users while either creating a new user or editing an existing one. For example, Microsoft Azure, G-Suite, Okta, etc..
  * **App Id / Entity Id:** This Id should exactly match the Entity Id that you have used while configuring single sign-on with your application in the [Basic SAML Configuration](#basic-saml-configuration) section on Microsoft Azure.
  * **Single Sign-On URL:** Copy the Login URL (App Federation Metadata Url) from the [SAML Signing Certificate](#saml-signing-certificate) section of your application configuration on Microsoft Azure and paste it in this section.
  * **Certificate Signature:** Upload the certificate that you have downloaded from the Microsoft Azure SSO application. See the [SAML Signing Certificate ](#saml-signing-certificate)​section, for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lyh2VavEoIAmsKiGe-7%2F-Lyh7a-rEGNN0WQ11U4n%2Fmsazure-sso.png?alt=media\&token=24bd15f4-91bc-4056-a730-7822853200eb)

## Testing Integration

After you configure and integrate MS-Azure SSO with Avaamo Platform, the users are automatically signed in to the Avaamo Platform when they are on their corporate devices and connected to the network.&#x20;

* Roles applicable to a user is automatically assigned when a user logs in to the Avaamo Platform Dashboard. If a user is mapped to multiple groups, then roles assigned to a user is a union of roles from all the groups.
* If you have **Settings** role access, then you can view the groups as per the [groups claims policy](#groups-claim-policy) setup in MS-Azure AD in the Settings -> User & Groups -> Groups page. See [Syncing with Azure AD groups](https://docs.avaamo.com/user-guide/how-to/users-and-permissions/groups#syncing-with-azure-ad-groups), for more information on how to edit and delete groups.
* You can now manage all the users and groups via Azure AD and it is synced when the user logs in to the Avaamo Platform Dashboard. For example, if you assign the roles for a group, then the same is applied to the user when the user logs out and logs back into the Avaamo Platform.&#x20;
* If users logout from the Avaamo dashboard, then the users are logged out from MS-Azure IDP too.

{% hint style="info" %}
**Note**: If the user is already logged in to the Avaamo Platform Dashboard and the same user is updated in the MS-Azure AD, then the user must log out and log back in for the changes to get reflected.&#x20;
{% endhint %}
