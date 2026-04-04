# Source: https://docs.getint.io/getting-started-with-the-platform/apps-connectors/hubspot.md

# HubSpot

## Getint: Simplifying HubSpot Integration and Data Synchronization

**Getint** is designed to connect and synchronize various tools, supporting integrations such as HubSpot with Jira, Asana, or Azure DevOps. We offer SaaS and On-Premise solutions, providing flexibility for different business needs.

### Key Topics Covered

* [Setting Up the App](#how-to-set-up-getint-for-hubspot)
* [Supported Fields in HubSpot](#supported-fields-for-hubspot-integration)
* [Supported Item Types](#supported-item-types-for-hubspot-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

Getint helps synchronize data across platforms or instances, including HubSpot. It enables users to monitor and manage tasks or activities across projects and integrate HubSpot with other tools.

### How to Set Up Getint for HubSpot

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* For Jira users: If you want to integrate Jira with HubSpot, download the app from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1231637/hubspot-integration-for-jira-bi-directional-issue-sync?hosting=cloud\&tab=overview).
* For other tools: Select between Getint On-Premise or SaaS options.

**Step 2: Set Up a Connection with HubSpot**

* Ensure you have the correct [access permissions](https://docs.getint.io/guides/quickstart/connection#hubspot).
* Choose HubSpot as the app, create a new connection, and enter your HubSpot credentials.

**Step 3: Connect to Another Tool**

* Pick the platform you want to integrate with HubSpot, such as Jira.

**Step 4: Map Types and Fields**

* Match HubSpot categories like Contacts or Deals with their counterparts in the other tool.
* Use the "Quick Build" feature for automatic mapping or customize mappings manually if needed.

Our support team is always available to assist with any setup or operational challenges.

For additional guidance on using Getint with HubSpot, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira HubSpot Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-hubspot-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for HubSpot Integration

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **HubSpot Field**                                               | **One Way** | **Both Ways** |
| --------------------------------------------------------------- | ----------- | ------------- |
| All associated contact companies                                | ✔️          |               |
| All associated contact emails                                   | ✔️          |               |
| All associated contact first names                              | ✔️          |               |
| All associated contact last names                               | ✔️          |               |
| All associated contact mobile phones                            | ✔️          |               |
| All associated contact phones                                   | ✔️          |               |
| All conversation mentions                                       | ✔️          |               |
| All Owner IDs                                                   | ✔️          |               |
| All Team IDs                                                    | ✔️          |               |
| All teams                                                       | ✔️          |               |
| Amount                                                          | ✔️          | ✔️            |
| Amount in company currency                                      | ✔️          |               |
| Annual contract value                                           | ✔️          |               |
| Annual recurring revenue                                        | ✔️          |               |
| Applied SLA                                                     | ✔️          | ✔️            |
| Assigned Teams                                                  | ✔️          |               |
| Assigned To (Assignees)                                         | ✔️          | ✔️            |
| Assignment Method                                               | ✔️          | ✔️            |
| Associated Shared Deal Product Interests                        | ✔️          |               |
| Associated Shared Deal Type                                     | ✔️          |               |
| Attributed reporting team                                       | ✔️          | ✔️            |
| Auto-generated from thread id                                   | ✔️          |               |
| Average ticket sentiment                                        | ✔️          |               |
| Average ticket sentiment score                                  | ✔️          |               |
| Business units                                                  | ✔️          | ✔️            |
| Campaign of last booking in meetings tool                       | ✔️          |               |
| Category                                                        | ✔️          |               |
| Close date                                                      | ✔️          | ✔️            |
| Closed Deal Amount                                              | ✔️          |               |
| Closed deal amount in home currency                             | ✔️          |               |
| Closed Deal Close Date                                          | ✔️          |               |
| Closed Deal Create Date                                         | ✔️          |               |
| Closed Deal Lost Reason                                         | ✔️          | ✔️            |
| Closed won count                                                | ✔️          |               |
| Closed Won Date (Internal)                                      | ✔️          |               |
| Closed Won Reason                                               | ✔️          | ✔️            |
| Companies                                                       | ✔️          | ✔️            |
| Comments & Attachments                                          | ✔️          | ✔️            |
| Contacts                                                        | ✔️          | ✔️            |
| Conversation NPS score                                          | ✔️          |               |
| Conversations originating thread id                             | ✔️          |               |
| Copied at                                                       | ✔️          |               |
| Copied by user                                                  | ✔️          |               |
| Copied ticket                                                   | ✔️          |               |
| Copied ticket source                                            | ✔️          |               |
| Create Date                                                     | ✔️          | ✔️            |
| Created by                                                      | ✔️          | ✔️            |
| Created by user ID                                              | ✔️          |               |
| Cumulative time in                                              | ✔️          |               |
| Currency                                                        | ✔️          | ✔️            |
| Custom fields                                                   | ✔️          | ✔️            |
| Custom inbox ID                                                 | ✔️          | ✔️            |
| Customer Agent ticket status                                    | ✔️          |               |
| Date entered                                                    | ✔️          |               |
| Date entered current stage                                      | ✔️          |               |
| Date exited                                                     | ✔️          |               |
| Date of last engagement                                         | ✔️          |               |
| Date of last meeting booked in meetings tool                    | ✔️          |               |
| Days to close                                                   | ✔️          |               |
| Days to close (without rounding)                                | ✔️          |               |
| Draft UserIDs                                                   | ✔️          |               |
| Deal amount calculation preference                              | ✔️          | ✔️            |
| Deal Collaborator                                               | ✔️          | ✔️            |
| Deal Description                                                | ✔️          | ✔️            |
| Deal Name                                                       | ✔️          | ✔️            |
| Deal owner                                                      | ✔️          | ✔️            |
| Deal probability                                                | ✔️          | ✔️            |
| Deal Score                                                      | ✔️          |               |
| Deal Split Users                                                | ✔️          |               |
| Deal Stage                                                      | ✔️          | ✔️            |
| Deal stage probability shadow                                   | ✔️          |               |
| Deal Tags                                                       | ✔️          |               |
| Deal Type                                                       | ✔️          | ✔️            |
| Email Subject                                                   | ✔️          |               |
| External object ids                                             | ✔️          |               |
| Exchange rate                                                   | ✔️          | ✔️            |
| File upload                                                     | ✔️          | ✔️            |
| First agent email response date                                 | ✔️          |               |
| First agent response date                                       | ✔️          |               |
| First message sentiment                                         | ✔️          |               |
| First message sentiment score                                   | ✔️          |               |
| Forecast amount                                                 | ✔️          |               |
| Forcast category                                                | ✔️          | ✔️            |
| Forecast probability                                            | ✔️          | ✔️            |
| Form                                                            | ✔️          |               |
| Form submission conversion ID                                   | ✔️          |               |
| Global Term Line Item Discount Percentage                       | ✔️          | ✔️            |
| Global Term Line Item Recurring Frequency                       | ✔️          | ✔️            |
| Global Term Line Item Recurring Billing Period                  | ✔️          | ✔️            |
| Global Term Line Item Recurring Billing Start                   | ✔️          |               |
| Help Desk onboarding ticket                                     | ✔️          |               |
| Helpdesk Sort Timestamp                                         | ✔️          |               |
| HubSpot Campaign                                                | ✔️          | ✔️            |
| HubSpot Create Date                                             | ✔️          | ✔️            |
| HubSpot Sales Lead                                              | ✔️          |               |
| HubSpot Shared Deal MRR                                         | ✔️          |               |
| HubSpot Shared Deal MRR Currency Code                           | ✔️          |               |
| HubSpot Team                                                    | ✔️          |               |
| ID                                                              | ✔️          |               |
| Inbox ID                                                        | ✔️          |               |
| Is Closed (numeric)                                             | ✔️          |               |
| Is Open (numeric)                                               | ✔️          |               |
| Item Type                                                       | ✔️          |               |
| Language                                                        | ✔️          | ✔️            |
| Last Activity Date                                              | ✔️          |               |
| Last Activity Date (Ticket Note)                                | ✔️          |               |
| Last Contacted                                                  | ✔️          |               |
| Last CES                                                        | ✔️          |               |
| Last customer reply date                                        | ✔️          |               |
| Last email activity                                             | ✔️          |               |
| Last email date                                                 | ✔️          |               |
| Last email ID                                                   | ✔️          |               |
| Last email type                                                 | ✔️          |               |
| Last Modified Date                                              | ✔️          |               |
| Last Response Date                                              | ✔️          |               |
| Latest Approval Status                                          | ✔️          |               |
| Latest Approval Status ID                                       | ✔️          |               |
| Latest Meeting Activity                                         | ✔️          |               |
| Latest message                                                  | ✔️          |               |
| Latest time in                                                  | ✔️          |               |
| Latest Traffic Source                                           | ✔️          |               |
| Likelihood to close by the close date                           | ✔️          |               |
| Medium of last booking in meetings tool                         | ✔️          |               |
| Merged Deal IDs                                                 | ✔️          |               |
| Merged Ticket IDs                                               | ✔️          |               |
| mentioned\_note\_user\_IDs                                      | ✔️          |               |
| mentions\_user\_IDs                                             | ✔️          |               |
| Microsoft Teams message ID for this ticket.                     | ✔️          |               |
| Monthly recurring revenue                                       | ✔️          |               |
| Most relevant SLA status                                        | ✔️          | ✔️            |
| Most Relevant SLA Type                                          | ✔️          | ✔️            |
| Next Pipeline Impact                                            | ✔️          | ✔️            |
| Next Activity Date                                              | ✔️          |               |
| Next Activity Type                                              | ✔️          |               |
| Next Meeting ID                                                 | ✔️          |               |
| Next Meeting Name                                               | ✔️          |               |
| Next Meeting Start Time                                         | ✔️          |               |
| Next step                                                       | ✔️          | ✔️            |
| Next Step Updated At                                            | ✔️          |               |
| Number of Active Deal Registrations                             | ✔️          |               |
| Number of Associated Contacts                                   | ✔️          |               |
| Number of Associated Line Items                                 | ✔️          |               |
| Number of Deal Splits                                           | ✔️          |               |
| Number of Sales Activities                                      | ✔️          |               |
| Number of target accounts                                       | ✔️          |               |
| Number of times contacted                                       | ✔️          |               |
| Object Type                                                     | ✔️          |               |
| Open deal create date                                           | ✔️          |               |
| Original Traffic Source                                         | ✔️          | ✔️            |
| Original Traffic Source Drill-Down 1                            | ✔️          |               |
| Original Traffic Source Drill-Down 2                            | ✔️          |               |
| Owner assigned date                                             | ✔️          |               |
| Owning Teams                                                    | ✔️          | ✔️            |
| Pinned Engagement ID                                            | ✔️          | ✔️            |
| Pipeline                                                        | ✔️          | ✔️            |
| Primary Company ID                                              | ✔️          |               |
| Primary Company Name                                            |             |               |
| Priority                                                        | ✔️          | ✔️            |
| Recent Sales Email Replied Date                                 | ✔️          |               |
| Record creation source                                          | ✔️          |               |
| Record creation source ID                                       | ✔️          |               |
| Record creation source user ID                                  | ✔️          |               |
| Record ID                                                       | ✔️          |               |
| Record source                                                   | ✔️          |               |
| Record source detail 1                                          | ✔️          |               |
| Record source detail 2                                          | ✔️          |               |
| Record source detail 3                                          | ✔️          |               |
| Shared teams                                                    | ✔️          | ✔️            |
| Shared users                                                    | ✔️          |               |
| Source Object ID                                                | ✔️          |               |
| Source of last booking in meetings tool                         | ✔️          |               |
| Status transition                                               | ✔️          | ✔️            |
| Task Type                                                       | ✔️          | ✔️            |
| Tasks completed                                                 | ✔️          |               |
| Task Title                                                      | ✔️          | ✔️            |
| The predicted deal amount                                       | ✔️          |               |
| <p>The predicted deal amount in your company's currency<br></p> | ✔️          |               |
| Time in                                                         | ✔️          |               |
| Time to                                                         | ✔️          |               |
| Total contract value                                            | ✔️          |               |
| Unique creation Key                                             | ✔️          |               |
| Updated by user ID                                              | ✔️          |               |
| URL                                                             | ✔️          |               |
| User IDs of all notification followers                          | ✔️          |               |
| User IDs of all notification unfollowers                        | ✔️          |               |
| User IDs of all owners                                          | ✔️          |               |
| Users Interaction                                               | ✔️          |               |
| Weighted amount                                                 | ✔️          |               |
| Weighted amount in company currency                             | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Supported Item Types for HubSpot Integration

| Company   |
| --------- |
| Contact   |
| Deal      |
| Line Item |
| Quote     |
| Task      |
| Ticket    |

### Limitations and Considerations

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Issue Types:** When Getint creates a new issue in HubSpot, it will always be one specific type (i.e., Task, Deal, or Ticket). You can set the default item type using a rule or manually adjust it in HubSpot after creation.
* **Comments:** Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account.

Comments and attachments transferred from HubSpot to Jira will be set to either public or private. You can configure Jira to mark all comments from HubSpot as private automatically. However, it is impossible to enable both public and private visibility options simultaneously.

* **Change History:** Unfortunately, Getint cannot integrate the history of changes.
* **Inline** **images** aren't supported for the Description field.

### Contacting Our Support Team

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
