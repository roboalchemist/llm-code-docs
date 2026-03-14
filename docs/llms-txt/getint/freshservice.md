# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/freshservice.md

# Freshservice

## Getint: Connecting Freshservice and Synchronizing Data Across Platforms <a href="#getint-connecting-freshservice-and-synchronizing-data-across-platforms" id="getint-connecting-freshservice-and-synchronizing-data-across-platforms"></a>

Getint makes it easier to connect Freshservice with other tools and keep data aligned. It supports a wide range of setups, including Freshservice-Jira, Freshservice-Asana, Freshservice-Monday, Freshservice-Azure DevOps, and more. Whether you’re using a SaaS or On-Premise version, Getint offers flexible options to support different business needs.

### What’s Inside: <a href="#whats-inside" id="whats-inside"></a>

* [How to Set Up the App](#setting-up-getint-with-freshservice)
* [Supported Fields for Freshservice Connections](#supported-fields-for-freshservice-integrations)
* [Key Limitations and Setup Notes](#things-to-keep-in-mind)
* [Case Studies and How to Reach Support](#case-studies-and-support)

Getint helps teams keep data consistent across platforms and environments. With support for Freshservice, users can track and manage work across systems without losing visibility or control.

### Setting Up Getint with Freshservice <a href="#setting-up-getint-with-freshservice" id="setting-up-getint-with-freshservice"></a>

Connecting Freshservice to other tools through Getint is straightforward. You can sync data or run a one-time migration. The process includes mapping issue types (e.g., Task → Incident) and fields (e.g., Description → Description). If you need help during setup, our support team is available to guide you.

#### Helpful Resources: <a href="#helpful-resources" id="helpful-resources"></a>

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Instructions](https://docs.getint.io/guides/integration-synchronization/jira-freshservice-integration)
* [Migration Steps](https://docs.getint.io/guides/migration)
* [Workflow Overview](https://docs.getint.io/getintio-platform/workflows)

#### Freshservice Integration: Step-by-Step <a href="#freshservice-integration-step-by-step" id="freshservice-integration-step-by-step"></a>

Here’s a quick look at how to connect Freshservice with other platforms:

1. **Access Getint**: If you're using Jira, go to the Apps section and install Getint from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1227929/freshservice-freshdesk-integration-for-jira-2-way-work-sync?hosting=cloud\&tab=overview). For other platforms, choose either Getint SaaS or On-Premise, depending on your setup.
2. **Generate Your Freshservice API Token**: Log in to [Freshservice](https://docs.getint.io/guides/quickstart/connection#freshservice), click your profile icon in the top-right corner, and go to Profile Settings. On the right sidebar, click "View API Key," complete the captcha, and copy the key. You'll use this to connect Freshservice to Getint.
3. **Create the Connection**: Make sure you’re logged in with the right permissions. In Getint, click "Select App" and choose Freshservice. Then click "Create New" to start a new connection. Add your Freshservice URL, enter your credentials, and save the connection.
4. **Link a Second Tool**: Choose another platform to connect with Freshservice—this could be another Freshservice instance, Jira, ServiceNow, or any other supported tool.
5. **Map Types and Fields**: Use Getint's Quick Build feature to automatically map Freshservice fields, or configure them manually. You can link incident types and sync fields like status, priority, and description.

If you run into any issues or need help with setup, our support team is ready to assist.

### Supported Fields for Freshservice Integrations <a href="#supported-fields-for-freshservice-integrations" id="supported-fields-for-freshservice-integrations"></a>

Getint lets you map fields between Freshservice and other platforms. Here’s how it works:

#### Field Mapping Options: <a href="#field-mapping-options" id="field-mapping-options"></a>

* **One-Way Mapping**: Changes made in one app appear in the other, but not the reverse.
* **Two-Way Mapping**: Updates are reflected in both apps automatically.

{% hint style="info" %}
Tip: Read-only fields can’t be edited directly, but Getint offers a way to sync or migrate them using custom fields. Setup steps are available in our guides.
{% endhint %}

| **Freshservice Field**                                                         | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------ | ----------- | ------------- |
| Assigned to                                                                    | ✔️          | ✔️            |
| Category                                                                       | ✔️          | ✔️            |
| Comments & Attachments                                                         | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Dropdown - Single line text</strong></p> | ✔️          | ✔️            |
| Department                                                                     | ✔️          | ✔️            |
| Description                                                                    | ✔️          | ✔️            |
| Group                                                                          | ✔️          | ✔️            |
| Id                                                                             | ✔️          |               |
| Item                                                                           | ✔️          | ✔️            |
| Priority                                                                       | ✔️          | ✔️            |
| Requester                                                                      | ✔️          | ✔️            |
| Status                                                                         | ✔️          | ✔️            |
| Source                                                                         | ✔️          | ✔️            |
| Status                                                                         | ✔️          | ✔️            |
| Subject                                                                        | ✔️          | ✔️            |
| Sub-category                                                                   | ✔️          | ✔️            |
| Time Tracking - Original Estimate                                              | ✔️          | ✔️            |
| Time tracking date field                                                       | ✔️          | ✔️            |
| Type                                                                           | ✔️          | ✔️            |
| URL                                                                            | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Things to Keep in Mind

While Getint supports many features, here are a few important notes:

* **Required Fields**: You must map Requester, Status (set to "Open" for new tickets), and Priority for the integration to work properly. More information about field mappings [here](https://docs.getint.io/guides/integration-synchronization/jira-freshservice-integration#id-7.-field-mapping).
* **Comment Attribution**: Comments will appear under the account selected during setup. For best results, we recommend using a dedicated Service Account. The original author's name will still show in the comment footer.
* **Change History**: Syncing historical changes isn't supported due to API limitations in Jira and Freshservice.

### Case Studies and Support

Our team is here to help you get started, troubleshoot issues, and answer any questions. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Real-World Examples

Companies of all sizes use Getint to connect their tools and manage data more effectively. Check out our [Case Studies](https://www.getint.io/case-studies) to see how others have used Getint in different environments.

{% hint style="info" %}
**Need something specific that's not currently supported?**

Please contact our [support team](https://getint.io/help-center), and we will assist you in developing a customized solution to your specific needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
