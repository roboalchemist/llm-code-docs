# Source: https://docs.getint.io/getintio-platform/managing-and-exporting-integrations.md

# Managing and Exporting Integrations

With Getint, you have tools to manage, organize, and export your integrations. Whether you're running multiple syncs across platforms or need to back up your configurations, this guide covers how to use the **Integrations List**, organize them into **Groups**, and leverage the **Export/Import** functionality.

### Integrations List

The **Integrations List** displays all your active and inactive integrations in one place. For each integration, the following columns are shown:

* **Name**: The custom name of your integration.
* **Last Run**: The most recent sync timestamp.
* **Status**: Indicates if the integration is currently active or disabled.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6WVVmysYrj8dr4zavOFq%2FChecking%20the%20Integration%20list.png?alt=media&#x26;token=f51fa27f-e9ce-4982-9c1e-634d0f6e9edb" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Integrations marked as disabled won’t run until you re-enable them.
{% endhint %}

### Filtering Integrations

You can now quickly narrow down your view using the filters at the top of the page:

* **Owner**: Filter by the user who created the integration.
* **Application**: View integrations by app type (i.e., Jira, Asana, Azure DevOps).
* **Status**: Show only active or disabled integrations.
* **Name Search**: Use the text field to search by integration name.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQ4F5EVKdc0QUGVpLFaXw%2FFiltering%20integrations%201.png?alt=media&#x26;token=660ada4f-084e-4727-8570-d39e72ab68d1" alt=""><figcaption></figcaption></figure>

These filters make it easier to manage large sets of integrations, especially in collaborative environments.

### Organizing Integrations in Groups

Groups let you keep related integrations together for easier navigation and maintenance. By default, all integrations start in the **Default** group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7DxfXRWWcrdHD0Lm2UDq%2FOrganizing%20Integrations%20in%20Groups.png?alt=media&#x26;token=dbf3b9ce-9726-49d9-9ea3-1d80f1e921ae" alt=""><figcaption></figcaption></figure>

#### How to Assign an Integration to a Group

1. Click the name of the integration in the **Integrations List** to open it.
2. Click the **Settings** button to open the integration settings panel.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZqi8qu5vwwj9dO49Kxkl%2FAssigning%20an%20integration%20to%20a%20group.png?alt=media&#x26;token=33c36bb2-8ffe-46dd-b913-e65f43283f6f" alt=""><figcaption></figcaption></figure>

1. &#x20;In the **Group Name** field, enter a name for your group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSQj9hwV0ZzVhqqm3UgMX%2FAdding%20a%20name%20to%20the%20group.png?alt=media&#x26;token=7ec532e4-610d-46e2-9a58-dcee53408c2f" alt=""><figcaption></figcaption></figure>

1. Click **Save** in the pop-up, then **Save Integration** to apply the change.

The new group will appear in the **Groups** dropdown menu at the top. Clicking on a group filters the list to show only the integrations assigned to it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzfFQDntM9MRCeOPnCwIO%2FLooking%20for%20Groups.png?alt=media&#x26;token=9876954e-f932-4dc7-9138-8500f77b0bb0" alt=""><figcaption></figcaption></figure>

### Integration Actions: Duplicate and Export

In the **Actions** column of the Integrations List, you can:

* **Duplicate**: Create a copy of an existing integration, useful for reusing configuration templates across teams or projects.
* **Export**: Copy the script for the integration configuration and save (for backup), or apply it to duplicate the integration. This is ideal for backup purposes or transferring setups between environments.
* **Export with Connections**: Copy the script for the integration configuration with their respective connections. Save it for backup or apply it to duplicate the integration. This is perfect for backup or transferring setups between new environments.
* **Delete**: This is used to remove unused integrations.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8Of7LmDl1aK7INNRoOD4%2FIntegration%20Actions%20Duplicate%20and%20Export.png?alt=media&#x26;token=946a3ea0-9390-41fa-814c-8da42d0bdb4b" alt=""><figcaption></figcaption></figure>

### How to Export and Import Integrations

#### Exporting an Integration

1. In the **Actions** column of the desired integration, click the **Export** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJt9BpG8ABqjZmpvjjDPU%2FIntegration%20Actions%20Duplicate%20and%20Export.png?alt=media&#x26;token=700fa7e1-3eb2-40f2-bbb8-bf326906e880" alt=""><figcaption></figcaption></figure>

1. A script containing the integration's configuration will show after setting up an encryption key.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVo21p1HesjLVBdfSmQCt%2Fscript%20library.png?alt=media&#x26;token=2897d22a-1cc7-4dfd-8970-50a85de5021e" alt=""><figcaption></figcaption></figure>

#### Importing an Integration

1. Click the **Import** button located above the Integrations List.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNJbRfm6w141FyZavyg1h%2FImporting.png?alt=media&#x26;token=9a2c4fb3-8421-4bda-bb7a-1f7ec2bf5aab" alt=""><figcaption></figcaption></figure>

1. Paste the previously exported script from your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI20iqwwUWvBSw5mTpPvZ%2Fpreviously%20exported%20script.png?alt=media&#x26;token=c19c41c7-d8bf-48e7-8334-531a8a86e6ae" alt=""><figcaption></figcaption></figure>

1. Click Next, then name the new integration and select the connections.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLuV3QqQcBfa5RTizKV7o%2FImporting%20the%20integration%20script.png?alt=media&#x26;token=244c6ee5-0057-4840-aaf6-1aaa606d4b15" alt=""><figcaption></figcaption></figure>

1. Click on **Import,** and the integration will be recreated using the imported configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgDVxVt8bOmLGZYYWLz3S%2Frecreate%20an%20integration%20using%20the%20import.png?alt=media&#x26;token=4f6a7c12-d70e-425e-9c47-355d6d032182" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The new Integration is disabled by default and needs to be enabled to start running.
{% endhint %}

This feature is especially useful for teams migrating between environments or maintaining version control over their integration setups.

***

Need more help? Visit our [Help Center](https://help.getint.io/) or contact support for hands-on guidance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
