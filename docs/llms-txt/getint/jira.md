# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/jira.md

# Jira

## Getint: Simplifying Jira Integration and Data Synchronization <a href="#title-text" id="title-text"></a>

Getint is expertly designed to integrate and synchronize an extensive range of tools. It accommodates a variety of connectivity scenarios, such as Jira - Jira, Jira - Azure DevOps, Jira - Asana, Jira - ServiceNow, and more. With its availability as both a Software-as-a-Service (SaaS) and On-Premise solution, Getint offers the versatility to meet the unique requirements of various businesses.

### What does this article cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-jira)
* [Supported Fields in Jira](#supported-fields-in-jira)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

Getint enables seamless data synchronization within the same platform or different platforms/different instances. It supports Jira and Jira Service Management of all types (Cloud, Server, Data Center), and across different projects. Allowing users to efficiently track and manage Jira tickets, tasks, bugs, and epics in diverse Jira environments, as well as integrating Jira with other platforms.

### Setting up Getint for Jira <a href="#setting-up-getint-for-jira" id="setting-up-getint-for-jira"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as Jira, map types (i.e., Task - Task), and fields (i.e., Priority - Priority). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Jira integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Jira with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-jira-integration)):

1. **Access the Getint App in Jira:** The app is available for download in the Atlassian Marketplace. After the installation, navigate to Jira, go to "Apps," and select "the Getint app." Select "Create Integration" then "Continuous Sync" or "Migration" based on your requirements.
2. **Token Generation for Jira Cloud:** Visit Atlassian Account Settings. Go to Security, navigate to the API Token section, and generate a token. This token serves as the password for the Jira Cloud.
3. **Establish a Connection with Jira:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose Jira. Select "Create New" to establish a new connection with your Jira instance. Name your connection, and add the URL of your Jira instance (without "/" at the end). Provide the login credentials.
4. **Choose and Connect the Second App:** Choose and connect another tool you'd like to integrate with your Jira—either another Jira instance, DevOps, ServiceNow, Salesforce, or any other tool that we support.
5. **Map Types and Fields:** Link Jira types (Task, Bug, Epic, Story) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team is readily available to provide guidance and help.

### Supported Fields in Jira <a href="#supported-fields-in-jira" id="supported-fields-in-jira"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

<table data-header-hidden><thead><tr><th width="249"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Jira Field</strong></td><td><strong>One Way</strong></td><td><strong>Both Ways</strong></td></tr><tr><td>Assignee</td><td>✔️</td><td>✔️</td></tr><tr><td>Attachments</td><td>✔️</td><td>✔️</td></tr><tr><td>Created</td><td>✔️</td><td> </td></tr><tr><td>Comments</td><td>✔️</td><td>✔️</td></tr><tr><td><p>Custom fields</p><p><strong>Short text - Paragraph - Date - Number - Time Stamp - Labels - Dropdown - Checkbox - People - Dependent dropdown - URL</strong></p></td><td>✔️</td><td>✔️</td></tr><tr><td>Description</td><td>✔️</td><td>✔️</td></tr><tr><td>Design</td><td>✔️</td><td>✔️</td></tr><tr><td>Due date</td><td>✔️</td><td>✔️</td></tr><tr><td>Flagged</td><td>✔️</td><td>✔️</td></tr><tr><td>ID</td><td>✔️</td><td> </td></tr><tr><td>Issue color</td><td>✔️</td><td>✔️</td></tr><tr><td>Issue key</td><td>✔️</td><td> </td></tr><tr><td>Issue type name</td><td>✔️</td><td> </td></tr><tr><td>Labels</td><td>✔️</td><td>✔️</td></tr><tr><td>Linked issues</td><td>✔️</td><td>✔️</td></tr><tr><td>Priority</td><td>✔️</td><td>✔️</td></tr><tr><td>Project key</td><td>✔️</td><td> </td></tr><tr><td>Project name</td><td>✔️</td><td> </td></tr><tr><td>Reporter</td><td>✔️</td><td>✔️</td></tr><tr><td>Reporter display name</td><td>✔️</td><td> </td></tr><tr><td>Reporter email</td><td>✔️</td><td> </td></tr><tr><td>Request type</td><td>✔️</td><td>✔️</td></tr><tr><td>Resolution</td><td>✔️</td><td> </td></tr><tr><td>Resolved</td><td>✔️</td><td>✔️</td></tr><tr><td>Satisfaction</td><td>✔️</td><td></td></tr><tr><td>Sprint</td><td>✔️</td><td> </td></tr><tr><td>Start date</td><td>✔️</td><td>✔️</td></tr><tr><td>Status</td><td>✔️</td><td>✔️</td></tr><tr><td>Story point estimate</td><td>✔️</td><td>✔️</td></tr><tr><td>Story points</td><td>✔️</td><td>✔️</td></tr><tr><td>Subtasks</td><td>✔️</td><td>✔️</td></tr><tr><td>Time tracking - Original estimate</td><td>✔️</td><td>✔️</td></tr><tr><td>Time tracking - Remaining estimate</td><td>✔️</td><td> </td></tr><tr><td>Time tracking - Time spent</td><td>✔️</td><td> </td></tr><tr><td>Title (Summary)</td><td>✔️</td><td>✔️</td></tr><tr><td>Updated</td><td>✔️</td><td> </td></tr><tr><td>URL</td><td>✔️</td><td> </td></tr></tbody></table>

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered <a href="#limitations-to-be-considered" id="limitations-to-be-considered"></a>

At Getint, we're constantly updating our supported features, fields, and compatible apps. However, there are a few limitations you should be aware of:

* When a new issue is created in Jira by Getint, it will always be one type of issue, whether that's a Task, an Epic, a Feature, or a Bug. You can set the default item type using a rule or manually change it in Jira after it's created.
* Comments will be added as the user you choose to create the connection. Therefore, it is advised to create a dedicated Service Account to build your integration. The original author will appear in the comment footer; however, it will still be assigned to the account that established the connection.
* The history of changes can't be integrated.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
