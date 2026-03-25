# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/jackrabbit-repository-perfomance-tuning/jackrabbit-hangs-on-unused-data.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/jackrabbit-repository-perfomance-tuning/jackrabbit-hangs-on-unused-data.md

# Jackrabbit hangs on unused data

Jackrabbit Repository (JCR) often retains a lot of unused data if you perform migrations from the same repository multiple times. This leads to an increase in table sizes and slowdowns on the repository.

You can clean up this unused data in the JCR by enabling a system listener designed for this purpose. Cleaning up the JCR can only be done with no users logged into it, and the repository remains locked while the process is running.

1. Stop the Pentaho Server.
2. Locate the `pentaho-server/pentaho-solutions/scheduler-plugin` directory and open the `plugin.spring.xml` with any text editor.
3. Add the following listener bean:

   ```xml
   <bean id="repositoryCleanerSystemListener" class="org.pentaho.platform.plugin.services.repository.RepositoryCleanerSystemListener">  
   	<property name="gcEnabled" value="true"/>
   	<property name="execute" value="now"/>
   </bean>
   ```
4. Add a reference to the listener bean (`repositoryCleanerSystemListener`) as shown in the following list:

   ```
   <util:list id="schedulerLifecycleListenerList" list-class="java.util.ArrayList" value-type="org.pentaho.platform.api.engine.IPluginLifecycleListener">
    <ref bean="embeddedQuartzSystemListener"/>
    <ref bean="embeddedVersionCheckSystemListener"/>
    <ref bean="emailGroupLifecycleListener"/> 
    <ref bean="repositoryCleanerSystemListener"/>
   </util:list>
   ```
5. Save and close the `plugin.spring.xml` file and restart the Pentaho Server.

You can customize the settings for the `repositoryCleanerSystemListener` by editing these properties. It is best practice to clean up the Jackrabbit repository on a regular schedule.

| Property      | Description                                                                                                                                                                                                                                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **gcEnabled** | A Boolean flag that turns the listener On (`true`) or Off (`false`).                                                                                                                                                                                                                                                          |
| **execute**   | <p>You can choose to run the listener:- <strong><code>now</code></strong></p><p>runs once during server start-up</p><ul><li><strong><code>weekly</code></strong></li></ul><p>runs on the first day of each week (Sunday)</p><ul><li><strong><code>monthly</code></strong></li></ul><p>runs on the first day of each month</p> |
