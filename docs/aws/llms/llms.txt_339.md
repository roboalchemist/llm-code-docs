# Source: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/llms.txt

# AWS Elemental Conductor File Cluster Configuration Guide

- [About This Guide](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/about-cf-cg.html)
- [Document History](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/doc-history.html)

## [Getting Ready for Phase 2](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/ready-cf-cg.html)

- [General Information](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/ready-cf-cg-gen.html)
- [Web Interface Access](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/ready-cf-cg-access.html): Many of the steps in this procedure involve working in the web interface.
- [Where to Work: Configuration Screens](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/ready-cf-cg-where.html): The procedures in this guide use one of three screens on the Conductor web interface.


## [Configuring the AWS Elemental Conductor File Node](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg.html)

- [Run the AWS Elemental Conductor File Configuration Script](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-script.html): Perform this procedure if one of these applies:

### [Configure Ethernet Devices on AWS Elemental Conductor File Nodes](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-ethernet.html)

When you installed each AWS Elemental product in the cluster, you configured eth0.

- [Add Ethernet Devices](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-ethernet-add.html)
- [Bond Ethernet Devices](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-ethernet-bond.html): You can bond Ethernet devices to suit your networking requirements.
- [Configure DNS and NTP Servers](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-servers.html): You can configure servers in the following ways:
- [Open Ports on the Firewall](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-firewall.html): You can enable or disable the firewall.
- [Add Mount Points](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-mount.html): You might want to specify files as the input sources for jobs.

### [Configure Database Backup](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-bkup.html)

- [View Folder for Database Backups](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-bkup-view.html)
- [Change Folder for Database Backups](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-bkup-change.html): The default folder for backups is on the node at /home/elemental/database_backups.
- [Restore a Database Backup](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-bkup-restore.html): Follow this procedure if you ever need to restore a backed-up version of the database.
- [Configure Authentication Settings](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-users-auth.html)
- [Add Users](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-users.html): To set up users for the entire cluster, you need to perform this setup only on the Conductor node.
- [Set Failover Timing](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-failover.html): This section describes how to set the timeout rate for failover.

### [Configure Redundancy](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-redundancy.html)

Read this section if you have two Conductor nodes.

- [Step A: Get Ready](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-redundancy-ready.html)
- [Step B: Create a dbrepl_config.yml File](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-redundancy-yml.html)
- [Step C: Run the Redundancy Install Script](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-redundancy-run.html): This install script configures Conductor redundancy.
- [Step D: Test Failover](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-redundancy-test.html)


## [Configuring the Worker Node](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg.html)

### [Configure Ethernet Devices](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-ethernet.html)

When you installed each AWS Elemental product in the cluster, you configured eth0.

- [Add Ethernet Devices](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-ethernet-add.html)
- [Bond Ethernet Devices](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-ethernet-bond.html): You can bond Ethernet devices to suit your networking requirements.

### [Add AWS Elemental Server Nodes to the Cluster](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-add.html)

Add all of the worker nodes to the cluster so that they can be controlled by the Conductor node.

- [Discover Nodes](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-add-discover.html): If a node did not appear in the list of all nodes, you can force its discovery.
- [Open Ports on the Firewall](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-firewall.html): The procedure for opening ports on the firewall for AWS Elemental Server nodes is the same as for AWS Elemental Conductor File nodes.
- [Add Mount Points](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-mount.html): If you have mounted remote shares on the Conductor node or nodes, we strongly recommend that you mount the same shares on all worker nodes.


## [Working with Users](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/users.html)

- [View User Information](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-users-view.html): Each user can log in to the web interface and view their own profile.
- [Change and Delete Users](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-users-candd.html)
- [Create New User Types](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-users-create.html): The policies determine what actions a user can perform on the node.
- [Manage Global Access Features](https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-users-manage.html): You can set some access features that apply globally to all users on the node.
