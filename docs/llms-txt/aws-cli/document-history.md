# Document History

> Find the revision dates, related releases, and important changes to the AWS Command Line Interface User Guide.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/document-history.html

---

# AWS CLI user guide document history

The following table describes important additions to the
            *AWS Command Line Interface User Guide*, beginning in January 2019. For notification about
        updates to this documentation, you can subscribe to the RSS feed.

ChangeDescriptionDate
[Account-based endpoint support added to the AWS CLI version 2](https://docs.aws.amazon.com/en_us/cli/latest/userguide/cli-configure-endpoints.html#endpoints-accountid)

Account-based endpoints using your AWS account ID are now supported in the AWS CLI version 2.

March 20, 2025

[Account-based endpoint support added to the AWS CLI version 1](https://docs.aws.amazon.com/en_us/cli/v1/userguide/cli-configure-endpoints.html#endpoints-accountid)

Account-based endpoints using your AWS account ID are now supported in the AWS CLI version 2.

February 24, 2025

Updated credential and authentication information.

Updated credential and authentication method instructions and examples. This
                    includes updating relevant
                        Getting started pages and configuration pages. To accommodate this
                    increase in documentation, relevant credential topics were moved to the new
                        [Authentication and access
                        credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)
                    section.

March 31, 2023

[Token
                    provider configuration with automatic authentication refresh for AWS IAM Identity Center
                    added](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html)

The new process to configure the AWS CLI to authenticate users with AWS IAM Identity Center
                    (IAM Identity Center) using the SSO token provider configuration, which can automatically
                    retrieve refreshed authentication tokens.

December 7, 2022

[Official Amazon ECR Public image for the AWS CLI version 2
                    released](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-docker.html)

The official supported Amazon ECR Public image for the AWS CLI version 2 is released for
                    Linux, macOS, and Windows.

November 18, 2022

[Updated
                    the guide for migrating from AWS CLI V1 to V2](https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration.html)

Expanded the breaking changes guide to include migration instructions to going
                    from AWS CLI version 1 to the AWS CLI version 2. Includes updates to the Troubleshooting page to
                    help with installation issues. 

May 13, 2022

[New
                    process to build a AWS CLI installer from source.](https://docs.aws.amazon.com/en_us/cli/latest/userguide/getting-started-source-install.html)

New process to install or update from source to the latest release of the
                    AWS CLI on supported operating systems.

February 17, 2022

Content for the AWS CLI V1 and V2 are now separated into their respective
                    guides

For clarity and ease, the AWS CLI version 1 and AWS CLI version 2 content is now separated into
                    their own guides. 
                        For AWS CLI version 1, see the [AWS CLI version 1 User
                        Guide.](https://docs.aws.amazon.com/cli/v1/userguide/)

November 2, 2021

[Added AWS CLI alias information](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-alias.html)

Added AWS CLI alias information. Aliases are shortcuts you can create in the
                    AWS Command Line Interface (AWS CLI) to shorten commands or scripts that you frequently use.

March 11, 2021

[Updated filter output information](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html)

Updated information for filters and moved to their own page.

February 1, 2021

[Added information for
                    Wizards](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-wizard.html)

Added AWS CLI version 2 wizard information.

November 20, 2020

[Updated
                    auto-prompt](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-prompting.html)

Updated the AWS CLI version 2 auto-prompt information with current features.

November 10, 2020

[Added Amazon S3 scripting example](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-lifecycle-example.html)

Added an Amazon S3 lifecycle scripting example.

October 15, 2020

[Added Amazon EC2 scripting example](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instance-type-script.html)

Added an Amazon EC2 instance type scripting example.

October 15, 2020

[Added retries information](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html)

Added a retries page for features and behavior of retries in the AWS CLI.

September 17, 2020

[Server-side and client-side pagination page](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html)

Updated pagination information and centralized on a single page.

August 17, 2020

[Updated s3 commands page](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)

Updated the high-level s3 commands page with new examples and
                    resources.

July 30, 2020

[Updated installation information](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

The install, update, and uninstall information for Linux, macOS, and Windows
                    are updated.

May 19, 2020

[Added information for text file encoding on the
                    AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration.html)

By default, AWS CLI version 2 uses the same text file encoding as the local. You can now
                    use environment variables to set text file encoding.

May 14, 2020

[Official Docker image for the AWS CLI version 2
                    released](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-docker.html)

The official support Docker image for the AWS CLI version 2 is released for all Linux,
                    macOS, and Windows.

March 31, 2020

[Added information regarding client-side pagers for
                    AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html)

By default, AWS CLI version 2 uses the pager program `less` for all
                    client-side output.

February 19, 2020

[AWS Command Line Interface (AWS CLI) Version 2 is officially
                    released](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html)

The AWS CLI version 2 is generally available and is the recommended version for
                    customers to install. 

February 10, 2020

[macOS installer for AWS CLI version 2 is now an Apple Package installer
                        `.pkg` file. ](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html)

The macOS installer for AWS CLI version 2 has been updated from a
                        `.zip` file with a shell script to full macOS Installer
                    package. This simplifies installation and makes it compatible with the newest
                    macOS releases.

February 3, 2020

[Added content for AWS CLI version 2's improved default handling of S3 and STS Regional
                    endpoints](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-config-sts_regional_endpoints)

By default, AWS CLI version 2 now directs requests for the Amazon S3 and AWS STS services to
                    the currently configured Regional endpoint instead of the global
                    endpoint.

January 13, 2020

[Developer preview release for AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

Announcing preview release of AWS CLI version 2. Added instructions about installing
                    version 2. Add Migration topic to discuss differences between versions 1 and
                    2.

November 7, 2019

[Added support for AWS IAM Identity Center to AWS CLI named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)

AWS CLI version 2 adds support for creating a named profile that can directly login to
                    IAM Identity Center and get AWS temporary credentials for use in subsequent AWS CLI
                    commands.

November 7, 2019

[New MFA section](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html#cli-configure-role-mfa)

Added a new section describing how to access the CLI using multi-factor
                    authentication and roles.

May 3, 2019

[Update to "Using the CLI" section](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html)

Major improvements and additions to the usage instructions and
                    procedures.

March 7, 2019

[Update to "Installing the CLI" section](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

Major improvements and additions to the AWS CLI installation instructions and
                    procedures.

March 7, 2019

[Update to "Configuring the CLI" section](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

Major improvements and additions to the AWS CLI configuration instructions and
                    procedures.

March 7, 2019