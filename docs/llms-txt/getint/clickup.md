# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/clickup.md

# ClickUp

## Getint: Simplifying ClickUp Integration and Data Synchronization

Getint connects and synchronizes multiple tools, enabling seamless integrations between platforms such as ClickUp, Jira, Asana, and Azure DevOps. Available as both a Cloud and an on-premise solution, Getint offers the flexibility to meet diverse business requirements.

### Key Topics Covered

* [Setting Up the App](#how-to-set-up-getint-for-clickup)
* [Supported Fields in ClickUp](#supported-fields-for-clickup-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support](#contacting-our-support-team)

Getint synchronizes data across platforms or instances, including ClickUp, allowing users to monitor and manage tasks and activities across projects while integrating ClickUp with other tools.

### How to Set Up Getint for ClickUp

Getint makes it easy to connect systems and synchronize or migrate data between them. Follow the steps below to get started with ClickUp.

**Step 1: Access Getint**

* **For Jira users**: If you plan to integrate Jira with ClickUp, download the Getint app from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1231636/clickup-integration-for-jira-2-way-clickup-connector?hosting=cloud\&tab=overview).
* **For other tools**: Choose between Getint's **SaaS** or **On-Premise** deployment options, depending on your requirements.

**Step 2: Set Up a Connection with ClickUp**

* Ensure you have the necessary [access permissions](https://docs.getint.io/guides/quickstart/connection#clickup) in ClickUp.
* Select **ClickUp** as the application.
* Create a new connection and enter your ClickUp credentials.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with ClickUp, such as **Jira**, **Asana**, or **Azure DevOps**.

**Step 4: Map Types and Fields**

* Match ClickUp entities (for example, tasks, custom fields, or statuses) with their corresponding entities in the other tool.
* Use the **Quick Build** feature for automatic mapping, or manually customize mappings to fit your workflow.

Our support team is always available to help with setup or operational questions.

For additional guidance on using Getint with ClickUp, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira ClickUp Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-clickup-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for ClickUp Integration

Getint enables field mapping between ClickUp and other platforms. Below is an overview of the currently supported field-mapping options and their functionality.

{% hint style="info" %}

#### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. For more detailed information, please refer to this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **ClickUp Field**                                                                      | **One Way** | **Both Ways** |
| -------------------------------------------------------------------------------------- | ----------- | ------------- |
| Assignee                                                                               | ✔️          | ✔️            |
| Comments & Attachments                                                                 | ✔️          | ✔️            |
| <p>Custom Fields</p><p><strong>Dropdown - Labels - Number - People - Text</strong></p> | ✔️          | ✔️            |
| Description                                                                            | ✔️          | ✔️            |
| Id                                                                                     | ✔️          |               |
| Item Type                                                                              | ✔️          |               |
| Status                                                                                 | ✔️          | ✔️            |
| Tags                                                                                   | ✔️          |               |
| Title                                                                                  | ✔️          | ✔️            |
| URL                                                                                    | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Considerations

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Attachments**: Inline images aren’t supported for the Description field.
* **Change History**: Unfortunately, Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account.
* **Issue Types**: Currently, the integration supports ClickUp tasks as the only issue type.
* **Item Hierarchy**: Sub-items are not currently supported in Jira–ClickUp synchronization.
* **Multi-project Support**: Many-to-many project synchronization between Jira and ClickUp is not supported.
* **Synchronization Scope**: In ClickUp, you can specify a Space and Folder, but not an individual List, which means all lists in a folder are synced.
* **Text Formatting Errors**: Formatting is not fully preserved during synchronization; bullet points may not convert correctly in Jira, and embedded links can be removed.

### Contacting Our Support Team

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
