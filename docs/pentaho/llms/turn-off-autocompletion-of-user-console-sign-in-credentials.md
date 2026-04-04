# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/turn-off-autocompletion-of-user-console-sign-in-credentials.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/turn-off-autocompletion-of-user-console-sign-in-credentials.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/turn-off-autocompletion-of-user-console-sign-in-credentials.md

# Turn off autocompletion of User Console sign-in credentials

The User Console's sign-in settings have autocomplete turned on by default.

Perform the following steps to manually turn off the autocompletion functionality:

1. Stop the Pentaho Server.
2. Navigate to the `/pentaho-server/tomcat/webapps/pentaho/jsp` directory and open the `PUCLogin.jsp` file with any text editor.
3. Find the following two sections of code and change the **autocomplete** entry to `off`, as shown:

   ```xml
   <input id="j_username" name="j_username" type="text" placeholder="" autocomplete="off">
   ```

   ```xml
   <input id="j_password" name="j_password" type="password" placeholder="" autocomplete="off">
   ```
4. Save and close the `PUCLogin.jsp` file.
5. Restart the Pentaho Server.

Autocompletion of usernames and passwords is now turned off for the User Console sign-in screen.
