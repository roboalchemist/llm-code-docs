# Source: https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app.md

# Starting the Free Trial and Accessing the Getint App

Installing and integrating applications within your Jira tool is a seamless process, provided you have the right access and permissions. This document outlines user-friendly steps for both Jira Server/Data Center and Jira Cloud, ensuring a smooth experience for all users.

### **Starting the Free Trial and Accessing the Getint App** <a href="#starting-the-free-trial-and-accessing-the-getint-app" id="starting-the-free-trial-and-accessing-the-getint-app"></a>

#### **Jira Cloud Integration**

#### **Admin User**

Access your Atlassian using the admin account, as these steps require admin access to the Jira Cloud. Navigate to the Atlassian marketplace.

* Navigate to the Atlassian Marketplace and select "Explore More Apps."
* Search for the Getint app, select "Try it Free," and let it install.
* Go to "Manage Apps" and, if the trial hasn't started, click "Start Trial."
* When the trial begins, click the "Apps" tab again and choose the Getint app you want to use.
* Once the trial begins, choose the Getint app under the "Apps" tab to initiate integration.
* Users will be routed to the Getint app and prompted to begin their integration. To get started, select integration or migration. (Click here to learn how to begin the integration.)

{% embed url="<https://youtu.be/GzmQYVt9U04>" %}

**Non-Admin Users**

Non-admin users should request app authorization from administrators

* Select the "Apps" tab, "Explore More Apps," and search for the Getint app.
* Request installation, and administrators will see the request under "Apps > View App Requests."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fo5fGNzzZ1ZNdtYuK9UL5%2FRequest%20installation%20from%20your%20Jira%20admin.png?alt=media&#x26;token=0295d43f-eb2a-4045-ab51-972d4af7021d" alt=""><figcaption></figcaption></figure>

* After approval, administrators configure the app. Users will not be able to access or view the application.

#### **Jira Server/Data Center**

To follow these instructions, you will need administrator access to the Jira server or data center.

* Go to "Settings" under your avatar, and select "Atlassian Marketplace."
* Search for the Getint app, choose "Free Trial," and accept the installation.
* Generate the license and follow the steps that will appear. Apply the license, go to "Manage Apps," and start the trial if not already initiated.
* After trial or purchase, access the app by selecting Admin in the left menu.
* You will be transferred to the Getint app and prompted to start their integration. To get started, choose integration or migration. (Click here to learn how to begin the integration.)

{% embed url="<https://youtu.be/Zx8LPlSk5Rg?si=dLe4xQOgMwJd2922>" %}

{% hint style="info" %}
Admin access to the Jira Server/ Data Center is necessary to administer the apps and enable downloads.
{% endhint %}

### **User Access feature** <a href="#user-access-feature" id="user-access-feature"></a>

We are excited to introduce the User Management Feature, enhancing flexibility and enabling non-admin users to create and manage integrations starting from version 1.52.

*Jira Admin can handle integrations, logs, and data. They can view it and authorize access to it. The system administrator can also troubleshoot all user-created integrations in the user's management views and download logs to submit to support if necessary.*

To enable the User Management Feature option, carefully follow the instructions below:

#### **Jira Cloud**

* In your Jira Cloud instance, log in as an administrator.
* Go to Settings and select "User Management, on the right side, select "Groups." Create a group (e.g., getint-jira-azure), select "View details," and add members.
* To access the application, the user will now see the app under the tab Apps and should click on it. They should select the app, and the Getint app will open. The option to create a new integration will prompt, giving the option to create a new integration if it is the first time accessing the app.

{% embed url="<https://youtu.be/voGnW9j1oRo>" %}

*Groups created must adhere to the Getint-xx format, such as:*

* getint-jira-jira
* getint-jira-azure
* getint-jira-wrike
* getint-jira-servicenow
* getint-jira-monday
* getint-jira-notion
* getint-jira-airtable
* getint-jira-trello
* getint-jira-hubspot
* getint-jira-gitlab
* getint-jira-freshdesk
* getint-jira-zendesk
* getint-jira-clickup
* getint-jira-asana

{% hint style="warning" %}
**Important:** This naming convention is required for the integration to work correctly.\
For example, if you're connecting **Jira** with **Monday**, the group name must be:\
\&#xNAN;**`getint-jira-monday`**
{% endhint %}

{% embed url="<https://youtu.be/BDDVf2mM1Xo>" %}

#### **Jira Server/Data Center (DC)**

* Enter your Jira Server or Data Center instance and log in as an administrator.
* Navigate to Settings, click the gear in the upper right corner of the screen, then select "User Management." Select "Groups" and create a new group (as Jira Cloud, the format should adhere to *Getint-xx*: getint-jira-azure or Getint-integrations). Please utilize the same format for the groups mentioned above.
* Select "Add," and the newly created group will appear in the group list. Choose "Edit members" and add the username, or choose it from your user list. Select "Add selected users,".

{% embed url="<https://youtu.be/DNERhFm-8jg>" %}

{% hint style="info" %}
*Access to apps can be given to Project Admin or non-admin users*
{% endhint %}

**Accessing the app:**

**Non-administrative users**

* After being granted access, users will be able to manage the integration, create a new one, and view logs and data.
* To see the application's contents, a non-admin user must get the URL to access the Getint app for now.

**Project Admin User**

* If the user is a project administrator, they will be able to locate the app in the project settings.
* On the project page, select "Project Settings". On the menu that appears, the Getint app will now appear.
* The Getint app will launch, and creating and maintaining the integrations will be possible.

{% embed url="<https://youtu.be/EXlV1TNW-Nc>" %}

{% hint style="info" %}
**For all the Non-Jira Admin roles:**

* Other users' integrations are visible but cannot be managed or saved.
* Logs for these integrations are securely encrypted to protect data privacy and cannot be viewed.
  {% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmNmcgv7EiaNxX2LTkq5D%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=e3bc4f73-2bed-47ae-a7fa-139dd809c092" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
