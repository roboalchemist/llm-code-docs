# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/asana.md

# Asana

## Getint: Simplifying Asana Integration and Data Synchronization <a href="#getint-simplifying-asana-integration-and-data-synchronization" id="getint-simplifying-asana-integration-and-data-synchronization"></a>

Getint is expertly designed to integrate and synchronize an extensive range of tools. It accommodates a variety of connectivity scenarios, such as Asana - Jira, Asana - Asana, Asana - Monday, Asana - Azure DevOps, and more. With its availability as both a Software-as-a-Service (SaaS) and On-Premise solution, Getint offers the versatility to meet the unique requirements of various businesses.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [How to Set Up the App](#what-does-this-article-cover)
* [Supported Fields in Asana](#setting-up-getint-for-asana)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

Getint enables seamless data synchronization within the same platform, different platforms/different instances. It supports Asana across different projects. This allows users to efficiently track and manage Asana tasks and subtasks in diverse environments as well as integrate Asana with other platforms.

### Setting Up Getint for Asana <a href="#setting-up-getint-for-asana" id="setting-up-getint-for-asana"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as Asana, map types (i.e. Task - Task), and fields (i.e. Assignee - Assignee). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Asana integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Asana with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-asana-integration)):

1. **Access Getint:**
   * If you’re using Jira, go to "Apps," "Find new apps," and get the app from the Atlassian Marketplace.
   * If you want to integrate Asana with any other, non-Jira application, opt for the [Getint On-Premise or Getint SaaS](https://app.getint.io/).
2. **Token Generation for Asana:** Visit your Asana Settings. Go to the "Apps" section and launch the developer console. Now, click "Create new token" in the developer console under "Personal access token." This will serve as the password to create your connection.
3. **Establish a Connection with Asana:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose Asana. Select "Create New" to establish a new connection with your Asana instance. Name your connection, and add the URL of your Asana instance (without "/" at the end). Provide the login credentials.
4. **Choose and Connect the Second App:** Choose and connect another tool you'd like to integrate with Asana—either another Asana instance, DevOps, Jira, or any other tool that we support.
5. **Map Types and Fields:** Link Asana types (Task, Subtasks) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team is readily available to provide guidance and help.

### Supported Fields in Asana <a href="#supported-fields-in-asana" id="supported-fields-in-asana"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Asana Field**                                                                                 | **One Way** | **Both Ways** |
| ----------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Assignee                                                                                        | ✔️          | ✔️            |
| Attachments                                                                                     | ✔️          | ✔️            |
| Created                                                                                         | ✔️          |               |
| Comments                                                                                        | ✔️          | ✔️            |
| Completed                                                                                       | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Single-select - Date - Text - Number - Formula - ID</strong></p> | ✔️          | ✔️            |
| Description (Notes)                                                                             | ✔️          | ✔️            |
| Estimated time                                                                                  | ✔️          | ✔️            |
| ID                                                                                              | ✔️          |               |
| Priority                                                                                        | ✔️          | ✔️            |
| Reporter                                                                                        | ✔️          | ✔️            |
| Section                                                                                         | ✔️          | ✔️            |
| Start date                                                                                      | ✔️          | ✔️            |
| Status                                                                                          | ✔️          | ✔️            |
| Subtasks                                                                                        | ✔️          | ✔️            |
| Tags                                                                                            | ✔️          | ✔️            |
| Title (Name)                                                                                    | ✔️          | ✔️            |
| URL                                                                                             | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered

At Getint, we’re constantly updating our supported features, fields, and compatible apps. However, there are a few limitations you should be aware of:

* When a new issue is created in Asana by Getint, it will always be one type of issue, whether that's a Task or a Subtask. You can set the default item type using a rule or manually change it in Asana after it's created.
* Comments will be added as the user you choose to create the connection. Therefore, it is advised to create a dedicated Service Account to build your integration. The original author will appear in the comment footer; however, it will still be assigned to the account that established the connection.
* The history of changes can't be integrated.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
