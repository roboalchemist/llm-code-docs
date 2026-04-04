# Source: https://docs.pentaho.com/pba/data-source-wizard-cp-overview/before-using-the-data-source-wizard.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-wizard-cp-overview/before-using-the-data-source-wizard.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-wizard-cp-overview/before-using-the-data-source-wizard.md

# Before using the Data Source Wizard

The Data Source Wizard is intended for prototyping or as a starting point for Pentaho Analysis and Pentaho Metadata models used with Interactive Reports, Analyzer reports, and dashboards. As a best practice, re-create or edit these models with the Schema Workbench or Metadata Editor to ensure query performance and to leverage enhanced features when used in production environments.

**CAUTION:**

Data sources created with the Data Source Wizard are not supported for use in a production environment.

Because of the following reasons, data sources created with the Data Source Wizard are not supported for use in a production environment:

* Data sources created with the Data Source Wizard cannot be secured using Pentaho roles, as per the security configuration.
* They are not optimized for performance.
* They may not conform to design best practices.
