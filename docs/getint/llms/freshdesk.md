# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/freshdesk.md

# Freshdesk

## Getint: Streamlining Freshdesk Integration and Data Synchronization <a href="#getint-streamlining-freshdesk-integration-and-data-synchronization" id="getint-streamlining-freshdesk-integration-and-data-synchronization"></a>

Getint revolutionizes the integration and synchronization of various tools, including Freshdesk. It supports diverse connectivity scenarios such as Freshdesk-Jira, Freshdesk-Asana, Freshdesk-Monday, Freshdesk-Azure DevOps, and more. Whether you need a SaaS or On-premise solution, Getint offers the flexibility to meet the unique needs of different businesses.

### The Article Covers the Following Topics: <a href="#the-article-covers-the-following-topics" id="the-article-covers-the-following-topics"></a>

* [How to Set Up the App](#setting-up-getint-for-freshdesk)
* [Supported Fields for Freshdesk Integrations](#supported-fields-for-freshdesk-integrations)
* [Limitations and Considerations to Keep in Mind](#limitations-to-keep-in-mind)
* [Case Studies and Contacting Our Support Team](#case-studies-and-support-contact)

Getint ensures seamless data synchronization across platforms and instances, specifically supporting Freshdesk. Users can efficiently monitor and manage tasks in diverse environments while integrating seamlessly with other platforms.

### Setting Up Getint for Freshdesk <a href="#setting-up-getint-for-freshdesk" id="setting-up-getint-for-freshdesk"></a>

Getint simplifies data integration and migration. Follow these straightforward steps to connect your systems, such as Freshdesk, map types (i.e., Task - Incident), and fields (i.e., Description - Description). Whether you’re syncing data or performing a continuous one-time migration, Getint has you covered. Our dedicated support team is ready to assist you with any setup or operational challenges.

For more detailed guides on setting up your Freshdesk integration, refer to the following resources:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

#### Simplified Freshdesk Integration Process <a href="#simplified-freshdesk-integration-process" id="simplified-freshdesk-integration-process"></a>

Here's a simplified version of how to integrate Freshdesk with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-freshdesk)):

1. **Access Getint:** If you’re using Jira, navigate to the **Apps** section, search for new apps, and acquire the app from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1227929/freshdesk-freshservice-jira-works-behind-the-firewall?hosting=cloud\&tab=overview) Alternatively, if you need to integrate Freshdesk with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://www.getint.io/contact)
2. **Token Generation for Freshdesk:** Log in to your Freshdesk account, click on your profile picture in the top right corner, and select **Profile Settings.** In the sidebar on the right, locate the **View API key** button, click on it to access the API key, and complete the captcha verification when prompted. Copy the provided API key and paste it to authenticate your Getint integration.
3. **How to Establish a Connection with Freshdesk:** Ensure you’re logged in as a user with the correct permissions. Click **Select App** and choose **Freshdesk.** Select **Create New** to establish a new connection with your Freshdesk instance. Name your connection and add the **URL** of your Freshdesk instance. Provide your login credentials to connect with Getint.
4. **Choose and Connect the Second App:** Select and link another tool to integrate with Freshdesk—options include another Freshdesk instance, ServiceNow, Jira, or any other supported tool.
5. **Mapping Types and Fields:** Link **Freshdesk types** (Incidents) to synchronize with other tools. You can use the **Quick Build** feature, which allows you to map available fields automatically or set them manually.

Getint’s support team is committed to ensuring a smooth and efficient integration experience tailored to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team is here to help.

### Supported Fields for Freshdesk Integrations <a href="#supported-fields-for-freshdesk-integrations" id="supported-fields-for-freshdesk-integrations"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported fields for Freshdesk integrations:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synchronized apps, those changes will appear in the other app. However, updates made in the other app won’t impact the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synchronized fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While it’s technically not possible to directly modify read-only fields, we provide a solution for achieving bidirectional integration or migrating these fields using custom fields. Setting up this solution requires specific steps, but it is indeed feasible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Freshdesk Field**                                                                              | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------------------------ | ----------- | ------------- |
| Agent                                                                                            | ✔️          | ✔️            |
| Comments & Attachments                                                                           | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Dependent field - Dropdown - Single line text</strong></p> | ✔️          | ✔️            |
| Description                                                                                      | ✔️          | ✔️            |
| Group                                                                                            | ✔️          | ✔️            |
| Id                                                                                               | ✔️          |               |
| Priority                                                                                         | ✔️          | ✔️            |
| Requester                                                                                        | ✔️          | ✔️            |
| Status                                                                                           | ✔️          | ✔️            |
| Source                                                                                           | ✔️          | ✔️            |
| Subject                                                                                          | ✔️          | ✔️            |
| Type                                                                                             | ✔️          | ✔️            |
| URL                                                                                              | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to Keep in Mind

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* To ensure your integration functions correctly, you must map the following mandatory fields: Requester, Status (mapped with a fixed value “Open” for newly created tickets), and Priority. For detailed instructions on mapping these fields with platforms like Jira, please refer to the guide available [here.](https://docs.getint.io/guides/integration-synchronization/jira-freshdesk#field-mapping)
* Comments added to the issue will display under the user account you select when creating the connection. For a seamless integration, we recommend creating a dedicated Service Account. Although the original author’s name will appear in the comment footer, the comment will still be linked to the account that established the connection.
* Unfortunately, integrating the history of changes is not possible due to the technical limitations of Jira / Freshdesk APIs.

### Case Studies and Support Contact

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for data integration. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
