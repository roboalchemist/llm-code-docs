# Source: https://docs.aws.amazon.com/elemental-live/latest/configguide/llms.txt

# AWS Elemental Live Configuration Guide

> AWS Elemental Live is a real-time video service that lets you create live outputs for broadcast and streaming delivery. This Configuration Guide describes how to configure nodes to successfully run AWS Elemental Live.

- [About this guide](https://docs.aws.amazon.com/elemental-live/latest/configguide/about-lv-cg.html)
- [Getting ready](https://docs.aws.amazon.com/elemental-live/latest/configguide/ready-lv-cg.html)
- [Configuring licenses](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-live-licenses.html)
- [Document history](https://docs.aws.amazon.com/elemental-live/latest/configguide/doc-history.html)

## [Initial configuration](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg.html)

- [Enable HTTPS](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-ssl.html): .
- [Verify the licenses](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-licenses.html): Make sure that you have the appropriate AWS Elemental Live licenses installed.
- [Set the time zone](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-timezone.html): Follow this procedure if you didn't set the time zone when you ran the install script (via the ât prompt), or if you want to change the time zone on the AWS Elemental Live node.
- [Manage Ethernet devices](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-cf-cg-ethernet.html): When you installed each AWS Elemental Live in the cluster, you configured eth0.
- [Manage bonds](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-live-cg-ethernet.html): If you set up more Ethernet devices on the AWS Elemental Live node, you can optionally bond two devices.
- [Configure DNS and NTP Servers](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-servers.html): You can add Domain Name System (DNS) name servers and Network Time Protocol (NTP) servers for the AWS Elemental Live node to use.
- [Open ports on the firewall](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-cf-cg-firewall.html): You can enable or disable the firewall on AWS Elemental Live nodes.
- [Add mount points](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-cf-cg-mount.html): To make remote assets, such as scripts, image files, or video source files, available to your AWS Elemental Live nodes, create mount points as described in this section.
- [Add SDI input devices](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-sdi-dev.html): Input devices are cards that are installed in the hardware unit.

### [Add SDI video routers](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-sdi-rou.html)

If your deployment includes SDI video inputs that pass through a router, provide information about your router configuration on the AWS Elemental Live node.

- [Step A: Get ready](https://docs.aws.amazon.com/elemental-live/latest/configguide/sdi-rou-ready.html): To get ready to add an SDI video router, perform the following steps.
- [Step B: Create the router](https://docs.aws.amazon.com/elemental-live/latest/configguide/sdi-rou-create.html): Create the router on the Elemental Live node.
- [Step C: Complete the input mappings](https://docs.aws.amazon.com/elemental-live/latest/configguide/sdi-rou-input.html): Next, complete the Input mappings to assign an ID to each input on the router.
- [Step D: Complete the output mappings](https://docs.aws.amazon.com/elemental-live/latest/configguide/sdi-rou-output.html): Map each router output to the SDI input on the Elemental Live hardware unit that you plan to use.
- [Step E: Use the router inputs](https://docs.aws.amazon.com/elemental-live/latest/configguide/sdi-rou-using.html): When you create a profile or event, the inputs that you created are displayed in the Input field.
- [Enable RTMP inputs](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-rtmp.html): Elemental Live is configured by default to support Real Time Messaging Protocol (RTMP) inputs.
- [Configure database backups](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-bkup.html): During a database backup, AWS Elemental Live copies the data that's related to your framework (channels, profiles, nodes, MPTS outputs, and redundancy groups) from the Elemental Live node to another server.

### [Configure notifications](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-notifications.html)

AWS Elemental Live provides status information through alerts and messages.

### [Email notification](https://docs.aws.amazon.com/elemental-live/latest/configguide/notification-email.html)

You can configure AWS Elemental Live to email you notifications when alerts occur.

- [Configure Sendmail relay server](https://docs.aws.amazon.com/elemental-live/latest/configguide/notification-email-sendmail.html): Use this procedure to set up a Sendmail relay server if your network doesn't accept open relay messages.
- [Web callback notification](https://docs.aws.amazon.com/elemental-live/latest/configguide/notification-web.html): You can configure AWS Elemental Live to send you web callback notifications when alerts occur.
- [Simple Network Management Protocol (SNMP) traps](https://docs.aws.amazon.com/elemental-live/latest/configguide/notification-trap.html): You can configure AWS Elemental Live to generate Simple Network Magement Protocol (SNMPv2) traps for the following activity:

### [Simple Network Management Protocol (SNMP) polling](https://docs.aws.amazon.com/elemental-live/latest/configguide/notification-polling.html)

Rather than passively receiving SNMP traps from AWS Elemental Live, you can actively poll the SNMP interface.

- [Management Information Bases (MIBs) in Elemental Live](https://docs.aws.amazon.com/elemental-live/latest/configguide/notification-polling-mibs.html): AWS Elemental provides the following management information bases (MIBs) for use with Elemental Live:
- [Enable user authentication](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-auth.html): You can require users to provide valid credentials when they access Elemental Live from both the web interface and REST API.
- [Add users](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users.html): When you enable local authentication on the AWS Elemental Live node, users must enter valid credentials to access the node.


## [Managing the configuration](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-manage.html)

- [Disable HTTPS](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-ssl-chg.html): .

### [Database Backups](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-bkup-chg.html)

This section describes how to restore a database backup and how to disable backups entirely.

- [Restore a backup](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-bkup-restore.html): Follow this procedure if you ever need to restore a backed-up version of the database.
- [Disable database backups](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-bkup-dis.html): Follow these steps to disable automatic backups of the AWS Elemental Live database.

### [Users](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users-chg.html)

This section describes how to manage users that you've already added to the AWS Elemental Live node.

- [View user information](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users-view.html): Each user can log in to the AWS Elemental Live web interface and view their own profile.
- [Change and delete users](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users-candd.html): Administrators can change and delete users of AWS Elemental Live.
- [Create new user roles](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users-create.html): The policies determine what actions a user can perform on the AWS Elemental Live node.
- [Manage global access features](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users-manage.html): You can set some access features that apply globally to all users on the AWS Elemental Live node.


## [User authentication reference](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-auth-ref.html)

- [Supported types of user authentication](https://docs.aws.amazon.com/elemental-live/latest/configguide/auth-ref-type-auth.html): AWS Elemental Live supports the following types of user authentication:
- [Authentication user types](https://docs.aws.amazon.com/elemental-live/latest/configguide/auth-ref-type-user.html): This table describes the types of users available with authentication.
