# Source: https://docs.getint.io/guides/quickstart.md

# Quickstart

Welcome to Getint, where simplicity meets power! Our goal is to make your first integration not just possible but enjoyable in minutes, whether you're handling straightforward tasks or diving into complex cases. Forget the hassle of installing multiple apps or choosing between an intuitive UI and complex scripting. Getint combines the best of both worlds: a single, user-friendly UI for all your integration needs, with the power of scripting at your fingertips for those unique challenges. To start your free trial, follow the instructions provided in the [Getint documentation](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app).

Feel free to explore the platform and experience the benefits of Getint!

### **Why Choose Getint?**

* **One UI to Rule Them All**: Manage all your connectors from a single interface. No separate installations, no toggling between modes—just seamless integration.
* **Flexibility and Power**: Start with the basics, then effortlessly scale to more advanced features like custom fields, sync directions, filtering, and handling comments, all tailored to your needs.
* **Simplified Setup**: From your very first task integration to syncing attachments and status mapping, see immediate results and scale your setup as needed.

Before diving in, prepare for your integration journey by reviewing our [preparation guide](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration) and claiming your free trial instance, available via the Atlassian Marketplace or directly through Getint SaaS or Getint OnPremise options.

### Iteration 1: Establishing a Basic Integration MVP

#### Step-by-Step Setup

1. **Initiate Your Integration**:
   * Click "**Create Integration"**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgTUZUxhtbdXnPrQiPUIZ%2Ffirst%20workflow%20screen%20qucikstart.png?alt=media&#x26;token=99d60ac9-8ff3-4b80-9996-00236e7cca14" alt=""><figcaption></figcaption></figure>

