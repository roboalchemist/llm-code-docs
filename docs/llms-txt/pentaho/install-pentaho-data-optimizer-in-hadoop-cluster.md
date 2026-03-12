# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-pentaho-data-optimizer-in-hadoop-cluster.md

# Install Pentaho Data Optimizer in Hadoop Cluster

Pentaho Data Optimizer is a File System in Userspace (FUSE) file system purpose-built for Hadoop Distributed File System (HDFS) DataNodes, to enable seamless HDFS data tiering to Hitachi Content Platform, Hitachi Content Platform for cloud scale, or Simple Storage Service (S3) object storage.

This guide covers the installation, configuration, and management of Data Optimizer, including best practices and troubleshooting techniques.

The terms used in the installation procedures are summarized in the following table:

<table><thead><tr><th width="228.4444580078125">Term</th><th>Description</th></tr></thead><tbody><tr><td>Object store</td><td>Refers interchangeably to either Hitachi Content Platform, Hitachi Content Platform for cloud scale, or a Simple Storage Service (S3) object.</td></tr><tr><td>Hitachi Content Platform</td><td>Refers to the Hitachi Content Platform (Content Platform) 7.x or 8.x product line and is not Hitachi Content Platform for cloud scale (HCP for cloud scale).</td></tr><tr><td>Hitachi Content Platform for cloud scale</td><td>Refers to Hitachi Content Platform for cloud scale (HCP for cloud scale) and is not the Hitachi Content Platform (Content Platform) 7.x or 8.x product line.</td></tr><tr><td>Hadoop</td><td>Refers to Apache Hadoop-based big data software and includes Apache Hadoop, Hortonworks Data Platform (HDP), Cloudera Distribution of Apache Hadoop (CDH), and Cloudera Data Platform (CDP).</td></tr><tr><td>HDFS</td><td>Hadoop Distributed File System is the distributed file system software that the Pentaho Data Optimizer file system is designed to integrate with. HDFS is a core component of Hadoop.</td></tr><tr><td>Cloudera Manager</td><td>The web interface for configuring and managing Cloudera clusters.</td></tr><tr><td>CDP</td><td>Cloudera Data Platform</td></tr><tr><td>CDH</td><td>Cloudera’s Distribution of Hadoop</td></tr><tr><td>Apache Ambari</td><td>The web interface for configuring and managing Hadoop clusters.</td></tr></tbody></table>

## Before you begin

Review these prerequisites before you start the installation. This guide assumes that you have:

* Read through the entire installation documentation before performing the installation instructions on the system. You must decide on the installation options before performing these procedures to ensure that the selected installation method is the best method for you.
* Verified the system requirements for either Apache Ambari or Cloudera are met.
* Uninstalled any evaluation version of Pentaho Data Optimizer.

You should understand the following concepts about the Data Optimizer installation before starting the process:

### **Audience**

This document is intended for customers and partners who license and use Data Optimizer.

### **Requirements**

The following table summarizes the requirements before you get started.

<table><thead><tr><th width="286.22216796875">Requirement</th><th>Details</th></tr></thead><tbody><tr><td>Pentaho Data Optimizer software</td><td>Download from the <a href="https://support.pentaho.com/hc/en-us">Support Portal</a>.</td></tr><tr><td>Environment</td><td><p>Includes: </p><ul><li>Environment that meets the hardware and software requirements indicated in <a href="components-reference">Components Reference</a>.</li><li>A supported operating system</li><li>Java Development Kit (JDK)</li></ul></td></tr></tbody></table>

### Login Credentials

To begin the installation process, you need administrator access to Cloudera Manager or Apache Ambari. Linux users need root access.

## Pentaho Data Optimizer volume

The Pentaho Data Optimizer volume is the primary role type or component type that will be deployed to the Hadoop Datanodes. Whether deploying with Cloudera Manager to a Cloudera Data Platform (CDP) cluster or with Apache Ambari to a Hadoop Data Platform (HDP) cluster, it is the Data Optimizer volume that gives the capability for Data Nodes to tier to an object store.

A Data Optimizer volume is lightweight software that uses the Linux `libfuse` interface to create a mounted filesystem on a Hadoop node that looks like a local volume to the HDFS DataNode service. The Data Optimizer volume translates the local filesystem operations into S3 object storage operations. With a Data Optimizer volume, the HDFS datanode frees up critical local disk capacity by tiering the contents of infrequently accessed HDFS block replicas onto object storage.

## Pentaho Data Optimizer policy runner

Pentaho Data Optimizer policy runner is a role that executes at scheduled intervals, as defined in the Data Optimizer configuration, to fetch migration jobs from the Pentaho Data Catalog system. It performs the migration or archiving of HDFS files and folders within the Hadoop cluster based on the scheduled jobs.

## Security considerations

You can securely use Data Optimizer on a secure cluster even if you do not have direct Kerberos integration. Because Data Optimizer neither offers a service endpoint nor subscribes to service endpoints, it does not have to acquire or validate Kerberos tickets.

Data Optimizer supports version 1.2 and later of the Transport Layer Security (TLS) protocol for secure data in flight encryption between the datanode and the object store. Data Optimizer only maintains user data at rest on the object store and on the datanode in a temporary cache for open files. Data Optimizer does not read or interpret user data in any way. Access to user data using a Data Optimizer volume instance on a datanode is secured by the Linux file system, in the same way that user data is secured on local disk volumes on the same datanode.
