# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/hide-user-console-home-perspective-widgets.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/hide-user-console-home-perspective-widgets.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/hide-user-console-home-perspective-widgets.md

# Hide User Console Home perspective widgets

The User Console default Home perspective contains the Getting Started widget, which has easy instructions and tutorials for evaluators.

Perform the following steps to hide not only the Getting Started widget, but also other Home perspective widgets, as needed:

1. Shut down the Pentaho Server if it is currently running.
2. Choose one of the following options depending on your deployment status:
   * If you have not yet deployed, navigate to the `/pentaho-platform/user-console/source/org/pentaho/mantle/home/properties/config.properties` file.
   * If you have manually deployed and want to hide widgets later, navigate to the `/pentaho-server/tomcat/webapps/pentaho/mantle/home/properties/config.properties` file.
3. Find the line that starts with `disabled-widgets=` and type in the ID of the widget getting-started, as shown in the following example:

   ```xml
   disabled-widgets=getting-started,recents,favorites
   ```

   You can also hide the Recents and Favorites widgets using the same method, as shown here. Save and close the file.
4. Save and close the file.
5. Locate the `/pentaho-server/tomcat/webapps/pentaho/mantle/home` directory and open the `index.jsp` file with any text editor.
6. Find the following line of code and comment it out, then save and close the file.

   ```javascript
   <script language='JavaScript' type='text/javascript' src='http://admin.brightcove.com/js/BrightcoveExperiences.js'></script>
   ```
7. Start the Pentaho Server and log in to the User Console.

You now have a Home page without the specified widgets.
