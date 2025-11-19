# Source: https://docs.datafold.com/faq/data-monitoring-observability.md

# Data Monitoring and Observability

<Accordion title="How does Datafold compare to data observability tools?">
  Most data observability tools focus on monitoring metrics (e.g., null counts, row counts) in the data warehouse. But catching data quality issues in the data warehouse is usually too late: the bad data has already affected downstream processes and negatively impacted the business.

  Our platform focuses on prevention rather than detection of data quality issues. By [integrating deeply into your CI process](/deployment-testing/how-it-works), Datafold's [Data Diff](/data-diff/what-is-data-diff) helps data teams fix potential regressions during development and deployment, before bad code and data get into the production environment.

  Our [Data Monitors](/data-monitoring/monitor-types) make it easy to monitor production data to catch issues early before they are propagated through the warehouse to business stakeholders.

  This proactive data quality strategy not only enhances the reliability and accuracy of your data pipelines but also reduces the risk of disruptions and the need for reactive troubleshooting.
</Accordion>
