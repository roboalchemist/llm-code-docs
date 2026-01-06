# Source: https://docs.velodb.io/cloud/4.x/management-guide/user-and-organization

Version: 4.x

On this page

# User and Organization

## Registration and Login​

Click <https://www.velodb.cloud/> to enter the VeloDB Cloud registration and
trial page and fill in the relevant information to complete the registration.

![user register](/assets/images/user-
register-f4bf7408e0671addc942afba8a108c54.png)

> **Tip** VeloDB Cloud includes two independent account systems: One is used
> for logging into the console, as described in this topic. The other one is
> used to connect to the warehouse, which is described in the Connections
> topic.

If you have already registered on VeloDB Cloud, you can click Go to login
below to log in directly.

![user login](/assets/images/user-login-b17b88e370c05389979ac3b6cb956faa.png)

## Account Management​

### Change Password​

After login, click **User Menu** > **Security** to change the login password
for the VeloDB Cloud console.

![change user password](/assets/images/change-user-
password-9531a1cd03598f385130a912a4035ef2.png)

Once you have successfully changed the password for the first time, you can
use the password for subsequent logins.

### Manage Multi-Factor Authentication (MFA)​

Multi-factor authentication adds additional security by requiring an
Authenticator app to generate a one-time verification code for login.

When you log in, VeloDB Cloud verifies both your password and the MFA
verification code.

You can use any Authenticator app from the iOS or Android App Store to
generate this password, such as Google Authenticator and Authy.

![security-mfa](/assets/images/security-mfa-
de34ce49125251a1a33f498140ff9977.png)

### Notifications​

At the bottom of the left navigation bar, click **User Menu** >
**Notifications** to go to the message center.

Users, organizations, authorized warehouses, cluster operations, and alarms in
the platform will be notified to remind users when they are triggered.

You can filter by time range, filter unread/read messages with one click, view
messages in pages, mark all messages as read with one click, mark checked
messages as read with one click, etc.

![notifications](/assets/images/notifications-d33eadd0dbfbdca33a8eea18d2a01297.png)

You can switch to the **Scheduled Events** page to see scheduled events.

Scheduled events include system-initiated events (for example, the system
automatically upgrades the core version according to the policy set by the
user) and user-initiated events (for example, manually upgrading the core
version by specifying an execution time window).

Some events (such as version upgrades) may cause disconnection and other
impacts on the business. Please ensure that the business has the reconnection
mechanism.

Before the event is executed, you can modify the scheduled execution time
window or cancel the event.

## Organization Management​

Organization is the billing unit. Each organization will be billed
individually. We recommend that you divide organizations by cost unit, and one
user can be affiliated to multiple organizations.

Multiple warehouses can be created under one organization, and the data of
different warehouses are isolated.

You can switch the current organization in the menu bar - switch organization
in the user menu.

![switch-organization](/assets/images/switch-
organization-023e35ca045ea5913b6fde9075818d53.png)

### Role Management​

In the lower left corner, click **User Menu** > **Access Control** > **Role
Management**.

There are three roles by default in an organization, and you can create
multiple custom roles.

| **Manage Access Control**| **Manage Billing**| **Manage Organization**|
**Manage Warehouse**|  Organization Admin| Yes| Yes| Yes| All warehouse:
Create / Edit / View / Query / Monitor| Warehouse Admin| No| No| No| All
warehouse: Edit / View / Query / Monitor| Warehouse Viewer| No| No| No| All
warehouse: View / Query / Monitor  
---|---|---|---|---  
  
  * View existing roles:

![access control role management](/assets/images/access-control-role-
management-c98e5670d120dd5f09a94c73113158fe.png)

  * New role:

You can specify the role name and its corresponding privileges during
creation.

Custom roles can also be deleted or edited.

The user who creates the organization will be the organization administrator
role by default.

![access control new role](/assets/images/access-control-new-role-
cef0df279fcd5d92a42a8d6abb138317.png)

### User Management​

Organization administrators can invite new users to the current organization
and grant different roles.

New users can join the organization by activating the link in the invitation
email.

![access control user management invite users](/assets/images/access-control-
user-management-invite-users-fb4e5b707d28d4898d9789621c89e63b.png)

### MFA Settings​

After enabling MFA, all organization users must complete secondary
authentication before logging in.

![mfa-settings](/assets/images/mfa-
settings-9a8ef338348c896a8fbdeed228ace470.png)

### Audit​

After login, click **User Menu** > **Audit** to see the audit log for the
VeloDB Cloud console.

VeloDB Cloud logs the historical activities at the organization level. An
event indicates a change in your VeloDB Cloud organization. You can view the
logged activitied on the audit page, including the activity, time, IP and
user.

![audit-log](/assets/images/audit-log-42d4d408b758359153ea6832c397eb22.png)

### Organization Details​

click **User Menu** > **Organization Details** to see the organization ID,
create time and organization name.

![organizaion-details](/assets/images/organizaion-
details-38091b7b98e1d21f2ef4b20ae3275077.png)

On This Page

  * Registration and Login
  * Account Management
    * Change Password
    * Manage Multi-Factor Authentication (MFA)
    * Notifications
  * Organization Management
    * Role Management
    * User Management
    * MFA Settings
    * Audit
    * Organization Details

