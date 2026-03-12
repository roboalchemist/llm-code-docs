# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/target-users.md

# Target Users

The **Target Users** are those who receive e-mails that will be sent through the platform. This document explains how to add target users to the platform so that it can send training, phishing, campaigns, and other emails to them.

## Managing Target Users

You can manage all target users from the **Company > Target Users** menu. You may create, remove, modify, and add target users to a group on this page.

{% hint style="info" %}
The platform will notify the system user to validate the email domains after creating the target users on the platform. For more information, click [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/allowed-domains).
{% endhint %}

## Methods for Adding Target Users

### 1. Adding Target Users via XLS(x) or CSV Files

You can easily add target users to the system by importing a list on an Excel file. To use this option, please follow the steps below:

* Go to the **Company > Target Users** menu.
* Click the **"New"** button.
* Click the "**Import from a file"** option.
* To view a sample sheet, please click "**DOWNLOAD EXAMPLE SHEET"** on the target users page.

After downloading a sample sheet, it's time to fill in the required fields. Please open the sheet file and fill in the following fields.

* **First Name:** It's required.
* **Last Name:** It's required.
* **Email Address:** It's required.
* **Phone Number:** It's optional.
* **Department:** It's optional.
* **Time Zone:** It's optional. Please see the following information if you prefer to use the time zone for your target users in your sheet file.
* **Priority:** It's optional.

{% hint style="info" %}
The downloaded spreadsheet has time zones in SHEET2. Please copy all time zones from the "Time Zone" column in SHEET2 and paste them properly for your target user's time zone column.
{% endhint %}

After your file is ready, please follow the steps below:

* Go to the **Company > Target Users** menu.
* Click the **"New"** button.
* Click the "**Import from a file"** option.
* Click **Upload** **File**, choose the file on your computer, and click **NEXT.**
* The **Map Fields** tab will require you to match the titles to the fields on the platform.
* When you complete matching the fields, click **NEXT**.
* Then either pick the users you wish to add and click **IMPORT SELECTED**, or click **IMPORT ALL** to add all the users to the platform.

### 2. Adding Target Users Manually

​​From the left menu, select **Company > Target Users**. Then, click **New** and click **"Add users manually"** on the new page. Fill out the required boxes in the **"Add New User"** window to add a new target user to the system.

<table data-full-width="false"><thead><tr><th width="164">Field</th><th>Description</th></tr></thead><tbody><tr><td>First name</td><td>Specify the first name information of the target user.</td></tr><tr><td>Last name</td><td>Specify the last name information of the target user.</td></tr><tr><td>Email</td><td>Specify the email information of the target user.</td></tr><tr><td>Phone Number</td><td>You may add target user's phone number.</td></tr><tr><td>Department</td><td>Specify the department information of the target user.</td></tr><tr><td>Preferred Language</td><td>Specify the preferred language for the user.</td></tr><tr><td>Time Zone</td><td>Select a time zone and send campaigns to the target user in their own time zone.</td></tr><tr><td>Target Groups</td><td>Add the new user to the target group(s).</td></tr><tr><td>Proritiy</td><td>Specify the priority information of the target user. If the priority is high, the user will get the email first.</td></tr><tr><td>Active</td><td>Disable the target user on the platform. Disabled users won't receive training or simulation emails.</td></tr></tbody></table>

### 3. Adding Target Users via SCIM

SCIM (System for Cross-domain Identity Management) is a standard that automates the sharing of user identity information (e.g., first name, last name, email, phone number) across multiple identity platforms. Keepnet's platform supports SCIM integration to automate and synchronize target user data from identity providers to the platform.

To use this option, please follow the steps below:

* Go to the **Company > Target Users** menu.
* Click the **"New"** button.
* Click the "**SCIM Sync"** option.

Please click [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings) to learn how to set up or synchronize your employees' information via SCIM on the platform.

### 4. Adding Target Users via Google Workspace

The Google Workspace User Sync feature allows you to automatically import and synchronize user information (e.g., first name, last name, email, phone number) from Google Workspace into Keepnet's platform. This ensures that your user data is always up to date without the need for manual updates.

To use this option, please follow the steps below:

* Go to the **Company > Target Users** menu.
* Click the **"New"** button.
* Select the **"Google Sync"** option.

Please click [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/google-user-provisioning) to learn how to set up or synchronize your employees' information via Google Workspace on the platform.

### 5. Adding Target Users via LDAP

LDAP is a standard protocol that allows platforms to access an Active Directory to retrieve user information, such as name, surname, email, department, phone number, and other details, enabling automatic synchronization with the platform. The benefits of LDAP include automating user management, saving time, reducing stress, and minimizing manual user management tasks.

To use this option, please follow the steps below:

* Go to the **Company > Target Users** menu.
* Click the **"New"** button.
* Click the "**Import from LDAP"** option.

