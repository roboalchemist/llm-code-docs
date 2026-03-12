# Source: https://docs.pentaho.com/pba-aggregation-designer/glossary-of-terms.md

# Source: https://docs.pentaho.com/pba-aggregation-designer/9.3-aggregation-designer/glossary-of-terms.md

# Source: https://docs.pentaho.com/pba-aggregation-designer/10.2-aggregation-designer/glossary-of-terms.md

# Glossary of Terms

* **Aggregate**

  Definitions for aggregate tables that help optimize a cube; also, summarized data.
* **Aggregate Tables**

  Coexists with the base fact table, and contains pre-aggregated measures built from the fact table. It is registered in Mondrian's schema, so that Mondrian can choose whether to use the aggregate table rather than the fact table, if applicable for a particular query. For related information, see [Introduction to Aggregate Table](http://mondrian.pentaho.com/documentation/aggregate_tables.php).
* **Aggregation**

  The process of merging multiple data values into one value. For example, sales data collected daily can then be aggregated to the week level, the week data could be aggregated to the month level, and so on. The data can then be referred to as aggregate data. Aggregation and summarization are synonyms, as are aggregate data and summary data.
* **Data Definition Language (DDL)**

  Originally a subset of SQL, this language defines data structures, including rows, columns, tables, indexes, and database specifics such as file locations. DDL SQL statements are more a part of the database management system, and have large differences between SQL implementations. For related information, see [Data Definition Language](http://en.wikipedia.org/wiki/Data_Definition_Language).
* **Mondrian Schema**

  Defines a multi-dimensional database. A Mondrian schema contains a logical model, consisting of cubes, hierarchies, and members, and a mapping of this model onto a physical model. The logical model consists of the constructs used to write queries in the MDX language: cubes, dimensions, hierarchies, levels, and members. The physical model is the source of the data presented through the logical model. It is typically a star schema, which is a set of tables in a relational databases. For related information, see [How to Design a Mondrian Schema](http://mondrian.pentaho.com/documentation/schema.php).
* **Relational Online Analytic Processing (ROLAP)**

  An alternative to MOLAP (Multidimensional OLAP) technology. While both ROLAP and MOLAP analytic tools are designed to allow analysis of data through the use of a multidimensional data model, ROLAP differs significantly in that it does not require the pre-computation and storage of information. Instead, ROLAP tools access the data in a relational database and generate SQL queries to calculate information at the appropriate level when an end user requests it. With ROLAP, it is possible to create additional database tables (summary tables or aggregations) which summarize the data at any desired combination of dimensions. For related information, see [ROLAP Overview](http://en.wikipedia.org/wiki/ROLAP).
* **Snowflake Schema**

  A way of arranging tables in a relational database such that the entity relationship diagram resembles a snowflake in shape. At the center of the schema are fact tables which are connected to multiple dimension tables. Thus a snowflake simplifies to a star schema when relatively few dimensions are used. The star and snowflake schemas are most commonly found in data warehouses where the speed of data retrieval is more important than the speed of insertion. As such, these schemas are not normalized much, and are frequently left in third normal form or second normal form. For related information, see [Snowflake Schema](http://en.wikipedia.org/wiki/Snowflake_schema).
