# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-scim/scim-setup-in-okta.md

# SCIM Setup in Okta

The document show step-by-step how to synchronize users' information from the Okta identity provider to the platform.

Please make sure to set up the mandatory settings from the ‘[Getting Started](https://app.gitbook.com/o/-LMcQ_WBbT5jibln-2Mt/s/lKFxOYqYqSykikkXpwjG/next-generation-product/getting-started/2.-add-target-users/step-2-add-target-users/scim-integration/okta-scim-integration)’ page in this document before proceeding to the following step.

## **OKTA Configuration** <a href="#okta-configuration" id="okta-configuration"></a>

1. Please log in to <https://www.okta.com/> as an admin user.
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

## **Synchronization Users or Groups** <a href="#synchronization-users-or-groups" id="synchronization-users-or-groups"></a>

1. Go to the **Assignments** menu and click on the **Assign** button to assign **Users or Groups** to this SCIM application which will be synchronized to the platform.
2. To import **user(s)** or **group(s)**, click on the **Assign** button to synchronize users or groups to synchronize to the platform.

✅ **You have now added your first Target Users. Now you need to**[ **ensure they are able to receive emails from Keepnet**](https://github.com/ucarozan/keepnet-docs/blob/main/next-generation-product/getting-started/3.-email-deliverability) **successfully ➡️**

### Tutorial Video <a href="#tutorial-video" id="tutorial-video"></a>

This video tutorial shows the documentation steps for synchronizing users' information from the Okta identity provider to the platform.

{% embed url="<https://youtu.be/3XXAkrxhAm4>" %}