Please click [here](https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-ldap) to learn how to set up and synchronize your employees' information via LDAP integration.

### 6. Adding Target Users via API

Using the platform's APIs, target users may be effortlessly migrated. The API endpoints that are required are detailed below.

You need to create Rest API keys on the platform from here in order to use this API import option.

{% hint style="info" %}
Use your own domain if you are using an on-premise version. e.g. <https://api.PLATFORM\\_DOMAIN/docs/index.html>
{% endhint %}

#### Instructions for adding target users using an API

<mark style="color:green;">**POST**</mark> **​/api​/target-users**

* Go to the Swagger [link](https://api.keepnetlabs.com/docs/index.html).
* Click the **Authorize** button on the top right side of the page.
* Complete the authorization step with the **Client ID** and **Client Secret** key that you created on the platform.
* Make sure that the **api1** option is checked (✓) on the **Scopes** section.
* Then use this endpoint to add a **new target user** to the platform.

{% hint style="info" %}
The most up-to-date format of the body content that you need to use for requesting an API is available on the Swagger interface.
{% endhint %}

#### Searching for a user using API

<mark style="color:green;">**POST**</mark> **​/api​/target-users​/search**

* Go to the Swagger [link](https://api.keepnetlabs.com/docs/index.html).
* Click the **Authorize** button on the top right side of the page.
* Complete the authorization step with the **Client ID** and **Client Secret** key that you created on the platform.
* Make sure that the **api1** option is checked (✓) on the **Scopes** section.
* Then use this endpoint to **search for a target user** on the platform.

{% hint style="info" %}
The most up-to-date format of the body content that you need to use for requesting an API is available on the Swagger interface.
{% endhint %}

#### Editing Target Users using API

<mark style="color:orange;">**PUT**</mark> **​/api​/target-users​/{resourceId}**

* Go to the Swagger [link](https://api.keepnetlabs.com/docs/index.html).
* Click the **Authorize** button on the top right side of the page.
* Complete the authorization step with the **Client ID** and **Client Secret** key that you created on the platform.
* Make sure that the **api1** option is checked (✓) on the **Scopes** section.
* Then use this endpoint to **edit a target user** on the platform.

{% hint style="info" %}
The most up-to-date format of the body content that you need to use for requesting an API is available on the Swagger interface.
{% endhint %}

#### Deleting Target Users using API

<mark style="color:red;">**DELETE**</mark> **​/api​/target-users​/{resourceId}**

* Go to the Swagger [link](https://api.keepnetlabs.com/docs/index.html).
* Click the **Authorize** button on the top right side of the page.
* Complete the authorization step with the **Client ID** and **Client Secret** key that you created on the platform.
* Make sure that the **api1** option is checked (✓) on the **Scopes** section.
* Then use this endpoint to **delete a target user** on the platform.

{% hint style="info" %}
The most up-to-date format of the body content that you need to use for requesting an API is available on the Swagger interface.
{% endhint %}

## Adding Target Users to Groups

You may create new groups by clicking the **New** button on the **Company > Target Users > Group** menu.

To add target users to a group, click **⁞** icon under the **Action** column and click **Add users to the group**. Select the users you want to add to a group and click **“Add Selected Users”** to complete the process.

## Deleting Target Users

To delete target users on the platform, go to the **Company > Target Users > People** menu and select the user(s) that you want to remove. Click **⁞** icon under the **Action** column and click **“Delete”** to complete the process.

## Deleting Groups

To delete target user groups on the platform, go to the **Company > Target Users > Group** menu and select the group(s) that you want to remove. Click **⁞** icon under the **Action** column and click **“Delete”** to complete the process.

{% hint style="info" %}
Deleting a target user group will not delete the users defined in the group. It will only delete the group.
{% endhint %}

## **Repeat Offenders**

**Repeat Offenders** is an automated target group that includes users who have been phished two or more times in the last 3 months across all phishing simulation campaigns such as from Vishing Simulator, Quishing Simulator, Phishing Simulator, Callback Simulator and Smishing Simulator. You can view the risky users and send them training more frequently.

There are two ways to see the repeat offender users.

1. Go to **Company > Target Users > Groups**. There, you will find the **Repeat Offenders** target group, which contains users who have been phished multiple times.
2. Go to **Company > Target Users**. There, you will see a banner labeled **Repeat** **Offenders**. Click the **SEE** **REPEAT OFFENDERS** button to view users who have been phished multiple times.

## **New Hires**

New Hires is an automated target group designed to include new employees in your organization for a period of 90 days. This group ensures that new hires receive focused training and simulations, helping them quickly adapt to your organization's security culture.

The training and simulations for this group are selected and assigned by system admins. This ensures that the content is tailored to improve their awareness and preparedness against potential security threats. After the 90-day period, the new hires are automatically removed from the group.

To view the **New** **Hires** group:

1. Go to **Company > Target Users > Groups**
   * Here, you will find the **New** **Hires** group listed.

By using the **New** **Hires** group, you can ensure that your newest team members are equipped with the knowledge and skills necessary to maintain a strong security posture from day one.

## Non-Simulated Users

The **Non-Simulated Users** group is an automated target group designed to include users who have not yet participated in any phishing simulations. Users are automatically added to this group and remain in it until they engage in their first simulation. This allows organizations to focus on users who have not been exposed to phishing scenarios, helping them build security awareness from the ground up.

Simulations for this group can be specifically tailored to introduce users to phishing risks and improve their ability to recognize potential threats. Once a user completes a simulation, they are automatically removed from the group.

**To view the Non-Simulated Users group:**

1. Go to **Company > Target Users > Groups**
   * Here, you will find the **Non-Simulated Users** group listed.

By utilizing the **Non-Simulated Users** group, you can ensure that employees who have not yet participated in phishing simulations receive the necessary exposure to enhance their awareness and resilience against social engineering attacks.

## Untrained Users

The **Untrained Users** group is an automated target group that includes users who have not enrolled in any training courses. Users are automatically assigned to this group until they complete at least one training session. This allows organizations to prioritize security awareness training for employees who have yet to engage with learning modules.

Training content for this group can be tailored to provide essential cybersecurity knowledge, ensuring that users gain the skills needed to protect against evolving threats. Once a user enrolls in a training course, they are automatically removed from the group.

**To view the Untrained Users group:**

1. Go to **Company > Target Users > Groups**
   * Here, you will find the **Untrained Users** group listed.

By using the **Untrained Users** group, you can ensure that employees who have not yet undergone cybersecurity training receive structured learning, equipping them with the necessary knowledge to maintain a strong security posture.

## View User Activity Timeline

The new **User Activity Timeline** button under the **Company > Target Users > Actions** column allows admins to view a target user's activity history across simulations, reporting and training. This helps track performance and engagement. For more details, visit [Gamification Report](https://doc.keepnetlabs.com/next-generation-product/platform/reports/gamification-report) documentation.

## Deleted users in the list

When you view **Company > Target Users**, users who have been deleted from the platform are still listed for reporting and audit purposes. Deleted users appear with:

* **Disabled or greyed-out rows** — So you can quickly distinguish them from active and inactive users.
* **Status text** such as **"This user has been deleted"** — Shown in the user row or status column.

You cannot perform **Delete User** or **Add to Group** on already deleted users. This avoids "Not Found" errors and makes it clear that deleted users are no longer manageable.

## Target Users Summary Widgets

The **Company > Target Users** page includes four widgets that help you quickly understand the status of your user base and track user changes over time. Each widget displays a number and provides a clear summary of who is currently active, who is inactivated, who is deleted, and how many users were added during a selected month for billing purposes.

The widgets are:

* **Active Users:** Shows users who are currently active on the platform. These users can receive emails and can be tracked in simulations and reporting.
* **Inactive Users:** Shows users who are temporarily inactivated. The simulation or training delivery is paused for these users, but their existing data remains available in the platform.
* **Deleted Users:** Shows users removed from active use. These users are no longer part of the active user base, but their historical records are retained for reporting and audit purposes.
* **Monthly Users:** Shows how many users were added to the platform during the selected month, regardless of whether they are currently Active, Inactive, or Deleted. You can change the month using the selector. Monthly Users data is available starting from December for all customers.

## Video Tutorial

The **Target Users** are those who receive e-mails that will be sent through the platform. This video tutorial explains how to add target users to the platform so that it can send training, phishing, campaigns, and other emails to them.

{% embed url="<https://youtu.be/S0nN_uE8NjQ>" %}

## **FAQ**

### Q: Is it possible to add a target user with any domain name?

A: You can only add e-mail addresses with authorized domains. Contact your Account Manager or Support Team if you wish to add users with a different domain address.

### Q: Would the remaining license count increase when a target user is deleted?

A: No, when a target user is added, your remaining license is reduced appropriately, but your license is not increased when the target user is deleted.

### Q: What will happen when the license count is exceeded?

A: The system will warn the admin when add a new user although the license count is exceeded. If the admin goes further and adds new users, each unique user will be charged. Please contact the support team for the additional license.

The **license warning** pop-up (when adding users or when the count is near or over the limit) counts only **Active** target users. Inactive and Deleted users are excluded from this count, so the warning reflects actual license usage for active users.

### Q: What will happen when the license date is expired?

A: All data will stay remain but the admin will not be able to login into the platform. Please contact the support team to renew the license.

### Q: Can I add a custom column under the "People" page in Target Users?

A: Yes, go to **Company > Target Users > People** and click the **Settings** button to open table settings. After that, click the **EDIT** **FIELDS** button to create or manage any custom fields.
