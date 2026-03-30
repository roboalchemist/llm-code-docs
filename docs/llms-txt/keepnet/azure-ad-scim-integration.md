# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/azure-ad-scim-integration.md

# Azure AD SCIM Integration

This document shows step-by-step how to synchronize users' information from the Azure AD identity provider to the platform.

Please make sure to set up the mandatory settings from the ‘[Getting Started](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/getting-started-with-scim)’ page in this document before proceeding to the following step.

## **Azure Active Directory Configuration**

1. Please log in to [https://portal.azure.com/](https://portal.azure.com) as an **Admin** and select **Azure Active Directory** under the **Azure Services** section.
2. Click on **Enterprise applications** on the left-hand side of the screen.
3. Click **+New application** to create an application for SCIM integration.
4. Click on the **+Create your own application** to create an application.
   1. **Enter a name** for the application.
   2. Select **‘Integrate any other application you don't find in the gallery (Non-gallery)’** option.
   3. Click the **Save** button to create the application.
5. Click on the application to enter the application settings.
   1. Select the **‘Provisioning’** menu from the left side.
   2. Click the **‘New Configuration’** button and then enter the following information.
   3. **Tenant URL:** <https://scim-api.keepnetlabs.com/scim>
   4. **Secret Token:** Enter the token which was created on the platform.
   5. **Provisioning Status:** If this option is "Off", please switch it to "On" status.
   6. Click the **‘Test Connection’** button to test your configuration. If it’s successful, click the **Save** button to save settings.
6. Before starting the synchronization, set the synchronization type in the application.
   1. Click the **‘Edit Provisioning’** button and then under **Settings**, you can see the **‘Scope’** setting.
   2. You can select an option to synchronize users to the platform.
      1. If you select, **‘Sync all users and groups**’, all users or groups that are available in the Azure AD will be synchronized to the platform. This option might be dangerous for your platform license count.
      2. If you select, **‘Sync only assigned users and groups’,** only specific assigned users or groups to the application will be synchronized to the platform.

## **Synchronization Users or Groups**

1. Depending on your **‘Scope’** selection, you can assign your users or groups to the application by clicking the **Users and Groups** menu under the **Manage** column on the left and then click the **‘Start Provision’** button to start synchronization.
2. You can see target users on the platform approximately in a few minutes. The Azure AD rechecks the application for new users, changes or deleted users every 40 minutes.

## **Troubleshooting**

If a user can not be synchronized to the platform, please check the following settings.

1. The user may need to assign to the SCIM application from the **Users and Groups** menu in order to sync it to the platform depending on your **‘Scope’** selection.
2. The **‘mail’** attribute is mandatory, if this attribute doesn’t exist in the application, please create one under **Prevision > Edit Prevision > Users** page.
3. Go to **Provisioning**, click on **Provision** **Azure** **Directory** **Users** under **Mappings** field and make sure that **Source** **Object** **Scope** is **"All Records"** selected.

## How to Sync User's Timezone Info to Platform?

Please follow the steps below to sync the timezone information of Azure AD users to the platform.

1. Go to **Provisioning Settings** and click **Users** under **Mappings** to access attributes. Add a new attribute with these settings:
   * **Mapping Type**: Direct
   * **Source Attribute**: usageLocation
   * **Default Value if Null (Optional)**: Leave as default
   * **Target Attribute**: timezone
   * **Match Objects Using This Attribute**: No
   * **Matching Precedence**: Leave as default
   * **Apply This Mapping**: Always
2. Ensure all users have a **Usage Location** info set.
   * Go to **Azure AD**, open **Users**, and check the properties of a user.
   * At the bottom of the properties page, confirm **Usage Location** is set.
3. If provisioning has already started:
   * Stop provisioning.
   * Start provisioning again.
   * Restart provisioning to apply changes immediately.

This process syncs timezone info for all users on the platform.

## How to Group Users by Region / Country

If you would like to sync your users to the platform and group them by **their Region / Country**, please follow the steps below.

Once completed, users will be automatically assigned to groups based on their **Region / Country** information. For example, if a user has **UK** in their Region / Country attribute, a group named **UK** will be created, and the user will be assigned to it automatically.

#### Target User Custom Column Creation

1. Go to **Company > Target Users**.
2. While on the **People** menu, look at the **right-hand side** for the **Actions** column at the top.
   * Click the **Settings** button to access table settings.
3. Click the **EDIT FIELDS** button.
4. Click the **+ ADD CUSTOM FIELD** button.
   * Name the column **Country / Region** (or similar).
5. Click **Save** to create the custom column.

This column will later be used to sync users based on their **Country / Region** data.

#### Create New SCIM Settings

1. Go to **Company > Company Settings > SCIM Settings**.
2. Click the **+ NEW** button to create a new SCIM setting.
3. Enter a name for the setting.
4. In the **Map Fields** section:
   * Select the **Country / Region** option.
   * Then in the field next to it, select:\
     `addresses[type eq "work"].country`
   * Click **Next**.
5. Leave the **Group Name** field empty.
6. Under **Grouping Criteria**, select the **Country / Region** option.
7. Leave the **Synchronize groups with** **Identity Management Platform** option empty.
8. Click **Save**.
9. Copy the **Token** and paste it into your SCIM application.
   1. If you haven't created a SCIM application yet, refer to the beginning of this document for setup instructions.
10. Go to the **Provisioning** page on your SCIM application and:
    * First, click **STOP**
    * Then click **START**
    * Finally, restart the **Provisioning** process step by step
    * This will re-sync your users and group them based on their **Country / Region** information.

You may need to wait a few minutes for your users to sync from Azure AD to the platform.

## Tutorial Video

This video tutorial shows the documentation steps for synchronizing users' information from the Azure AD identity provider to the platform.

{% embed url="<https://youtu.be/Lg-4aF6yGh8>" %}