* Choose **Continuous sync** and learn about integration vs. migration [here](https://chat.openai.com/c/8fae8437-be08-44b9-b71b-1d51c3815ddd).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVTGfwx9DEp63YZNwY0bZ%2Fquickstart%20contin%20sync.png?alt=media&#x26;token=9e8211b6-348b-4004-a7e8-4d9779f18134" alt=""><figcaption></figcaption></figure>

1. **Connect Your First Application (Example: Jira)**:

* Select **Connect App**, choose Jira, and click **Create New Connection**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWPMt3DlF235dF97eTu84%2Fquickstart_1app_1.png?alt=media&#x26;token=3f279819-0315-449e-9325-9d72580c76e8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIrUUbzFInakzSJPpQVgE%2Fquickstart_select_Jira.png?alt=media&#x26;token=309cf168-942e-414b-ade5-a9b1a3d8f483" alt=""><figcaption></figcaption></figure>

* Enter the URL of your Jira instance (e.g., `https://demogetintio.atlassian.net/`).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPTkpvltDTANDHuQdxGP4%2Fquickstart%20instance%20url.png?alt=media&#x26;token=ed635a2d-a3ab-4551-b0b0-3c6a92d45142" alt=""><figcaption></figcaption></figure>

* Name your connection, Provide the email and Personal Access Token for the admin service account.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fhp0j8imS22rByW00vZNg%2Fquickstart%20connect%20app.png?alt=media&#x26;token=58fc25f8-3e8c-40f2-9ea0-b547a78bf7b1" alt=""><figcaption></figcaption></figure>

* Select your newly created connection, choose a test project, and click **Connect.**

1. **Repeat for the Second Application (Example: Azure DevOps)**: Follow the steps above to establish a connection with your second application.
2. **Type Mapping**: Map a Task in Jira to a Task in Azure DevOps. Provide a name for your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBUhiXctRPVFPBNXDpXIK%2Ftype_mapping_quickstart.png?alt=media&#x26;token=30af9c16-e2b1-466a-9b67-9aeee74112d8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMyC0pFb0pW9P1sv7Jer5%2Fqucik%20start%20task%20task.png?alt=media&#x26;token=a1fa97b1-134a-486b-8bfb-61d81ad972a9" alt=""><figcaption></figcaption></figure>

1. **Finalize**: Click **Create**. Your integration is now live!

**Test Your Integration**: Create a task in Jira with a title and description. It should appear in Azure DevOps (or an app of your choice) shortly.

### Iteration 2: Enhancing Integration with Fields, Statuses, and Comments

1. **Refine Your Integration**: Return to **Workflows**, select your integration, and access the previously created Type Mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Flxh79r1zlKWUAKLjt8Mc%2Fqucik_start_task_task_to_field.png?alt=media&#x26;token=f50e4da9-ac89-4a6f-ab53-cc89e8196a3e" alt=""><figcaption></figcaption></figure>

1. **Field Mapping**:&#x20;
   * Map fields between apps, e.g., Jira's **Assignee** to Azure DevOps's **Assigned to**. Adjust mappings for dropdown fields as necessary.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbrMzX4fHOWqtI789zInj%2FField%20mapping%201.png?alt=media&#x26;token=de5e323b-b3ee-4570-b829-23cc6c11d128" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnIFQxOVEynTA13hGG1um%2FField%20mapping%202.png?alt=media&#x26;token=4fdec8c6-1e24-4197-b66d-2f09220f5b1c" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJjp03B2IG9V32VdXneUH%2FField%20mapping%203.png?alt=media&#x26;token=9a0ceb2d-639b-4d3e-94cf-256067cd7a3e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Frgf3EZ8Md7k1CmLHN9Wp%2FField%20mapping%204.png?alt=media&#x26;token=4d65dd9f-5765-4c0c-9ae2-fa2dd23cd90f" alt=""><figcaption></figcaption></figure>

1. **Status Mapping**: Customize your status mappings to fit your workflow.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoaaG8xmffobnFvZPbIl8%2Fquickstart%20statuses%201.png?alt=media&#x26;token=d0ad0f91-2578-4891-b393-5a632cff9251" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6m2gbfA49aAXSs1IKXDe%2Fquickstart%20statuses%202.png?alt=media&#x26;token=f92a7687-10a3-436e-bc08-dfa00e050dea" alt=""><figcaption></figcaption></figure>

1. **Comments and Attachments**: Enable attachment sync and apply your settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft19fGWTAwkizKgAZbwBQ%2Fqucistart_attachments.png?alt=media&#x26;token=db6030ca-ca41-4b66-8f71-845ae18e293d" alt=""><figcaption></figcaption></figure>

1. **Save Your Progress**: Don’t forget to save your integration changes.

**Test Enhancements**: Update your test task with comments, attachments, assignees, and status changes to see the reflection in both systems.

### Iteration 3: Monitoring Your Integration

1. **Access Reporting**: Upon opening the first tab, you'll be presented with a comprehensive table listing all **Performed Syncs** along with their respective statuses. This provides a quick snapshot of your integration activity.
2. **Detailed Sync Analysis**:

* **Sync ID**: For a deeper dive into a specific sync, click on its **ID** (e.g., #139010). This action opens a detailed view of the sync, offering insights into its execution.
* **Trigger Source**: By selecting **Triggered by** (e.g., AM-3235), you can review the task that initiated the sync. A clickable URL facilitates direct access to the triggering task, enabling easy review and analysis.
* **Sync Outcome**: Clicking on **Synced with** (e.g., AM-3235) reveals the task resulting from the sync, complete with a direct URL for quick access. This feature allows you to evaluate the sync's effectiveness and outcome clarity.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FczlaRRHZMyaEqgqZL4zn%2Fquickstart_reporting.png?alt=media&#x26;token=f9fee898-ed51-4ce9-9507-066e34f5fae3" alt=""><figcaption></figcaption></figure>

1. **Troubleshoot**: The **Mode** section is your go-to for assessing the sync's success. A successful sync indicates everything is functioning as expected. Conversely, should you encounter any issues, this section will guide you to identify errors. Should an error be detected, revisit step 1 for troubleshooting. To facilitate resolution, copy the error details and submit a support ticket for assistance.

### Always Here to Help

Encounter a snag? Reach out at any stage of your integration journey. Click the chat icon, schedule a [free onboarding demo call](https://www.getint.io/schedule-demo-call), or [open a support ticket.](https://getintio.atlassian.net/servicedesk/) We're here to ensure your integration success with Getint.

<br>
