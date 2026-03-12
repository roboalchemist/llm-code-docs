# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/notion.md

# Notion

## Getint: Simplifying Notion Integration and Data Synchronization

Getint simplifies the integration and synchronization of a wide range of tools. It supports various connectivity scenarios, including Notion - Jira, Notion - Asana, Notion - Monday, Notion - Azure DevOps, and more. Whether you need a software-as-a-service (SaaS) or an On-premise solution, Getint offers the flexibility to meet the unique requirements of different businesses.

### The article covers the following topics

* [How to Setup the App](#setting-up-getint-for-notion)
* [Supported Fields in Notion](#supported-fields-in-notion)
* [Limitations and Considerations to Keep in Mind](#limitations-to-keep-in-mind)
* [Case Studies and Contacting Our Support Team](#contacting-our-support-team-and-case-studies)

Getint ensures seamless data synchronization across platforms and instances, with specific support for Notion. Users can effectively monitor and manage tasks in diverse environments while seamlessly integrating with other platforms.

### Setting Up Getint for Notion

Getint simplifies data integration and migration. Follow these straightforward steps to connect your systems, such as Notion, map types (i.e., Task - Task), and fields (i.e., Description - Summary). Whether you’re syncing data or performing a continuous one-time migration, Getint has you covered. Our dedicated support team is ready to assist you with any setup or operational challenges.

For more detailed guides on setting up your Notion integration, refer to the following resources:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Notion with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-notion-integration)):

1. **Access Getint:** If you’re using Jira, navigate to the "Apps" section, search for new apps, and acquire the app from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1231784/notion-integration-for-jira?tab=overview\&hosting=cloud) Alternatively, if you need to integrate Notion with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://www.getint.io/contact)
2. **Token Generation for Notion:**
   * Open the "Notion" app.
   * Click on the "three dots" located in the top right corner.
   * Select "Add a Connection."
   * Navigate to "Manage Connections" and choose "Develop or Manage integrations."
   * Click on "New Integration."
   * Provide a name for your integration, grant the necessary permissions, and copy the "API token." This will be your password to create a connection.
3. **How to Establish a Connection with Notion:** Ensure you’re logged in as a user with the correct permissions. Click "Select App" and choose "Notion." Select "Create New" to establish a new connection with your Notion instance. Name your connection and add the "URL" of your Notion instance. Provide your login credentials to connect with Getint.
4. **Choose and Connect the Second App:** Select and link another tool to integrate with Notion—options include another Notion instance, ServiceNow, Jira, or any other supported tool.
5. **Mapping Types and Fields:** Link Notion types (Tasks) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically or set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team can provide guidance and assistance.

### Supported Fields in Notion

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synchronized apps, those changes will appear in the other app. However, updates made in the other app won’t impact the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synchronized fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While it’s technically not possible to directly modify read-only fields, we provide a solution for achieving bidirectional integration or migrating these fields using custom fields. Setting up this solution requires specific steps, but it is indeed feasible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Notion Field**                                                                                                     | **One Way** | **Both Ways** |
| -------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Comments & Attachments                                                                                               | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Checkbox - Date - Description - Estimates - Select - Status - Text - URL</strong></p> | ✔️          | ✔️            |
| Database Id                                                                                                          | ✔️          | ✔️            |
| Due (End Date)                                                                                                       | ✔️          | ✔️            |
| Due (Start Date)                                                                                                     | ✔️          | ✔️            |
| Item Type                                                                                                            | ✔️          |               |
| Priority                                                                                                             | ✔️          | ✔️            |
| Reason                                                                                                               | ✔️          | ✔️            |
| Status                                                                                                               | ✔️          | ✔️            |
| Summary                                                                                                              | ✔️          | ✔️            |
| Task name                                                                                                            | ✔️          | ✔️            |
| URL                                                                                                                  | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to Keep in Mind

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* At the time of publishing this article, we currently only support mapping Tasks for Notion, and Assignees are not supported.
* Comments added to the issue will display under the user account you select when creating the connection. For a seamless integration, we recommend creating a dedicated Service Account. Although the original author’s name will appear in the comment footer, the comment will still be linked to the account that established the connection.
* Unfortunately, integrating the history of changes is not possible due to the technical limitations of Jira / Notion APIs.

### Contacting Our Support Team & Case Studies

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
