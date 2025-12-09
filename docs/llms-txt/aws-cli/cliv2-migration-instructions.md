# Migration instructions

> Learn how to migrate from AWS CLI version 1 to AWS CLI version 2.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration-instructions.html

---

# Installing AWS CLI version 2 from  AWS CLI version 1

This topic provides instructions for migrating from AWS CLI version 1 to AWS CLI version 2.

AWS CLI versions 1 and 2 use the same `aws` command name. If you have both
        versions installed, your computer uses the first one found in your search path. If you
        previously installed AWS CLI version 1, we recommend that you do one of the following to use
        AWS CLI version 2:

- 
            
** Recommended** â [Uninstall AWS CLI version 1 and use only
                    AWS CLI version 2](#cliv2-migration-instructions-migrate).

- 
            
[To have both version
                    installed](#cliv2-migration-instructions-side-by-side), use your operating system's ability to create a symbolic
                link (symlink) or alias with a different name for one of the two `aws`
                commands.

For information on breaking changes between version 1 and version 2, see [New features and changes in the AWS CLI version 2](./cliv2-migration-changes.html).

## Replacing version 1 with version
                2

Perform the following steps to replace AWS CLI version 1 with AWS CLI version 2. 

###### To replace AWS CLI version 1 with AWS CLI version 2

- 
                
Prepare any existing scripts you have for the migration by confirming any
                    breaking changes between version 1 and version 2 in [New features and changes in the AWS CLI version 2](./cliv2-migration-changes.html).

- 
                
Uninstall the AWS CLI version 1 by following the uninstall instructions for your
                    operating system in [Installing, updating, and uninstalling the
                        AWS CLI version 1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html).

- 
                
Confirm that the AWS CLI is completely uninstalled by using the following
                    command.

`$ `aws --version
                Complete one of the following based on the output:

**No version returned:** You've
                            successfully uninstalled the AWS CLI version 1 and can proceed to the next
                            step.

- 
                        
**A version is returned:** You still have
                            an install of the AWS CLI version 1. For troubleshooting steps, see [The "aws --version" command returns a
                version after uninstalling the AWS CLI](./cli-chap-troubleshooting.html#tshoot-uninstall-1). Perform troubleshooting steps until
                            no version output is received.

            - 
                
Install the AWS CLI version 2 by following the appropriate install instructions for your
                    operating system in [Installing or updating to the latest version of
            the AWS CLI](./getting-started-install.html).

## Side-by-side
                install

To have both versions installed, use your operating system's ability to create a
            symbolic link (symlink) or alias with a different name for one of the two
                `aws` commands. 

- 
                
Install the AWS CLI version 2 by following the appropriate install instructions for your
                    operating system in [Installing or updating to the latest version of
            the AWS CLI](./getting-started-install.html).

- 
                
Use your operating system's ability to create a symlink or alias with a
                    different name for one of the two `aws` commands, such as using
                            `aws2` for AWS CLI version 2. The following
                    are symlink examples for AWS CLI version 2. Replace the `PATH`
                    with your install location.

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

New features and changes

Uninstall