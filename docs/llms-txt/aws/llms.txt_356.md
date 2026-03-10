# Source: https://docs.aws.amazon.com/elemental-server/latest/configguide/llms.txt

# AWS Elemental Server Configuration Guide

> AWS Elemental Server provides fast, reliable video processing for file-based transcoding workflows. It performs simultaneous, faster-than-real-time conversion of multiple video files to create mezzanine deliverables, traditional on-demand assets, and adaptive bitrate outputs for delivery to TVs, PCs, and mobile devices. This Configuration Guide describes how to configure settings and set up nodes.

- [About This Guide](https://docs.aws.amazon.com/elemental-server/latest/configguide/about-srvr-cg.html)
- [Getting Ready](https://docs.aws.amazon.com/elemental-server/latest/configguide/ready-srvr-cg.html)
- [Document History](https://docs.aws.amazon.com/elemental-server/latest/configguide/doc-history.html)

## [Initial Configuration](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg.html)

- [Verify the Licenses](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-licenses.html): Make sure that you have the appropriate licenses installed.
- [Set the Time Zone](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-timezone.html): Follow this procedure if you didn't set the time zone when you ran the install script (via the ât prompt), or if you want to change the time zone.

### [Configure Ethernet Devices](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-ethernet.html)

When you installed each AWS Elemental product in the cluster, you configured eth0.

- [Add Ethernet Devices](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-ethernet-add.html): The eth0 device was automatically set up during installation.

### [Bond Ethernet Devices](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-ethernet-bond.html)

You can bond Ethernet devices to suit your networking requirements.

- [Step A: Create the Bond](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-ethernet-bond-create.html): First, create the bond for the network devices.
- [Step B: Assign the Devices](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-ethernet-bond-assign.html): Next, add the Ethernet devices to the bond that you created in .
- [Configure DNS and NTP Servers](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-servers.html): You can add Domain Name System (DNS) name servers and Network Time Protocol (NTP) servers for the node to use.
- [Open Ports on the Firewall](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-firewall.html): You can enable or disable the firewall.
- [Add Mount Points](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-mount.html): To make remote assets, such as scripts, image files, or video source files, available to your AWS Elemental Server nodes, create mount points as described in this section.
- [Configure Database Backups](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-bkup.html): During a database backup, AWS Elemental Server copies the data that's related to your framework (channels, profiles, nodes, MPTS outputs, and redundancy groups) from the AWS Elemental Server node to another server.

### [Configure Notifications](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-notifications.html)

AWS Elemental Server provides status information through alerts and messages.

### [Email Notifications](https://docs.aws.amazon.com/elemental-server/latest/configguide/notification-email.html)

You can configure AWS Elemental Server to email you notifications when alerts occur.

- [Configure Sendmail Relay Server](https://docs.aws.amazon.com/elemental-server/latest/configguide/notification-email-sendmail.html): Use this procedure to set up a Sendmail relay server if your network doesn't accept open relay messages.
- [Web Callback Notification](https://docs.aws.amazon.com/elemental-server/latest/configguide/notification-web.html): You can configure AWS Elemental Server to send you web callback notifications when alerts occur.
- [Simple Network Management Protocol (SNMP) Traps](https://docs.aws.amazon.com/elemental-server/latest/configguide/notification-trap.html): You can configure AWS Elemental Server to generate Simple Network Management Protocol (SNMPv2) traps for activity on the node.

### [Simple Network Management Protocol (SNMP) Polling](https://docs.aws.amazon.com/elemental-server/latest/configguide/notification-polling.html)

Rather than passively receiving SNMP traps from AWS Elemental Server, you can actively poll the SNMP interface.

- [Management Information Bases (MIBs) in AWS Elemental Server](https://docs.aws.amazon.com/elemental-server/latest/configguide/notification-polling-mibs.html): AWS Elemental provides the following management information bases (MIBs) for use with AWS Elemental Server:
- [Enable User Authentication](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-auth.html): You can require users to provide valid credentials when they access AWS Elemental Server from both the web interface and REST API.
- [Add Users](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-users.html): When you enable local authentication on the node, users must enter valid credentials to access the node.


## [Managing the Configuration](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-manage.html)

- [Disable SSL](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-ssl-chg.html): This section describes how to disable HTTPS (SSL) access to the node.

### [Database Backups](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-bkup-chg.html)

This section describes how to restore a database backup, and how to disable backups entirely.

- [Restore a Backup](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-bkup-restore.html): Follow this procedure if you ever need to restore a backed-up version of the database.
- [Disable Automatic Database Backups](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-bkup-dis.html): Follow these steps to disable automatic backups.

### [Users](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-users-chg.html)

This section describes how to manage users that you've already added to the AWS Elemental Server node.

- [View User Information](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-users-view.html): Each user can log in to the web interface and view their own profile.
- [Change and Delete Users](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-users-candd.html)
- [Create New User Roles](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-users-create.html): The policies determine what actions a user can perform on the node.
- [Manage Global Access Features](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-users-manage.html): You can set some access features that apply globally to all users on the node.


## [User Authentication Reference](https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-auth-ref.html)

- [Supported Types of User Authentication](https://docs.aws.amazon.com/elemental-server/latest/configguide/auth-ref-type-auth.html): AWS Elemental Server supports the following types of user authentication:
- [Authentication User Types](https://docs.aws.amazon.com/elemental-server/latest/configguide/auth-ref-type-user.html): This table describes the types of users available with authentication.
