# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/airtable.md

# Airtable

## Getint: Simplifying Airtable Integration and Data Synchronization <a href="#getint-simplifying-airtable-integration-and-data-synchronization" id="getint-simplifying-airtable-integration-and-data-synchronization"></a>

Getint facilitates seamless integration between multiple platforms, enabling synchronization across tools like Airtable, Jira, Asana, and Azure DevOps. It supports both SaaS and On-Premise deployment, offering adaptability to suit diverse business requirements.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Installing and Configuring the Application](#installing-and-configuring-getint-for-airtable)
* [Supported Airtable Fields](#supported-airtable-fields)
* [Key Considerations](#key-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

By synchronizing data across instances and platforms, Getint empowers users to efficiently track and manage tasks while integrating Airtable with other project management tools.

### Installing and Configuring Getint for Airtable <a href="#installing-and-configuring-getint-for-airtable" id="installing-and-configuring-getint-for-airtable"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* **Want to integrate Jira with Airtable?** Just download the app from the Atlassian Marketplace. It’s quick and easy! You can find it here: [Airtable Integration for Jira.](https://marketplace.atlassian.com/apps/1231789/airtable-integration-for-jira-airtable-connector?hosting=cloud\&tab=overview)
* Other tools: Select between [Getint On-Premise or SaaS options.](https://app.getint.io/app/auth/sign-up)

**Step 2: Set Up a Connection with Airtable**

* Ensure you have the correct access permissions. Here you will find all the steps to generate an access token in Airtable: [Generating an Airtable Token.](https://docs.getint.io/guides/quickstart/connection#airtable)
* Choose Airtable as the app, create a new connection, and enter your Airtable access token.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with Airtable, such as Jira.

**Step 4: Map Types and Fields**

* Match Airtable issue types, such as Tasks, with their equivalents in the other tool.
* Leverage the Quick Build feature for automatic mapping, or adjust mappings manually to fit your needs.

If you need help with setup or run into any challenges, our support team is always here to assist.

For additional guidance on using Getint with Airtable, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira Airtable Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-airtable-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Airtable Fields <a href="#supported-airtable-fields" id="supported-airtable-fields"></a>

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

| **Airtable Field**                                                                                         | **One Way**                                                                                                                                                                          | **Both Ways**                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Attachments                                                                                                | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> |
| Comments                                                                                                   | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| <p>Custom Fields</p><p><strong>Long Text - Rich Text Field -Single Line Text - Single Select</strong> </p> | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| ID                                                                                                         | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Item Type                                                                                                  | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Last modified time                                                                                         | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Name                                                                                                       | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Notes                                                                                                      | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Record API URL                                                                                             | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Status                                                                                                     | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| URL                                                                                                        | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |

{% hint style="danger" %}
**Important Note:** While we make every effort to ensure the accuracy of this list, please be aware that supported fields may differ in the original product.
{% endhint %}

### Key Considerations <a href="#key-considerations" id="key-considerations"></a>

At Getint, we are committed to continuously updating our supported features, fields, and compatible apps. However, please keep the following key points in mind:

* **Attachments** aren't supported.
* **Change History**: Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account. Also, comments and attachments transferred from Airtable to Jira will be set to public or private (they will be public by default). You can configure Jira to mark all comments from Airtable as private automatically. However, enabling both public and private visibility options is impossible.
* **Rich text** formatting is supported for text fields.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is here to assist with your integration and migration needs. Whether you have questions or seek deeper insights into our solution, you’re welcome to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Discover how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) highlight real-world solutions designed to empower teams and organizations.

{% hint style="info" %}
**Looking for a solution we don’t currently support?** Reach out to our [support team](https://getint.io/help-center); we’d be happy to help you explore a customized solution tailored to your needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
