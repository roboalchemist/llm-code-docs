# Source: https://docs.axonius.com/docs/active-directory-advanced-settings.md

# Active Directory Advanced Settings 

<Callout icon="💡">
  Advanced settings can either apply to all connections for this adapter or to a specific connection. Refer to [Advanced Configuration for Adapters](https://docs.axonius.com/docs/advanced-configuration-for-adapters).
</Callout>

You can use **Advanced Configuration** settings to fine-tune how the Active Directory adapter fetches data.
These settings can be applied globally to all adapter connections, or customized for individual connections.

Per-connection customization is useful when you need multiple fetch cycles for the same data source, for example:

* A light, frequent fetch for quick updates.
* A less frequent, more resource-intensive fetch for deeper data collection.

<Callout icon="📘" theme="info">
  The default value for "Ignore Devices not seen in X hours" for this adapter is 2160 hours (fetch devices seen in last 90 days).
</Callout>

***

## Accessing Advanced Configuration

* Navigate to the **Adapters** page → search for `Active Directory` → click on the adapter tile.
* On the left menu, select **Advanced Configuration** under Advanced Settings.

***

## Advanced Configuration Parameters

### Settings field descriptions

1. **Enable IP Resolving** *(default: true)* - Select this option so that adapter will try to find the IP of the fetched AD entities using three entities (the DNS configured on the machine, the DNS supplied in the creds, and the AD DC itself). Otherwise this adapter will try to find the IP of the fetched AD entities using only AD DC itself.

2. **Max parallel DNS queries** *(default: 1000)* - This field limits the number of parallel DNS queries.

3. **Fetch Users Image** *(default: true)* - Select this option to fetch users images.

4. **Fetch Trusted Domains information** *(default: False)* - Select this option to fetch information about the domains that are trusted by the user/device domain. The data will be displayed in the **Domains & URLs** assets page.

5. **Enrich group members with SID for each group** - Select this option to enrich group members with their SID.

6. **Enrich group members with distinguished name for each group** - Select to fetch the distinguished names of group members.

7. **Get nested group membership for each user** *(default: true)* - Select this option to fetch the group membership for each user.

8. **Get the most recent lastLogon by connecting to all DCs** - By default, the "LastLogonTimestamp" value is replicated only once every 2 weeks in the domain, and the "LastLogon" value shows the value of the last logon per each Domain Controller. If this option is selected, Axonius will connect to each domain controller to pull the "LastLogon" value for each user, to show this value accurately in Axonius.

9. **LDAP pagination (entries per page)** *(default: 900)* - Set the number of  entities to fetch in each LDAP request.

10. **LDAP socket connection timeout (seconds)** *(default: 10)* - Set the maximum socket connection timeout.

11. **LDAP socket receive timeout (seconds)** *(default: 120)* -  Set the  maximum socket receive timeout.

12. **Devices to exclude by objectCategory** -
    * If supplied, all connections for this adapter will exclude devices with the specified AD objectCategory.
    * If not supplied, all connections for this adapter will not exclude any devices.
      This field allows you to add input in order to exclude devices that have a specific AD objectCategory.

13. **LDAP fields to exclude** - Specify a comma-separated list one or more LDAP fields to exclude from the data. For example, "employeeID, givenName". This will exclude both of these from the raw and parsed data from the adapter.
    * If supplied, all connections for this adapter will not fetch the specified LDAP fields. The specified fields will not be part of the assets data in Axonius.
    * If not supplied, all connections for this adapter will fetch all asset LDAP fields.

14. **Exclude ms-Msc-AdmPwd field** *(default: true)* -  This setting removes the ms-Msc-AdmPwd field from the raw data fetched by Axonius. Clear this setting to include this field. In order to completely prevent this field being fetched from the API, remove 'All Extended rights' from Active Directory permissions.

15. **Parse all LDAP attributes to basic view** -  Select to show all fields/values from the Advanced view in Basic view on the Device Profile page.

16. **Parse User Customized Attributes With Prefix** - Enter prefixes of custom AD fields you want mapped into Axonius fields in the Users asset page.

17. **Fetch Specops password expiration date** - Select whether to fetch the number of days left to password expiration from Specops for systems that manage passwords using Specops, and calculate a password expiration date.

18. **Use msDS-UserPasswordExpiryTimeComputed to calculate user password expiration time** - Select to calculate the 'User > Password Expiration Date' field using the Active Directory LDAP value of the "msDS-UserPasswordExpiryTimeComputed" attribute.

19. **Distinguish standalone managed service accounts as users** - Select to to fetch standalone managed service accounts as Users.

20. **Distinguish group managed service accounts as users** *(optional)* - Select to distinguish group Managed Service Accounts as users. When cleared, group Managed Service Accounts are considered devices.

21. **Fetch Bitlocker Recovery Password** - Select to fetch Bitlocker Recovery Password.

22. **Hostnames to resolve** - Add a semi-colon separated list to specify a list of hostnames that the AD adapter will resolve to a specific IP address once, and cache the resolution for subsequent usage of the hostname.

23. **Admin Groups** - Enter one or more  AD Groups to specify AD groups which consist of administrators (press Enter between groups). All the members of the specified groups will be marked as admin meaning “IsAdmin” attribute will be set to Yes. This list is in addition to the default  'Domain Admins' group.

24. **Parse patch information from AD memberof entries** - Select this option to parse the AD 'member of' field for entries beginning with 'Patch\_" to add that data to the 'AD Patch MemberOf Information' field.

25. **Parse user mail as specific field** - Select this option to parse the user mail as a specific field, and not an aggregated field. Use this field only after direction from Axonius support.

26. **Ignore inactive users that were not seen for the last X days** - Do not fetch users that are inactive (as defined by AD UserAccountControl), and have not been seen for the last x days. If the last seen date is unknown, the users are not ignored.

27. **Fetch Subnets from Sites** - Select this option to fetch data from Active Directory Sites.

28. **Custom hosts map** - A custom host map to use when advanced configurations are required, for instance SASL authentication. Each entry should be in the format of "ip:hostname", separated by a  semicolon ";".

29. **Username alternative parsing** - Select the value that will be displayed in the Username field in the Users table. You can choose between `displayName` and `userPrincipalName`. If no value is selected, the default Username value will be `sAMAccountName`.

30. **Fetch and Parse Group Customized Attributes** - Enter custom AD fields you want mapped into Axonius fields in the Groups asset page.

31. **Fetch Interactive Logon for Users** - Select this option to fetch the 'Is Interactive' field for the Users asset.

32. **Fetch Protect from accidental deletion information for Users** -  Select this option to fetch the 'Fetch Protect from accidental deletion information for Users' field for the Users asset. This field is boolean (True/False). This setting uses Powershell commands instead of LDAP, and requires to enable WinRM service in the hostname. **TCP port 9586** access is required.

33. **Fetch Permissions** - Select this option to fetch Permissions (of users and groups) as assets. This setting uses Powershell commands instead of LDAP, and requires to enable WinRM service in the hostname. **TCP port 9586** access is required.

34. **WinRM Port** *(default: 9586)* - Select a port to connect to WinRM, usually 9585 (http) or 9586 (https).

35. **WinRM Use SSL** - When port 9586 is used, enabling this setting is required.

36. **Fetch Contacts** - Enable to fetch contacts as AD users.
    <Callout icon="📘" theme="info">
      **WinRM Port** and **WinRM Use SSL** are only needed when enabling either of the “Fetch Interactive Logon for Users” or “Fetch Permissions” advanced settings , because both of them use WinRM to fetch data.
    </Callout>

<br />