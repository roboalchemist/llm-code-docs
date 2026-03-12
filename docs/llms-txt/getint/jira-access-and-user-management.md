# Source: https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app/jira-access-and-user-management.md

# Jira Access and User Management

Integrating applications within Jira Server/Data Center and Jira Cloud environments requires careful consideration of access permissions and system configurations. This comprehensive guide provides step-by-step instructions tailored for both environments, ensuring a seamless integration process with Getint.

### Starting the Free Trial and Accessing the Getint App <a href="#starting-the-free-trial-and-accessing-the-getint-app" id="starting-the-free-trial-and-accessing-the-getint-app"></a>

#### **Jira Cloud Integration:** <a href="#jira-cloud-integration" id="jira-cloud-integration"></a>

**Admin User:**

1. **Access Atlassian Marketplace:**
   * Log in to your Atlassian account using admin credentials.
   * Navigate to the Atlassian Marketplace and select "Explore More Apps."
2. **Search and Install Getint:**
   * Search for the Getint app, select "Try it Free," and install it.
   * Go to "Manage Apps" and, if the trial hasn't started, click "Start Trial."
   * When the trial begins, select the Getint app under the "Apps" tab to initiate integration.
3. **Start the Integration:**
   * Users will be routed to the Getint app and prompted to begin their integration. Choose "Integration" or "Migration" to get started. [(Click here to learn how to begin the integration.)](https://docs.getint.io/guides/quickstart)

{% embed url="<https://youtu.be/GzmQYVt9U04>" %}

**Non-Admin Users:**

1. **Request App Authorization:**
   * Request app authorization from administrators.
   * Select the "Apps" tab, "Explore More Apps," and search for the Getint app.
   * Request installation and administrators will see the request under "Apps > View App Requests."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpFug3GMkPKkBLgUAAUW3%2FRequest%20installation%20from%20your%20Jira%20admin.png?alt=media&#x26;token=10bdfee0-358a-4d32-bf6d-835cabbcbb97" alt=""><figcaption></figcaption></figure>

1. **Post-Approval:**

* After approval, administrators configure the app. Users will not be able to access or view the application until it is configured.

#### **Jira Server/Data Center Integration:** <a href="#jira-server-data-center-integration" id="jira-server-data-center-integration"></a>

**Admin User:**

1. **Access Atlassian Marketplace:**
   * Log in as an administrator, go to "Settings" under your avatar, then select "Atlassian Marketplace."
2. **Search and Install Getint:**
   * Search for the Getint app, choose "Free Trial," and accept the installation.
   * Generate the license and follow the steps that appear. Apply the license, go to "Manage Apps," and start the trial if not already initiated.
3. **Start the Integration:**
   * After trial or purchase, access the app by selecting admin in the left menu.
   * You will be transferred to the Getint app and prompted to start their integration. Choose "Integration" or "Migration" to get started.

{% embed url="<https://youtu.be/Zx8LPlSk5Rg>" %}

{% hint style="info" %}
**Note:** Admin access to the Jira Server/Data Center is necessary to administer the apps and enable downloads.
{% endhint %}

#### Verifying your trial license <a href="#verifying-your-trial-license" id="verifying-your-trial-license"></a>

1. Ensure that the steps generate a valid license. Go to Marketplace > Manage Apps and check the generated license. For Jira Server/DC and Cloud apps, these steps are applicable. For On-premise installation, the license will appear under Settings > License.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOr3GudUE6HS0pjUAJKz7%2FChecking%20your%20license%20in%20Cloud%20apps.png?alt=media&#x26;token=0d3db4d9-1b81-4658-a8f2-06b12c2e86b4" alt=""><figcaption></figcaption></figure>

### User Access Feature <a href="#user-access-feature" id="user-access-feature"></a>

We are excited to introduce the User Management Feature, enhancing flexibility and enabling non-admin users to create and manage integrations starting from version 1.52.

#### **On-premise:** <a href="#on-premise" id="on-premise"></a>

1. **Switch the workspace:**

* Select the "Account" icon on the bottom left side and switch to Getint Administration
* Then select "Users" and tap on "Create User."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYepxxq6j57NEaJGei3kS%2Fimage-20240617-125527.png?alt=media&#x26;token=bc3d9017-3b2c-42bc-bda1-38f484a5133f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6C7g6IzRFoWUx2IUN7IO%2Fimage-20240617-125725.png?alt=media&#x26;token=a34c292d-2096-4a21-be33-4ebde94cabd7" alt=""><figcaption></figcaption></figure>

* On the screen that appears, create a user with the desired credentials.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbOwD0QTvbs1CiSecnKxq%2Fimage-20240617-130159%20(1).png?alt=media&#x26;token=0344c2c2-50b8-4e21-b954-0fe5c22f1512" alt=""><figcaption></figcaption></figure>

* The user will be created, and now you need to assign the Workspace that they have access to. Select the three dots on the right and click “Edit”. Assign the workspace, select “add access,” and enable the user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhJ0MbalgabXeSTXDYDCV%2Fimage-20240618-082411.png?alt=media&#x26;token=11b446e4-6fdb-415b-82b5-26211d3d58dc" alt=""><figcaption></figcaption></figure>

**Jira Cloud:**

1. **Enable User Management:**
   * Log in as an administrator in your Jira Cloud instance.
   * Go to Settings, select "User Management," then "Groups."
   * Create a group (e.g., getint-jira-azure), select "View details," and add members.
2. **Accessing the App:**
   * Users will now see the app under the "Apps" tab and should click on it.
   * The Getint app will open, prompting users to create a new integration if it is their first time accessing the app.

{% embed url="<https://youtu.be/BDDVf2mM1Xo>" %}

**Groups Naming Requirements**

To ensure smooth integration and avoid any confusion, all groups must follow this naming convention: **getint-jira-xxx**.

**Mandatory Format:**

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
**Important Note:** This naming convention is a must for proper integration. For example, if your integration is between Jira and Monday, ensure the group name follows this format: **getint-jira-monday**.
{% endhint %}

**Jira Server/Data Center (DC):**

1. **Enable User Management:**
   * Enter your Jira Server or Data Center instance and log in as an administrator.
   * Navigate to Settings, click the gear in the upper right corner of the screen, then select "User Management."
   * Select "Groups" and create a new group (e.g., getint-jira-azure).
2. **Add Members:**
   * Select "Add," and the newly created group will appear in the group list.
   * Choose "Edit members" and add the username, or select it from your user list. Select "Add selected users."

{% embed url="<https://youtu.be/DNERhFm-8jg>" %}

**Groups Naming Requirements**

Same as the steps for Jira Cloud, Jira Data Center Groups must follow this naming convention: **getint-jira-xxx**.

**Mandatory Format:**

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
**Important Note:** This naming convention is a must for proper integration. For example, if your integration is between Jira and ServiceNow, ensure the group name follows this format: **getint-jira-servicenow**.
{% endhint %}

**Accessing the App:**

**Non-administrative Users:**

* After being granted access, users can manage the integration, create a new one, and view logs and data.
* To see the application's contents, a non-admin user must get the URL to access the Getint app for now.

**Project Admin User:**

* If the user is a project administrator, they can locate the app in the project settings.
* On the project page, select "Project Settings." On the menu that appears, the Getint app will now appear.
* The Getint app will launch, allowing for creating and maintaining integrations.

**For all Non-Jira Admin Roles:**

* Other users' integrations are visible but cannot be managed or saved.
* Logs for these integrations are securely encrypted to protect data privacy and cannot be viewed.

This comprehensive guide ensures administrators and non-admin users can effectively navigate and utilize the Getint app within Jira Server/Data Center and Jira Cloud environments, promoting a smooth integration process. For further assistance, please get in touch with our support team at our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmNmcgv7EiaNxX2LTkq5D%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=e3bc4f73-2bed-47ae-a7fa-139dd809c092" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
