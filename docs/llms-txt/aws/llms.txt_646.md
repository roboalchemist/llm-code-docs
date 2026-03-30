# Source: https://docs.aws.amazon.com/parallelcluster/v2/ug/llms.txt

# AWS ParallelCluster AWS ParallelCluster User Guide (v2)

- [What is AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/what-is-aws-parallelcluster.html)
- [Troubleshooting](https://docs.aws.amazon.com/parallelcluster/v2/ug/troubleshooting.html)
- [AWS ParallelCluster support policy](https://docs.aws.amazon.com/parallelcluster/v2/ug/support-policy.html)
- [Release notes and document history](https://docs.aws.amazon.com/parallelcluster/v2/ug/document_history.html)

## [Setting up AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/getting_started.html)

### [Installing AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/install.html)

Install AWS ParallelCluster on your system.

- [Virtual environment](https://docs.aws.amazon.com/parallelcluster/v2/ug/install-virtualenv.html): Install AWS ParallelCluster in a Python virtual environment.

### [Linux](https://docs.aws.amazon.com/parallelcluster/v2/ug/install-linux.html)

Install AWS ParallelCluster on Linux.

- [Python](https://docs.aws.amazon.com/parallelcluster/v2/ug/install-linux-python.html): Install Python on Linux with a package manager.
- [macOS](https://docs.aws.amazon.com/parallelcluster/v2/ug/install-macos.html): Install AWS ParallelCluster on macOS.
- [Windows](https://docs.aws.amazon.com/parallelcluster/v2/ug/install-windows.html): Install AWS ParallelCluster on Windows.
- [Configuring AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/getting-started-configuring-parallelcluster.html): After you install AWS ParallelCluster, complete the following configuration steps.
- [Best practices](https://docs.aws.amazon.com/parallelcluster/v2/ug/best-practices.html)
- [Moving from CfnCluster to AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/moving-from-cfncluster-to-aws-parallelcluster.html): AWS ParallelCluster is an enhanced version of CfnCluster.
- [Supported Regions](https://docs.aws.amazon.com/parallelcluster/v2/ug/supported-regions.html): AWS ParallelCluster version 2.x is available in the following AWS Regions:


## [Using AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/working.html)

- [Network configurations](https://docs.aws.amazon.com/parallelcluster/v2/ug/networking.html): AWS ParallelCluster uses Amazon Virtual Private Cloud (VPC) for networking.
- [Custom Bootstrap Actions](https://docs.aws.amazon.com/parallelcluster/v2/ug/pre_post_install.html): AWS ParallelCluster can run arbitrary code either before (pre-install) or after (post-install) the main bootstrap action when the cluster is created.
- [Working with Amazon S3](https://docs.aws.amazon.com/parallelcluster/v2/ug/s3_resources.html): To provide cluster resources permission to access to Amazon S3 buckets, specify the bucket ARNs in the and parameters in the AWS ParallelCluster configuration.
- [Working with Spot Instances](https://docs.aws.amazon.com/parallelcluster/v2/ug/spot.html): AWS ParallelCluster uses Spot Instances if the cluster configuration has set = spot.
- [AWS Identity and Access Management roles in AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/iam.html): AWS ParallelCluster uses AWS Identity and Access Management (IAM) roles for Amazon EC2 to enable instances to access AWS services for the deployment and operation of a cluster.

### [Schedulers supported by AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/schedulers.html)

Schedulers supported by AWS ParallelCluster include AWS Batch, Slurm Workload Manager, Son of Grid Engine, and Torque Resource Manager.

- [Son of Grid Engine](https://docs.aws.amazon.com/parallelcluster/v2/ug/schedulers.sge.html)

### [Slurm Workload Manager](https://docs.aws.amazon.com/parallelcluster/v2/ug/schedulers.slurm.html)

AWS ParallelCluster version 2.11.9 uses Slurm 20.11.9.

- [Multiple queue mode](https://docs.aws.amazon.com/parallelcluster/v2/ug/queue-mode.html): AWS ParallelCluster version 2.9.0 introduced multiple queue mode.
- [Slurm guide for multiple queue mode](https://docs.aws.amazon.com/parallelcluster/v2/ug/multiple-queue-mode-slurm-user-guide.html): AWS ParallelCluster version 2.9.0 introduced multiple queue mode and a new scaling architecture for Slurm Workload Manager (Slurm).
- [Torque Resource Manager](https://docs.aws.amazon.com/parallelcluster/v2/ug/schedulers.torque.html)

### [AWS Batch](https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli.html)

For information about AWS Batch, see AWS Batch.

- [awsbsub](https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli.awsbsub.html): Submits jobs to the job queue of the cluster.
- [awsbstat](https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli.awsbstat.html): Shows the jobs that are submitted in the clusterâs job queue.
- [awsbout](https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli_awsbout.html): Shows the output of a given job.
- [awsbkill](https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli_awsbkill.html): Cancels or terminates jobs submitted in the cluster.
- [awsbqueues](https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli_awsbqueues.html): Shows the job queue that is associated with the cluster.
- [awsbhosts](https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli_awsbhosts.html): Shows the hosts that belong to the clusterâs compute environment.
- [Tagging](https://docs.aws.amazon.com/parallelcluster/v2/ug/resources-tags.html): AWS ParallelCluster resource tags.
- [Amazon CloudWatch dashboard](https://docs.aws.amazon.com/parallelcluster/v2/ug/cloudwatch-dashboard.html): AWS ParallelCluster creates an Amazon CloudWatch dashboard when the cluster is created.
- [Integration with Amazon CloudWatch Logs](https://docs.aws.amazon.com/parallelcluster/v2/ug/cloudwatch-logs.html): Starting with AWS ParallelCluster version 2.6.0, common logs are stored in CloudWatch Logs by default.
- [Elastic Fabric Adapter](https://docs.aws.amazon.com/parallelcluster/v2/ug/efa.html): Elastic Fabric Adapter (EFA) is a network device that has OS-bypass capabilities for low-latency network communications with other instances on the same subnet.
- [Intel Select Solutions](https://docs.aws.amazon.com/parallelcluster/v2/ug/intel-select-solutions.html): AWS ParallelCluster is available as an Intel Select Solution for simulation and modeling.
- [Enable Intel MPI](https://docs.aws.amazon.com/parallelcluster/v2/ug/intelmpi.html): Intel MPI is an implementation of the MPI-3.0 specification optimized for Intel processors.
- [Intel HPC Platform Specification](https://docs.aws.amazon.com/parallelcluster/v2/ug/intel-hpc-platform-specification.html): The Intel HPC Platform Specification provides a set of compute, fabric, memory, storage, and software requirements to help achieve a high standard of quality and compatibility with HPC workloads.
- [Arm Performance Libraries](https://docs.aws.amazon.com/parallelcluster/v2/ug/arm-performance-libraries.html): The Arm Performance Libraries provides optimized standard core math libraries for high-performance computing applications on Arm processors.
- [Connect to the head node through Amazon DCV](https://docs.aws.amazon.com/parallelcluster/v2/ug/dcv.html): Amazon DCV is a remote visualization technology that enables users to securely connect to graphic-intensive 3D applications that are hosted on a remote high-performance server.
- [Using pcluster update](https://docs.aws.amazon.com/parallelcluster/v2/ug/using-pcluster-update.html): Starting with AWS ParallelCluster version 2.8.0, analyzes the settings used to create the current cluster and the settings in the configuration file for issues.
- [AMI patching and EC2 instance replacement](https://docs.aws.amazon.com/parallelcluster/v2/ug/instance-updates-ami-patch.html): To ensure that all dynamically launched cluster compute nodes behave in a consistent manner, AWS ParallelCluster disables cluster instance automatic OS updates.


## [AWS ParallelCluster CLI commands](https://docs.aws.amazon.com/parallelcluster/v2/ug/commands.html)

### [pcluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.html)

pcluster is the primary AWS ParallelCluster CLI command.

- [pcluster configure](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.configure.html): Begins an AWS ParallelCluster configuration.
- [pcluster create](https://docs.aws.amazon.com/parallelcluster/v2/ug/pluster.create.html): Creates a new cluster.
- [pcluster createami](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.createami.html): (Linux/macOS) Creates a custom AMI to use with AWS ParallelCluster.
- [pcluster dcv](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.dcv.html): Interacts with the Amazon DCV server running on the head node.
- [pcluster delete](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.delete.html): Deletes a cluster.
- [pcluster instances](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.instances.html): Displays a list of all instances in a cluster.
- [pcluster list](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.list.html): Displays a list of stacks that are associated with AWS ParallelCluster.
- [pcluster ssh](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.ssh.html): Runs an ssh command with the user name and IP address of the cluster pre-populated.
- [pcluster start](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.start.html): Starts the compute fleet for a cluster that has been stopped.
- [pcluster status](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.status.html): Pulls the current status of the cluster.
- [pcluster stop](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.stop.html): Stops the compute fleet, leaving the head node running.
- [pcluster update](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.update.html): Analyzes the configuration file to determine if the cluster can be safely updated.
- [pcluster version](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.version.html): Displays the AWS ParallelCluster version.
- [pcluster-config](https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster-config.html): Updates the AWS ParallelCluster configuration file.


## [Configuration](https://docs.aws.amazon.com/parallelcluster/v2/ug/configuration.html)

- [[global] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/global.html): Specifies global configuration options related to pcluster.
- [[aws] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/aws.html): (Optional) Used to select the AWS Region.
- [[aliases] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/aliases.html)
- [[cluster] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/cluster-definition.html): Defines a cluster template that can be used to create a cluster.
- [[compute_resource] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/compute-resource-section.html): Defines configuration settings for a compute resource. [compute_resource] sections are referenced by the setting in the [queue] section. [compute_resource] sections are only supported when is set to slurm.
- [[cw_log] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/cw-log-section.html): Defines configuration settings for CloudWatch Logs.
- [[dashboard] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/dashboard-section.html): Defines configuration settings for the CloudWatch dashboard.
- [[dcv] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/dcv-section.html): Defines configuration settings for the Amazon DCV server running on the head node.
- [[ebs] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/ebs-section.html): Defines Amazon EBS volume configuration settings for volumes that are mounted on the head node and shared to the compute nodes through NFS.
- [[efs] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/efs-section.html): Defines the configuration settings for the Amazon EFS that's mounted on the head and compute nodes.
- [[fsx] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/fsx-section.html): Defines configuration settings for an attached FSx for Lustre file system.
- [[queue] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/queue-section.html): Defines configuration settings for a single queue. [queue] sections are only supported when is set to slurm.
- [[raid] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/raid-section.html): Defines configuration settings for a RAID array that's built from a number of identical Amazon EBS volumes.
- [[scaling] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/scaling-section.html)
- [[vpc] section](https://docs.aws.amazon.com/parallelcluster/v2/ug/vpc-section.html): Specifies Amazon VPC configuration settings.
- [Examples](https://docs.aws.amazon.com/parallelcluster/v2/ug/examples.html)


## [How AWS ParallelCluster works](https://docs.aws.amazon.com/parallelcluster/v2/ug/functional.html)

- [AWS ParallelCluster processes](https://docs.aws.amazon.com/parallelcluster/v2/ug/processes.html)
- [AWS services used by AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/aws-services.html): The following Amazon Web Services (AWS) services are used by AWS ParallelCluster.
- [AWS ParallelCluster Auto Scaling](https://docs.aws.amazon.com/parallelcluster/v2/ug/autoscaling.html)


## [Tutorials](https://docs.aws.amazon.com/parallelcluster/v2/ug/tutorials.html)

- [Running your first job on AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/v2/ug/tutorials_01_hello_world.html): This tutorial walks you through running your first Hello World job on AWS ParallelCluster.
- [Building a Custom AWS ParallelCluster AMI](https://docs.aws.amazon.com/parallelcluster/v2/ug/tutorials_02_ami_customization.html)
- [Running an MPI job with AWS ParallelCluster and awsbatch scheduler](https://docs.aws.amazon.com/parallelcluster/v2/ug/tutorials_03_batch_mpi.html): This tutorial walks you through running an MPI job with awsbatch as a scheduler.
- [Disk encryption with a custom KMS Key](https://docs.aws.amazon.com/parallelcluster/v2/ug/tutorials_04_encrypted_kms_fs.html): AWS ParallelCluster supports the configuration options ebs_kms_key_id and fsx_kms_key_id.
- [Multiple queue mode tutorial](https://docs.aws.amazon.com/parallelcluster/v2/ug/tutorial-mqm.html): AWS ParallelCluster supports multiple queues of compute nodes for processing jobs when using Slurm Workload Manager.


## [Development](https://docs.aws.amazon.com/parallelcluster/v2/ug/development.html)

- [Setting up a custom AWS ParallelCluster cookbook](https://docs.aws.amazon.com/parallelcluster/v2/ug/custom_cookbook.html)
- [Setting up a custom AWS ParallelCluster node package](https://docs.aws.amazon.com/parallelcluster/v2/ug/custom_node_package.html)


## [Security](https://docs.aws.amazon.com/parallelcluster/v2/ug/security.html)

- [Data protection](https://docs.aws.amazon.com/parallelcluster/v2/ug/data-protection.html): Learn how the AWS shared responsibility model applies to data protection when using AWS ParallelCluster.
- [Identity and Access Management](https://docs.aws.amazon.com/parallelcluster/v2/ug/security-iam.html): AWS ParallelCluster uses roles to access your AWS resources and their services.
- [Compliance validation](https://docs.aws.amazon.com/parallelcluster/v2/ug/security-compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Enforcing TLS 1.2](https://docs.aws.amazon.com/parallelcluster/v2/ug/security-enforcing-tls.html): Learn how to enforce a minimum version of TLS 1.2 for AWS ParallelCluster.
