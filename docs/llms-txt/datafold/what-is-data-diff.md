# Source: https://docs.datafold.com/data-diff/what-is-data-diff.md

# What's a Data Diff?

> A data diff is the value-level comparison between two tables, used to identify critical changes to your data and guarantee data quality.

When you **git diff** your code, you’re comparing two versions of your code files to see what has changed, such as lines added, removed, or modified. Similarly, a **data diff** compares two versions of a dataset or two databases to identify differences in individual cells in the data.

<img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9c6fdaf4be1e5f7ff097e35e236aad4c" alt="what's a data diff" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="images/data_diff/what_is_data_diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=729bba594d308250446243de02d4f99d 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a4db13429bfb4d5dff9c2d4c9b0fb488 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8e2907a41e5244333a7393d9ee5f4e48 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a98f715a31041441606278f26f2b9c7a 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=0f8f72e0eded067cf0258b1e06ab3aa1 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3ef6e9f7143d2a03512dc5b304cb0fb5 2500w" />

## Why do I need to diff data?

Just as diffing code and text is fundamental to software engineering and working with text documents, diffing data is essential to the data engineering workflow.

Why? In data engineering, both data and the code that processes it are constantly evolving. Without the ability to easily diff data, understanding and tracking data changes becomes challenging. This slows down the development process and makes it harder to ensure data quality.

There is a lot you can do with data diff:

* Test SQL code by comparing development or staging environment data to production
* Compare tables in source and target systems to identify discrepancies when migrating data between databases
* Detect value-level outliers, or unexpected changes, in data flowing through your ETL/ELT pipelines
* Verify that reports generated for regulatory compliance accurately reflect the underlying data by comparing report outputs with source data

## Why Datafold?

Data diffing is a fundamental capability in data engineering that every engineer should have access to.

Datafold's [Data Diff](https://www.datafold.com/data-diff) is a tool that compares datasets fast, within or across databases. Datafold offers an enterprise-ready solution for comparing datasets within or across databases at scale. It includes comprehensive, optimized, and automated diffing solutions, API access, and secure deployment options.

Here's how you can identify row-level discrepancies in Datafold:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=414ebe833488adcc05e8c6f196db307a" data-og-width="8271" width="8271" data-og-height="6306" height="6306" data-path="images/data-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ea5f6d9604a64fc668bcd6a05377dad7 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2033ff369770ceed8eb7c9aaf7040b3b 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=54b5f3618d3fb0b7a0f5b61d205e5803 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d324c0f4af625fc0dd044a3739aedaea 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6fd0a5f4f4551a5c258ed6b364438b5c 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8575823e25178f8407b3fae24672df6b 2500w" />
</Frame>

Datafold provides end-to-end solutions for automating testing, including column-level lineage, ML-based anomaly detection, and enterprise-scale infrastructure support. It caters to complex and production-ready scenarios, including:

* Automated and collaborative diffing and testing for data transformations in CI
* Data diffing informed by column-level lineage, and validation of code changes with visibility into BI applications
* Validating large data migrations or continuous replications with automated cross-database diffing capabilities

Here's a high-level overview of what Datafold offers:

|                                                        Feature Category                                                       |                     Datafold                     |
| :---------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------: |
|                      **Database Support**<br />*Databases that are supported for source-destination diff*                     | Any SQL database, inquire about specific support |
|                                    **Scale**<br />*Size of datasets supported for diffing*                                    | Unlimited with advanced performance optimization |
|               **Primary Key Data Type Support**<br />*Data types of primary keys that are supported for diffing*              |  Numerical, string, datetime, boolean, composite |
|                   **Data Types Diffing Support**<br />*Data types that are supported for per-column diffing*                  |                  All data types                  |
|               **Export Diff Results to Database**<br />*Materialize diffing results in your database of choice*               |           <Icon icon="square-check" />           |
|     **Value-level diffs**<br />*Investigate row-by-row column value differences between source and destination databases*     |     <Icon icon="square-check" /> (JSON & GUI)    |
|                **Diff UI**<br />*Explore diffs visually and easily share them with your team and stakeholders*                |           <Icon icon="square-check" />           |
|           **API Access**<br />*Automatically create diffs and receive results at scale using the Datafold REST API*           |           <Icon icon="square-check" />           |
| **Persisting Diff History**<br />*Persist the result history of diffs to know how your data and diffs have changed over time* |           <Icon icon="square-check" />           |
|                          **Scheduled Checks**<br />*Run scheduled diffs for a defined list of tables*                         |           <Icon icon="square-check" />           |
|      **Alerting**<br />*Receive automatic alerts about detected discrepancies between tables within or across databases*      |           <Icon icon="square-check" />           |
|                       **Security and Compliance**<br />*Run diffs in secure and compliant environments*                       |        HIPAA, SOC2 Type II, GDPR compliant       |
|            **Deployment Options**<br />*Deploy your diffs in secure environments that meet your security standards*           |     Multi-tenant SaaS or Single-tenant in VPC    |
|                **Support**<br />*Choose which channels offer the greatest support to your use cases and users*                |   Enterprise support from Datafold team members  |
|        **SLA**<br />*The types of SLAs that exist to guarantee your team can diff and interact with diffs as expected*        |    <Icon icon="square-check" /> (Coming soon)    |

## Three ways to learn more

If you're new to Datafold or data diffing, here are three easy ways to get started:

1. **Explore our CI integration guides**: See how Datafold fits into your continuous integration (CI) pipeline by checking out our guides for [No-Code](../deployment-testing/getting-started/universal/no-code), [API](../deployment-testing/getting-started/universal/api), or [dbt](../integrations/orchestrators) integrations.
2. **Try it yourself**: Use your own data with our [14-day free trial](https://app.datafold.com/) and experience Datafold in action.
3. **Book a demo**: Get a deeper technical understanding of how Datafold integrates with your company’s data infrastructure by [booking a demo](https://www.datafold.com/booktime) with our team.
