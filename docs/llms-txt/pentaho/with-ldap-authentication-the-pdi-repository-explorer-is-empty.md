# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/security-issues/with-ldap-authentication-the-pdi-repository-explorer-is-empty.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues/with-ldap-authentication-the-pdi-repository-explorer-is-empty.md

# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/with-ldap-authentication-the-pdi-repository-explorer-is-empty.md

# With LDAP authentication, the PDI Repository Explorer is empty

If you log on to a solution repository from the PDI client before you switch authentication to LDAP, then the repository IDs and security structures will be broken. You will not see an error message, but the solution repository explorer will be empty and you will not be able to create new folders or save PDI content.

To fix the problem, you will have to delete the security settings established with the previously used authentication method, which will force the Pentaho Server to regenerate them for LDAP.

**Note:** Following this procedure will destroy any previously definedPentaho Repository users, roles, and access controls. You should back up the files that you delete in these instructions.

1. Stop the Pentaho Server.
2. Delete the security and default directories from the following directory: `/pentaho-solutions/system/jackrabbit/repository/workspaces/`
3. Start the Pentaho Server.

You should now have a proper LDAP-based Pentaho Repository that can store content and create new directories.
