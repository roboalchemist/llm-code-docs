# Source: https://adempiere.gitbook.io/docs/introduction/system-administration/general-rules/security-1/roles-and-managing-data-access.md

# Roles and Managing Data Access

## User Level

The user level determines the extent of information the User has access to. The possible settings and limitations are shown in the table below. Organization access is controlled via the fields ***Access All Orgs***, ***Use User Org Access*** and through the **Org Access** tab in the **Role** window. Table access levels are set by the System Administrator but can be further restricted by Role in the **Role Data Access** window.

{% hint style="info" %}
Organizations are specified by name except for a special organization identified by the asterisk symbol (\*) which means All Organizations.
{% endhint %}

| Users with this Level... | Can update records from the ...                          | and can view tables with Access Level ...                                                   |
| ------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Client                   | Login Client and all Organizations (\*)                  | <p>All,<br>Client Only,<br>Client + Organization,<br>System + Client</p>                    |
| Client + Organization    | Login Client and all allowed Organizations, including \* | <p>All,<br>Client Only,<br>Organization,<br>Client + Organization</p><p>System + Client</p> |
| Organization             | Login Client and all allowed Organizations except \*     | <p>All,</p><p>Organization,<br>Client + Organization</p>                                    |
| System                   | System Client and Organization \*                        | <p>All,<br>System Only,<br>System + Client</p>                                              |
