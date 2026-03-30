# Source: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/llms.txt

# AWS Elemental Conductor Live Configuration Guide

> Learn how to configure AWS Elemental nodes into an AWS Elemental Conductor Live cluster.

- [About this guide](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/about-conductor-live-cg.html)
- [Rules and limits](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-rules.html)
- [Accessing the nodes](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/ready-conductor-live-config-access.html)
- [Designing the cluster](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/ready-conductor-live-cg.html)
- [Document History](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/doc-history.html)

## [Key cluster setup procedures](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-checklists.html)

- [Initial configuration](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-checklist-newcluster.html): Read about the typical steps to follow to set up AWS Elemental Conductor Live, AWS Elemental Live, and (optionally) AWS Elemental Statmux for the first time.
- [Upgrading standalone nodes](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-checklist-standalone-to-cluster.html): Read about the typical steps to follow to upgrade from a standalone AWS Elemental Live to a cluster of AWS Elemental Conductor Live, AWS Elemental Live, and (optionally) AWS Elemental Statmux.
- [Adding user authentication](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-checklist-add-auth.html): Read about the typical steps to add user authentication to a cluster of AWS Elemental Conductor Live, AWS Elemental Live, and (optionally) AWS Elemental Statmux nodes.
- [Adding Conductor redundancy](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-checklist-add-redundancy.html): Read about the typical steps to follow to add Conductor redundancy to an AWS Elemental Conductor Live cluster.


## [Reference: Configure connectivity](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-network.html)

- [DNS servers](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-cluster-dns.html): Learn how to configure the nodes in an Conductor Live cluster to use DNS.
- [Clocks: NTP and PTP servers](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-cluster-ntp.html): Learn how to configure an NTP clock server or PTP clock server on the nodes in an AWS Elemental Conductor Live cluster.

### [Ethernet interfaces](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-config-ethernet-add.html)

Learn how to set up Ethernet interfaces (network devices) on the nodes in an AWS Elemental Conductor Live cluster.

- [Creating an Ethernet interface](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-ethernet-create.html): You use the CLI to create Ethernet interfaces using the web interface.
- [Modifying an Ethernet interface](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-ethernet-modify.html): You use the CLI to modify Ethernet interfaces using the web interface.
- [Creating or modifying a bond](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-config-bond-add.html): If you set up more Ethernet interfaces on the Conductor Live node, you can optionally bond two Ethernet interfaces.
- [Dedicating interfaces to MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-cluster-mpts.html): This section applies only of your cluster includes AWS Elemental Statmux nodes.
- [Firewalls and ports](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/network-firewall.html): Learn how to enable or disable the firewall on the nodes in an AWS Elemental Conductor Live cluster.
- [HTTPS](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/ssl-config.html): Learn how to enable HTTPS on the nodes in an AWS Elemental Conductor Live cluster.
- [Input: Directly connected SDI inputs](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-sdi-dev.html): Learn how to configure the SDI cards that are attached to individual AWS Elemental Live nodes in an AWS Elemental Conductor Live cluster.

### [Inputs: Routers for handling SDI inputs](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-sdi-rou.html)

Learn how to configure a router, if you are using one in your AWS Elemental Conductor Live cluster.

- [Step A: Gather information](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-router-gather-info.html)
- [Step B: Run cables from the router to each node](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-rou-ready.html): Perform this procedure on the Elemental Live node that is connected to the router.
- [Step C: Add the router](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-rou-create.html): Perform this procedure on the primary Conductor Live node.
- [Step D: Complete the Router Input Mappings](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-rou-input.html): Perform this procedure on the primary Conductor Live node.
- [Step E: Complete the Router Output Mappings](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-rou-output.html): Perform this procedure on the Conductor Live node.
- [Step F: Sync the Routers](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-rou-sync.html): Perform this procedure on the Conductor Live node.
- [Step G: Use the Router Inputs](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-rou-using.html): When you create a profile or event, the inputs that you created are displayed in the Input field.
- [Mount points](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-wrkr-cf-config-mount.html): Learn how to create mount points on an AWS Elemental Conductor Live node, so that the nodes in a cluster can access remote assets.
- [Time zone](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-timezone.html): Learn how to set the time zone on an AWS Elemental Conductor Live, AWS Elemental Live, or AWS Elemental Statmux node.


## [Reference: Configure worker features](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-features.html)

