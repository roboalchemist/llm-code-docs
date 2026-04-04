# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/servicenow.md

# ServiceNow

## Getint: Simplifying ServiceNow Integration and Data Synchronization <a href="#getint-simplifying-servicenow-integration-and-data-synchronization" id="getint-simplifying-servicenow-integration-and-data-synchronization"></a>

Getint is expertly designed to seamlessly integrate and synchronize a wide range of tools. It supports various connectivity scenarios, including ServiceNow - Jira, ServiceNow - Asana, ServiceNow - Azure DevOps, and ServiceNow - Zendesk. Whether you choose the Software-as-a-Service (SaaS) or On-Premise solution, Getint offers the flexibility to meet diverse business requirements.

### Key Points Covered in the Article: <a href="#key-points-covered-in-the-article" id="key-points-covered-in-the-article"></a>

* [Setting Up the App](#how-to-setup-getint-for-servicenow)
* [Supported Fields in ServiceNow](#supported-fields-for-servicenow-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Our Support Team - Case studies](#contacting-our-support-team)

Getint enables seamless data synchronization within the same platform, different platforms/different instances. It supports ServiceNow across different projects. This allows users to efficiently track and manage ServiceNow tasks/incidents in diverse environments as well as integrate ServiceNow with other platforms.

### How to Set Up Getint for ServiceNow <a href="#how-to-setup-getint-for-servicenow" id="how-to-setup-getint-for-servicenow"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as ServiceNow, map types (i.e., Task - Incident), and fields (i.e., Assignee - Assigned to). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your ServiceNow integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate ServiceNow with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration)):

1. **Accessing Getint:**
   * If you're using Jira, find the app in the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223935/servicenow-integration-for-jira-servicenow-connector?hosting=cloud\&tab=overview).
   * For non-Jira applications, choose between [Getint On-Premise or Getint SaaS](https://app.getint.io/).
2. **Establish a Connection with ServiceNow:**
   * Log in with the correct permissions.
   * Select ServiceNow as the app, create a new connection, and provide the instance URL and login credentials.
3. **Choose and Connect the Second App:**
   * Choose another tool (i.e., DevOps, Jira) to integrate with ServiceNow.
4. **Map Types and Fields:**
   * Link ServiceNow types (e.g., Incidents, Tasks) to synchronize with other tools.
   * Use the "Quick Build" feature or set mappings manually.

Getint's support team ensures a smooth integration experience customized to your needs. If you encounter challenges or need assistance, we're here to help!

### Supported Fields for ServiceNow Integration <a href="#supported-fields-for-servicenow-integration" id="supported-fields-for-servicenow-integration"></a>

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

| **ServiceNow Field**                                                                                      | **One Way** | **Both Ways** |
| --------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Actual end                                                                                                | ✔️          | ✔️            |
| Actual start                                                                                              | ✔️          | ✔️            |
| Approval                                                                                                  | ✔️          | ✔️            |
| Approval set                                                                                              | ✔️          | ✔️            |
| Assigned to (Assignees)                                                                                   | ✔️          | ✔️            |
| Assignment group                                                                                          | ✔️          | ✔️            |
| Attachments                                                                                               | ✔️          | ✔️            |
| Business impact                                                                                           | ✔️          | ✔️            |
| Business resolve time                                                                                     | ✔️          |               |
| Caller                                                                                                    | ✔️          | ✔️            |
| Category                                                                                                  | ✔️          | ✔️            |
| Child Incidents                                                                                           | ✔️          | ✔️            |
| Close code                                                                                                | ✔️          | ✔️            |
| Close notes                                                                                               | ✔️          | ✔️            |
| Closed                                                                                                    | ✔️          | ✔️            |
| Closed by                                                                                                 | ✔️          | ✔️            |
| Configuration item                                                                                        | ✔️          | ✔️            |
| Contact type                                                                                              | ✔️          | ✔️            |
| Correlation display                                                                                       | ✔️          | ✔️            |
| Correlation ID                                                                                            | ✔️          | ✔️            |
| Created                                                                                                   | ✔️          |               |
| Created by                                                                                                | ✔️          | ✔️            |
| Comments                                                                                                  | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Dropdown fields - Text fields - Reference fields - URL</strong></p> | ✔️          | ✔️            |
| Description                                                                                               | ✔️          | ✔️            |
| Due date                                                                                                  | ✔️          | ✔️            |
| Effective number                                                                                          | ✔️          |               |
| Escalation                                                                                                | ✔️          |               |
| Expected start                                                                                            | ✔️          | ✔️            |
| Follow up                                                                                                 | ✔️          | ✔️            |
| Id                                                                                                        | ✔️          |               |
| Impact                                                                                                    | ✔️          | ✔️            |
| Incident state                                                                                            | ✔️          | ✔️            |
| Last reopened at                                                                                          | ✔️          |               |
| Last reopened by                                                                                          | ✔️          |               |
| Location                                                                                                  | ✔️          | ✔️            |
| Notify                                                                                                    | ✔️          | ✔️            |
| Number                                                                                                    | ✔️          | ✔️            |
| On hold reason                                                                                            | ✔️          | ✔️            |
| Opened                                                                                                    | ✔️          | ✔️            |
| Opened by                                                                                                 | ✔️          | ✔️            |
| Order                                                                                                     | ✔️          | ✔️            |
| Priority                                                                                                  | ✔️          | ✔️            |
| Probable cause                                                                                            | ✔️          | ✔️            |
| Reassignment count                                                                                        | ✔️          | ✔️            |
| Reopen count                                                                                              | ✔️          | ✔️            |
| Resolve time                                                                                              | ✔️          |               |
| Resolved                                                                                                  | ✔️          | ✔️            |
| Resolved by                                                                                               | ✔️          | ✔️            |
| Service                                                                                                   | ✔️          | ✔️            |
| Severity                                                                                                  | ✔️          | ✔️            |
| Short description                                                                                         | ✔️          | ✔️            |
| State (Status)                                                                                            | ✔️          | ✔️            |
| Subcategory                                                                                               | ✔️          | ✔️            |
| Subtasks                                                                                                  | ✔️          | ✔️            |
| Task type                                                                                                 | ✔️          | ✔️            |
| Transfer reason                                                                                           | ✔️          |               |
| Updated                                                                                                   | ✔️          |               |
| Updated by                                                                                                | ✔️          | ✔️            |
| Updates                                                                                                   | ✔️          | ✔️            |
| Upon approval                                                                                             | ✔️          | ✔️            |
| Upon reject                                                                                               | ✔️          | ✔️            |
| Urgency                                                                                                   | ✔️          | ✔️            |
| URL                                                                                                       | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Considerations

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Issue Types:** When Getint creates a new issue in ServiceNow, it will always be one specific type (e.g., Task or Incident). You can set the default item type using a rule or manually adjust it in ServiceNow after creation.
* **Comments:** Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author's name will appear in the comment footer, but the comment will be assigned to the connecting account.
* **Change History:** Unfortunately, Getint cannot integrate the history of changes.
* **Private Tasks:** While Getint allows the creation of private tasks in ServiceNow, setting them up on boards is not supported.

### Contacting Our Support Team

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
