# Source: https://docs.axonius.com/docs/zendesk-adapter.md

# Zendesk

Zendesk is a cloud-based help desk management solution offering customizable tools to build customer service portal, knowledge base, and online communities.

| Attributes                  | Axonius Cyber Assets                | Axonius SaaS Applications                                        |
| --------------------------- | ----------------------------------- | ---------------------------------------------------------------- |
| Service Account Required?   | Yes                                 | Yes                                                              |
| Service Account Permissions | Administrator                       | Administrator                                                    |
| API Key Required            | Yes                                 | Yes                                                              |
| Required Adapter Fields     | Sub Domain, Username, API Key/Token | Sub Domain, Username and Password, API Key/Token, 2FA Secret Key |

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles
* Groups
* Licenses
* Application Settings
* SaaS Applications
* Tickets
* Accounts

## Adapter Integration Setup

To successfully connect this adapter, you need to create a user account and an API token by completing the following steps:

1. [Creating a new user account](/docs/zendesk-adapter#creating-a-new-user-account)
2. [Generating a new API token](/docs/zendesk-adapter#generating-a-new-api-token)

### Creating a New User Account

It is recommended for the username and password to be derived from a newly created user account dedicated for the usage of Axonius. Retrieve the username and password from that user account.

<Callout icon="📘" theme="info">
  Note

  When single-sign-on is enabled, it is recommended to derive the Email address and password from a user account maintained by the single-sign-on solution. Please contact Axonius support for assistance.
</Callout>

1. Log in as an admin to the Admin Center. In the sidebar, click **People** in the sidebar, then select **Team `>` Team members**.
2. At the top of the page, click **Add user**.
3. Enter the user's **Name** and **Email**.
4. Choose a **Staff member** for the **User type**.
5. Select the **Administrator** role.
6. Click **Add**.

### Generating a New API Token

API tokens can be used by anyone on the account and aren't associated with specific users. Admins can view, add, delete, and manage API tokens in the Zendesk Admin interface. To generate an API token, you must be an administrator and API token access must be enabled.

API token access is disabled by default. Before you can generate an API token, enable API token access. Once you have enabled API token access, admins can generate an API token.

To enable API token access and to generate an API token:

1. Log in as an admin. In the Admin Center, in the sidebar, click **Apps and integrations** in the sidebar, then select **APIs `>` Zendesk APIs**.
2. Click the **Token Access** toggle to enable API token access.
3. Click the **Settings** tab, and then click **Add API token** to the right of **Active API Tokens**.
   The token is generated and displayed.
4. Enter an **API token** description.
5. Copy the generated API token.
6. Click **Save** to return to the API page.
7. Back in Axonius, paste the copied token in the API Key/Token field in the ZenDesk adapter connection form.

## Parameters

The parameters that you need to fill out will differ based on the capabilities in your Axonius platform. 'General' pertains to users with **Axonius Cyber Assets** and/or **Axonius SaaS Applications**.

### General

* **Sub Domain** *(required)* - The subdomain used to access Zendesk. For example, Axonius is the subdomain for *[https://axonius.zendesk.com/](https://axonius.zendesk.com/)*.

* **User Name** *(required)* - The username of an Axonius dedicated user account.

* **API Key/Token** *(required)* - An API Key/Token associated with a user account that has permissions to fetch assets.

* **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ZendeskNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ZendeskNew.png" />

### Axonius SaaS Applications

* **Password** - The password of the Axonius dedicated user account.
* **2FA Secret Key** - The secret generated in Zendesk for setting up two-factor authentication for the Zendesk user created to collect Axonius SaaS Applications data. See Zendesk documentation for instructions on [how to set up two-factor authentication (2FA) and generate the 2FA secret](https://support.zendesk.com/hc/en-us/articles/4408829277466-Using-2-factor-authentication).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

In **Advanced Settings**, at the top of the Advanced Configuration tab, you can choose asset types that are relevant to specific advanced configurations.

* From the dropdown, select one or more asset types.
* The relevant advanced configurations are displayed.
* Next to certain configurations, you can find a small info icon. Hover over the icon to see more information.
* The Advanced Configuration page is divided into sections, which can be collapsed to make it easier to navigate.

### Users Fetch Settings

* **Entities to fetch** - From the dropdown, select to fetch Users, All Tickets, or both Users and Tickets.

### Roles Fetch Settings

* **Roles to Filter by** - From the dropdown, select the users' roles to fetch. If no roles are selected, all roles are fetched.

### Tickets Settings

#### Tickets Fetch Settings

* **Entities to fetch** - From the dropdown, select to fetch Users, All Tickets, or both Users and Tickets.
* **Exclude Closed Tickets** - Select this option to filter out closed tickets from the data fetched by this adapter.

#### Tickets Parsing Settings

* **Use user email as ticket assignee** - Select this option to use the user email as the ticket assignee name.

#### Tickets General Settings

* **Enable real-time asset updates (Supported events: New Tickets)** - Select this option to update assets in real-time with New Tickets events.
* **Fetch EC Action ticket updates** - Select this option to configure the adapter to fetch updates on tickets created by Axonius users. The updated ticket information is displayed in the **Tickets** table showing information on all tickets in the system (**Assets> Tickets**) or on Tickets of a specific asset (in the **Asset Profile** of the relevant asset).

## APIs

Axonius uses the following APIs:

* [api/v2/users](https://developer.zendesk.com/api-reference/ticketing/users/users/)
* [api/v2/groups](https://developer.zendesk.com/api-reference/ticketing/groups/groups/)
* [api/v2/organizations](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/)
* [api/v2/organization\_memberships](https://developer.zendesk.com/api-reference/ticketing/organizations/organization_memberships/)
* [api/v2/organization\_subscriptions](https://developer.zendesk.com/api-reference/ticketing/organizations/organization_subscriptions/)
* [api/v2/group\_memberships](https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/)
* [api/v2/apps/installations](https://developer.zendesk.com/api-reference/ticketing/apps/app_location_installations/)

## Required Permissions

<Callout icon="📘" theme="info">
  Note

  While to access SaaS data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application. This applies to both the user account and the credentials associated with the API key.
</Callout>

## **Related Enforcement Actions**

[Zendesk - Create Ticket](/docs/create-zendesk-ticket) <br />
[Zendesk - Create Ticket Per Entity](/docs/zendesk-create-ticket-per-entity)<br />
[Update Zendesk Ticket](/docs/update-zendesk-tickets)<br />
[Zendesk - Create Custom Object per Asset](/docs/zendesk-create-custom-object-per-asset)<br />
[Zendesk - Assign Group to Users](/docs/assign-zendesk-group-to-user)<br />
[Zendesk - Create User](/docs/create-zendesk-user)<br />
[Zendesk - Delete User](/docs/delete-zendesk-user)<br />