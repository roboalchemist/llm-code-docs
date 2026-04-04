# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/sample-use-cases.md

# Sample use cases

Data lineage and impact analysis can be applicable in several ways.

* **As an ETL Developer:**
  * There are changes in my source system, such as fields which are added, deleted and renamed. What parts of my ETL processes need to adapt? (Impact Analysis)
  * I need additional information in my target system, such as for reports. What sources are can provide this additional information? (Data Lineage)
* **As a Data Steward:**
  * There is a need for auditability and transparency to determine where data is coming from. A global, company-wide, metadata repository needs data lineage information from different systems and applications, i.e. very fine-grained metadata.
  * What elements (fields, tables, etc.) in my ETL processes are never used? How many times is a specific element used in some or all of my ETL processes?
* **As a Report/Business User:**
  * Is my data accurate?
  * I want to find reports which include specific information from a source, such as a field. This process is "data discovery." For example, are there any data sources which include sales and gender? Are there any reports which include sales and zip codes?
* **As a Troubleshooting Operator:**
  * The numbers in the report are wrong (or supposed to be wrong). What processes (transformations, jobs) are involved to help me determine where these numbers are coming from?
  * A job or transformation did not finish successfully. What target tables and fields are affected which are used in the reports?
* **As an Administrator:**
  * For documentation and auditing purposes, I want to have a report on external sources and target fields, tables, and databases of my ETL processes. I need the data for a specific date and version.
  * To ensure compliance, I want to validate naming conventions of artifacts (fields, tables, etc.)
  * For integration into third-party data lineage tools, I want a flexible way of exporting the collected data lineage information.
