# Source: https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/llms.txt

# Microsoft SQL Server on Amazon EC2 User Guide

- [Set up SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/setting-up.html)
- [Find a SQL Server license-included AMI](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-amis.html)
- [Deploy SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/create-sql-server-on-ec2-instance.html)
- [Connect to SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/connect-sql-server-on-ec2-instance.html)
- [VSS based database backup](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/ms-ssdb-ec2-bkup-vss.html)
- [Migrating an on-premises database to Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/migrate-sql-from-on-premises.html)
- [Document history](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/doc-history.html)

## [What is Microsoft SQL Server on Amazon EC2?](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-overview.html)

- [Options to run SQL Server](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-options.html): Understand and choose from your options to run SQL Server on Amazon EC2 in the AWS Cloud.
- [Concepts and terminology](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-concepts.html): Understand the concepts and terminology of running SQL Server on Amazon EC2.
- [SQL Clustering best practices](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/aws-sql-ec2-clustering.html): Provides recommended best practices for operating a SQL Server Always On availability groups in AWS.


## [Licensing options and considerations](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-licensing.html)

### [Amazon EC2 High Availability for SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-high-availability.html)

A feature that reduces SQL Server licensing costs for High Availability deployments on Amazon EC2 by automatically identifying and exempting passive failover instances from SQL Server license fees while maintaining full functionality.

- [How it works](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-high-availability-how.html): Upon registration, Amazon EC2 High Availability for SQL Server (SQL HA) automatically monitors your Amazon EC2 instances running Windows SQL Server License Included AMIs and classifies them as either active or standby based on their current role in your SQL Server deployment.

### [Getting started](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-high-availability-get-started.html)

To get started with Amazon EC2 High Availability for SQL Server (SQL HA), perform the following steps:

- [Windows user setup](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-high-availability-windows-user-setup.html)
- [Disable Amazon EC2 High Availability for SQL Server](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-high-availability-disable.html): You can disable Amazon EC2 High Availability for SQL Server (SQL HA).
- [View states](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-high-availability-view.html): You can view the Amazon EC2 High Availability for SQL Server (SQL HA) current and historical states.

### [Security](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/security-sql-ha-server-on-ec2.html)

Configure Microsoft SQL Server on Amazon EC2 to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your SQL Server on EC2 resources.

### [Identity and access management](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/security-iam.html)

Use IAM roles and policies to control access to Amazon EC2 resources for Microsoft SQL Server on Amazon EC2 instances.

- [AWS managed policies](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for SQL Server on EC2 and recent changes to those policies.
- [Service-linked role](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/slr-sql-ha.html): Get information about the service-linked role for Amazon EC2 High Availability for SQL Server that grants SQL Server on EC2 access to detect whether an EC2 instance that's tagged with the EC2 SQL High Availability identifier is running in standby or passive mode.


## [VSS based database restore with automation runbook](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/ms-ssdb-ec2-restore-vss.html)

- [Prerequisites](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/ms-ssdb-ec2-vss-restore-prereq.html): Prerequisites for restoring a Microsoft SQL Server database running on an EC2 Windows instance using AWS VSS solution based EBS volume snapshots.
- [Restore from VSS snapshots](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/ms-ssdb-ec2-vss-restore-from-snap.html): Restore a Microsoft SQL Server database running on an EC2 Windows instance from AWS VSS solution based EBS volume snapshots.


## [Evaluate downgrading your SQL Server edition](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/downgrade-sql-server-on-ec2.html)

- [Downgrade your SQL Server Enterprise edition](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/downgrade-sql-server-manual-steps.html): Understand how to downgrade your SQL Server edition on Amazon EC2.


## [Migrate Microsoft SQL Server from Windows to Linux](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/replatform-sql-server.html)

- [Replatforming script prerequisites](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/replatform-sql-server-setting-up.html): Learn about the Windows to Linux replatforming assistant prerequisites.
- [Run the replatforming script](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/replatform-sql-server-script.html): Learn how to run the replatforming assistant for SQL Server script.
