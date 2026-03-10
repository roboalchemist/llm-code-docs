# Source: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/llms.txt

# AWS Encryption SDK Developer Guide

> Use the AWS Encryption SDK to protect data with secure client-side encryption.

- [Interacting with AWS KMS](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/getting-started.html)
- [Best practices](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/best-practices.html)
- [Configuring the SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/configure.html)
- [Versions of the AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/about-versions.html)
- [Frequently asked questions](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/faq.html)
- [Document history](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/document-history.html)

## [What is the AWS Encryption SDK?](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html)

- [Concepts](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/concepts.html): Learn about the concepts used in the AWS Encryption SDK
- [How the SDK works](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/how-it-works.html): Learn how the AWS Encryption SDK encrypts and decrypts your data.
- [Supported algorithm suites](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/supported-algorithms.html): Choose a supported algorithm suite.


## [Key stores](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/keystores.html)

- [Implementing least privileged permissions](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/keystore-least-privilege.html): When using a key store and AWS KMS Hierarchical keyrings, we recommend that you follow the principle of least privilege by defining the following roles:
- [Create a key store](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/create-keystore.html): Learn how to create a key store to persist hierarchical data and reduce AWS KMS calls with your Hierarchical keyring.
- [Configure key store actions](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/keystore-actions.html): Key store actions determine what operations your users can perform and how their AWS KMS Hierarchical keyring uses the KMS keys allowlisted in your key store.
- [Create branch keys](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/create-branch-keys.html): Learn how to create new active branch keys in your key store.
- [Rotate your active branch key](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rotate-branch-key.html): There can only be one active version for each branch key at a time.


## [Keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/choose-keyring.html)

- [AWS KMS keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-kms-keyring.html): An AWS KMS keyring uses AWS KMS keys to generate, encrypt, and decrypt data keys.
- [AWS KMS Hierarchical keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-hierarchical-keyring.html): With the AWS KMS Hierarchical keyring, you can protect your cryptographic materials under a symmetric encryption KMS key without calling AWS KMS every time you encrypt or decrypt data.
- [AWS KMS ECDH keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-kms-ecdh-keyring.html): An AWS KMS ECDH keyring uses asymmetric key agreement AWS KMS keys to derive a shared symmetric wrapping key between two parties.
- [Raw AES keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-raw-aes-keyring.html): The AWS Encryption SDK lets you use an AES symmetric key that you provide as a wrapping key that protects your data key.
- [Raw RSA keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-raw-rsa-keyring.html): The Raw RSA keyring performs asymmetric encryption and decryption of data keys in local memory with an RSA public and private keys that you provide.
- [Raw ECDH keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-raw-ecdh-keyring.html): The Raw ECDH keyring uses the elliptic curve public-private key pairs that you provide to derive a shared wrapping key between two parties.
- [Multi-keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-multi-keyring.html): You can combine keyrings into a multi-keyring.


## [Programming languages](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/programming-languages.html)

### [C](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language.html)

Download and install the AWS Encryption SDK for C.

- [Installing](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language-installation.html): Learn how to build the AWS Encryption SDK for C on all supported platforms.
- [Using the C SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language-using.html): Learn how to use the features of the AWS Encryption SDK for C.
- [Examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-examples.html): Examples of how to use the AWS Encryption SDK for C.

### [.NET](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/dot-net.html)

Learn how to program with the AWS Encryption SDK for .NET

- [Examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/dot-net-examples.html): The following examples show the basic coding patterns that you use when programming with the AWS Encryption SDK for .NET.
- [Go](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/go.html): This topic explains how to install and use the AWS Encryption SDK for Go.

### [Java](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/java.html)

Download and install the AWS Encryption SDK for Java.

- [Examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/java-example-code.html): Example code for learning how to use the AWS Encryption SDK for Java.

### [JavaScript](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript.html)

Download and install the AWS Encryption SDK for JavaScript.

