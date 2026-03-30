# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/wrike.md

# Wrike

## Getint: Simplifying Wrike Integration and Data Synchronization <a href="#getint-simplifying-wrike-integration-and-data-synchronization" id="getint-simplifying-wrike-integration-and-data-synchronization"></a>

Getint connects and synchronizes multiple tools, allowing teams to create seamless integrations between platforms such as Wrike, Jira, Asana, and Azure DevOps. Available as both a Cloud and an on-premise solution, Getint provides the flexibility to support a wide range of business needs and deployment preferences.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [App Setup](#app-setup)
* [Supported Wrike Fields](#supported-wrike-fields)
* [Limitations and Important Notes](#limitations-and-important-notes)
* [Support Resources and Case Studies](#contacting-our-support-team)

Getint enables data synchronization across platforms and instances, including Wrike. This allows users to track, manage, and update tasks across multiple projects while keeping Wrike aligned with other tools in their ecosystem.

### App Setup <a href="#app-setup" id="app-setup"></a>

Getint simplifies the process of connecting systems and synchronizing or migrating data between them. Follow the steps below to start integrating Wrike with your preferred tools.

**Step 1: Access Getint**

* **For Jira users:** If you are integrating Jira with Wrike, install the Getint app directly from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223936/wrike-integration-for-jira-wrike-connector?hosting=cloud\&tab=overview).
* **For other platforms:** Select either the browser version ([app.getint.io](http://app.getint.io/)) or On-Premise version of Getint based on your organizational requirements.

**Step 2: Set Up a Connection with Wrike**

* Ensure you have the necessary [access permissions](https://docs.getint.io/guides/quickstart/connection#wrike) in Wrike.
* Select **Wrike** as the application.
* Create a new connection and enter your Wrike credentials.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with Wrike, such as **Jira** or **Azure DevOps**.

**Step 4: Map Types and Fields**

* Match Wrike types and fields with their corresponding entities in the other tool.
* Use the **Quick Build** option for automatic mapping, or define mappings manually to better align with your workflows.

Our support team is always available to help with setup or operational questions.

For additional guidance on using Getint with Wrike, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira Wrike Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-wrike-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Wrike Fields <a href="#supported-wrike-fields" id="supported-wrike-fields"></a>

Getint enables field mapping between Wrike and other platforms. Below is an overview of the currently supported field-mapping options and their functionality.

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. For more detailed information, please refer to this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Wrike Field**                                                          | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------ | ----------- | ------------- |
| Assignee                                                                 | ✔️          | ✔️            |
| Comments & Attachments                                                   | ✔️          | ✔️            |
| Custom Fields                   **Date - Number - Single Select - Text** | ✔️          | ✔️            |
| Description                                                              | ✔️          | ✔️            |
| Due Date                                                                 | ✔️          | ✔️            |
| Id                                                                       | ✔️          |               |
| Is Milestone                                                             | ✔️          |               |
| Start Date                                                               | ✔️          | ✔️            |
| Status                                                                   | ✔️          | ✔️            |
| Title                                                                    | ✔️          | ✔️            |
| URL                                                                      | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Important Notes <a href="#limitations-and-important-notes" id="limitations-and-important-notes"></a>

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Change History**: Unfortunately, Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account.
* **Multi-project support**: Many-to-many project synchronization between Jira and Wrike is not supported.
* **Sub-tasks**: Currently, syncing sub-tasks is not supported.
* **Text Formatting Errors**: Formatting is not fully preserved during synchronization. For example, bullet points may not convert correctly in Jira.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
