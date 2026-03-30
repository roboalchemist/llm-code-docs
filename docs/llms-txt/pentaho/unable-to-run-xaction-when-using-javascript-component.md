# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-server-issues/unable-to-run-xaction-when-using-javascript-component.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues/unable-to-run-xaction-when-using-javascript-component.md

# Unable to run XAction when using JavaScript component

Using the JavaScriptAction allows arbitrary JavaScript code to be executed within the Pentaho Server environment. It has, therefore, been decided the disable the JavaScriptAction by default. If you understand the risk of enabling the JavaScriptAction, it may be enabled by following the steps described below.

Perform the following steps to enable the JavaScript:

1. Stop the server, if it is running.
2. Navigate to `/tomcat/webapps/pentaho/WEB-INF/classes/org/pentaho/platform/engine/services/runtime`.
3. Open the `plugins.properties` file with any text editor.
4. Locate the following component names and remove the hash (#) at the beginning of each line:

   ```javascript
    # org.pentaho.component.JavascriptRule = !org.pentaho.platform.plugin.action.javascript.JavascriptRule

   ```

   ```javascript
   # JavascriptRule = org.pentaho.platform.plugin.action.javascript.JavascriptRule

   ```

   ```javascript
   # org.pentaho.plugin.javascript.JavascriptRule = !org.pentaho.platform.plugin.action.javascript.JavascriptRule

   ```
5. Save and close the file.
6. Restart the server.
