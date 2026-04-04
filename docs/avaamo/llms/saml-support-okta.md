# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-okta.md

# SAML Support - Okta

Configure your application on Okta to enable the SAML support-based Single Sign-On. In SAML terminology, you can configure Okta (your SAML Identity Provider or "SAML IdP"), with the details of your application (the new SAML Service Provider or "SAML SP").

## Before you begin

Ensure you meet the following pre-requisites before configuring and integrating the `SAML SSO Okta` application in the Avaamo Platform:

* Administration login credentials for the Okta account
* You have configured the **Settings** roles for your user. Only a user with the **Settings** role can configure Identity providers in the Avaamo Platform. See [Users and Roles](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions), for more information.

## Create SAML Application on Okta

Setup and configure your application on Okta with the steps below:

* Access your Okta organization by logging in as a user with administrative privileges.
* Click on the `Admin` button at the top of the page to enter the administrative interface.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjkELeEFlptUu8i5aobCc%2FScreenshot%2030-08-2024%20at%2019.46.png?alt=media&#x26;token=a0f9b2ec-941a-43a6-bb80-d8e6b0aad9f1" alt=""><figcaption></figcaption></figure>

* Navigate to the `Dashboard>Getting Started` section and click on `Add App`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXGu0rRM2fAWVpjLm1cPc%2FScreenshot%2030-08-2024%20at%2019.50.png?alt=media&#x26;token=d9f936bc-737a-4b6f-9c12-fac7aa2b0eda" alt=""><figcaption></figcaption></figure>

* Click the `Create New App` button to begin the setup process.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6lT3VOMvlgnlr6LwSUbG%2FScreenshot%2030-08-2024%20at%2019.51.png?alt=media&#x26;token=d8f0ee22-c1f6-4c91-9384-541b93a80c36" alt=""><figcaption></figcaption></figure>

* In the `Create a new app integration` popup window, select the radio button for **SAML 2.0** under the `Sign-in method` section.
* Click `Next` .

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjBEDoFGo3kpQAht0D7am%2FScreenshot%202024-08-30%20at%207.30.20%E2%80%AFPM.png?alt=media&#x26;token=cb03df5e-2cdc-4b8a-8e00-25ada9fe530b" alt=""></div>

## Configure SAML Application on Okta

After you create a SAML SSO application in Okta, you can configure the below settings.

### Configure General Settings

* In the `General Settings` screen, enter "Avaamo SAML Application" in the **App name** field.
* Click `Next` .

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ft4RdGWiZqyHJpFF5JRU9%2FScreenshot%2030-08-2024%20at%2020.01.png?alt=media\&token=d8030c41-9c7c-4d85-a280-27f73604e290)

### Configure SAML&#x20;

Under configure SAML, for section A - SAML settings, paste the following URL in the Single sign-on URL and Audience URI (SP Entity ID) fields:

