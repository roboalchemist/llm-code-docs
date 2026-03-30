# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/troubleshooting-integration-task-retrieval-error.md

# Troubleshooting: Integration Task Retrieval Error

Encountering difficulties in retrieving tasks after setting up and activating your integration? This troubleshooting guide addresses a specific error where the system fails to fetch flow triggers or encounters similar issues during the task retrieval process. Explore the detailed steps below to diagnose and resolve the problem effectively.

### Problem

Following a successful connection and activation of the integration, users may encounter an issue where the system fails to retrieve tasks. An error notification is displayed, indicating a problem with fetching flow triggers or a similar issue.

Upon attempting to fetch flow triggers, users may encounter an error message similar to:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FL2WObhDlmeuEcIRli7RP%2FRetrieval%20Error.png?alt=media&#x26;token=086bdcae-96ed-40d6-a160-816441aca661" alt=""><figcaption></figcaption></figure>

### Solution <a href="#ud83c-udf31-solution" id="ud83c-udf31-solution"></a>

1. Log in to your Jira with Admin credentials.
2. Navigate to "Projects," and locate the specific project integrated with the system.
3. Click on the three dots on the right and select "Project Settings."
4. In the Project Settings page, on the left menu, select "Access."
5. Examine if the user assigned for this integration has adequate access to the project with the correct permissions.
   * If the user is not assigned to the project, the integration will be unable to function properly, lacking the necessary access to create or update items.
6. To add the user, click on "Add People," search for the user, and invite them to join the project. If the user is not found on the list, add the email used during integration creation and send an invitation to join the project.
7. Specify the appropriate role and click "Add."

{% hint style="info" %}
If you continue to encounter issues, please verify that you are logged in with the correct user account that was selected for the integration (the user you chose for the connection), and then test whether you have access to the project.
{% endhint %}

**After adjusting access:**

* Refresh the integration settings.
* Test the integration by triggering an update or creating a new task.

Make sure the integration user has the necessary project access to avoid task retrieval issues.
