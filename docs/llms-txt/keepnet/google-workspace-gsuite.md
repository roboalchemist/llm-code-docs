# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/7.-incident-responder-setup/step-2.-mail-configurations/google-workspace-gsuite.md

# Google Workspace (Gsuite)

You can integrate your Google Workspace environment with the Incident Responder product by following the steps below.

* Log into <https://console.cloud.google.com/> using an account that has administrative permissions.
* Click **Select a project > New Project**.
* Click on the related new project.
* On the left-side menu, go to **APIs and Services > Library**, search for **Admin SDK API**, and click **Enable**.
* Return to the previous page and search for **Gmail API**, then click **Enable** to activate the API.
* Select **IAM & Admin > Service Accounts** from the left-side menu.
* Click **Create Service Account**, name it, and click **Create and Continue.**
* Select **Service Directory > Service Directory Admin** as the role and click **Continue > Done** to complete the process.
* After creating a service account, click on the related user and go to the user details page.
* Go to the **Keys** tab, click **Add Key > Create** new key.
* Select **JSON** as the key type and click **Create**. **Save** the JSON file.
* Go to the **Details** tab and copy **Unique ID** information. Save this information for the next step.

Next, log in to [admin.google.com](https://admin.google.com/).

* Go to **Security > Access and data control > API controls** on the left-side menu.
* Scroll down to **Domain-wide delegation** and click **Manage Domain-Wide Delegation**.
* Click **Add New**.
* For **Client ID**, enter the **Unique ID** information that you saved earlier.
* For **OAuth Scopes**, paste the scope information below:

<https://mail.google.com/,https://www.googleapis.com/auth/admin.directory.user,https://www.googleapis.com/auth/admin.directory.user.readonly,https://www.googleapis.com/auth/gmail.labels,https://www.googleapis.com/auth/gmail.modify>

* Click **Authorize** to complete the process.

## Test the Configuration <a href="#test-the-configuration" id="test-the-configuration"></a>

To make sure that the integration is working, you can test it on the platform. Go to **Incident Responder > Mail Configurations** on the left sidebar menu of the dashboard and then click **+ NEW** and choose the mail provider - in this case, Google Workspace.Complete the following fields in the configuration table:

| Name               | Name of the configuration                                                   |
| ------------------ | --------------------------------------------------------------------------- |
| Credential JSON    | Open the JSON file with a text editor and copy/paste all of the information |
| Test Email Address | An active email address to be used for testing purposes                     |
| Test Connection    | Perform a test of the configuration                                         |

The new configuration will now appear in the list of mail configurations if the test was successful.

{% hint style="warning" %}
If an X appears, it indicates there was a problem and the email server integration failed; please review the instructions.
{% endhint %}

## About Permissions

### Application Programming Interface (API) Scopes

API scopes identify the information an application will be able to access on a user’s behalf.

### Permissions Required by the Platform

#### Email (read/write/send) - <https://mail.google.com/>

This permission allows the app access to emails in user mailboxes. Please note, it is only used to enable investigative searches; we do not create, read, edit, or send emails using this permission.

The platform uses this permission to scan and filter users' emails. For example, when the “From” filter is selected as a criterion for investigation, this authorization enables the creation of a list of the emails that meet the specified parameter. Other uses include regex and keyword searches.

This permission enables quick deletion of malicious content without compromising user privacy.

#### View Users on the Domain - /auth/admin.directory.user.readonly

This permission allows the app to read data in the organization's user directory. The platform uses this access to retrieve a client's user list and their email addresses when an investigation has been initiated.

#### Email (Manage Labels) - /auth/gmail.labels

This permission allows the app to create, read, update, and delete labels. The platform uses this authority to mark emails in the user's inbox with a warning message when the client deems this appropriate. For example, after running an investigation, you may choose to warn the user rather than delete the email results.

## FAQ

### Q: Can I start an investigation on Incident Responder without integrating Google Workspace?

A: No. In order to be able to start an investigation and take action on emails, integration with Google Workspace is required.
