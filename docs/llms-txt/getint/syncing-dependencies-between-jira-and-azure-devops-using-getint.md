# Source: https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration/syncing-dependencies-between-jira-and-azure-devops-using-getint.md

# Syncing Dependencies between Jira and Azure DevOps using Getint

1. **Understanding Work Items Links in Azure DevOps:**
   * Azure DevOps offers "Related Work" options for linking tasks, featuring system-defined, process-defined, or user-defined link types. To learn more about how to create a Work link in DevOps, see the guides: [Link work items to objects](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/add-link?view=azure-devops) and [Reference guide for link types](https://learn.microsoft.com/en-us/azure/devops/boards/queries/link-type-reference?view=azure-devops\&source=recommendations).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEc967yDSN0rlTZpQ5d87%2Fimage.png?alt=media&#x26;token=9d9582d0-55e3-4b0e-974d-9d61e83b45e5" alt=""><figcaption></figcaption></figure>

1. **Syncing Jira-DevOps Dependencies with Getint:**
   * Open the integration tab, and choose the integration.
   * Navigate to Dependencies to configure settings.
   * Align Jira dependencies with their Azure DevOps-related work items links.
   * Click "Apply" and then "Save" to implement changes. The next sync will seamlessly integrate the new dependencies.
   * Getint will then update tasks with the corresponding Work link based on matched fields, applying to new and migrated items. Ensure non-migrated tasks have the necessary link field.

{% embed url="<https://youtu.be/vspK_h3gnDU>" %}

**Important Reminder:**

{% hint style="info" %}
When mapping fields, do not select the "Linked Issues" option in dropdowns. Use the Dependency box for creating dependencies between platforms.

Links will be established only if both items, intended to be linked within the app, have already been synchronized by Getint; otherwise, they will be skipped
{% endhint %}
