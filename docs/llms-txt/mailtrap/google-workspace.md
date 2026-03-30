# Source: https://docs.mailtrap.io/account-and-organization/management/sso/google-workspace.md

# Google Workspace

## Overview

This guide walks you through configuring SAML-based Single Sign-On (SSO) between Google Workspace and Mailtrap.

## On Google Admin side

### Access the Apps section

{% stepper %}
{% step %}
Go to **Apps** in the **Google Admin console**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fauq1VsOyQV3Ug1LF4Vhz%2Fsetup-sso-with-google-workspace-1.png?alt=media&#x26;token=d96fedd1-f20b-4c59-b417-57bd776e7de8" alt="" width="375"></div>
{% endstep %}

{% step %}
Navigate to **Web and mobile apps**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FXPMvdRKDZEImFwA7PQpS%2Fsetup-sso-with-google-workspace-2.png?alt=media&#x26;token=846d76b2-825d-4e20-9a97-9feafd69b126" alt="" width="375"></div>
{% endstep %}
{% endstepper %}

### Create a custom SAML app

{% stepper %}
{% step %}
Navigate to the **Web and mobile apps** section in Google Admin.
{% endstep %}

{% step %}
Click the **Add app** dropdown button to see available app options.
{% endstep %}

{% step %}
Select **Add custom SAML app** from the dropdown menu.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FzzIN5JEn9X0E3oS6ctq6%2Fsetup-sso-with-google-workspace-3.png?alt=media&#x26;token=25598f52-358d-49ad-9e8d-b025e401ba7b" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

### Copy Google identity provider details

Google will provide you with the following SAML configuration details. Copy these values to use in Mailtrap:

* **SSO URL**
* **Entity ID**
* **Certificate**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FoQy4uqOExto7BOtIuLH1%2Fsetup-sso-with-google-workspace-4.png?alt=media&#x26;token=f85ce951-2254-48f2-a6be-6390581f1092" alt="" width="375"></div>

### Configure service provider details

Provide the following SAML Provider details to Google from Mailtrap:

* **ACS URL** → Assertion Consumer Service URL from Mailtrap
* **Entity ID** → Entity ID from Mailtrap

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FkJ79ZkYpni7xGFc7bom4%2Fsetup-sso-with-google-workspace-5.png?alt=media&#x26;token=6e158dbe-bdc7-4bfa-87a6-27e08ac9c957" alt="" width="375"></div>

### Verify the application

After configuration, your SAML app will appear in the Web and mobile apps list:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FRNxupZ9ou7WFS95Uw73a%2Fsetup-sso-with-google-workspace-6.png?alt=media&#x26;token=495b50ab-0b77-4010-9cc7-551729e79caa" alt="" width="563"></div>

### Review the configuration

You can review the service provider details and configure attribute mapping:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FnCTFQHlFn2lb1kC2wJmm%2Fsetup-sso-with-google-workspace-7.png?alt=media&#x26;token=3acde508-db45-42c8-8169-42ada8625d22" alt="" width="563"></div>

### Enable the application

Turn on the SAML app for your users:

{% stepper %}
{% step %}
Go to the **Service Status** section for your SAML app.
{% endstep %}

{% step %}
Select **ON for everyone** to enable the app for all users, or choose specific organizational units if you want to limit access.
{% endstep %}

{% step %}
Click **Save** to apply the changes and enable the application.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FFbyTDddpi5GtLIe9JKrV%2Fsetup-sso-with-google-workspace-8.png?alt=media&#x26;token=0a69836b-a272-434c-ba8f-d0fbfb87b03e" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

## Permissions

By default, we create users with no permissions. If you want the user to be automatically assigned to Account Admin or Account Viewer role, you need to set up the role mapping.

### Configure role mapping

In the following example, we assign the roles depending on the **Type** of employee attribute value.

#### Configure attribute mapping in Google

{% stepper %}
{% step %}
Click **SAML attribute mapping**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Ff219KSZQb0SKAItE3PC9%2Fsetup-sso-with-google-workspace-9.png?alt=media&#x26;token=76f8ec1e-5493-4e1e-8a5e-b2e575457b3e" alt="" width="375"></div>
{% endstep %}

{% step %}
Map the **Google Directory attribute** to the **App attribute**

* **Google Directory attributes**: Employee Details > Type
* **App attributes**: Type

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FiL3EU1uzeUM2bxrGbNP9%2Fsetup-sso-with-google-workspace-10.png?alt=media&#x26;token=63d88680-cf04-4b8a-83d6-28781bc6a6b3" alt="" width="563"></div>
{% endstep %}

{% step %}
Save your attribute mapping configuration.
{% endstep %}
{% endstepper %}

#### Set employee type in Google Directory

In the **Google Directory** user profile, set the **Type of employee** field (e.g., "Admin", "Viewer"):

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FalVfthPMIOyitxAoiLMk%2Fsetup-sso-with-google-workspace-11.png?alt=media&#x26;token=66b3237f-fa97-45db-85ea-51c5c022c9d3" alt="" width="375"></div>

#### Configure role mapping in Mailtrap

In Mailtrap SSO settings, map the **Type** attribute to the appropriate Mailtrap roles (Admin, Viewer)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FzL9kQtTrxiPXcgwfigwZ%2Fsetup-sso-with-google-workspace-12.png?alt=media&#x26;token=6d55dcec-e1a0-4261-a3d5-268a85303875" alt="" width="563"></div>

Your Google Workspace SSO configuration with role mapping is now complete.
