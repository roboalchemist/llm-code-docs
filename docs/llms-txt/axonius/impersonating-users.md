# Source: https://docs.axonius.com/docs/impersonating-users.md

# Impersonating Users

Administrator users can use the Impersonation feature to log on to and use the system as if they are another user, and carry out activities with the permissions of that user.
You can use this feature:

* To assist a user.
* Help a user configure private items, such as dashboards, private queries, and reports.
* To manage and review private items.
* For troubleshooting – When the admin user logs on using “impersonation”, they can only see what the specific user is able to see, and thus help troubleshoot.
* View items that were private to a deleted user. See [Managing User Status](https://docs.axonius.com/axonius-help-docs/docs/manage-users#manage-user-status).

<Callout icon="📘" theme="info">
  Note

  * Impersonation cannot be done using API.

  * You cannot impersonate Admin users.
</Callout>

**To impersonate a user:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/System%20Settings%20icon.png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Users**.
3. Click on a user; the user details drawer opens.
4. Click the Impersonate icon; the system informs you that you are about to impersonate the selected user.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UserDrawerImpersonate.png)
5. Click **Yes, continue** to impersonate the user in their main data scope.

A message bar appears at the top of the screen indicating that you are impersonating the user.
Perform actions in the system as if you are the user you are impersonating. You can only see the assets, queries, enforcement actions, dashboards, and reports that the user you are impersonating is authorized to see, and you can only perform actions they are authorized to perform.
During your work, a banner appears on the screen saying that you are impersonating the user that you chose.

<Image alt="DashboardImpersonate.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DashboardImpersonate.png" />

5. Once you are done, click **Stop** in the banner. The system logs you out and then opens the login page so that you can log in again under your own admin credentials.

Impersonation sessions can last for up to 30 minutes.
Actions performed by an Admin in impersonation mode are listed in the Log as 'Impersonated By'.