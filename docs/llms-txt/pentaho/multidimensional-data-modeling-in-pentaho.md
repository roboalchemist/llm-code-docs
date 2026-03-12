# Source: https://docs.pentaho.com/install/multidimensional-data-modeling-in-pentaho.md

# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho.md

# Multidimensional Data Modeling in Pentaho

Pentaho Business Analytics is built on the Mondrian online analytical processing (OLAP) engine. OLAP relies on a multidimensional data model that, when queried, returns a dataset that resembles a grid. The rows and columns that describe and bring meaning to the data in that grid are dimensions, and the hard numerical values in each cell are the measures or facts. In Pentaho Analyzer, dimensions are shown in yellow and measures are in blue.

OLAP requires a properly prepared data source in the form of a star or snowflake schema that defines a logical multi-dimensional database and maps it to a physical database model. When you have the initial data structure in place, you must design a descriptive layer for it in the form of a Mondrian schema, which consists of one or more cubes, hierarchies, and members. Only when you have a tested and optimized Mondrian schema is the data prepared on a basic level for end-user tools like Pentaho Analyzer.

Pentaho also offers expanded functionality in Pentaho Analysis Enterprise Edition, including:

* The Pentaho Analyzer visualization tool.
* A pluggable Enterprise Cache with support for highly scalable, distributable cache implementations including Infinispan and Memcached.

A special Pentaho Server package must also be installed; this process is covered in the [Installation of the Pentaho design tools](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools) documentation.

All relevant configuration options for these features are covered in this section.
