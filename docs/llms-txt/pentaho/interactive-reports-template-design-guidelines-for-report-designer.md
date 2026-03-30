# Source: https://docs.pentaho.com/pba-report-designer/create-report-design-wizard-templates-cp/interactive-reports-template-design-guidelines-for-report-designer.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-report-design-wizard-templates-cp/interactive-reports-template-design-guidelines-for-report-designer.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-report-design-wizard-templates-cp/interactive-reports-template-design-guidelines-for-report-designer.md

# Interactive Reports template design guidelines

Interactive Reports are saved as `.prpti` files. Report Designer report files have a `.prpt` extension. In the User Console, Interactive Reports are displayed with a special icon that differentiates them from reports that are created in Report Designer.

If you want to create a new Interactive Reports template, you must create it in Report Designer and place the template in the Interactive Reports templates directory.

To create a new Interactive Reports template, you must use Report Designer to create a report with certain template-specific properties enabled. The resultant PRPT file is then deployed to the Interactive Reports plugin's template directory.

## Requirements

The **generated-content-marker** attribute in the wizard group is the flag that turns a normal report into a template. This attribute can only be applied to a band (group header, group footer, details header, details footer, details, or sub-band).

RDW will insert its auto-generated content into the first band with the **generated-content-marker** set to `true`. This applies to the group header, group footer, details header, details footer, and the details bands. In the event there are more groups defined in the Report Design Wizard than defined in the template, it repeats the last defined group header and footer in the template.

## Formatting inheritance

Formatting styles are inherited, so any formatting applied to a band will also be applied to the elements used within it. Formatting is applied in three ways and in the following order:

1. Through the template via band inheritance
2. Through query data where it is defined in Pentaho Metadata Editor
3. As defined by Interactive Reports users through the Interactive Reports interface

## Inheriting styles from the data query

The query-metadata section of the **Attributes** tab contains options that determine whether formatting styles can come from the data query and be applied to the detail header, details, or detail footer band. This must be set directly on the detail header, detail footer, or details band; and the **style-format** option must be set to true for it to work. You must also disable any individual formatting styles (`enable-style-*=true`) that you don’t want to come from the query.

## Padding and grid lines

Since the **Details** band is dynamically generated, you have to specify grid line and padding settings in the template definition. This is done through the wizard attribute group for the band that has the **generated-content-marker** enabled.

## Updating

A template is not just a set of initial defaults for a report - it is the basis for that report. So if a template is updated, completed reports that were based on that template will also change.

**Note:** Note: Report Design Wizard templates have the opposite behavior; when an RDW template is changed, none of the reports based on that template will be automatically be updated with those changes. Instead, you will have to edit each report, apply the new template, and save it.
