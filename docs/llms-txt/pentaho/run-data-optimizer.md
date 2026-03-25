# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-pentaho-data-optimizer-in-hadoop-cluster/run-data-optimizer.md

# Run Data Optimizer

As a best practice, it is recommended to run Data Optimizer as a service because `systemd` provides protection against the service stopping permanently due to unforeseen circumstances. If the Data Optimizer process stops unexpectedly, `systemd` immediately restarts the service. Also, by running as service, you can have Data Optimizer automatically start when your operating system starts.

How you run Data Optimizer as a service depends on whether you are using Ambari or Cloudera:

* [Running and stopping Data Optimizer in Ambari](#running-and-stopping-data-optimizer-in-ambari)
* [Running and stopping Data Optimizer in Cloudera](#running-and-stopping-data-optimizer-in-cloudera)

## Running and stopping Data Optimizer in Ambari

You can perform the following actions with Data Optimizer in Ambari:

### Start and stop Data Optimizer

When you are stopping services for a single host or for all hosts in the cluster, start the Data Optimizer volume component before the HDFS DataNode component and stop it after the HDFS DataNode component. Stopping the Data Optimizer volume while HDFS is running might lead to data availability issues or lead to transient HDFS volume failures. Starting HDFS when Data Optimizer is not running can negatively impact your operations.

If the DataNode is not put into maintenance mode, more blocks will be created to maintain the number of required replication copies. Set the DataNode to a maintenance state as described in [HDFS-7877](https://issues.apache.org/jira/browse/HDFS-7877) to avoid unnecessarily re-protecting a large number of blocks on a Data Optimizer volume when performing routine DataNode maintenance.

### Start and stop Data Optimizer volumes

Start Data Optimizer volumes before the HDFS DataNodes and stop them after stopping the HDFS DataNodes. This sequence ensures optimal operation and prevents potential data availability issues. Like most services and service roles, the Data Optimizer service and the Volume role include `start` and `stop` commands that you can access and execute in multiple ways through Ambari.

* **Service-wide actions**

  Use the **Start** and **Stop** actions on the Data Optimizer service to start and stop all volume instances associated with the service simultaneously.
* **Individual volume actions**

  Start and stop individual volume instances via the Hosts tab. Drill down into an individual host and select Start, Stop, or Restart from the action menu for the specific volume instance.

### Start and stop all services

The Data Optimizer Management Pack for Ambari includes a dependency definition indicating that the HDFS DataNode component depends on the Data Optimizer volume component. Due to this dependency, when using the cluster or host-level start, stop, and restart commands, Ambari ensures that HDFS is stopped before Data Optimizer and started after Data Optimizer.

As a result, safely use the cluster-level start and stop actions, as Ambari automatically manages the correct sequence for starting and stopping services, maintaining the integrity and availability of your data.

## Running and stopping Data Optimizer in Cloudera

You can perform the following actions with Data Optimizer in Cloudera:

### Start and stop Data Optimizer

When you are stopping services for a single host or for all hosts in the cluster, start the Data Optimizer volume component before the HDFS DataNode component and stop it after the HDFS DataNode component. Stopping the Data Optimizer volume while HDFS is running might lead to data availability issues or lead to transient HDFS volume failures. Starting HDFS when Data Optimizer is not running can negatively impact your operations.

If the DataNode is not put into maintenance mode, more blocks will be created to maintain the number of required replication copies. Set the DataNode to a maintenance state as described in [HDFS-7877](https://issues.apache.org/jira/browse/HDFS-7877) to avoid unnecessarily re-protecting a large number of blocks on a Data Optimizer volume when performing routine DataNode maintenance.

### Start and stop Data Optimizer volumes

Start Data Optimizer volumes before the HDFS DataNodes and stop them after stopping the HDFS DataNodes. This sequence ensures optimal operation and prevents potential data availability issues. Like most services and service roles, the Data Optimizer service and the Volume role include `start` and `stop` commands that you can access and execute in multiple ways through Cloudera Manager.

* **Service-wide actions**

  Use the **Start** and **Stop** actions on the Data Optimizer service to start and stop all volume instances associated with the service simultaneously.
* **Individual volume actions**

  Start and stop individual volume instances through the Hosts tab. Drill down into an individual host and select Start, Stop, or Restart from the action menu for the specific volume instance.

### Start and stop all services

You cannot use Cloudera Manager to define dependencies between services or to influence the order when stopping or starting all services or when performing rolling restarts. Cloudera Manager is unaware that HDFS depends on Data Optimizer and assumes that Data Optimizer (like most services) is dependent on HDFS. When using the cluster or host level `Start`, `Stop`, and `Restart` commands, HDFS will be stopped after Data Optimizer, and started before Data Optimizer. The cluster `Stop` command stops Data Optimizer volumes before it stops HDFS DataNodes.

The cluster **Start** command starts HDFS DataNodes before it starts Data Optimizer volumes. For this reason, always start the Data Optimizer service before using the cluster `Start` command.
