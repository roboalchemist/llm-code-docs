# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/add-logos-to-interactive-reports/add-a-custom-logo-to-an-interactive-report-template.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/add-logos-to-interactive-reports/add-a-custom-logo-to-an-interactive-report-template.md

# Add a custom logo to an interactive report template

Use the following procedure to add a custom logo to an interactive report.

Prepare a custom logo in PNG format.

1. From User Console **Home**, click **Create New**, then **Interactive Report**.
2. From the **Select Data Source** dialog box, choose a data source for the report, and then click **OK**.
3. Click the **General** tab, then click **Select**.

   A window displaying available templates appears.
4. Browse through the available templates and click a template with a red "Change ME" logo.

   Interactive report templates are stored in the following folder:

   ```
   <server_installation_folder> > pentaho-server > pentaho-solutions > system > pentaho-interactive-reporting > resources > templates
   ```
5. To replace the default logo with a logo of your choice, go to the `images` folder:

   ```
   <server_installation_folder> > pentaho-server > pentaho-solutions > system > pentaho-interactive-reporting > resources > images > pentaho > <tenantId>
   ```
6. Rename the `Logo.png` image file, which contains the default logo, to another name, such as `Logo-orig.png`.

   Optionally, the original file can be deleted.
7. Rename your new logo image file to `Logo.png`.
8. Refresh the template to check that the new logo appears correctly.

Your custom logo has been been added to the selected template. To change the logo's alignment on the page, see [Change logo alignment](https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/add-logos-to-interactive-reports/change-logo-alignment).
