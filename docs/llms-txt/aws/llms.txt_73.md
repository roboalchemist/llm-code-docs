# Source: https://docs.aws.amazon.com/amazonglacier/latest/dev/llms.txt

# Amazon Glacier Developer Guide

> Amazon Glacier (Amazon Glacier) provides a low-cost storage service optimized for durable storage with security features for data archiving and backup of infrequently used data, or "cold data." The Amazon Glacier Developer Guide explains how to use the Amazon Glacier web service to create, configure, and manage vaults and archives using both the AWS Management Console and the Amazon Glacier API.

- [Data Retrieval Policies](https://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html)
- [Tagging Resources](https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html)
- [Audit Logging with AWS CloudTrail](https://docs.aws.amazon.com/amazonglacier/latest/dev/audit-logging.html)
- [Document History](https://docs.aws.amazon.com/amazonglacier/latest/dev/document-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/amazonglacier/latest/dev/glossary.html)

## [What Is Amazon Glacier?](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)

- [Data Model](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-data-model.html): Amazon Glacier is a REST-based web service.
- [Supported Operations](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-supported-operations.html): Amazon Glacier supports a set of operations to retrieve an archive or a vault inventory.
- [Accessing Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-accessing.html): Access Amazon Glacier through direct requests to the Amazon Glacier web service API or by using the AWS SDKs that wrap the Amazon Glacier REST API calls.


## [Getting Started](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-getting-started.html)

- [Step 1: Before You Begin](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-before-you-begin.html): To begin with Amazon Glacier, sign up for an AWS account and download the AWS SDK for Java, .NET, or PHP.
- [Step 2: Create a Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-create-vault.html): Example of how to create a vault, which is a container for storing archives, in Amazon Glacier in the US West (Oregon) Region.

### [Step 3: Upload an Archive to a Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-upload-archive.html)

Example of how to upload a sample archive to the vault that you created in Amazon Glacier.

- [Upload an Archive by Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-upload-archive-java.html): Java code example to upload a sample archive to the vault in Amazon Glacier by using the AWS SDK for Java.
- [Upload an Archive by Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-upload-archive-dotnet.html): C# code example to upload a sample archive to the vault in Amazon Glacier by using the high-level API of the AWS SDK for .NET.

### [Step 4: Download an Archive from a Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-download-archive.html)

Example of how to download an archive from a vault in Amazon Glacier by initiating a retrieval job and then downloading the bytes after the job is completed.

- [Download an Archive by Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-download-archive-java.html): Java code example to download an archive from a vault in Amazon Glacier by using the AWS SDK for Java.
- [Download an Archive by Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-download-archive-dotnet.html): C# code example to download an archive that you have uploaded in Amazon Glacier by using the high-level API of the AWS SDK for .NET.

### [Step 5: Delete an Archive from a Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-delete-archive.html)

Example of how to delete an archive from a vault in Amazon Glacier.

- [Delete an Archive by Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-delete-archive-java.html): Java code example to delete an archive that you have uploaded to a vault in Amazon Glacier by using the AWS SDK for Java.
- [Delete an Archive by Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-delete-archive-dotnet.html): C# code example to delete an archive that you have uploaded to a vault in Amazon Glacier by using the AWS SDK for .NET high-level API.
- [Deleting an Archive by Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-delete-archive-cli.html): Set up the AWS Command Line Interface (AWS CLI) and use the delete-archive command to delete an archive in Amazon Glacier.
- [Step 6: Delete a Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-delete-vault.html): Example of how to delete a vault, which is a container for storing archives, in Amazon Glacier in the US West (Oregon) Region by using the AWS Management Console.
- [Where Do I Go From Here?](https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-where-do-i-go-next.html): The next step is to learn more about working with vaults and archives in Amazon Glacier.


## [Working with Vaults](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html)

### [Creating a Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html)

Examples of how to create a vault in Amazon Glacier using the AWS SDK for Java, AWS SDK for .NET, the REST API, or the Amazon Glacier console.

- [Creating a Vault Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults-sdk-java.html): Java code example of how to create a vault in Amazon Glacier using the AWS SDK for Java.
- [Creating a Vault Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults-dotnet-sdk.html): C# code example of how to create a vault in Amazon Glacier using the AWS SDK for .NET for either high-level and low-level APIs.
- [Creating a Vault Using REST](https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults-rest-api.html): Example of how to create a vault in Amazon Glacier using the REST API,
- [Creating a Vault Using the Console](https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults-console.html): Create a vault using the Amazon Glacier console.
- [Creating a Vault Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults-cli.html): Set up the AWS CLI and use the create-vault command to create a vault in Amazon Glacier.

### [Retrieving Vault Metadata](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html)

Examples of retrieving vault information and metadata in Amazon Glacier using the Amazon SDK for Java, Amazon SDK for .NET, or REST API.

- [Retrieving Vault Metadata Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info-sdk-java.html): Java code example of retrieving vault information and metadata in Amazon Glacier using the Amazon SDK for Java.
- [Retrieving Vault Metadata Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info-sdk-dotnet.html): C# code example of retrieving vault information and metadata in Amazon Glacier using the Amazon SDK for .NET.
- [Retrieving Vault Metadata Using REST](https://docs.aws.amazon.com/amazonglacier/latest/dev/listing-vaults-rest-api.html): Example of retrieving vault information in Amazon Glacier using the REST API.
- [Retrieving Vault Metadata Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info-cli.html): Set up the AWS CLI and follow this example of retrieving vault information and metadata in Amazon Glacier.

### [Downloading a Vault Inventory](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html)

Examples of downloading or retrieving a vault inventory in Amazon Glacier using the AWS SDK for Java low-level API, AWS SDK for .NET, or REST API.

- [Downloading a Vault Inventory Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-inventory-java.html): Java code examples of downloading or retrieving a vault inventory using the Amazon SDK for Java low-level API.
- [Downloading a Vault Inventory Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-inventory-sdk-dotnet.html): C# code examples of downloading or retrieving a vault inventory in Amazon Glacier using the Amazon SDK for .NET.
- [Downloading a Vault Inventory Using REST](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-inventory-rest-api.html): Example of downloading or retrieving a vault inventory in Amazon Glacier using the REST API.
- [Downloading a Vault Inventory Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-inventory-cli.html): Example of downloading or retrieving a vault inventory in Amazon Glacier using the AWS CLI.

### [Configuring Vault Notifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html)

Create and delete vaults, get vault metadata, download vault inventories, and configure vault notifications.

- [Configuring Vault Notifications Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications-sdk-java.html): Java code examples on how to configure vault notifications in Amazon Glacier using the Amazon SDK for Java.
- [Configuring Vault Notifications Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications-sdk-dotnet.html): C# code examples on how to configure vault notifications in Amazon Glacier using the Amazon SDK for .NET low-level API.
- [Configuring Vault Notifications Using the REST API](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications-rest-api.html): Configure vault notifications in Amazon Glacier by using the REST API.
- [Configuring Vault Notifications by Using the Console](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications-console.html): Configure vault notifications by using the Amazon Glacier console to specify job completion and publish notification events.
- [Configuring Vault Notifications Using the CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications-cli.html): Configure vault notifications using the AWS Command Line Interface to specify job completion and publish notification events.

### [Deleting a Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults.html)

Examples of how to delete a vault in Amazon Glacier using the Amazon SDK for Java, Amazon SDK for .NET, the REST API, or the Amazon Glacier console.

- [Deleting a Vault Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults-sdk-java.html): Java code example of how to delete a vault in Amazon Glacier using the Amazon SDK for Java.
- [Deleting a Vault Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults-sdk-dotnet.html): C# code example of how to delete a vault in Amazon Glacier using the Amazon SDK for .NET for both high-level and low-level APIs.
- [Deleting a Vault Using REST](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vault-rest-api.html): Examples of how to delete a vault in Amazon Glacier using the REST API.
- [Deleting an Empty Vault by Using the Console](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults-console.html): Example of how to delete an empty vault by using the Amazon Glacier console.
- [Deleting a Vault Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults-cli.html): Set up the AWS CLI and use the delete-vault command to delete a vault in Amazon Glacier.
- [Tagging Vaults](https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging-vaults.html): Assign your own metadata tags to your Amazon Glacier vaults to help you manage them.

### [Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html)

Explains how to use Amazon Glacier Vault Lock to lock vaults and use Vault Lock policies to enforce compliance controls.

- [Vault Locking by Using the API](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-how-to-api.html): Explains how to lock an Amazon Glacier vault by using the API.
- [Vault Locking Using the CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-how-to-cli.html): Explains how to lock a Amazon Glacier vault by using the CLI.
- [Vault Locking by Using the Console](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-walkthrough.html): Explains how to lock an Amazon Glacier vault by using the console.


## [Working with Archives](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html)

### [Uploading an Archive](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html)

Examples of uploading an archive in Amazon Glacier in either a single operation or in parts using the multipart upload API.

### [Uploading an Archive in a Single Operation](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-single-operation.html)

Examples of uploading an archive in Amazon Glacier in a single operation using the Amazon SDK for Java, Amazon SDK for .NET, or the REST API.

- [Uploading an Archive in a Single Operation Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-single-op-using-cli.html): Example of uploading an archive in Amazon Glacier in a single operation using the AWS Command Line Interface
- [Uploading an Archive in a Single Operation Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-single-op-using-java.html): Java code example of uploading an archive in a single operation in Amazon Glacier using the Amazon SDK for Java.
- [Uploading an Archive in a Single Operation Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-single-op-using-dotnet.html): C# code examples of uploading an archive in Amazon Glacier in a single operation using the Amazon SDK for .NET.
- [Uploading an Archive in a Single Operation Using REST](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-single-op-using-rest.html): Example of uploading an archive in Amazon Glacier in a single operation using the REST API.

### [Uploading Large Archives in Parts](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html)

Examples of uploading large archives in parts in Amazon Glacier using the Multipart Upload API.

- [Uploading Large Archives in Parts by Using AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-mpu-using-cli.html): Learn how to upload an archive in Amazon Glacier in a single operation by using the AWS Command Line Interface (AWS CLI).
- [Uploading Large Archives in Parts Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-mpu-using-java.html): Java code examples of uploading large archives in parts in Amazon Glacier using the Amazon SDK for Java.
- [Uploading Large Archives in Parts Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-mpu-using-dotnet.html): C# code example of uploading large archives in parts in Amazon Glacier using the Amazon SDK for .NET.
- [Uploading Large Archives in Parts Using the REST API](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive-mpu-using-rest.html): Example of uploading large archives in parts in Amazon Glacier using the REST API.

### [Downloading an Archive](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive.html)

Examples of downloading an archive in Amazon Glacier by using the AWS SDK for Java, AWS SDK for .NET, or the Amazon Glacier REST API.

- [Retrieving Archives](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-two-steps.html): Explains Amazon Glacier archive retrievals and retrieval options.
- [Downloading an Archive Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-using-java.html): Java code examples of downloading an archive in Amazon Glacier using the Amazon SDK for Java.
- [Downloading an Archive Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-using-dotnet.html): C# code examples of downloading an archive in Amazon Glacier using the Amazon SDK for .NET.
- [Downloading a Large Archive Using Python](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-large-archive-parallel-python.html): Python code example of downloading a large archive from Amazon Glacier using parallel processing to overcome connection timeout issues.
- [Downloading an Archive by Using REST](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-using-rest.html): Example of downloading an archive in Amazon Glacier by using the REST API.
- [Downloading an Archive Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-using-cli.html): Examples of downloading an archive in Amazon Glacier using the AWS Command Line Interface.

### [Deleting an Archive](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html)

Examples of how to delete an archive from a vault in Amazon Glacier using the Amazon SDK for Java, Amazon SDK for .NET, or the REST API.

- [Deleting an Archive Using Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive-using-java.html): Java code example of how to delete an archive from a vault in Amazon Glacier using the Amazon SDK for Java.
- [Deleting an Archive Using .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive-using-dot-net.html): C# code examples of how to delete an archive from a vault in Amazon Glacier using the Amazon SDK for .NET for both high-level and low-level APIs.
- [Deleting an Archive Using REST](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive-using-rest.html): How to delete an archive from a vault in Amazon Glacier using the REST API.
- [Deleting an Archive Using the AWS CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive-using-cli.html): Set up the AWS CLI and use the delete-archive command to delete an archive in Amazon Glacier.


## [Using the AWS SDKs](https://docs.aws.amazon.com/amazonglacier/latest/dev/using-aws-sdk.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/amazonglacier/latest/dev/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Using the AWS SDK for Java](https://docs.aws.amazon.com/amazonglacier/latest/dev/using-aws-sdk-for-java.html): Use the Amazon SDK for Java with Amazon Glacier with both low-level and high-level APIs.
- [Using the AWS SDK for .NET](https://docs.aws.amazon.com/amazonglacier/latest/dev/using-aws-sdk-for-dot-net.html): Use the Amazon SDK for .NET with Amazon Glacier with both low-level and high-level APIs.


## [Code examples](https://docs.aws.amazon.com/amazonglacier/latest/dev/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/amazonglacier/latest/dev/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Glacier with AWS SDKs.

- [Hello Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_Hello_section.html): Hello Amazon Glacier

### [Actions](https://docs.aws.amazon.com/amazonglacier/latest/dev/service_code_examples_actions.html)

The following code examples show how to use Amazon Glacier with AWS SDKs.

- [AddTagsToVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_AddTagsToVault_section.html): Use AddTagsToVault with an AWS SDK or CLI
- [CreateVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_CreateVault_section.html): Use CreateVault with an AWS SDK or CLI
- [DeleteArchive](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_DeleteArchive_section.html): Use DeleteArchive with an AWS SDK or CLI
- [DeleteVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_DeleteVault_section.html): Use DeleteVault with an AWS SDK or CLI
- [DeleteVaultNotifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_DeleteVaultNotifications_section.html): Use DeleteVaultNotifications with an AWS SDK or CLI
- [DescribeJob](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_DescribeJob_section.html): Use DescribeJob with an AWS SDK or CLI
- [DescribeVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_DescribeVault_section.html): Use DescribeVault with an AWS SDK or CLI
- [GetJobOutput](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_GetJobOutput_section.html): Use GetJobOutput with an AWS SDK or CLI
- [GetVaultNotifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_GetVaultNotifications_section.html): Use GetVaultNotifications with an AWS SDK or CLI
- [InitiateJob](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_InitiateJob_section.html): Use InitiateJob with an AWS SDK or CLI
- [ListJobs](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_ListJobs_section.html): Use ListJobs with an AWS SDK or CLI
- [ListTagsForVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_ListTagsForVault_section.html): Use ListTagsForVault with an AWS SDK or CLI
- [ListVaults](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_ListVaults_section.html): Use ListVaults with an AWS SDK or CLI
- [SetVaultNotifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_SetVaultNotifications_section.html): Use SetVaultNotifications with an AWS SDK or CLI
- [UploadArchive](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_UploadArchive_section.html): Use UploadArchive with an AWS SDK or CLI
- [UploadMultipartPart](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_UploadMultipartPart_section.html): Use UploadMultipartPart with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/amazonglacier/latest/dev/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Glacier with AWS SDKs.

- [Archive a file, get notifications, and initiate a job](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_Usage_UploadNotifyInitiate_section.html): Archive a file to Amazon Glacier, get notifications, and initiate a job using an AWS SDK
- [Get archive content and delete the archive](https://docs.aws.amazon.com/amazonglacier/latest/dev/example_glacier_Usage_RetrieveDelete_section.html): Get Amazon Glacier archive content and delete the archive using an AWS SDK


## [Security](https://docs.aws.amazon.com/amazonglacier/latest/dev/security.html)

### [Data Protection](https://docs.aws.amazon.com/amazonglacier/latest/dev/DataDurability.html)

Amazon Glacier provides durable storage for data archiving and long-term backup.

- [Data Encryption](https://docs.aws.amazon.com/amazonglacier/latest/dev/DataEncryption.html): Use data encryption to provide added security for your data objects stored in Amazon Glacier.
- [Key Management](https://docs.aws.amazon.com/amazonglacier/latest/dev/key-management.html): Encrypt data at rest in Amazon Glacier using keys that are maintained by AWS.
- [Internetwork Traffic Privacy](https://docs.aws.amazon.com/amazonglacier/latest/dev/InternetworkTrafficPrivacy.html): Describes how Amazon Glacier secures connections from the service to other locations.

### [Identity and Access Management](https://docs.aws.amazon.com/amazonglacier/latest/dev/security-iam.html)

How to authenticate requests and manage access to your Amazon Glacier resources.

- [How Amazon Glacier works with IAM](https://docs.aws.amazon.com/amazonglacier/latest/dev/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Glacier, learn what IAM features are available to use with Amazon Glacier.
- [Identity-based policy examples](https://docs.aws.amazon.com/amazonglacier/latest/dev/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Glacier resources.

### [Resource-based policy examples](https://docs.aws.amazon.com/amazonglacier/latest/dev/security_iam_resource-based-policy-examples.html)

A Amazon Glacier vault can have one vault access policy and one Vault Lock policy associated with it.

- [Vault Access Policies](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html): Control access to vaults with vault access policies.
- [Vault Lock Policies](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html): An Amazon Glacier (Amazon Glacier) vault can have one resource-based vault access policy and one Vault Lock policy attached to it.
- [Troubleshooting](https://docs.aws.amazon.com/amazonglacier/latest/dev/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Glacier and IAM.
- [Amazon Glacier API Permissions Reference](https://docs.aws.amazon.com/amazonglacier/latest/dev/glacier-api-permissions-ref.html): When you are setting up and writing a permissions policy that you can attach to an IAM identity (identity-based policies) or a resource (resource-based policies), you can use the following table as a reference.
- [Logging and Monitoring](https://docs.aws.amazon.com/amazonglacier/latest/dev/glacier-incident-response.html): Tools in Amazon Glacier for monitoring resources and responding to incidents.
- [Compliance Validation](https://docs.aws.amazon.com/amazonglacier/latest/dev/glacier-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/amazonglacier/latest/dev/disaster-recovery-resiliency.html): Describes AWS architecture for data redundancy and specific Amazon Glacier services for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/amazonglacier/latest/dev/network-isolation.html): Describes how Amazon Glacier isolates service traffic.


## [API Reference](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-api.html)

- [Common Request Headers](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-common-request-headers.html): Lists the Amazon Glacier REST request headers that contain basic information about the request.
- [Common Response Headers](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-common-response-headers.html): Response headers that are common to most Amazon Glacier responses.
- [Signing Requests](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-signing-requests.html): Sign requests with a digital signature using a cryptographic hash function to authenticate your requests in Amazon Glacier.

### [Computing Checksums](https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html)

Examples of how to compute checksums when uploading an archive in either a single request or using a multipart upload.

- [Receiving Checksums When Downloading Data](https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations-range.html): Examples of how to retrieve an archive range when downloading data.
- [Error Responses](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-error-responses.html): Lists error exceptions, responses, codes, and their descriptions returned by the Amazon Glacier API.

### [Vault Operations](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-operations.html)

Lists the API vault operations available for use in Amazon Glacier.

- [Abort Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AbortVaultLock.html): Stops the Amazon Glacier vault locking process for the specified vault.
- [Add Tags To Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AddTagsToVault.html): Add tags to a vault.
- [Create Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html): Creates a new vault with the unique name that you have specified.
- [Complete Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-CompleteVaultLock.html): Completes the Amazon Glacier vault locking process.
- [Delete Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html): Deletes a vault, if there are no archives in the vault and there have been no writes to the vault since the last inventory.
- [Delete Vault Access Policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-DeleteVaultAccessPolicy.html): Deletes the current access policy for the specified vault.
- [Delete Vault Notifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-delete.html): Deletes the notification configuration set for a vault.
- [Describe Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-get.html): Returns information about a vault, including the vault ARN, the creation date, the number of archives, and the total size of all the archives.
- [Get Vault Access Policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetVaultAccessPolicy.html): Returns the current access policy for the specified vault.
- [Get Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetVaultLock.html): Returns the current information about the Amazon Glacier vault lock for the specified vault.
- [Get Vault Notifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-get.html): Returns the notification configuration subresource set on the vault, or a 404 error if the notification configuration for the vault is not set.
- [Initiate Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-InitiateVaultLock.html): Initiates the Amazon Glacier vault lock process for the specified vault.
- [List Tags For Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-ListTagsForVault.html): List the tags attached to a vault.
- [List Vaults](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vaults-get.html): Returns a list of all vaults owned by the calling userâs account; the list is ASCII-sorted by vault name.
- [Remove Tags From Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-RemoveTagsFromVault.html): Removes tags from a vault.
- [Set Vault Access Policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetVaultAccessPolicy.html): Sets and enacts a access policy in the specified vault.
- [Set Vault Notification Configuration](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-put.html): Sets a notification configuration on a specific vault.

### [Archive Operations](https://docs.aws.amazon.com/amazonglacier/latest/dev/archive-operations.html)

Lists the API archive operations available for use in Amazon Glacier.

- [Delete Archive](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html): Deletes an archive from a vault so that subsequent requests to initiate a retrieval of this archive will fail.
- [Upload Archive](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html): Adds an archive to a vault.

### [Multipart Upload Operations](https://docs.aws.amazon.com/amazonglacier/latest/dev/multipart-archive-operations.html)

Lists the API multipart upload operations available for use in Amazon Glacier.

- [Abort Multipart Upload](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-upload.html): Stops a multipart upload identified by the upload ID.
- [Complete Multipart Upload](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-complete-upload.html): Informs Amazon Glacier that all the archive parts have been uploaded and to assemble the archive from the uploaded parts.
- [Initiate Multipart Upload](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-initiate-upload.html): Starts a multipart upload where Amazon Glacier creates a multipart upload resource and returns its Upload ID in the response.
- [List Parts](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html): Displays a list of the parts of an archive that have been uploaded in a specific multipart upload identified by an upload ID.
- [List Multipart Uploads](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-uploads.html): Displays a list of in-progress multipart uploads for the specified vault.
- [Upload Part](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-upload-part.html): Uploads a part of an archive.

### [Job Operations](https://docs.aws.amazon.com/amazonglacier/latest/dev/job-operations.html)

Lists the API of job operations available in Amazon Glacier.

- [Describe Job](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-describe-job-get.html): Returns information about a job you previously initiated, including initiation date, user, status code/message, and the Amazon SNS topic to notify.
- [Get Job Output](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html): Downloads the output of the job you initiated using the POST jobs operation.
- [Initiate Job](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html): Starts a job of the specified type, for example a vault inventory or archive retrieval job.
- [List Jobs](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html): Displays a list of jobs for a vault including jobs that are in progress and jobs that have recently finished.

### [Data Types Used in Job Operations](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-data-types.html)

This section describes data types used with Amazon Glacier API job operations.

- [CSVInput](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-CSVInput.html): Contains information about the comma-separated values (CSV) file.
- [CSVOutput](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-CSVOutput.html): Contains information about the comma-separated values (CSV) format that the job results are stored in.
- [Encryption](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-Encryption.html): Contains information about the encryption used to store the job results in Amazon S3.
- [GlacierJobDescription](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GlacierJobDescription.html): Contains the description of a Amazon Glacier job.
- [Grant](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-Grant.html): Contains information about a grant.
- [Grantee](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-Grantee.html): Contains information about a grantee.
- [InputSerialization](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-InputSerialization.html): Describes how the archive is serialized.
- [InventoryRetrievalJobInput](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-InventoryRetrievalJobInput.html): Provides options for specifying a range inventory retrieval job.
- [jobParameters](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobParameters.html): Provides options for defining a job.
- [OutputLocation](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-OutputLocation.html): Contains information about the location where the job results and errors are stored.
- [OutputSerialization](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-OutputSerialization.html): Describes how the output is serialized.
- [S3Location](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-S3Location.html): Contains information about the location in Amazon S3 where the job results are stored.
- [SelectParameters](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SelectParameters.html): Contains information about the parameters used for the select.

### [Data Retrieval Operations](https://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy-operations.html)

Lists the API of the data retrievalârelated operations available in Amazon Glacier.

- [Get Data Retrieval Policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetDataRetrievalPolicy.html): Returns the current data retrieval policy for the AWS account and AWS Region specified.
- [List Provision Capacity](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-ListProvisionedCapacity.html): List the provisioned capacity.
- [Purchase Provisioned Capacity](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-PurchaseProvisionedCapacity.html): This operation purchases a provisioned capacity unit for an AWS account.
- [Set Data Retrieval Policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetDataRetrievalPolicy.html): Sets and enacts a data retrieval policy in the specified AWS Region.
