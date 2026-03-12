# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-11-13-data-classification.md

# Nov 13, 2025: Excluding objects from sensitive data classification (*General availability*)

By default, Snowflake automatically classifies all sensitive data in a database that has a classification profile set on it. You can now
configure Snowflake to exclude schemas, tables, or columns from automatic classification so that they are skipped during the classification
process.

For more information, see [Excluding data from sensitive data classification](../../../user-guide/classify-auto-exclude.md).
