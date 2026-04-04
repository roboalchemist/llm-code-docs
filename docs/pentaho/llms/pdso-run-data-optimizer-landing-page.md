# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-run-data-optimizer-landing-page.md

# Run Data Optimizer

As a best practice, it is recommended to run Data Optimizer as a service because `systemd` provides protection against the service stopping permanently due to unforeseen circumstances. If the Data Optimizer process stops unexpectedly, `systemd` immediately restarts the service. Also, by running as service, you can have Data Optimizer automatically start when your operating system starts.

## Running and stopping Data Optimizer

How you run Data Optimizer as a service depends on whether you are using Ambari or Cloudera:

* Running and stopping Data Optimizer in Ambari
* Running and stopping Data Optimizer in Cloudera

### Running and stopping Data Optimizer in Ambari

Use the following best practices when starting and stopping Data Optimizer, its volumes, and other services.

#### Start and stop Data Optimizer <a href="#start-and-stop-data-optimizer" id="start-and-stop-data-optimizer"></a>

When you are stopping services for a single host or for all hosts in the cluster, as a best practice, always start the Data Optimizer volume component before the HDFS DataNode component and stop it after the HDFS DataNode component. Stopping the Data Optimizer volume while HDFS is running might lead to data availability issues or lead to transient HDFS volume failures. Starting HDFS when Data Optimizer is not running can negatively impact your operations.

