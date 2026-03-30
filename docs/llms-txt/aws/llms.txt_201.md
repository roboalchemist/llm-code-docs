# Source: https://docs.aws.amazon.com/cloudhsm/latest/userguide/llms.txt

# AWS CloudHSM User Guide

> Learn how to use AWS CloudHSM, a web service that provides cost effective hardware key management at cloud scale for sensitive and regulated workloads. AWS CloudHSM provides a managed hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud.

- [Cloned clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloned-clusters.html)
- [Performance](https://docs.aws.amazon.com/cloudhsm/latest/userguide/performance.html)
- [Quotas](https://docs.aws.amazon.com/cloudhsm/latest/userguide/limits.html)
- [Document history](https://docs.aws.amazon.com/cloudhsm/latest/userguide/document-history.html)

## [What is AWS CloudHSM?](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)

- [Use cases](https://docs.aws.amazon.com/cloudhsm/latest/userguide/use-cases.html): Get an overview of the goals (use cases) that you can accomplish with AWS CloudHSM.

### [How it works](https://docs.aws.amazon.com/cloudhsm/latest/userguide/whatis-concepts.html)

Learn the basic terms and concepts used in AWS CloudHSM and how they work together to help protect your data.

- [Clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html): Create a collection of synchronized HSMs, called a cluster, for load balancing and to improve reliability.
- [Users in AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-users.html): You must use an identity completely separate from the IAM resources in your AWS account to access AWS CloudHSM.
- [Keys in AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/whatis-hsm-keys.html): AWS CloudHSM allows you to securely generate, store, and manage your encryption keys in single-tenant HSMs that are in your AWS CloudHSM cluster.
- [Client SDKs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-tools-and-libraries.html): Use AWS CloudHSM Client SDKs to manage and use the HSM in your cluster.
- [Backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/backups.html): AWS CloudHSM makes secure backups of your cluster on a regular basis, using NSIT compliant methods and functions for cryptographic operations.
- [Supported Regions for AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/regions.html): Use AWS CloudHSM in these supported AWS Regions.
- [Pricing for AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pricing.html): With AWS CloudHSM, you pay by the hour with no long-term commitments or upfront payments.


## [Getting started](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html)

- [Create IAM administrators](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-iam-user.html): The first step to getting started with AWS CloudHSM is to set up IAM permissions.
- [Create a VPC](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-vpc.html): To begin setting up an AWS CloudHSM cluster, create a virtual private cloud (VPC).
- [Create a cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-cluster.html): Create an AWS CloudHSM cluster
- [Review the cluster security group](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html): Configure the cluster's default security group to communicate with an Amazon EC2 client instance.
- [Launch an EC2 client](https://docs.aws.amazon.com/cloudhsm/latest/userguide/launch-client-instance.html): Create an Amazon EC2 instance to access your AWS CloudHSM cluster.
- [Configure EC2 instance security groups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg-client-instance.html): Attach the cluster security group to the Amazon EC2 instance to allow communication between an Amazon EC2 client and AWS CloudHSM instances.
- [Create an HSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-hsm.html): Create your first HSM.
- [Verify HSM identity (optional)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/verify-hsm-identity.html): To verify the identity and authenticity of the HSM in your AWS CloudHSM cluster, get the certificates and signing request, verify the certificate chains, and compare public keys.
- [Initialize the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html): Initialize your AWS CloudHSM cluster by first obtaining and signing its certificate signing request.
- [Install CloudHSM CLI](https://docs.aws.amazon.com/cloudhsm/latest/userguide/gs_cloudhsm_cli-install.html): Install CloudHSM CLI on your Amazon EC2 instance so you can interact with the HSMs in your cluster.
- [Activate the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/activate-cluster.html): Activate an AWS CloudHSM cluster by logging in to the hardware security module (HSM) as the unactivated admin and then changing the default password to become the admin.
- [Setup mTLS (recommended)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started-setup-mtls.html): Setup mTLS
- [Create and use keys in AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-apps.html): Build applications and work with keys using AWS CloudHSM.


## [Best practices](https://docs.aws.amazon.com/cloudhsm/latest/userguide/best-practices.html)

- [Cluster management](https://docs.aws.amazon.com/cloudhsm/latest/userguide/bp-cluster-management.html): Get a high-level list of best practices for working with AWS CloudHSM clusters.
- [User management](https://docs.aws.amazon.com/cloudhsm/latest/userguide/bp-hsm-user-management.html): Get a high-level list of best practices for working with AWS CloudHSM users.
- [Key management](https://docs.aws.amazon.com/cloudhsm/latest/userguide/bp-hsm-key-management.html): Get a high-level list of best practices for working with AWS CloudHSM keys.
- [Application integration](https://docs.aws.amazon.com/cloudhsm/latest/userguide/bp-application-integration.html): Get a high-level list of best practices for working with AWS CloudHSM application integration.
- [Monitoring](https://docs.aws.amazon.com/cloudhsm/latest/userguide/bp-monitoring.html): Get a high-level list of best practices for working with AWS CloudHSM monitoring.


## [Clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-clusters.html)

- [Cluster architecture](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-architecture.html): When you create a cluster, you specify an Amazon Virtual Private Cloud (VPC) in your AWS account and one or more subnets in that VPC.
- [Cluster synchronization](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-synchronization.html): In an AWS CloudHSM cluster, AWS CloudHSM keeps the keys on the individual HSMs in sync.
- [Cluster high availability and load balancing](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-high-availability-load-balancing.html): When you create an AWS CloudHSM cluster with more than one HSM, you automatically get load balancing.
- [Cluster modes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-hsm-types.html): AWS CloudHSM offers multiple cluster modes and HSM types.
- [HSM types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-types.html): AWS CloudHSM also offers two hardware security module (HSM) types: hsm1.medium and hsm2m.medium.
- [Connecting to the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-connect.html): Use the instruction in this topic for connecting to the cluster using Client SDK 5 or Client SDK 3.

### [Scaling HSMs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/add-remove-hsm.html)

Scale your AWS CloudHSM cluster up or down by adding or removing HSMs with the AWS CloudHSM console, AWS SDKs, or command line tools.

- [Adding an HSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/add-hsm.html): Scale your AWS CloudHSM cluster up by adding or HSMs with the AWS CloudHSM console, AWS SDKs, or command line tools.
- [Removing an HSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/remove-hsm.html): Scale your AWS CloudHSM cluster down by adding HSMs with the AWS CloudHSM console, AWS SDKs, or command line tools.
- [Deleting a cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete-cluster.html): Delete an AWS CloudHSM cluster by using the AWS CloudHSM console, AWS SDKs, or command line tools.
- [Creating clusters from backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-cluster-from-backup.html): Create a new cluster by restoring the cluster from a backup.

### [Migrating HSM cluster types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-hsm-type-modification.html)

Upgrade the AWS CloudHSMtype of an existing cluster.

- [Migrating from hsm1.medium to hsm2m.medium](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm1-to-hsm2-migration.html): Upgrade your AWS CloudHSM cluster from hsm1.medium to hsm2m.medium


## [HSM users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users.html)

### [User management with CloudHSM CLI](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users-chsm-cli.html)

Manage AWS CloudHSM users with CloudHSM CLI.

- [Prerequisites](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users-chsm-cli-prereq.html): Before you use CloudHSM CLI to manage hardware security modules (HSM) users in AWS CloudHSM, you must complete these prerequisites.
- [User types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understanding-users.html): Use the credentials of the appropriate type of HSM user to securely interact with the HSMs in your AWS CloudHSM cluster.
- [Permissions table](https://docs.aws.amazon.com/cloudhsm/latest/userguide/user-permissions-table-chsm-cli.html): The following table lists hardware security module (HSM) operations sorted by the type of HSM user or session that can perform the operation in AWS CloudHSM.
- [Create admin](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-admin-cloudhsm-cli.html): Follow these steps to create a hardware security module (HSM) admin user using the CloudHSM CLI.
- [Create CUs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-user-cloudhsm-cli.html): Follow these steps to create a hardware security module (HSM) crypto user (CU) using the CloudHSM CLI.
- [List all users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/list-users-cloudhsm-cli.html): Use user list command in the CloudHSM CLI to list all the users in the AWS CloudHSM cluster.
- [Change passwords](https://docs.aws.amazon.com/cloudhsm/latest/userguide/change-user-password-cloudhsm-cli.html): Use the user change-password command in the CloudHSM CLI to change a hardware security module (HSM) user's password.
- [Delete users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete-user-cloudhsm-cli.html): Use user delete in the CloudHSM CLI to delete a hardware security module (HSM) user.

### [Manage user MFA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/login-mfa-token-sign.html)

Add an extra layer of protection for accessing the cluster as the admin.

- [Quorum authentication](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-mfa-cloudhsm-cli.html): The AWS CloudHSM cluster uses the same key for quorum authentication and for multi-factor authentication (MFA).
- [Key pair requirements](https://docs.aws.amazon.com/cloudhsm/latest/userguide/mfa-key-pair-cloudhsm-cli.html): To enable multi-factor authentication (MFA) for a hardware security module (HSM) user in AWS CloudHSM, you can create a new key pair or use an existing key that meets the following requirements:
- [Set up MFA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/set-up-mfa-for-cloudhsm-cli.html): Follow these steps to set up multi-factor authentication (MFA) for CloudHSM CLI.
- [Create users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-mfa-users-cloudhsm-cli.html): Follow these steps to create AWS CloudHSM users with multi-factor authentication (MFA) enabled.
- [Log in users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/login-mfa-cloudhsm-cli.html): Follow these steps to log in AWS CloudHSM users with multi-factor authentication (MFA) enabled.
- [Rotate keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/rotate-mfa-cloudhsm-cli.html): Follow these steps to rotate keys for AWS CloudHSM users with multi-factor authentication (MFA) enabled.
- [Deregister an MFA public key](https://docs.aws.amazon.com/cloudhsm/latest/userguide/deregister-mfa-cloudhsm-cli.html): Follow these steps to deregister a multi-factor authentication (MFA) public key for AWS CloudHSM admin users when MFA public key is registered.
- [Token file reference](https://docs.aws.amazon.com/cloudhsm/latest/userguide/reference-mfa-cloudhsm-cli.html): The token file generated when either registering a multi-factor authentication (MFA) public key or when attempting to login to the CloudHSM CLI using MFA consists of the following:

### [Manage quorum authentication (M of N)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli.html)

Enable and enforce quorum authentication (also known as M of N access control) on the HSM in your AWS CloudHSM cluster.

- [Quorum authentication process](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-overview.html): Learn about the quorum authentication processes for CloudHSM CLI
- [Supported services and types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-service-names.html): Admin Services: Quorum authentication is used for admin privileged services like creating users, deleting users, changing user passwords, setting quorum values, and deactivating quorum and MFA capabilities.
- [First time setup](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-first-time.html): Set up admins to use quorum authentication for hardware security module (HSM) user management operations on the HSM in your AWS CloudHSM cluster.
- [User management with quorum (M of N)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-admin.html): Use quorum authentication for HSM user management operations that admins perform on the HSM in your AWS CloudHSM cluster.
- [Change the minimum value](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-min-value.html): Change the quorum minimum value for HSM user management operations that crypto officers (COs) perform on the HSM in your CloudHSM cluster.

### [User management with CMU](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users-cmu.html)

Manage AWS CloudHSM users with CloudHSM CLI and CloudHSM Management Utility (CMU).

- [Prerequisites](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understand-users.html): Before you use AWS CloudHSM Management Utility (CMU) to manage hardware security module (HSM) users in AWS CloudHSM, you must complete these prerequisites.
- [User types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understanding-users-cmu.html): Use the credentials of the appropriate type of HSM user to securely interact with the HSMs in your AWS CloudHSM cluster.
- [Permissions table](https://docs.aws.amazon.com/cloudhsm/latest/userguide/user-permissions-table-cmu.html): The following table lists hardware security module (HSM( operations sorted by the type of HSM user or session that can perform the operation in AWS CloudHSM.
- [Create users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-users-cmu.html): Use createUser in AWS CloudHSM Management Utility (CMU) to create new users on the hardware security module (HSM).
- [List all users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/list-users.html): Use listUsers command in the AWS CloudHSM Management Utility (CMU) to list all the users in the AWS CloudHSM cluster.
- [Change passwords](https://docs.aws.amazon.com/cloudhsm/latest/userguide/change-user-password-cmu.html): Use changePswd in the AWS CloudHSM Management Utility (CMU) to change a hardware security module (HSM) user's password.
- [Delete users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete-user.html): Use deleteUser in the AWS CloudHSM Management Utility (CMU) to delete a hardware security module (HSM) user.

### [Manage user 2FA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-2fa.html)

Add an extra layer of protection for accessing the cluster as the crypto officer (CO).

- [Quorum authentication](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-2fa.html): The cluster uses the same key for quorum authentication and for two-factor authentication 2FA).
- [Key pair requirements](https://docs.aws.amazon.com/cloudhsm/latest/userguide/enable-2fa-kms.html): To enable two-factor authentication (2FA) for an AWS CloudHSM hardware security module (HSM) user, use a key that meets the following requirements.
- [Create users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-2fa.html): Use AWS CloudHSM Management Utility CMU (CMU) and the key pair to create a new crypto office (CO) user with two-factor authentication (2FA) enabled.
- [Manage user 2FA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/rotate-2fa.html): Use changePswd in AWS CloudHSM Management Utility (CMU) to modify two-factor authentication (2FA) for a user.
- [Disable 2FA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/disable-2fa.html): Use the AWS CloudHSM Management Utility (CMU) to disable two-factor authentication (2FA) for hardware security module HSM) users in AWS CloudHSM.
- [Configuration reference](https://docs.aws.amazon.com/cloudhsm/latest/userguide/reference-2fa.html): The following is an example of the two-factor authentication (2FA) properties in the authdata file for both the AWS CloudHSM Management Utility (CMU) generated request and your responses.

### [Using CMU to manage quorum authentication](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-authentication.html)

Enable and enforce quorum authentication (also known as M of N access control) on the HSM in your AWS CloudHSM cluster.

- [Quorum authentication process](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-authentication-overview.html): The following steps summarize the quorum authentication processes.
- [First time setup](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-authentication-crypto-officers-first-time-setup.html): Set up crypto officers (COs) to use quorum authentication for hardware security module (HSM) user management operations on the HSM in your AWS CloudHSM cluster.
- [User management with quorum (M of N)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-authentication-crypto-officers.html): Use quorum authentication for HSM user management operations that crypto officers (COs) perform on the HSM in your AWS CloudHSM cluster.
- [Change the minimum value](https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-authentication-crypto-officers-change-minimum-value.html): Change the quorum minimum value for HSM user management operations that crypto officers (COs) perform on the HSM in your AWS CloudHSM cluster.


## [Keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys.html)

### [Key sync and durability](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-key-sync.html)

Synchronize AWS CloudHSM token keys.

- [Concepts](https://docs.aws.amazon.com/cloudhsm/latest/userguide/concepts-key-sync.html): The following are concepts to be aware of when working with keys in AWS CloudHSM.
- [Understanding key synchronization](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understand-key-sync.html): AWS CloudHSM uses key synchronization to clone token keys across all the hardware security modules (HSM) in a cluster.
- [Change client key durability settings](https://docs.aws.amazon.com/cloudhsm/latest/userguide/working-client-sync.html): Key synchronization is mostly an automatic process, but you can manage client-side key durability settings.
- [Synchronizing keys across cloned clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cli-sync.html): Client-side and server-side synchronization are only for synchronizing keys within the same AWS CloudHSM cluster.
- [AES key wrapping](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-aes-key-wrapping.html): AES Key Wrap options available in AWS CloudHSM and how to use them.

### [Trusted keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-using-trusted-keys.html)

Use trusted keys and trusted wrap attributes to secure data from an insider threat or an attacker.

- [Understanding trusted keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understand-trusted-key-wraps.html): A trusted key is a key that is used to wrap other keys and that admins and cryptographic officers (COs) specifically identify as trusted using the attribute CKA_TRUSTED.
- [Trusted key attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_attribute_background.html): The following attributes allow you to mark an AWS CloudHSM key as trusted, specify a data key can only be wrapped and unwrapped with a trusted key, and control what a data key can do after it is unwrapped:
- [How to use trusted keys to wrap data keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/wrap_keys_using_trusted.html): To use a trusted key to wrap a data key in AWS CloudHSM, you must complete three basic steps:
- [How to unwrap a data key with a trusted key](https://docs.aws.amazon.com/cloudhsm/latest/userguide/unwrap_keys_using_trusted.html): To unwrap a data key in AWS CloudHSM, you need a trusted key that has CKA_UNWRAP set to true.

### [Key management with CloudHSM CLI](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-chsm-cli.html)

If using the latest SDK version series, use CloudHSM CLI to manage the keys in your AWS CloudHSM cluster.

### [Generate keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-cloudhsm-cli-generate.html)

Before you can generate a key, you must start CloudHSM CLI and log in as a crypto user (CU).

- [Generate symmetric keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm-cli-generate-symmetric-keys.html): Use the commands listed in to generate symmetric keys for AWS CloudHSM.
- [Generate asymmetric keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm-cli-generate-asymmetric-keys.html): Use the commands listed in to generate asymmetric key pairs for AWS CloudHSM clusters.
- [Related topics](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm-cli-generate-keys-seealso.html): See the following sections for additional information about keys in AWS CloudHSM.
- [Delete keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-cloudhsm-cli-delete.html): Use the example in this topic to delete a key with CloudHSM CLI.
- [Share and unshare keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-cloudhsm-cli-share.html): Use the commands in this topic to share and unshare keys in CloudHSM CLI.
- [Filter by keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-cloudhsm-cli-filtering.html): Use the key commands in this topic to utilize the standardized key filtration mechanisms for CloudHSM CLI.
- [Mark a key as trusted](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-cloudhsm-cli-trusted.html): The content in this section provides instructions on using CloudHSM CLI to mark a key as trusted.

### [Manage quorum authentication (M of N)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key-quorum-auth-chsm-cli.html)

Enable and enforce quorum authentication (also known as M of N access control) on the HSM in your AWS CloudHSM cluster.

- [Quorum authentication process](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key-quorum-auth-chsm-cli-overview.html): The following steps summarize the quorum authentication processes for CloudHSM CLI.
- [Supported services and types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key-quorum-auth-chsm-cli-service-names.html): Admin Services: Quorum authentication is used for admin privileged services like creating users, deleting users, changing user passwords, setting quorum values, and deactivating quorum and MFA capabilities.
- [First time setup](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key-quorum-auth-chsm-cli-first-time.html): Set up crypto-users to use quorum authentication for hardware security module (HSM) key management/usage operations on the HSM in your AWS CloudHSM cluster.
- [Key management and usage with quorum (M of N)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key-quorum-auth-chsm-cli-crypto-user.html): Use quorum authentication for HSM key management operations that crypto-users perform on the HSM in your AWS CloudHSM cluster.

### [Key management with KMU](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-kmu-cmu.html)

If using the latest SDK version series, use CloudHSM CLI to manage the keys in your AWS CloudHSM cluster.

### [Generate keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate-keys.html)

To generate keys on the hardware security module (HSM), use the command in AWS CloudHSM key_mgmt_util (KMU) that corresponds to the type of key that you want to generate.

- [Generate symmetric keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate-symmetric-keys.html): Use the genSymKey command in AWS CloudHSM key_mgmt_util (KMU) to generate AES and other types of symmetric keys for AWS CloudHSM.
- [Generate RSA key pairs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate-rsa-key-pairs.html): To generate an RSA key pair for AWS CloudHSM, use the genRSAKeyPair command in AWS CloudHSM key_mgmt_util.
- [Generate ECC (elliptic curve cryptography) key pairs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate-ecc-key-pairs.html): To generate an ECC key pair for AWS CloudHSM, use the genECCKeyPair command in AWS CloudHSM key_mgmt_util.

### [Import keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/import-keys.html)

To import secret keysâthat is, symmetric keys and asymmetric private keysâinto the hardware security module (HSM) using the AWS CloudHSM key_mgmt_util, you must first create a wrapping key on the HSM.

- [Import secret keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/import-secret-keys.html): Complete the following steps to import a secret key into AWS CloudHSM using the key_mgmt_util (KMU).
- [Import public keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/import-public-keys.html): Use the importPubKey command in the AWS CloudHSM key_mgmt_util (KMU) to import a public key.

### [Export keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/export-keys.html)

To export AWS CloudHSM secret keysâthat is, symmetric keys and asymmetric private keysâfrom the hardware security module (HSM) using the AWS CloudHSM key_mgmt_util (KMU), you must first create a wrapping key.

- [Export secret keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/export-secret-keys.html): Complete the following steps to export a secret key from AWS CloudHSM using the key_mgmt_util (KMU).
- [Export public keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/export-public-keys.html): Use the exportPubKey command in the AWS CloudHSM key_mgmt_util (KMU) to export a public key.
- [Delete keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete-keys.html): Use the deleteKey command to delete a key, as in the following example.
- [Share and unshare keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/share-keys.html): In AWS CloudHSM, the CU who creates the key owns it.
- [Mark a key as trusted](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_using_trusted_keys_control_key_wrap.html): The content in this section provides instructions on using the CMU to mark a key as trusted.


## [Cluster backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-backups.html)

- [Working with backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/backups-using.html): When you add a hardware security module (HSM) to a cluster in AWS CloudHSM that previously contained one or more active HSMs, the service restores the latest backup onto the new HSM.
- [Delete backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete-restore-backup.html): Delete cluster backups.
- [Restore backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/restore-backup.html): Restore cluster backups.
- [Configure backup retention](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-backup-retention.html): Configure how long AWS CloudHSM retains backups for the cluster.
- [Copying backups across Regions](https://docs.aws.amazon.com/cloudhsm/latest/userguide/copy-backup-to-region.html): Copy an AWS CloudHSM cluster backup into a different region.
- [Working with shared backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html): Working with shared backups.


## [Tag resources](https://docs.aws.amazon.com/cloudhsm/latest/userguide/tag-resources.html)

- [Add or update tags](https://docs.aws.amazon.com/cloudhsm/latest/userguide/add-update-tags.html): You can add or update tags from the AWS CloudHSM console, the AWS Command Line Interface (AWS CLI), or the AWS CloudHSM API.
- [List tags](https://docs.aws.amazon.com/cloudhsm/latest/userguide/list-tags.html): You can list tags for a cluster from the AWS CloudHSM console, the AWS CLI, or the AWS CloudHSM API.
- [Remove tags](https://docs.aws.amazon.com/cloudhsm/latest/userguide/remove-tags.html): You can remove tags from an AWS CloudHSM cluster by using the AWS CloudHSM console, the AWS CLI, or the AWS CloudHSM API.


## [Command line tools](https://docs.aws.amazon.com/cloudhsm/latest/userguide/command-line-tools.html)

### [Configure tool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool.html)

Use the configure command line tool to update the hardware security module (HSM) data used by key management utility (KMU) and CloudHSM Management Utility (CMU).

### [Client SDK 5 configure tool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sdk-5.html)

Use the AWS CloudHSM Client SDK 5 configure tool to update client-side configuration files.

- [Syntax](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-syntax5.html): The following table illustrates the syntax for AWS CloudHSM configuration files for Client SDK 5.
- [Parameters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-params5.html): The following is a list of parameters to configure AWS CloudHSM Client SDK 5.
- [Examples](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-examples5.html): These examples show how to use the configure tool for AWS CloudHSM Client SDK 5.
- [Bootstrap OpenSSL Provider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-openssl-provider.html): Use the configure-openssl-provider tool to bootstrap your OpenSSL Provider installation and connect it to your AWS CloudHSM cluster.
- [Advanced configurations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sdk5-advanced-configs.html): The Client SDK 5 configure tool includes advanced configurations that are not part of the general features most customers utilize.
- [Related topics](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-seealso5.html): See the following related topics to learn more about the AWS CloudHSM Client SDK 5.

### [Client SDK 3 configure tool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sdk-3.html)

Use the AWS CloudHSM Client SDK 3 configure tool to bootstrap the client daemon and configure CloudHSM Management Utility (CMU).

- [Syntax](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-syntax.html): The following table illustrates the syntax for AWS CloudHSM configuration files for Client SDK 3.
- [Parameters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-params.html): The following is a list of parameters to configure AWS CloudHSM Client SDK 3.
- [Examples](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-examples.html): These examples show how to use the configure tool for AWS CloudHSM Client SDK 3.
- [Related topics](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-seealso.html): See the following related topics to learn more about the AWS CloudHSM Client SDK 3.

### [CloudHSM CLI](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli.html)

Use the CloudHSM CLI to manage users on the HSMs in your AWS CloudHSM cluster.

- [Supported platforms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm-cli-support.html): This topic describes the Linux and Windows platforms that the AWS CloudHSM CLI supports.

### [Getting started](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-getting-started.html)

Learn how to use CloudHSM CLI to manage HSM users.

- [Install the CloudHSM CLI](https://docs.aws.amazon.com/cloudhsm/latest/userguide/w2aac23c15c13b7.html): Use the following commands to download and install the CloudHSM CLI for AWS CloudHSM.
- [Use the CloudHSM CLI](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-getting-started-use.html): Use the following commands to start and use the CloudHSM CLI.
- [Command modes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-modes.html): There are two ways to run commands with CloudHSM CLI: single command mode and interactive mode.

### [Key attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-attributes.html)

Learn how to use CloudHSM CLI to set key attributes.

- [Supported attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-attributes-table.html): As a best practice, only set values for attributes you wish to make restrictive.
- [Check value](https://docs.aws.amazon.com/cloudhsm/latest/userguide/chsm-cli-key-attribute-details.html): The check value in CloudHSM CLI is a 3-byte hash or checksum of a key that is generated when the HSM imports or generates a key.
- [Related topics](https://docs.aws.amazon.com/cloudhsm/latest/userguide/chsm_cli-key-attributes-seealso.html): See the following topics for more information about CloudHSM CLI.

### [Advanced configurations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-configs.html)

Learn about the advanced configurations in AWS CloudHSM Command Line Interface (CLI).

### [Multiple clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-configs-multi-cluster.html)

With Client SDK 5, you can configure CloudHSM CLI to allow connections to multiple CloudHSM clusters from a single CLI instance.

- [Prerequisites](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-prereqs.html): Before configuring your cluster in AWS CloudHSM to connect to multiple clusters, you must meet the following prerequisites:
- [Configure multi-cluster functionality](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-config-run.html): To configure your CloudHSM CLI for multi-cluster functionality, follow these steps:
- [Add a cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-add-cluster.html): When connecting to multiple clusters, use the configure-cli add-cluster command to add a cluster to your configuration.
- [Remove a cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-remove-cluster.html): When connecting to multiple clusters with CloudHSM CLI, use the configure-cli remove-cluster command to remove a cluster from your configuration.
- [Interact with clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-usage.html): Learn about how to interact with multiple clusters with CloudHSM CLI,

### [Reference](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-reference.html)

Learn about the commands in the AWS CloudHSM Command Line Interface (CLI).

### [cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster.html)

cluster is a parent category for a group of commands that, when combined with the parent category, create a command specific to users.

- [activate](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-activate.html): Use the cluster activate command in CloudHSM CLI to activate your cluster.
- [hsm-info](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-hsm-info.html): Use the cluster hsm-info command in CloudHSM CLI to list the HSMs in your cluster.

### [mtls](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-mtls.html)

cluster mtls is a parent category for a group of commands that, when combined with the parent category, create a command specific to clusters.

- [deregister-trust-anchor](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-mtls-deregister-trust-anchor.html): Use the cluster mtls deregister-trust-anchor command in CloudHSM CLI to deregister a trust anchor for mutual TLS between client and AWS CloudHSM.
- [get-enforcement](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-mtls-get-enforcement.html): Use the cluster mtls get-enforcement command in CloudHSM CLI to get the enforcement level of the usage of mutual TLS between client and AWS CloudHSM.
- [list-trust-anchors](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-mtls-list-trust-anchors.html): Use the cluster mtls list-trust-anchors command in CloudHSM CLI to list all the registered trust anchors for mutual TLS between client and AWS CloudHSM.
- [register-trust-anchor](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-mtls-register-trust-anchor.html): Use the cluster mtls register-trust-anchor command in CloudHSM CLI to register a trust anchor for mutual TLS between client and AWS CloudHSM.
- [set-enforcement](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-mtls-set-enforcement.html): Use the cluster mtls set-enforcement command in CloudHSM CLI to set the enforcement level of the usage of mutual TLS between client and AWS CloudHSM.

### [crypto](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto.html)

crypto is a parent category for a group of commands that, when combined with the parent category, create a command specific to cryptographic operations.

### [sign](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-sign.html)

crypto sign is a parent category for a group of commands that, when combined with the parent category, create a command specific to cryptographic operations.

- [ecdsa](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-sign-ecdsa.html): The crypto sign ecdsa command generates a signature using an EC private key and the ECDSA signing mechanism.
- [ed25519ph](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-sign-ed25519ph.html): The crypto sign ed25519ph command generates a signature using an Ed25519 private key and the HashEdDSA signing mechanism.
- [rsa-pkcs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-sign-rsa-pkcs.html): The crypto sign rsa-pkcs command generates a signature using an RSA private key and the RSA-PKCS signing mechanism.
- [rsa-pkcs-pss](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-sign-rsa-pkcs-pss.html): The crypto sign rsa-pkcs-pss command generates a signature using an RSA private key and the RSA-PKCS-PSS signing mechanism.

### [verify](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-verify.html)

crypto verify is a parent category for a group of commands that, when combined with the parent category, confirms whether a file has been signed by a given key.

- [ecdsa](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-verify-ecdsa.html): Use the crypto verify ecdsa command to complete crypto verification commands.
- [ed25519ph](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-verify-ed25519ph.html): Use the crypto verify ed25519ph command to complete crypto verification commands.
- [rsa-pkcs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-verify-rsa-pkcs.html): Use the crypto verify rsa-pkcs command to verify that a file is signed by the RSA-PKCS signing mechanism.
- [rsa-pkcs-pss](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-verify-rsa-pkcs-pss.html): The crypto sign rsa-pkcs-pss command is used to complete the following operations.

### [key](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key.html)

key is a parent category for a group of commands that, when combined with the parent category, create a command specific to keys.

- [delete](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-delete.html): Use the key delete command in CloudHSM CLI to delete a key from an AWS CloudHSM cluster.
- [generate-file](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-generate-file.html): Use the key generate-file to generate a key file from a key in the AWS CloudHSM cluster

### [generate-asymmetric-pair](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-generate-asymmetric-pair.html)

key generate-asymmetric-pair is a parent category for a group of commands that, when combined with the parent category, create a command that generates asymmetric key pairs.

- [ec](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-generate-asymmetric-pair-ec.html): Use the key generate-asymmetric-pair ec command in CloudHSM CLI to generate an asymmetric Elliptic-curve (EC) key pair in your AWS CloudHSM cluster.
- [rsa](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-generate-asymmetric-pair-rsa.html): Use the key asymmetric-pair rsa command in CloudHSM CLI to generate an asymmetric RSA key pair in your AWS CloudHSM cluster.

### [generate-symmetric](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-generate-symmetric.html)

key generate-symmetric is a parent category for a group of commands that, when combined with the parent category, create a command that generates symmetric key.

- [aes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-generate-symmetric-aes.html): Use the key generate-symmetric aes command to generate a symmetric AES key in your AWS CloudHSM cluster.
- [generic-secret](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-generate-symmetric-generic-secret.html): Use the key generate-asymmetric-pair command to generate a symmetric Generic Secret key in your AWS CloudHSM cluster.
- [import pem](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-import-pem.html): The key import pem command in AWS CloudHSM imports a PEM format key into an HSM.
- [list](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-list.html): Use the key list command to finds all keys for the current user present in your AWS CloudHSM cluster.
- [replicate](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-replicate.html): Use the key replicate command to replicate a key across cloned AWS CloudHSM clusters.
- [set-attribute](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-set-attribute.html): Use the key set-attribute command to set the attributes of keys in your AWS CloudHSM cluster.
- [share](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-share.html): Use the key share command to share a key with other CUs in your AWS CloudHSM cluster.
- [unshare](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unshare.html): Use the key unshare command to unshare a key with other CUs in your AWS CloudHSM cluster.

### [unwrap](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap.html)

w

- [aes-gcm](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-aes-gcm.html): The key unwrap aes-gcm command unwraps a payload key into the cluster using the AES wrapping key and the AES-GCM unwrapping mechanism.
- [aes-no-pad](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-aes-no-pad.html): The key unwrap aes-no-pad command unwraps a payload key into the cluster using the AES wrapping key and the AES-NO-PAD unwrapping mechanism.
- [aes-pkcs5-pad](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-aes-pkcs5-pad.html): The key unwrap aes-pkcs5-pad command unwraps a payload key using the AES wrapping key and the AES-PKCS5-PAD unwrapping mechanism.
- [aes-zero-pad](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-aes-zero-pad.html): The key unwrap aes-zero-pad command unwraps a payload key into the cluster using the AES wrapping key and the AES-ZERO-PAD unwrapping mechanism.
- [cloudhsm-aes-gcm](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-cloudhsm-aes-gcm.html): The key unwrap cloudhsm-aes-gcm command unwraps a payload key into the cluster using the AES wrapping key and the CLOUDHSM-AES-GCM unwrapping mechanism.
- [rsa-aes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-rsa-aes.html): The key unwrap rsa-aes command wraps a payload key using an RSA public key on the HSM and the RSA-AES wrapping mechanism.
- [rsa-oaep](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-rsa-oaep.html): The key unwrap rsa-oaep command unwraps a payload key using the RSA private key and the RSA-OAEP unwrapping mechanism.
- [rsa-pkcs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap-rsa-pkcs.html): The key unwrap rsa-pkcs command unwraps a payload key using the RSA private key and the RSA-PKCS unwrapping mechanism.

### [wrap](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap.html)

The key wrap command in CloudHSM CLI exports an encrypted copy of a symmetric or private key from the HSM to a file.

- [aes-gcm](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-aes-gcm.html): The key wrap aes-gcm command wraps a payload key using an AES key on the HSM and the AES-GCM wrapping mechanism.
- [aes-no-pad](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-aes-no-pad.html): The key wrap aes-no-pad command wraps a payload key using an AES key on the HSM and the AES-NO-PAD wrapping mechanism.
- [aes-pkcs5-pad](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-aes-pkcs5-pad.html): The key wrap aes-pkcs5-pad command wraps a payload key using an AES key on the HSM and the AES-PKCS5-PAD wrapping mechanism.
- [aes-zero-pad](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-aes-zero-pad.html): The key wrap aes-zero-pad command wraps a payload key using an AES key on the HSM and the AES-ZERO-PAD wrapping mechanism.
- [cloudhsm-aes-gcm](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-cloudhsm-aes-gcm.html): The key wrap cloudhsm-aes-gcm command wraps a payload key using an AES key on the HSM and the CLOUDHSM-AES-GCM wrapping mechanism.
- [rsa-aes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-rsa-aes.html): The key wrap rsa-aes command wraps a payload key using an RSA public key on the HSM and the RSA-AES wrapping mechanism.
- [rsa-oaep](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-rsa-oaep.html): The key wrap rsa-oaep command wraps a payload key using an RSA public key on the HSM and the RSA-OAEP wrapping mechanism.
- [rsa-pkcs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-wrap-rsa-pkcs.html): The key wrap rsa-pkcs command wraps a payload key using an RSA public key on the HSM and the RSA-PKCS wrapping mechanism.

### [login](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-login.html)

Use the login command in AWS CloudHSM CloudHSM CLI to log in and out of each HSM in a cluster.

- [mfa-token-sign](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-login-mfa-token-sign.html): Use the login mfa-token-sign command in AWS CloudHSM CloudHSM CLI log in using multi-factor authentication.
- [logout](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-logout.html): Use the logout command in AWS CloudHSM CloudHSM CLI to log out of each HSM in a cluster.

### [user](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user.html)

user is a parent category for a group of commands that, when combined with the parent category, create a command specific to users.

### [change-mfa](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-change-mfa.html)

In the CloudHSM CLI, user change-mfa is a parent category for a group of commands that, when combined with the parent category, create a command specific to changing multi-factor authentication (MFA) for users.

- [token-sign](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-change-mfa-token-sign.html): Use the user change-mfa token-sign command in CloudHSM CLI to update a user accountâs multi-factor authentication (MFA) setup.
- [change-password](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-change-password.html): Use the user change-password command in CloudHSM CLI to change the password of an existing user in your AWS CloudHSM cluster.

### [change-quorum](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-chqm.html)

user change-quorum is a parent category for a group of commands that, when combined with the parent category, create a command specific to changing quorum for users.

### [token-sign](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-chqm-token.html)

user change-quorum token-sign is a parent category for commands that, when combined with this parent category, create a command specific to token-sign quorum operations.

- [register](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-chqm-token-reg.html): Use the user change-quorum token-sign register command in CloudHSM CLI to register the token-sign quorum strategy for an admin user.
- [create](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-create.html): Use the user create command in CloudHSM CLI to create users in your AWS CloudHSM cluster.
- [delete](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-delete.html): Use the user delete command in CloudHSM CLI to delete a user from an HSM.
- [list](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-list.html): Use the user list command in CloudHSM CLI to get the users in the HSM, along with their user type and other attributes.
- [replicate](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-replicate.html): Use the user replicate command to replicate a user across cloned AWS CloudHSM clusters.

### [quorum](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-qm.html)

quorum is a parent category for a group of commands that, when combined with quorum, creates a command specific to quorum authentication or M of N operations.

### [token-sign](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-qm-token.html)

quorum token-sign is a parent category for a group of commands that, when combined with quorum token-sign, create a command specific to quorum authentication or M of N operations.

- [delete](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-qm-token-del.html): Use the quorum token-sign delete command in CloudHSM CLI to delete one or more tokens for a quorum authorized service.
- [generate](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-qm-token-gen.html): Use the quorum token-sign generate command in CloudHSM CLI to generate a token for a quorum authorized service.
- [list](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-qm-token-list.html): Use the quorum token-sign list command in CloudHSM CLI to list all token-sign quorum tokens present in your AWS CloudHSM cluster.
- [list-quorum-values](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-qm-token-list-qm.html): Use the quorum token-sign list-quorum-values command in CloudHSM CLI to lists the quorum values set in your AWS CloudHSM cluster.
- [set-quorum-value](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-qm-token-set-qm.html): Use the quorum token-sign set-quorum-value command in CloudHSM CLI to set a new quorum value for a quorum authorized service.

### [AWS CloudHSM Management Utility](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util.html)

Use the cloudhsm_mgmt_util command line tool to manage users on the HSMs in your AWS CloudHSM cluster.

- [Supported platforms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cmu-support.html): This topic describes the Linux and Windows platforms that the AWS CloudHSM Management Utility (CMU) supports.
- [Getting started](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-getting-started.html): Learn how to use CloudHSM Management Utility (CMU) to manage HSM users.
- [Install the client (Linux)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cmu-install-and-configure-client-linux.html): Install the Linux AWS CloudHSM client and command tools on your Amazon EC2 instance so you can interact with the HSMs in your cluster.
- [Install the client (Windows)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cmu-install-and-configure-client-win.html): Install the AWS CloudHSM client software for Windows on your Amazon EC2 instance so you can interact with the HSMs in your cluster.

### [Reference](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-reference.html)

Learn about the commands in the AWS CloudHSM cloudhsm_mgmt_util command line tool.

- [changePswd](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-changePswd.html): Use the changePswd command in cloudhsm_mgmt_util to change your password or the password of another user.
- [createUser](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-createUser.html): Use the createUser command in cloudhsm_mgmt_util to create users on the HSM.
- [deleteUser](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-deleteUser.html): Use the deleteUser command in cloudhsm_mgmt_util to delete a user from an HSM.
- [findAllKeys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-findAllKeys.html): Use the findAllKeys command in cloudhsm_mgmt_util to get keys for a user or a hash of the user info on each HSM.
- [getAttribute](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-getAttribute.html): Use the getAttribute command in cloudhsm_mgmt_util to write the attribute values for a key to a file.
- [getHSMInfo](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-getHSMInfo.html): Use the getHSMInfo command in cloudhsm_mgmt_util gets information about the hardware on which each HSM runs.
- [getKeyInfo](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-getKeyInfo.html): Use the getKeyInfo command in cloudhsm_mgmt_util to get the HSM user IDs of users who can use the key.
- [info](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-info.html): Use the info command in cloudhsm_mgmt_util gets information about each HSM in the cluster, including the logged in user.
- [listAttributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-listAttributes.html): Use the listAttributes command in AWS CloudHSM cloudhsm_mgmt_util to list the attributes of a key and the constants that represent them.
- [listUsers](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-listUsers.html): Use the listUsers command in cloudhsm_mgmt_util to get the users in the HSM, along with their user type and other attributes.
- [loginHSM and logoutHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-loginLogout.html): Use the loginHSM and logoutHSM commands in AWS CloudHSM cloudhsm_mgmt_util to log in and out of each HSM in a cluster.
- [registerQuorumPubKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-registerQuorumPubKey.html): Use the registerQuorumPubKey command in cloudhsm_mgmt_util to associates hardware security module (HSM) users with asymmetric RSA-2048 key pairs.
- [server](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-server.html): Use the server command in cloudhsm_mgmt_util to enter server mode and execute commands on a particular HSM's server.
- [setAttributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-setAttribute.html): Use the setAttribute command in cloudhsm_mgmt_util to change the value of the label, encrypt, decrypt, wrap, and unwrap attributes of a key in the HSMs.
- [quit](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-quit.html): Use the quit command in cloudhsm_mgmt_util to exit the cloudhsm_mgmt_util.
- [shareKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-shareKey.html): Use the shareKey command in cloudhsm_mgmt_util to share and unshare an existing key.
- [syncKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-syncKey.html): Use the syncKey command in AWS CloudHSM cloudhsm_mgmt_util to synchronize keys across HSM instances within a cluster or across cloned clusters.
- [syncUser](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-syncUser.html): Use the syncUser command in AWS CloudHSM cloudhsm_mgmt_util to synchronize users across HSM instances within a cluster or across cloned clusters.

### [Key Management Utility](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util.html)

Use the key management utility (KMU) command line tool to manage keys on the hardware security modules (HSM) in your AWS CloudHSM cluster.

### [Getting started](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-getting-started.html)

Set up and start the key_mgmt_util command line tool that is included in AWS CloudHSM.

- [Set up](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-setup.html): Complete the following setup before you use AWS CloudHSM key_mgmt_util (KMU).
- [Log in to the HSMs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-log-in.html): Use the loginHSM command in key_mgmt_util (KMU) to log in to the hardware security modules (HSM) in an AWS CloudHSM cluster.
- [Log out from the HSMs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-log-out.html): Use the logoutHSM command in key_mgmt_util (KMU) to log out from the hardware security modules (HSM) in an AWS CloudHSM cluster.
- [Stop key_mgmt_util](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-stop.html): Use the exit command to stop the AWS CloudHSM key_mgmt_util.
- [Install the client (Linux)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/kmu-install-and-configure-client-linux.html): Install the Linux AWS CloudHSM client and command tools on your Amazon EC2 instance so you can interact with the HSMs in your cluster.
- [Install the client (Windows)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/kmu-install-and-configure-client-win.html): Install the AWS CloudHSM client software for Windows on your Amazon EC2 instance so you can interact with the HSMs in your cluster.

### [Reference](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-reference.html)

Learn about the commands in the AWS CloudHSM key_mgmt_util command line tool.

- [aesWrapUnwrap](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-aesWrapUnwrap.html): Use the aesWrapUnwrap command in AWS CloudHSM key_mgmt_util to encrypt or decrypt a file on disk.
- [deleteKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-deleteKey.html): Use the deleteKey command in AWS CloudHSM key_mgmt_util to delete a key from the HSM.
- [Error2String](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-Error2String.html): Use the Error2String command in AWS CloudHSM key_mgmt_util to return the error that corresponds to a hexadecimal error code.
- [exit](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-exit.html): Use the exit command in AWS CloudHSM key_mgmt_util to exit key_mgmt_util.
- [exportPrivateKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-exportPrivateKey.html): Use the exportPrivateKey command in AWS CloudHSM key_mgmt_util to export an asymmetric private key out of an HSM.
- [exportPubKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-exportPubKey.html): Use the exportPubKey command in AWS CloudHSM key_mgmt_util to export an asymmetric private key out of an HSM.
- [exSymKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-exSymKey.html): Use the exSymKey command in AWS CloudHSM key_mgmt_util to export a plaintext copy of a symmetric key from the HSM.
- [extractMaskedObject](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-extractMaskedObject.html): Use the extractMaskedObject command in AWS CloudHSM key_mgmt_util to extract a key as a masked object from an HSM.
- [findKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-findKey.html): Use the findKey command in AWS CloudHSM key_mgmt_util to search for keys by using the values of the key attributes.
- [findSingleKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-findSingleKey.html): Use the findSingleKey command in AWS CloudHSM key_mgmt_util to verify that a key exists on all HSMs in the cluster.
- [genDSAKeyPair](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-genDSAKeyPair.html): Use the genDSAKeyPair command in AWS CloudHSM key_mgmt_util to generate a Digital Signing Algorithm (DSA) key pair in your HSMs.
- [genECCKeyPair](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-genECCKeyPair.html): Use the genECCKeyPair command in the AWS CloudHSM key_mgmt_util tool to generate an Elliptic Curve Cryptography (ECC) key pair in your hardware security modules (HSM).
- [genRSAKeyPair](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-genRSAKeyPair.html): Use the genRSAKeyPair command in AWS CloudHSM key_mgmt_util to generate an RSA asymmetric key pair.
- [genSymKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-genSymKey.html): Use the genSymKey command in AWS CloudHSM key_mgmt_util to generate a symmetric key in your HSMs.
- [getAttribute](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-getAttribute.html): Use the getAttribute command in AWS CloudHSM key_mgmt_util to write the attribute values for a key to a file.
- [getCaviumPrivKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-getCaviumPrivKey.html): Use the getCaviumPrivKey command in AWS CloudHSM key_mgmt_util to export a private key from an HSM in fake PEM format.
- [getCert](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-getCert.html): Use the getCert command to get the partition certificates of a particular HSM in a cluster.
- [getKeyInfo](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-getKeyInfo.html): Use the getKeyInfo command in AWS CloudHSM key_mgmt_util to get the HSM user IDs of users who can use the key.
- [help](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-help.html): Use the help command in AWS CloudHSM key_mgmt_util to display information about all available key_mgmt_util commands.
- [importPrivateKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-importPrivateKey.html): Use the importPrivateKey command in AWS CloudHSM key_mgmt_util to import an asymmetric private key into an HSM.
- [importPubKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-importPubKey.html): Use the importPubKey command in AWS CloudHSM key_mgmt_util to import a PEM-encoded public key into an HSM.
- [imSymKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-imSymKey.html): Use the imSymKey command in the AWS CloudHSM key_mgmt_util tool to import a plaintext copy of a symmetric key from a file into the hardware security module (HSM).
- [insertMaskedObject](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-insertMaskedObject.html): Use the insertMaskedObject command in AWS CloudHSM key_mgmt_util to insert a masked object into an HSM.
- [IsValidKeyHandlefile](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-IsValidKeyHandlefile.html): The IsValidKeyHandlefile command in key_mgmt_util is used to find out whether a key file contains a real private key or a fake RSA PEM key.
- [listAttributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-listAttributes.html): Use the listAttributes command in AWS CloudHSM key_mgmt_util to list the attributes of a key and the constants that represent them.
- [listUsers](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-listUsers.html): Use the listUsers command in AWS CloudHSM key_mgmt_util to get the users in the HSM, along with their user type and other attributes.
- [loginHSM and logoutHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-loginHSM.html): Use the loginHSM and logoutHSM commands in AWS CloudHSM key_mgmt_util to log in and out of the HSMs in a cluster.
- [setAttribute](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-setAttribute.html): Use the setAttribute command in AWS CloudHSM key_mgmt_util to convert a session-only key to a persistent key that exists until you delete it.
- [sign](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-sign.html): Use the sign command in AWS CloudHSM key_mgmt_util to generate a signature for a file with a chosen private key.
- [unWrapKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-unwrapKey.html): Use the unWrapKey command in AWS CloudHSM key_mgmt_util to import a wrapped (encrypted) key from a file into the HSM.
- [verify](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-verify.html): Use the verify command in AWS CloudHSM key_mgmt_util to determine the key used to sign a file.
- [wrapKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-wrapKey.html): Use the wrapKey command in AWS CloudHSM key_mgmt_util to export an encrypted copy of a key from the HSM to a file.
- [Key attribute reference](https://docs.aws.amazon.com/cloudhsm/latest/userguide/key-attribute-table.html): Learn about the key attributes and the constants that represent them in AWS CloudHSM key_mgmt_util commands.


## [Client SDKs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/use-hsm.html)

- [Check your version](https://docs.aws.amazon.com/cloudhsm/latest/userguide/check-client_version.html): Use the following commands to verify the version of Client SDK that you're using with AWS CloudHSM.
- [Compare component support](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk3-compare.html): In addition to the command-line tools, Client SDK 3 contains components that enable off-loading cryptographic operations to the HSM from various platform or language-based applications.

### [Migrating to the latest SDK](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-sdk-migration.html)

In AWS CloudHSM, customer applications perform cryptographic operations using the AWS CloudHSM Client Software Development Kit (SDK).

- [Migrate PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-migrate-to-sdk-5.html): Use this topic to migrate your PKCS #11 library from Client SDK 3 to Client SDK 5.
- [Migrate OpenSSL Dynamic Engine](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-migrate-to-sdk-5.html): Use this topic to migrate your OpenSSL Dynamic Engine from Client SDK 3 to Client SDK 5.
- [Migrate Key Storage Provider (KSP)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-migrate-to-sdk-5.html): Learn how to migrate your Key Storage Provider (KSP) from Client SDK 3 to Client SDK 5
- [Migrate JCE provider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-migrate_to_sdk5.html): Use this topic to migrate your JCE provider from Client SDK 3 to Client SDK 5.

### [Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-sdk5.html)

AWS CloudHSM includes two major Client SDK versions:

- [Benefits of the latest SDK](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-sdk-5-benefits.html): Client SDK 5 offers customers many benefits Client SDK 3 does not.

### [Supported platforms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-supported-platforms.html)

Platform support for Client SDK 5 and Client SDK 3 from AWS CloudHSM, including command-line tools (KMU/CMU), the PKCS #11 library, Java Cryptographic Extension (JCE) provider, OpenSSL Dynamic Engine, and Cryptography API: Next Generation (CNG) and key storage providers (KSP) for Windows.

- [Linux support for Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk8-linux.html): AWS CloudHSM Client SDK 5 supports the following Linux operating systems and platforms.
- [Windows support for Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk8-windows.html): AWS CloudHSM Client SDK 5 supports the following versions of Windows Server.
- [Serverless support for Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk8-serverless.html): AWS CloudHSM Client SDK 5 supports the following AWS serverless services.
- [HSM compatibility for Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk5-hsm-types.html): The following table describes AWS CloudHSM Client SDK 5 compatibility for HSMs.

### [PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library.html)

AWS CloudHSM offers implementations of the PKCS #11 library to offload cryptographic operations to the hardware security modules (HSM) in your cluster.

- [Install the PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-install.html): Installation instructions for the PKCS #11 library included in Client SDK 5.
- [Authenticate to the PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-pin.html): When you use the PKCS #11 library, your application runs as a particular crypto user (CU) in your HSMs in AWS CloudHSM.
- [Key types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-key-types.html): The PKCS #11 library for AWS CloudHSM Client SDK 5supports the following key types.
- [Mechanisms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-mechanisms.html): The PKCS #11 library is compliant with version 2.40 of the PKCS #11 specification.
- [API operations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-apis.html): The PKCS #11 library supports the following PKCS #11 API operations for AWS CloudHSM Client SDK 5.

### [Key attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-attributes.html)

An AWS CloudHSM key object can be a public, private, or secret key.

- [Attributes tables](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-attributes-interpreting.html): The PKCS #11 library tables for AWS CloudHSM contain a list of attributes that differ by key types.
- [Modifying attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/modify-attr.html): Some PKCS #11 library attributes for of an AWS CloudHSM object can be modified after the object has been created, whereas some cannot.
- [Interpreting error codes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/attr-errors.html): Specifying in the template a PKCS #11 library attribute that is not supported by a specific key results in an error.
- [Code samples](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-samples.html): The code samples on GitHub show you how to accomplish basic tasks using the PKCS #11 library for AWS CloudHSM Client SDK 5.

### [Advanced configurations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-configs.html)

The AWS CloudHSM PKCS #11 provider includes advanced configurations, which are not part of the general configurations most customers utilize.

### [Multiple slots](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-configs-multi-slot.html)

A single slot in the Client SDK 5 PKCS #11 library represents a single connection to a cluster in AWS CloudHSM.

- [Configure for multi-slot functionality](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-multi-slot-config-run.html): To configure your PKCS #11 library for multi-slot functionality for AWS CloudHSM, follow these steps:
- [Add a cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-multi-slot-add-cluster.html): When connecting to multiple slots with PKCS #11 for AWS CloudHSM, use the configure-pkcs11 add-cluster command to add a cluster to your configuration.
- [Remove a cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-multi-slot-remove-cluster.html): When connecting to multiple slots with PKCS#11 for AWS CloudHSM, use the configure-pkcs11 remove-cluster command to remove a cluster from available PKCS #11 slots.
- [Retry commands](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-configs-retry.html): AWS CloudHSM Client SDK 5.8.0 and later have a built-in automatic retry strategy which will retry HSM-throttled operations from the client side.

### [Certificate storage](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage.html)

With AWS CloudHSM PKCS #11 library, you can store public key certificates on hsm2m.medium instances.

- [Enable certificate storage](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-configuration.html): You can enable certificate storage on hsm2m.medium clusters using the PKCS #11 library configuration tool.
- [Certificate storage API](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-api.html): The following PKCS #11 operations support the certificate object type (CKO_CERTIFICATE):
- [Certificate attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-attributes.html): The following table lists the supported certificate object attributes and their values:
- [Certificate storage audit logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-audit-logs.html): AWS CloudHSM writes audit logs for certificate storage operations that modify data to a separate Amazon CloudWatch Events log stream within your cluster's CloudWatch log group.

### [OpenSSL Dynamic Engine](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-library.html)

Use the OpenSSL Dynamic Engine as an OpenSSL interface to the hardware security modules (HSM) in your AWS CloudHSM cluster.

- [Install](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl5-install.html): Use the following sections to install the OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 5.
- [Key types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-key-types.html): The AWS CloudHSM OpenSSL Dynamic Engine supports the following key types.
- [Mechanisms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-mechanisms.html): Learn how to use AWS CloudHSM OpenSSL Dynamic Engine mechanisms.

### [Advanced configurations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-library-configs.html)

The AWS CloudHSM OpenSSL provider includes advanced configurations, which are not part of the general configurations most customers utilize.

- [Retry commands](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-library-configs-retry.html): AWS CloudHSM Client SDK 5.8.0 and later have a built-in automatic retry strategy which will retry HSM-throttled operations from the client side.

### [OpenSSL Provider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-library.html)

Use the OpenSSL Provider as a OpenSSL Provider interface to the hardware security modules (HSM) in your AWS CloudHSM cluster.

- [Install](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-install.html): Install the AWS CloudHSM OpenSSL Provider on supported Linux platforms
- [Key Types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-key-types.html): Key types supported by the AWS CloudHSM OpenSSL Provider SDK
- [Mechanisms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-mechanisms.html): Cryptographic mechanisms supported by the AWS CloudHSM OpenSSL Provider SDK

### [Advanced Configuration](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-advanced-config.html)

Advanced configuration options for the AWS CloudHSM OpenSSL Provider SDK

- [Retry commands](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-configs-retry.html): AWS CloudHSM Client SDK 5.8.0 and later have a built-in automatic retry strategy which will retry HSM-throttled operations from the client side.

### [Key storage provider (KSP)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library.html)

AWS CloudHSM offers implementations of the Key Storage Provider (KSP) to offload cryptographic operations to the hardware security modules (HSM) in your cluster.

- [Install](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-install.html): Installation instructions for the Key Storage Provider (KSP) included in Client SDK 5
- [Authentication](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-authentication.html): Learn how to set the credentials to the Key storage provider (KSP) for AWS CloudHSM Client SDK 5
- [Key types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library--key-types.html): The AWS CloudHSM Key Storage Provider (KSP) supports the following key types.

### [API operations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis.html)

The parameters in the KSP are defined by Microsoft KSP.

- [NCryptOpenStorageProvider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-open-provider.html): The NCryptOpenStorageProvider function loads and initializes the Key Storage Provider (KSP).
- [NCryptOpenKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-open-key.html): The NCryptOpenKey function opens a key that exists in the Key Storage Provider (KSP).
- [NCryptCreatePersistedKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-create-persisted-key.html): The NCryptCreatePersistedKey function creates a new key and stores it in the Key Storage Provider (KSP).
- [NCryptGetProperty](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-get-property.html): The NCryptGetProperty function retrieves property values for a key storage object.
- [NCryptSetProperty](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-set-property.html): The NCryptSetProperty function sets property values for a key storage object.
- [NCryptFinalizeKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-finalize-key.html): The NCryptFinalizeKey function completes a KSP key.
- [NCryptDeleteKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-delete-key.html): The NCryptDeleteKey function deletes a KSP key from the Key Storage Provider (KSP).
- [NCryptFreeObject](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-free-object.html): The NCryptFreeObject function releases provider or key handle from the Key Storage Provider (KSP).
- [NCryptFreeBuffer](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-free-buffer.html): The NCryptFreeBuffer function releases a block of memory that was allocated by the Key Storage Provider (KSP).
- [NCryptIsAlgSupported](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-is-alg-supported.html): NCryptIsAlgSupported function determines if Key Storage Provider (KSP) supports a specific cryptographic algorithm.
- [NCryptEnumAlgorithms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-enum-algorithms.html): The NCryptEnumAlgorithms function retrieves the names of algorithms that the Key Storage Provider (KSP) supports.
- [NCryptEnumKeys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-enum-keys.html): NCryptEnumKeys function lists the keys stored in the Key Storage Provider (KSP).
- [NCryptExportKey](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-export-key.html): The NCryptExportKey function exports a KSP key to a memory BLOB.
- [NCryptSignHash](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-sign-hash.html): The NCryptSignHash function creates a signature of a hash value.
- [NCryptVerifySignature](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-verify-signature.html): The NCryptVerifySignature function confirms whether a signature matches a specified hash.

### [Advanced configurations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-configs.html)

The AWS CloudHSM Key Storage Provider (KSP) includes advanced configurations, which are not part of the general configurations most customers utilize.

- [SDK3 compatibility mode](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-configs-sdk3-compatibility-mode.html): Key Storage Provider (KSP) implements different approaches for HSM key interaction:

### [JCE provider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library.html)

Introduces the AWS CloudHSM JCE provider.

- [Install](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library-install_5.html): Install JCE provider so that you can write Java applications that communicate with the HSMs in your cluster.
- [Key types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-keys_5.html): Introduces supported keys for AWS CloudHSM JCE provider.
- [Key management basics](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library-key-basics_5.html): The basics on key management in the JCE provider involve importing keys, exporting keys, loading keys by handle, or deleting keys.
- [Mechanisms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-supported_5.html): Learn which Java Cryptography Architecture (JCA) classes and interfaces are supported by AWS CloudHSM.
- [Key attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-attributes_5.html): AWS CloudHSM provides a new proprietary extension for the Java library that enables you to set more values for commonly used attributes.
- [Code samples](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-samples.html): Links to Java code samples that show you how to use the AWS CloudHSM software library for Java to perform basic tasks in AWS CloudHSM.
- [Javadocs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-javadocs_5.html): Links to Java code samples that show you how to use the AWS CloudHSM software library for Java to perform basic tasks in AWS CloudHSM.
- [AWS CloudHSM KeyStore](https://docs.aws.amazon.com/cloudhsm/latest/userguide/alternative-keystore_5.html): Use special-purpose software key store that supports associating certificates with keys.

### [Advanced configurations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-configs.html)

The AWS CloudHSM JCE provider includes advanced configurations, which are not part of the general configurations most customers utilize.

### [Multiple clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-configs-multi.html)

This configuration allows a single client instance to communicate to multiple clusters

- [Configure with a file (Default configuration)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-configs-default.html): The default way to configure the AWS CloudHSM CloudHsmProvider class is with a file.
- [Configure using code](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-configs-using-code.html): As of Client SDK version 5.8.0, you can also configure the AWS CloudHSM CloudHsmProvider class using Java code.
- [Connect to multiple clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-connecting-to-multiclusters.html): Each CloudHsmProvider represents a connection to your AWS CloudHSM Cluster.

### [Key extraction](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-configs-getencoded.html)

The AWS CloudHSM JCE provider includes advanced configurations, which are not part of the general configurations most customers utilize.

- [Extract private keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-encoded-take-out-private-keys.html): Use the following steps to allow AWS CloudHSM JCE provider to extract your private key secrets.
- [Retry commands](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-configs-retry.html): AWS CloudHSM Client SDK 5.8.0 and later have a built-in automatic retry strategy which will retry HSM-throttled operations from the client side.

### [Previous version](https://docs.aws.amazon.com/cloudhsm/latest/userguide/choose-client-sdk.html)

- [Upgrade Client SDK 3](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-upgrade.html): Upgrade to the latest AWS CloudHSM Client SDK 3 version to use the latest features.

### [Supported platforms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk3-support.html)

- [Linux support for Client SDK 3](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk3-linux.html): AWS CloudHSM Client SDK 3 supports the following Linux operating systems and platforms.
- [Windows support for Client SDK 3](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk3-windows.html): AWS CloudHSM Client SDK 3 supports the following versions of Windows Server.
- [HSM compatibility for Client SDK 3](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sdk3-hsm-types.html): The following table describes AWS CloudHSM Client SDK 3 compatibility for HSMs.

### [PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-library.html)

AWS CloudHSM offers implementations of the PKCS #11 library to offload cryptographic operations to the hardware security modules (HSM) in your cluster.

- [Install the PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/install-pkcs11-v3.html): Installation instructions for the PKCS #11 library for Client SDK 3.
- [Authenticate to the PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-pin.html): When you use the PKCS #11 library, your application runs as a particular crypto user (CU) in your HSMs in AWS CloudHSM.
- [Key types](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-key-types.html): The PKCS #11 library supports the following key types with AWS CloudHSM Client SDK 3.
- [Mechanisms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-mechanisms.html): The PKCS #11 library supports the following algorithms for AWS CloudHSM Client SDK 3:
- [API operations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-apis.html): The PKCS #11 library supports the following PKCS #11 API operations for AWS CloudHSM Client SDK 3.

### [Key attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-attributes.html)

A key object can be a public, private, or secret key.

- [Attributes table](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-attributes-interpreting.html): The PKCS #11 library table for AWS CloudHSM Client SDK 3 contains a list of attributes that differ by key types.
- [Modifying attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-modify-attr.html): Some attributes of an object can be modified after the object has been created, whereas some cannot.
- [Interpreting PKCS #11 library error codes for AWS CloudHSM Client SDK 3](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-attr-errors.html): Specifying in the template a PKCS #11 library attribute that is not supported by a specific key results in an error.
- [Code samples](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-samples.html): The code samples on GitHub show you how to accomplish basic tasks using the PKCS #11 library for AWS CloudHSM.

### [OpenSSL Dynamic Engine](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl3-install.html)

The AWS CloudHSM OpenSSL Dynamic Engine enables you to offload cryptographic operations to your CloudHSM cluster through the OpenSSL API.

- [Prerequisites](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl3-install-dyn3-prereqs.html): For information about platform support, see .
- [Install](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl3-install-openssl-library.html): The following steps describe how to install and configure the AWS CloudHSM dynamic engine for OpenSSL with Client SDK 3.
- [Use](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl3-use-library.html): To use the AWS CloudHSM dynamic engine for OpenSSL from an OpenSSL-integrated application, ensure that your application uses the OpenSSL dynamic engine named cloudhsm.

### [JCE provider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library_3.html)

The AWS CloudHSM JCE provider is a provider implementation built from the Java Cryptographic Extension (JCE) provider framework.

- [Install](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library-install.html): Install JCE provider so that you can write Java applications that communicate with the HSMs in your cluster.
- [Key management basics](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library-key-basics.html): The basics on key management in the JCE provider involve importing keys, exporting keys, loading keys by handle, or deleting keys.
- [Mechanisms](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-supported.html): Learn which Java Cryptography Architecture (JCA) classes and interfaces are supported by AWS CloudHSM.
- [Key attributes](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-attributes.html): AWS CloudHSM provides a new proprietary extension for the Java library that enables you to set more values for commonly used attributes.
- [Code samples](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-samples_3.html): Links to Java code samples that show you how to use the AWS CloudHSM software library for Java to perform basic tasks in AWS CloudHSM.
- [AWS CloudHSM KeyStore](https://docs.aws.amazon.com/cloudhsm/latest/userguide/alternative-keystore.html): Use special-purpose software key store that supports associating certificates with keys.

### [KSP and CNG providers](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-v3-library.html)

Introduces the CNG and KSP providers for Windows and how you can use them with AWS CloudHSM.

- [Verify provider installation](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-v3-library-install.html): Verify that the KSP and CNG providers were installed.
- [Prerequisites](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-prereq.html): Learn how to set the prerequisites for using the Windows Client
- [Associate a key with a certificate](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-associate-key-certificate.html): Learn how to associate a key on AWS CloudHSM with a certificate
- [Code sample](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-sample.html): Code sample that enumerates the registered cryptographic providers on your system to find the CNG provider installed with CloudHSM client for Windows.


## [Integrating third-party applications](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-party-applications.html)

### [SSL/TLS offload](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload.html)

Configure SSL/TLS offload for your web server with AWS CloudHSM.

- [How it works](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-overview.html): See an overview of how SSL/TLS offload with AWS CloudHSM works.
- [Offload on Linux with OpenSSL Engine](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-offload-linux-openssl.html): Follow these steps to use OpenSSL Dynamic Engine with AWS CloudHSM for SSL/TLS offload on Linux
- [Offload on Linux with OpenSSL Provider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-offload-linux-openssl-provider.html): Follow these steps to use OpenSSL Provider with AWS CloudHSM for SSL/TLS server identity offload on Linux using NGINX
- [Offload on Linux with JSSE](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-offload-linux-jsse.html): This topic provides step-by-step instructions for setting up SSL/TLS offload using Java Secure Socket Extension (JSSE) with the AWS CloudHSM JCE SDK.
- [Offload on Windows](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-windows.html): Follow this tutorial to use SSL/TLS offload with AWS CloudHSM on your Windows web server.
- [Add a load balancer (optional)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-offload-add-lb.html): Use Elastic Load Balancing to add a load balancer to your web servers that use SSL/TLS offload with AWS CloudHSM.

### [Windows Server CA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-ca-toplevel.html)

AWS CloudHSM offers support to configure Windows Server as a certificate authority (CA) through Client SDK 3 and Client SDK 5.

- [Client SDK 5 with Windows Server CA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/win-ca-overview-sdk5.html): Configure Windows Server as a certificate authority (CA) with Client SDK 5.
- [Client SDK 3 with Windows Server CA](https://docs.aws.amazon.com/cloudhsm/latest/userguide/win-ca-overview-sdk3.html): Configure Windows Server as a certificate authority (CA) with Client SDK 3.
- [Oracle database encryption](https://docs.aws.amazon.com/cloudhsm/latest/userguide/oracle-tde.html): Configure Oracle Transparent Data Encryption (TDE) with AWS CloudHSM.

### [Microsoft SignTool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-signtool-toplevel.html)

AWS CloudHSM offers support to use Microsoft Signtool to sign file through Client SDK 3 and Client SDK 5.

- [Client SDK 5 with Microsoft SignTool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/signtool-sdk5.html): Learn how to use Microsoft SignTool with Client SDK 5 to sign and verify executables and scripts.
- [Client SDK 3 with Microsoft SignTool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/signtool-sdk3.html): Learn how to use Microsoft SignTool with Client SDK 3 to sign and verify executables and scripts.

### [Java Keytool and Jarsigner](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third_java-sdk_integration.html)

AWS CloudHSM offers integration with the Java Keytool and Jarsigner utilities through Client SDK 3 and Client SDK 5.

### [Client SDK 5 with Java Keytool and Jarsigner](https://docs.aws.amazon.com/cloudhsm/latest/userguide/keystore-third-party-tools_5.html)

How to use Client SDK 5 to integrate with Java Keytool and Jarsigner.

- [Prerequisites](https://docs.aws.amazon.com/cloudhsm/latest/userguide/keystore-prerequisites_5.html): To use the AWS CloudHSM key store, you must first initialize and configure the AWS CloudHSM JCE SDK.

### [Use key store with keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/using_keystore_with_keytool_5.html)

Keytool is a popular command line utility for common key and certificate tasks.

- [Create new keys with keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create_key_keytool_5.html): You can use keytool to generate RSA, AES, and DESede type of key supported by the AWS CloudHSM JCE SDK.
- [Delete a key using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete_key_using_keytool_5.html): The AWS CloudHSM key store doesn't support deleting keys.
- [Generate a CSR using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate_csr_using_keytool_5.html): You receive the greatest flexibility in generating a certificate signing request (CSR) if you use the .
- [Use keytool to import certificates into key store](https://docs.aws.amazon.com/cloudhsm/latest/userguide/import_cert_using_keytool_5.html): To import a CA certificate in AWS CloudHSM, you must enable verification of a full certificate chain on a newly imported certificate.
- [Use keytool to delete certificates from key store](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete_cert_using_keytool_5.html): The following command shows an example of how to delete a AWS CloudHSM certificate from a Java keytool key store.
- [Import a working certificate into key store using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/import_working_cert_using_keytool_5.html): Once a certificate signing request (CSR) is signed, you can import it into the AWS CloudHSM key store and associate it with the appropriate key pair.
- [Export a certificate using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/export_cert_using_keytool_5.html): The following example generates a certificate in binary X.509 format.

### [Use key store with Jarsigner](https://docs.aws.amazon.com/cloudhsm/latest/userguide/using_keystore_jarsigner_5.html)

Jarsigner is a popular command line utility for signing JAR files using a key securely stored on a hardware security module (HSM).

- [Set up keys and certificates](https://docs.aws.amazon.com/cloudhsm/latest/userguide/jarsigner_set_up_certificates_5.html): Before you can sign AWS CloudHSM JAR files with Jarsigner, make sure you have set up or completed the following steps:
- [Sign a JAR file](https://docs.aws.amazon.com/cloudhsm/latest/userguide/jarsigner_sign_jar_using_hsm_jarsigner_5.html): Use the following command to sign a JAR file using AWS CloudHSM and Jarsigner:
- [Known issues](https://docs.aws.amazon.com/cloudhsm/latest/userguide/known-issues-keytool-jarsigner_5.html): The following list provides the current list of known issues for integrations with AWS CloudHSM and Java Keytool and Jarsigner using Client SDK 5.

### [Client SDK 3 with Java Keytool and Jarsigner](https://docs.aws.amazon.com/cloudhsm/latest/userguide/keystore-third-party-tools.html)

How to use Client SDK 3 to integrate with Java Keytool and Jarsigner.

- [Prerequisites](https://docs.aws.amazon.com/cloudhsm/latest/userguide/keystore-prerequisites.html): To use the AWS CloudHSM key store, you must first initialize and configure the AWS CloudHSM JCE SDK.

### [Use key store with keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/using_keystore_with_keytool.html)

Keytool is a popular command line utility for common key and certificate tasks on Linux systems.

- [Create new keys with keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create_key_keytool.html): You can use keytool to generate any type of key supported by the AWS CloudHSM JCE SDK.
- [Delete a key using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete_key_using_keytool.html): The AWS CloudHSM key store doesn't support deleting keys.
- [Generate a CSR using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate_csr_using_keytool.html): You receive the greatest flexibility in generating a certificate signing request (CSR) if you use the .
- [Use keytool to import certificates into key store](https://docs.aws.amazon.com/cloudhsm/latest/userguide/import_cert_using_keytool.html): To import a CA certificate into AWS CloudHSM, you must enable verification of a full certificate chain on a newly imported certificate.
- [Use keytool to delete certificates from key store](https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete_cert_using_keytool.html): The following command shows an example of how to delete an AWS CloudHSM certificate from a Java keytool key store.
- [Import a working certificate into key store using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/import_working_cert_using_keytool.html): Once a certificate signing request (CSR) is signed, you can import it into the AWS CloudHSM key store and associate it with the appropriate key pair.
- [Export a certificate using keytool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/export_cert_using_keytool.html): The following example generates a certificate in binary X.509 format.

### [Use key store with jarsigner](https://docs.aws.amazon.com/cloudhsm/latest/userguide/using_keystore_jarsigner.html)

Jarsigner is a popular command line utility for signing JAR files using a key securely stored on a hardware security module (HSM).

- [Set up keys and certificates](https://docs.aws.amazon.com/cloudhsm/latest/userguide/jarsigner_set_up_certificates.html): Before you can sign AWS CloudHSM JAR files with Jarsigner, make sure you have set up or completed the following steps:
- [Sign a JAR file](https://docs.aws.amazon.com/cloudhsm/latest/userguide/jarsigner_sign_jar_using_hsm_jarsigner.html): Use the following command to sign a JAR file using AWS CloudHSM and jarsigner:
- [Known issues](https://docs.aws.amazon.com/cloudhsm/latest/userguide/known-issues-keytool-jarsigner.html): The following list provides the current list of known issues for integrations with AWS CloudHSM and Java Keytool and Jarsigner using Client SDK 3.
- [Register pre-existing keys with key store](https://docs.aws.amazon.com/cloudhsm/latest/userguide/register-pre-existing-keys-with-keystore.html): For maximum security and flexibility in attributes and labeling, we recommend you generate your AWS CloudHSM signing keys using key_mgmt_util.
- [Microsoft Manifest Generation and Editing Tool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/third-magetool.html): AWS CloudHSM supports using the Microsoft Manifest Generation and Editing Tool (Mage.exe) to sign files in Client SDK 5.
- [Other third-party vendor integrations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/other-integrations.html): List of several third-party vendor integrations that support AWS CloudHSM as a root of trust.


## [Monitoring](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-logs.html)

- [Client SDK logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-client-logs.html): Retrieve and rotate the logs generated by the Client SDK.
- [AWS CloudTrail](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-api-logs-using-cloudtrail.html): Learn about logging AWS CloudHSM with AWS CloudTrail.

### [Audit logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-hsm-audit-logs-using-cloudwatch.html)

View and monitor your AWS CloudHSM Audit Logs in Amazon CloudWatch Logs.

- [How logging works](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-audit-logs-from-cloudwatch.html): Audit logging is automatically enabled in all AWS CloudHSM clusters.
- [Viewing logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understand-audit-logs.html): Amazon CloudWatch Logs organizes the audit logs into log groups and, within a log group, into log streams.
- [Interpreting logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/interpreting-audit-logs.html): The events in the HSM audit logs have standard fields.
- [Log reference](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm-audit-log-reference.html): AWS CloudHSM records HSM management commands in audit log events.
- [CloudWatch metrics](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-metrics-cw.html): Use CloudWatch to monitor your AWS CloudHSM cluster in real time.


## [Security](https://docs.aws.amazon.com/cloudhsm/latest/userguide/security.html)

- [Control API access with IAM policies](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ip-access.html): Control API access with IAM policies.

### [Data protection](https://docs.aws.amazon.com/cloudhsm/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS CloudHSM.

- [End-to-end encryption](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-end-to-end-encryption.html): Communication between the client instance and the HSM in your cluster is encrypted from end to end.
- [Cluster backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/data-protection-backup-security.html): When AWS CloudHSM makes a backup from the HSM, the HSM encrypts all of its data before sending it to AWS CloudHSM.

### [Identity and access management](https://docs.aws.amazon.com/cloudhsm/latest/userguide/identity-access-management.html)

Specify the actions that a user can perform with your AWS CloudHSM resources by using IAM permissions.

- [Service-linked roles](https://docs.aws.amazon.com/cloudhsm/latest/userguide/service-linked-roles.html): The IAM policy that you created previously to includes the iam:CreateServiceLinkedRole action.

### [Compliance validation](https://docs.aws.amazon.com/cloudhsm/latest/userguide/fips-validation.html)

For clusters in FIPS mode, AWS CloudHSM provides FIPS-approved HSMs that meet PCI-PIN, PCI-3DS, and SOC2 compliance requirements.

- [PCI-PIN FAQs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/compliance-pci-pin-faqs.html): PCI PIN provides security requirement and assessment standards for transmitting, processing, and managing personal identification number (PIN) data, information that is used for transactions at ATMs and point-of-sale (POS) terminals.
- [Deprecations](https://docs.aws.amazon.com/cloudhsm/latest/userguide/compliance-dep-notif.html): AWS CloudHSM may deprecate functionality in order to remain compliant with the requirements of FIPS 140, PCI-DSS, PCI-PIN, PCI-3DS and SOC2.
- [Resilience](https://docs.aws.amazon.com/cloudhsm/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS CloudHSM features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/cloudhsm/latest/userguide/infrastructure-security.html): Learn how AWS CloudHSM isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm-vpc-endpoint.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS CloudHSM without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Update management](https://docs.aws.amazon.com/cloudhsm/latest/userguide/update-management.html): AWS manages the firmware.


## [Troubleshooting](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting.html)

### [AWS CloudHSM known issues](https://docs.aws.amazon.com/cloudhsm/latest/userguide/KnownIssues.html)

Learn about the known issues in AWS CloudHSM

- [Known issues for all HSM instances](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-all.html): The following issues impact all AWS CloudHSM users regardless of whether they use the key_mgmt_util command line tool, the PKCS #11 SDK, the JCE SDK, or the OpenSSL SDK.
- [Known issues for hsm1.medium](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-hsm1-medium.html): The following issues impact all AWS CloudHSM hsm1.medium instances.
- [Known issues for hsm2m.medium](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-hsm2m-medium.html): The following issues impact all AWS CloudHSM hsm2m.medium instances.
- [Known issues for the PKCS #11 library](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-pkcs11-sdk.html): The following issues impact the PKCS #11 library for AWS CloudHSM.
- [Known issues for the JCE SDK](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-jce-sdk.html): The following issues impact the JCE SDK for AWS CloudHSM.
- [Known issues for the OpenSSL Dynamic Engine](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-openssl-sdk.html): These are the known issues for OpenSSL Dynamic Engine for AWS CloudHSM.
- [Known issues for the Key Storage Provider (KSP)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-ksp-sdk.html): These are the known issues for Key Storage Provider (KSP) for AWS CloudHSM.
- [Known issues for the OpenSSL Provider](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-openssl-provider-sdk.html): These are the known issues for OpenSSL Provider for AWS CloudHSM.
- [Known issues for Amazon EC2 instances running Amazon Linux 2](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-al2.html): The following issues impact AWS CloudHSM and Amazon EC2 instances that are running on Amazon Linux 2.
- [Known issues for integrating third-party applications](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-third-party.html): The following issues impact AWS CloudHSM when integrating with third-party applications.
- [Known issues for cluster modification](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-cluster-modification.html): The following issues impact customers attempting to use the modify-cluster API to change the HSM type of a cluster.
- [Known issues of operation failure using AWS CloudHSM client version 5.12.0 on hsm2.medium](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-hsm2-old-sdk.html): The following issues impact AWS CloudHSM when using AWS CloudHSM client version 5.12.0
- [Client SDK 3 key synchronization failures](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ts-client-sync-fail.html): In Client SDK 3, if client-side synchronization fails, AWS CloudHSM makes a best-effort response to clean up any unwanted keys that may have been created (and are now unwanted).
- [Client SDK 3 verify performance](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-verify-hsm-performance.html): Use the pkpspeed (Linux) or pkpspeed_blocking (Windows) tool to verify the performance of the HSMs in your AWS CloudHSM cluster.
- [Client SDK 5 user contains inconsistent values](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-sdk5-inconsistent-value.html): The user list command in AWS CloudHSM Client SDK 5 returns a list of all users, and user properties, in your cluster.
- [Client SDK 5 user replicate failures](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-sdk5-user-replicate-failures.html): The user replicate command in the CloudHSM CLI replicates a user between cloned AWS CloudHSM clusters.
- [Client SDK 5 key replicate failures](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-sdk5-key-replicate-failures.html): The key replicate command in the CloudHSM CLI replicates a key from a source AWS CloudHSM cluster to a destination AWS CloudHSM cluster.
- [AWS CloudHSM error seen during key availability check](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-key-availability-check.html): Problem: An AWS CloudHSM hardware security module (HSM) is returning the following error:
- [Extracting keys using JCE](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-getencoded.html): Use the following sections to troubleshoot issues extracting AWS CloudHSM keys using JCE.
- [HSM throttling](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-hsm-throttling.html): When your workload exceeds your AWS CloudHSM clusterâs hardware security module (HSM) capacity, you will receive error messages stating HSMs are busy or throttled.
- [Keep HSM users in sync](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-keep-hsm-users-in-sync.html): Edit the cloudhsm_mgmt_util configuration file before managing HSM users to keep the users in sync across HSMs in your AWS CloudHSM cluster.
- [Lost connection](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-lost-connection.html): Update the AWS CloudHSM client configuration file to restore a lost connection to the HSMs in your AWS CloudHSM cluster.
- [Missing AWS CloudHSM audit logs in CloudWatch](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-missing-audit-logs.html): Enable a service-linked role in order to receive AWS CloudHSM audit logs in CloudWatch
- [Non-compliant AES key wraps](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-aes-keys.html): Guidelines to help you determine and recover from a problem with AES keys wrapped with custom IVs using version 3.0.0 of PKCS #11 library.
- [Resolving AWS CloudHSM cluster creation failures](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-create-cluster.html): Use these procedures to fix cluster creation failures that are related to the AWS CloudHSM service-linked role.

### [Retrieving AWS CloudHSM client configuration logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshooting-log-collection-script.html)

Use tools to gather information for AWS Support for troubleshooting.

- [Client SDK 5 support tool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/support-tool-sdk5.html): The script for AWS CloudHSM Client SDK 5 extracts the following information:
- [Client SDK 3 support tool](https://docs.aws.amazon.com/cloudhsm/latest/userguide/support-tool-sdk3.html): The script for the AWS CloudHSM Client SDK 3 extracts the following information:


## [Downloads](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-history.html)

- [Latest release](https://docs.aws.amazon.com/cloudhsm/latest/userguide/latest-releases.html): Download the latest version of the AWS CloudHSM Client SDK.
- [Previous release](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-version-previous.html): Download previous versions of the AWS CloudHSM Client SDK.
- [Deprecated releases](https://docs.aws.amazon.com/cloudhsm/latest/userguide/deprecated.html): Download deprecated version of the AWS CloudHSM Client SDK.
- [End-of-life releases](https://docs.aws.amazon.com/cloudhsm/latest/userguide/end-of-life-release.html): Learn about end-of-life versions of the AWS CloudHSM Client SDK.
