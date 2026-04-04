# Source: https://docs.getint.io/getintio-platform/workflows/hierarchy.md

# Hierarchy

Hierarchy is crucial in organizing work, managing projects, and tracking progress. Within Getint, we provide the possibility to integrate your current workflow with other tools or across other Jira instances/projects. Therefore, setting the hierarchy levels is necessary to incorporate all issues efficiently.

### How Does It Work

This feature is available for all type mappings when building an integration. However, it is important to note that not all apps support hierarchy in the same way as Jira, Asana, Monday, or Azure DevOps, to name a few.

At its core, it revolves around different types of issues, such as:

* **Epics:** Represent high-level initiatives or large work items.
* **Stories/Tasks:** Individual units of work that contribute to an epic.
* **Subtasks:** Manageable tasks required to complete a story.

For example, this would be the standard hierarchy levels in a Jira to Jira integration. For other apps, please ensure you use type mappings that match the items on the other side (i.e., Epic - Epic, Task - Item, Subtask - Subitem).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCLwzz1VbdP77DS7AsZvE%2FJira%20Jira%20Integration%20hierarchy.png?alt=media&#x26;token=4a2db69a-ab52-445d-901c-f6113ceb37ca" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
At present, Getint allows syncing the **Hierarchy** in a standard manner. While it works perfectly for simple scenarios, we’re currently working on improving the feature for more advanced use cases where the hierarchy tree consists of several hierarchy levels and uses links for defining relationships.
{% endhint %}

### How to Set up a Hierarchy

The feature is easily accessible within your type mappings, but it is required to select the correct options for an error-free synchronization.

#### Enabling the Feature

1. Go to your integration and open the corresponding type mapping. For stories/tasks/bugs that you would like to sync the Epic link, you’ll need to go to **Hierarchy** > enable **Synchronize Epic relationship** > display the dropdown and select the **Parent Link (NextGen projects)**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft0F3A3IhgeZSYV6vbmIJ%2FSyncing%20Epic%20Link%20Relationship.png?alt=media&#x26;token=a7ac2f29-f85e-4402-9293-e71a0d85f903" alt=""><figcaption></figcaption></figure>

1. For subtasks, open the corresponding type mapping > enable the **Synchronize Subtasks relationship** > display the dropdown, and select the **Parent Link**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXhpGKpLBxFc75zU9LOrU%2FSyncing%20subtask%20relationship.png?alt=media&#x26;token=6839a4b0-e069-4e36-b8b5-8cc348751d17" alt=""><figcaption></figcaption></figure>

1. Save the changes and test your integration.

### Considerations to take <a href="#considerations-to-take" id="considerations-to-take"></a>

Please make sure the following criteria are met when setting up your hierarchy. Otherwise, issues won’t sync properly.

* Respect the hierarchy levels. The **Quickbuild** feature enables you to align your type mappings appropriately and automatically establishes links for available hierarchy relationships. However, if you’re building your integration manually, it is necessary to order the issues properly. Otherwise, sync will fail as Getint will try to create/update a task first without an existing parent. This would be the correct order: **Epics** first, **Stories/Tasks/Bugs** second, and **Subtasks** last.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FS3rs5gBLbhRgreU86UNN%2FRespecting%20the%20hierarchy%20levels.png?alt=media&#x26;token=497e7ea1-0acb-4c37-b3c7-87dffd7b9f29" alt=""><figcaption><p>Incorrect order for type mappings</p></figcaption></figure>

* Previously, changing the Parent issue would break the sync between linked Tasks and Subtasks, requiring manual reconfiguration or risking duplicate issues. Now, when you assign a new Parent issue, the child task is automatically updated to reflect the change, keeping everything aligned.
* When working with existing projects that have an established hierarchy, it’s advisable to move or bulk-move all the issues in order. For example, move all the Epics to the other side first, and then handle the Tasks and Subtasks afterward. This approach ensures that when updating any tickets or creating subtasks, they will sync accordingly since there’s already an existing parent on the other side.

### Common issues when establishing a hierarchy <a href="#common-issues-when-establishing-a-hierarchy" id="common-issues-when-establishing-a-hierarchy"></a>

When establishing a hierarchy, it is crucial to follow all the recommended steps outlined in this article. Failing to do so may result in errors similar to those listed below.

| Error                                                                                                                                           |                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| <mark style="background-color:red;">**Invalid response status code received (expected: 201 but got 400). Response: {errorMessages":\[]**</mark> | <mark style="background-color:red;">**errors:{"parentId":"Given parent issue does not belong to appropriate hierarchy."}}"**</mark> |

This error occurs when issues are not mapped in the correct sequence required to establish the hierarchy. For example, if the parent issue is not yet synced in the integration or if the items are mapped incorrectly. Additionally, if the hierarchy levels exceed what is currently supported, the workflow will not match the one that was mapped.

| Error                                                                                                                                           |                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <mark style="background-color:red;">**Invalid response status code received (expected: 201 but got 400). Response: {errorMessages":\[]**</mark> | <mark style="background-color:red;">**errors:{"parent":"Could not find issue by id or key."}}"**</mark> |

This error happens when Getint can't find or create the matching item on the other side. First, transfer all the issues, and then set up the **ParentLink**. If the items are out of order, like Subtasks - Subitems, and then Tasks - Items, Getint will struggle to find the parent because it’s attempting to sync the Subtask ahead of everything else.

| Error                                                                                                                                           |                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| <mark style="background-color:red;">**Invalid response status code received (expected: 201 but got 400). Response: {errorMessages":\[]**</mark> | <mark style="background-color:red;">**errors:{"issuetype":"Issue type is a sub-task but parent issue key or id not specified."}}”**</mark> |

This issue will occur when the hierarchy is not configured for subtask types.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Thanks to the Hierarchy feature, Getint allows users to sync issues with their respective parents and children without losing track of their progress. This opens a wide range of possibilities to group any stories, tasks, and subtasks to efficiently manage your workflows.

At Getint, we're dedicated to providing exceptional support throughout your integration journey. Our team is committed to delivering the best customer experience. For any questions about this integration or assistance with the setup process, don't hesitate to open a ticket at our [Support Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team). We're here to help!

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
