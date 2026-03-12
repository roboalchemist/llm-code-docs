# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-scim/scim-setup-in-jumpcloud.md

# SCIM Setup in JumpCloud

The document show step-by-step how to synchronize users' information from the JumpCloud identity provider to the platform.

## **SCIM Configuration in JumpCloud**

1. Please log in to JumpCloud as an **admin** and follow the following steps.
2. Please create a group and assign users to the group for synchronization.
3. Go to **SSO** > **+** > and then click the **Custom SSO SAML.**
4. Enter a name for the **Application name**.
5. Go to the **SSO** submenu and **enter a number like ‘1’** into the **‘IdP Entity ID’** and **‘SP Identity ID’** fields.
6. Go to the **Identity Management** submenu and then go to the bottom of the page to fill up the following fields.
   1. **SCIM Version:** SCIM 2.0
   2. **Base URL:** <https://scim-api.keepnetlabs.com/scim>
   3. **Token Key:** Please enter the secret token.
   4. Click the **‘Test Connection’** button to test the connection and then please click the **‘Activate’** button next to the **‘Test Connection’ button**.
   5. Edit the **SSO** rule and then go to the **SSO** menu to **Disable the SSO** at the bottom of the page.

JumpCloud configuration has been successfully finished. You can proceed with the following step.

## **Synchronization Users or Groups**

1. Go to the **SAML** application and then select **Groups** that contain users that will be synchronized to the platform and then click the **Save** button.
2. The users will be synchronized to the platform in approximately a few minutes.

✅ **You have now added your first Target Users. Now you need to** [**ensure they are able to receive emails from Keepnet**](https://github.com/ucarozan/keepnet-docs/blob/main/next-generation-product/getting-started/3.-email-deliverability) **successfully ➡️**
