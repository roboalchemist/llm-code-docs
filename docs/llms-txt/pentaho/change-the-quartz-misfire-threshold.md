# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-the-quartz-misfire-threshold.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-quartz-misfire-threshold.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-quartz-misfire-threshold.md

# Change the Quartz misfire threshold

With Quartz, sometimes scheduled jobs, transformations, or reports might try to run several times when they are manually stopped and restarted, instead of running only once. This is typically caused by the **misfireThreshold** property in Quartz being set at too high of a number.

These steps show how to reset the **misfireThresholdto** a lower numerical value.

1. Stop the Pentaho Server.
2. Locate the `/pentaho-server/pentaho-solutions/system/scheduler-plugin/quartz` directory.
3. Open the `quartz.properties` file with any text editor.
4. Find the property shown below and change the default to a smaller number, such as `5000`. The default value represents the number of milliseconds.

   ```
   org.quartz.jobStore.misfireThreshold = 60000
   ```
5. Save and close the `quartz.properties` file.
6. Start the Pentaho Server.
