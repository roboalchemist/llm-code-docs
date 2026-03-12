# Source: https://docs.pentaho.com/pba-report-designer/create-report-design-wizard-templates-cp/set-the-default-interactive-reports-template.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-report-design-wizard-templates-cp/set-the-default-interactive-reports-template.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-report-design-wizard-templates-cp/set-the-default-interactive-reports-template.md

# Set the default Interactive Reports template

To change the default template for Interactive Reports, edit the `/pentaho-solutions/system/pentaho-interactive-reporting/settings.xml` file and change the value of the \<default-template> node. You do not have to provide a path to the template PRPT file - just the filename.

```
<!-- default template -->
<default-template>1_jade_1_left_aligned.prpt</default-template>
```
