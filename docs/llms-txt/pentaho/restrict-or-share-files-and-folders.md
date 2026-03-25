# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/pentaho-server-security/restrict-or-share-files-and-folders.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/pentaho-server-security/restrict-or-share-files-and-folders.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/pentaho-server-security/restrict-or-share-files-and-folders.md

# Restrict or share files and folders

Access to files or folders can be refined using the Pentaho User Console. Each file or folder can either use the default permissions or you can tailor them for specific users and roles.

Prior to performing this task, you need to have determined whether you are going to use the default Pentaho roles, or created specific users and roles. You must also have successfully set up your security back end. Once you establish roles, you can share or restrict files and folders by role-type from the administration view within the User Console.

1. Log in to the User Console using the administrator role.
2. From the Browse Files page, choose the folder you want to set permissions on from the **Folders** pane.

   If you want to set permissions on a specific file within that folder, click to highlight the file in the center **Files** pane.
3. Click **Properties** in the **Actions** pane on the right.

   The Properties window appears.
4. On the **Share** tab, highlight the **Role** that you want to set permissions for, then clear the check box next to **Inherits folder permissions**.

   The **Permissions for \[Role]** field becomes accessible.
5. Select the permissions for that role using the check boxes and click **OK**.

The permissions are set for that file or folder and are associated with the selected role.

For additional security in multi-tenancy organizations, you can hide individual users' Home folders. See [Hiding user folders in PUC and PDI](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/pentaho-server-security/hiding-user-folders-in-puc-and-pdi-cp) for more information.
