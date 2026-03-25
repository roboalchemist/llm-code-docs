# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation.md

# Install

This article outlines the main procedures for installing, configuring, running, and managing Data Optimizer volumes in your Hitachi Content Platform, Cloudera Data Platform, and Cloudera’s Distribution of Hadoop clusters using the Data Optimizer plugins for Apache Ambari and for Cloudera Manager.

The terms used in the installation procedures are summarized in the following table:

<table><thead><tr><th width="216">Term</th><th>Description</th></tr></thead><tbody><tr><td>Object store</td><td>Refers interchangeably to either Hitachi Content Platform, Virtual Storage Platform One Object, or a Simple Storage Service (S3) object.</td></tr><tr><td>Hitachi Content Platform</td><td>Refers to the Hitachi Content Platform (Content Platform) 7.x or 8.x product line and is not Virtual Storage Platform One Object (VSP One Object).</td></tr><tr><td>Virtual Storage Platform One Object</td><td>Refers to Virtual Storage Platform One Object (VSP One Object) and is not the Hitachi Content Platform (Content Platform) 7.x or 8.x product line.</td></tr><tr><td>Hadoop</td><td>Refers to Apache Hadoop-based big data software and includes Apache Hadoop, Hortonworks Data Platform (HDP), Cloudera Distribution of Apache Hadoop (CDH), and Cloudera Data Platform (CDP).</td></tr><tr><td>HDFS</td><td>Hadoop Distributed File System is the distributed file system software that the Pentaho Data Optimizer file system is designed to integrate with. HDFS is a core component of Hadoop.</td></tr><tr><td>Cloudera Manager</td><td>The web interface for configuring and managing Cloudera clusters.</td></tr><tr><td>CDP</td><td>Cloudera Data Platform</td></tr><tr><td>CDH</td><td>Cloudera’s Distribution of Hadoop</td></tr><tr><td>Apache Ambari</td><td>The web interface for configuring and managing Hadoop clusters.</td></tr></tbody></table>

## Before you begin

Review these prerequisites before you start the installation.

This guide assumes that you have:

* Read through the entire installation documentation prior to performing the installation instructions on your system. You need to decide on your installation options prior to performing these procedures to ensure that your selected installation method is the best method for you.
* Verified the system requirements for either Apache Ambari or Cloudera are met.
* Uninstalled any evaluation version of Pentaho Data Optimizer.

You should understand the following concepts about the Data Optimizer installation before starting the process:

* **Audience**

  This document is intended for customers and partners who license and use Data Optimizer.
* **Requirements**

  The following table summarizes the requirements you need to get started.

<table><thead><tr><th width="240">Requirement</th><th>Details</th></tr></thead><tbody><tr><td>Pentaho Data Optimizer software</td><td>Download from the <a href="https://support.pentaho.com/hc/en-us">Support Portal</a>.</td></tr><tr><td>Environment</td><td><p>Includes:- Environment that meets the hardware and software requirements indicated in <a href="../../pdso-requirements#system-requirements">System requirements</a></p><ul><li>A supported operating system</li><li>Java Development Kit (JDK)</li></ul></td></tr><tr><td>PostgresSQL software</td><td>PostgresSQL is used for the repository to store transactional metadata for Data Catalog. You must supply, install, and configure PostgresSQL yourself.</td></tr></tbody></table>

\- \*\*Login Credentials\*\*

```
To begin the installation process, you need administrator access to Cloudera Manager or Apache Ambari. Linux users need root access.
```

## Pentaho Data Optimizer volume

The Pentaho Data Optimizer volume is the primary role type or component type that will be deployed to the Hadoop Datanodes. Whether deploying with Cloudera Manager to a Cloudera Data Platform (CDP) cluster or with Apache Ambari to a Hadoop Data Platform (HDP) cluster, it is the Data Optimizer volume that provides the capability for Data Nodes to tier to an object store.

A Data Optimizer volume is lightweight software that uses the Linux `libfuse` interface to create a mounted filesystem on a Hadoop node that looks like a local volume to the HDFS DataNode service. The Data Optimizer volume translates the local filesystem operations into S3 object storage operations. With a Data Optimizer volume, the HDFS datanode frees up critical local disk capacity by tiering the contents of infrequently accessed HDFS block replicas onto object storage.

## Planning your deployment

Prior to deploying Data Optimizer in your Hadoop cluster, work with your IT administrator to determine which HDFS datanodes will host the volumes. As a best practice, you should run more than three Data Optimizer volumes such as one volume instance for every datanode to achieve the best performance and most even distribution of tiered HDFS blocks across datanodes. However, it is not required to run Data Optimizer on all datanodes.

As a best practice, if you are deploying fewer Data Optimizer volumes than you have Data Nodes, distribute the Data Optimizer volumes evenly across the racks in your Hadoop cluster so that you can leverage rack locality.

**Note:** Ensure that the entire Hadoop cluster is running the same major OS version, and that it is a supported OS version for Data Optimizer.

## Security considerations

You can securely use Data Optimizer on a secure cluster even if you do not have direct Kerberos integration. Because Data Optimizer neither offers a service endpoint nor subscribes to service endpoints, it does not have to acquire or validate Kerberos tickets.

Data Optimizer supports version 1.2 and higher of the Transport Layer Security (TLS) protocol for secure data in flight encryption between the datanode and the object store. Data Optimizer only maintains user data at rest on the object store and on the datanode in a temporary cache for open files. Data Optimizer does not read or interpret user data in any way. Access to user data using a Data Optimizer volume instance on a datanode is secured by the Linux file system, in the same way that user data is secured on local disk volumes on the same datanode.

## Installing Data Optimizer on your cluster

Depending on the type of cluster, use the following instructions to install Data Optimizer:

* [Installing Pentaho Data Optimizer on an Apache Ambari Cluster](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster)
* [Installing Pentaho Data Optimizer on a Cloudera Manager cluster](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp)
