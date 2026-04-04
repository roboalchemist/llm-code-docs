# Source: https://docs.snowflake.com/en/guides-overview-privacy.md

# Privacy in Snowflake

Snowflake provides industry-leading features that maintain the privacy of individuals and sensitive data.

[Differential privacy](user-guide/diff-privacy/differential-privacy-overview.md)
:   Protect the identity and information of entities against targeted privacy attacks. Data providers assign privacy policies to tables and
    views to protect their data with differential privacy.

[Aggregation policies](user-guide/aggregation-policies.md)
:   Require queries to aggregate data in order to return results.

[Join policies](user-guide/join-policies.md)
:   Require queries to join tables in order to return results.

    [Preview Feature](release-notes/preview-features.md) — Open

    Available to all accounts that are Enterprise Edition (or higher).

    To inquire about upgrading, please contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

[Projection policies](user-guide/projection-policies.md)
:   Prevent queries from using a SELECT statement to project values from a column.

[Synthetic data](user-guide/synthetic-data.md)
:   Programmatically create realistic datasets that closely mirror your original data. This allows you to safely represent sensitive, confidential, or restricted information across various workloads, such as testing and validation.
