# Source: https://docs.aws.amazon.com/lightsail/latest/userguide/llms.txt

# Amazon Lightsail User Guide

> The Amazon Lightsail User Guide contains conceptual overviews, how-to topics, tutorials, and references for creating Amazon EC2 instances, domains, static IP addresses, and more. With Lightsail, you can run a number of pre-installed applications and operating systems, such as WordPress, Ubuntu, LAMP, SQL Server, Node, and Nginx.

- [What is Lightsail?](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)
- [Set up](https://docs.aws.amazon.com/lightsail/latest/userguide/setting-up.html)
- [Access Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/access-lightsail.html)
- [Billing](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-your-amazon-lightsail-bill.html)
- [Document history](https://docs.aws.amazon.com/lightsail/latest/userguide/document-history.html)
- [Get help](https://docs.aws.amazon.com/lightsail/latest/userguide/getting-help-in-amazon-lightsail.html)

## [Getting started](https://docs.aws.amazon.com/lightsail/latest/userguide/getting-started.html)

- [Using Lightsail with the AWS CLI](https://docs.aws.amazon.com/lightsail/latest/userguide/getstarted-awscli.html): This tutorial guides you through common Amazon Lightsail operations using the AWS Command Line Interface (AWS CLI).


## [Lightsail resellers](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-resellers.html)

- [Become a Lightsail reseller](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-resellers-become-a-reseller.html): Learn about how you can request to become a Lightsail reseller.
- [Service quota increases](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-resellers-request-quota-increase.html): Learn about how you can request a service quota increase for your reseller accounts.
- [Contact Lightsail as a reseller](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-resellers-contact-lightsail.html): Learn how to contact Lightsail as a reseller.


## [Instances](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-instances-virtual-private-servers-in-amazon-lightsail.html)

### [Create an instance](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-create-amazon-lightsail-instance-virtual-private-server-vps.html)

Learn how to create a virtual private server (VPS) instance on Amazon Lightsail with pre-configured operating systems, applications, or development stacks.

- [Linux instances](https://docs.aws.amazon.com/lightsail/latest/userguide/getting-started-with-amazon-lightsail.html): Create Linux/Unix-based instances with applications like WordPress or LAMP on Amazon Lightsail, connect with SSH, and manage instances within the Lightsail console.
- [Windows instances](https://docs.aws.amazon.com/lightsail/latest/userguide/get-started-with-windows-based-instances-in-lightsail.html): Learn how to create and connect to Windows Server-based instances on Amazon Lightsail, with options for Windows Server 2022, 2019, 2016, and SQL Server Express.
- [Blueprints](https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image.html): Learn about the available Amazon Lightsail instance images and blueprints.
- [Bundles](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bundles.html): Review the available Amazon Lightsail instance bundle specifications, including pricing, compute resources, storage, and Data transfer allowances.

### [Instance firewalls](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-firewall-and-port-mappings-in-amazon-lightsail.html)

Learn how to control inbound traffic to your Amazon Lightsail instances using firewalls and port mappings to enhance security and access management.

- [Add firewall rules](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-editing-firewall-rules.html): Learn how to add and edit IPv4 and IPv6 firewall rules for your Amazon Lightsail instance to control inbound traffic based on protocols, ports, and source IP addresses.
- [Delete firewall rules](https://docs.aws.amazon.com/lightsail/latest/userguide/firewall-deleting-rules.html): Learn how to delete IPv4 and IPv6 firewall rules for your Amazon Lightsail instance to control inbound traffic based on protocols, ports, and source IP addresses.
- [Instance firewall rules](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-firewall-rules-reference.html): Discover how Amazon Lightsail firewall rules enable secure access for web, database, DNS, email servers, and remote connections to instances.

### [Burst capacity and performance](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-burst-capacity.html)

Learn how to identify when your Amazon Lightsail instance bursts to manage CPU utilization and capacity for optimal performance.

- [CPU performance](https://docs.aws.amazon.com/lightsail/latest/userguide/baseline-cpu-performance.html): Learn how Amazon Lightsail instances accrue CPU burst capacity over baseline performance to handle spikes in CPU utilization.
- [Burst capacity accrual](https://docs.aws.amazon.com/lightsail/latest/userguide/cpu-burst-capacity-accrual.html): Learn how CPU burst capacity for Amazon Lightsail instances accrues over time, allowing bursts of higher CPU performance when needed, and discover important details regarding capacity persistence.
- [Identify instance bursts](https://docs.aws.amazon.com/lightsail/latest/userguide/identifying-instance-burst.html): Sustainable and burstable zones for you Amazon Lightsail instance.
- [Monitor burst capacity](https://docs.aws.amazon.com/lightsail/latest/userguide/monitoring-cpu-burst-capacity.html): Learn how to monitor the CPU burst capacity of your Amazon Lightsail instance.
- [View burst capacity](https://docs.aws.amazon.com/lightsail/latest/userguide/viewing-instance-burst-capacity.html): Learn how to view your Amazon Lightsail instance's CPU utilization and remaining burst capacity using the CPU overview page in the Lightsail console.
- [Troubleshoot high CPU](https://docs.aws.amazon.com/lightsail/latest/userguide/troubleshooting-high-cpu-utilization.html): Troubleshoot CPU utilization and burst capacity for your Amazon Lightsail instance.

### [Instance management](https://docs.aws.amazon.com/lightsail/latest/userguide/managing-your-instance-using-lightsail.html)

Learn how to connect to and manage your Amazon Lightsail instance for running virtual private servers (VPS), including starting, stopping, restarting, forcing stop, configuring networking, extending storage, running scripts, and securing Windows instances.

- [Start, stop, or restart your instance](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.html): Learn how to start, stop, or reboot your Amazon Lightsail instance (virtual private server) to manage its lifecycle and state.
- [Force stop instances](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-force-stop-instance.html): Learn how to force stop an Amazon Lightsail instance stuck in the stopping state using the Lightsail console or AWS CLI.
- [Enhanced networking](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-updating-ec2-instances.html): Learn how to update Amazon EC2 instances to use enhanced networking and latest generation instance types when migrating from Amazon Lightsail.
- [Extend Windows Server file system in Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/extending-windows-server-storage-space-in-amazon-lightsail.html): Extend the file system of your Amazon Lightsail Windows Server instance to use maximum available storage space after creating it with a larger plan snapshot.
- [Linux shell scripts](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-configure-server-additional-data-shell-script.html): Learn how to configure your new Linux/Unix Amazon Lightsail instance using a shell script that runs during launch to install software, update packages, or customize the environment.
- [PowerShell scripts](https://docs.aws.amazon.com/lightsail/latest/userguide/create-powershell-script-that-runs-when-you-create-windows-based-instance-in-lightsail.html): Learn how to configure your Windows-based Amazon Lightsail instance using PowerShell or batch scripts that run automatically after instance creation, enabling customization and software installation.
- [Windows security best practices](https://docs.aws.amazon.com/lightsail/latest/userguide/best-practices-for-securing-windows-based-lightsail-instances.html): Secure your Windows Server-based Amazon Lightsail instances by following best practices for password management, security patching, account lockout policies, and firewall settings.
- [Delete instances](https://docs.aws.amazon.com/lightsail/latest/userguide/delete-an-amazon-lightsail-instance.html): Learn how to delete your Amazon Lightsail instances to stop incurring charges, using the console or AWS CLI, and discover best practices for managing associated resources like snapshots and static IPs.

### [SSH and connecting to instances](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-ssh-in-amazon-lightsail.html)

Learn how to manage SSH key pairs and securely connect to your Amazon Lightsail instances using browser-based and third-party SSH/RDP clients.

- [Set up SSH keys](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-set-up-ssh.html): Learn how to securely connect to your Amazon Lightsail Linux instance using SSH keys, creating new keys, uploading existing ones, managing keys across regions, and downloading private keys for SSH clients.
- [Manage SSH keys](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-ssh-keys.html): Learn how to manage SSH keys to securely connect to yourAmazon Lightsail instances, including viewing, creating, uploading, downloading, and deleting default and custom key pairs.
- [Manage instance SSH keys](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-remove-ssh-key-on-instance.html): Manage SSH key pairs on Amazon Lightsail Linux instances to control secure access and prevent unauthorized connections.

### [Connect to Linux instances](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-connect-to-your-instance-virtual-private-server.html)

Learn how to securely connect to your Linux or Unix instances on Amazon Lightsail using the browser-based SSH client or your own SSH client.

- [Connect with SSH command](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-ssh-using-terminal.html): Use the SSH command to securely connect to your Linux or Unix Amazon Lightsail instance from a Linux, Unix, or macOS terminal, enabling remote access and management.
- [Connect with PuTTY](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-ssh-connect-to-instance-virtual-private-server-using-putty.html): Learn how to connect to your Linux/Unix-based Amazon Lightsail instance using PuTTY, an SSH client, with your private key and instance details.
- [Set up PuTTY](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-set-up-putty-to-connect-using-ssh.html): Learn how to set up PuTTY, a free SSH client, to securely connect to your Amazon Lightsail Linux/Unix instance using an SSH key pair.
- [Transfer files with SFTP](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-linux-unix-instance-using-sftp.html): Learn how to transfer files securely between your local computer and your Amazon Lightsail Linux instance using SFTP (SSH File Transfer Protocol) and the FileZilla client.

### [Connect to Windows instances](https://docs.aws.amazon.com/lightsail/latest/userguide/connect-to-your-windows-based-instance-using-amazon-lightsail.html)

Connect to your Amazon Lightsail Windows instance seamlessly using the browser-based RDP client to install software, configure applications, and perform administrative tasks securely.

- [Change the Administrator password](https://docs.aws.amazon.com/lightsail/latest/userguide/use-non-default-key-with-windows-based-instance-in-lightsail.html): Discover how to change the default Administrator password on your Windows Server-based Lightsail instance and decrypt the ciphertext using the AWS CLI to enhance security.
- [Windows RDC client](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-windows-instance-using-rdc.html): Learn how to connect to your Amazon Lightsail Windows instance using Microsoft Remote Desktop.
- [macOS RDC client](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-windows-instance-using-microsoft-remote-desktop.html): Learn how to connect to your Windows instance on Amazon Lightsail using Microsoft Remote Desktop from macOS, with steps to obtain the required credentials and configure the client.

### [Instance Metadata Service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-instance-metadata.html)

Discover how to access and configure instance metadata and user data in Amazon Lightsail for managing and customizing your instances' behavior.

- [Configure IMDS](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-instance-metadata-service.html): Learn how to access and configure Instance Metadata Service (IMDSv1 and IMDSv2) to securely retrieve instance metadata on Amazon Lightsail instances.


## [Disks](https://docs.aws.amazon.com/lightsail/latest/userguide/elastic-block-storage-and-ssd-disks-in-amazon-lightsail.html)

- [Attach disks to Linux instances](https://docs.aws.amazon.com/lightsail/latest/userguide/create-and-attach-additional-block-storage-disks-linux-unix.html): Learn how to create and attach additional block storage disks to your Linux-based Amazon Lightsail instance, format and mount disks, and automatically mount disks on reboot for persistent storage.
- [Attach disks to Windows instances](https://docs.aws.amazon.com/lightsail/latest/userguide/create-and-attach-additional-block-storage-disks-windows.html): Learn how to create and attach a block storage disk to your Windows Server instance in Amazon Lightsail.
- [Detach and delete disks](https://docs.aws.amazon.com/lightsail/latest/userguide/detach-and-delete-block-storage-disks.html): Learn how to safely detach and delete Amazon Lightsail block storage disks, ensuring data backup and resource cleanup.


## [Snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html)

### [Automatic snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html)

Use Amazon Lightsail to enable or disable automatic snapshots for instances and disks, retaining up to seven days of backups for data protection.

- [Change snapshot time](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-automatic-snapshot-time.html): Learn how to change the automatic snapshot time for Amazon Lightsail instances and block storage disks to suit your schedule for data backups.
- [Delete automatic snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-automatic-snapshots.html): Learn how to delete automatic snapshots of Amazon Lightsail instances and block storage disks to manage storage costs and cleanup unused backups.
- [Keep automatic snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots.html): Learn how to keep automatic snapshots of Amazon Lightsail instances and block storage disks from being replaced or deleted by copying them as manual snapshots using the Lightsail console or AWS CLI.
- [Linux snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-create-a-snapshot-of-your-instance.html): Learn how to create snapshots of your Linux/Unix-based Amazon Lightsail instances to back up system disks and attached block storage for data protection and instance recovery.
- [Windows snapshots and sysprep](https://docs.aws.amazon.com/lightsail/latest/userguide/prepare-windows-based-instance-and-create-snapshot.html): Learn how to create a reusable snapshot of your Windows Server instance for Amazon Lightsail by running System Preparation (Sysprep) and creating a backup snapshot.
- [Create block storage disk snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/create-block-storage-disk-snapshot.html): Create snapshots of Amazon Lightsail block storage disks for backups or new disk baselines.
- [Create disk from snapshot](https://docs.aws.amazon.com/lightsail/latest/userguide/create-new-block-storage-disk-from-snapshot.html): Create a new Amazon Lightsail block storage disk from an existing snapshot to backup or serve as a baseline for new disks.
- [Create a root volume snapshot](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-create-an-instance-root-volume-snapshot.html): Create a snapshot of your Amazon Lightsail instance's root volume for backup or data recovery.
- [Create an instance from a snapshot](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-create-instance-from-snapshot.html): Learn how to create a new Amazon Lightsail instance using a snapshot with configurable settings like instance size, networking type, availability zone, and launch script.
- [Create a larger resource from a snapshot](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-create-larger-instance-from-snapshot-using-console.html): Learn how to upsize your Amazon Lightsail instance, block storage, or database using snapshots to create larger resources for scaling your cloud project.
- [Create a larger resource from a snapshot using the AWS CLI](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-create-larger-instance-from-snapshot-using-aws-cli.html): Use the AWS CLI to create a larger Amazon Lightsail instance from a snapshot to scale your cloud project with more compute power.
- [Delete snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-snapshots.html): Learn how to delete instance, database, and disk snapshots in Amazon Lightsail to avoid incurring monthly charges for unused snapshots.
- [Copy snapshots across Regions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-copying-snapshots-from-one-region-to-another.html): Learn how to copy instance and block storage snapshots to another AWS Region for replicating resources or migrating to a new Region with the Amazon Lightsail management console.

### [Export snapshots to EC2](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-exporting-snapshots.html)

Learn how to export Amazon Lightsail snapshots to Amazon Elastic Compute Cloud (Amazon EC2), create Amazon EC2 resources from exported snapshots, choose compatible Amazon EC2 instance types, connect to Amazon EC2 instances, and secure Amazon EC2 instances created from Lightsail snapshots.

- [How to export snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-exporting-snapshots-to-amazon-ec2.html): Learn how to export an Amazon Lightsail instance and disk snapshots to Amazon Elastic Compute Cloud (Amazon EC2) for further utilization, creating AMIs and EBS snapshots.
- [Monitor exports](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-task-monitor.html): Learn how to monitor snapshot exports in Amazon Lightsail to track the status of exporting snapshots to Amazon EC2 or creating Amazon EC2 instances from exported snapshots using the Exports section of the Lightsail console.
- [Create EC2 instances from exported snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-ec2-instances-from-exported-snapshots.html): Learn how to create Amazon Elastic Compute Cloud instances from exported Amazon Lightsail snapshots using the Lightsail console, enabling seamless migration to Amazon EC2.
- [Create EBS volumes from exported snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-ebs-volumes-from-exported-snapshots.html): Learn how to create Amazon Elastic Block Store volumes from exported Amazon Lightsail disk snapshots for use with Amazon EC2 instances.
- [Connect to Linux EC2 instances](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-linux-unix-amazon-ec2-instances.html): Learn how to connect to your Linux or Unix instance in Amazon Elastic Compute Cloud created from an Amazon Lightsail snapshot using PuTTY and secure shell (SSH) keys to authenticate.
- [Secure Linux or Unix EC2 instances](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-securing-linux-unix-amazon-ec2-instances.html): Learn how to secure a Linux or Unix instance in Amazon Elastic Compute Cloud (Amazon EC2) created from an Amazon Lightsail snapshot by removing residual Lightsail keys for improved security.
- [Connect to Windows EC2 instances](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-windows-server-amazon-ec2-instances.html): Learn how to connect to your Windows Server instance in Amazon Elastic Compute Cloud created from an Amazon Lightsail snapshot using Remote Desktop Protocol (RDP) and the default Lightsail key pair.
- [Secure Windows EC2 instances](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-securing-windows-server-amazon-ec2-instances.html): Learn how to improve security for Windows Server instances in Amazon EC2 created from Lightsail snapshots by changing the default administrator password to remove associations with Lightsail key pairs.
- [CloudFormation stacks](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-cloudformation-stacks.html): Learn how to view and access the CloudFormation stacks created by Amazon Lightsail to provisionAmazon Elastic Compute Cloud instances from exported snapshots.


## [Domains and DNS](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-registration.html)

### [DNS in Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-dns-in-amazon-lightsail.html)

Learn how to route web traffic to your Amazon Lightsail instance using DNS records and manage your domain's DNS zone.

- [Create a DNS zone](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-create-dns-entry.html): Learn how to create an Amazon Lightsail DNS zone to manage your domain's DNS records and route traffic to Lightsail instances..
- [Edit a DNS zone](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-edit-or-delete-a-dns-zone.html): Learn how to edit DNS records for a DNS zone in Amazon Lightsail to manage your domain's DNS hosting.
- [Delete a DNS zone](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-delete-dns-zone.html): Learn how to delete a DNS zone in Amazon Lightsail to manage your domain's DNS hosting.
- [Internet traffic routing](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-internet-traffic-routing.html): Learn how Amazon Lightsail routes internet traffic via DNS to your website, instances, load balancers, and container services using domain name records.
- [Point domain to an instance](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-routing-to-instance.html): Learn how to point your domain to an Amazon Lightsail instance.
- [Point domain to a load balancer](https://docs.aws.amazon.com/lightsail/latest/userguide/add-alias-record-for-lightsail-load-balancer.html): Learn how to point your domain or subdomain to an Amazon Lightsail load balancer by adding an address (A) record in DNS zones or Amazon Route 53;.
- [Transfer DNS management](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-register-other-dns-service-procedure.html): Learn how to use Amazon Lightsail to transfer DNS record management for your registered domain to another DNS hosting provider while ensuring uninterrupted traffic routing during the transition.
- [Use Route 53](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-route-53-to-point-a-domain-to-an-instance.html): Learn how to point a domain to your Lightsail instance using Amazon Route 53, enabling custom domain routing, DNS record management, and enhanced configurability.
- [Register a domain](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-register-new-domain.html): Learn how to register a new domain using Amazon Lightsail.
- [Domain details](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-whois-rdap.html): Discover how to view registration details and contact information for .com, .net, and .org domains registered with Amazon Registrar through Amazon Lightsail or Route 53, using WHOIS or RDAP protocols.
- [Format domain names](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-name-format.html): Discover the domain name format guidelines for registering and managing DNS zones and records in Amazon Lightsail, including valid characters, wildcards, and subdomain handling.
- [Manage domain in R53](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-manage-domain-advanced.html): Learn how to manage your Amazon Lightsail domain using advanced features in Amazon Route 53, including viewing registration status, locking domains, restoring expired domains, transferring domains, and deleting registrations.
- [Registration information](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-register-values-specify.html): Learn how to register or transfer a domain with Amazon Lightsail and provide necessary information like registration term, contact details, privacy protection settings, and automatic renewal configuration.
- [Registration renewal](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-manage-auto-renew.html): Learn how to manage automatic domain renewal with Amazon Lightsail to easily renew or deactivate domain registration, ensuring uninterrupted access to your domain.
- [Privacy protection](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-privacy-protection.html): Learn how to manage privacy protection for domain contacts in Amazon Lightsail to hide or reveal contact information for WHOIS queries.
- [Update domain contact information](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-update-contacts.html): Learn how to update contact information for your registered domain in Amazon Lightsail, including registrant, administrator, and technical contacts, ensuring ownership verification and domain management.


## [Databases](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-databases.html)

- [Create a database](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-a-database.html): Create an Amazon Lightsail database with the latest MySQL or PostgreSQL version; configure high availability and allocate resources.
- [Select a database engine](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-choosing-a-database.html): Learn how to choose between MySQL and PostgreSQL databases in Amazon Lightsail for your project's requirements, and optimize data import based on database plan specifications.
- [High availability databases](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-high-availability-databases.html): Learn how high availability databases in Amazon Lightsail provide failover support for your managed database.
- [Connect to MySQL](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-your-mysql-database.html): Learn how to connect to your Amazon Lightsail MySQL database using a MySQL client application by obtaining the necessary connection details and configuring public availability for external connectivity.
- [Connect to MySQL using SSL](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-mysql-database-using-ssl.html): Learn how to securely connect to your Amazon Lightsail MySQL database using SSL/TLS encryption, verify server certificates, and download trusted SSL certificates for your AWS Region.
- [Connect to PostgreSQL](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-your-postgres-database.html): Learn how to connect to your Amazon Lightsail PostgreSQL database using standard PostgreSQL clients and utilities with endpoint, port, username, and password from the Lightsail console.
- [Connect to PostgreSQL using SSL](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-postgres-database-using-ssl.html): Discover how to securely connect to your Amazon Lightsail PostgreSQL database using SSL and a trusted root certificate, ensuring data protection and guarding against spoofing attacks.
- [Delete a database](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-your-database.html): Learn how to delete your Amazon Lightsail managed database when no longer needed, and optionally create a final snapshot before deletion.

### [Data import mode](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-database-data-import-mode.html)

Learn how to enable data import mode for your Amazon Lightsail managed database to suspend backup operations while importing large datasets, preventing delays.

- [Import SQL data](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-importing-data-into-your-mysql-database.html): Learn how to import SQL data into your Amazon Lightsail MySQL database using MySQL Workbench, enabling data transfer and management for your applications.
- [Import data PostgreSQL](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-importing-data-into-your-postgres-database.html): Learn how to import a PostgreSQL database backup file into your Amazon Lightsail managed database using pgAdmin, allowing you to restore data and configurations efficiently.

### [Database logs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-database-logs-and-history.html)

Learn how to view database logs and history in the Amazon Lightsail console to diagnose issues and monitor changes for your MySQL or PostgreSQL databases.

- [MySQL query logs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-enabling-mysql-general-and-slow-query-logs.html): Learn how to enable and control general and slow query logging for your Amazon Lightsail MySQL database to monitor queries and improve performance.
- [Disable point-in-time-backups](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-turn-off-database-point-in-time-backup.html): Learn how to disable point-in-time backups for Amazon Lightsail managed databases, enhancing data recovery capabilities using the AWS CLI or AWS CloudShell.

### [Database snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-a-database-snapshot.html)

Learn how to create a snapshot of your Amazon Lightsail database to backup and restore data easily.

- [Restore database](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-a-database-from-point-in-time-backup.html): Restore a failed database to a specific date and time in the last week using point-in-time backups in Amazon Lightsail.
- [Create database from snapshot](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-a-database-from-snapshot.html): Learn how to create a new managed database in Amazon Lightsail from a snapshot, offering the ability to change plans, ensure high availability, and leverage point-in-time backups for disaster recovery.

### [Download SSL certificate](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-download-ssl-certificate-for-managed-database.html)

Learn how to download an SSL/TLS certificate to securely connect your applications to Amazon Lightsail managed databases (MySQL, PostgreSQL) while ensuring data privacy.

- [Update CA certificate](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-modifying-database-to-use-a-specific-certificate.html): Learn how to update your Amazon Lightsail database to use a new SSL/TLS certificate for secure connections, improving security and compliance.
- [Maintenance and backup windows](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-preferred-maintenance-and-backup-windows.html): Learn how to change the preferred maintenance and backup window times for your Amazon Lightsail database to minimize downtime when database operations occur.
- [Manage database password](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-database-password.html): Learn how to view and change the password for your Amazon Lightsail database to secure database access, using the Lightsail console.
- [Public mode](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-database-public-mode.html): Learn how to configure public access mode for your Amazon Lightsail database, enabling external connections using the endpoint, port, username, and password.
- [Update parameters](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-updating-database-parameters.html): Learn how to list and update your Amazon Lightsail managed database parameters using the AWS CLI, allowing you to optimize performance and configure properties like connection limits or buffer pool size.
- [Upgrade major version](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-upgrade-database-major-version.html): Discover how to upgrade the major version of your Amazon Lightsail MySQL or PostgreSQL database to benefit from new features and improvements, using the AWS CLI and CloudShell.
- [Migrate from MySQL 5.6](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-migrate-mysql-56-to-newer-database.html): Learn how to migrate data from a MySQL 5.6 database to a newer MySQL version on Amazon Lightsail, ensuring compatibility for your applications.


## [Load balancers](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-lightsail-load-balancers.html)

- [Create load balancer](https://docs.aws.amazon.com/lightsail/latest/userguide/create-lightsail-load-balancer-and-attach-lightsail-instances.html): Learn how to create an Amazon Lightsail load balancer and attach instances to distribute traffic and handle increased web demand with redundancy.
- [Update load balancer settings](https://docs.aws.amazon.com/lightsail/latest/userguide/update-settings-for-lightsail-load-balancer-health-check-path-https-session-stickiness-persistence-cookie-duration.html): Learn how to customize Amazon Lightsail load balancer settings for health checks, HTTPS encryption, and session persistence to enhance performance and security.
- [Instance load balancing](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-lightsail-instances-for-load-balancing.html): Learn how to configure your Amazon Lightsail instances for load balancing to scale your applications horizontally.
- [Configure TLS security policy](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-load-balancer-tls-security-policy.html): Learn how to configure TLS security policies on your Amazon Lightsail load balancers.
- [HTTP to HTTPS redirect](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-load-balancer-https-redirection.html): Learn how to configure HTTP to HTTPS redirection for your Amazon Lightsail load balancer to automatically redirect users to an encrypted connection.
- [Session persistence](https://docs.aws.amazon.com/lightsail/latest/userguide/enable-session-stickiness-persistence-or-change-cookie-duration.html): Learn how to enable session persistence and manage cookie duration for your Amazon Lightsail load balancer to maintain user sessions and shopping carts.

### [Health checks](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-lightsail-load-balancer-health-checking.html)

Learn how to customize the health check path and monitor health check metrics for your Amazon Lightsail load balancer instances to ensure optimal performance.

- [Health checks](https://docs.aws.amazon.com/lightsail/latest/userguide/enable-set-up-health-checking-for-lightsail-load-balancer-metrics.html): Learn how to configure Amazon Lightsail load balancer health checks to monitor instance health and customize the health check path for optimal performance.
- [Detach instances](https://docs.aws.amazon.com/lightsail/latest/userguide/detach-lightsail-instances-from-load-balancer.html): Learn how to detach instances from your Amazon Lightsail load balancer to manage network traffic more efficiently.
- [Delete load balancers](https://docs.aws.amazon.com/lightsail/latest/userguide/delete-lightsail-load-balancer.html): Learn how to delete an Amazon Lightsail load balancer and its associated SSL/TLS certificates to optimize resource usage and costs.


## [Distributions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-content-delivery-network-distributions.html)

- [Create a distribution](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-content-delivery-network-distribution.html): Learn how to create an Amazon Lightsail content delivery network distribution to cache and serve your web content globally using the Lightsail console, configuring caching behavior, origin resource, and distribution plan.
- [Delete a distribution](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-distribution.html): Learn how to delete an Amazon Lightsail distribution directly from the console to manage your resources effectively.

### [Caching behavior](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-default-cache-behavior.html)

Discover how to configure caching behavior for yourAmazon Lightsail distribution, including presets, file overrides, and advanced settings to optimize performance and control content delivery.

- [Reset cache](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-resetting-distribution-cache.html): Learn how to reset the cache of your Amazon Lightsail distribution to ensure the latest content is served to users.
- [Change origin](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-distribution-origin.html): Learn how to change the content origin for your Amazon Lightsail distribution and configure the origin protocol policy for HTTP/HTTPS.
- [Use buckets with distributions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-distributions-with-buckets.html): Learn how to configure an Amazon Lightsail bucket as the origin of a content delivery network (CDN) distribution and integrate it with a WordPress website to serve media files efficiently.
- [Change plan](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lighstail-changing-distribution-plan.html): Learn how to change the plan of your Amazon Lightsail distribution to increase monthly data transfer quota and avoid overage charges.

### [Distribution custom domains](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-enabling-distribution-custom-domains.html)

Learn how to enable custom domains for your Amazon Lightsail distributions to use your registered domain names with your distributions.

- [Point your domain to a distribution](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-point-domain-to-distribution.html): Learn how to point your registered domains to your Amazon Lightsail distribution by adding alias records in your DNS zone to enable custom domain access for your web content delivery network.
- [Change custom domain](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-distribution-custom-domains.html): Learn how to change the custom domains used by your Amazon Lightsail distribution by updating the SSL/TLS certificate with new domains for content delivery network management.
- [Disable distribution custom domains](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-disabling-distribution-custom-domains.html): Discover how to disable custom domains for your Amazon Lightsail distribution, allowing traffic only through the default distribution domain and preventing access from previously associated custom domains.
- [Add distribution domain to container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-distribution-default-domain-to-container-service.html): Add a content delivery network (CDN) distribution's default domain to an Amazon Lightsail container service using the AWS Command Line Interface.
- [Request and response behaviors](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-distribution-request-and-response.html): Discover how Amazon Lightsail distributions process and forward requests to your origin, and handle responses from your origin, to deliver content efficiently with AWS's content delivery network (CDN).
- [Test distribution](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-testing-distribution.html): Learn how to test your Amazon Lightsail distribution to ensure it's caching and serving content correctly from your origin using browser developer tools.


## [Networking](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-networking-resources-in-lightsail.html)

### [IP addresses](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.html)

Learn how to view and manage IPv4 and IPv6 addresses for your Amazon Lightsail instances, container services, CDN distributions, and load balancers.

### [Static IP addresses](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-static-ip-addresses-in-amazon-lightsail.html)

Learn how to configure static IP addresses in Amazon Lightsail to ensure consistent public IP assignment for your instances.

- [Create a static IP address](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-create-static-ip.html): Learn how to create a static IP address and attach it to your Amazon Lightsail instance to prevent the public IP from changing when restarting, simplifying domain management.
- [Delete a static IP address](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-delete-static-ip.html): Learn how to delete a static IP address in Amazon Lightsail to free up resources and clean up your account.

### [Dual-stack networking](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-enable-disable-ipv6.html)

Learn how to enable or disable IPv6 networking for Amazon Lightsail instances, container services, and load balancers to support IPv4 and IPv6 communication.

- [Enable IPv6 networking for Lightsail resources](https://docs.aws.amazon.com/lightsail/latest/userguide/enable-ipv6.html): Learn how to enable IPv6 networking for Amazon Lightsail instances, CDN distributions, and load balancers to support IPv6 traffic and addresses.
- [Disable IPv6 networking for Lightsail resources](https://docs.aws.amazon.com/lightsail/latest/userguide/disable-ipv6.html): Learn how to disable IPv6 networking for Amazon Lightsail instances, CDN distributions, and load balancers.

### [IPv6-only networking](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-ipv6-only-plans.html)

Learn how to configure IPv6-only networking for Amazon Lightsail instances, ensuring IPv6 reachability and compatibility with supported blueprints.

- [Change networking type](https://docs.aws.amazon.com/lightsail/latest/userguide/migrate-to-ipv6-only-plan.html): Learn how to change the networking type of your Amazon Lightsail instance to IPv6-only or dual-stack for better connectivity and IPv6 compatibility.
- [IPv6 compatible blueprints](https://docs.aws.amazon.com/lightsail/latest/userguide/ipv6-only-blueprints.html): The following Lightsail blueprints are compatible with an IPv6-only instance plan

### [Regions and Availability Zones](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)

Learn how to create Amazon Lightsail resources in AWS Regions closest to your users, leveraging multiple Availability Zones for fault tolerance and high availability with your applications.

- [Enable Regions](https://docs.aws.amazon.com/lightsail/latest/userguide/opt-in-regions-for-lightsail-enable.html): Describes the process to enable an opt-in Region for Lightsail.
- [Disable Regions](https://docs.aws.amazon.com/lightsail/latest/userguide/opt-in-regions-for-lightsail-disable.html): Describes the considerations and process to disable an opt-in Region for Lightsail.
- [VPC peering](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-set-up-vpc-peering-with-aws-resources.html): Learn how to set up VPC peering to connect your Amazon Lightsail resources to AWS services outside Lightsail like Amazon RDS.

### [SSL/TLS Certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-tls-ssl-certificates-in-lightsail-https.html)

Learn how to enable HTTPS encryption with SSL/TLS certificates for your Amazon Lightsail load balancers, distributions, and container services.

### [Container certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-services-certificates.html)

Learn how to create SSL/TLS certificates for secure HTTPS connections to your Amazon Lightsail container services with custom domains.

- [Validate certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-validating-container-services-certificates.html): Learn how to validate SSL/TLS certificates for Amazon Lightsail container services by adding CNAME records to DNS zones, ensuring secure communication.
- [View certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-container-services-certificates.html): Learn how to view SSL/TLS certificates for your Amazon Lightsail container service to secure custom domains with HTTPS.

### [Distribution certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-create-a-distribution-certificate.html)

Create secure HTTPS connections for your Amazon Lightsail content delivery network (CDN) distributions using SSL/TLS certificates.

- [View SSL/TLS certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-distribution-certificates.html): Learn how to view SSL/TLS certificates attached to your Amazon Lightsail distribution to manage encryption and domain validation.
- [Validate SSL/TLS certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-validating-a-distribution-certificate.html): Learn how to validate SSL/TLS certificates for your Amazon Lightsail distribution by adding CNAME records to your domain's DNS zone, enabling secure custom domains.
- [Configure TLS protocol](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-distribution-tls-version.html): Learn how to configure the minimum TLS protocol version for your Amazon Lightsail distribution to enhance security and meet compliance requirements using the AWS CLI.
- [Delete distribution certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-distribution-certificates.html): Learn how to delete SSL/TLS certificates no longer used on your Amazon Lightsail distributions, including expired or replaced certificates.

### [Load balancer certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/create-tls-ssl-certificate-and-attach-to-lightsail-load-balancer-https.html)

Learn how to create an SSL/TLS certificate and attach it to your Amazon Lightsail load balancer to enable HTTPS for secure web traffic.

- [Add alternate domains](https://docs.aws.amazon.com/lightsail/latest/userguide/add-alternate-domain-names-to-tls-ssl-certificate-https.html): Learn how to add alternate domains and subdomains to your SSL/TLS certificate for your Lightsail load balancer.
- [Verify SSL/TLS certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/verify-tls-ssl-certificate-using-dns-cname-https.html): Learn how to verify ownership of domains and subdomains by adding CNAME records to your DNS zone for an SSL/TLS certificate in Amazon Lightsail.
- [Attach certificate to load balancer](https://docs.aws.amazon.com/lightsail/latest/userguide/attach-validated-certificate-to-load-balancer.html): Learn how to attach a validated SSL/TLS certificate to your Amazon Lightsail load balancer for secure data transfer.
- [Remove SSL/TLS certificate](https://docs.aws.amazon.com/lightsail/latest/userguide/delete-tls-ssl-certificate-lightsail-load-balancer-https.html): Learn how to delete SSL/TLS certificates from your Amazon Lightsail load balancer when no longer needed to secure HTTPS traffic.
- [Configure reverse DNS](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-reverse-dns.html): Learn how to configure reverse DNS for an email server on your Amazon Lightsail instance to prevent outbound messages from being marked as spam, by following prerequisites and submitting a request to Support.


## [Buckets](https://docs.aws.amazon.com/lightsail/latest/userguide/buckets-in-amazon-lightsail.html)

- [Create buckets](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-buckets.html): Learn how to create and manage Amazon Lightsail buckets for cost-effective object storage, including uploading files, configuring access permissions, monitoring metrics, and integrating with other AWS services.
- [Delete buckets](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-buckets.html): Learn how to permanently delete Amazon Lightsail object storage buckets, including when force deletion is required.
- [Create access keys](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-bucket-access-keys.html): Learn how to create bucket access keys, granting full access to objects, with Amazon Lightsail object storage for secure AWS API, SDK, and CLI access.
- [Delete access keys](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-bucket-access-keys.html): Learn how to delete access keys for Amazon Lightsail object object storage.
- [Block public access](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-block-public-access-for-buckets.html): Discover how to block public access to your Amazon Lightsail buckets and objects using account-level block public access configurations in Amazon S3.

### [Bucket access logs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bucket-access-logs.html)

Learn how to enable and use bucket access logs in Amazon Lightsail to track requests made to your object storage buckets for auditing, security, and customer analytics.

- [Access log format](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bucket-access-log-format.html): Discover how Amazon Lightsail bucket access logs work to track requests made to object storage buckets for auditing, security, and customer analysis.
- [Manage access logs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-enabling-bucket-access-logs.html): Learn how to enable or disable bucket access logging for your Amazon Lightsail object storage to track requests and analyze usage.
- [Use access logs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-bucket-access-logs.html): Use bucket access logs to identify, query, and analyze requests to an Amazon Lightsail bucket, enabling monitoring, troubleshooting, and security analysis through Amazon Athena.

### [Bucket objects](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-objects-in-a-bucket.html)

Discover how to view objects and folders stored in your Amazon Lightsail bucket using the console or AWS CLI, and learn about managing buckets and objects in the service.

- [Copy and move objects](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-copying-moving-bucket-objects.html): Learn how to copy and move objects between Amazon Lightsail object storage buckets using the console or AWS CLI, enabling efficient data management and organization across Lightsail locations and AWS Regions.
- [Delete objects](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-bucket-objects.html): Learn how to delete objects and object versions from your Amazon Lightsail buckets to free up storage space, using the Lightsail console or AWS CLI.
- [Download objects](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-downloading-bucket-objects.html): Learn how to download objects from an Amazon Lightsail bucket using the console or AWS CLI for efficient file retrieval and management.
- [Filter objects](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-filtering-bucket-objects.html): Learn how to filter objects in your Amazon Lightsail bucket using the console or AWS CLI to quickly find specific files by name prefix.
- [Manage object versioning](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-bucket-object-versioning.html): Learn how to enable and suspend object versioning in Amazon Lightsail's object storage service, keeping multiple versions of objects to recover from unintended actions or failures.
- [Restore object versions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-restoring-bucket-object-versions.html): Learn how to restore previous versions of objects in your Amazon Lightsail bucket to recover from unintended actions or failures, using the Lightsail console or AWS CLI.
- [Tag objects](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tagging-bucket-objects.html): Discover how to categorize bucket objects by tagging them with key-value pairs using the Amazon Lightsail console or AWS CLI, enabling easier organization and management.
- [Bucket resource access](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-bucket-resource-access.html): Learn how to configure resource access for an Amazon Lightsail bucket by attaching instances for programmatic access, ideal for software configurations like WordPress media storage.
- [Change bucket plans](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-bucket-plans.html): Learn how to change the storage plan for your Amazon Lightsail bucket to accommodate fluctuating usage and ensure sufficient storage space and data transfer quotas.
- [Configure access permissions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-bucket-permissions.html): Learn how to configure access permissions for your Amazon Lightsail bucket to control public read-only access to objects, enhancing security and privacy.
- [Cross-account access](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-bucket-cross-account-access.html): Learn how to configure cross-account access for an Amazon Lightsail bucket, allowing read-only access to objects for other AWS accounts and their users.
- [Individual object access permissions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-individual-object-access.html): Learn how to configure read-only public access for individual objects in an Amazon Lightsail bucket to securely share selected files while restricting others.
- [Multipart upload](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.html): Learn how to upload large files efficiently to your Amazon Lightsail bucket using multipart upload with improved throughput, quick recovery from network issues, and flexible upload scheduling.
- [Naming rules](https://docs.aws.amazon.com/lightsail/latest/userguide/bucket-naming-rules-in-amazon-lightsail.html): Understand bucket naming requirements to create compliant buckets for Amazon Lightsail object storage, including length, character set, and uniqueness rules.
- [Object key names](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-bucket-object-key-names-in-amazon-lightsail.html): Learn how to construct compliant object key names for your Amazon Lightsail bucket objects, including guidelines for safe characters, special handling, and XML constraints.
- [Object storage security best practices](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bucket-security-best-practices.html): Learn how to secure your Amazon Lightsail object storage buckets with best practices for access control, encryption, monitoring, and auditing to protect your data.
- [Bucket permissions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-understanding-bucket-permissions.html): Learn how to control access to Amazon Lightsail buckets and objects using permissions, cross-account access, access keys, and Lightsail instance resource access for secure object storage.
- [Upload files to bucket](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-uploading-files-to-a-bucket.html): Learn how to upload files and manage objects in Amazon Lightsail object storage buckets for secure data storage.

### [CORS in Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html)

Learn about cross-origin resource sharing (CORS) for your Lightsail object storage buckets and how to enable web applications from different domains to access your bucket resources.

- [How Lightsail evaluates CORS configurations](https://docs.aws.amazon.com/lightsail/latest/userguide/cors-how-evaluation-works.html): Learn about how cross-origin resource sharing (CORS) is evaluated in Lightsail.
- [Configure CORS using the AWS CLI](https://docs.aws.amazon.com/lightsail/latest/userguide/cors-configuration-cli.html): Learn how to configure cross-origin resource sharing (CORS) for Lightsail object storage buckets.
- [Troubleshooting CORS](https://docs.aws.amazon.com/lightsail/latest/userguide/cors-troubleshooting.html): Learn about troubleshooting cross-origin resource sharing (CORS) for Lightsail object storage buckets.


## [Container services](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services.html)

- [Create a container](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-services.html): Create highly available, scalable container services on Amazon Lightsail using preconfigured deployments or custom containers from public registries.

### [Container images](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-images.html)

Learn how to create and build Docker container images locally using a Dockerfile for deployment to Amazon Lightsail container services.

- [Manage container images](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-pushing-container-images.html): Learn how to push, view, and delete container images for your Amazon Lightsail container service from your local machine.
- [Install container services plugin](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-install-software.html): Learn how to install Docker, AWS CLI, and the Lightsail Control plugin to create and push container images for Amazon Lightsail container services.
- [ECR private repository access](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access.html): Learn how to grant your Amazon Lightsail container services access to Amazon Elastic Container Registry private repositories and deploy images from them.

### [Manage containers and deployments](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services-deployments.html)

Discover how to create and manage container service deployments on Amazon Lightsail to launch, configure, and manage your containerized applications.

- [Change container capacity](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-container-service-capacity.html): Learn how to dynamically scale and change the power of your Amazon Lightsail container service to adjust capacity without downtime.
- [Manage deployment versions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services-deployment-versions.html): Learn how to view and manage deployment versions for your Amazon Lightsail container services to launch or redeploy containers efficiently.
- [View container logs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-container-service-container-logs.html): View and analyze container logs for your Amazon Lightsail container service to diagnose operations and filter entries by date, term, or inclusion and exclusion.

### [Container service custom domains](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-enabling-container-services-custom-domains.html)

Learn how to enable and manage custom domains for your Amazon Lightsail container service to use registered domain names.

- [Point Lightsail domain to container](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-point-domain-to-container-service.html): Learn how to point your domain to an Amazon Lightsail container service by adding DNS records for routing traffic to your service's default domain.
- [Point Route 53 domain to container](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-route-53-alias-record-for-container-service.html): Use Route 53 to route domain traffic to an Amazon Lightsail container service by adding an alias record to your hosted zone.
- [Delete a container](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-container-services.html): Learn how to delete your Amazon Lightsail container service when it is no longer needed.


## [Security](https://docs.aws.amazon.com/lightsail/latest/userguide/security.html)

- [Infrastructure security](https://docs.aws.amazon.com/lightsail/latest/userguide/infrastructure-security.html): Learn how Amazon Lightsail isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/lightsail/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Lightsail features for data resiliency.

### [Identity and access management](https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam.html)

How to authenticate requests and manage access your Lightsail resources.

- [AWS managed policies](https://docs.aws.amazon.com/lightsail/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Lightsail and recent changes to those policies.

### [Lightsail policies and roles](https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html)

Learn how Amazon Lightsail works with AWS Identity and Access Management.

- [Identity-based policy examples](https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_id-based-policy-examples.html): Discover how to grant least-privilege permissions for Amazon Lightsail using IAM identity-based policies, including allowing resource creation and deletion based on tags.
- [Resource-level permissions policy examples](https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_resource-based-policy-examples.html): Discover how to manage specific Amazon Lightsail instances and databases using resource-level permissions in IAM policies to control access and actions.
- [Use service-linked roles](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html): Learn how to use service-linked roles to give Amazon Lightsail access to resources in your AWS account.
- [Manage buckets with IAM](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bucket-management-policies.html): Learn how to manage Amazon Lightsail object storage buckets, including creating, securing, logging, uploading files, versioning objects, monitoring utilization, and connecting to other resources.
- [Manage IAM user access](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-access-for-an-iam-user.html): Learn how to manage access to Amazon Lightsail for an IAM user by creating an IAM policy, group, and user with Lightsail permissions.
- [Update management](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-update-management.html): Use Amazon Lightsail update management to keep your instances and container services secure by regularly updating, patching, and securing the operating system and applications following vendor guidance.
- [Compliance validation](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-compliance.html): Discover how AWS provides resources to help meet compliance requirements, including deployment guides, workbooks, AWS Config for evaluating resource configurations, and AWS Security Hub CSPM for a comprehensive security overview.
- [AWS PrivateLink](https://docs.aws.amazon.com/lightsail/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and Amazon Lightsail.


## [Monitor performance](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-resource-health-metrics.html)

### [Resource health metrics](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-instance-health-metrics-in-amazon-lightsail.html)

Discover how Amazon Lightsail resource metrics work to monitor and troubleshoot instances, databases, distributions, load balancers, containers, and buckets.

- [Metric notifications](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications.html): Learn how to configure notifications for Amazon Lightsail resources to monitor metrics, receive alerts when thresholds are crossed, and manage contacts for email and SMS notifications.
- [View instance metrics](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-health-metrics.html): Learn how to view and monitor CPU, network, status check, and metadata metrics for Amazon Lightsail instances to optimize performance and availability.
- [Metric alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms.html): Learn how to configure metric alarms to monitor Amazon Lightsail resources like instances, databases, load balancers, and CDN distributions, and receive notifications when thresholds are breached.
- [Create instance alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-instance-health-metric-alarms.html): Create instance alarms to monitor metrics and receive notifications for Amazon Lightsail resources.
- [Delete or disable alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-health-metric-alarms.html): Learn how to delete or disable Amazon Lightsail metric alarms to stop notifications when monitored metrics cross thresholds.

### [Bucket metrics](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-bucket-metrics.html)

Discover how to view and monitor Amazon Lightsail bucket metrics to ensure optimal performance and storage utilization for your object storage needs.

- [Create alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-bucket-metric-alarms.html): Discover how to create and manage metric alarms for Amazon Lightsail buckets to monitor storage usage and capacity.
- [Container metrics](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-container-services-metrics.html): Learn how to view metrics for your Amazon Lightsail container service to monitor CPU and memory utilization across all nodes.

### [Database metrics](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-database-health-metrics.html)

Learn how to view and monitor database metrics in Amazon Lightsail to maintain resource reliability, availability, and performance for your database.

- [Create database alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-database-health-metric-alarms.html): Learn how to create and test database health metric alarms in Amazon Lightsail to monitor performance and receive notifications.

### [Distribution metrics](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-distribution-health-metrics.html)

Learn how to view distribution health metrics like requests, bytes uploaded and downloaded, and error rates in the Amazon Lightsail console to monitor performance.

- [Create distribution alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-distribution-health-metric-alarms.html): Use metric alerts to monitor your Amazon Lightsail distribution's health and receive timely notifications.

### [Load balancer metrics](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-load-balancer-health-metrics.html)

Learn how to view and monitor load balancer health metrics on Amazon Lightsail to maintain reliability, availability, and performance of your resources.

- [Load balancer alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-load-balancer-health-metric-alarms.html): Learn how to create, configure, and test Amazon Lightsail load balancer alarms for monitoring metrics and receiving notifications based on defined thresholds.
- [Add notification contacts](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-editing-notification-contacts.html): Learn how to configure Amazon Lightsail to notify you through email or SMS when resource metrics cross thresholds, by adding and verifying notification contacts.
- [Delete notification contacts](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-notification-contacts.html): Learn how to delete notification contacts in Amazon Lightsail to stop receiving email and SMS notifications for your resources.
- [Review Lightsail alarm notifications](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarm-notifications.html): Learn how you can review alarm notifications for your resources and contacts pending verification in the Lightsail console.


## [Tags](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags.html)

- [Add tags](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-adding-tags-to-a-resource.html): Learn how to categorize your Amazon Lightsail resources using tags for organization, cost tracking, and access control by adding tags through the console.
- [Delete tags](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-tags.html): Learn how to remove tags from Amazon Lightsail resources like instances, containers, CDN distributions, buckets, databases, disks, DNS zones, and load balancers.
- [Permissions and authorization based on tags](https://docs.aws.amazon.com/lightsail/latest/userguide/resource-level-permissions-and-auth-based-on-tags-support.html): Learn how to use resource-level permissions and tag-based authorization with Amazon Lightsail API actions for enhanced access control and security.
- [Use tags to control access](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags.html): Learn how to control access to Amazon Lightsail resources using tags for IAM policies, restricting resource creation, deletion, and tag modification based on defined key-value pairs.
- [Use tags to organize costs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-organizing-costs-using-tags.html): Use tags to organize your Amazon Lightsail resource costs for better billing visibility; activate user-defined tags in the AWS Billing console, and generate cost allocation reports filtered by tag keys.
- [Use tags to organize resources](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-organizing-resources-using-tags.html): Use tags to organize and filter your Amazon Lightsail resources like instances, containers, and databases for better visibility and management.


## [Troubleshooting](https://docs.aws.amazon.com/lightsail/latest/userguide/troubleshooting.html)

### [WordPress setup](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-troubleshooting-wp-setup.html)

Learn how to troubleshoot WordPress setup failures, resolve common errors like DNS misconfiguration, deprecated repositories, and rate limits for Let's Encrypt certificates on your Amazon Lightsail instance.

- [Common errors](https://docs.aws.amazon.com/lightsail/latest/userguide/wp-setup-common-errors.html): Learn how to troubleshoot and fix common errors that occur during WordPress setup on Amazon Lightsail, including DNS, connectivity, version compatibility, and firewall port issues, ensuring seamless WordPress site deployment.
- [Setup failures](https://docs.aws.amazon.com/lightsail/latest/userguide/wordpress-setup-failures.html): Learn how to troubleshoot and resolve WordPress setup failures in Amazon Lightsail.
- [403 error (unauthorized)](https://docs.aws.amazon.com/lightsail/latest/userguide/create-policy-that-grants-access-to-amazon-lightsail.html): Learn how to troubleshoot and resolve a 403 (unauthorized) error when accessing the Amazon Lightsail console by managing IAM user access and contacting Support.
- [Block storage disks](https://docs.aws.amazon.com/lightsail/latest/userguide/troubleshooting-block-storage-disk-issues.html): Troubleshoot common issues with Amazon Lightsail block storage disks, including deleting attached disks, disk errors, detaching disks from running instances, disk size limits, disk quota limits, and attaching disks in different Availability Zones.
- [Browser-based SSH or RDP client](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-troubleshooting-browser-based-ssh-rdp-client-connection.html): Troubleshoot connectivity issues with Amazon Lightsail's browser-based SSH and RDP clients, resolving error messages like "Can't connect" or "Can't connect right now" for seamless instance access.
- [Ghost service unavailable](https://docs.aws.amazon.com/lightsail/latest/userguide/troubleshoot-ghost-instance-service-unavailable.html): Learn how to troubleshoot and resolve a 503 service unavailable error for a Ghost instance on Amazon Lightsail by restarting the Ghost service.
- [IAM issues](https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_troubleshoot.html): Learn about resource-based policies in Amazon Lightsail.
- [IPv6 reachability](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-ipv6-reachability.html): Learn how to verify IPv6 connectivity and test reachability from your local computer to an Amazon Lightsail instance using ping, enabling IPv6, and configuring firewall rules.
- [Insufficient instance capacity error](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-instance-capacity.html): Learn how to resolve insufficient instance capacity errors in Amazon Lightsail by trying alternative Availability Zones, reducing instance counts, choosing different instance plans, or creating new instances from snapshots to get capacity.
- [Load balancers](https://docs.aws.amazon.com/lightsail/latest/userguide/troubleshooting-lightsail-load-balancer-issues.html): Learn how to troubleshoot common issues with Amazon Lightsail load balancers, including certificate quotas, instance attachment limits, and instance availability for load balancing.
- [Notifications](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-troubleshooting-notifications.html): Discover how to troubleshoot notification issues in Amazon Lightsail, including verifying email addresses, resending verification requests, and managing SMS text message opt-outs for seamless notification delivery.
- [SSL/TLS certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/troubleshooting-tls-ssl-certificate-issues.html): Learn how to troubleshoot SSL/TLS certificate issues Amazon Lightsail, including quotas, failed requests, and invalid domain verification.


## [Tutorials](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-tutorials.html)

### [Quick start guides](https://docs.aws.amazon.com/lightsail/latest/userguide/quick-start-chapter.html)

Discover how to quickly get started with Amazon Lightsail blueprints for various applications like WordPress, cPanel, Drupal, and Node.js using step-by-step guides.

### [AlmaLinux](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-almalinux.html)

Learn how to create and configure an AlmaLinux instance on Amazon Lightsail, including selecting instance location and plan, setting up networking and security, and migrating data from CentOS.

- [Migrate to AlmaLinux](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-migrate-centos-to-almalinux.html): Learn how to migrate your data from a CentOS instance to an AlmaLinux instance on Amazon Lightsail by transferring files or moving block storage disks.
- [cPanel & WHM](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-cpanel.html): Learn how to configure and manage your cPanel & WHM instance on Amazon Lightsail for hosting websites, email, and other web services.
- [Drupal](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-drupal.html): Discover how to configure and customize your Drupal website on Amazon Lightsail, including setting up domains, enabling HTTPS, and creating instance snapshots.
- [Ghost](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-ghost.html): Learn how to get your Ghost website up and running on Amazon Lightsail, including configuring domains, SSL certificates, and backups.
- [GitLab CE](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-gitlab.html): Learn how to set up and configure a GitLab CE instance on Amazon Lightsail, including accessing the admin area, attaching a static IP, securing with HTTPS, and configuring DNS.
- [Joomla!](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-joomla.html): Learn how to get started with your Joomla! instance on Amazon Lightsail, including accessing the control panel, configuring domain and HTTPS, and managing your website.
- [LAMP](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-lamp.html): Learn how to get started with your LAMP instance on Amazon Lightsail, including getting the application password, attaching a static IP, visiting the welcome page, mapping your domain, reading Bitnami documentation, and creating snapshots for backups.
- [Magento](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-magento.html): Learn how to set up and configure Magento on Amazon Lightsail, including securing your website with HTTPS and configuring email notifications.
- [Nginx](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-nginx.html): Learn how to deploy and manage an Nginx web server on Amazon Lightsail, including securing with SSL, attaching static IPs, and mapping domains.
- [Node.js](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-nodejs.html): Learn how to get started with your Node.js instance on Amazon Lightsail, including obtaining the application password, creating a static IP, visiting the welcome page, mapping your domain, reading Bitnami documentation, and creating a snapshot.
- [OpenClaw](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-openclaw.html): Learn how to get started with OpenClaw on Amazon Lightsail, including pairing your browser, enabling AI capabilities with Amazon Bedrock, connecting messaging channels, and creating snapshots for backups.
- [Plesk](https://docs.aws.amazon.com/lightsail/latest/userguide/set-up-and-configure-plesk-stack-on-lightsail.html): Learn how to create a Plesk hosting stack on Amazon Lightsail.
- [PrestaShop](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-prestashop.html): Learn how to set up and configure a PrestaShop website on Amazon Lightsail, including retrieving passwords, attaching static IPs, signing in to the administration dashboard, configuring domains and HTTPS, setting up email notifications, and creating instance snapshots.
- [Redmine](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-redmine.html): Learn how to configure and customize your Redmine instance on Amazon Lightsail for project management, including securing it with HTTPS and using a custom domain.
- [Ruby on Rails](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-rubyonrails.html): Learn how to get started with your Ruby on Rails instance on Amazon Lightsail, including attaching a static IP, accessing the application, deploying your application, and creating snapshots for backups.
- [WordPress](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-wordpress.html): Learn how to launch and configure a WordPress instance on Amazon Lightsail, including creating a WordPress instance, configuring domains, DNS, static IP, SSL/TLS certificates, and accessing the admin dashboard.
- [WordPress Multisite](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-quick-start-guide-wordpress-multisite.html): Learn how to set up and configure a WordPress Multisite instance on Amazon Lightsail for hosting multiple blogs with domains or subdomains.

### [Bitnami](https://docs.aws.amazon.com/lightsail/latest/userguide/bitnami-tutorials.html)

Learn how to work with Bitnami pre-packaged applications and development stacks on Amazon Lightsail using tutorials for user authentication, banner removal, and more Bitnami features.

- [Bitnami user name and password](https://docs.aws.amazon.com/lightsail/latest/userguide/log-in-to-your-bitnami-application-running-on-amazon-lightsail.html): Learn how to obtain the default application and database user names and passwords to sign in and administer Bitnami instances such as WordPress, Joomla, and Drupal on Amazon Lightsail.
- [Remove Bitnami banner](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-remove-bitnami-banner.html): Remove the Bitnami banner from your Amazon Lightsail Bitnami blueprint instance.

### [WordPress](https://docs.aws.amazon.com/lightsail/latest/userguide/wordpress-tutorials.html)

Learn how to configure and manage WordPress websites and blogs on Amazon Lightsail, including connecting to databases, storage, CDN, and enabling HTTPS.

- [Configure WordPress](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tutorial-launching-and-configuring-wordpress.html): Learn how to launch and configure a WordPress instance on Amazon Lightsail to host your website or blog with ease, including setting up a domain, securing traffic with HTTPS, and accessing the admin dashboard.
- [Connect to Amazon S3](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-wordpress-to-amazon-s3.html): Use the WP Offload Media plugin to connect your WordPress website on Amazon Lightsail to an Amazon Simple Storage Service bucket for storing media files.
- [Connect to Aurora DB](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connect-wordpress-instance-to-aurora-database.html): Learn how to connect a WordPress instance on Amazon Lightsail to an Amazon Aurora database for enhanced data durability and availability, ensuring your website data remains protected.
- [Connect to MySQL](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connect-wordpress-to-mysql-managed-database.html): Learn how to transfer your WordPress website data to a MySQL managed database in Amazon Lightsail, enhancing data security and recoverability for posts, pages, and users.
- [Connect to a storage bucket](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-buckets-to-wordpress.html): Learn how to connect your WordPress website running on an Amazon Lightsail instance to a Lightsail bucket for hosting static content like images and attachments using the WP Offload Media Lite plugin.
- [Configure a CDN](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-editing-wp-config-for-distribution.html): Learn how to configure your WordPress instance to work seamlessly with an Amazon Lightsail content delivery network distribution for optimized performance and caching.
- [Enable email](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-enabling-email-on-wordpress.html): Learn how to enable email on your WordPress instance in Amazon Lightsail by configuring Amazon Simple Email Service (Amazon SES) and the WP Mail SMTP plugin.
- [Enable HTTPS](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-enabling-https-on-wordpress.html): Learn how to enable HTTPS for your WordPress website on Amazon Lightsail, enhancing security and search ranking by using the Bitnami HTTPS configuration tool (`bncert`) to request and automatically renew Let's Encrypt SSL/TLS certificates.
- [Migrate to Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/migrate-your-wordpress-blog-to-amazon-lightsail.html): Learn how to migrate your existing WordPress blog to Amazon Lightsail, AWS's easy-to-use virtual private server, enjoying full control over plugins, themes, and more with affordable pricing plans.

### [WordPress Multisite](https://docs.aws.amazon.com/lightsail/latest/userguide/wordpress-multisite-tutorials.html)

Learn how to manage multiple websites from the same WordPress instance with WordPress Multisite tutorials for Amazon Lightsail.

- [WordPress Multisite: Add blogs as domains](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-add-blogs-as-domains-to-your-wordpress-multisite.html): Add new blog sites using different domains to your WordPress Multisite instance on Amazon Lightsail. for efficient content management.
- [WordPress Multisite: Add blogs as subdomains](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-add-blogs-as-subdomains-to-your-wordpress-multisite.html): Learn how to add blogs as subdomains to your WordPress Multisite instance on Amazon Lightsail, enabling multiple sites under one domain for better organization and management.
- [WordPress Multisite: Define domain](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-define-the-primary-domain-for-your-wordpress-multisite.html): Learn how to define the primary domain to use for the main blog of your WordPress Multisite instance in Amazon Lightsail.

### [Let's Encrypt](https://docs.aws.amazon.com/lightsail/latest/userguide/lets-encrypt-tutorials.html)

Learn how to enable secure, encrypted communication for websites, applications, and online services hosted on Amazon Lightsail using free SSL/TLS certificates from Let's Encrypt.

- [LAMP Let's Encrypt certificate](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-lets-encrypt-certificates-with-lamp.html): Use Certbot to request a Let's Encrypt SSL wildcard certificate and integrate it with your Amazon Lightsail LAMP instance to secure your website or application.
- [NGINX Let's Encrypt certificate](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-lets-encrypt-certificates-with-nginx.html): Learn how to secure your Amazon Lightsail NGINX website with free Let's Encrypt SSL/TLS certificates for HTTPS encryption and automated renewal.
- [WordPress Let's Encrypt certificate](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-lets-encrypt-certificates-with-wordpress.html): Learn how to secure your Amazon Lightsail WordPress instance with free Let's Encrypt SSL/TLS certificates and integrate them using the Really Simple SSL plugin.

### [IPv6 networking](https://docs.aws.amazon.com/lightsail/latest/userguide/network-tutorials.html)

Learn how to configure IPv6 networking on Amazon Lightsail instances.

- [IPv6 for cPanel and WHM](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-ipv6-on-cpanel.html): Learn how to configure IPv6 on cPanel instances in Amazon Lightsail by enabling IPv6, editing network interface configuration, and updating cPanel settings to utilize the assigned IPv6 address.
- [IPv6 for GitLab](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-ipv6-on-gitlab.html): Learn how to configure IPv6 for GitLab instances on Amazon Lightsail by enabling IPv6, rebooting the instance, and verifying IPv6 address recognition.
- [IPv6 for Nginx](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-ipv6-on-nginx.html): Learn how to configure IPv6 on Nginx instances in Amazon Lightsail to enable IPv6 connectivity for web hosting.
- [IPv6 for Plesk](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-ipv6-on-plesk.html): Learn how to configure IPv6 on Plesk instances in Amazon Lightsail to enable public IPv6 addresses for enhanced connectivity.
- [AWS CLI for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-set-up-and-configure-aws-cli.html): Learn how to set up and configure the AWS Command Line Interface (AWS CLI) to control Amazon Lightsail through terminal commands for advanced users and developers.
- [AWS CloudShell](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-cloudshell.html): Learn how to use AWS CloudShell, a browser-based shell, to manage your Lightsail resources through the command line and pre-installed tools like the AWS CLI.

### [Launch and configure LAMP](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tutorial-launching-and-configuring-lamp.html)

Learn how to launch and configure a LAMP (Linux, Apache, MySQL, PHP) instance on Amazon Lightsail to quickly deploy your PHP applications or install Bitnami applications like WordPress, Drupal, and Magento.

- [Connect a LAMP instance to an Aurora database](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connect-lamp-instance-to-aurora-database.html): Learn how to connect an Amazon Lightsail LAMP instance to an Amazon Aurora database for secure, managed MySQL storage and transfer application data seamlessly.
- [Launch and configure Windows Server 2016](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tutorial-launching-and-configuring-windows-server-2016.html): Learn how to launch and configure a Windows Server 2016 instance on Amazon Lightsail, including steps to connect via RDP, create a static IP, and map a domain.
- [CloudTrail logging](https://docs.aws.amazon.com/lightsail/latest/userguide/logging-lightsail-api-calls-using-aws-cloudtrail.html): Discover how AWS CloudTrail captures Amazon Lightsail API calls, enabling you to monitor and audit actions taken on your Lightsail resources for security and compliance.
- [Create a HAR file](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-create-har-file.html): Learn how to create a HAR file to troubleshoot issues with the Amazon Lightsail console or virtual private servers, and submit it securely to Support.
- [Install Prometheus](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-install-prometheus.html): Use Prometheus, an open-source monitoring tool, to track system resources and applications with time-series data collection, querying, and visualization on Amazon Lightsail Linux instances.
- [Transfer files with scp](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-transfer-files-between-linux-instances.html): Learn how to securely transfer files between Linux instances on Amazon Lightsail using the scp command and SSH keys.
- [Work with other AWS services](https://docs.aws.amazon.com/lightsail/latest/userguide/using-lightsail-with-other-aws-services.html): Discover how to integrate Amazon Lightsail resources with other AWS services through VPC peering for enhanced capabilities and advanced features.
- [AWS CloudFormation resources](https://docs.aws.amazon.com/lightsail/latest/userguide/creating-resources-with-cloudformation.html): Learn about how to create resources for Amazon Lightsail using an AWS CloudFormation template.
- [Additional information about Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-additional-resources.html): Discover how to leverage Amazon Lightsail's additional resources, including blogs, tutorials, and videos, to learn about deploying various applications, configurations, and best practices on this easy-to-use cloud platform.


## [FAQs](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-frequently-asked-questions-faq.html)

- [About Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-frequently-asked-questions-faq-general.html): Learn how Amazon Lightsail simplifies cloud computing, enabling easy deployment and management of websites, web apps, virtual private servers, databases, and more with predictable, low-cost pricing.
- [Billing and account management](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.html): Learn about billing, account management, and data transfer allowance in Amazon Lightsail.
- [Data transfer](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-data-transfer-allowance.html): Frequently asked questions about data transfer in Amazon Lightsail.
- [Block storage (Disks)](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-block-storage.html): Discover how block storage disks work in Amazon Lightsail.
- [Certificates](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-certificates.html): Discover how SSL/TLS certificates work in Amazon Lightsail.
- [Contacts and monitoring notifications](https://docs.aws.amazon.com/lightsail/latest/userguide/faq-contacts-and-notifications.html): Learn how to configure notifications and contacts for monitoring Amazon Lightsail instances, databases, and load balancers across AWS Regions using email and SMS.
- [Container services](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-containers.html): Discover how container services work in Amazon Lightsail.
- [Content delivery network distributions](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-cdn-distributions.html): Discover how Content delivery network distributions work in Amazon Lightsail.
- [Databases](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-databases.html): Discover how managed databases work in Amazon Lightsail.
- [Domains](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-domains.html): Discover how domains work in Amazon Lightsail.
- [Export resources to Amazon EC2](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-export-to-ec2.html): Discover how exports work in Amazon Lightsail.
- [Instances](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-instances.html): Discover how instances (virtual private servers) work in Amazon Lightsail.
- [Load balancers](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-load-balancers.html): Discover how load balancers work in Amazon Lightsail.
- [Snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-snapshots.html): Discover how snapshots work in Amazon Lightsail.
- [Metrics and alarms](https://docs.aws.amazon.com/lightsail/latest/userguide/faq-metrics-and-alarms.html): Learn how to monitor and maintain resource reliability, availability, and performance with Amazon Lightsail metrics and alarms for instances, databases, and load balancers.
- [Networking](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-networking.html): Learn about networking and IP addresses in Amazon Lightsail.
- [Object storage (Buckets)](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-buckets.html): Discover how object storage buckets work in Amazon Lightsail.
- [Tags in Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-tagging.html): Discover how tags work in Amazon Lightsail.
