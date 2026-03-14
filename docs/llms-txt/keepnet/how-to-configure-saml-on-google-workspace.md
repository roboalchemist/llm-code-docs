# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-google-workspace.md

# How to Configure SAML on Google Workspace

This document explains the steps of integrating the Google Workspace identity provider with the platform over SAML to log in to the platform by using your Google Workspace email account.

## **Google Workspace Settings**

Please follow the steps below to set up SAML settings correctly on the Google Workspace side.

* Log in to [Google Workspace](https://admin.google.com) with a privileged account that can create applications.
* Go to the **Directory > Users > More Options > Manage custom** **attributes** menu from the main dashboard.
* Click on **Add Custom Attributes** and add the following attribute.
  * **Category:** SAMLRole
  * **Description:** Add a description to the custom attribute for your reference.
  * Under **"Custom Fields"** header
    * **Name:** spRole
    * **Info Type:** Text
    * **Visibility:** Visible to the organization
    * **No. Of Values:** Single value
* You can set a role name for specific users. To do that:
  * Go to the **Users** page and **click on** the selected user.
  * **C**lick the **User Information** page.
  * Scroll down to find **spRole**. You can click on it and set custom SAML role name such as Company Admin, Reseller or if you created a custom role on the platform, you can define the role name to here as well.
    * If a value is not set to spRole such as Company Admin, the system will assign the default role for the user after login to the platform that admin is specified on the platform SAML settings. **You may also skip this step for now and then revisit it if needed.**
* Now, go to **Dashboard > Apps > Web and mobile apps > Add App > Add custom SAML** **app** and then follow the steps below.
  * **Name:** Write SAML name.
  * Click the **Continue** button.
  * Click the **Download Metadata** button and then click the **Continue** button.
  * **ACS URL:** Please login to the platform and go to **Company > Company Settings > SAML Settings** **>** click **+ NEW** and then see the **"SSO Sign-in URL"** field at the bottom of the page. Please write the related URL on **Google's ACS URL** page.
  * **Entity ID:** Please login to the platform and go to **Company > Company Settings > SAML Settings** **>** click **+ NEW** and then see the **"Idp Entity ID"** field at the bottom of the page. Please write the related URL on **Google's Entity ID** page.
  * Click the **Continue** button.
  * Add the following attributes by clicking the **ADD MAPPING** button.
    * Primary Email > email
    * First name > firstName
    * Name Last name > lastName
    * Phone number > phoneNumber
    * spRole > spRole
  * Click the **Finish** button.
* Go to the SAML app settings that is created and then click on **User Access.**
  * If you want everyone in the organization to be able to log in to the platform, enable the **‘On for everyone’** option.
  * If you want a few users in the organization to be able to log in to the platform, you can make a group of those users and assign the group to the SAML app.

## **Platform Settings**

Log in to the platform with the privileged user who can access the SAML settings on the platform and then follows up on the document here to fill up the required fields.

Please follow the steps below to set up SAML settings correctly on the platform.

* Log in to the platform with a privileged user who can access SAML settings.
* From the left menu, under **Company heading**, click on **Company Settings -> SAML Settings**.
* Click on the **“Create your first SAML configuration”** button in the middle of the page.
* Then, fill in the following details when the **"New SAML Configuration"** field is opened.
  * **SAML Name:** Enter a name for SAML setting.
  * **Allowed Domains:** Enter the domain name that the admin will be using to log in to the platform. The platform will recognize the user with the domain and redirect to the SSO authentication.
  * **SAML Configuration For Keepnet Labs:** By clicking the **"Upload Metadata"** button under this field and then uploading the **Google Workspace metadata file** to the platform. According to the information in the metadata, the "Issuer URL of the IdP", "IdP SSO URL" and "IdP Certificate" fields will be filled automatically.
  * **Default Role:** Assign a default role to the users who will log in to the platform. If this option is not enabled, the user must have the **‘spRole’** attribute configured in the Google Workspace with the correct system role name to log in to the platform.

## **How to Test SAML Configuration**

Check whether the configuration works or not by following the steps below.

* Make sure the admin who will log in to the platform over SAML is created in the platform under the Company > System Users page.
* Go to the login page of the platform.
* Enter the email address. The email **domain** must be the one that is defined in the SAML settings.
* The platform will redirect you to the Google Workspace SSO page to authenticate.

## Video Tutorial

This video tutorial shows the above documentation steps for integrating the Google Workspace identity provider with the platform over SAML to log in to the platform by using your Google Workspace email account.

{% embed url="<https://youtu.be/y8MKhEXHCmw>" %}