- [OCR for captions](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-ocr.html): Learn how to enable the OCR conversion feature on ECL3; node that is in an AWS Elemental Conductor Live cluster.
- [RTMP inputs](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-rtmp.html): Learn how to disable polling for RTMP inputs on ECL3; node that is in an AWS Elemental Conductor Live cluster.
- [Virtual input switching](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-vips.html): Learn how to configure the maximum number of virtual inputs on ECL3; node that is in an AWS Elemental Conductor Live cluster.


## [Reference: Configure the cluster](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-nodes.html)

### [Manage nodes](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-nodes.html)

Learn how to add or remove nodes in an AWS Elemental Conductor Live cluster.

- [Add (recruit) nodes](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-nodes-add.html): Learn how to add (recruit) nodes into an AWS Elemental Conductor Live cluster.
- [Remove a worker node](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-nodes-remove.html): Learn how to remove AWS Elemental Live or AWS Elemental Statmux nodes from an Conductor Live cluster.
- [Remove a Conductor Live node](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-cl-node-remove.html): Learn how to remove Conductor Live nodes from a cluster.

### [Redundancy groups](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-redundancy.html)

Learn how to create groups of redundant nodes in an AWS Elemental Conductor Live cluster.

- [Conductor Live redundancy group](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-redundancy-cl.html): If you are implementing Conductor Live redundancy, then you should have two Conductor Live nodes â a primary node and a secondary node.
- [Worker redundancy groups](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-wrkr-red.html): To set up worker nodes for failover resiliency, you create one or more redundancy groups, then you add worker nodes to each group.

### [High availability (HA)](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-ha-about.html)

Learn how to enable high availability (HA) when you have set up a primary and a secondary AWS Elemental Conductor Live node as a redundancy group.

- [Verifying the current HA state](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-ha-current-state.html): On the web interface for the primary Conductor Live node, go to the Cluster page and choose Redundancy.
- [Enabling HA](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-ha.html): If you have set up the cluster with a primary and a secondary Conductor Live node, you must enable HA before you start running channels and MPTSes in the cluster.
- [Disabling HA](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-ha-chg.html): The main reason to disable HA is to make a change to the configuration of one or both Conductor Live nodes.


## [Reference: Configure user authentication](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-user-auth.html)

- [About user authentication](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-user-auth-overview.html): Learn about the types of user authentication that you can set up on an Conductor Live cluster.
- [Step 1: Enable user authentication](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-auth.html): Learn how to enable user authentication on an Conductor Live node.
- [Step 2: Apply authentication](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-auth-wrkr.html): Learn how to enable user authentication on ECL3; or an AWS Elemental Statmux node.
- [Disabling user authentication](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-auth-chg.html): Learn how to disable user authentication on an Conductor Live cluster.


## [Reference: Manage users](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-users.html)

- [Types of users](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/users-types.html): Learn about the types of users you can set up in an Conductor Live cluster.
- [Adding users to Conductor Live](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-users.html): Learn how to add users to an Conductor Live cluster.
- [Adding users to workers](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-users-add-workers.html): Learn how to add local users to ECL3; or AWS Elemental Statmux node in an Conductor Live cluster.
- [Role policies for PAM authentication](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-rpolicies.html): Learn about the role policies use for PAM authentication in an Conductor Live cluster.


## [Reference: Configure notifications](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-notifications.html)

### [Email notification](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-email.html)

Learn how to configure AWS Elemental Conductor Live so that you can receive email notifications about activity on the cluster.

- [Configure sendmail relay server](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-email-sendmail.html): Use this procedure to set up a Sendmail relay server if your network doesn't accept open relay messages.
- [Web callback notification](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-web.html): Learn how to configure AWS Elemental Conductor Live so that you can receive web callback notifications about activity on the cluster.
- [SNMP traps](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-trap.html): Learn how to configure AWS Elemental Conductor Live to generate SNMP traps for activity on the cluster.

### [SNMP polling](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-polling.html)

Learn how to configure AWS Elemental Conductor Live to poll the SNMP interface for SNMP traps about activity on the cluster.

- [MIBs in Conductor Live](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-polling-mibs.html): Read a list of MIBS that AWS Elemental provides for use with Conductor Live.


## [Reference: Backup and restore](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-backup.html)

- [Configuring for backup](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-bkup.html): Configure backup for Conductor Live.
- [Disabling database backups](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-bkup-dis.html): Disable database backups on the AWS Elemental Conductor Live interface. disable database backup
- [Restoring a backup](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-bkup-restore.html): Restore a backup version of the database on a Conductor Live, Elemental Live, or Elemental Statmux node.
