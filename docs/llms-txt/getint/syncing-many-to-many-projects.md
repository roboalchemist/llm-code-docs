# Source: https://docs.getint.io/getintio-platform/syncing-many-to-many-projects.md

# Syncing Many to Many Projects

This document provides best practices for handling many-to-many projects in Getint, where a single or multiple projects must synchronize with other target projects across apps such as Jira, ServiceNow, Monday, Azure DevOps, and Asana.

{% hint style="warning" %}
The many-to-many projects feature is only available for Jira–Jira, Jira–ServiceNow, Jira-Azure DevOps, Jira-Monday, and Jira–Asana integrations.
{% endhint %}

### How to Sync Many Projects <a href="#how-to-sync-many-projects" id="how-to-sync-many-projects"></a>

1. To synchronize multiple projects, begin by creating an integration as you normally would. Next, choose Jira as the connector on the left side.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fl9PJWMomH0EJW6xoGLlT%2FStarting%20one%20to%20many%20project.png?alt=media&#x26;token=3b868a31-23aa-4dec-9017-6896241b1a27" alt=""><figcaption></figcaption></figure>

1. Next, either select an existing connection or create a new one. After the connection is set, you’ll see a checkbox labeled “Sync many projects” above the dropdown list.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLToNMLB4rYmsgdcr9uvh%2Fsync%20many%20projects%20option.png?alt=media&#x26;token=d44eb650-6e3f-4dba-b885-70d54bee5367" alt=""><figcaption></figcaption></figure>

1. Select the projects you want to sync, then click “Connect.”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6fqIo75ZJxZVgfRz93Wg%2Fsyncing%20many%20projects%20at%20once.png?alt=media&#x26;token=6638cef1-5365-435b-bad4-57024d531068" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
An “X” appears next to each project name. Click it to remove a project from the selection if you chose the wrong one.
{% endhint %}

1. Select the counterpart application—in this example, Jira. Then repeat the previous steps to choose the projects you want to sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvrpwemwNcSDlufWjxbMU%2FSyncing%20many%20projects%20from%20the%20counterpart%20app.png?alt=media&#x26;token=6656438c-acd2-46ee-adf2-6c14f251e857" alt=""><figcaption></figcaption></figure>

1. Click “Start with Mapping Types” to map the work item types.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8rrEDAJ9qII0HAiaDYjs%2Fmapping%20types.png?alt=media&#x26;token=01d89f25-f4c0-482d-990f-1b8688fd42f6" alt=""><figcaption></figcaption></figure>

1. After mapping issue types, you can start adding fields to them. At the time we’re publishing this article, the “Quick Build” feature is not available for many-to-many projects. You will need to map fields manually.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fmebo3ZqpxUbJ28Ejp5Bt%2FMapping%20issue%20types%20for%20many%20to%20many%20projects.png?alt=media&#x26;token=fcf5e33f-dae5-4458-80c9-454fa2570611" alt=""><figcaption></figcaption></figure>

#### Defining Conditions in Items Routing <a href="#defining-conditions-in-items-routing" id="defining-conditions-in-items-routing"></a>

The next step is to define conditions, as routing refers to the path a work item takes across connected systems. By setting clear rules, you ensure Getint knows which project each incoming work item belongs to and what type it should have.

Please follow the next steps to set up the rules for syncing your items, and then review the subsequent configuration steps to confirm that transitions, field mappings, and workflows are properly aligned.

{% hint style="warning" %}
Item routing must be defined on both sides; otherwise, work items will not sync.
{% endhint %}

1. Please select the project where the item will be routed and specify its issue type. In this example, we are configuring how items from the right side will sync into the corresponding project on the left.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGnbZ5XutM53rF4nQ39VJ%2FMany%20to%20many%20projects%20item%20routing.png?alt=media&#x26;token=31389f66-9f87-428f-bd73-86bf14eb8b4e" alt=""><figcaption></figcaption></figure>

1. Choose the field that will trigger the sync. For example, click “+Add New Field” to add conditions across multiple fields. If all conditions are met, the item will sync to the project you are routing it to.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3aQEQW30fUxCOolSXrTS%2FAdding%20item%20routing%20for%20projects.png?alt=media&#x26;token=45f81c06-549a-4225-8d69-74d473931811" alt=""><figcaption></figcaption></figure>

1. Now repeat the same steps for the right side of the integration. In this case, you are defining how items from the left will sync into the corresponding project on the right as long as conditions are met.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSKA3ckl9DrQs8DuH3WVm%2FAdding%20item%20routing%20for%20both%20projects.png?alt=media&#x26;token=f11d39e4-1401-4f88-9cd5-33676ea20475" alt=""><figcaption></figcaption></figure>

1. Click “Apply” to submit the changes, then save the integration. After that, test the integration to confirm that routing works correctly and items are syncing as expected.

#### Removing or Adding Projects to Existing Integrations <a href="#removing-or-adding-projects-to-existing-integrations" id="removing-or-adding-projects-to-existing-integrations"></a>

You may need to adjust the projects connected to an integration. This can involve adding new projects to expand its scope or removing existing ones to simplify or restructure it. Follow the steps below to make these changes:

* Click the box for the side of the app you want to modify. You can choose either side, depending on your goal.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXgz73ngigDAqR2RO0Yv2%2FAdjusting%20the%20projects%20poscreation.png?alt=media&#x26;token=9555fe30-875e-4e6d-9f98-2324a22f8de7" alt=""><figcaption></figcaption></figure>

* Use the dropdown list to browse your projects and add new ones. You can also remove projects from the integration by clicking the “X” icon next to the project name. This works the same way as when you added or removed projects during the initial setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fgb4vr4ChfZxwkL5nAv3l%2FDisplay%20the%20dropdown%20to%20select%20new%20projects.png?alt=media&#x26;token=b6fcec3a-dced-459a-84e4-53182c30f3df" alt=""><figcaption></figcaption></figure>

* Close the tab and save the integration to submit your changes.

{% hint style="warning" %}
You need to define new conditions to route work items to any project you’ve added.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

Managing integrations is not a one‑time task but an ongoing process. Whether you are adding new projects to expand collaboration or removing existing ones to simplify workflows, the key is to define clear routing conditions and test thoroughly. By carefully mapping fields, setting rules, and validating sync behavior, you ensure that work items flow correctly between systems.

Need more help? Visit our [Help Center](https://getint.io/help-center) or reach out to support by clicking the chat bubble for direct assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDJ1yThyNC3Q2o96EkYmv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=d3229fa0-1281-459d-b681-7f78b855bcaf" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
