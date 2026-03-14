# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/people.md

# People

This section describes how to create authorized accounts with various permission levels, called System Users, who manage and perform all activities on the platform.

## How to Create a System User?

After logging into the platform, you can go to the **System Users** page by following **Company > System Users** on the left menu. System users currently registered to the system are listed on this page.

{% hint style="warning" %}
You need to be an authorized admin to create a system user in this menu.
{% endhint %}

By clicking the **+ New** button in the upper right corner, you can create a new system user by filling in the following fields.

After creating a new system user, the relevant system user receives an email to create a password to log in to the system. The user can create a password and log in to the platform by clicking the link in this e-mail.

<table><thead><tr><th width="210.021693394458">Field</th><th width="532.4285714285713">Description</th></tr></thead><tbody><tr><td>First Name</td><td>System user's First Name</td></tr><tr><td>Last Name</td><td>System user's Last Name</td></tr><tr><td>Email Address</td><td>System user's Email Address</td></tr><tr><td>Phone number</td><td><p>System user's Phone Number</p><p>Hint: This information is required for MFA purposes</p></td></tr><tr><td>Status</td><td>Validity of the system user: active or not. If not active, the user cannot log in to the platform.</td></tr><tr><td>Role</td><td>System user's permission level. You can create custom roles for your users and limit their access to various products on the platform.<br><br>Please click <a href="user-roles">here</a> for more information about the usage of the Roles feature.</td></tr></tbody></table>

## How to Edit a System User?

System user information can be edited at any time. First, go to the System Users page by following the **Company > System Users** on the left menu. You will see all the system users here. Then, go to the **Actions** column, and click the **pencil icon ✎** to go to the section where you can edit user details.

## How to Delete a System User?

System user accounts can be deleted at any time to cancel access to the platform. To delete a system user to terminate all associations with the platform, go to the **System User's** list at the **Company > System Users** on the left menu. You will see all the registered system users here. Find the related system user and click the **Delete** button on the **Actions** column. Then, click **Delete** again to confirm the process.

{% hint style="danger" %}
This action cannot be undone, and the deleted user will be not able to log in to the platform and the processes related to the user will be disabled. Therefore it would be wise to double-check the user information.
{% endhint %}

## FAQ

### Q: Why can’t I set permissions of new system users when adding them into Keepnet?

A: Yes, first you have to create your custom role with the permissions you want. then assign that system user to that custom role. You can create this role by going to Company > System Users > Roles > New +.

### Q: I’ve accidently deleted the system user, can I create it again?

A: Yes, you can recreate it by following the documentation.

### Q: How can I access the activities of the system user I created on the platform?

A: You can check the all system admin’s actions that user made on the platform from the **Audit Log** field under the Company on the left menu. For more information, you can review the **Audit** document here.

### Q: I’ve accidently deleted the system user, can I create it again?

A: Yes, you can recreate it by following the documentation.

### Q: How can I access the activities of the system user I created on the platform?

A: You can check the all system admin’s actions that user made on the platform from the **Audit Log** field under the Company on the left menu. For more information, you can review the **Audit** document here.

### Q: How can I edit the system user's permission?

A: You can review and customize admin’s permission on the Role Management page, please click [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles) to access the relevant document.
