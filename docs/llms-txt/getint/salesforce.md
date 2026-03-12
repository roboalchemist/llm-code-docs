# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/salesforce.md

# Salesforce

## Getint: Simplifying Salesforce Integration and Data Synchronization <a href="#getint-simplifying-salesforce-integration-and-data-synchronization" id="getint-simplifying-salesforce-integration-and-data-synchronization"></a>

Getint, a powerful integration solution, seamlessly connects and synchronizes various tools. It supports various connectivity scenarios, including Salesforce - Jira, Salesforce - Azure DevOps, and more. Whether you require Software-as-a-Service (SaaS) or On-Premise deployment, Getint provides the flexibility to meet the distinct needs of different businesses and companies.

### What does this article cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-salesforce)
* [Supported Fields in Salesforce](#supported-fields-in-salesforce)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

**Getint** facilitates smooth data synchronization across various platforms and instances. It supports Salesforce, allowing users to monitor and manage tasks in diverse environments effectively. Additionally, it enables seamless integration with other platforms.

### Setting Up Getint for Salesforce <a href="#setting-up-getint-for-salesforce" id="setting-up-getint-for-salesforce"></a>

Getint simplifies data integration and migration. You can connect your systems with easy setup steps, such as Salesforce, map types (i.e., Task - Case), and fields (i.e., Priority - Priority). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Salesforce integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Salesforce with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-salesforce-integration)):

1. **Access Getint:** Navigate through the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1231635/connector-for-salesforce-jira-salesforce-integration?hosting=cloud\&tab=overview), go to your "Apps" section in Jira, and search for the "Getint Salesforce integration" app. Alternatively, if you need to integrate Salesforce with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://app.getint.io/)
2. **Token Generation for Salesforce:** To connect with Salesforce, users must grant an "API token" to Getint via the "OAuth authentication" method within our app.
3. **Establishing a Connection with Salesforce:**
   * Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose "Salesforce."
   * Select "Create New" to establish a new connection with your Salesforce instance. Name your connection, and add the URL of your Salesforce instance.
   * Provide the login credentials. Click the "Authorize Getint" button.
   * You’ll be redirected to the Salesforce login page. Once authorized, a confirmation message will prompt you to click "Add" to create the connection. Click "Add."
   * Select the newly created connection and press "Connect."
4. **Choose and Connect the Second App:** You can select and link an additional tool to integrate with Salesforce. Options include another Salesforce instance, ServiceNow, Jira, or other supported tools.
5. **Map Types and Fields:** Link Salesforce types (Account, Case, and Contact) to synchronize with other tools. You can use the Quick Build feature, which allows you to map available fields automatically, or you can set them manually.

Getint’s support team is dedicated to delivering a seamless and efficient integration experience customized to your specific requirements. Should you encounter any inconveniences or need assistance with missing features, our committed support team is ready to provide guidance and help.

### Supported Fields in Salesforce <a href="#supported-fields-in-salesforce" id="supported-fields-in-salesforce"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Salesforce Field**                                                                             | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------------------------ | ----------- | ------------- |
| Case Number                                                                                      | ✔️          |               |
| Case Origin                                                                                      | ✔️          | ✔️            |
| Case Reason                                                                                      | ✔️          | ✔️            |
| Case Type                                                                                        | ✔️          | ✔️            |
| Company                                                                                          | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date/Time - Email - Number - Phone - Picklist - Text</strong></p> | ✔️          | ✔️            |
| Engineering Req Number                                                                           | ✔️          | ✔️            |
| Free Text                                                                                        | ✔️          | ✔️            |
| ID                                                                                               | ✔️          |               |
| Internal Comments                                                                                | ✔️          | ✔️            |
| Item Type                                                                                        | ✔️          |               |
| Name                                                                                             | ✔️          | ✔️            |
| Object Type                                                                                      | ✔️          |               |
| Phone                                                                                            | ✔️          | ✔️            |
| Potenial Liability                                                                               | ✔️          | ✔️            |
| Priority                                                                                         | ✔️          | ✔️            |
| Product                                                                                          | ✔️          | ✔️            |
| Single select                                                                                    | ✔️          | ✔️            |
| SLA Violation                                                                                    | ✔️          | ✔️            |
| Status                                                                                           | ✔️          | ✔️            |
| Subject                                                                                          | ✔️          | ✔️            |
| URL                                                                                              | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* When you add comments to an issue, they will be displayed under the user account you select to establish the connection. For smooth integration, it’s advisable to create a dedicated Service Account specifically for building your integration. Although the original author’s name will be visible in the comment footer, the comment itself will remain associated with the account that set up the connection.
* Unfortunately, incorporating the history of changes is not feasible at this time.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getintio.atlassian.net/servicedesk/customer/portals), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
