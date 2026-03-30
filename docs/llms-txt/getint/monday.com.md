# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/monday.com.md

# Monday.com

## Getint: Simplifying Monday.com Integration and Data Synchronization <a href="#getint-simplifying-monday.com-integration-and-data-synchronization" id="getint-simplifying-monday.com-integration-and-data-synchronization"></a>

Getint, a powerful integration solution, seamlessly connects and synchronizes various tools. It supports multiple connectivity scenarios, including Jira - Monday.com, Monday.com - Azure DevOps, Monday.com - Asana, and more. Whether you choose Software-as-a-Service (SaaS) or On-Premise deployment, Getint provides the flexibility to meet the distinct needs of different businesses.

### What does this article cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-monday.com)
* [Supported Fields in Monday.com](#supported-fields-in-monday.com)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

**Getint** facilitates smooth data synchronization across various platforms and instances. It supports **Monday.com,** allowing users to monitor and manage tasks in diverse environments effectively. Additionally, it enables seamless integration with other platforms.

### Setting up Getint for Monday.com <a href="#setting-up-getint-for-monday.com" id="setting-up-getint-for-monday.com"></a>

Getint simplifies data integration and migration. You can connect your systems with easy setup steps, such as Monday.com, map types (i.e., Task - Item), and fields (i.e., Assignee - Responsable). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to configure your Monday.com integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Monday.com with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-monday.com-integration)):

1. **Access Getint:** Navigate through the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1225780/monday-com-integration-for-jira-monday-com-connector?hosting=cloud\&tab=overview) or go to your "Apps" section in Jira, and search for the "Getint Monday.com integration app." Alternatively, if you need to integrate Monday.com with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://app.getint.io/)
2. **Token Generation for Monday.com:** There are two options to see your API token:
   1. **Admin Tab:**
      * Log in to your "Monday.com" account.
      * Click your "avatar/profile picture" in the top right corner.
      * Go to **Administration** > **Connections** > **API.**
      * Copy your personal token.
   2. **Developer Tab:**
      * Log in to your "Monday.com" account.
      * Click your profile picture in the top right corner.
      * Visit "Developers" to open the Developer Center.
      * Click **My Access Tokens** > **Show.**
      * Copy your personal token.
3. **Establish a Connection with Monday.com:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose "Monday.com." Select "Create New" to establish a new connection with your Monday.com instance. Name your connection, and add the URL of your Monday.com instance. Provide the login credentials.
4. **Choose and Connect the Second App:** You can select and link an additional tool to integrate with Monday.com. Options include another Monday.com instance, ServiceNow, Jira, or any other supported tool.
5. **Map Types and Fields:** Link "Monday.com types" (Items, SubItems) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is dedicated to delivering a seamless and efficient integration experience tailored to your specific requirements. Should you encounter any setup challenges or need assistance with missing features, our committed support team is ready to provide guidance and help.

### Supported Fields in Monday.com <a href="#supported-fields-in-monday.com" id="supported-fields-in-monday.com"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **Field Mappings Explained:** <a href="#field-mappings-explained" id="field-mappings-explained"></a>

**One-Way Mapping:**

* When you update fields in one of the synchronized apps, those changes will appear in the other app.
* However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps.
* If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While it’s technically not possible to directly modify read-only fields, we offer a solution for achieving bidirectional integration or migrating these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Monday.com Field**                                                                                                            | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Comments & Attachments                                                                                                          | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Dropdown - Label - People - Priority - Status - Text - Timeline Start Date/End Date</strong></p> | ✔️          | ✔️            |
| Date                                                                                                                            | ✔️          | ✔️            |
| Group                                                                                                                           | ✔️          | ✔️            |
| ID                                                                                                                              | ✔️          |               |
| Person                                                                                                                          | ✔️          | ✔️            |
| Status                                                                                                                          | ✔️          | ✔️            |
| Title (Name)                                                                                                                    | ✔️          | ✔️            |
| URL                                                                                                                             | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* When you add comments to an issue, they will be displayed under the user account you select to establish the connection. For smooth integration, it’s advisable to create a dedicated Service Account specifically for building your integration. Although the original author’s name will be visible in the comment footer, the comment itself will remain associated with the account that set up the connection.
* Unfortunately, incorporating the history of changes is not feasible at this time.
* Attachments need to be uploaded from the **Files** column in your Monday.com project, not from the **Files** section within the tasks. Otherwise, your attachments will not trigger syncs to the other app you integrate.
* Updates to existing comments will not trigger syncs. Subcomments do not trigger syncs as well.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
