# Source: https://www.metabase.com/docs/latest/paid-features/

<div>

1.  

2.  Pro and Enterprise features

</div>

<div>

[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.57](/docs/v0.57)
-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Pro and Enterprise features

This page lists the features included in Metabase Pro and Enterprise plans. See [Pricing](/pricing/).

## Query data

A straight-forward way for everyone to ask questions and get answers from your data on their own.

### Metabot AI

Ask questions in natural language in the chat interface, generate and debug SQL, and more. [Learn more](/features/metabot-ai).

### Granular result and duration caching

Get super specific about which databases, dashboards, and questions to cache, and for how long. [Learn more](/docs/latest/configuring-metabase/caching).

## Data visualization and sharing

Dashboards and charts that people will actually use.

### Scheduled delivery and alerts via email

Send scheduled updates to yourself, your team, or even people outside of your org. Get alerts when things change you and need to take action. [Learn more](/features/analytics-dashboards).

### Scheduled delivery and alerts via Slack

Send scheduled updates to yourself, your team, or even people outside of your org. Get alerts when things change you and need to take action. [Learn more](/features/analytics-dashboards).

### Scheduled delivery with custom filters

Set different filters for each subscription when sending results. [Learn more](/docs/latest/dashboards/subscriptions#customize-filter-values-for-each-dashboard-subscription).

### Customize suggested recipients

Control which recipients people can see when they create a new dashboard subscription or alert. [Learn more](/docs/latest/configuring-metabase/email#suggest-recipients-on-dashboard-subscriptions-and-alerts).

### PDF export and downloads (.png, .csv, .xlsx, .json) 

No screenshots required. Save and share dashboards and charts in your preferred format. Remove Metabase branding on PDF exports on Pro and Enterprise. [Learn more](/features/analytics-dashboards).

### Documents

Create and share stories with your data. [Learn more](/docs/latest/documents/introduction).

## Organization

Analytics with a bit of order, so it's easy to find and return to important stuff.

### Official collections

Admins can mark collections as fresh and trustworthy. [Learn more](/features/collections).

### Moderated questions

Show which questions have been vetted by someone in the know. [Learn more](/features/collections).

### Verified models

Make sure your team is using an accurate data source with models marked as verified. [Learn more](/features/models).

### Automatic dependency checks

Automatically detect when changes to questions, models, metrics or snippets will break something. [Learn more](/docs/latest/questions/introduction#checking-for-breaking-changes).

### Remote Sync

Connect your Metabase to a Git repo so you can manage content like you manage code. [Learn more](/docs/latest/installation-and-operation/remote-sync).

## Multi-tenant data segregation and permissions

Fine-grained control over who sees what.

### Row- and column-level permissions

Granular control over permissions for multi-tenant analytics. [Learn more](/features/data-segregation).

### Database-managed row-level permissions

Apply the permissions you've set up for people in your database in Metabase. [Learn more](/features/permissions).

### Native support for one-database-per-tenant

Database routing ensures queries go to the correct database per user. [Learn more](/features/permissions).

### Application permissions

Give some, but not all, admin permissions to select groups. [Learn more](/features/permissions).

### SSO permission mapping

Manage permissions at scale easier by mapping to user attributes with SSO. [Learn more](/features/permissions).

### Snippet controls

Save and organize your Snippets with controlled permissions. [Learn more](/features/permissions).

### Download results

Determine which groups can download results, and how many rows. [Learn more](/features/permissions).

### Group managers

Group managers can manage other people within their group. [Learn more](/features/permissions).

### Table metadata permissions

Control who can see and edit table metadata. [Learn more](/docs/latest/permissions/data#manage-table-metadata-permissions).

### Database management permissions

Control who can see and edit database connections. [Learn more](https://www.metabase.com/docs/latest/permissions/data#manage-database-permissions).

## Security and Single sign-on

Secure your perimeter and stay compliant with all the best practices.

### LDAP

Authenticate your users with LDAP and automatically map permissions. [Learn more](/docs/latest/people-and-groups/ldap).

### LDAP group membership filter

Sync only the groups you want. [Learn more](/docs/latest/people-and-groups/ldap#ldap-group-membership-filter).

### Syncing user attributes with LDAP

Manage user attributes such as names, emails, and roles from your LDAP directory. [Learn more](/docs/latest/people-and-groups/ldap#syncing-user-attributes-with-ldap).

### SAML

Authenticate your users and maps permissions with Okta, Auth0, Google, Keycloak, and more. [Learn more](/docs/latest/people-and-groups/authenticating-with-saml).

### JWT

Authenticate your users and map permissions with JSON web token. [Learn more](/docs/latest/people-and-groups/authenticating-with-jwt).

### SLO

End auth sessions with multiple apps with a single logout. [Learn more](/docs/latest/people-and-groups/authenticating-with-saml#saml-single-logout-slo).

### SCIM account provisioning

Decouple authentication from provisioning, with support for deprovisioning user accounts. [Learn more](/docs/latest/people-and-groups/user-provisioning).

### Authenticating with a provider for PostgreSQL

Authenticate with a provider for PostgreSQL. [Learn more](/docs/latest/databases/connections/postgresql#use-an-authentication-provider).

### Disabling password login

Enforce logging in via Single Sign-on. [Learn more](/docs/latest/people-and-groups/changing-password-complexity#disabling-password-logins).

### Session timeout

Set time limit for when people are logged out of Metabase. [Learn more](/docs/latest/people-and-groups/changing-session-expiration#session-timeout).

### Approved domains

Limit the available domains for dashboard subscription and alert emails. [Learn more](/docs/latest/configuring-metabase/email#approved-domains-for-notifications).

### Multiple domains for Google Sign-in

Allow people to sign in with multiple domains in your Google Workspace. [Learn more](/docs/latest/people-and-groups/google-sign-in#multiple-domains-for-google-sign-in).

## Meta analytics

See who did what, when to ensure your data's being put to good use, and to meet compliance needs.

### Usage analytics

See which dashboards and questions are being viewed, downloaded and subscribed to most. [Learn more](/features/usage-analytics).

### Question error logs

See which queries returned errors when last run. [Learn more](/docs/latest/usage-and-performance-tools/tools#question-error-logs).

## Embedded analytics

Let your customers see and play with their data with as much (or as little) flexibility as you want.

### Static embedding

Basic embedding of dashboards and charts. [Learn more](/docs/latest/embedding/static-embedding).

### Interactive embedding

The full power of Metabase in your app, with interactive features like the drill-through menu to explore, and your branding. (The most awesome version of embedding). [Learn more](/product/embedded-analytics).

### Embedded natural language querying

Give you customers AI-powered analytics to ask questions in natural language with an LLM interface for your data. [Learn more](/product/embedded-analytics).

### Embedded query builder

Let your customers ask their own questions for fully customized access to their data. [Learn more](/product/embedded-analytics).

### Multi-tenant analytics

Fine-grained permissions mapped with SSO so your customers or users only see what they need to. [Learn more](/product/embedded-analytics).

### White-label with your branding

Metabase made to look like you, with your logo, colors, even name and domain name. [Learn more](/features/white-label-analytics).

### Custom colors, fonts, and UI elements

Full control over your Metabase's look, down to the copy. Choose from our library or upload your own fonts and colors. [Learn more](/features/white-label-analytics).

### Multi-language embeds

Set locale for interactive embeds. [Learn more](/docs/latest/embedding/interactive-ui-components#locale).

### Content translation for static embeds

Translate the content of static embeds into different languages. [Learn more](/docs/v0.56/embedding/translations).

### Embedded analytics SDK for React

React toolkit for fully integrated, custom in-app analytics [Learn more](/product/embedded-analytics-sdk).

### Embedded analytics JS

JS library built on top of the SDK for embedding and customizing individual Metabase components. [Learn more](/docs/v0.56/embedding/embedded-analytics-js).

### Disabling downloads for static embeds

Control whether people can download results from static embeds. [Learn more](/docs/latest/embedding/static-embedding-parameters#disable-downloads-for-an-embedded-question-or-dashboard).

## Data sources

Put a simple, intuitive interface between your data and your business-users for easier analytics.

### Deleting models and tables created by uploads

Remove models and tables created by people uploading CSVs. [Learn more](/docs/latest/exploration-and-organization/uploads#deleting-models-and-tables-created-by-uploads).

## Deployment

Self-host your own instance or let us do it for you.

### Fully air-gapped deployment

Run Metabase on-prem in ultra-secure and private environments [Learn more](/product/air-gapping).

### Serialization

Export and import everything about an instance to create backups, or parallel instances for testing, staging and production environments. [Learn more](/docs/latest/installation-and-operation/serialization).

### Development Instances

Get an environment for testing and development. [Learn more](/docs/latest/installation-and-operation/development-instance).

### Loading settings from a configuration file

Initialize Metabase on launch from a config file [Learn more](/docs/latest/configuring-metabase/config-file).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.]() ]