# Source: https://docs.pentaho.com/pba-report-designer/create-report-design-wizard-templates-cp/deploy-a-template-to-interactive-reports.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-report-design-wizard-templates-cp/deploy-a-template-to-interactive-reports.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-report-design-wizard-templates-cp/deploy-a-template-to-interactive-reports.md

# Deploy a template to Interactive Reports

Once you've created a template for Interactive Reports, you must follow the below process to deploy it to the Interactive Reports plugin.

1. Shut down the Pentaho Server if it is currently running.
2. Create an icon for your template, in PNG format, with the same name as the template file.

   The size of the icon doesn't matter; Interactive Reports will scale it to fit the correct dimensions. However, you can avoid unusual scaling issues by creating a square-shaped (equal width and height) graphic. If you'd like further guidance, take a look at the default template icons that Pentaho provides in the templates directory.
3. Copy the icon and the PRPT template files to the `/pentaho-solutions/system/pentaho-interactive-reporting/resources/templates/` directory.
4. Edit the `/pentaho-solutions/system/pentaho-interactive-reporting/resources/messages/messages.properties` file and add a new line for your template with the `template_` prefix, the name of your template file, and a friendly name for the template as you'd like it to appear in the Interactive Reports interface.

   As in the following example (given a template filename of`template_demo.prpt`):

   ```
   template_template_demo=Template Demo
   ```

Your template is now deployed to Pentaho Interactive Reports.
