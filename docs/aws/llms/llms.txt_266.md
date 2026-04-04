# Source: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/llms.txt

# AWS Database Encryption SDK Developer Guide

> Learn how to use the AWS Database Encryption SDK to encrypt and sign table items in your application.

- [Interacting with AWS KMS](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/using-kms.html)
- [Configuring the SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/configure.html)
- [DynamoDB Encryption Client rename](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/DDBEC-rename.html)
- [Reference](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/reference.html)
- [Document history](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/document-history.html)

## [What is the AWS Database Encryption SDK?](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html)

- [Concepts](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/concepts.html): Understand the concepts used in the AWS Database Encryption SDK.
- [How it works](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/how-it-works.html): Learn how the AWS Database Encryption SDK encrypts, signs, decrypts, and verifies your database records.
- [Supported algorithm suites](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/supported-algorithms.html): Choose a supported algorithm suite.


## [Key stores](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/keystores.html)

- [Implementing least privileged permissions](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/keystore-least-privilege.html): When using a key store and AWS KMS Hierarchical keyrings, we recommend that you follow the principle of least privilege by defining the following roles:
- [Create a key store](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/create-keystore.html): Learn how to create a key store to persist hierarchical data and reduce AWS KMS calls with your Hierarchical keyring.
- [Configure key store actions](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/keystore-actions.html): Key store actions determine what operations your users can perform and how their AWS KMS Hierarchical keyring uses the KMS keys allowlisted in your key store.
- [Create branch keys](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/create-branch-keys.html): Learn how to create new active branch keys in your key store.
- [Rotate your active branch key](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/rotate-branch-key.html): There can only be one active version for each branch key at a time.


## [Keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/keyrings.html)

- [AWS KMS keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-kms-keyring.html)
- [AWS KMS Hierarchical keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-hierarchical-keyring.html)
- [AWS KMS ECDH keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-kms-ecdh-keyring.html)
- [Raw AES keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-raw-aes-keyring.html)
- [Raw RSA keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-raw-rsa-keyring.html)
- [Raw ECDH keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-raw-ecdh-keyring.html)
- [Multi-keyrings](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-multi-keyring.html)


## [Searchable encryption](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/searchable-encryption.html)

- [Beacons](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/beacons.html)

### [Planning beacons](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/plan-searchable-encryption.html)

- [Choosing a beacon type](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/choosing-beacon-type.html)
- [Choosing a beacon length](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/choosing-beacon-length.html)
- [Choosing a beacon name](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/choosing-beacon-name.html)

### [Configuring beacons](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/configure-beacons.html)

- [Example configurations](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/beacon-config-examples.html)
- [Using beacons](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/using-beacons.html)
- [Searchable encryption for multitenant databases](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/searchable-encryption-multitenant.html): Learn how searchable encryption differs for multitenant databases.


## [Amazon DynamoDB](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/dynamodb-encryption-client.html)

- [Client-side and server-side encryption](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/client-server-side.html)
- [Which fields are encrypted and signed?](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/DDB-encrypted-and-signed.html)
- [Searchable encryption in DynamoDB](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-searchable-encryption.html): To configure your Amazon DynamoDB tables for searchable encryption, you must use the AWS KMS Hierarchical keyring to generate, encrypt, and decrypt the data keys used to protect your items.
- [Updating your data model](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-update-data-model.html): Learn how to update your cryptographic actions in the AWS Database Encryption SDK for DynamoDB.

### [Programming languages](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-programming-languages.html)

The AWS Database Encryption SDK for DynamoDB is available for the following programming languages.

### [Java](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java.html)

Download and install version 3.x of the Java client-side encryption library for DynamoDB.

- [Using the Java client](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-using.html): Learn about functions and helper classes in the Java client-side encryption library for DynamoDB.
- [Java examples](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-examples.html): Example code for learning how to use the Java client-side encryption library for DynamoDB.
- [Add version 3.x to an existing table](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-config-existing-table.html): Learn how to add version 3.x of the Java client-side encryption library for DynamoDB to an existing, populated DynamoDB table.
- [Migrate to version 3.x](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-migrate.html): Learn how to migrate from earlier versions of the Java client-side encryption library for DynamoDB to version 3.x.

### [.NET](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net.html)

Download and install version 3.x of the .NET client-side encryption library for DynamoDB.

- [Using the .NET client](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net-using.html): Learn how to use the .NET client-side encryption library for DynamoDB.
- [.NET examples](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net-examples.html): Example code for learning how to use the .NET client-side encryption library for DynamoDB.
- [Add version 3.x to an existing table](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net-config-existing-table.html): Learn how to add version 3.x of the .NET client-side encryption library for DynamoDB to an existing, populated DynamoDB table.

### [Rust](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-rust.html)

Download and install the Rust client-side encryption library for DynamoDB.

- [Using the Rust client](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-rust-using.html): Learn how to use the Rust client-side encryption library for DynamoDB.

### [Legacy](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/legacy-dynamodb-encryption-client.html)

Learn more about AWS Database Encryption SDK for DynamoDB version support.

- [How it works](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/DDBEC-legacy-how-it-works.html): Learn how legacy versions of the DynamoDB Encryption Client work.
- [Concepts](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/DDBEC-legacy-concepts.html): Understand the concepts used in the Amazon DynamoDB Encryption Client.

### [Cryptographic materials provider](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/crypto-materials-providers.html)

Learn about the Cryptographic Materials Providers in the DynamoDB Encryption Client and how to select one for your DynamoDB applications.

- [Direct KMS Provider](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/direct-kms-provider.html): Learn about the Direct KMS Provider in the DynamoDB Encryption Client and how to use it in your DynamoDB applications.
- [Wrapped Provider](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/wrapped-provider.html): Learn about the Wrapped Materials Provider in the DynamoDB Encryption Client and how to use it in your DynamoDB applications.
- [Most Recent Provider](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/most-recent-provider.html): Learn about the Most Recent Provider cryptographic materials provider in the DynamoDB Encryption Client and how to use it in your DynamoDB applications.
- [Static Provider](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/static-provider.html): Learn about the Static Materials Provider in the DynamoDB Encryption Client.

### [Programming languages](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/programming-languages.html)

Download and install the Amazon DynamoDB Encryption Client for your preferred programming language.

### [Java](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/java.html)

Download and install the Amazon DynamoDB Encryption Client for Java.

- [Using the DynamoDB Encryption Client for Java](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/java-using.html): Learn about functions and helper classes in the DynamoDB Encryption Client for Java.
- [Java examples](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/java-examples.html): Example code for learning how to use the DynamoDB Encryption Client for Java.

### [Python](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/python.html)

Download and install the DynamoDB Encryption Client for Python.

- [Using the DynamoDB Encryption Client for Python](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/python-using.html): Learn about functions and helper classes in the DynamoDB Encryption Client for Python.
- [Python examples](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/python-examples.html): Example code for learning how to use the DynamoDB Encryption Client for Python.
- [Changing your data model](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/data-model.html): Learn how to update your DynamoDB attribute actions
- [Troubleshooting](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/troubleshooting.html): Learn how to fix common problems in a Amazon DynamoDB Encryption Client implementation.
