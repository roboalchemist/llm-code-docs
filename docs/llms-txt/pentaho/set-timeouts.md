# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/set-timeouts.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/set-timeouts.md

# Set timeouts

To help you maintain the health of your Pentaho system, we provide tips to help you diagnose processing errors and monitor the Pentaho Server performance.

## Disable server and session-related timeouts to debug

Follow the instructions below to disable server and session timeouts associated with the User Console.

**Note:** These instructions are applicable when you are in a test environment. Once you go live, we recommend you set your timeouts to five or ten minutes so that sensitive Pentaho Server-related data can be protected. The time must be expressed in minutes.

1. Open the `server.xml` file located under: `pentaho-server/tomcat/conf`
2. Find the **connectionTimeout="20000"** parameter and change its value to: `0` (zero)

   If this value is set to a negative number it will never timeout.
3. Open the `web.xml` file, located under: `pentaho-server/tomcat/webapps/pentaho/WEB-INF/web.xml`
4. Find the **session-timeout** parameter and change its value to: `-1` (negative one)
5. Save the file and refresh the User Console.

## Define result row limit and timeout

When a query in the User Console returns an unusually large number of rows, this may impact server performance. To limit the number of rows returned by a query and to set up a timeout, you must create two custom properties, **max\_rows** and **timeout**, in the Metadata Editor.

The values you define for the row number limit (**max-rows**) and **timeout** properties are passed to the JDBC driver.

To define **max rows** and **timeout**:

1. In the Metadata Editor, expand the **Business Model** node and select **Orders**.
2. Right-click **Orders** and choose **Edit**.

   The Business Model Properties page displays a list of properties that were previously defined.
3. In the Business Model Properties page, click the **Add** icon.

   The Add New Property page dialog box appears.
4. Enable **Add a custom property**.
5. In the ID text box, type: `max_rows`

   **Important:** The ID is case-sensitive and must be typed exactly as shown.
6. Click the down-arrow in the **Type** field and choose: **Numeric**

   The Business Model Properties page appears. The **max\_rows** property is listed under **Custom** in the navigation tree.
7. In the right pane, under **Custom**, enter a value for your **max\_rows** property.

   If you enter `3000` as your value, the number of rows allowed to display in a query result is constrained to 3,000.
8. Repeat steps 3 through 6 to for the **timeout** custom property.
9. In the right pane, under **Custom**, enter a value for your **timeout** property.

   The timeout property requires a numeric value defined in number of seconds. For example, if you enter: `3600` the limit for query results is one minute.
10. Click **OK** in the Business Model Properties page to save your newly created properties.
