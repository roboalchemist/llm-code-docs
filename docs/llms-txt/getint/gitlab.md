# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/gitlab.md

# GitLab

## Getint: Simplifying GitLab Integration and Data Synchronization <a href="#getint-simplifying-gitlab-integration-and-data-synchronization" id="getint-simplifying-gitlab-integration-and-data-synchronization"></a>

**Getint** is designed to connect and synchronize various tools, supporting integrations such as GitLab with Jira, Asana, or Azure DevOps. It offers both SaaS and On-Premise solutions, providing flexibility for different business needs.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Setting Up the App](#how-to-set-up-getint-for-gitlab)
* [Supported Fields in GitLab](#supported-fields-for-gitlab-integration)
* [Supported Item Types](#supported-fields-for-gitlab-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

Getint helps synchronize data across platforms or instances, including GitLab. It enables users to monitor and manage tasks or activities across projects and integrate GitLab with other tools.

### How to Set Up Getint for GitLab <a href="#how-to-set-up-getint-for-gitlab" id="how-to-set-up-getint-for-gitlab"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* **Want to integrate Jira with GitLab?** Just download the app from the Atlassian Marketplace. It's quick and easy! You can find it here: [GitLab Integration for Jira.](https://marketplace.atlassian.com/apps/1223999/gitlab-integration-for-jira-gitlab-connector-2-way-sync?hosting=cloud\&tab=overview)
* Other tools: Select between Getint On-Premise or SaaS options.

**Step 2: Set Up a Connection with GitLab**

* Ensure you have the correct access permissions. Here you will find all the steps to generate an access token in GitLab: [Generating a GitLab Token.](https://docs.getint.io/guides/quickstart/connection#gitlab)
* Choose GitLab as the app, create a new connection, and enter your GitLab access token.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with GitLab, such as Jira.

**Step 4: Map Types and Fields**

* Match GitLab issue types, such as Incidents, with their equivalents in the other tool.
* Leverage the Quick Build feature for automatic mapping, or adjust mappings manually to fit your needs.

If you need help with setup or run into any challenges, our support team is always here to assist.

For additional guidance on using Getint with GitLab, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira GitLab Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-gitlab)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for GitLab Integration <a href="#supported-fields-for-gitlab-integration" id="supported-fields-for-gitlab-integration"></a>

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

| **GitLab Field**  | **One Way** | **Both Ways** |
| ----------------- | ----------- | ------------- |
| Assignee          | ✔️          | ✔️            |
| Attachments       | ✔️          |               |
| Author Name       | ✔️          |               |
| Closed At         | ✔️          |               |
| Comments          | ✔️          | ✔️            |
| Confidential      | ✔️          |               |
| Created At        | ✔️          |               |
| Discussion Locked | ✔️          |               |
| Due date          | ✔️          | ✔️️           |
| Epic Id           | ✔️          |               |
| Epic Name         | ✔️          |               |
| ID                | ✔️          |               |
| Labels            | ✔️          | ✔️            |
| Milestone Name    | ✔️          |               |
| Reporter          | ✔️          |               |
| Status            | ✔️          | ✔️            |
| Time Estimate     | ✔️          |               |
| Time Spent        | ✔️          |               |
| Title             | ✔️          |               |
| Updated At        | ✔️          |               |
| URL               | ✔️          |               |
| Weight            | ✔️          |               |

{% hint style="warning" %}
**Important Note:** While we make every effort to ensure the accuracy of this list, please be aware that supported fields may differ in the original product.
{% endhint %}

### Limitations and Considerations <a href="#limitations-and-considerations" id="limitations-and-considerations"></a>

At Getint, we are committed to continuously updating our supported features, fields, and compatible apps. However, please keep the following key points in mind:

* **Attachments**: You can sync attachments from GitLab to Jira with a cookie header. These attachments will always sync one way from GitLab to the counterpart tool. More information about this option here: [Attachments Sync in GitLab Integration.](https://docs.getint.io/guides/integration-synchronization/jira-gitlab/attachments-sync-in-gitlab-integration)
* **Change History**: Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account. Also, comments and attachments transferred from GitLab to Jira will be set to public or private (they will be public by default). You can configure Jira to mark all comments from GitLab as private automatically. However, enabling both public and private visibility options is impossible.
* **Custom fields**: Currently, GitLab has no support for custom fields.
* **Inline** **images** aren’t supported.
* **Issue Types**: When Getint creates a new issue in GitLab, it will always be one specific type (i.e., Issue, or Incident). You can set the default item type using a rule or manually adjust it in GitLab after creation.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is here to assist with your integration and migration needs. Whether you have questions or seek deeper insights into our solution, you’re welcome to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Discover how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) highlight real-world solutions designed to empower teams and organizations.

{% hint style="info" %}
**Looking for a solution we don’t currently support?** Reach out to our [support team](https://getint.io/help-center)—we’d be happy to help you explore a customized solution tailored to your needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
