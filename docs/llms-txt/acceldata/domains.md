# Source: https://docs.acceldata.io/documentation/domains.md

# Domains

In large organizations, different teams — like Finance, Marketing, Data Engineering, or Compliance — often work with distinct sets of data assets, dashboards, or pipelines. Giving every team access to all resources is not only inefficient but risky.

That’s why ADOC’s Domain Management feature allows administrators to create logical boundaries around data and resources. These are called domains, and they form the foundation for secure, structured, and purpose-driven collaboration.

## What Is a Domain in ADOC?

A domain is a virtual container for organizing related resources (like asset groups or reports) and controlling which users or user groups can access them, and what they can do.

Think of it like a project folder in a cloud drive — each folder has its own files and a custom list of people who can view or edit them. In ADOC, domains help isolate resources by department, use case, or sensitivity level.

Key Benefits of Domains

- **Centralized Resource Grouping**: Keep data assets, reports, and monitoring tools organized under meaningful categories.
- **Scoped Access Control**: Combine with RBAM to define who sees what and what actions they can perform within each domain.
- **Role-Based Collaboration**: Assign user groups with tailored roles like viewer, editor, or owner — per domain.
- **Easier Governance**: Track usage, changes, and permissions by domain — improving auditability and control.

## Managing Domains in ADOC

### Accessing the Domain Management Panel

To get started:

1. Click the **Settings** icon in the ADOC left-side navigation pane.
2. Under **Domain Management**, select **Domains**.
3. This takes you to the **Domains Overview** page.

### Viewing Existing Domains

The **Domains Overview** provides a consolidated view of all the domains defined within the system, allowing you to quickly understand how resources are organized and managed. Each domain entry includes key details such as the name of the domain (e.g., "Marketing Analytics" or "Finance Compliance"), the user groups that have been assigned access to it, the resources associated with the domain (such as asset groups or report groups), and the creator, indicating the user or system that originally set up the domain.

Click on a domain name to view more details, such as:

- User Group Role Mapping
- Activity Log (creation, edits, assignments)

### Creating a New Domain

Only administrators can create domains. Here’s how:

1. Navigate to **Settings**.
2. Click **Domains** under **Domain Management**.
3. Click the **Create** button
4. Fill in the form:

    1. **Name** (Required): Give the domain a unique, descriptive name.
    2. **Description** (Optional): Summarize its purpose — e.g., “Holds all assets related to Q4 Revenue Reporting.”
    3. Click **Add Resource Group** to link asset or report groups to the domain.
    4. Click **Add** under **User Groups** to:

        1. Assign one or more user groups
        2. Set their domain-specific roles (e.g., resource_owner, resource_editor, resource_viewer)

5. Click **Create** to finalize.

The domain is now active — users in the assigned groups will only see and interact with the associated resources as per their roles.

## Editing an Existing Domain

You can make changes at any time by:

1. Navigating to the **Domains** page.
2. Clicking the domain name you want to edit.
3. In the **Domain Details Panel**, click **Edit**.
4. From here, you can:

    1. Rename the domain or update its description
    2. Add/remove resource groups
    3. Adjust which user groups are assigned, or change their role mappings

5. Click **Save** when done.