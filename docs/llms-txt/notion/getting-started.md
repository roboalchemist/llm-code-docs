# Source: https://developers.notion.com/docs/getting-started.md

# Notion API Overview

Discover how to leverage Notion's Public API to build integrations.

## Using Notion's API for Integrations

A Notion workspace is a collaborative environment where teams can organize work, manage projects, and store information in a highly customizable way. Notion's REST API facilitates direct interactions with workspace elements through programming. Key functionalities include:

- [Pages](https://developers.notion.com/docs/working-with-page-content): Create, update, and retrieve page content.
- [Databases](https://developers.notion.com/docs/working-with-databases) and [Data Sources](/reference/data-sources): Manage databases, data source properties, entries, and schemas.
- [Users](https://developers.notion.com/reference/user): Access user profiles and permissions.
- [Comments](https://developers.notion.com/docs/working-with-comments): Handle page and inline comments.
- [Content Queries](https://developers.notion.com/reference/post-search): Search through workspace content.
- [Authentication](https://developers.notion.com/docs/authorization): Secure integrations with OAuth 2.0.
- [Link Previews](https://developers.notion.com/docs/link-previews): Customize how links appear when shared.

To make interactions within Notion workspaces programmatically, you must associate these actions with a Notion user. Notion facilitates this by allowing API requests to be linked to a "bot" user.

Developers create integrations to define a bot's capabilities, including authenticating API requests, deciding when to make requests, and setting the bot's read/write permissions. Essentially, using Notion's Public API involves creating an integration that outlines how a bot interacts with your workspace and assigns REST API requests to the bot.

There are two primary integration types:

- [Internal](https://developers.notion.com/docs/getting-started#internal-integrations): For private workspace workflows and automations.
- [Public](https://developers.notion.com/docs/getting-started#public-integrations): For broader, shareable functionalities, including [Link Previews](https://developers.notion.com/docs/link-previews).

For further details on integration possibilities and API specifics, proceed with the guide or consult the [API reference](https://developers.notion.com/reference/intro). Check out our [demos](https://developers.notion.com/page/examples) for practical examples.

## What is a Notion Integration?

A Notion integration, sometimes referred as a [connection](https://www.notion.so/help/add-and-manage-connections-with-the-api), enables developers to programmatically interact with Notion workspaces. These integrations facilitate linking Notion workspace data with other applications or the automation of workflows within Notion.

Integrations are installed in Notion workspaces and require **explicit permission** from users to access Notion pages and databases.

![Create Notion integrations that unlock new possibilities for teams.](https://files.readme.io/0f06356-notion_overview.jpg)

Notion users have access to a vast [library](https://www.notion.so/integrations/all) of existing integrations to enrich their experience further. For developers interested in creating custom solutions, Notion supports the development of both internal and public integrations. Both utilize the Notion API for workspace interactions.

Let's explore internal and public integrations.

## Internal vs. Public Integrations

Notion integrations come in two types: Internal and Public. Understanding the differences between them helps in choosing the right approach for your development needs.

- **Internal Integrations** are exclusive to a single workspace, accessible only to its members. They are ideal for custom workspace automations and workflows.
- **Public Integrations** are designed for a wider audience, usable across any Notion workspace. They cater to broad use cases and follow the OAuth 2.0 protocol for workspace access.

> Public integrations must undergo a Notion security review before publishing.

### Key Differences

| Feature           | Internal Integrations                                            | Public Integrations                                             |
|-------------------|------------------------------------------------------------------|---------------------------------------------------------------|
| Scope             | Confined to a single, specific workspace                           | Available across multiple, unrelated workspaces                      |
| User Access       | Only accessible by members of the workspace where it's installed. | Accessible by any Notion user, regardless of their workspace.          |
| Creation         | Created by Workspace Owners within the integration dashboard.     | Created by Workspace Owners within the integration dashboard.      |
| Permissions       | Workspace members explicitly grant access to their pages or databases via Notion's UI. | Users authorize access to their pages during the OAuth flow, or by sharing pages directly with the integration. |
| OAuth Protocol     | Not applicable, as access is limited to a single workspace.        | Uses the OAuth 2.0 protocol to securely access information across multiple workspaces. |
| Dashboard Visibility | Visible to Workspace Owners in the integration dashboard, including integrations created by others. | - |

## What You Can Build: Integration Use Cases

Notion’s REST API opens up a world of possibilities for integrations, ranging from enhancing internal workflow to creating public-facing applications. Here’s a closer look at some of the innovative integrations developers have built with Notion:

### Data Integrations

Data integrations enable developers to seamlessly connect Notion workspaces to various applications, enhancing functionality and data management.

#### Example: Custom Workflow with Data Integration

Imagine a scenario where you want to automatically sync changes in your Notion workspace with a project management tool like Trello. With a data integration, you can set up workflows that trigger actions based on updates in your Notion pages, effectively integrating your workspace with other systems.

#### Example: Enhancing Project Management with Data Integration

Developers can also create integrations that enhance project management tools by providing additional context or insights into Notion data. This could involve syncing tasks from Notion to Trello or integrating Notion with project management software like Asana.

These examples illustrate the wide range of applications and use cases that Notion integrations can support. Whether you're building workflows within your own organization or creating public-facing applications, Notion offers a robust platform for integrating and managing data across different platforms.
```

# Using Notion's API for Integrations

A Notion workspace is a collaborative environment where teams can organize work, manage projects, and store information in a highly customizable way. Notion's REST API facilitates direct interactions with workspace elements through programming. Key functionalities include:

- [Pages](/docs/working-with-page-content): Create, update, and retrieve page content.
- [Databases](/docs/working-with-databases) and [Data Sources](/reference/data-sources): Manage databases, data source properties, entries, and schemas.
- [Users](/reference/user): Access user profiles and permissions.
- [Comments](/docs/working-with-comments): Handle page and inline comments.
- [Content Queries](/reference/post-search): Search through workspace content.
- [Authentication](/docs/authorization): Secure integrations with OAuth 2.0.
- [Link Previews](/docs/link-previews): Customize how links appear when shared.

To make interactions within Notion workspaces programmatically, you must associate these actions with a Notion user. Notion facilitates this by allowing API requests to be linked to a "bot" user.

Developers create integrations to define a bot's capabilities, including authenticating API requests, deciding when to make requests, and setting the bot's read/write permissions. Essentially, using Notion's Public API involves creating an integration that outlines how a bot interacts with your workspace and assigns REST API requests to the bot.

There are two primary integration types:

- [Internal](/docs/getting-started#internal-integrations): For private workspace workflows and automations.
- [Public](/docs/getting-started#public-integrations): For broader, shareable functionalities, including [Link Previews](/docs/link-previews).

For further details on integration possibilities and API specifics, proceed with the guide or consult the [API reference](/reference/intro). Check out our [demos](/page/examples) for practical examples.

## What is a Notion Integration?

A Notion integration, sometimes referred as a [connection](https://www.notion.so/help/add-and-manage-connections-with-the-api), enables developers to programmatically interact with Notion workspaces. These integrations facilitate linking Notion workspace data with other applications or the automation of workflows within Notion.

Integrations are installed in Notion workspaces and require **explicit permission** from users to access Notion pages and databases.

![Create Notion integrations that unlock new possibilities for teams.](https://files.readme.io/0f06356-notion_overview.jpg)

Notion users have access to a vast [library](https://www.notion.so/integrations/all) of existing integrations to enrich their experience further. For developers interested in creating custom solutions, Notion supports the development of both internal and public integrations. Both utilize the Notion API for workspace interactions.

Let's explore internal and public integrations.

### Internal vs. Public Integrations

Notion integrations come in two types: Internal and Public. Understanding the differences between them helps in choosing the right approach for your development needs.

- **Internal Integrations** are exclusive to a single workspace, accessible only to its members. They are ideal for custom workspace automations and workflows.
- **Public Integrations** are designed for a wider audience, usable across any Notion workspace. They cater to broad use cases and follow the OAuth 2.0 protocol for workspace access.

> 🔑 Public integrations must undergo a Notion security review before publishing.

#### Key Differences

| Feature | Internal Integrations | Public Integrations |
| --- | --- | --- |
| Scope | Confined to a single, specific workspace. | Available across multiple, unrelated workspaces. |
| User Access | Only accessible by members of the workspace where it's installed. | Accessible by any Notion user, regardless of their workspace. |
| Creation | Created by Workspace Owners within the integration dashboard. | Created by Workspace Owners within the integration dashboard. |
| Permissions | Workspace members explicitly grant access to their pages or databases via Notion’s UI. | Users authorize access to their pages during the OAuth flow, or by sharing pages directly with the integration. |
| OAuth Protocol | Not applicable, as access is limited to a single workspace. | Uses the OAuth 2.0 protocol to securely access information across multiple workspaces. |
| Dashboard Visibility | Visible to Workspace Owners in the integration dashboard, including integrations created by others. | - |

## What You Can Build: Integration Use Cases

Notion’s REST API opens up a world of possibilities for integrations, ranging from enhancing internal workflow to creating public-facing applications. Here’s a closer look at some of the innovative integrations developers have built with Notion:

### Data Integrations

Data integrations leverage the Notion API to automate data flow between Notion and other systems.

- **Automated Notifications:** Develop integrations that monitor Notion databases for changes. Upon detecting a change, these integrations can automatically send notifications various communication channels.
- **Github Synchronization:** Create integrations that keep Notion issues in sync with GitHub issues.
- **External Data Import:** Build integrations that import data from external sources directly into Notion databases. This can include importing customer data, project updates, or any other relevant information.

> 🔗 Examples:
>
> - [Create an integration](/docs/create-a-notion-integration)
> - [Working with comments](/docs/working-with-comments)
> - [Working with databases](/docs/working-with-databases)
> - [Working with files and media](/docs/working-with-files-and-media)
> - [Working with page content](/docs/working-with-page-content)

### Link Preview Integrations

Enhance the sharing experience within Notion with Link preview integrations, offering a glimpse into the content of shared links:

![Link preview of a GitHub PR.](https://files.readme.io/ce5daa3-Screen_Shot_2023-06-27_at_3.48.22_PM.png)

Link Preview of a GitHub PR.

Create integrations that allow for the customization of how shared links are presented in Notion, providing context and enhancing engagement.

> 🔑 Link Preview Integrations differ from public integrations. Review the [Link Preview guide](/docs/build-a-link-preview-integration).

> 🛠️ To build a Link Preview integration, developers must first apply for access to the feature through the [Notion Link Preview API request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com).
>
> Link Preview integrations published for distribution require a review from Notion's platform and security teams.

> 🔗 Quick Links
>
> - [Introduction to Link Preview integrations](/docs/link-previews)
> - [Build a Link Preview integration](/docs/build-a-link-preview-integration)
> - [API reference docs for the Link Preview unfurl attribute object](/reference/unfurl-attribute-object)
> - [Help Centre](https://www.notion.so/help/guides/notion-api-link-previews-feature)

### Identity Management Integrations (Enterprise Plans ONLY)

For enterprise-level workspaces, Notion offers advanced identity management capabilities:

- **SCIM API for User and Group Management**: Utilize the SCIM API to automate the provisioning and management of users and groups within enterprise workspaces, streamlining administrative tasks.
- **SAML SSO for Enhanced Security**: Implement Single Sign-On (SSO) using SAML for a secure and convenient authentication process, simplifying access for users across the enterprise.

> 🔗 Quick Links
>
> - [Provision users and groups with SCIM](https://www.notion.so/help/provision-users-and-groups-with-scim)
> - [SAML SSO configuration](https://www.notion.so/help/saml-sso-configuration)

## Starting Your Integration Journey

Embarking on building an integration with Notion? Begin with our foundational [_Build your first integration guide_](https://developers.notion.com/docs/create-a-notion-integration). As you become more familiar with the basics, expand your knowledge and skills with in-depth guides on [Authorization](https://developers.notion.com/docs/authorization), [Page content](https://developers.notion.com/docs/working-with-page-content), and [Databases](https://developers.notion.com/docs/working-with-databases).

## Key Resources

- [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js): Leverage our SDK designed for JavaScript environments to simplify interactions with the REST API, making development more efficient.
- [Technology Partner Program](https://www.notion.so/technology-partner-program): Have you developed a public integrations? Join our Technology Partner Program for access to dedicated support, exclusive distribution channels, and marketing opportunities.

Explore these resources and join the [Notion Devs Slack community](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg) to share your projects, gain insights from fellow developers, and discover new ways to enhance Notion with integrations.

> 🔗 Quick Links
>
> - [API reference documentation](https://developers.notion.com/reference/intro)
> - [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)
> - [Postman collection](https://www.postman.com/notionhq/)
> - [TypeScript starter template](https://github.com/makenotion/notion-sdk-typescript-starter)
> - [FAQs](https://developers.notion.com/page/frequently-asked-questions)
> - [Notion Devs Slack community](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg)
```

# Integrate with Notion

## What is Notion?

Notion is a cloud-based workspace that helps teams organize information, collaborate effectively, and achieve their goals together. It provides a robust platform for individuals and organizations to create, store, and share documents, databases, pages, and more.

## Why Integrate with Notion?

Integrating Notion with other tools or systems can streamline workflows, enhance productivity, and improve collaboration. Here are some key reasons why integrating Notion with other services might be beneficial:

- **Centralized Data Storage**: Combine Notion with other applications to centralize your data storage, making it easier to access and manage information from multiple sources.
- **Improved Collaboration**: Facilitate seamless communication and collaboration among team members by sharing and editing documents, databases, and pages in a single, unified environment.
- **Enhanced Functionality**: Leverage the capabilities of Notion alongside other software to unlock new possibilities for your business operations.
- **Customization Options**: Customize various features in Notion to fit your specific needs and preferences, such as themes, templates, and automation tools.

## How to Connect to Notion

### Step 1: Access Notion Workspace

Visit the [Notion workspace](https://www.notion.so/) and sign up for an account if you haven't already done so.

### Step 2: Obtain Access Token

Click on "Settings" at the top right corner of your Notion workspace.
- **Go to Settings** → **Access & Security**
- **Click on Manage tokens**
- **Add a new token**

![Image 1](https://assets.notion.so/47c2f633-604e-4010-b95f-50e91494951b/Access%20tokens.png)

- **Enter a name for the token**
- **Select the scope(s) required for your integration**
- **Click Add token**

![Image 2](https://assets.notion.so/47c2f633-604e-4010-b95f-50e91494951b/oauth-scopes.png)

### Step 3: Generate Client ID and Client Secret

In your Notion workspace:
- **Go to Settings** → **OAuth**
- **Click on Create client**

![Image 3](https://assets.notion.so/47c2f633-604e-4010-b95f-50e91494951b/client-id-secret.png)

- **Copy both Client ID and Client secret**
- **Paste them into your integration setup script**

### Step 4: Configure Your Integration

Now that you have your credentials, you can configure your integration to connect Notion with your chosen service provider. This step typically involves setting up authentication mechanisms between the two platforms.

### Step 5: Test Your Integration

After configuring your integration, test it to ensure everything is working correctly. Verify that you can successfully authenticate and interact with Notion using the integrated service.

## What is a Notion Integration?

A Notion integration serves as a bridge between Notion and other applications, allowing seamless data exchange, automation, and enhanced functionality. Integrations enable users to access and manipulate Notion data through external tools, facilitating a broader range of use cases and workflows.

## Internal vs. Public Integrations

### Key Differences

| Feature | Internal Integrations | Public Integrations |
| --- | --- | --- |
| **Scopes** | Limited to Notion APIs | Broad range of third-party APIs |
| **Security** | Typically less secure due to fewer restrictions | Generally considered more secure and reliable |
| **Integration Complexity** | Smaller-scale integrations | More complex integrations with larger providers |
| **Support** | Limited to Notion user base | Extensive support from the provider |

### Examples

- **Data Integrations**: Connecting Notion databases to CRM systems or analytics platforms.
- **Link Preview Integrations**: Integrating Notion pages with email clients or CMS platforms.
- **Identity Management Integrations (Enterprise Plans ONLY)**: Automating user provisioning and authentication processes.

## What You Can Build: Integration Use Cases

### Data Integrations

Connect Notion data sources like databases and spreadsheets to various applications, enabling data-driven decision-making and analysis.

### Link Preview Integrations

Enable users to preview and edit links directly within Notion, enhancing workflow efficiency and collaboration.

### Identity Management Integrations (Enterprise Plans ONLY)

Automate user provisioning and authentication processes, streamlining access management and improving security.

## Starting Your Integration Journey

Embarking on building an integration with Notion? Begin with our foundational [_Build your first integration guide_](https://www.notion.so/docs/create-a-notion-integration). As you become more familiar with the basics, expand your knowledge and skills with in-depth guides on [Authorization](https://www.notion.so/docs/authorization), [Page content](https://www.notion.so/docs/working-with-page-content), and [Databases](https://www.notion.so/docs/working-with-databases).

## Key Resources

- [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js): Leverage our SDK designed for JavaScript environments to simplify interactions with the REST API, making development more efficient.
- [Technology Partner Program](https://www.notion.so/technology-partner-program): Have you developed a public integrations? Join our Technology Partner Program for access to dedicated support, exclusive distribution channels, and marketing opportunities.

Explore these resources and join the [Notion Devs Slack community](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg) to share your projects, gain insights from fellow developers, and discover new ways to enhance Notion with integrations.

## FAQs

- [How do I get started with integrating Notion with my application?](https://www.notion.so/docs/integrate-with-notion#how-do-i-get-started-with-integrating-notion-with-my-application)
- [Can I build an integration for Notion without creating a new application?](https://www.notion.so/docs/integrate-with-notion#can-i-build-an-integration-for-notion-without-creating-a-new-application)
- [What are the benefits of integrating Notion with my existing tools?](https://www.notion.so/docs/integrate-with-notion#what-are-the-benefits-of-integrating-notion-with-my-existing-tools)
- [How does Notion handle authentication when connecting to third-party applications?](https://www.notion.so/docs/integrate-with-notion#how-does-notion-handle-authentication-when-connecting-to-third-party-applications)
- [Can I customize the integration settings for Notion?](https://www.notion.so/docs/integrate-with-notion#can-i-customize-the-integration-settings-for-notion)
- [What kind of data can I integrate with Notion?](https://www.notion.so/docs/integrate-with-notion#what-kind-of-data-can-i-integrate-with-notion)
- [How often should I update my integration to ensure it remains secure?](https://www.notion.so/docs/integrate-with-notion#how-often-should-i-update-my-integration-to-ensure-it-remains-secure)
```