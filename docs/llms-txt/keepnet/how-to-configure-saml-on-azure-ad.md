# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-azure-ad.md

# How to Configure SAML on Azure AD

This document explains the steps of integrating the Azure AD identity provider with the platform over SAML to log in to the platform by using your Azure AD account.

## **Azure AD Settings**

Please follow the steps below to set up SAML settings correctly on the Azure AD side.

* Log in to the Azure AD with a privileged account that can create applications.
* Go to the **Azure Active Directory** panel from the main dashboard.
* Click on **Enterprise Applications > New Application > Create your own application** and then fill out the following fields.
  * **Name of the application:** Please write the name of the application.
  * **Type of the application:** Select the **"Integrate any other application you don't find in the gallery (Non-gallery)"** option.
* Click the **Create** button to create the application.

After the application is created, please follow the steps below.

* Click on the **Single Sign On** option on the application menu on the left.
* Click on the **SAML** option.
* On the **Setup Single Sign-On with SAML** page, choose the **Upload metadata file** option.
* Leave the Azure AD settings open. Now log into the platform and navigate to **Company > Company Settings > SAML Settings**.
  * Click the **+ NEW** button. Keep this page also open, as you'll need the settings throughout this process.
  * Go to the "**SAML Configuration For Your Identity Provider"** section and click on the "**Download Metadata"** button to download the metadata file.
* Return to Azure AD settings and upload the metadata file you downloaded by selecting the "**Upload Metadata File"** option.
* A pop-up for **"Basic SAML Configuration"** will appear. Save your changes and close this pop-up.
* Make sure you are still on the **"Set up Single Sign-On with SAML"** page and go to the **"Attributes & Claims"** section:
  * Click on the existing rule under "**Required claim"**, change the "**user.principalname"** to **"user.mail",** and save.
  * Delete the **four existing rules** under the **"Additional Claims"**.
  * At the top of the page, click on the **"+ Add New Claim"** button and create the following claims:
    * **First Claim**: Name it "**firstName**" with the source attribute "**user.givenname**". Leave the "**Namespace**" field empty and save.
    * **Second Claim**: Name it "**lastName**" with the source attribute "**user.surname**". Leave the "**Namespace**" field empty and save.
    * **Third Claim**: Name it "**phoneNumber**" with the source attribute as either "**user.mobilephone**" or "**user.telephonenumber**". Leave the "**Namespace**" field empty and save.
* Under the "**SAML Certificates**" field, click on the "**Federation Metadata XML"** button to download the XML file.
* Return to the SAML settings tab you left open on the platform. Upload the XML file by clicking the "**Upload Metadata"** button under **"SAML Configuration For Keepnet Labs"**.
* While still on the SAML settings page, enter a "**Name"** for your SAML settings. Also, in the "**Allowed Domains"** field, add your email domain and click the **+ Add** button to include it in the allowed domains list.
* Click the **Save** button at the bottom of the SAML settings page to create SAML settings on the platform.
* Navigate back to the SAML settings in Azure AD. Under "**Users and Groups"**, add the admin user who will log in to the platform with Single Sign-On (SSO).

## **How to Test SAML Configuration**

Check whether the configuration works or not by following the steps below.

* Make sure the admin who will log in to the platform over SAML is created in the platform under the **Company > System Users** page.
* Go to the platform login page.
* Enter the email address. The email **domain** must be defined in the SAML settings under the **"Allowed Domains"** list.
* The platform will redirect you to the Azure AD SSO page to authenticate.
* If the authentication is verified, the user will be redirected to the platform, and the login step will be completed.

## How to Assign Different Roles to Users over SAML

Let's assume there are three administrators who will manage the platform, each with different roles and privileges. The example table below shows that Josh will have the default Company Admin role, which does not include privileges to create sub-companies and many other privileges compared to Reseller users.

<table><thead><tr><th width="168">User's Name</th><th>User's Permission</th></tr></thead><tbody><tr><td>Josh</td><td>Company Admin</td></tr><tr><td>William</td><td>Reseller</td></tr><tr><td>Robert</td><td>Reseller</td></tr></tbody></table>

In this example, let's follow the steps below.

* Log in to the platform. Navigate to **Company > Company Settings > SAML Settings** and modify your SAML settings.
  * At the bottom of the page, change the **Default** **Role** to **"Company Admin."** Users without the "**spRole**" defined in Azure AD will be assigned the **Company** **Admin** role by default when authenticated over SAML.
* Go to Azure AD and access the **SAML application settings**.
* Click on **Single Sign-On** from the left menu.
* Navigate to "**Attributes & Claims"** and click the Edit button.
* Click the "**+ Add New Claim"** button and configure the following:
  * Name it "**spRole**".
* Select the **Source** as "**Transformation**".
  * From dropdown, select the **Transformation** as **"Contains()".**
  * **Parameter 1 (input)** will be in **Attribute** format.
  * **Attribute Name** will be **"user.userprincipalname".**
  * For **Value** field, please write the **William's** **email** **address** who is Reseller.
  * **Parameter 2 (Output)** will be **Attribute** format.
  * **Attribute Name** will be "**Reseller**".
  * For William, that's all we do. Now let's repeat the same steps for Robert.
  * Click **+ Add Transformation** button and select the **Transformation** as **"Contains()"**.
  * **Value** will be **Robert's email address** such as "<robert@test.com>"
  * **Parameter 2 (Output)** will be **Attribute**.
  * **Attribute Name** will be "**Reseller**".
* Click the "**Add**" button to add your additional claim.
* To test the settings, ask William, Robert, and Josh to log in to the platform and check their roles.

Now, the William and Robert who will log in to the platform over SAML will have the Reseller role. The other users who will log in to the platform over SAML will have the default role which is Company Admin.

You can do this with any permission. You can create a [custom role](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles) in the platform and define the custom role name instead of Reseller and the users will login to the platform over the specified custom permission role.

## Video Tutorial

This video tutorial shows the above documentation steps for integrating the Azure AD identity provider with the platform over SAML to log in to the platform by using your Azure AD account.

{% embed url="<https://youtu.be/RXml1fc_-KY>" %}
