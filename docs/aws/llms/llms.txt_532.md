# Source: https://docs.aws.amazon.com/linux/al2023/ug/llms.txt

# Amazon Linux 2023 User Guide

> Describes key concepts of AL2023 and provides instructions for using key features of AL2023.

- [System Requirements](https://docs.aws.amazon.com/linux/al2023/ug/system-requirements.html)
- [The Amazon Linux Kernel](https://docs.aws.amazon.com/linux/al2023/ug/kernel-lifecycle.html)
- [Graphical Desktop](https://docs.aws.amazon.com/linux/al2023/ug/graphical-desktop-al2023.html)
- [Codecs available in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/codecs-amazon-linux-2023.html)

## [What is Amazon Linux 2023?](https://docs.aws.amazon.com/linux/al2023/ug/what-is-amazon-linux.html)

- [Release cadence](https://docs.aws.amazon.com/linux/al2023/ug/release-cadence.html): Learn about the Amazon Linux 2023 release cadence, support phases, and update mechanisms.
- [Naming and versioning](https://docs.aws.amazon.com/linux/al2023/ug/naming-and-versioning.html): There is a minor release every three months.
- [Performance and operational optimizations](https://docs.aws.amazon.com/linux/al2023/ug/performance-optimizations.html): Learn about features of kernel 6.1, toolchain and package selections, and deployment in the cloud.
- [Relationship to Fedora](https://docs.aws.amazon.com/linux/al2023/ug/relationship-to-fedora.html): Major releases of AL2023 are based in part on the current version of the upstream Fedora Linux distribution.
- [Customized cloud-init](https://docs.aws.amazon.com/linux/al2023/ug/cloud-init.html): AL2023 provides a customized version of cloud-init, the industry standard multi-distribution method for cross-platform cloud instance initialization.
- [Security updates and features](https://docs.aws.amazon.com/linux/al2023/ug/security-features.html): Top priority security is built into many features of AL2023.
- [Networking service](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html): Learn about the capabilities of the systemd-networkd project that's available in Amazon Linux distributions.
- [Core toolchain packages glibc, gcc, binutils](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html): Learn about the purposes of new core toolchain packages that build most software in your distribution.
- [Package management tool](https://docs.aws.amazon.com/linux/al2023/ug/package-management.html): Use the new default package management commands.
- [Default SSH server configuration](https://docs.aws.amazon.com/linux/al2023/ug/ssh-host-keys-disabled.html): Learn about your SSH host keys.


## [Deprecated Functionality](https://docs.aws.amazon.com/linux/al2023/ug/deprecated.html)

- [Deprecated functionality discontinued in AL1, removed in AL2](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al1.html): This section describes functionality that is available in AL1, and is no longer available in AL2.

### [Functionality deprecated in AL2 and removed in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2.html)

This section describes functionality that is available in AL2, and no longer available in AL2023.

- [ftp Package](https://docs.aws.amazon.com/linux/al2023/ug/ftp-package-exclusion.html): Learn about the deprecation of the legacy FTP package, and recommended alternatives for migrating to AL2023.
- [Deprecated in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html): This section describes functionality that exists in AL2023 and is likely to be removed in a future version of Amazon Linux.


## [Comparing AL2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html)

- [EPEL](https://docs.aws.amazon.com/linux/al2023/ug/epel.html): There is no EPEL for AL2023.
- [Python 2.7 has been replaced with Python 3](https://docs.aws.amazon.com/linux/al2023/ug/python2.7-no-more.html): AL2 provides support and security patches for Python 2.7 until June 2025, as part of our long-term support (LTS) commitment for AL2 core packages.

### [Security updates](https://docs.aws.amazon.com/linux/al2023/ug/security-updates.html)

Amazon Linux 2023 improves upon the hardening present in AL2.

- [SELinux](https://docs.aws.amazon.com/linux/al2023/ug/selinux.html): By default, Security Enhanced Linux (SELinux) for AL2023 is enabled and set to permissive mode.
- [OpenSSL 3](https://docs.aws.amazon.com/linux/al2023/ug/openssl3.html): AL2023 features the Open Secure Sockets Layer version 3 (OpenSSL 3) cryptography toolkit.
- [IMDSv2](https://docs.aws.amazon.com/linux/al2023/ug/imdsv2.html): By default, any instances launched with the AL2023 AMI require IMDSv2-only and your default hop limit will be set to 2 to allow for containerized workload support.
- [Removal of log4j hotpatch (log4j-cve-2021-44228-hotpatch)](https://docs.aws.amazon.com/linux/al2023/ug/log4j-hotpatch.html)
- [Deterministic upgrades for stability](https://docs.aws.amazon.com/linux/al2023/ug/compare-deterministic-upgrades.html): With the deterministic upgrades through versioned repositories feature, every AL2023 AMI by default is locked to a specific repository version.
- [gp3 as default Amazon EBS volume type](https://docs.aws.amazon.com/linux/al2023/ug/continuing-al2-filesystem.html): The AL2023 AMI and AL2 both use the XFS file system on the root file system.
- [Unified Control Group hierarchy (cgroup v2)](https://docs.aws.amazon.com/linux/al2023/ug/cgroupv2.html): A Control Group (cgroup) is a Linux kernel feature to hierarchically organize processes and distribute system resources between them.
- [systemd timers replace cron](https://docs.aws.amazon.com/linux/al2023/ug/cron.html): The cronie package was installed by default on the AL2 AMI, providing support for the traditional crontab way of scheduling periodic tasks.
- [Improved toolchain: gcc, binutils, and glibc](https://docs.aws.amazon.com/linux/al2023/ug/glibc-gcc-and-binutils.html): AL2023 includes many of the same core packages as AL2.
- [systemd journal replaces rsyslog](https://docs.aws.amazon.com/linux/al2023/ug/journald.html): In AL2023 the logging system package has changed from AL2.

### [Minimized package dependencies](https://docs.aws.amazon.com/linux/al2023/ug/minimized-pkg-dependencies.html)

Amazon Linux 2023 minimizes the dependency graph of many packages to provide a smaller footprint for applications.

- [Package changes for curl and libcurl](https://docs.aws.amazon.com/linux/al2023/ug/curl-minimal.html): AL2023 separates out the common protocols and functionality of the curl and libcurl packages into curl-minimal and libcurl-minimal.
- [GNU Privacy Guard (GNUPG)](https://docs.aws.amazon.com/linux/al2023/ug/gnupg-minimal.html): AL2023 separates out minimal and complete functionality for the gnupg2 package into gnupg2-minimal and gnupg2-full packages.
- [Amazon Corretto as the default JVM](https://docs.aws.amazon.com/linux/al2023/ug/compare-al2-java.html): AL2023 ships with Amazon Corretto as the default (and only) Java Development Kit (JDK).
- [AWS CLI v2](https://docs.aws.amazon.com/linux/al2023/ug/awscli2.html): AL2023 ships with AWS CLI version 2, whereas AL2 ships with version 1 of the AWS CLI.
- [UEFI Preferred and Secure Boot](https://docs.aws.amazon.com/linux/al2023/ug/uefi-preferred.html): By default, any instances launched with the AL2023 AMI on instance types that support UEFI firmware will launch in UEFI mode.
- [SSH server default configuration changes](https://docs.aws.amazon.com/linux/al2023/ug/ssh-host-key.html): Find out host key changes and about default disabling of ssh-rsa signatures.
- [Kernel changes in AL2023 from AL2](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2-kernel.html): Learn about key Linux kernel differences between AL2 and Amazon Linux 2023.
- [/tmp changes](https://docs.aws.amazon.com/linux/al2023/ug/compare-al2-al2023-tmp.html): Use /var/tmp for temporary on-disk storage, /tmp is now tmpfs and is for smaller items.
- [AMI and Container Image changes](https://docs.aws.amazon.com/linux/al2023/ug/w2aac11c69.html): There have been some changes to the packages included in AMIs and containers.
- [Amazon Linux 2 and AL2023 AMI comparison](https://docs.aws.amazon.com/linux/al2023/ug/amzn2-al2023-ami.html): A comparison of packages on the Amazon Linux 2 (AL2) and Amazon Linux 2023 (AL2023) AMIs.
- [Amazon Linux 2 and AL2023 Minimal AMI comparison](https://docs.aws.amazon.com/linux/al2023/ug/amzn2-al2023-minimal-ami.html): A comparison of packages on the Amazon Linux 2 (AL2) and Amazon Linux 2023 (AL2023) Minimal AMIs.
- [Amazon Linux 2 and AL2023 Container comparison](https://docs.aws.amazon.com/linux/al2023/ug/amzn2-al2023-container.html): A comparison of packages on the Amazon Linux 2 (AL2) and Amazon Linux 2023 (AL2023) base container images.


## [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html)

- [Kernel changes in AL2023 from AL1](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1-kernel.html): Learn about key Linux kernel differences between AL1 and AL2023.
- [AL1 and AL2023 AMI comparison](https://docs.aws.amazon.com/linux/al2023/ug/amzn1-al2023-ami.html): A comparison of packages on the Amazon Linux 1 (AL1, formerly Amazon Linux AMI) and Amazon Linux 2023 (AL2023) AMIs.
- [AL1 and AL2023 Minimal AMI comparison](https://docs.aws.amazon.com/linux/al2023/ug/amzn1-al2023-minimal-ami.html): A comparison of packages on the Amazon Linux 1 (AL1, formerly Amazon Linux AMI) and Amazon Linux 2023 (AL2023) Minimal AMIs.
- [AL1 and AL2023 Container comparison](https://docs.aws.amazon.com/linux/al2023/ug/amzn1-al2023-container.html): A comparison of packages on the Amazon Linux 1 (AL1, formerly Amazon Linux AMI) and Amazon Linux 2023 (AL2023) base container images.


## [Supplementary Packages for Amazon Linux](https://docs.aws.amazon.com/linux/al2023/ug/spal.html)

- [Configure SPAL on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/configure-spal-repository.html): This section provides instructions for configuring and using the SPAL repository on your AL2023 instance.


## [Running applications](https://docs.aws.amazon.com/linux/al2023/ug/running-applications.html)

- [Resource control with systemd](https://docs.aws.amazon.com/linux/al2023/ug/resource-limiting-systemd.html): Learn how to use systemd to control what resources processes can use.
- [Using cgroups utilities](https://docs.aws.amazon.com/linux/al2023/ug/resource-limiting-raw-cgroups.html): Using utilities in the libcgroup-tools package to limit resource usage of processes.


## [Using AL2023 on AWS](https://docs.aws.amazon.com/linux/al2023/ug/aws.html)

### [AL2023 on Amazon EC2](https://docs.aws.amazon.com/linux/al2023/ug/ec2.html)

Start using AL2023 by setting up a new instance in the AWS CLI using the CloudFormation AMI ID parameter.

- [Connecting to AL2023 instances](https://docs.aws.amazon.com/linux/al2023/ug/connecting-to-instances.html): Use SSH, AWS Systems Manager, or EC2 Instance Connect to connect to an AL2023 instance.

### [Comparing AL2023 standard (default) and minimal AMIs](https://docs.aws.amazon.com/linux/al2023/ug/AMI-minimal-and-standard-differences.html)

Use a standard AMI (default) to get started quickly and have all the major AMI features.

- [AL2023 image package list comparison](https://docs.aws.amazon.com/linux/al2023/ug/image-comparison.html): List of packages in the Amazon Linux 2023 (AL2023) AMI, Minimal AMI, and Container images.

### [AL2023 in containers](https://docs.aws.amazon.com/linux/al2023/ug/container.html)

Learn about the options for using AL2023 in containers and the options for base images.

- [AL2023 Base Container Image](https://docs.aws.amazon.com/linux/al2023/ug/base-container.html): Learn about using the AL2023 base container image.
- [AL2023 Minimal container image](https://docs.aws.amazon.com/linux/al2023/ug/minimal-container.html): Learn how to use the minimal container image for your application based on AL2023
- [Building bare-bones AL2023 container images](https://docs.aws.amazon.com/linux/al2023/ug/barebones-containers.html): Learn how to build bare-bones containers for your application based on AL2023
- [AL2023 container image package list comparison](https://docs.aws.amazon.com/linux/al2023/ug/al2023-container-image-types.html): List of packages in each Amazon Linux 2023 (AL2023) container image type: base and minimal
- [AL2023 Minimal AMI compared to container images](https://docs.aws.amazon.com/linux/al2023/ug/al2023-container-ami.html): List of packages in the Amazon Linux 2023 (AL2023) Minimal AMI compared to the base and minimial container images
- [AL2023 on Elastic Beanstalk](https://docs.aws.amazon.com/linux/al2023/ug/beanstalk.html): Start using AL2023 with AWS Elastic Beanstalk
- [AL2023 CloudShell](https://docs.aws.amazon.com/linux/al2023/ug/cloudshell.html): Learn about Amazon Linux 2023 based AWS CloudShell.
- [AL2023 for Amazon ECS container hosts](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html): Learn how to use the AL2023 Amazon ECS optimized AMIs to host containerized workloads.
- [Amazon EFS on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/efs.html): Learn how to use the Amazon Elastic File System on Amazon Linux 2023 instances.
- [Amazon EMR on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/emr.html): Learn how to use Amazon EMR built on Amazon Linux 2023.
- [AL2023 on AWS Lambda](https://docs.aws.amazon.com/linux/al2023/ug/lambda.html): Learn how to use Amazon Linux 2023 in AWS Lambda


## [Tutorials](https://docs.aws.amazon.com/linux/al2023/ug/tutorials-al2023.html)

- [Install LAMP on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/ec2-lamp-amazon-linux-2023.html): Install the Apache web server with PHP and MariaDB support on your EC2 instance.
- [Configure SSL/TLS on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/SSL-on-amazon-linux-2023.html): Install and configure SSL/TLS on a single EC2 instance running AL2023 and Apache web server.
- [Host a WordPress blog on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/hosting-wordpress-aml-2023.html): Tutorial to install, configure, and secure a WordPress blog on your EC2 instance.
- [Redis 6 to Valkey Transition on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/redis6-to-valkey-al2023.html): This documentation guides you through migrating from Redis 6 to Valkey on AL2023, including installation, configuration, and data migration steps
- [Install GNOME on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/installing-gnome-al2023.html): Install the GNOME desktop environment on your EC2 instance.
- [Configure VNC on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/vnc-configuration-al2023.html): Install TigerVNC server on your EC2 instance.
- [Using Multi-Gen LRU (MGLRU) on AL2023 kernels](https://docs.aws.amazon.com/linux/al2023/ug/kernel-mglru-al2023.html): Using Multi-Gen LRU (MGLRU) on AL2023 kernels


## [AL2023 outside Amazon EC2](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)

- [Download AL2023 VM Images](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2-download.html): Amazon Linux 2023 disk images for use with KVM, VMware, and Hyper-V can be downloaded from cdn.amazonlinux.com.

### [Supported Configurations](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2-supported-configurations.html)

This section covers the requirements for running Amazon Linux 2023 in non-Amazon EC2 virtualized environments such as on KVM, VMware, or and Hyper-V.

- [KVM Requirements](https://docs.aws.amazon.com/linux/al2023/ug/kvm-supported-configurations.html): This section describes the requirements for running AL2023 on KVM.
- [VMware Requirements](https://docs.aws.amazon.com/linux/al2023/ug/vmware-supported-configurations.html): This section describes the requirements for running AL2023 on VMware.
- [Hyper-V Requirements](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html): This section covers the requirements for running Amazon Linux 2023 on Hyper-V.

### [AL2023 VM configuration](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2-configuration.html)

This section covers how to set up and configure a Amazon Linux 2023 virtual machine when not run directly on Amazon EC2, such as when on KVM, VMware, or Hyper-V.

- [NoCloud seed.iso based configuration](https://docs.aws.amazon.com/linux/al2023/ug/seed-iso.html): This section covers how to create and use a seed.iso image to configure Amazon Linux 2023 running on KVM or VMware.
- [VMware guestinfo based configuration](https://docs.aws.amazon.com/linux/al2023/ug/vmware-guestinfo.html): VMware environments do not have the Amazon EC2 Instance Meta Data Service (IMDS), so an alternate method of configuring AL2023 is required.
- [AL2023 package list comparison for the standard AMI and KVM image](https://docs.aws.amazon.com/linux/al2023/ug/al2023-ami-kvm-image.html): List of packages for Amazon Linux 2023 (AL2023) standard AMI compared to the KVM image
- [AL2023 package list comparison for the standard AMI and VMware OVA image](https://docs.aws.amazon.com/linux/al2023/ug/al2023-ami-vmware-image.html): List of packages for Amazon Linux 2023 (AL2023) standard AMI compared to the VMware OVA image
- [AL2023 package list comparison for the standard AMI and Hyper-V image](https://docs.aws.amazon.com/linux/al2023/ug/al2023-ami-hyperv-image.html): List of packages for Amazon Linux 2023 (AL2023) standard AMI compared to the Hyper-V image


## [Identifying Amazon Linux versions](https://docs.aws.amazon.com/linux/al2023/ug/identifying.html)

- [/etc/os-release](https://docs.aws.amazon.com/linux/al2023/ug/ident-os-release.html): Amazon Linux supports the os-release standard for determining the OS and OS version.
- [Amazon Linux Specific](https://docs.aws.amazon.com/linux/al2023/ug/ident-amazon-linux-specific.html): There are some files that are specific to Amazon Linux that can be used for identifying Amazon Linux and what version it is.
- [Example code](https://docs.aws.amazon.com/linux/al2023/ug/ident-example-code.html): Code examples for programmatically detecting operating systems and versions.


## [Filesystem Layout](https://docs.aws.amazon.com/linux/al2023/ug/filesystem.html)

- [/](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-root.html): The / (root) directory on AL2023.
- [/boot](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-boot.html): The /boot directory on AL2023.
- [/etc](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-etc.html): The /etc directory on AL2023.
- [/home](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-home.html): The /home directory on AL2023.
- [/root](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-root.html): The /root directory on AL2023.
- [/srv](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-srv.html): The /srv directory on AL2023.
- [/tmp](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-tmp.html): The /tmp directory on AL2023.
- [/run](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-run.html): The /run, /run/log, /run/user/ directories on AL2023.
- [/usr](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-usr.html): The vendor-supplied Operating System resources in /usr on AL2023.
- [/var](https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-var.html): Persistent variable system data is stored in /var on AL2023.


## [Updating AL2023](https://docs.aws.amazon.com/linux/al2023/ug/updating.html)

- [Best practices for safely deploying updates](https://docs.aws.amazon.com/linux/al2023/ug/updating-best-practice.html): Covers best practices for deploying AL2023 updates in a safe manner.
- [Receive notifications on new updates](https://docs.aws.amazon.com/linux/al2023/ug/receive-update-notification.html): Use Amazon SNS to receive notifications when AL2023 updates are released.

### [Deterministic upgrades through versioned repositories](https://docs.aws.amazon.com/linux/al2023/ug/deterministic-upgrades.html)

Learn how to use deterministic upgrades through versioned repositories to ensure consistency of package versions and updates across your environment.

- [Instance replacement](https://docs.aws.amazon.com/linux/al2023/ug/security-instance-replacement.html): Learn about using instance replacement to apply Amazon Linux updates.
- [In-place Deterministic upgrades](https://docs.aws.amazon.com/linux/al2023/ug/deterministic-upgrades-usage.html): Deterministic upgrades through versioned repository usage in AL2023 ensures the OS release doesn't change without approval.
- [Managing updates](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html): Manage packages and OS updates in AL2023.
- [Kernel Live Patching](https://docs.aws.amazon.com/linux/al2023/ug/live-patching.html): Keep your AL2023 instance secure and the system up to date using Kernel Live Patch.
- [Kernel Updates](https://docs.aws.amazon.com/linux/al2023/ug/kernel-update.html): Update the Linux kernel to latest versions to benefit from new features and performance improvements.


## [Programming languages and runtimes](https://docs.aws.amazon.com/linux/al2023/ug/language-runtimes.html)

- [C/C++ and Fortran](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html): AL2023 includes both the GNU Compiler Collection (GCC) and the Clang frontend for LLVM (Low Level Virtual Machine).
- [Go](https://docs.aws.amazon.com/linux/al2023/ug/go.html): You might want to build your own code written in Go on Amazon Linux, and might want to use a toolchain provided with AL2023.
- [Java](https://docs.aws.amazon.com/linux/al2023/ug/java.html): AL2023 provides several versions of Amazon Corretto to support Java based workloads.
- [Node.js](https://docs.aws.amazon.com/linux/al2023/ug/nodejs.html): Node.js in AL2023 is represented by versions 20, 22 and 24.
- [Perl](https://docs.aws.amazon.com/linux/al2023/ug/perl.html): AL2023 provides version 5.32 of the Perl programming language.
- [PHP](https://docs.aws.amazon.com/linux/al2023/ug/php.html): AL2023 currently provides the PHP programming language, versions 8.1, 8.2, 8.3, 8.4, and 8.5.
- [Python](https://docs.aws.amazon.com/linux/al2023/ug/python.html): AL2023 removed Python 2.7 and any components requiring Python are now written to work with Python 3.
- [Rust](https://docs.aws.amazon.com/linux/al2023/ug/rust.html): You might want to build code written in Rust on Amazon Linux, and might want to use a toolchain provided with AL2023.
- [TypeScript](https://docs.aws.amazon.com/linux/al2023/ug/typescript.html)


## [AL2023 Reserved Users and Groups](https://docs.aws.amazon.com/linux/al2023/ug/reserved-users-groups.html)

- [List of AL2023 Reserved Users](https://docs.aws.amazon.com/linux/al2023/ug/al2023-reserved-users-list.html): Provides a list of AL2023 Reserved Users.
- [List of AL2023 Reserved Groups](https://docs.aws.amazon.com/linux/al2023/ug/al2023-reserved-groups-list.html): Provides a list of AL2023 Reserved Groups.


## [Security and Compliance](https://docs.aws.amazon.com/linux/al2023/ug/security.html)

- [Security advisories](https://docs.aws.amazon.com/linux/al2023/ug/alas.html): Learn about where to read about security advisories for AL2023.
- [Listing applicable Advisories](https://docs.aws.amazon.com/linux/al2023/ug/listing-applicable-advisories.html): Learn how to find what advisories apply.
- [In-place updates](https://docs.aws.amazon.com/linux/al2023/ug/security-inplace-update.html): Apply security updates to an existing instance.

### [Setting SELinux modes for AL2023](https://docs.aws.amazon.com/linux/al2023/ug/selinux-modes.html)

SELinux, by default enabled and permissive, provides a strong, flexible, MAC architecture.

- [Default SELinux status and modes for AL2023](https://docs.aws.amazon.com/linux/al2023/ug/default-SELinux-modes-states.html): By default, SELinux in permissive mode logs but doesn't enforce permission denials.
- [Change to enforcing mode](https://docs.aws.amazon.com/linux/al2023/ug/enforcing-mode.html): When you run SELinux in enforcing mode, the SELinux utility enforces the configured policy.
- [Option to disable SELinux](https://docs.aws.amazon.com/linux/al2023/ug/disable-option-selinux.html): Disabling SELinux eliminates logging of AVC messages and all other benefits of running SELinux.
- [Enable FIPS Mode on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/fips-mode.html): How to enable FIPS on AL2023
- [Enable FIPS Mode in an AL2023 Container](https://docs.aws.amazon.com/linux/al2023/ug/fips-mode-container.html): How to enable FIPS in an AL2023 container
- [Swap OpenSSL FIPS providers on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/fips-openssl-swap-provider.html): How to swap OpenSSL FIPS providers on AL2023
- [Kernel Hardening](https://docs.aws.amazon.com/linux/al2023/ug/kernel-hardening.html): Learn about the hardening features enabled in the AL2023 kernel.
- [UEFI Secure Boot on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html): Use UEFI to secure your instances .