- [Compatibility](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript-compatibility.html): The AWS Encryption SDK for JavaScript is designed to be interoperable with other language implementations of the AWS Encryption SDK.
- [Installation](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript-installation.html): The AWS Encryption SDK for JavaScript consists of a collection of interdependent modules.
- [Modules](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript-modules.html): The modules in the AWS Encryption SDK for JavaScript make it easy to install the code that you need for your projects.
- [Examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/js-examples.html): Examples of how to use the AWS Encryption SDK for JavaScript.

### [Python](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/python.html)

Download and install the AWS Encryption SDK for Python.

- [Examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/python-example-code.html): Example code for learning how to use the AWS Encryption SDK for Python.

### [Rust](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rust.html)

This topic explains how to install and use the AWS Encryption SDK for Rust.

- [Examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rust-examples.html): The following examples show the basic coding patterns that you use when programming with the AWS Encryption SDK for Rust.

### [Command line interface](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli.html)

Download, install, and configure the AWS Encryption SDK Command Line Interface.

- [Installing the CLI](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli-install.html): Download, install, and configure the AWS Encryption SDK Command Line Interface.
- [How to use the CLI](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli-how-to.html): Learn how to use the AWS Encryption SDK Command Line Interface (AWS Encryption CLI)
- [Examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli-examples.html): Learn how to use the AWS Encryption SDK Command Line Interface (AWS Encryption CLI) from these examples.
- [Syntax and parameter reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli-reference.html): Find syntax diagrams and parameter descriptions for the AWS Encryption SDK Command Line Interface.
- [Versions](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli-versions.html): Describes the versions of the AWS Encryption CLI.


## [Data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-key-caching.html)

- [How to use data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/implement-caching.html): This topic shows you how to use data key caching in your application.
- [Setting cache security thresholds](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/thresholds.html): When you implement data key caching, you need to configure the security thresholds that the caching CMM enforces.
- [Data key caching details](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-caching-details.html): Most applications can use the default implementation of data key caching without writing custom code.

### [Data key caching example](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/sample-cache-example.html)

Example using AWS Encryption SDK with data key caching and a local cache.

- [Example code](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/sample-cache-example-code.html): Code sample for a basic implementation of data key caching that uses a local cache.
- [CloudFormation template](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/sample-cache-example-cloudformation.html): AWS CloudFormationtemplate to set up local cache example resources.


## [Migrating your AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/migration.html)

- [How to migrate and deploy](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/migration-guide.html): When migrating from an AWS Encryption SDK version earlier than 1.7.x to version 2.0.x or later, you must transition safely to encrypting with key commitment.
- [Updating AWS KMS master key providers](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/migrate-mkps-v2.html): Learn how to update AWS KMS master key providers for version 1.7.x and later
- [Updating AWS KMS keyrings](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/migrate-keyrings-v2.html): Learn how to add an account filter to AWS KMS discovery keyrings
- [Setting your commitment policy](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/migrate-commitment-policy.html): Learn how to set the commitment policy that determines whether your data is encrypted and decrypted with key commitment.
- [Troubleshooting migration to the latest versions](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/troubleshooting-migration.html): Provides help for errors you might encounter while upgrading from earlier versions of the AWS Encryption SDK to version 2.0.x or later.


## [Reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/reference.html)

- [Message format reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/message-format.html): Understand the data structure (or message format) produced by the AWS Encryption SDK and reference it to build libraries that conform to the standard.
- [Message format examples](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/message-format-examples.html): See examples of the AWS Encryption SDK message format.
- [Body AAD reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/body-aad-reference.html): Learn how to form the additional authenticated data (AAD) required to build a library compatible with the AWS Encryption SDK message format.
- [Algorithms reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/algorithms-reference.html): How to implement the algorithms used in the AWS Encryption SDK.
- [Initialization vector reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/IV-reference.html): Detailed information about the use of initialization vectors in the AWS Encryption SDK.
- [AWS KMS Hierarchical keyring technical details](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/hierarchical-keyring-details.html): The AWS KMS Hierarchical keyring uses a unqiue data key to encrypt each message and encrypts each data key with a unique wrapping key derived from an active branch key.
