# Source: https://docs.aws.amazon.com/linux/al2/ug/llms.txt

# Amazon Linux 2 User Guide

> Describes key concepts of AL2 and provides instructions for using key features of AL2.

- [What is Amazon Linux 2?](https://docs.aws.amazon.com/linux/al2/ug/what-is-amazon-linux.html)
- [Prepare your migration to AL2023](https://docs.aws.amazon.com/linux/al2/ug/prepare-for-al2023.html)
- [AL2 Limitations](https://docs.aws.amazon.com/linux/al2/ug/limitations.html)
- [AWS integration in AL2](https://docs.aws.amazon.com/linux/al2/ug/aws-integration.html)
- [AL2 Source Packages](https://docs.aws.amazon.com/linux/al2/ug/amazon-linux-source-packages.html)

## [Deprecated functionality](https://docs.aws.amazon.com/linux/al2/ug/deprecated.html)

- [Deprecated functionality discontinued in AL1, removed in AL2](https://docs.aws.amazon.com/linux/al2/ug/deprecated-al1.html): This section describes functionality that is available in AL1, and is no longer available in AL2.

### [Functionality deprecated in AL2 and removed in AL2023](https://docs.aws.amazon.com/linux/al2/ug/deprecated-al2.html)

This section describes functionality that is available in AL2, and no longer available in AL2023.

- [ftp Package](https://docs.aws.amazon.com/linux/al2/ug/ftp-package-exclusion.html): Learn about the deprecation of the legacy FTP package, and recommended alternatives for migrating to AL2023.


## [Compare AL1 and AL2](https://docs.aws.amazon.com/linux/al2/ug/compare-with-al1.html)

- [AL1 and AL2 AMI comparison](https://docs.aws.amazon.com/linux/al2/ug/amzn1-amzn2-ami.html): Compares the packages on the AL1 and Amazon Linux 2 (AL2) AMIs.
- [AL1 and AL2 container comparison](https://docs.aws.amazon.com/linux/al2/ug/amzn1-amzn2-container.html): A comparison of packages on the AL1 and AL2 base container images.


## [AL2 on Amazon EC2](https://docs.aws.amazon.com/linux/al2/ug/ec2.html)

- [Using cloud-init on AL2](https://docs.aws.amazon.com/linux/al2/ug/amazon-linux-cloud-init.html): The cloud-init package is an open-source application built by Canonical that is used to bootstrap Linux images in a cloud computing environment, such as Amazon EC2.

### [Configure instances](https://docs.aws.amazon.com/linux/al2/ug/configure-ec2-instance.html)

Customize your AL2 instance.

### [Manage software](https://docs.aws.amazon.com/linux/al2/ug/managing-software.html)

Manage software on an Amazon Linux instance.

- [Update software](https://docs.aws.amazon.com/linux/al2/ug/install-updates.html): Update a single software package or all packages within an AL2 instance.
- [Add repositories](https://docs.aws.amazon.com/linux/al2/ug/add-repositories.html): Add additional software repositories to an AL2 instance.
- [Find and install software packages](https://docs.aws.amazon.com/linux/al2/ug/find-install-software.html): Find and install available software packages in your configured repositories using the yum search command.
- [Prepare to compile software](https://docs.aws.amazon.com/linux/al2/ug/compile-software.html): Install development tools to compile software.
- [Processor state control](https://docs.aws.amazon.com/linux/al2/ug/processor_state_control.html): Some EC2 instance types provide the ability for an operating system to control processor C-states and P-states.
- [I/O scheduler](https://docs.aws.amazon.com/linux/al2/ug/io-scheduler.html): The I/O scheduler is a part of the Linux operating system that sorts and merges I/O requests and determines the order in which they are processed.
- [Change the hostname](https://docs.aws.amazon.com/linux/al2/ug/set-hostname.html): Set the hostname for your Amazon Linux instance using a dynamic DNS provider.
- [Set up dynamic DNS](https://docs.aws.amazon.com/linux/al2/ug/dynamic-dns.html): Use a dynamic DNS provider with Amazon EC2 and configure the instance to update the IP address associated with a public DNS name each time the instance starts.
- [Configure network interfaces using ec2-net-utils](https://docs.aws.amazon.com/linux/al2/ug/ec2-net-utils.html): Amazon Linux 2 AMIs may contain additional scripts installed by AWS, known as ec2-net-utils.
- [User provided kernels](https://docs.aws.amazon.com/linux/al2/ug/UserProvidedKernels.html): Use custom kernels with your Linux instances.
- [AL2 AMI release notifications](https://docs.aws.amazon.com/linux/al2/ug/linux-ami-notifications.html): To be notified when new Amazon Linux AMIs are released, you can subscribe using Amazon SNS.
- [Configure the MATE desktop connection](https://docs.aws.amazon.com/linux/al2/ug/amazon-linux-ami-mate.html): Steps to launch and connect to an Amazon EC2 instance that was created with the AL2 AMI that includes .Net Core, PowerShell, Mono, and the MATE Desktop Environment.

### [AL2 Tutorials](https://docs.aws.amazon.com/linux/al2/ug/al2-tutorials.html)

Tutorials for using AL2 on Amazon EC2.

- [Install LAMP on AL2](https://docs.aws.amazon.com/linux/al2/ug/ec2-lamp-amazon-linux-2.html): Install the Apache web server with PHP and MariaDB support on your Amazon EC2 AL2 instance.
- [Configure SSL/TLS on AL2](https://docs.aws.amazon.com/linux/al2/ug/SSL-on-amazon-linux-2.html): Install and configure SSL/TLS on a single EC2 instance running AL2 and Apache web server.
- [Host a WordPress blog on AL2](https://docs.aws.amazon.com/linux/al2/ug/hosting-wordpress.html): Tutorial to install, configure, and secure a WordPress blog on your EC2 instance.


## [AL2 outside Amazon EC2](https://docs.aws.amazon.com/linux/al2/ug/outside-ec2.html)

- [Run AL2 on premises](https://docs.aws.amazon.com/linux/al2/ug/amazon-linux-2-virtual-machine.html): Use the AL2 virtual machine (VM) images for on-premises development and testing.


## [Identifying Amazon Linux versions](https://docs.aws.amazon.com/linux/al2/ug/identifying.html)

- [/etc/os-release](https://docs.aws.amazon.com/linux/al2/ug/ident-os-release.html): Amazon Linux supports the os-release standard for determining the OS and OS version.
- [Amazon Linux Specific](https://docs.aws.amazon.com/linux/al2/ug/ident-amazon-linux-specific.html): There are some files that are specific to Amazon Linux that can be used for identifying Amazon Linux and what version it is.
- [Example code](https://docs.aws.amazon.com/linux/al2/ug/ident-example-code.html): Code examples for programmatically detecting operating systems and versions.


## [Programming languages and runtimes](https://docs.aws.amazon.com/linux/al2/ug/language-runtimes.html)

- [C/C++ and Fortran](https://docs.aws.amazon.com/linux/al2/ug/c-cplusplus.html): AL2 includes both the GNU Compiler Collection (GCC) and the Clang frontend for LLVM.
- [Go in AL2](https://docs.aws.amazon.com/linux/al2/ug/go.html): You might want to build your own code written in Go on Amazon Linux using a toolchain provided with AL2.
- [Java](https://docs.aws.amazon.com/linux/al2/ug/java.html): AL2 provides several versions of Amazon Corretto to support Java based workloads, as well as some OpenJDK versions.
- [Perl](https://docs.aws.amazon.com/linux/al2/ug/perl.html): AL2 provides version 5.16 of the Perl programming language.
- [PHP](https://docs.aws.amazon.com/linux/al2/ug/php.html): AL2 currently provides two fully supported versions of the PHP programming language as part of .
- [Python in AL2](https://docs.aws.amazon.com/linux/al2/ug/python.html): AL2 provides support and security patches for Python 2.7 until June 2026, as part of our long-term support commitment for AL2 core packages.
- [Rust in AL2](https://docs.aws.amazon.com/linux/al2/ug/rust.html): You might want to build your own code written in Rust on AL2 using a toolchain provided with AL2.


## [AL2 kernel](https://docs.aws.amazon.com/linux/al2/ug/kernel.html)

- [AL2 supported kernels](https://docs.aws.amazon.com/linux/al2/ug/aml2-kernel.html): Supported kernel versions
- [Kernel Live Patching](https://docs.aws.amazon.com/linux/al2/ug/al2-live-patching.html)


## [AL2 Extras](https://docs.aws.amazon.com/linux/al2/ug/al2-extras.html)

- [List of Amazon Linux 2 Extras](https://docs.aws.amazon.com/linux/al2/ug/al2-extras-list.html): A list of Amazon Linux 2 (AL2) Extras.


## [AL2 Reserved Users and Groups](https://docs.aws.amazon.com/linux/al2/ug/reserved-users-groups.html)

- [List of Amazon Linux 2 Reserved Users](https://docs.aws.amazon.com/linux/al2/ug/al2-reserved-users-list.html): Provides a list of Amazon Linux 2 Reserved Users.
- [List of Amazon Linux 2 Reserved Groups](https://docs.aws.amazon.com/linux/al2/ug/al2-reserved-groups-list.html): Provides a list of Amazon Linux 2 Reserved Groups.


## [Security and Compliance](https://docs.aws.amazon.com/linux/al2/ug/security-and-compliance.html)

- [Enable FIPS Mode on AL2](https://docs.aws.amazon.com/linux/al2/ug/fips-mode.html): How to enable FIPS on AL2
