# Source: https://docs.pentaho.com/pba-report-designer/create-report-design-wizard-templates-cp/deploy-a-template-to-report-design-wizard.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-report-design-wizard-templates-cp/deploy-a-template-to-report-design-wizard.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-report-design-wizard-templates-cp/deploy-a-template-to-report-design-wizard.md

# Deploy a template to Report Design Wizard

Once you have created a template for the Report Design Wizard, you must follow the below process to deploy it to the Report Design Wizard in Pentaho Report Designer (PRD) and Pentaho Data Integration (PDI).

1. Shut down Pentaho Report Designer and Pentaho Data Integration if either one of them is currently running.
2. Create an icon for your template, in PNG format, with the same name as the template file.

   The size of the icon does not matter since the PRD Wizard will scale it to fit the correct dimensions. However, you can avoid unusual scaling issues by creating a square-shaped (equal width and height) graphic. If you would like further guidance, take a look at the default template icons that Pentaho provides in the templates directory.
3. Copy the icon and the `.prpt` template files to the following directories:
   * `design-tools/report-designer/templates`
   * `design-tools/data-integration/plugins/spoon/agile-bi/templates`

Your template is now deployed to the Report Design Wizard and will be available when you next start Pentaho Report Designer or Pentaho Data Integration.
