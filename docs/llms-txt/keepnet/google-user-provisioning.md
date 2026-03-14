# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/google-user-provisioning.md

# Google User Provisioning

This document provides a step-by-step guide on how to synchronize users' information, such as **First** **Name**, **Last** **Name**, **Email** **Address**, **Department** **Name**, etc., from the **Google** **Workspace** email server to the platform.

{% hint style="danger" %}
You must have an admin account to set up the Google Workspace integration.
{% endhint %}

Please follow the steps below.

1. Go to **Company > Company Settings > Google User Provisioning** page.
2. Click the **CONNECT TO GOOGLE** button.
3. Click **Continue** and then click the **Allow** button to grant the requested permissions.
4. After successful integration, please proceed with the following configurations.
5. In the **Select Sync Source** field, choose one of the following options:
   1. **Sync Organizational Units (OU):** Sync users from the organizational units. Select all organizational units or choose the ones you wish to sync users from.
   2. **Sync Groups:** Sync users from group(s) that are from your Google Workspace. Select all groups or choose the ones you wish to sync users from.
6. In the **Select Sync Method** field, choose one of the following three options:
   1. **Sync all users to target users:** This will sync all users from the selected organizational units or groups.
   2. **Sync all users to a target group:** This will sync all users from the selected organizational units or groups and add them to the selected target group on the platform.
   3. **Sync users and create a matching group:** This option will sync users from the selected organizational units or groups, and the system will automatically create target groups with the same names on the platform. The users will then be assigned to the corresponding groups or organizational units on the platform.
7. Now, click the **START SYNC** button to begin synchronization.

The synchronization may take some time depending on the number of target users. Once the synchronization is complete, you can view the synced users on the **Company > Target Users** page.

The synchronization automatically repeats every 24 hours to ensure all users are updated with the latest information from Google Workspace, or to remove any target users who are no longer available in Google Workspace.

If you wish to sync the user's latest information to the platform immediately without waiting 24 hours, please click the **SYNC NOW** button.

## How to Remove Google Workspace Integration

If you no longer need to sync users from Google Workspace to the platform and wish to remove the integration, you can follow the steps below.

{% hint style="danger" %}
Once the integration is removed, the synced users will be deleted from the platform.
{% endhint %}

* Go to **Company > Company Settings > Google User Provisioning** page.
* Click the Unlink **Integration** button to remove the integration.

The integration is now successfully deleted.
