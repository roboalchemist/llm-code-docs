# Source: https://www.apollographql.com/docs/graphos/platform/access-management/org.md

# GraphOS Organizations

All data in GraphOS (graphs, schemas, metrics, etc.) is associated with a particular *organization*.
Every organization has one or more *members* who manage it and can access its associated data.
Each member is assigned a *role* that defines their capabilities within the organization. Members can only be assigned one role.

Enterprise organizations have access to fine-grained access controls via additional [member roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles).

## Create an organization

You create your first organization as part of the [account creation process](https://www.apollographql.com/docs/graphos/platform/access-management/account), unless you've been invited to an existing organization by another Apollo user.

You can create additional organizations by clicking **Create a new organization** at the bottom of your organization dropdown in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content):

A single organization can include any number of graphs, so a single company rarely needs more than one or two organizations.

## View your organizations

Click the organization dropdown at the top of the page in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content) to view the list of all organizations you belong to.

* Click on an organization to view its associated graphs and metrics.
* Each organization has a **Graphs** list, a **Dashboard**, a **Members** management page, and a **Settings** page.

  * Enterprise organizations have access to [audit logs](https://www.apollographql.com/docs/graphos/platform/access-management/audit-log) on the **Audit** page.
  * The **Settings** page lets you view and edit organization properties like organization name, logo, ID, and domain.

## Delete an organization

This action can't be undone!

You can delete an organization at any time. Doing so removes all traces of the organization from GraphOS.

Deleting your organization does all the following:

* Removes all user memberships from the organization
* Permanently deletes all graphs from the organization, along with their associated data. These graph IDs cannot be reused later.
* Immediately terminates any plan subscription associated with the organization. We can't issue refunds for this, unfortunately.

## Internal graph visibility (Enterprise only)

By default, graphs are visible to all members of your organization. If you have a GraphOS Enterprise plan, you can set a graph to instead be visible only to members you invite.

You can configure visibility and grant your organization's members explicit access to your graph from the **Permissions** tab of your graph's **Settings** page.

**Org Admins** can always see all graphs in your organization.

## Ownership transfer

Organization members with the [appropriate permissions](https://www.apollographql.com/docs/graphos/platform/graph-management/transfers#required-roles) can [transfer ownership](https://www.apollographql.com/docs/graphos/platform/graph-management/transfers) of a graph from one organization to another.