**Single sign-on URL** - [https://cx.avaamo.com/dashboard\_user/users/saml/auth](https://c*.avaamo.com/dashboard_user/users/saml/auth), Here, "cx" in the URL is the Avaamo instance that you are using.\
**Audience URI (SP Entity ID)** - AvaamoApp&#x20;

Under the `Attribute Statements (optional)` section add the following name and value.

* **Name** - user.mail
* **Name format** - Unspecified
* **Value** - nameidentifier

Click `Add Another` to enter the fields for user email:

* **Name** - user.mail
* **Name format** - Unspecified
* **Value** - emailaddress

Click `Add Another` to enter the fields for firstname:

* **Name** - <http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname>
* **Name format** - URI Reference
* **Value** - user.firstName

Click `Add Another` to enter the fields for lastname:

* **Name** -- <http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname>
* **Name format** -- URI Reference
* **Value** -- user.lastName

Click `Add Another` to enter the fields for roles:

* **Name** - <http://schemas.microsoft.com/ws/2008/06/identity/claims/role>
* **Name format** - URI Reference
* **Values** - user.roles

Under the `Group Attribute Statements (optional)` section add the following names and values.

* **Name** - <http://schemas.microsoft.com/ws/2008/06/identity/claims/groups>
* **Name format** - URI Reference
* **Value** - can be the group's name according to your filter preferences.<br>

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVmrkKUCo2orO0UNG7aNp%2FScreenshot%202024-09-02%20at%209.29.05%E2%80%AFAM.png?alt=media&#x26;token=93efac49-f9d9-4a30-ba57-7d4979883f4b" alt=""></div>

* For section B - `Preview the SAML assertion generated from the information above`, Click `Preview the SAML Assertion` to preview and verify your configuration.
* Click `Next` .

{% hint style="info" %}
**Note:**\
The Preview feature can be used to verify changes and SAML assertions. However, the following conditions must be met:

* The user must be logged in.
* The user must be assigned to the app's user list.
* The user must have a group.
* The user must have a role.
  {% endhint %}

### Complete the Setup:

* Under the `Feedback` section, choose the appropriate option (e.g., an Okta customer or a software vendor), and click  "`Finish`."

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXkazEgU5k0vARUUuhYOA%2FScreenshot%2030-08-2024%20at%2020.17.png?alt=media&#x26;token=4ff66dd5-ac2f-4e38-95ea-e6a82ec2502d" alt=""></div>

Under the Feedback tab, use the settings that work best for your company and the application.

* On the General settings page, scroll down to the **App Embed Link** section, now copy the embed link. This URL must be added to the Avaamo UI to configure Okta SAML support.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FxhPLZOIZkJdm7Urz4EMP%2FScreenshot%2002-09-2024%20at%2013.32.png?alt=media&#x26;token=be78c1d7-0b7d-4896-9a64-693e481af4ea" alt=""><figcaption></figcaption></figure>

### SAML Signing Certificate

1. Navigate to `Applications -> Applications.`
2. Select your application and go to the SSO tab.
3. Navigate to the `SAML Signing Certificates` Tab. Click `Actions` and select `Download certificate`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F0PXLljnfcfoHs6uOWVtB%2FScreenshot%202024-09-02%20at%209.19.27%E2%80%AFAM.png?alt=media&#x26;token=34d3b832-1a42-453a-92fb-6568daaae24f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Only **SHA-2 type SAML Signing Certificates** are supported for download.
{% endhint %}

### Setup Application Roles

Adding these roles ensures that Okta correctly sends role information in the SAML assertion, which Avaamo can use to manage user roles and permissions effectively.

1. Navigate to `Profile Editor` the Okta dashboard. Select `Avaamo SAML Application User` app.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F1jidaOI5Cmx9elokPf0n%2FScreenshot%202024-09-02%20at%2010.17.55%E2%80%AFAM.png?alt=media&#x26;token=3d8ca887-9426-49bf-a291-491478ee80b8" alt=""><figcaption></figcaption></figure>

2. Click `Add Attribute` under the `Attributes` Tab.
3. Fill out the details and click `Save` to apply the changes.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLiWjTk0yAwPSIwFm3DSe%2FScreenshot%202024-09-02%20at%2012.03.28%E2%80%AFPM.png?alt=media&#x26;token=65e65e73-d720-4af9-90c0-1afe6b256c51" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="192">Options</th><th>Values</th></tr></thead><tbody><tr><td>Data type</td><td>string array</td></tr><tr><td>Display name</td><td>Roles</td></tr><tr><td>Variable name</td><td>roles</td></tr><tr><td>Description</td><td>Defines the specific roles or access levels assigned to users within the Avaamo platform. These roles determine the user's permissions and access to various features and environments within the application.</td></tr><tr><td>Enum</td><td>Leave this option unchecked.</td></tr><tr><td>Attribute required</td><td>Click the checkbox if you want to make this attribute compulsory</td></tr><tr><td>User permission</td><td>Read-Write</td></tr></tbody></table>

### Assign Application

1. Navigate to the `Directory` tab and click on `People`**.** Select the profile to which you want to assign an application.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSJLD3s11Es45Pt4N0S3P%2FScreenshot%2026-09-2024%20at%2015.08.png?alt=media&#x26;token=e67e09cc-6b2e-4151-8719-6185f945da9a" alt=""><figcaption></figcaption></figure>

2. Click on `Assign Applications`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FFgDUmiYp0XysmM29Z6TL%2FScreenshot%2026-09-2024%20at%2015.09.png?alt=media&#x26;token=4ace3ac7-577f-48ac-a1b4-92b4b1fbcc52" alt=""><figcaption></figcaption></figure>

3. Choose the application you want to assign from the list. Click `Assign`.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fr2jWui7Guzsy0ISGKGgX%2FScreenshot%2026-09-2024%20at%2015.10.png?alt=media&#x26;token=de2d4c6d-2a09-4c02-be6a-f141b2ed1a7d" alt=""><figcaption></figcaption></figure>

4. Click `Done`.

### Add Roles to Users&#x20;

1. Navigate to the `Directory` tab and click on `People`. Select the profile you wish to edit.
2. Navigate to `Profile` tab. Click `edit` under `Attributes` option.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHdmlc1W4L9lG47bkHLD4%2FScreenshot%202024-09-02%20at%2012.33.07%E2%80%AFPM.png?alt=media&#x26;token=8f1f373c-b5b6-4b51-8d8c-bf5209b0933c" alt=""><figcaption></figcaption></figure>

3. Scroll down and find the attribute `Roles` and click `Add Another` to add value to it. \
   Below is the list of platform-supported roles the user can configure. Note that the role names are case-sensitive:\
   broadcast\_manage\
   broadcast\_read\
   broadcast\_send\
   cap\_admin\
   cap\_supervisor\
   development \
   live\_agent \
   production\
   settings \
   staging\
   supervisor\
   testing\
   cap\[Depending on the features enabled for your company]\
   campaign(broadcast) \[Depending on the features enabled for your company]

{% hint style="info" %}
**Note**: These roles get mapped to the roles in the Avaamo Platform when you integrate Okta SSO. See [Roles and Permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmZx27vyOGf6xigIT7Hso%2FScreenshot%2002-09-2024%20at%2012.05.png?alt=media&#x26;token=0709bc2f-94d5-45fb-94a3-83745f2dfb90" alt=""><figcaption></figcaption></figure>

4. Click `Save` to assign roles to the user.

### Add Users to Groups

1. Navigate to `Groups`. It displays all the existing Groups. Select the group you wish to add users.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fr45MCmetBBT6yPZszLUc%2FScreenshot%2002-09-2024%20at%2012.37.png?alt=media&#x26;token=ca08e2a5-475a-4a77-9717-b86628b6ad1a" alt=""><figcaption></figcaption></figure>

2. Click `Assign people`.It displays all the users.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnSGStD2eeVWrGnJWSBZy%2FScreenshot%2002-09-2024%20at%2012.38.png?alt=media&#x26;token=1895b613-83de-4406-9727-ba535eee8971" alt=""><figcaption></figcaption></figure>

2. Click the "+" symbol to add users to the group.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F78WHkQLqtjWzvRoAVpc3%2FScreenshot%2002-09-2024%20at%2012.39.png?alt=media&#x26;token=6aae7ebf-8eb0-4c03-9a2a-b9c39dadc3aa" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Key Point**: Instead of managing individual users, you can also create groups with users and assign roles to the groups. If you have added new users, you can directly assign them to the group based on their roles and responsibilities.
{% endhint %}

Now, let us integrate the application on the Avaamo UI.

## Avaamo Admin SAML Integration

To integrate the Okta SAML SSO support on Avaamo, follow the steps below:

1. Open a new Chrome browser window, and enter cx.avaamo.com(cx is the platform assigned to you).
2. Login with your admin credentials.
3. On the Avaamo dashboard, click on the action over the button (the three dots) for the menu bar. Select **Settings**.\
   On the settings page click on **Identity Providers**.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FoCPKlE3IKNwNwOO3YPWB%2FScreenshot%202024-09-02%20at%201.38.43%E2%80%AFPM.png?alt=media&#x26;token=9ac2ee7b-b4f8-4d32-9815-15016ff29261" alt=""><figcaption></figcaption></figure>

4. Click on Add New. On the **New Identity Provider** popup window, enter the following details:

**Identity Provider Name**-- A unique identity provider name for your identification. This name is displayed in the drop-down list when selecting an identity provider for your dashboard users while creating a new user or editing an existing one. For example, Microsoft Azure, G-Suite, Okta, etc..

**App Id / Entity Id**-- This Id should exactly match the `Audience URI (SP Entity ID)` that you have used while configuring sign-on with your application in the [Configure SAML](#configure-saml) section on Okta.

**Single Sign-On URL**-- Copy the Login URL from the `Embed Link` Section from your application configuration on Okta and paste it in this section.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzoZxqENspGgS43BaRA42%2FScreenshot%2002-09-2024%20at%2020.44.png?alt=media&#x26;token=b24431d6-0fe1-4820-8d7d-298dbf3228b9" alt=""><figcaption></figcaption></figure>

**Certificate Signature**-- Download the raw certificate from ​the [SAML Signing Certificate](#saml-signing-certificate) ​Section from your app configuration on Okta and upload it here.

**Sign request:** This can be unchecked.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FihGNzIGc7VGOLcd7B6e6%2FScreenshot%202024-09-02%20at%201.39.26%E2%80%AFPM.png?alt=media&#x26;token=1d3dd7df-4bb0-4d1e-bcb4-9cc8fbc3dd1e" alt=""><figcaption></figcaption></figure>

### **Assign an Identity Provider to a User**

Once the application is configured on Okta and integrated with the Avaamo platform, assign the identity provider to a user for an SSO login.

1. Navigate to the Users and Groups sub-tab.
2. Select the user you want to assign the SSO login, click on the action over the button under actions, and click on edit.
3. On the popup window, under **Authentication Identity Provider** select Okta from the drop-down list.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FCYSDFZOwQzzo5oFJ7YjL%2FScreenshot%2002-09-2024%20at%2013.52.png?alt=media&#x26;token=d5fd4a0e-0675-47bc-98ee-e883ce37474b" alt=""><figcaption></figcaption></figure>

## Testing Integration

After you configure and integrate Okta SSO with Avaamo Platform, the users are automatically signed in to the Avaamo Platform when they are on their corporate devices and connected to the network.

* Roles applicable to a user are automatically assigned when a user logs in to the Avaamo Platform Dashboard. If a user is mapped to multiple groups, then roles assigned to a user are a union of roles from all the groups.
* You can now manage all the users and groups via Okta and it is synced when the user logs in to the Avaamo Platform Dashboard. \
  For example, if you assign the roles for a group, then the same is applied to the user when the user logs out and logs back into the Avaamo Platform.
* If users log out from the Avaamo dashboard, then the users are logged out from Okta too.
