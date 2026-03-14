# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-okta.md

# How to Configure SAML on Okta

This document explains the steps of integrating the Okta identity provider with the platform over SAML to log in to the platform by using your Okta account.

## **Okta Settings**

Please follow the steps below to set up SAML settings correctly on the Okta side.

* Log in to Okta with a privileged account that can create applications.
* Go to the **Applications > Applications** menu from the main dashboard.
* Click on **Create App Integration,** select **SAML 2.0**, and then click the **Next** button.
* Enter the **App** **Name** and click **Next**.
* Enter the following information and click **Next**.
  * **Single sign-on URL:** <https://api.keepnetlabs.com/api/saml/assertion>
  * **Audience URI (SP Entity ID):** KeepnetLabs
  * **Name ID format:** EmailAddress
  * **Application username:** Email
* Select the **App Type** as **Internal** **App** and click **Finish**.
* Click the **View SAML setup instructions** button on the right side of the opened page.
* Copy the following information to your notepad and download the certificate.
  * **Identity Provider Single Sign-On URL:**
  * **Identity Provider Issuer:**
  * **X.509 Certificate:**
* Please go to your **Application** **settings** and then the **Assignments** menu. Add the users here who will log in to the Keepnet platform over SAML.

That's it for Okta settings. Now, we need to do the rest of the SAML settings on the Keepnet platform.

## **Platform Settings**

Log in to the platform with the privileged user who can access the SAML settings, and then follow up on the document here to fill out the required fields.

* Log in to the platform with a privileged user who can access SAML settings.
* From the left menu, under **Company** heading, click on **Company Settings > SAML Settings**.
* Click on the **“Create your first SAML configuration”** button in the middle of the page.
* Then, fill in the following details when the **"New SAML Configuration"** field is opened.
  * **SAML Name:** Enter a name for the SAML setting.
  * **Allowed Domains:** Enter the domain name that the admin will be using to log in to the platform. The platform will recognize the user with the domain and redirect to the SSO authentication.
  * **Issuer URL of the IdP:** Enter the **"Identity Provider Issuer"** address that you noted from the Okta SAML instructions page.
  * **IdP SSO URL:** Enter the **"Identity Provider Single Sign-On URL"** address that you noted from the Okta SAML instructions page.
  * **Upload Certificate:** Upload the Okta SAML certificate.
  * **Default Role:** Assign a default role to the users who will log in to the platform. If this option is not enabled, the user must have the **‘spRole’** attribute configured in the Okta with the correct system role name to log in to the platform.

## **How to Test SAML Configuration**

Check whether the configuration works or not by following the steps below.

* Make sure the system admin who will log in to the platform over SAML is created in the platform under the **Company > System Users** page.
* Go to the platform login page.
* Enter the email address. The email **domain** must be the one that is defined in the SAML settings.
* The platform will redirect you to the Okta SSO page to authenticate.

You have now successfully logged in to the platform.

## How to Assign Custom System User Roles on Okta over SAML

This section explains how to pass a role value from Okta to Keepnet Platform using a SAML attribute, so specific system users can sign in with custom roles, while everyone else keeps the default role.

### Okta Settings

Follow the steps below to add a role attribute to Okta users, then send it to Keepnet in the SAML assertion.

#### 1) Create a custom user attribute in Okta

1. Log in to the **Okta Admin Dashboard**.
2. Go to **Directory**, then **Profile Editor**.
3. Open the **User default profile**, identify where you want the attribute, and click **Add Attribute**.
4. Fill in the attribute details:
   1. **Data Type:** String
   2. **Display name:** Keepnet Role
   3. **Variable name:** KeepnetRoleName
   4. Optional, if you want a dropdown: define enum values that match the role names in Keepnet Platform exactly.
5. Click **Save**.

{% hint style="info" %}
The value you set for a user must match the **Keepnet role name** exactly, for example Basic Role, Training Role.
{% endhint %}

#### 2) Add the role attribute to the Keepnet SAML application

1. Go to **Applications**, then **Applications**.
2. **Open the** **SAML application** you created for Keepnet Platform.
3. Go to **General**, click **Edit** in the **SAML Settings** section.
4. In the **Configure** **SAML** step, find **Attribute** **Statements**.
5. **Add an attribute** statement:
   1. **Name:** spRole
   2. **Value:** user.keepnetRole
   3. Click **Next**, then **Finish**.

{% hint style="warning" %}
If you used a different variable name than KeepnetRoleName, use that in the Value field, for example user.yourAttributeName.
{% endhint %}

#### 3) Set role values for specific users in Okta

1. **Find the Okta user** profile for each user.
2. **Set Keepnet Role**, meaning **KeepnetRoleName**, to the target Keepnet role name.

### Platform Settings

1. **Log in to Keepnet Platform** with a privileged user who can access SAML settings.
2. Go to **Company**, then **Company** **Settings**, then **SAML** **Settings**.
3. Set **Default Role** to **Company** **Admin**, so admins without **spRole** still get the usual role.
4. Make sure the system users exist under **Company**, then **System** **Users**, using the same emails they will use through SSO.

Keepnet behaviour to rely on:

1. **System Users without spRole** use the **Default** **Role** when authenticated over SAML.
2. To log in without a default role, the user must have **spRole** configured with the correct custom role name.
3. You can use custom roles as long as the role name you send matches the custom role name in the platform.
