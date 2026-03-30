# Source: https://docs.aws.amazon.com/transfer/latest/userguide/llms.txt

# AWS Transfer Family User Guide

> AWS Transfer Family is a secure transfer service that stores your data in Amazon Simple Storage Service or Amazon Elastic File System and simplifies the migration of Secure File Transfer Protocol (SFTP), File Transfer Protocol Secure (FTPS), File Transfer Protocol (FTP), and Applicability Statement 2 (AS2) workflows to AWS.

- [What is AWS Transfer Family?](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)
- [CloudTrail logging](https://docs.aws.amazon.com/transfer/latest/userguide/cloudtrail-logging.html)
- [Transfer Family Terraform modules](https://docs.aws.amazon.com/transfer/latest/userguide/terraform.html)
- [API refererence](https://docs.aws.amazon.com/transfer/latest/userguide/api-welcome.html)
- [Document history](https://docs.aws.amazon.com/transfer/latest/userguide/doc-history.html)

## [Prerequisites](https://docs.aws.amazon.com/transfer/latest/userguide/setting-up.html)

- [Sign up for AWS](https://docs.aws.amazon.com/transfer/latest/userguide/requirements-aws-signup.html): Sign up for an AWS account.
- [Configure storage](https://docs.aws.amazon.com/transfer/latest/userguide/configure-storage.html): Describes the storage options for use with AWS Transfer Family, and details for each option.
- [Create an IAM role and policy](https://docs.aws.amazon.com/transfer/latest/userguide/requirements-roles.html): Create IAM roles and policies for AWS Transfer Family.


## [Transfer Family tutorials](https://docs.aws.amazon.com/transfer/latest/userguide/tutorials-transfer.html)

- [Get started with server endpoints](https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html): Walk through creating an SFTP server, creating a service-managed user, and performing a file transfer with AWS Transfer Family.
- [Create a decryption Workflow](https://docs.aws.amazon.com/transfer/latest/userguide/workflow-decrypt-tutorial.html): Learn how to create a managed workflow in AWS Transfer Family that contains a decrypt step.
- [Create and use SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/sftp-connectors-tutorial.html): Learn how to create an SFTP connector to send and retrieve files using both service managed and VPC egress types
- [Use a custom identity provider](https://docs.aws.amazon.com/transfer/latest/userguide/gateway-api-tutorial.html): Walk through how to create a custom identity provider by setting up a CloudFormation stack, an API Gateway, and a Transfer Family server.
- [Set up an AS2 configuration](https://docs.aws.amazon.com/transfer/latest/userguide/as2-example-tutorial.html): Walks through how to set up an Applicability Statement 2 (AS2) configuration with AWS Transfer Family for testing purposes.
- [Set up a basic web app](https://docs.aws.amazon.com/transfer/latest/userguide/web-app-tutorial.html): Learn how to set up a basic Transfer Family web app with standard S3 bucket access.
- [Set up web app with selective multi-bucket access](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-s3-tutorial.html): Learn how to configure AWS Transfer Family web app with granular Amazon S3 bucket permissions for a single user, allowing them to download from one bucket and upload to another while maintaining security.


## [Transfer Family for SFTP, FTPS, FTP](https://docs.aws.amazon.com/transfer/latest/userguide/sftp-for-transfer-family.html)

### [Configure a Transfer Family server endpoint](https://docs.aws.amazon.com/transfer/latest/userguide/tf-server-endpoint.html)

Describe how to create a Transfer Family server, including the available protocols and both public and private endpoints.

- [Create an SFTP-enabled server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-sftp.html): Use the AWS Transfer Family service to create an SFTP-enabled server.
- [Create an FTPS-enabled server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-ftps.html): Use the AWS Transfer Family service to create an FTPS-enabled server.
- [Create an FTP-enabled server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-ftp.html): Use the AWS Transfer Family service to create an FTP-enabled server.

### [Create a server in a VPC](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html)

Create a server in a virtual private cloud (VPC) to use for transferring data over your client to and from an Amazon S3 bucket without going over the public internet.

- [Updating the server endpoint type to VPC](https://docs.aws.amazon.com/transfer/latest/userguide/update-endpoint-type-vpc.html): Transfer is discontinuing use of the VPC_ENDPOINT Endpoint type.
- [Working with custom hostnames](https://docs.aws.amazon.com/transfer/latest/userguide/requirements-dns.html): Use a custom domain that you have registered for your server hostname when working with AWS Transfer Family.
- [Transfer files over server endpoint](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-file.html): Set up and use clients with AWS Transfer Family to perform file operations.

### [Manage users](https://docs.aws.amazon.com/transfer/latest/userguide/create-user.html)

Assign users to one or more file transfer protocol enabled servers.

- [Service-managed users](https://docs.aws.amazon.com/transfer/latest/userguide/service-managed-users.html): Set up and configure service-managed users for AWS Transfer Family

### [Custom identity provider](https://docs.aws.amazon.com/transfer/latest/userguide/custom-idp-intro.html)

Describe the available options for using a custom identity provider with AWS Transfer Family.

- [Custom IdP solution](https://docs.aws.amazon.com/transfer/latest/userguide/custom-idp-toolkit.html): Standard patterns for implementing a custom provider that accounts for details including logging and where to store the additional session metadata needed for AWS Transfer Family, such as the HomeDirectoryDetails.
- [Lambda as an identity provider](https://docs.aws.amazon.com/transfer/latest/userguide/custom-lambda-idp.html): Use a Lambda function as an identity provider for Transfer Family
- [Using Amazon API Gateway to integrate your identity provider](https://docs.aws.amazon.com/transfer/latest/userguide/authentication-api-gateway.html): This topic describes how to use an AWS Lambda function to back an API Gateway method.
- [Multiple auth for custom IdP](https://docs.aws.amazon.com/transfer/latest/userguide/custom-idp-mfa.html): Details for how multiple authentication methods work with a Transfer Family custom identity provider
- [IPv6 support](https://docs.aws.amazon.com/transfer/latest/userguide/custom-idp-ipv6.html): Information about IPv6 support when implementing custom identity providers for AWS Transfer Family.
- [Directory service for MS AD](https://docs.aws.amazon.com/transfer/latest/userguide/directory-services-users.html): Use AWS Directory Service for Microsoft Active Directory to authenticate Transfer users that use Microsoft Active Directory.
- [Directory service for Entra ID](https://docs.aws.amazon.com/transfer/latest/userguide/azure-sftp.html): For customers that need SFTP Transfer only, and do not want to manage a domain, there is Simple Active Directory.

### [Use logical directories](https://docs.aws.amazon.com/transfer/latest/userguide/logical-dir-mappings.html)

Use logical directories to create a virtual directory structure to manage navigation and to avoid disclosing absolute directory paths or bucket names to your users.

- [Implementing logical directories](https://docs.aws.amazon.com/transfer/latest/userguide/implement-log-dirs.html): Learn how to implement logical directories and chroot functionality for AWS Transfer Family servers.
- [Configure logical directories examples](https://docs.aws.amazon.com/transfer/latest/userguide/logical-dir-example.html): Practical examples of configuring logical directories for AWS Transfer Family users using AWS CLI commands.
- [Access FSx for NetApp ONTAP file systems](https://docs.aws.amazon.com/transfer/latest/userguide/fsx-s3-access-points.html): You can use Amazon FSx file systems as storage for your Transfer Family servers through S3 access points.


## [Transfer Family web apps](https://docs.aws.amazon.com/transfer/latest/userguide/web-app.html)

- [Configure your identity provider](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-identity-center.html): Configure Identity Center, or an alternative identity provider, for use with the Transfer Family web app.
- [Configure IAM roles](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-roles.html): Configure IAM roles for use with the Transfer Family web app.
- [Configure a Transfer Family web app](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-configure.html): Configure a Transfer Family web app and assign users.
- [Create a Transfer Family web app in a VPC](https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html): Host your web app endpoint inside a virtual private cloud for private data transfers.
- [Assign or add users or groups to a Transfer Family web app](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-add-users.html): After you create a Transfer Family web app, you can assign users and groups who can then access the web app.
- [Set up Cross-origin resource sharing (CORS) for your bucket](https://docs.aws.amazon.com/transfer/latest/userguide/access-grant-cors.html): Set up cross origin resource sharing which defines a way for a client web application that is loaded in one domain to interact with resources in a different domain.
- [Configure Amazon S3 Access Grants](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-access-grant.html): Configure Amazon S3 Access Grants for use with the Transfer Family web app.
- [Use a custom URL](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-customize.html): Customize your access endpoint URL for a Transfer Family web app.
- [Logging for Transfer Family web apps](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-cloudtrail.html): Transfer Family web apps integration with CloudTrail for monitoring user authentication and data access activities.
- [Troubleshooting your web apps](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-troubleshooting.html): Troubleshooting common errors for Transfer Family web apps.
- [End user instructions](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-end-users.html): Usage instructions for Transfer Family web app end users


## [SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/creating-connectors.html)

### [Creating SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/configure-sftp-connector.html)

Learn how create to SFTP connectors in AWS Transfer Family for transferring files between your AWS storage and a partner's SFTP server.

- [Store credentials in Secrets Manager](https://docs.aws.amazon.com/transfer/latest/userguide/sftp-connector-secret-procedure.html): Procedure that describes how to store a secret in Secrets Manager for use with Transfer Family connectors.
- [Create an SFTP connector with service-managed egress](https://docs.aws.amazon.com/transfer/latest/userguide/create-sftp-connector-procedure.html): Procedure for creating SFTP connectors that use service-managed egress
- [Create an SFTP connector with VPC-based egress](https://docs.aws.amazon.com/transfer/latest/userguide/create-vpc-sftp-connector-procedure.html): Learn how to create SFTP connectors with VPC connectivity using Cross-VPC Resource Access to connect with remote SFTP servers through your Virtual Private Cloud environments.
- [Test an SFTP connector](https://docs.aws.amazon.com/transfer/latest/userguide/test-sftp-connector.html): Details for testing an SFTP connector after you create it.
- [VPC connectivity](https://docs.aws.amazon.com/transfer/latest/userguide/sftp-connectors-vpc-overview.html): Overview of VPC connectivity for SFTP connectors, including when to use it, requirements, and implementation guidance for connecting to remote SFTP servers through your Virtual Private Cloud environments.

### [Using SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-sftp-connectors.html)

Learn how to use SFTP connectors with AWS Transfer Family to perform up to 30 simultaneous file transfers between Transfer Family and remote servers both in the cloud and on-premises.

- [Transfer files](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-files-and-track.html): Describe how to send and retrieve files using an SFTP connector, and how to track the progress of these transfers.
- [List contents of remote directories](https://docs.aws.amazon.com/transfer/latest/userguide/sftp-connector-list-dir.html): This topic describes how to retrieve the contents of a folder on a remote SFTP server, so that you can then determine which files to retrieve using a StartFileTransfer command.
- [Move and delete files on the remote server](https://docs.aws.amazon.com/transfer/latest/userguide/move-delete-remote-files.html)
- [Monitoring SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/track-connector-progress.html): Details for how to monitor the progress of your file transfers that use Transfer Family SFTP connectors, including API queries, EventBridge events, CloudWatch logs, and VPC connectivity monitoring.
- [Managing SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/manage-sftp-connectors.html): Learn how to manage SFTP connectors with AWS Transfer Family, including updating connector configurations and viewing connector details.
- [Quotas for SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/scale-and-limits-sftp-connector.html): Describe miscellaneous info for SFTP connectors: SFTP connector quotas, and how to scale them.
- [Reference architectures](https://docs.aws.amazon.com/transfer/latest/userguide/reference-architectures.html): List of reference materials that are available for SFTP connectors for AWS Transfer Family


## [Transfer Family for AS2](https://docs.aws.amazon.com/transfer/latest/userguide/as2-for-transfer-family.html)

- [Configure AS2](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html): Use AWS Transfer Family to create a server for business-to-business (B2B) transfers that's enabled for the AS2 file-transfer protocol.
- [Manage AS2 certificates](https://docs.aws.amazon.com/transfer/latest/userguide/managing-as2-partners.html): Discuss how to manage AS2 certificates, profiles, and agreements for Transfer Family.
- [Create AS2 profiles](https://docs.aws.amazon.com/transfer/latest/userguide/configure-as2-profile.html): Create profiles for working with the AS2 protocol in AWS Transfer Family.
- [Create an AS2 server](https://docs.aws.amazon.com/transfer/latest/userguide/create-as2-transfer-server.html): Use AWS Transfer Family to create a server for business-to-business (B2B) transfers that's enabled for the AS2 file-transfer protocol.
- [Configure AS2 connectors](https://docs.aws.amazon.com/transfer/latest/userguide/configure-as2-connector.html): Learn how create to AS2 connectors in AWS Transfer Family for transferring messages from a Transfer Family server to your trading partners.
- [Transfer AS2 messages](https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html): Details for sending and receiving AS2 messages between an AS2-enabled Transfer Family server and a trading partner.
- [Custom HTTP Headers for AS2](https://docs.aws.amazon.com/transfer/latest/userguide/as2-custom-http-headers.html): A CloudFormation template for implementing customized HTTP headers for AS2 messages sent through AWS Transfer Family.
- [Monitor AS2](https://docs.aws.amazon.com/transfer/latest/userguide/as2-monitoring.html): Monitor your AS2 usage using Amazon CloudWatch and AWS CloudTrail.
- [Certificate expiration monitoring](https://docs.aws.amazon.com/transfer/latest/userguide/certificate-expiry-monitoring.html): Monitor AS2 certificate expiration dates using Amazon CloudWatch metrics and set up automated notifications.


## [Managing file-processing workflows](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-workflows.html)

- [Create a workflow](https://docs.aws.amazon.com/transfer/latest/userguide/create-workflow.html): Learn how to create a file-processing workflow in AWS Transfer Family.
- [Use predefined steps](https://docs.aws.amazon.com/transfer/latest/userguide/nominal-steps-workflow.html): Learn about how to use the tag, copy, decrypt, and delete steps for workflows in AWS Transfer Family managed workflows.
- [Use custom file-processing steps](https://docs.aws.amazon.com/transfer/latest/userguide/custom-step-details.html): Learn how to create custom workflow steps that use AWS Lambda code in AWS Transfer Family managed workflows.
- [IAM policies for workflows](https://docs.aws.amazon.com/transfer/latest/userguide/workflow-execution-role.html): Learn how to use AWS Identity and Access Management (IAM) roles with AWS Transfer Family workflows.
- [Monitor workflow execution](https://docs.aws.amazon.com/transfer/latest/userguide/cloudwatch-workflow.html): Learn about the logging and metrics that are available for AWS Transfer Family workflows.
- [Create workflow from template](https://docs.aws.amazon.com/transfer/latest/userguide/workflow-template.html): Learn how to create an AWS Transfer Family workflow and server from an CloudFormation template.


## [Managing servers](https://docs.aws.amazon.com/transfer/latest/userguide/configuring-servers.html)

- [View SFTP server details](https://docs.aws.amazon.com/transfer/latest/userguide/configuring-servers-view-info.html): View information about your AWS Transfer Family SFTP, FTPS, and FTP servers.
- [View AS2 server details](https://docs.aws.amazon.com/transfer/latest/userguide/view-as2-server-details.html): View information about your AWS Transfer Family AS2 servers.
- [IPv6 support](https://docs.aws.amazon.com/transfer/latest/userguide/ipv6-support.html): Information about IPv6 support for AWS Transfer Family servers and endpoints.
- [Edit server details](https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html): Edit the properties of a server in the AWS Transfer Family service.
- [Edit identity provider configuration](https://docs.aws.amazon.com/transfer/latest/userguide/configuring-servers-edit-custom-idp.html): Change your server's identity provider type and configure the required settings for each identity provider.

### [Manage server host keys](https://docs.aws.amazon.com/transfer/latest/userguide/configuring-servers-change-host-key.html)

Change the host key for your SFTP-enabled server, or rotate or add additional keys.

- [Add an additional server host key](https://docs.aws.amazon.com/transfer/latest/userguide/server-host-key-add.html): How to add an additional server host key to your AWS Transfer Family SFTP-enabled server.
- [Delete a server host key](https://docs.aws.amazon.com/transfer/latest/userguide/server-host-key-delete.html): How to delete a server host key for your AWS Transfer Family SFTP-enabled server.
- [Rotate the server host keys](https://docs.aws.amazon.com/transfer/latest/userguide/server-host-key-rotate.html): How to rotate server host keys for an AWS Transfer Family SFTP-enabled server.
- [Additional server host key information](https://docs.aws.amazon.com/transfer/latest/userguide/server-host-key-other.html): Information about server host keys for an AWS Transfer Family SFTP-enabled server.
- [Monitor usage within console](https://docs.aws.amazon.com/transfer/latest/userguide/monitor-usage-transfer-console.html): Monitor server, workflow, and AS2 usage from within the Transfer console.


## [Managing access controls](https://docs.aws.amazon.com/transfer/latest/userguide/users-policies.html)

- [Creating an S3 bucket access policy](https://docs.aws.amazon.com/transfer/latest/userguide/users-policies-all-access.html): Create a policy that allows read and write access to a specific Amazon S3 bucket, and assign an IAM role to your user that has this policy.
- [Creating a session policy](https://docs.aws.amazon.com/transfer/latest/userguide/users-policies-session.html): Use a session policy in AWS Transfer Family to enable your users to access only their home or other directory for Amazon S3.
- [Dynamic permission management](https://docs.aws.amazon.com/transfer/latest/userguide/dynamic-permission-management.html): Learn about different approaches for managing user permissions dynamically using session policies with AWS Transfer Family.


## [CloudWatch logging](https://docs.aws.amazon.com/transfer/latest/userguide/structured-logging.html)

- [Creating logging for servers](https://docs.aws.amazon.com/transfer/latest/userguide/log-server-manage.html): Learn about the structured logging flow when creating, updating and viewing servers.
- [Managing logging for workflows](https://docs.aws.amazon.com/transfer/latest/userguide/cloudwatch-workflows.html): Describes using CloudWatch for logging Transfer Family workflows.
- [Configuring a role for CloudWatch](https://docs.aws.amazon.com/transfer/latest/userguide/configure-cw-logging-role.html): Use Amazon CloudWatch logging for AWS Transfer Family.
- [Viewing Transfer Family log streams](https://docs.aws.amazon.com/transfer/latest/userguide/view-log-entries.html)
- [Examples to limit confused deputy problem](https://docs.aws.amazon.com/transfer/latest/userguide/cloudwatch-confused-deputy.html): Examples to limit the confused deputy problem
- [CloudWatch log structure for Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/cw-structure-logs.html): Example Amazon CloudWatch log entries for AWS Transfer Family events.
- [Example CloudWatch log entries](https://docs.aws.amazon.com/transfer/latest/userguide/cw-example-logs.html): Example Amazon CloudWatch log entries for AWS Transfer Family events.
- [Using CloudWatch metrics](https://docs.aws.amazon.com/transfer/latest/userguide/metrics.html): Using Transfer Family CloudWatch metrics.
- [CloudWatch queries](https://docs.aws.amazon.com/transfer/latest/userguide/cw-queries.html): Provide sample queries against Amazon CloudWatch Logs Insights, to run Athena queries and build a Quick dashboard.


## [Managing events using EventBridge](https://docs.aws.amazon.com/transfer/latest/userguide/eventbridge.html)

- [Events detail reference](https://docs.aws.amazon.com/transfer/latest/userguide/events-detail-reference.html): Descriptions for the fields containing metadata about the Transfer Family events.


## [Security](https://docs.aws.amazon.com/transfer/latest/userguide/security.html)

- [Security policies for servers](https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html): View the available AWS Transfer Family server security policies and a list of supported SSH ciphers, KEXs, MACs, content encryption ciphers, hash algorithms, and TLS ciphers.
- [Security policies for SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/security-policies-connectors.html): View the available AWS Transfer Family SFTP connector security policies and a list of supported SSH ciphers, KEXs, MACs, and TLS ciphers.
- [Post-Quantum security policies](https://docs.aws.amazon.com/transfer/latest/userguide/post-quantum-security-policies.html): Learn how to implement and test hybrid post-quantum key exchange algorithms with Transfer Family to protect your file transfers against future quantum computing threats while maintaining compatibility with classical cryptography.
- [Data protection](https://docs.aws.amazon.com/transfer/latest/userguide/encryption-at-rest.html): Learn how the AWS shared responsibility model applies to data protection and encryption in AWS Transfer Family.

### [Key management](https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html)

Generate and manage keys for AWS Transfer Family.

### [Generate SSH keys](https://docs.aws.amazon.com/transfer/latest/userguide/sshkeygen.html)

How to generate an SSH key for use with the AWS Transfer Family service.

- [Creating SSH keys on macOS, Linux, or Unix](https://docs.aws.amazon.com/transfer/latest/userguide/macOS-linux-unix-ssh.html): Create SSH keys on macOS, Linux, or Unix by using the ssh-keygen command.
- [Creating SSH keys on Windows](https://docs.aws.amazon.com/transfer/latest/userguide/windows-ssh.html): Create SSH keys on Windows using OpenSSH or third-party tools like PuTTYgen.
- [Converting SSH2 keys to SSH](https://docs.aws.amazon.com/transfer/latest/userguide/convert-ssh2-public-key.html): Describes the process for converting an SSH2 public key to SSH public key format for use with Transfer Family
- [Rotate SSH keys](https://docs.aws.amazon.com/transfer/latest/userguide/keyrotation.html): By rotating SSH keys, you replace SSH keys on a regular basis with new key pairs.
- [Generate PGP keys](https://docs.aws.amazon.com/transfer/latest/userguide/generate-pgp-keys.html): You can use Pretty Good Privacy (PGP) decryption with the files that Transfer Family processes with workflows.
- [Manage PGP keys](https://docs.aws.amazon.com/transfer/latest/userguide/manage-pgp-keys.html): To manage your PGP keys, use AWS Secrets Manager.
- [Supported PGP clients](https://docs.aws.amazon.com/transfer/latest/userguide/pgp-key-clients.html): A list of the PGP clients that are supported for use with encrypting and decrypting files in AWS Transfer Family.

### [Identity and access management](https://docs.aws.amazon.com/transfer/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS Transfer Family resources.

- [How AWS Transfer Family works with IAM](https://docs.aws.amazon.com/transfer/latest/userguide/security_iam_service-with-iam.html): How Transfer Family works with IAM
- [Identity-based policy examples](https://docs.aws.amazon.com/transfer/latest/userguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS Transfer Family resources.
- [Tag-based policy examples](https://docs.aws.amazon.com/transfer/latest/userguide/security_iam_tag-based-policy-examples.html): The following are examples of how to control access to AWS Transfer Family resources based on tags.
- [Troubleshooting identity and access](https://docs.aws.amazon.com/transfer/latest/userguide/security_iam_troubleshoot.html): Troubleshoot Transfer Family identity and access
- [IAM condition keys](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-condition-keys.html): Use IAM condition keys to restrict AWS Transfer Family resource configurations in IAM policies, including Service Control Policies (SCPs).
- [Compliance validation](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/transfer/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Transfer Family features for data resiliency.
- [VPC endpoints for APIs](https://docs.aws.amazon.com/transfer/latest/userguide/vpc-api-endpoints.html): Establish private connectivity between your VPC and AWS Transfer Family APIs using interface VPC endpoints powered by AWS PrivateLink.
- [Infrastructure security](https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html): Learn how AWS Transfer Family isolates service traffic and implements network security measures to protect your data.
- [Web application firewall](https://docs.aws.amazon.com/transfer/latest/userguide/web-application-firewall.html): Learn how to add a web application firewall to protect your Transfer Family endpoints from malicious traffic and enhance security for your file transfer workflows.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/transfer/latest/userguide/confused-deputy.html): Describes how to prevent the confused deputy issue in AWS Transfer Family and provides examples.
- [AWS managed policies](https://docs.aws.amazon.com/transfer/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Transfer Family and recent changes to those policies.


## [Troubleshooting Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/troubleshooting.html)

- [Authentication issues](https://docs.aws.amazon.com/transfer/latest/userguide/auth-issues.html): Solutions for common authentication problems with AWS Transfer Family servers, including SSH/SFTP failures, Active Directory issues, and API Gateway integration.
- [SFTP connector issues](https://docs.aws.amazon.com/transfer/latest/userguide/connector-troubleshooting.html): Solutions for common SFTP connector problems in AWS Transfer Family, including host key validation, key negotiation failures, throttling, and performance optimization.
- [SFTP connectivity issues](https://docs.aws.amazon.com/transfer/latest/userguide/sftp-connectivity-issues.html): Solutions for SFTP connection problems, file transfer failures, and client compatibility issues with AWS Transfer Family servers.
- [Custom identity provider issues](https://docs.aws.amazon.com/transfer/latest/userguide/custom-idp-troubleshooting.html): Solutions for issues with custom identity providers in AWS Transfer Family, including API Gateway integration errors, Lambda function timeouts, and authentication failures.
- [Workflow issues](https://docs.aws.amazon.com/transfer/latest/userguide/workflow-issues.html): Solutions for common issues with AWS Transfer Family managed workflows, including execution errors, copy failures, and decryption problems.
- [EFS issues](https://docs.aws.amazon.com/transfer/latest/userguide/efs-troubleshooting.html): Solutions for common issues when using Amazon Elastic File System storage with AWS Transfer Family, including permission problems, POSIX profile configuration, and logical directory setup.
- [Storage and encryption issues](https://docs.aws.amazon.com/transfer/latest/userguide/storage-encryption-issues.html): Solutions for common storage and encryption problems with AWS Transfer Family, including encrypted S3 bucket access and resource location issues.
- [Monitoring and alerting issues](https://docs.aws.amazon.com/transfer/latest/userguide/monitoring-issues.html): Information about troubleshooting monitoring and alerting issues with AWS Transfer Family.
- [Cross-region transfer issues](https://docs.aws.amazon.com/transfer/latest/userguide/cross-region-transfer-issues.html): Solutions for common problems when transferring files between AWS Regions using AWS Transfer Family, including permission issues and performance optimization.
- [Terraform deployment issues](https://docs.aws.amazon.com/transfer/latest/userguide/terraform-deployment-issues.html): Solutions for common problems when deploying AWS Transfer Family resources using Terraform, including resource creation failures and state management issues.
- [WAF integration issues](https://docs.aws.amazon.com/transfer/latest/userguide/waf-integration-issues.html): Solutions for common problems when integrating AWS WAF with AWS Transfer Family, including false positives and custom identity provider authentication failures.
- [Service-managed user issues](https://docs.aws.amazon.com/transfer/latest/userguide/service-managed-issues.html): Solutions for common problems with service-managed users in AWS Transfer Family, including public key format issues and key length constraints.
- [AS2 issues](https://docs.aws.amazon.com/transfer/latest/userguide/as2-troubleshooting.html): Solutions for common problems with Applicability Statement 2 (AS2) transfers in AWS Transfer Family, including certificate issues and Message Disposition Notification (MDN) receipt problems.
