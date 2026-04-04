# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/github.md

# GitHub

## Getint: Simplifying GitHub Integration and Data Synchronization <a href="#getint-simplifying-github-integration-and-data-synchronization" id="getint-simplifying-github-integration-and-data-synchronization"></a>

Getint facilitates seamless integration between multiple platforms, enabling synchronization across tools like GitHub, Jira, Asana, and Azure DevOps. It supports both SaaS and On-Premise deployment, offering adaptability to suit diverse business requirements.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Installing and Configuring the Application](#installing-and-configuring-getint-for-github)
* [Supported GitHub Fields](#supported-github-fields)
* [Key Considerations](#key-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

By synchronizing data across instances and platforms, Getint empowers users to efficiently track and manage tasks while integrating GitHub with other project management tools.

### Installing and Configuring Getint for GitHub <a href="#installing-and-configuring-getint-for-github" id="installing-and-configuring-getint-for-github"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* **Want to integrate Jira with GitHub?** Just download the app from the Atlassian Marketplace. It's quick and easy! You can find it here: [GitHub Integration for Jira.](https://marketplace.atlassian.com/apps/1223933/github-integration-for-jira-github-connector?hosting=cloud\&tab=overview)
* Other tools: Select between [Getint On-Premise or SaaS options.](https://app.getint.io/app/auth/sign-up)

**Step 2: Set Up a Connection with GitHub**

* Ensure you have the correct access permissions. Here you will find all the steps to generate an access token in GitHub: [Generating a GitHub Token.](https://docs.getint.io/guides/quickstart/connection#github)
* Choose GitHub as the app, create a new connection, and enter your GitHub access token.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with GitHub, such as Jira.

**Step 4: Map Types and Fields**

* Match GitHub issue types, such as Tasks, with their equivalents in the other tool.
* Leverage the Quick Build feature for automatic mapping, or adjust mappings manually to fit your needs.

If you need help with setup or run into any challenges, our support team is always here to assist.

For additional guidance on using Getint with GitHub, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira GitHub Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-github-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Setting Up a Git Repository Integration <a href="#setting-up-a-git-repository-integration" id="setting-up-a-git-repository-integration"></a>

#### **Configuration Steps**

1. **Create a Git Connector Integration**: Navigate to the Getint dashboard and select Git Connector. Choose GitHub as your app.
2. **Authenticate with GitHub**: Generate an [access token](https://docs.getint.io/guides/quickstart/connection#github). Grant access to the repositories you want to sync.
3. **Set up OAuth for Jira**: Unlike Continuous Syncs or data Migrations, Git integrations need OAuth setup directly within your Jira environment. Follow the steps outlined in our guide: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
4. **Select Repositories**: Choose one or more GitHub repositories to link with Getint. You can sync issues, pull requests, and commits.
5. **Test & Activate**: Run a test sync to verify everything works as expected. Once confirmed, activate the integration.
6. **Sync Your Branches**: Use the correct prefixes outlined in our [Git Integration](https://docs.getint.io/guides/integration-synchronization/git-integrations/git-connector-github#id-5.-test-the-integration-and-sync-your-branches) article to sync the branches, commits, and pull requests.

{% hint style="info" %}
All the installation steps to connect your Git Repository with Jira are located in our dedicated article: [Git Connector - GitHub](https://docs.getint.io/guides/integration-synchronization/git-integrations/git-connector-github).
{% endhint %}

### Supported GitHub Fields <a href="#supported-github-fields" id="supported-github-fields"></a>

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

| **GitHub Field** | **One Way**                                                                                                                                                                          | **Both Ways**                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Assignee         | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Author           | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Comments         | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Description      | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| ID               | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Labels           | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> |
| Title            | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |

{% hint style="warning" %}
**Important Note:** While we make every effort to ensure the accuracy of this list, please be aware that supported fields may differ in the original product.
{% endhint %}

### Key Considerations

At Getint, we are committed to continuously updating our supported features, fields, and compatible apps. However, please keep the following key points in mind:

* **Attachments**: You can sync attachments from GitHub to Jira by providing S3 credentials.
* **Change History**: Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account. Also, comments and attachments transferred from GitHub to Jira will be set to public or private (they will be public by default). You can configure Jira to mark all comments from GitHub as private automatically. However, enabling both public and private visibility options is impossible.
* **Custom fields**: Currently, there's no support for custom fields.
* **Inline** **images** aren't supported.
* **Labels** aren't supported.

### Contacting Our Support Team

Our dedicated Support Team is here to assist with your integration and migration needs. Whether you have questions or seek deeper insights into our solution, you’re welcome to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Discover how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) highlight real-world solutions designed to empower teams and organizations.

{% hint style="info" %}
**Looking for a solution we don’t currently support?** Reach out to our [support team](https://getint.io/help-center); we’d be happy to help you explore a customized solution tailored to your needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
