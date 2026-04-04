# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/set-analyzer-report-options/set-default-report-options.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/set-analyzer-report-options/set-default-report-options.md

# Set default report options

As an administrator, you can add default report options that are applied whenever a new report is created. Adding default report options does not apply the changes to existing reports. You can modify the options on reports without affecting the default option settings. You can also set an existing report back to the default settings by clicking the **Reset to default** link on the **Other** tab of the **Report Options** dialog box.

Role permissions are as follows:

| Actions | Administrator | Power user | Business analyst (View-only) |
| ------- | ------------- | ---------- | ---------------------------- |
| Set     | X             |            |                              |
| Reset   | X             | X          |                              |
| Remove  | X             |            |                              |

Perform the following steps to set a default report option:

1. Open the report you want to modify.
2. Select the **More actions and options** button, then click **Report Options**.

   The **Report Options** dialog box displays.
3. Enter the new default options in the **Report Options** dialog box and select **Set as default for all reports**.

   The **Alert** dialog box displays and gives you the option of canceling your changes.
4. Click **OK** to apply your new defaults.

   The default options are set for new reports.

   **Note:** Default settings cannot be applied to the dimensions that are available on the **Drill-Through Columns** dialog box.
