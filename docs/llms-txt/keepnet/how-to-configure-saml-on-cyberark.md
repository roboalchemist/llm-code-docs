# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-cyberark.md

# How to Configure SAML on CyberArk

This document explains the steps of integrating the CyberArk identity provider with the platform over SAML to log in to the platform by using your CyberArk account.

## CyberArk **Settings**

Please follow the steps below to set up SAML settings correctly on the CyberArk side.

* Log in to the CyberArk with a privileged account that can create applications.
* Click on the **User Portal** icon from the main dashboard and then click **Admin** **Portal**.
* Click on **Apps & Widgets** from the left menu and then click **Web Apps**.
* Click on **Add** **Web** **Apps**, select **Custom** option and then scroll a bit down to **add** **SAML**.
* Select your organization or leave it empty. Click the **Yes** button to add the application.
* Fill out the following fields.
  * **Name:** Please write the name of the application.
  * **Description:** Please write the description of the application.
* Click the **Save** button to save the application settings.
* Go to the **Trust** menu and then **download** **the** **Metadata** **File** of CyberArk.
* Now, **login** **to the** Keepnet **platform** and go to **Company > Company Settings > SAML Settings**. Click **+ NEW** button to create SAML settings.
* Fill out the following fields.
  * **SAML Name:** Enter a name for the SAML settings.
  * **Allowed Domains:** Enter the domain name that the admin will be using to log in to the platform. The platform will recognize the user with the domain and redirect to the SSO authentication. Please make sure to click the **+ ADD** button to add the domain to the SAML settings.
  * **SAML Configuration For Keepnet:** By clicking the **"Upload Metadata"** button under this field and then uploading the CyberArk metadata file to the platform. According to the information in the metadata, the "Issuer URL of the IdP", "IdP SSO URL" and "IdP Certificate" fields will be filled automatically.
  * **SAML Configuration For Your Identity Provider:** Download the metadata file from the platform to upload to CyberArk.
* Return to **CyberArk** **SAML** **application** **settings** page, under **"Service Provider Configuration"**, please upload the metadata file that is downloaded from the platform.
* Click the **Save** button to apply changes.
* Go to **Permissions** menu on the CyberArk SAML settings page and then **add the users** who are going to login the platform over SAML authentication. Please make sure the added users has **"Run"** and **"Automatically Deploy"** options selected.
* Click the **Save** button to apply changes.
* Return back to the platform and confirm the last setting, which is the **Default** **Role** of the users who will be logged in to the platform. This is by default **"Company Admin"** role, you may change it depends on your needs.
  * **Default Role:** Assign a default role to the users who will log in to the platform. If this option is not enabled, the user must have the **‘spRole’** attribute configured in the CyberArk with the correct system role name to log in to the platform.
* Click the **Save** button to create the SAML settings on the platform.

## **How to Test SAML Configuration**

Check whether the configuration works or not by following the steps below.

* Make sure the admin who will log in to the platform over SAML is created in the platform under the **Company > System Users** page.
* Go to the platform login page.
* Enter the email address. The email **domain** must be defined in the SAML settings under the **"Allowed Domains"** list.
* The platform will redirect you to the CyberArk SSO page to authenticate.
* If the authentication is verified, the user will be redirected to the platform, and the login step will be completed.
