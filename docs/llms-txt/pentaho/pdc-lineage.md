# Source: https://docs.pentaho.com/pdc-use/pdc-lineage.md

# Lineage

Lineage in Pentaho Data Catalog helps you understand the complete journey of your data, from its origin to its final use in reports, dashboards, and downstream systems. It provides a visual representation of how data flows across tables, files, datasets, and reports, enabling users to trace relationships, validate data trust, and assess impact across the data landscape.

Lineage is a critical capability for:

* Data governance and audit readiness
* Regulatory compliance (such as GDPR, CCPA, or IFRS)
* Impact analysis during data model or schema changes
* Root cause analysis and troubleshooting

In Data Catalog, you can have two types of lineage views:

## **Data lineage**

With the Data Lineage view, you can visualize how structured and unstructured data assets are connected across systems. It displays the upstream sources and downstream consumers of a selected data resource, such as a table, file, or dataset, helping you understand how data is transformed and used throughout the organization. Data lineage helps you to:

* Trace data origin and usage paths
* Explore relationships between datasets, schemas, and files
* Validate data integrity and identify dependencies\
  To learn more, see [Data lineage](https://docs.pentaho.com/pdc-use/pdc-lineage/pdc-data-lineage-cp).

## **Report lineage**

Similar to [Data lineage](https://docs.pentaho.com/pdc-use/pdc-lineage/pdc-data-lineage-cp), the Report Lineage view focuses on business intelligence (BI) components, including reports, dashboards, datasets, and charts, from connected BI servers such as Tableau. It shows how reports are built from datasets, which in turn are derived from data entities, tables, or files. Report lineage helps you to:

* Understand the data flow into and within reports
* Support compliance and data privacy requirements
* Perform impact analysis before modifying source data\
  To learn more, see [Report lineage](https://docs.pentaho.com/pdc-use/pdc-lineage/pdc-report-lineage).
