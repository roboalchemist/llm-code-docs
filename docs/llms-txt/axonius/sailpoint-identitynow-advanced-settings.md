# Source: https://docs.axonius.com/docs/sailpoint-identitynow-advanced-settings.md

# SailPoint IdentityNow Advanced Settings

The following advanced settings apply to the [SailPoint IdentityNow](https://docs.axonius.com/axonius-help-docs/docs/sailpoint-identity-now) adapter.

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Use alias as employee ID** - Select this option to set the alias field as the employee ID.
2. **List of private account attributes to include** *(optional)* - Enter a list of private attributes to include with the users. Leave the field empty to include none.
3. **Include All Attributes** - Select this option to parse all the attributes and ignore the **List of private account attributes to include** configuration list.
4. **Add Users Core Filters** - Select this option to fetch only users that satisfy the core filters. For more information, see "add-core-filters" in [Get a list of public identities](https://developer.sailpoint.com/docs/api/v3/get-public-identities/#get-a-list-of-public-identities) on the SailPoint website.
5. **Enrich Entitlements of Accounts and Access Profiles** *(only for accounts with Axonius Identities)* - Select this option to fetch entitlements of accounts and access profiles.
6. **Fetch Entitlements as Roles** *(only for accounts with Axonius Identities)* - Select this option to enrich users with the role permissions they are assigned in SailPoint.
7. **Exclude Campaigns with prefix** *(optional)* - Campaigns with the entered prefix will be excluded.
8. **Fetch Accounts** (only for accounts with Axonius Software Management) - When selected, the fetch will create users from accounts or enrich users with account information and will create User Extensions.
9. **Use Filters when fetching accounts** - Enable this option to set the following filters:
   1. **Fetch Accounts Created In Last X Days** - Enter a value for X.
   2. **Fetch Accounts Modified In Last X Days** - Enter a value for X.
   3. **Fetch Only Accounts That Have Entitlements**
      The fetch results will be filtered by what you define in this section.
10. **Fetch Sources** (only for accounts with Axonius Software Management) - When selected, the fetch will create accounts from sources,  fetch Applications, enrich users with sources data, and create User Extensions.
11. **Enrich Governance Groups With Connections** - Select this option to enrich the "List Governance Groups" endpoint with the “List Connections for Governance Group“ endpoint.
12. **Enrich Governance Groups With Members** - Select this option to enrich the "List Governance Groups" endpoint with the “List Governance Group Members“ endpoint.
13. **Use Username Value from Attributes** - Select to populate the Username and Email fields with values from the Attributes section.
14. **Use First and Last Name Values from Attributes** - Select to populate the First and Last Name with values from the Attributes section.
15. **Enable Custom Parsing** - Enable this option to define how to parse specific fields from the raw data fetched. You can choose to parse the data into an already existing field, or create a new one. This adapter supports **User Custom Parsing**. See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.