# Source: https://docs.pentaho.com/pba-report-designer/create-report-design-wizard-templates-cp/report-design-wizard-template-design-guidelines.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-report-design-wizard-templates-cp/report-design-wizard-template-design-guidelines.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-report-design-wizard-templates-cp/report-design-wizard-template-design-guidelines.md

# Report Design Wizard template design guidelines

To create a new Report Design Wizard (RDW) template, you must use Report Designer to create a report with certain template-specific properties enabled. The resultant Pentaho Report Template file `.prpt` file is then deployed to the Report Designer or Pentaho Data Integration template directory.

## Requirements

The **generated-content-marker** attribute in the wizard group is the flag that turns a normal report into a template. This attribute can only be applied to a band (group header, group footer, details header, details footer, details, or sub-band).

RDW will insert its auto-generated content into the first band with the **generated-content-marker** set to `true`. This applies to the group header, group footer, details header, details footer, and the details bands. In the event there are more groups defined in the Report Design Wizard than defined in the template, it repeats the last defined group header and footer in the template.

## Formatting inheritance

Formatting styles are inherited, so any formatting applied to a band will also be applied to the elements used within it.

Formatting is applied in three ways and in the following order:

1. Through the template via band inheritance
2. Through query data where it is defined in Pentaho Metadata Editor
3. As defined by Interactive Reports users through the Interactive Reports interface

## Inheriting styles from the data query

The query-metadata section of the **Attributes** tab contains options that determine whether formatting styles can come from the data query and be applied to the detail header, details, or detail footer band. This must be set directly on the detail header, detail footer, or details band; and the **style-format** option must be set to true for it to work. You must also disable any individual formatting styles (`enable-style-*=true`) that you don’t want to come from the query.

## Padding and grid lines

Since the **Details** band is dynamically generated, you have to specify grid line and padding settings in the template definition. This is done through the wizard attribute group for the band that has the **generated-content-marker** enabled.

## Updating

An RDW template is only a set of initial defaults for a report, so if a template is updated, completed reports that were based on that template will not be affected; there is no connection between the template and the report once the report is saved. If you want to update an RDW-based report to reflect template changes, you can edit the report with Report Design Wizard, make any necessary selections, and re-save it.

**Note:** Pentaho Interactive Reports templates have the opposite behavior because the report links itself to the template; when an Interactive Reports template is changed, all reports based on that template will automatically inherit the updated template.<br>
