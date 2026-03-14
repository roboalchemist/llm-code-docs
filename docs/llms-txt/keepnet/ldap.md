# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/ldap.md

# LDAP

This document explains the functionality of the LDAP feature as well as how to set up an LDAP to synchronize target users information such as **Name**, **Surname**, **Email**, **Department**, **Phone Number** or other information to the platform automatically.

## **What Is LDAP?**

LDAP is a standard protocol that allows the platforms to access an active directory to fetch target user’s information such as **Name**, **Surname**, **Email**, **Department**, **Phone Number**, and other information to synchronize these user’s information to the platform automatically.

## **How To Set LDAP**

Go to **Company > Company Settings > LDAP** from the platform menu to access the following LDAP configuration.

### Settings

<table data-header-hidden><thead><tr><th width="150"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Server URL</td><td>URL and Port number to access the active directory.</td></tr><tr><td>Bind Username</td><td>Read-only access account name in the active directory.</td></tr><tr><td>Bind User Password</td><td>Password of the read-only account.</td></tr><tr><td>Base DN</td><td>The starting point for searches in the LDAP directory server. Example of DC=company and DC=domain.com.</td></tr><tr><td>Relative DNS</td><td>A relative search will be conducted on the subbranches of base DN for LDAP users whose objectType=user. You can enter a different relative DN on each line.</td></tr><tr><td>Status</td><td>Disable the LDAP is no need to use more.</td></tr><tr><td>Connection</td><td>Test your configuration if successful to connect the active directory.</td></tr><tr><td>Save Changes</td><td>Saves the changes</td></tr></tbody></table>

If the test connection is successful, you will see that it’s successful, if not please see the detailed pop-up message.

Usually, an allow list rule is needed to access to the local Active Directory from the platform's IP address. You can contact support team to get IP address of the platform.

### Scheduled Syncs

This is where you can see your scheduled LDAP rules. This means LDAP will automatically scan daily for new users to add/update/delete to your specified target group.

The components of the Scheduled Syncs page are explained in detail in the table below.

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>Name</td><td>Name of target group</td></tr><tr><td>Status</td><td>Disables the scheduled rule if you don’t want the rule to work anymore.</td></tr><tr><td>Date Created</td><td>Date and time that the scheduled rule was created.</td></tr><tr><td>Last Run</td><td>The last time LDAP was scanned for new changes.</td></tr><tr><td>Next Run Time</td><td>The next time LDAP will be scanned for new changes.</td></tr><tr><td>Edit</td><td>Edit the scheduled rule to change the settings.</td></tr><tr><td>Delete</td><td>Delete LDAP synchronization if the LDAP rule shouldn’t work anymore.</td></tr></tbody></table>

### **Field Mapping**

This is where you can choose which information that will be fetched and imported to the specific column on the platform. The admin can fetch specific information from the active directory such as the **Manager**, **Country**, **City**, or other attributes and synchronize this information of the users.

The components of the **Field Mapping** page are explained in detail in the table below.

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>Email</td><td>User’s <strong>Email Address</strong> that will be imported</td></tr><tr><td>First Name</td><td>User’s <strong>First Name</strong> that will be imported</td></tr><tr><td>Last Name</td><td>User’s <strong>Last Name</strong> that will be imported</td></tr><tr><td>Department</td><td>User’s <strong>Department</strong> that will be imported</td></tr><tr><td>Phone Number</td><td>User's <strong>Phone</strong> <strong>Number</strong> that will be imported</td></tr><tr><td>Timezone</td><td>User's <strong>Timezone</strong> that will be imported</td></tr></tbody></table>

## **How to fetch custom attributes?**

While the **Email**, **First Name**, **Last Name**, or **Department** attributes are the most popular field mapping categories, you can have the option to synchronize **Display Name**, **Office**, **Telephone Number (Mobile** or **Home)**, **Address (Street**, **City**, **State**, **P.O Box**, **Country**, **Zip Code)**, **Company**, and more.

* Go to **Target Users > People** menu and then click the **Table Settings** button on the right top of the screen to click the **EDIT FIELDS** button.
* Create a custom field and then click the **Save** button.
* To map this custom field with LDAP, go to **Company Settings > LDAP > Field Mapping** and map any listed active attributes to a created custom field.

Do not forget to save changes by clicking the **Save Changes** button and then proceed to the following title.

## **Import Users with LDAP**

Follow the steps below to import target users to the platform from the integrated Active Directory by using the LDAP.

* Go to **Company > Target Users** from the platform menu.
* Click the **+ NEW button** on the top right of the page and then select the **‘Import users from LDAP’** option.

There is two following option to import users.

### **Entire LDAP**

This option fetches all unique email users in your active directory, no matter what active directory groups they are in.

* If this option is selected, please choose a target group that all users will be imported to on the platform.
  * If the target group is not selected, all users will be imported as a single member on the platform without being assigned to a target group. No worries, all users can be imported to a single target group later.
* There are three options to import users.
  * Choose **‘Select Manually’** if all users need to be imported manually without creating auto-synchronization.
  * Choose **‘Sync All Users’** if all users need to be synchronized automatically.
    * This process repeats every 24 hours automatically to fetch new users or update changes on the users.
  * Choose **‘Sync By Query’** if all users need to be synchronized users by criteria.
    * This process repeats every 24 hours automatically to fetch new users or update changes on the users that match the criteria.
    * Use the filters to create criteria to filter users out of all users to synchronize and then use the **View Users** button to see filtered users that will be synchronized.

### **LDAP Groups**

This option fetches unique email users that are in certain groups in your active directory.

* If this option is selected, please choose LDAP groups which users that are inside will be imported to the platform.
  * If the target group is not selected, all users will be imported as a single member on the platform without being assigned to a target group. No worries, all users can be imported to a single target group later.
* There are three options to import users.
  * Choose **‘Select Manually’** if all users need to be imported manually without creating auto-synchronization.
  * Choose **‘Sync All Users’** if all users need to be synchronized automatically.
    * This process repeats every 24 hours automatically to fetch new users or update changes on the users.
  * Choose **‘Sync By Query’** if all users need to be synchronized users by criteria.
    * This process repeats every 24 hours automatically to fetch new users or update changes on the users that match the criteria.
    * Use the filters to create criteria to filter users out of all users to synchronize and then use the **View Users** button to see filtered users that will be synchronized.
    * Click **‘+ Add Condition’** to add more conditions for filtering the users.

## Video Tutorial

The following video shows how to set up an LDAP connection and import or synchronize users to the platform.

{% embed url="<https://youtu.be/LrpgDzFwUrE>" %}

## FAQ

### **Q: How can I see scheduled synchronizations?**

A: Go to **Company Settings > LDAP > Scheduled Sync** menu to see all scheduled synchronizations. You can **Edit** to update the rule or **Delete** it.

### **Q: Can I delete scheduled email users on the platform?**

A: No, the scheduled target users cannot be deleted. If you wish the user not to synchronize to the platform, please find the related scheduled sync setting and update it.

### **Q: Can I delete manually imported email users on the platform?**

A: Yes, you can delete the manually imported users on the platform.

### **Q: Can I inactivate the scheduled synchronization in order to stop but not delete the synchronization?**

A: Yes, if you wish not to delete the synchronization but also inactive it to stop new fetch users or update changes on the user, you can do it from **Company Settings > LDAP > Scheduled Sync** menu.
