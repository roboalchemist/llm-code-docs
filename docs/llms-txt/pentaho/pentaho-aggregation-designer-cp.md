# Source: https://docs.pentaho.com/pba-aggregation-designer/9.3-aggregation-designer/pentaho-aggregation-designer-cp.md

# Source: https://docs.pentaho.com/pba-aggregation-designer/10.2-aggregation-designer/pentaho-aggregation-designer-cp.md

# Pentaho Aggregation Designer 10.2

The Pentaho Aggregation Designer simplifies the creation and deployment of aggregate tables that improve the performance of your Pentaho Analyzer (Mondrian) OLAP cubes.

Pentaho Analyzer is a pure, relational OLAP engine that works solely with the data stored in your relational database rather than providing its own multidimensional data storage model. This simplifies deployment and data management, but places limitations on performance when working with very large data sets (fact tables with more than 10 million records and/or cubes with a high cardinality of levels and members). To improve performance in these scenarios, Pentaho Analyzer supports aggregate tables. Aggregate tables coexist with the base fact table and contain pre-aggregated measures built from the fact table. This improves performance by enabling the Mondrian engine to fulfill certain summary level queries from the smaller aggregate table versus aggregating a large number of individual facts from the base fact table.

Pentaho Aggregation Designer provides you with a simple interface that allows you to create aggregate tables from levels within the dimensions you specify. Based on these selections, the Aggregation Designer generates the Data Definition Language (DDL) for creating the aggregate tables, the Data Manipulation Language (DML) for populating them, and an updated Mondrian schema which references the new aggregate tables. If you are unfamiliar with aggregate table design concepts, the Aggregation Designer also includes an intelligent adviser that evaluates the structure and cardinality of your OLAP cube and recommends some initial aggregate tables to create for improving performance.

For information about working with Pentaho Aggreation designer, see the following topics:&#x20;

* [Get started with the Pentaho Aggregation Designer](https://docs.pentaho.com/pba-aggregation-designer/10.2-aggregation-designer/get-started-with-the-pentaho-aggregation-designer)
* [Work with aggregate tables](https://docs.pentaho.com/pba-aggregation-designer/10.2-aggregation-designer/work-with-aggregate-tables)
* [Glossary of Terms](https://docs.pentaho.com/pba-aggregation-designer/10.2-aggregation-designer/glossary-of-terms)
