# Source: https://docs.pentaho.com/install/9.3-install/getting-started-with-pentaho-data-integration-and-analytics-installation-cp.md

# Getting started with Pentaho Data Integration and Analytics installation

Setting up Pentaho Data Integration and Analytics includes installation, configuration, and if necessary, upgrading to a current version. In addition, you may need to refine your Pentaho relational metadata and multidimensional Mondrian data models. or understand how to work with big data.

## Setting up your Pentaho Data Integration and Analytics installation

These sections are helpful in setting up your production version of the Pentaho Data Integration and Analytics installation.

* [Installation and Deployment](https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp)

  Choose between three production methods of installing based on how you want to use the Pentaho products. You can install individual components and tools. You can install the Pentaho Server and optionally a separate database in different locations. You can also deploy your installations through a Docker container.
* [Configuration](https://docs.pentaho.com/install/9.3-install/pentaho-configuration)

  As an IT administrator, configure the Pentaho Server and define what security to use. As a Pentaho administrator, configure data connections, manage the Pentaho Server, and set up the Business Analytics (BA) or Pentaho Data Integration (PDI) design tools.
* [Upgrade](https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp)

  If you installed a previous release of the Pentaho Server in a different location from the database or tools, follow the instructions in this section to upgrade to a current version.

## Data Modeling

Pentaho data modeling includes:

* [Multidimensional Modeling](https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho)

  Pentaho Analyzer and Report Designer are built on the Mondrian online analytical processing (OLAP) engine, which relies on a multidimensional data model.
* [Relational Modeling](https://docs.pentaho.com/install/9.3-install/relational-data-modeling-in-pentaho)

  A Pentaho relational data model maps the physical structure of your database into a logical business model.

## Big Data

Pentaho supports Hadoop and Spark for the entire big data analytics process from big data aggregation, preparation, and integration to interactive visualization, analysis, and prediction.

* [Hadoop](https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho)

  Pentaho Data Integration (PDI) can execute both outside of a Hadoop cluster and within the nodes of a Hadoop cluster.
* [Spark](https://docs.pentaho.com/install/9.3-install/using-spark-submit-cp)

  PDI can execute Spark jobs through a Spark Submit entry or the Adaptive Execution Layer (AEL).
