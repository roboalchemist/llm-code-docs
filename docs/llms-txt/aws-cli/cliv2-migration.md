# Migration guide

> Learn how to update the AWS CLI version 1 to AWS CLI version 2, and learn about the differences between the versions.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration.html

---

# Migration guide for the AWS CLI version 2

This section contains instructions for updating the AWS CLI version 1 to AWS CLI version 2. The AWS CLI version 2 builds
    on AWS CLI version 1 and includes features and enhancements based on community feedback. The AWS CLI version 2 is
    the most recent major version of the AWS CLI and supports all of the latest features. Some
    features that were introduced in version 2 are not backported to version 1 and you must upgrade
    to access those features. 

To prevent unexpected issues, before you migrate to version 2, [learn about the differences between the
            versions](./cliv2-migration-changes.html). The AWS CLI version 2 includes new features and changes that might require you to
        update your scripts or commands for backwards compatibility.

AWS CLI versions 1 and 2 use the same `aws` command name. If you have both
        versions installed, your computer uses the first one found in your search path. This could
        result in your `aws` command name calling your old AWS CLI version, even when you
        have the new one installed.

To update to the AWS CLI version 2, follow one of the below instructions:

- 
    
If you previously installed AWS CLI version 1, follow the instructions in 
        [Installing AWS CLI version 2 from  AWS CLI version 1](./cliv2-migration-instructions.html).

- 
        
If you have not previously installed AWS CLI version 1, follow the instructions in [Getting started with the AWS CLI](./cli-chap-getting-started.html).

###### Topics

- 
[New features and changes in the AWS CLI version 2](./cliv2-migration-changes.html)

- 
[Installing AWS CLI version 2 from  AWS CLI version 1](./cliv2-migration-instructions.html)

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Enforcing a minimum TLS version

New features and changes