# Source: https://docs.datafold.com/faq/data-diffing.md

# Data Diffing

<AccordionGroup>
  <Accordion title="What’s a data diff?">
    A [data diff](/data-diff/what-is-data-diff) is a value-level comparison between two tables—used to identify critical changes to your data and guarantee data quality.

    Similar to how git diff highlights changes in code by comparing different versions of files to show what lines have been added, modified, or deleted, a data diff compares rows and columns in two tables to pinpoint specific data changes.
  </Accordion>

  <Accordion title="What types of data can Datafold compare?">
    Datafold can compare data in tables, views, and SQL queries in databases and data lakes.

    Datafold facilitates data diffing by supporting a wide range of basic data types across popular database systems like Snowflake, Databricks, BigQuery, Redshift, and PostgreSQL. Datafold can also diff data across legacy warehouses like Oracle, SQL Server, Teradata, IBM Netezza, MySQL, and more.
  </Accordion>

  <Accordion title="Can you data diff unstructured data?">
    No, Datafold cannot perform data diffs on unstructured data such as files. However, it supports diffing structured and semi-structured data in tabular formats, including `JSON` columns.
  </Accordion>

  <Accordion title="How should I compare numeric columns, especially those with floating-point values?">
    When comparing numerical columns or columns of the `FLOAT` type, it is beneficial to [set tolerance levels for differences](/data-diff/in-database-diffing/creating-a-new-data-diff#tolerance-for-floats) to avoid flagging inconsequential discrepancies. This practice ensures that only meaningful differences are highlighted, maintaining the focus on significant changes.
  </Accordion>

  <Accordion title="Can you explain how Datafold handles expected changes?">
    When a change is detected, Datafold highlights the differences in the App or through PR comments, allowing data engineers and other users to review, validate, and approve these changes during the CI process.
  </Accordion>

  <Accordion title="How does Datafold’s in-database diffing work?">
    When diffing data within the same physical database or data lake namespace, data diff compares data by executing various SQL queries in the target database. It uses several JOIN-type queries and various aggregate queries to provide detailed insights into differences at the row, value, and column levels, and to calculate differences in metrics and distributions.
  </Accordion>

  <Accordion title="How does Datafold’s cross-database diffing work?">
    Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.
  </Accordion>

  <Accordion title="Can I materialize diff results back to my database?">
    Yes, while the Datafold App UI provides advanced exploration of diff results, you can also materialize these results back to your database. This allows you to further investigate with SQL queries or maintain audit logs, providing flexibility in how you handle and review diff outcomes. Teams may additionally choose to download diff results as a CSV directly from the Datafold App to share with their team members.
  </Accordion>
</AccordionGroup>
