# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/pentaho-big-data-and-hadoop.md

# Source: https://docs.pentaho.com/pdia-try-pdia/pentaho-big-data-and-hadoop.md

# Pentaho, big data, and Hadoop

The term big data applies to very large, complex, or dynamic datasets that need to be stored and managed over a long time. To derive benefits from big data, you need the ability to access, process, and analyze data as it is being created. However, the size and structure of big data makes it very inefficient to maintain and process it using traditional relational databases.

Big data solutions re-engineer the components of traditional databases, such as data storage, retrieval, query, processing, and massively scale them.

### In this topic

* [Big data overview](#big-data-overview)
* [About Hadoop](#about-hadoop)
* [Big data resources](#big-data-resources)

### Big data overview

Pentaho increases speed-of-thought analysis against even the largest of big data stores by focusing on the features that deliver performance.

* Instant access: Pentaho provides visual tools to make it easy to define the sets of data that are important to you for interactive analysis. These data sets and associated analytics can be easily shared with others, and as new business questions arise, new views of data can be defined for interactive analysis.
* High performance platform: Pentaho is built on a modern, lightweight, high performance platform. This platform fully leverages 64-bit, multi-core processors and large memory spaces to efficiently leverage the power of contemporary hardware.
* Extreme-scale, in-memory caching: Pentaho is unique in leveraging external data grid technologies, such as Infinispan and Memcached to load vast amounts of data into memory so that it is instantly available for speed-of-thought analysis.
* Federated data integration: Data can be extracted from multiple sources, including big data and traditional data stores, integrated together and then flowed directly into reports, without needing an enterprise data warehouse or data mart.

### About Hadoop

The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures.

A Hadoop platform consists of a Hadoop kernel, a [MapReduce](http://wiki.apache.org/hadoop/MapReduce) model, a distributed file system, and often a number of related projects—such as [Apache Hive](http://hive.apache.org/), [Apache HBase](http://hbase.apache.org/), and others.

A Hadoop Distributed File System, commonly referred to as HDFS, is a Java-based, distributed, scalable, and portable file system for the Hadoop framework.

### Big data resources

The following resources may help in understanding big data architecture and components:

* [Pentaho Big Data Analytics Center](http://www.pentahobigdata.com/resources)
* [Apache Hadoop project](http://hadoop.apache.org/) -- A project that contains libraries that allows for the distributed processing of large data sets across clusters of computers using simple programming models. There are several modules, including the [Hadoop Distributed File System (HDFS)](http://wiki.apache.org/hadoop/HDFS), which is a distributed file system that provides high-throughput access to application data and [Hadoop MapReduce](http://wiki.apache.org/hadoop/MapReduce), which is a key algorithm to distribute work around a cluster.
* [Avro](http://avro.apache.org/)—A data serialization system
* [HBase](http://hbase.apache.org/)—A scalable, distributed database that supports structured data storage for large tables
* [Hive](http://hive.apache.org/)—A data warehouse infrastructure that provides data summarization and on-demand querying
* [ZooKeeper](http://zookeeper.apache.org/)—A high-performance coordination service for distributed applications
* [MongoDB](http://www.mongodb.org/)— A NoSQL open source document-oriented database system developed and supported by 10gen
* [Splunk](http://www.splunk.com/) - A data collection, visualization and indexing engine for operational intelligence that is developed by Splunk, Inc.
* [CouchDB](http://couchdb.apache.org/)—A NoSQL open source document-oriented database system developed and supported by Apache
* [Sqoop](http://sqoop.apache.org/)—Software for transferring data between relational databases and Hadoop
* [Oozie](http://oozie.apache.org/)—A workflow scheduler system to manage Hadoop jobs