If the DataNode is not put into maintenance mode, more blocks will be created to maintain the number of required replication copies. As a best practice, set the DataNode to a maintenance state as described in [HDFS-7877](https://issues.apache.org/jira/browse/HDFS-7877) to avoid unnecessarily re-protecting a large number of blocks on a Data Optimizer volume when performing routine DataNode maintenance.

#### Start and stop Data Optimizer volumes <a href="#start-and-stop-data-optimizer-volumes" id="start-and-stop-data-optimizer-volumes"></a>

As a best practice, always start Data Optimizer volumes before the HDFS DataNodes and stop them after stopping the HDFS DataNodes. This sequence ensures optimal operation and prevents potential data availability issues. Like most services and service roles, the Data Optimizer service and the Volume role include `start` and `stop` commands that you can access and execute in multiple ways through Ambari.

* **Service-wide actions**

  Use the **Start** and **Stop** actions on the Data Optimizer service to start and stop all volume instances associated with the service simultaneously.
* **Individual volume actions**

  Start and stop individual volume instances via the Hosts tab. Drill down into an individual host and select Start, Stop, or Restart from the action menu for the specific volume instance.

#### Start and stop all services <a href="#start-and-stop-all-services" id="start-and-stop-all-services"></a>

The Data Optimizer Management Pack for Ambari includes a dependency definition indicating that the HDFS DataNode component depends on the Data Optimizer volume component. Due to this dependency, when using the cluster or host-level start, stop, and restart commands, Ambari ensures that HDFS is stopped before Data Optimizer and started after Data Optimizer. This order adheres to the recommended best practices.

As a result, it is safe to use the cluster-level start and stop actions, as Ambari automatically manages the correct sequence for starting and stopping services, maintaining the integrity and availability of your data.

### Running and stopping Data Optimizer in Cloudera

Use the following best practices when starting or stopping Data Optimizer, its volumes, and other services in Cloudera.

#### Start and stop Data Optimizer <a href="#start-and-stop-data-optimizer" id="start-and-stop-data-optimizer"></a>

When you are stopping services for a single host or for all hosts in the cluster, as a best practice, always start the Data Optimizer volume component before the HDFS DataNode component and stop it after the HDFS DataNode component. Stopping the Data Optimizer volume while HDFS is running might lead to data availability issues or lead to transient HDFS volume failures. Starting HDFS when Data Optimizer is not running can negatively impact your operations.

If the DataNode is not put into maintenance mode, more blocks will be created to maintain the number of required replication copies. As a best practice, set the DataNode to a maintenance state as described in [HDFS-7877](https://issues.apache.org/jira/browse/HDFS-7877) to avoid unnecessarily re-protecting a large number of blocks on a Data Optimizer volume when performing routine DataNode maintenance.

#### Start and stop Data Optimizer volumes <a href="#start-and-stop-data-optimizer-volumes" id="start-and-stop-data-optimizer-volumes"></a>

As a best practice, always start Data Optimizer volumes before the HDFS DataNodes and stop them after stopping the HDFS DataNodes. This sequence ensures optimal operation and prevents potential data availability issues. Like most services and service roles, the Data Optimizer service and the Volume role include `start` and `stop` commands that you can access and execute in multiple ways through Cloudera Manager.

* **Service-wide actions**

  Use the **Start** and **Stop** actions on the Data Optimizer service to start and stop all volume instances associated with the service simultaneously.
* **Individual volume actions**

  Start and stop individual volume instances through the Hosts tab. Drill down into an individual host and select Start, Stop, or Restart from the action menu for the specific volume instance.

#### Start and stop all services <a href="#start-and-stop-all-services" id="start-and-stop-all-services"></a>

Cloudera Manager does not provide a way to define dependencies between services or to influence the order when stopping or starting all services or when performing rolling restarts. Cloudera Manager is unaware that HDFS depends on Data Optimizer and assumes that Data Optimizer (like most services) is dependent on HDFS. Because of this, when using the cluster or host level `Start`, `Stop`, and `Restart` commands, HDFS will be stopped after Data Optimizer, and started before Data Optimizer, which is not recommended. Be aware that the cluster `Stop` command stops Data Optimizer volumes before it stops HDFS DataNodes.

The cluster **Start** command starts HDFS DataNodes before it starts Data Optimizer volumes. For this reason, always start the Data Optimizer service before using the cluster `Start` command.

## Using automated data tiering

As an admin or user, you can use Data Optimizer to perform data tiering with the Hadoop Storage Policies feature. You can automatically move tagged files from active Hadoop nodes to cloud-backed archive locations, for example, S3-backed archive locations, resulting in space and potential cost savings.

### Workflow <a href="#workflow" id="workflow"></a>

1. Your Hadoop admin or user creates the policy in the JSON configuration file.
2. Using the command line, run Data Optimizer's Policy Manager command to parse the policy configuration file, which:
   1. Scans files in the path specified by the policy and filters files based on the designated retention time.
   2. Fetches files not accessed since the designated number of days.
   3. Tags filtered files with a storage policy (COLD, WARM, and HOT).
   4. Moves the targeted files from Hadoop nodes into Pentaho Data Optimizer (PDSO) volumes.

### Perform automated data tiering

Policy Manager is installed on all nodes where Data Optimizer is running. You can run the commands on HDFS data nodes where Data Optimizer volumes are mounted to automatically tier data and move files. Perform the following steps from the command line interface (CLI) at a location accessible to the server.

1. Run `$cd ‘/opt/ldo’` to go to the Policy Manager working folder.
2. Create a policy configuration file, enter a unique name for the file, and then create the policies using a JSON format.

   See the following example to make sure the syntax is correct.

   ```
   $vi <policy file>   
   {
       "policy1" : {                              #1st Policy
           "name": "policy1",                  #Name of policy
           "path": "/data/path/to/scan",   # Which path in HDFS to scan files
           "tag": "COLD",                      # what tag to put for file
           "retention": 180                # number of days since file is last accessed
       }
   }
   ```

   A `policiesconfig.json` file is created, which scans files in the specified path then tags those not accessed for 180 days as `COLD`.
3. Run the following Policy Manager entries as a Hadoop user:

   ```
   cd /opt/ldo
   python policy_app_runner <policy file> <database file name>
   ```

   Where `<*policy file*>` is the name of the policy created in the previous step, and `<*database file name*>` is the location where you want to place the files.
4. (Optional) You can also update step 3 to schedule a cron job to run in Policy Manager by opening `/opt/ldo/policy_manager.sh` and adding the `crontab -e` command.

   For example, you can then add the following code in an opened file to run Policy Manager and execute a cron job at 12:00 AM on every Saturday of every month.

   ```
   0 0 * * 6 /opt/ldo/policy_manager.sh
   ```

   **Note:** See [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) to add scheduling parameters that meet your specific needs.

Policy Manager scans the nodes, compares files, and then moves files tagged COLD into the specified Data Optimizer volume.
