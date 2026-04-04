# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/zendesk.md

# Zendesk

## Getint: Simplifying Zendesk Integration and Data Synchronization <a href="#getint-simplifying-zendesk-integration-and-data-synchronization" id="getint-simplifying-zendesk-integration-and-data-synchronization"></a>

**Getint** connects and synchronizes various tools, enabling integrations between Zendesk and platforms like Jira, Asana, or Azure DevOps. It offers both SaaS and On-Premise solutions, allowing businesses to choose the deployment option that best fits their needs.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Setting Up the App](#how-to-set-up-getint-for-zendesk)
* [Supported Fields in Zendesk](#supported-fields-for-zendesk-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

Getint synchronizes data across platforms and instances, including Zendesk. It allows users to track and manage tasks or activities across projects while connecting Zendesk with other tools for improved coordination.

### How to Set Up Getint for Zendesk <a href="#how-to-set-up-getint-for-zendesk" id="how-to-set-up-getint-for-zendesk"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* For Jira users: If you want to integrate Jira with Zendesk, download the app from the Atlassian Marketplace [here](https://marketplace.atlassian.com/apps/1223934/zendesk-integration-for-jira-2-way-zendesk-connector?hosting=cloud\&tab=overview).
* For other tools: Select between Getint On-Premise or SaaS options.

**Step 2: Set Up a Connection with Zendesk**

* Ensure you have the correct [access permissions](https://docs.getint.io/guides/quickstart/connection#zendesk).
* Choose Zendesk as the app, create a new connection, and enter your Zendesk credentials.

**Step 3: Connect to Another Tool**

* Pick the platform you want to integrate with Zendesk, such as Jira.

**Step 4: Map Types and Fields**

* Match Zendesk categories with their counterparts in the other tool.
* Use the **Quick Build** feature for automatic mapping or customize mappings manually if needed.

Our support team is always available to assist with any setup or operational challenges.

For additional guidance on using Getint with Zendesk, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira Zendesk Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-zendesk-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for Zendesk Integration <a href="#supported-fields-for-zendesk-integration" id="supported-fields-for-zendesk-integration"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires additional steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Zendesk Field**                                                                 | **One Way** | **Both Ways** |
| --------------------------------------------------------------------------------- | ----------- | ------------- |
| Assignee                                                                          | ✔️          | ✔️            |
| Brand                                                                             | ✔️          | ✔️            |
| Comments & Attachments                                                            | ✔️          | ✔️            |
| <p>Custom Fields:</p><p><strong>Date - Dropdown - Multi-Line - Text</strong> </p> | ✔️          | ✔️            |
| Description                                                                       | ✔️          | ✔️            |
| Group                                                                             | ✔️          | ✔️            |
| ID                                                                                | ✔️          |               |
| IS Side Conversation                                                              | ✔️          |               |
| Priority                                                                          | ✔️          | ✔️            |
| Recipient                                                                         | ✔️          | ✔️            |
| Requester email (on-create only)                                                  | ✔️          |               |
| Requester name (on-create only)                                                   | ✔️          |               |
| Status                                                                            | ✔️          | ✔️            |
| Tags (Labels)                                                                     | ✔️          |               |
| Ticket form                                                                       | ✔️          | ✔️            |
| Ticket form ID                                                                    | ✔️          | ✔️            |
| Title (Subject)                                                                   | ✔️          | ✔️            |
| Topic                                                                             | ✔️          | ✔️            |
| Type                                                                              | ✔️          | ✔️            |
| URL                                                                               | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Considerations <a href="#limitations-and-considerations" id="limitations-and-considerations"></a>

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Issue Types**: When Getint creates a new issue in Zendesk, it will always be one specific type (Ticket).
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author's name will appear in the comment footer, but the comment will be assigned to the connecting account.

Comments and attachments transferred from Zendesk to Jira can be set to either public, private, or skipped completely. You can configure your integration to enable both public and private visibility options simultaneously.

* **Change History**: Unfortunately, Getint cannot integrate the history of changes.
* **Inline** **Images** aren’t supported for the Description field.
* **On-create Only Fields**: These fields will only trigger when a new ticket is created in Zendesk. This means that if you add this field to your integration later or if you update an existing issue in Jira, it won’t be possible to retrieve the information from these fields.
* **Ticket Synchronization**: Keep in mind that when you start a new integration, all existing tickets in Zendesk will begin syncing with the connected tool, one by one. If you disable your previous integration and set up a new one, the syncing process will restart automatically, which may result in duplicate tickets.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
