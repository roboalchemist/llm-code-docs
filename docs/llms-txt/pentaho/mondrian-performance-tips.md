# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips.md

# Mondrian performance tips

This section contains advice and procedures for testing and improving Pentaho Analyzer (Mondrian) performance. There are two facets of Pentaho Analyzer performance to consider: query speed and execution speed.

Query speed is the amount of time it takes to retrieve data from your data warehouse or data mart, and execution speed is the amount of time it takes to manipulate or perform calculations with that data after it has been retrieved. With these two performance factors in mind, review the following outline of questions to ask during a typical performance-tuning process:

* Locate the performance problem. Does the problem involve query speed (retrieving a result set) or execution speed (calculations done client-side and in the Mondrian engine)? Most commonly, the performance problem is in your data structure, not the Analysis engine or client machine.
* If query speed is slow, you must reconsider your data warehouse design and implementation.
* If your data warehouse is soundly designed, are you using an analytic database to achieve maximum query performance?
* If execution speed is slow, you may need to do some tuning of the Mondrian or Pentaho Reporting engine.
* If high-cardinality dimensions are unavoidable, you may need to partition them and streamline your schema to support table partitioning.

For more information for improving Mondrian performance, see the following topics:&#x20;

* [Optimize your infrastructure](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips/optimize-your-infrastructure)
* [Optimize Pentaho Analyzer](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips/optimize-pentaho-analyzer)
* [PentahoAnalyzer configuration files](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips/pentahoanalyzer-configuration-files)
