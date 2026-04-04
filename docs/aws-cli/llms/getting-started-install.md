# Install/Update

> Instructions to install or update the AWS CLI on your system.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

---

# Installing or updating to the latest version of
            the AWS CLI

This topic describes how to install or update the latest release of the AWS Command Line Interface (AWS CLI)
        on supported operating systems. For information on the latest releases of AWS CLI, see the
            [AWS CLI version 2
            Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst) on GitHub.

To
      install a past release of the AWS CLI, see [Installing past releases of the AWS CLI version 2](./getting-started-version.html).
    For uninstall instructions, see [Uninstalling the AWS CLI version 2](./uninstall.html).

###### Important

AWS CLI versions 1 and 2 use the same `aws` command name. If you previously
            installed AWS CLI version 1, see [Migration guide for the AWS CLI version 2](./cliv2-migration.html).

###### Topics

- 
[AWS CLI install and update
                instructions](#getting-started-install-instructions)

- 
[Troubleshooting AWS CLI install and uninstall
                errors](#install-tshoot)

- 
[Next steps](#install-next-steps)

## AWS CLI install and update
                instructions

For installation instructions, expand the section for your operating system.

#### Install and update requirements

- 
                        
You must be able to extract or "unzip" the downloaded package. If
                            your operating system doesn't have the built-in `unzip`
                            command, use an equivalent.

- 
                        
The AWS CLI uses `glibc`, `groff`, and
                            `less`. These are included by default in most major
                            distributions of Linux.

- 
                        
We support the AWS CLI on 64-bit versions of recent distributions of
                            CentOS, Fedora, Ubuntu, Amazon Linux 1, Amazon Linux 2, Amazon Linux 2023, and Linux
                            ARM.

- 
                        
Because AWS doesn't maintain third-party repositories other than
                                `snap`, we canât guarantee that they contain the latest
                            version of the AWS CLI.

#### Install or
                        update the AWS CLI

###### Warning

If this is your first time updating on Amazon Linux, to install the latest
                        version of the AWS CLI, you must uninstall the pre-installed
                        `yum` version using the following command:

`$ ``sudo yum remove awscli`After the `yum` installation of the AWS CLI is removed,
                        follow the below Linux install instructions.

You can install the AWS CLI by using one of the following methods:

- 
                            
**The command line installer** is
                                good option for version control, as you can specify the version to
                                install. This option does not auto-update and you must download a
                                new installer each time you update to overwrite previous
                                version.

- 
                            
**The officially supported `snap`
                                    package** is a good option to always have the latest
                                version of the AWS CLI as snap packages automatically refresh. There
                                is no built-in support for selecting minor versions of AWS CLI and
                                therefore is not an optimal install method if your team needs to pin
                                versions.

#### Install and update
                            requirements

- 
                            
We support the AWS CLI on macOS versions 11 and later. For more
                                information, see [macOS support policy updates for the AWS CLI v2](https://aws.amazon.com/blogs/developer/macos-support-policy-updates-for-the-aws-cli-v2/) on the
                                    *AWS Developer Tools
                                Blog*.

- 
                            
Because AWS doesn't maintain third-party repositories, we canât
                                guarantee that they contain the latest version of the AWS CLI.

**macOS version support matrix**

                    AWS CLI version
                    Supported macOS version

                    2.21.0 â current
                    11+

                    2.17.0 â2.20.0
                    10.15+

                    2.0.0 â 2.16.12
                    10.14 and below

#### Install or update the
                            AWS CLI

If you are updating to the latest version, use the same installation
                        method that you used in your current version. You can install the AWS CLI on
                        macOS in the following ways.

#### Install and update
                            requirements

- 
                            
We support the AWS CLI on Microsoft-supported versions of 64-bit
                                Windows.

- 
                            
Admin rights to install software

#### Install or update the
                            AWS CLI

To update your current installation of AWS CLI on Windows, download a new
                        installer each time you update to overwrite previous versions. AWS CLI is
                        updated regularly. To see when the latest version was released, see the
                            [AWS CLI version 2 Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst) on *GitHub*. 

- 
                            
Download and run the AWS CLI MSI installer for Windows
                                (64-bit):

[https://awscli.amazonaws.com/AWSCLIV2.msi](https://awscli.amazonaws.com/AWSCLIV2.msi)

Alternatively, you can run the `msiexec` command to run
                                the MSI installer.

`C:\> ``msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi`
                            For various parameters that can be used with `msiexec`,
                                see [msiexec](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec) on the *Microsoft
                                    Docs* website. For example, you can use the
                                    `/qn` flag for a silent installation.

`C:\> ``msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi /qn`
                        
- 
                            To confirm the installation, open the **Start**
                                menu, search for `cmd` to open a command prompt window,
                                and at the command prompt use the `aws --version`
                                command. 

`C:\> ``aws --version``
aws-cli/2.27.41 Python/3.11.6 Windows/10 exe/AMD64 prompt/off`
                            If Windows is unable to find the program, you might need to close
                                and reopen the command prompt window to refresh the path, or follow
                                the troubleshooting in [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

## Troubleshooting AWS CLI install and uninstall
                errors

If you come across issues after installing or uninstalling the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for troubleshooting steps. For the most
            relevant troubleshooting steps, see [Command not found errors](./cli-chap-troubleshooting.html#tshoot-install-not-found), [The "aws --version" command
                returns a different version than you installed](./cli-chap-troubleshooting.html#tshoot-install-wrong-version), and [The "aws --version" command returns a
                version after uninstalling the AWS CLI](./cli-chap-troubleshooting.html#tshoot-uninstall-1).

## Next steps

After you successfully install the AWS CLI, you can safely delete your downloaded
            installer files. After completing the steps in [Prerequisites to use the AWS CLI version 2](./getting-started-prereqs.html)
            and installing the AWS CLI, you should perform a [Setting up the AWS CLI](./getting-started-quickstart.html).

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Prerequisites

Past releases