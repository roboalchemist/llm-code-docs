# Source: https://docs.snowflake.com/en/guides-overview-db.md

# Databases, Tables and Views - Overview

All data in Snowflake is maintained in databases. Each database consists of one or more schemas, which are logical groupings of database objects,
such as tables and views. Snowflake does not place any hard limits on the number of databases, schemas (within a database), or objects (within
a schema) you can create.

Use the following pages to learn about tables and table types, views, design considerations and other related content.

[Understanding Snowflake Table Structures](user-guide/tables-micro-partitions.md)
:   Introduction to *micro-partitions* and *data clustering*, two of the principal concepts utilized in Snowflake physical table structures.

[Temporary and Transient Tables](user-guide/tables-temp-transient.md)
:   Snowflake supports creating temporary tables for storing non-permanent, transitory data such as ETL data, session-specific
    or other short lived data.

[External Tables](user-guide/tables-external-intro.md)
:   Snowflake supports the concept of an external table. External tables are read-only, and their files are stored in an external stage.

[Hybrid Tables](user-guide/tables-hybrid.md)
:   Snowflake supports the concept of a hybrid table. Hybrid tables provide
    optimized performance for read and write operations in transactional and
    hybrid workloads.

[Apache Iceberg™ tables](user-guide/tables-iceberg.md)
:   Snowflake supports the Apache Iceberg™ open table format. Iceberg tables use data in external cloud
    storage and give you the option to use Snowflake as the Iceberg catalog, an external Iceberg catalog, or to create a table
    from files in object storage.

[Views](user-guide/views-introduction.md)
:   A view allows the result of a query to be accessed as if it were a table.
    Views serve a variety of purposes, including combining, segregating, and protecting data.

[Secure Views](user-guide/views-secure.md)
:   Snowflake supports the concept of a secure view. Secure views are specifically designed for data privacy.
    For example to limit access to sensitive data that should not be exposed to all users of the underlying table(s).

[Materialized Views](user-guide/views-materialized.md)
:   Materialized views are views precomputed from data derived from a query specification and stored for later use.
    Querying a materialized view is faster than executing a query against the base table of the view because the data is pre-computed.

[Table Design Best Practices](user-guide/table-considerations.md)
:   Best practices, general guidelines, and important considerations when designing and managing tables.

[Cloning Best Practices](user-guide/object-clone.md)
:   Best practices, general guidelines, and important considerations when cloning objects in Snowflake, particularly databases, schemas,
    and permanent tables.

[Data storage considerations](user-guide/tables-storage-considerations.md)
:   Best practices and guidelines for controlling data storage costs associated with Continuous Data Protection (CDP), particularly for tables.
