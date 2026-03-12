# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/amazon-hive-job-executor/options-amazon-hive-job-executor/hive-settings-tab/cluster.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/amazon-emr-job-executor/options-amazon-emr-job-executor/emr-settings-tab/cluster.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/amazon-hive-job-executor/options-amazon-hive-job-executor/hive-settings-tab/cluster.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/amazon-emr-job-executor/options-amazon-emr-job-executor/emr-settings-tab/cluster.md

# Cluster

Select **New** if you want to create a new job flow (cluster), or **Existing** if you already have a job flow ID. Your job flow specifies all the functions you are trying to apply to your data. The ID identifies the job flow.

If you select **New**, use the following options to generate a new job flow:

| Option                   | Description                                                                                                                                                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EC2 role**             | Select the Amazon EC2 instance of the EMR role within your cluster. The processes that run on cluster instances use this role when they call other AWS services. The instances available in this list depend on your AWS account.                                                                                               |
| **EMR role**             | Select the role that permits Amazon EMR to call other AWS services such as Amazon EC2 on your behalf. See [https://docs.aws.amazon.com/emr/late...iam-roles.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html) for more information. The roles available in this list depend on your AWS account. |
| **Master instance type** | Select the Amazon EC2 instance type that will act as the Hadoop master in the cluster. This type will handle MapReduce task distribution.                                                                                                                                                                                       |
| **Slave instance type**  | Select the Amazon EC2 instance type that will act as one or more Hadoop slaves in the cluster. Slaves are assigned tasks from the master. This setup is only valid if the number of instances is greater than `1`.                                                                                                              |
| **EMR release**          | Select the EMR Hadoop cluster release version, which defines the set of service components and their versions.                                                                                                                                                                                                                  |
| **Number of instances**  | Specify the number of EC2 instances you want to assign to this job.                                                                                                                                                                                                                                                             |

If you select **Existing**, specify the existing ID through the **Existing JobFlow ID** option.
