# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/activate-view-only-mode-for-interactive-reports.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/activate-view-only-mode-for-interactive-reports.md

# Activate view-only mode for Interactive reports

In the Pentaho User Console, you can create a view-only user that does not have access to edit Interactive reports. This requires you to remove the edit icon in the report view for view-only users.

Perform the following steps to remove the edit icon:

1. Stop the Pentaho Server.
2. Locate the `server\pentaho-solutions\system` directory.
3. Open the `Pentaho.xml` file with any text editor.
4. Locate the `<edit-permission>` tag and uncomment the following line:

   ```
   <edit-permission>org.pentaho.repository.create</edit-permission>
   ```
5. Save and close the `Pentaho.xml` file.
6. Start the Pentaho Server.
