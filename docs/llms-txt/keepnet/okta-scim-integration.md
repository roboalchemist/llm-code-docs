# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/okta-scim-integration.md

# Okta SCIM Integration

The document show step-by-step how to synchronize users' information from the Okta identity provider to the platform.

Please make sure to set up the mandatory settings from the ‘[Getting Started](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/getting-started-with-scim)’ page in this document before proceeding to the following step.

## **OKTA Configuration**

1. Please log in to [https://www.okta.com/](https://www.okta.com) as an admin user.
2. Click on **Applications** and go to **Applications** from the left menu.
3. Click on the **Browse App Catalog** and search **SCIM 2.0 Test App (OAuth Bearer Token)** and then click **Add** button.
4. Enter a name for the application like **My SCIM Integration** and click on the **Next** button.
5. Choose **SAML 2.0** with the default settings and click on the **Done** button.
6. The application is now created successfully, go to the **Provision** menu and click the **Configure API Integration** button and then enable the **API Integration** option.
   1. **Tenant URL:** <https://scim-api.keepnetlabs.com/scim>
   2. **Secret Token:** Enter the token which was created on the platform.
   3. Click the **‘Test API Credentials’** button to test your configuration. If it’s successful, click the **Save** button to save settings.
   4. While on the **Provisioning** menu, go to the **‘To App’** menu and click the **Edit** button to enable the following fields. Please make sure to click the **Save** button after enabling the following fields.
      1. Create Users
      2. Update User Attributes
      3. Deactivate Users.

Okta configuration has been successfully finished. You can proceed with the following step.

## **Synchronization Users or Groups**

1. Go to the **Assignments** menu and click on the **Assign** button to assign **Users or Groups** to this SCIM application which will be synchronized to the platform.
2. To import **user(s)** or **group(s)**, click on the **Assign** button to synchronize users or groups to synchronize to the platform.

## How to Sync Okta User Groups Directly to the Keepnet Platform

If you have user groups defined in your Okta environment and wish to sync them — including the users in those groups — directly to the Keepnet platform, please follow the steps below.

#### Steps for Keepnet Platform

1. Log in to the **Keepnet platform.**
2. **Go to** `Company > Company Settings > SCIM Settings`.
3. **Click** `+ NEW`, **enter a name**, and then **click** `Next`.
4. On the **Group** **Settings** page, enable the **"Synchronize groups with Identity Management Platform"** option and click **Save**.
5. **Copy the SCIM token** to your notepad for later use.

#### Steps for Okta Platform

1. **Complete all steps in the** [**OKTA Configuration**](#okta-configuration) **section first**, then return to this section after successfully connecting Okta to Keepnet.
2. **After successful integration**, open your **Okta dashboard** and go to the **Push Groups** menu of your SCIM 2.0 application.
3. **Add the target groups** from your Okta directory to the **Push Groups** menu. This will initiate the synchronization process.
4. **Wait for synchronization** — typically within a few seconds to a few minutes, the groups and associated users will be synced to the Keepnet platform.
5. **Log in to the Keepnet platform** and navigate to:`Company > Target Users > Groups`
6. **Verify** that the Okta groups have been successfully synced. You should see both the groups and their respective users listed.

## Tutorial Video

This video tutorial shows the documentation steps for synchronizing users' information from the Okta identity provider to the platform.

{% embed url="<https://youtu.be/3XXAkrxhAm4>" %}
