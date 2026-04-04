# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/oracle/sample-data.md

# Source: https://docs.snowflake.com/en/user-guide/sample-data.md

# Sample data sets

Snowflake provides sample data sets, such as the industry-standard TPC-DS and TPC-H benchmarks, for evaluating and testing a broad range of Snowflake’s SQL support.

Sample data sets are provided in a database named SNOWFLAKE_SAMPLE_DATA that has been
[shared with your account](data-sharing-intro.md) from the Snowflake SFC_SAMPLES account.
If you do not see the database, you can create it yourself. Refer to [Use the sample database](sample-data-using.md).

The database contains a schema for each data set, with the sample data stored in the tables in each schema. The database and schemas
do not use any data storage so they do not incur storage charges for your account. You can execute queries on the tables in
these databases just as you would with any other databases in your account. Executing queries requires a running, current warehouse
for your session, which consumes credits.

**Next Topics:**

* [Use the sample database](sample-data-using.md)
* [Sample data: TPC-DS](sample-data-tpcds.md)
* [Sample data: TPC-H](sample-data-tpch.md)
* [Sample Data: OpenWeatherMap — *Deprecated*](sample-data-openweathermap.md)
