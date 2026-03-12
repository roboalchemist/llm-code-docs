# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart.md

# Data Integration Operations Mart

The Data Integration Operations Mart is a centralized data mart that stores job or transformation log data for auditing, reporting, and analysis. You can use the Data Integration Operations Mart to collect and query Data Integration log data. Then use the Pentaho Server tools to examine the log data in reports, charts, and dashboards.

The data mart is a collection of tables organized as a data warehouse using a star schema. Together, the dimension tables and a fact table represent the logging data. These tables must be created in the Data Integration Operations Mart database. Pentaho provides SQL scripts to create these tables for the PostgreSQL database. A Data Integration job populates the time and date dimensions.

**Note:** For optimal performance, be sure to [clean the operations mart](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/clean-up-operations-mart-tables) periodically.

For instructions for installing and working with DI Ops Mart, see the following topics:

* [Setting up DI Operations Mart with an archive installation](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/setting-up-the-di-ops-mart-with-an-archive-installation-cp)
* [Setting up the DI Operations Mart with a manual installation](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/setting-up-the-di-operations-mart-with-a-manual-installation-cp)
* [Charts, reports, and dashboards using the DI Operations Mart data](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/charts-reports-and-dashboards-using-pdi-operations-mart-data)
* [Clean up DI Operations Mart tables](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/clean-up-operations-mart-tables)
