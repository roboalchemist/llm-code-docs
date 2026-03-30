# Source: https://docs.mailtrap.io/account-and-organization/management/sso/azure-microsoft-entra.md

# Azure (Microsoft Entra)

## Overview

This guide walks you through configuring SAML-based Single Sign-On (SSO) between Azure Active Directory (Microsoft Entra) and Mailtrap.

## Configure Single Sign-On with Azure

### Create an Enterprise application

{% stepper %}
{% step %}
Open your Azure Active Directory and select **Enterprise applications**
{% endstep %}

{% step %}
Add a new application by clicking the **+ New application** button

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FH3G2frc29yvbNloKtJ25%2Fsetup-sso-with-azure-1.png?alt=media&#x26;token=f41b70e5-b9c8-4a39-b541-81ec7c3e379d" alt="" width="375"></div>
{% endstep %}

{% step %}
Choose **+ Create your own application**, enter the name of the application (e.g., "Mailtrap"), and select **Integrate any other application you don't find in the gallery (Non-gallery)**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F63Fk9Idem668CGJP7LF9%2Fsetup-sso-with-azure-2.png?alt=media&#x26;token=bec59cf3-792c-41b9-aead-ca9f68f837d8" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

### Set up Single Sign-On

After the application has been created, you can set up single sign-on:

{% stepper %}
{% step %}
Choose **Set up single sign-on** in the **Getting Started** section

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fn7ezSpWQAFiVooH0abOD%2Fsetup-sso-with-azure-3.png?alt=media&#x26;token=d010bd92-b632-419b-8ae9-7faa151598e1" alt=""></div>
{% endstep %}

{% step %}
For **Single Sign-on** mode, select **SAML** based Sign-on

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FDRKhjj2zaEpCamUQIec1%2Fsetup-sso-with-azure-4.png?alt=media&#x26;token=14c75c9f-b1ea-4776-b4b3-a2ed4bed814f" alt=""></div>

Follow the steps on the SSO with SAML screen. Azure AD has a detailed [configuration guide](https://docs.microsoft.com/en-gb/azure/active-directory/manage-apps/configure-single-sign-on-non-gallery-applications) at the top of the page for further guidance.
{% endstep %}
{% endstepper %}

### Basic SAML configuration

Click edit in the dropdown menu and provide the following SAML Provider details to your Azure from Mailtrap:

* **Entity ID** → Identifier (Entity ID)
* **Assertion Consumer Service URL** → Reply URL (Assertion Consumer Service URL)
* **Single Logout Service URL** → Logout URL

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FVQepfCpqQ5L8O54TQZxn%2Fsetup-sso-with-azure-5.png?alt=media&#x26;token=c040bf24-9287-4ddb-aff3-d3ae8f497c61" alt="" width="563"></div>

### User attributes and claims

In the User Identifier field, enter **user.mail**.

### SAML signing certificate

{% stepper %}
{% step %}
Click **Edit** and choose **SHA-1** Signing Algorithm
{% endstep %}

{% step %}
Click **Save**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F5jVKRNWKoDBB2VOh7BVV%2Fsetup-sso-with-azure-6.png?alt=media&#x26;token=dd80cb0e-88a0-4f37-946a-07215d7df161" alt="" width="375"></div>
{% endstep %}

{% step %}
Download **Certificate (Base64)**
{% endstep %}

{% step %}
Open it in any text editor and copy its content
{% endstep %}

{% step %}
Paste the certificate content into the Mailtrap **X509 Certificate** field
{% endstep %}
{% endstepper %}

### Identity provider details

Provide the following to Mailtrap from Azure:

* **IdP Entity ID** (Identity Provider Issuer) → Azure AD Identifier
* **Single Sign-on URL** → Login URL
* **Optional: Single Logout Service (SLO) URL** → Logout URL

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F7wF0QDeFPl1R3HfOluc6%2Fsetup-sso-with-azure-7.png?alt=media&#x26;token=ac90eb0a-7388-4a67-83e5-4b885e29e19f" alt="" width="563"></div>

Now you can save your SAML configuration on Mailtrap.

### Assign Users and Groups

With SAML configuration complete, you need to add users or groups to your application in Azure:

{% stepper %}
{% step %}
Click **Users and groups** on the left sidebar
{% endstep %}

{% step %}
Click on **+ Add User → Users and Groups**
{% endstep %}

{% step %}
Select all users you want to add to the application and click **Select**
{% endstep %}
{% endstepper %}

## Permissions

By default, we create users with no permissions. If you want the user to be automatically assigned to Account Admin or Account Viewer role, you need to set up the role mapping.

### Configure role mapping in Mailtrap

In the following example, we assign the roles depending on the **title** attribute value:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FnDx75vBlNMFmXDKr90j6%2Fsetup-sso-with-azure-8.png?alt=media&#x26;token=819d1b85-4158-49a1-a079-ab3924ce00e3" alt="" width="375"></div>

### Configure attributes in Azure

{% stepper %}
{% step %}
Navigate to **Attributes & Claims**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FPaEERfQLfzIAVD3oGdB1%2Fsetup-sso-with-azure-9.png?alt=media&#x26;token=77e4da62-1edd-43a1-aa67-3cb6f8b631d4" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Add new claim**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FzptgvMI50DVFQPq8M68R%2Fsetup-sso-with-azure-10.png?alt=media&#x26;token=e74db03a-749d-4dd2-b2af-abba0c8596c0" alt="" width="375"></div>
{% endstep %}

{% step %}
Add the **title** claim with the appropriate source attribute (e.g., **user.jobtitle**)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fg9GNFooHahMzkgiptgR8%2Fsetup-sso-with-azure-11.png?alt=media&#x26;token=14706ff6-a689-4b90-8de3-974a589337c4" alt="" width="375"></div>
{% endstep %}

{% step %}
Click **Save**
{% endstep %}
{% endstepper %}

Your Azure SSO configuration with role mapping is now complete.
