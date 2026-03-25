# Source: https://docs.axonius.com/docs/salesforce-advanced-settings.md

# Salesforce Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

Expand each of the following sections to view asset type-specific settings.

<Accordion title="Devices Fetch Settings" icon="fa-info-circle">
  * **Fetch nodes** - Select this option to enrich the Account devices field with data from the Opportunity and Contract tables. Axonius always tries to bring devices from the Axonius\_Environment\_\_c custom table. This setting is only supported for the Axonius\_Environment\_\_c table.
</Accordion>

<Accordion title="Users Fetch Settings" icon="fa-info-circle">
  * **Fetch chatter user data** - Select this option to fetch additional information about the chatter user platform.
    * **Fetch only active users** - Select this option to skip all inactive users and only fetch active users.
    * **Only fetch Employee users** - Select this option to fetch only "standard" Salesforce users.
    * **Fetch Tabs** - Select this option to fetch Salesforce tabs from the account.
</Accordion>

<Accordion title="Users Parse Settings" icon="fa-info-circle">
  * **Fetch nodes** - Select this option to enrich the Account devices field with data from the Opportunity and Contract tables. Axonius always tries to bring devices from the Axonius\_Environment\_\_c custom table. This setting is only supported for the Axonius\_Environment\_\_c table.
</Accordion>

<Accordion title="Group Fetch Settings" icon="fa-info-circle">
  * **Fetch user groups** - Select this option to fetch user group details.
</Accordion>

<Accordion title="Roles Fetch Settings" icon="fa-info-circle">
  * **Fetch user roles and permissions** - Select this option to fetch user roles and permissions configured for the Salesforce accounts in your organization.
</Accordion>

<Accordion title="Activities Fetch Settings" icon="fa-info-circle">
  * **Fetch Audit Events** -Eneable this setting to fetch audit events and show them on Axonius as Activities assets. When you select this option, the following settings are also available:
    * **Fetch Audit Events from the past X Days** - Select the number of days back from which to fetch Audit events.
    * Event types - Select the type of events to fetch (login, logout, API, Lightning URI, URI). Unselected event types will not be fetched at all.
</Accordion>

<Accordion title="Tickets Fetch Settings" icon="fa-info-circle">
  * **Fetch Tickets** *(default: off*) - Toggle on to fetch Cases from Salesforce as Tickets in Axonius. When you select this option, the following settings are also available:
    * **Fetch Tickets from the past X Days** *(default: 3)* - Select the number of days back from which to fetch tickets. Maximum 90 days back. Select **0** to fetch all tickets.
    * **Custom Fields to Fetch** *(optional)* - List of strings. Add custom fields here. The fields must exist on the Case object in your Salesforce. Example: `CustomField__c` .
    * **Additional WHERE clauses** *(optional)* - List of strings. Add additional WHERE clauses to filter the fetched tickets. Each clause is AND-ed to the others. You can nest clauses using parentheses.Examples:
      * IsClosed ≠ true
      * (Status = ‘New” OR Status = ‘Pending’)
</Accordion>

<Callout icon="📘" theme="info">
  Note:

  To learn more about Adapter Configuration tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings)
</Callout>