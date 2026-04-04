# Source: https://docs.getint.io/getintio-platform/workflows/managing-and-exporting-integrations-in-getint.md

# Managing and Exporting Integrations in Getint

With Getint, you have tools to manage, organize, and export your integrations. Whether you're running multiple syncs across platforms or need to back up your configurations, this guide covers how to use the **Integrations List**, organize them into **Groups**, and leverage the **Export/Import** functionality.

### Integrations List <a href="#integrations-list" id="integrations-list"></a>

The **Integrations List** displays all your active and inactive integrations in one place. For each integration, the following columns are shown:

* **Name**: The custom name of your integration.
* **Last Run**: The most recent sync timestamp.
* **Status**: Indicates if the integration is currently active or disabled.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FARsfEeQdgYhq4rKXTDEf%2FIntegration%20List.png?alt=media&#x26;token=b3f33cb0-c8bd-4685-9dce-efcf8afccd4c" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Integrations marked as disabled won’t run until you re-enable them.
{% endhint %}

### Filtering Integrations <a href="#filtering-integrations" id="filtering-integrations"></a>

You can now quickly narrow down your view using the filters at the top of the page:

* **Owner**: Filter by the user who created the integration.
* **Application**: View integrations by app type (i.e., Jira, Asana, Azure DevOps).
* **Status**: Show only active or disabled integrations.
* **Name Search**: Use the text field to search by integration name.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtAO9oeE8Dxj1ZEHZpir1%2FFiltering%20Integrations.png?alt=media&#x26;token=8a1abfc8-6f61-44e6-80d7-e8023ab9f40b" alt=""><figcaption></figcaption></figure>

These filters make it easier to manage large sets of integrations, especially in collaborative environments.

### Organizing with Groups <a href="#organizing-with-groups" id="organizing-with-groups"></a>

Groups let you keep related integrations together for easier navigation and maintenance. By default, all integrations start in the **Default** group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfpwMBicLaXQQhCyXygnT%2FOrganizing%20with%20Groups.png?alt=media&#x26;token=7dd81300-a3b6-4c4f-9781-4b0fb342d596" alt=""><figcaption></figcaption></figure>

#### How to Assign an Integration to a Group <a href="#how-to-assign-an-integration-to-a-group" id="how-to-assign-an-integration-to-a-group"></a>

1. Click the name of the integration in the **Integrations List** to open it.
2. Click the **Settings** button to open the integration settings panel.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAjlQZkq9OpOecC507rGh%2FHow%20to%20Assign%20an%20Integration%20to%20the%20Groups.png?alt=media&#x26;token=cdfdf8d3-beb0-46d0-b502-31d19c8112c5" alt=""><figcaption></figcaption></figure>

1. In the **Group Name** field, enter a name for your group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfXadpOXq44PphLXIoLBW%2FNaming%20the%20Group.png?alt=media&#x26;token=5f2be52c-7ea3-4dc5-aa7f-ec468c891ff3" alt=""><figcaption></figcaption></figure>

1. Click **Save** in the pop-up, then **Save Integration** to apply the change.

The new group will appear in the **Groups** dropdown menu at the top. Clicking on a group filters the list to show only the integrations assigned to it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXTqsc4q33fvcnxfjYs33%2FSaving%20the%20Group.png?alt=media&#x26;token=8e43245c-7b32-4930-8f10-65849b46625b" alt=""><figcaption></figcaption></figure>

### Integration Actions: Duplicate and Export <a href="#integration-actions-duplicate-and-export" id="integration-actions-duplicate-and-export"></a>

In the **Actions** column of the Integrations List, you can:

* **Duplicate**: Create a copy of an existing integration, useful for reusing configuration templates across teams or projects.
* **Export**: Copy the script for the integration configuration and save (for backup), or apply it to duplicate the integration. This is ideal for backup purposes or transferring setups between environments.
* **Export with Connections**: Copy the script for the integration configuration with their respective connections. Save it for backup or apply it to duplicate the integration. This is perfect for backup or transferring setups between new environments.
* **Delete**: This is used to remove unused integrations.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpXBVuDQeNQlU6NVOUo7H%2FDuplicate%20%26%20Export.png?alt=media&#x26;token=310d0a84-f5a5-45f0-a218-9039fb164f0b" alt=""><figcaption></figcaption></figure>

### How to Export and Import Integrations <a href="#how-to-export-and-import-integrations" id="how-to-export-and-import-integrations"></a>

#### Exporting an Integration <a href="#exporting-an-integration" id="exporting-an-integration"></a>

1. In the **Actions** column of the desired integration, click the **Export** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2XlnCy7S9SdI38IVgirt%2FHow%20to%20Export%20and%20Import%20Integrations.png?alt=media&#x26;token=bed76e99-414b-4c2f-8232-f0649428e373" alt=""><figcaption></figcaption></figure>

1. A script containing the integration's configuration will show after setting up an encryption key.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzNa8QdJs8AyS7NV70X84%2FExport%20Integration.png?alt=media&#x26;token=6e2f58ad-8659-4c8b-9d30-86f55ec9cf8e" alt=""><figcaption></figcaption></figure>

#### Importing an Integration <a href="#importing-an-integration" id="importing-an-integration"></a>

1. Click the **Import** button located above the Integrations List.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaanACMuLviFCmf6qixiE%2FImporting%20an%20Integration.png?alt=media&#x26;token=4922c1b8-f351-46e1-914c-6b110a2424ba" alt=""><figcaption></figcaption></figure>

1. Paste the previously exported script from your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmWDXlGNEluB9McXDBUlC%2FPasting%20the%20Import%20Script.png?alt=media&#x26;token=0296dd80-09f7-417f-9f8c-e3aaf3abd759" alt=""><figcaption></figcaption></figure>

1. Click **Next**, then name the new integration and select the connections.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7sV5BklVJAShrM5yrG3t%2FNaming%20the%20Imported%20integration.png?alt=media&#x26;token=b902d29a-4e60-4610-8efd-43590e6e66b0" alt=""><figcaption></figcaption></figure>

1. Click on **Import,** and the integration will be recreated using the imported configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoMC99Q8JkVBUler1CheU%2FRecreating%20the%20Integration%20with%20the%20Import%20option.png?alt=media&#x26;token=6a6b2f74-1115-46ec-bf4f-30c84b131ed2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The new Integration is disabled by default and needs to be enabled to start running.
{% endhint %}

This feature is especially useful for teams migrating between environments or maintaining version control over their integration setups.

Need more help? Visit our [Help Center](https://help.getint.io/) or contact support for hands-on guidance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FH3BvyKjK5sA4LofW0tkC%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=5291e1d4-30f6-45cf-b7da-9f7aee627b86" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
