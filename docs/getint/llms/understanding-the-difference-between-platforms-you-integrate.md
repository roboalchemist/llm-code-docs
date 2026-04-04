# Source: https://docs.getint.io/getting-started-with-the-platform/preparing-for-the-integration/understanding-the-difference-between-platforms-you-integrate.md

# Understanding the Difference Between Platforms you Integrate

### Field Naming Variations

* Different tools often use different terminologies for similar fields. It’s crucial to identify these variations and establish a mapping (e.g., Jira's "Summary" to Azure DevOps, "Description").

### Tool-Specific Fields and Custom Field Creation

* Some fields are unique to specific tools (e.g., "Assignment Group" in ServiceNow, "Area Path" in Azure DevOps).
* Technical Note: To integrate these unique fields, you may need to create corresponding custom fields in the other system to store this data. This ensures that all relevant information is captured and synced accurately.

### Inline Image Support Inconsistencies

* Different tools have varying capabilities for embedding images within items. This should be considered when setting up integrations to ensure compatibility.

### Out-of-the-Box vs. Custom Fields

* Tools like Jira offer numerous pre-defined fields, while others, like Monday.com, may start with fewer and require customizations for additional fields.

### Mandatory Fields Variance

* The presence and enforcement of mandatory fields differ across systems, affecting how data is entered and synchronized.

### Item Type Diversity

* The range of item types varies significantly among tools, influencing how data is categorized and managed during integration.

### Hierarchy and Structure Complexity

* The level of hierarchical complexity in tools can vary, impacting how sub-items are managed and synchronized.

### API Documentation and Usability

* The quality and detail of API documentation can greatly affect the ease of the integration setup and customization.

### Read-Only Field Integration

* Some fields in certain tools are read-only and can be integrated in only one direction.
* Technical Note: To enable bi-directional integration for such fields, a corresponding writable custom field may need to be created in the other system. This allows for two-way data flow while respecting the read-only nature of the original field.

### Custom Field Support

* The extent and flexibility of custom field support can vary, affecting how specific data points are handled during integration.

### Integration Limitations and Custom Solutions

* Each tool has its unique limitations regarding integration. Identifying these early can help in determining the need for workarounds or custom development.

### Workflow Mechanisms and Compatibility

* The complexity and nature of workflow configurations differ across tools, which should be considered for maintaining process integrity during integration.

In summary, technical preparation and a deep understanding of each tool’s capabilities and limitations are key to a successful integration process with Getint. Custom field creation, proper mapping, and accommodating read-only fields are just some of the technical strategies that can be employed to ensure seamless integration across diverse systems.

### Integration of Collaboration Tools: Detailed Technical Perspective

Integrating various collaboration tools using Getint requires a deep understanding of each platform's unique features and limitations. Here's an expert-level breakdown focusing on common collaboration tools and their differences:

#### Jira and Azure DevOps

* Jira's "Epic Link" correlates to Azure DevOps' "Parent Work Item."
* 'Sprint' in Jira aligns with 'Iteration Path' in Azure DevOps.

#### ServiceNow and Salesforce

* ServiceNow's "Assignment Group" can be mapped to a custom field in Salesforce, as Salesforce doesn't have a direct equivalent.
* "Incident State" in ServiceNow differs from "Case Status" in Salesforce in terms of the lifecycle of a ticket.

#### Asana and ClickUp

* Asana's "Sections" are similar to ClickUp's "Lists" within projects.
* 'Tags' in Asana can be equated to 'Labels' in ClickUp for categorization.

#### Monday.com and GitLab

* Monday.com's "Pulse" is conceptually similar to GitLab's "Issue."
* Custom status columns in Monday.com need to be mapped to GitLab's "Issue Status."

#### GitHub and Wrike

* GitHub's "Issues" can be mapped to "Tasks" in Wrike.
* "Milestones" in GitHub have a different implementation compared to Wrike's "Folders/Projects."

#### HubSpot and Trello

* HubSpot's "Deals" can be somewhat paralleled to Trello's "Cards" in a sales pipeline board.
* "Contact" in Hubspot versus "Member" in Trello reflects the CRM versus project management focus.

#### Zendesk and Jira Service Management

* "Ticket" in Zendesk corresponds to "Issue" in Jira Service Management.
* Zendesk's "Views" for ticket organization are different from Jira Service Management's "Queues."

#### Read-Only and Custom Fields

* Tools like Jira and Azure DevOps allow extensive custom fields, which might need to be created in other systems like Monday.com or Trello for a complete sync.
* For read-only fields in systems like Salesforce (e.g., "Created Date"), corresponding writable fields may be necessary in the integrated tool to facilitate bi-directional data flow.

In each case, understanding the specific functionalities and limitations of these tools is crucial. This knowledge informs the creation of custom fields and the mapping process to ensure accurate data synchronization. It's also important to consider the hierarchical structures, workflow mechanisms, and API capabilities of each tool for a successful integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
