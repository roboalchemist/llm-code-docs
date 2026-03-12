# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/move-pentaho-managed-data-sources-to-jndi.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/move-pentaho-managed-data-sources-to-jndi.md

# Move Pentaho managed data sources to JNDI

Most production BI environments have finely-tuned data sources for reporting and analysis. If you haven't done any data warehouse performance-tuning, you may want to consult [Mondrian performance tips](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips). for basic advice before proceeding.

Pentaho provides a Data Source Wizard in the Pentaho User Console that enables business users to develop rapid prototype data sources for interactive reporting and analysis. This is a great way to get off the ground quickly, but they are "quick and dirty" and not performant. For maximum performance, you should establish your own JNDI data connections at the Web application server level, and tune them for your database.

JNDI data sources can be configured for Pentaho client tools by adding connection details to the `~/.pentaho/simple-jndi/default.properties` file on Linux, or the `%userprofile%\.pentaho\simple-jndi\default.properties` file on Windows.
