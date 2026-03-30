# Source: https://docs.getint.io/getintio-platform/connections/changing-the-url-or-transitioning-between-instances.md

# Changing the URL or Transitioning Between Instances

To update your URL or switch instances (e.g., from Jira Cloud to Jira Data Center), Getint offers a straightforward process to adjust connections within integrations for a smooth transition. This guide outlines the necessary steps for changing your URL or transitioning to a new instance.

### **How to Change the URL in Your Integration** <a href="#how-to-change-the-url-in-your-integration" id="how-to-change-the-url-in-your-integration"></a>

If your Jira Cloud URL has changed:

1. Open the option to create an integration in Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fh9oilaDY7dLq878IrIqU%2FContinous%20Sync%20-%20Migration%20-%20Git%20Integration%20Sync.png?alt=media&#x26;token=2f168d7d-88a1-408c-a27b-d5c1545ab258" alt=""><figcaption></figcaption></figure>

1. Follow the steps to establish a new connection using the new URL (if you haven't already) and exit the creation tab. For further instructions, refer to our [Connection guide](https://docs.getint.io/guides/quickstart/connection).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcPQIosnkdgw7eyKmkk3k%2FFollow%20the%20steps%20to%20add%20the%20connection.png?alt=media&#x26;token=a6ba44c6-fa48-47d3-8528-97c9b916251f" alt=""><figcaption></figcaption></figure>

1. Open the integration you want to modify, click **More > Settings** in the top right, disable it, and save.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7wlM1eO7suZIoFw0juWv%2FModify%20the%20settings.png?alt=media&#x26;token=d376b929-a796-4b29-b86b-fcbfb53365dd" alt=""><figcaption></figcaption></figure>

1. Select the app icon you want to change.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbpOtcCzBmsCQHveGXZMI%2Fselect%20the%20app%20icon%20you%20want%20to%20change.png?alt=media&#x26;token=c89e73d4-f590-4f87-93c7-2ffd9a855a12" alt=""><figcaption></figcaption></figure>

1. Choose **Change Connection.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoCMIpXDcVXlP0Hi25bU1%2FChange%20connection.png?alt=media&#x26;token=8c0ed87a-18c5-4f02-b573-57b07d8a66e6" alt=""><figcaption></figcaption></figure>

1. Select the new connection and select **Change Connection.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2FdWpSg5CaDLlkIoT7FS%2Fselect%20the%20new%20connection.png?alt=media&#x26;token=fe2727dd-e7dc-4de7-9f16-0b4bd057f48b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FC7dtyPHfOv0jYFqLoioC%2Fselect%20change%20connection.png?alt=media&#x26;token=050ef441-fbc9-4492-8b36-e40c6780c69a" alt=""><figcaption></figcaption></figure>

1. Save the changes and re-enable the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoDjou786BSAvMMw8fEjX%2Fsave%20changes%20and%20re-enable%20the%20integration.png?alt=media&#x26;token=83a814d6-bc9c-4813-a7f0-2199b7aaa358" alt=""><figcaption></figcaption></figure>

#### **Transitioning Between Jira Instances** <a href="#transitioning-between-jira-instances" id="transitioning-between-jira-instances"></a>

If you’re transitioning between Jira instances, such as moving from Jira Data Center to Jira Cloud:

1. **Create a New Connection**:
   * Set up a new connection with the appropriate URL and credentials for the new Jira instance.
   * Ensure the new connection has the same permissions as the previous one to avoid data sync issues.
2. **Edit the Integration**:
   * Go to the **Integration Editor** and update the connection to point to the newly created one.
3. **Test the Sync**:
   * Verify that data syncs correctly between the new instance and the destination app.

{% hint style="warning" %}
**Warning:**\
Switching from **Jira Data Center to Jira Cloud** (or vice versa) by simply updating the connection **may not work** due to key structural differences between the two platforms, including:\
✔ **Field IDs** – Jira Cloud and Jira Data Center assign different internal IDs to custom and system fields, which may break mappings.\
✔ **Project IDs** – Each Jira instance generates unique project IDs, making direct migration difficult.\
✔ **User IDs** – Jira Cloud uses **Atlassian Accounts**, while Jira Data Center may rely on **internal directories or LDAP**, causing user mismatches.\
✔ **Field Names & Workflows** – Some fields, workflows, and statuses may **not be identical**, leading to synchronization issues or failed updates.

If you’re moving between Jira Cloud and Jira Data Center, we strongly recommend using Getint’s Migration option to ensure a proper migration rather than just changing the connection.
{% endhint %}

#### **When to Use the "Change Connection" Feature** <a href="#when-to-use-the-change-connection-feature" id="when-to-use-the-change-connection-feature"></a>

The **Change Connection** feature is designed to help with:

* **URL Changes**: For example, updating your Jira Cloud instance URL.
* **Account Updates**: Switching from a personal account to a service account.
* **Connection Errors**: Resolving connection-related issues by switching to a new connection.

#### **Best Practices and Considerations** <a href="#best-practices-and-considerations" id="best-practices-and-considerations"></a>

**Pros**:

* Easily update your connection without creating a new integration.
* Seamlessly transition between accounts or fix connection issues without affecting existing data.
* Supports URL changes for the same instance.

**Cons**:

* Ensure the new connection has identical permissions to access fields and issues already synced; otherwise, data sync errors may occur.
* Avoid using this feature for significant changes, like switching projects or migrating between fundamentally different instances (moving to a different app, for example)

{% hint style="info" %}
For more detailed modifications, you can access the **Connections** settings in the **Workflows** section of Getint. Refer to our [Connections Documentation](https://docs.getint.io/getintio-platform/connections) for additional guidance.
{% endhint %}

#### **Conclusion** <a href="#conclusion" id="conclusion"></a>

Getint's connection management features simplify the process of changing URLs or transitioning to a new instance. Ensure the new connection's permissions align with the previous ones to prevent disruptions.

For additional support, reach out to our [Support Portal](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
