# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/access-the-repository-explorer-window.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/access-the-repository-explorer-window.md

# Access the Repository Explorer window

To access the Repository Explorer window, perform the following steps:

1. Connect to a repository. To learn how to do this, see [Use a Pentaho Repository in PDI](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi).
2. Select **Tools** > **Repository** > **Explore**.
3. The Repository Explorer window appears.

   **Note:** Permissions set by your administrator determine what you are able to view and tasks you are able to perform in the repository.

   ![Repository Explorer window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f2cd0270b2d8c01b140f8f6cdddc4a167f3c8461%2FRepositoryExplorerWindow.png?alt=media)

   **Note:** If you are trying to use LDAP authentication security and the Repository Explorer is empty when it opens, your [security settings need to be updated to the LDAP authentication](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference).

### With LDAP authentication, the PDI Repository Explorer is empty

If you log on to a solution repository from the PDI client before you switch authentication to LDAP, then the repository IDs and security structures will be broken. You will not see an error message, but the solution repository explorer will be empty and you will not be able to create new folders or save PDI content.

To fix the problem, you will have to delete the security settings established with the previously used authentication method, which will force the Pentaho Server to regenerate them for LDAP.

**Note:** Following this procedure will destroy any previously definedPentaho Repository users, roles, and access controls. You should back up the files that you delete in these instructions.

1. Stop the Pentaho Server.
2. Delete the security and default directories from the following directory: `/pentaho-solutions/system/jackrabbit/repository/workspaces/`
3. Start the Pentaho Server.

You should now have a proper LDAP-based Pentaho Repository that can store content and create new directories.
