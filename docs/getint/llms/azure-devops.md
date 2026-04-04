# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/azure-devops.md

# Azure DevOps

## Getint: Simplifying Azure DevOps Integration and Data Synchronization <a href="#getint-simplifying-azure-devops-integration-and-data-synchronization" id="getint-simplifying-azure-devops-integration-and-data-synchronization"></a>

Getint is expertly designed to integrate and synchronize an extensive range of tools. It accommodates a variety of connectivity scenarios, such as Azure DevOps - Jira, Azure DevOps - Asana, Azure DevOps - Monday, Azure DevOps - ServiceNow, and more. With its availability as both a Software-as-a-Service (SaaS) and On-Premise solution, Getint offers the versatility to meet the unique requirements of various businesses.

### What Does this Article Cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-azure-devops)
* [Supported Fields in Azure DevOps](#supported-fields-in-azure-devops)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting our Support Team - Case Studies](#contacting-our-support-team)

**Getint** facilitates smooth data synchronization across various platforms and instances. It specifically supports **Azure,** allowing users to monitor and manage tasks in diverse environments effectively. Additionally, it enables seamless integration with other platforms.

### Setting Up Getint for Azure DevOps <a href="#setting-up-getint-for-azure-devops" id="setting-up-getint-for-azure-devops"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as Azure DevOps, map types (i.e. Epic - Epic), and fields (i.e. Assignee - Assigned to). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Azure integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Azure with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration)):

1. **Access Getint:** If you’re using Jira, navigate to the "Apps" section, search for new apps, and acquire the app from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223931/azure-devops-integration-for-jira-azure-devops-connector?hosting=cloud\&tab=overview). Alternatively, if you need to integrate Azure DevOps with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS](https://www.getint.io/contact).
2. **Token Generation for Azure DevOps:** Click on your user profile icon, navigate to the "Personal access tokens" section, and click "New token." Provide a name for the token, select the relevant organization, set an expiration, and choose "Full Access" in the scopes. This token will serve as your password to connect with Getint.
3. **Establish a Connection with Azure DevOps:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose "Azure DevOps." Select "Create New" to establish a new connection with your Azure DevOps instance. Name your connection, and add the URL of your Azure instance. Provide the login credentials.
4. **Choose and Connect the Second App:** You can select and link an additional tool to integrate with Azure DevOps. Options include another Azure instance, ServiceNow, Jira, or any other supported tool.
5. **Map Types and Fields:** Link "Azure types" (Epics, Tasks, Issues) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team can provide guidance and assistance.

### Supported Fields in Azure DevOps <a href="#supported-fields-in-azure-devops" id="supported-fields-in-azure-devops"></a>

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

| **Azure DevOps Field**                                                                                                                       | **One Way** | **Both Ways** |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Activated By                                                                                                                                 | ✔️          | ✔️            |
| Activated Date                                                                                                                               | ✔️          | ✔️            |
| Activity                                                                                                                                     | ✔️          | ✔️            |
| Area ID                                                                                                                                      | ✔️          | ✔️            |
| Area Path                                                                                                                                    | ✔️          | ✔️            |
| Assigned To (Assignees)                                                                                                                      | ✔️          | ✔️            |
| Changed By                                                                                                                                   | ✔️          | ✔️            |
| Closed By                                                                                                                                    | ✔️          | ✔️            |
| Closed Date                                                                                                                                  | ✔️          | ✔️            |
| Created By                                                                                                                                   | ✔️          | ✔️            |
| Completed Work                                                                                                                               | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Decimal - Identity - Integer - Picklist - Picklist integer - Text (Single/Multiple lines)</strong></p> | ✔️          | ✔️            |
| Description (System.Description)                                                                                                             | ✔️          | ✔️            |
| ID                                                                                                                                           | ✔️          |               |
| Iteration ID                                                                                                                                 | ✔️          | ✔️            |
| Iteration Path                                                                                                                               | ✔️          | ✔️            |
| Priority                                                                                                                                     | ✔️          | ✔️            |
| Reason                                                                                                                                       | ✔️          | ✔️            |
| Remaining Work                                                                                                                               | ✔️          | ✔️            |
| Resolved By                                                                                                                                  | ✔️          | ✔️            |
| Resolved Date                                                                                                                                | ✔️          | ✔️            |
| Stack Rank                                                                                                                                   | ✔️          | ✔️            |
| State                                                                                                                                        | ✔️          | ✔️            |
| State Change Date                                                                                                                            | ✔️          | ✔️            |
| Status                                                                                                                                       | ✔️          | ✔️            |
| Story Points                                                                                                                                 | ✔️          | ✔️            |
| Tags                                                                                                                                         | ✔️          | ✔️            |
| Target Date                                                                                                                                  | ✔️          | ✔️            |
| Team Project                                                                                                                                 | ✔️          | ✔️            |
| Title                                                                                                                                        | ✔️          | ✔️            |
| URL                                                                                                                                          | ✔️          |               |
| Work Item Type                                                                                                                               | ✔️          | ✔️            |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Supported Item Types for Azure DevOps Integration

| Code Review Request | Code Review Response |
| ------------------- | -------------------- |
| Epic                | Feedback Request     |
| Issue               | Feedback Response    |
| Shared Parameter    | Task                 |

### Limitations to be Considered

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* When Getint creates a new issue in Azure DevOps, it will always be one specific type of issue: an Epic, an Issue, a Test Plan, or a Task (to name a few). You can set the default item type with Getint or manually change it in Azure after it's created.
* Comments added to the issue will appear under the user account you choose to create the connection. To ensure seamless integration, creating a dedicated Service Account is recommended to build your integration. Although the original author’s name will appear in the comment footer, the comment will still be associated with the account that established the connection.
* Unfortunately, integrating the history of changes is not possible.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
