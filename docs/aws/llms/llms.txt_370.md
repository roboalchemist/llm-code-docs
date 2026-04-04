# Source: https://docs.aws.amazon.com/enclaves/latest/user/llms.txt

# AWS Nitro Enclaves User Guide

> Describes key concepts for AWS Nitro Enclaves and provides instructions for using enclaves.

- [What is Nitro Enclaves?](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html)
- [Nitro Enclaves concepts](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-concepts.html)
- [Getting started with the Hello Enclaves sample application](https://docs.aws.amazon.com/enclaves/latest/user/getting-started.html)
- [Working with multiple enclaves](https://docs.aws.amazon.com/enclaves/latest/user/multiple-enclaves.html)
- [Nitro Enclaves and Amazon EKS](https://docs.aws.amazon.com/enclaves/latest/user/kubernetes.html)
- [Verifying the root of trust](https://docs.aws.amazon.com/enclaves/latest/user/verify-root.html)
- [Document history](https://docs.aws.amazon.com/enclaves/latest/user/DocumentHistory.html)

## [Enclave workflow overview](https://docs.aws.amazon.com/enclaves/latest/user/flow.html)

### [Nitro Enclaves application development](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html)

Learn about how to develop an application designed to run inside an isolated enclave environment on Windows or Linux operating systems.

- [Application development on Linux](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications-linux.html): Understand how to develop applications on Linux for Nitro Enclaves.

### [Application development on Windows](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications-windows.html)

Understand how to develop applications on Windows for Nitro Enclaves.

- [Working with the vsock socket in Windows](https://docs.aws.amazon.com/enclaves/latest/user/vsock-win.html): Understand how to work with vsock sockets in Windows for Nitro Enclaves.
- [Building an enclave image file](https://docs.aws.amazon.com/enclaves/latest/user/building-eif.html): Learn how to build an enclave image file for the application you developed.
- [Creating an enclave](https://docs.aws.amazon.com/enclaves/latest/user/create-enclave.html): Learn how to create an enclave using the image file of the application you developed.


## [Cryptographic attestation](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html)

- [Using cryptographic attestation with AWS KMS](https://docs.aws.amazon.com/enclaves/latest/user/kms.html): Understand how to implement cryptographic attestation with AWS KMS for Nitro Enclaves.
- [Getting started with cryptographic attestation](https://docs.aws.amazon.com/enclaves/latest/user/hello-kms.html): Learn how to get started with cryptographic attestation by using the sample KMS Tool application.


## [AWS Certificate Manager for Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-refapp.html)

- [Install ACM for Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/install-acm.html): Use the following procedure to install and configure ACM for Nitro Enclaves.
- [Update ACM for Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/update-acm.html): If you have already installed , use the following command to update it to the latest version.
- [Uninstall ACM for Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/uninstall-acm.html): If you no longer want to use , use the following procedure to uninstall it.


## [Security](https://docs.aws.amazon.com/enclaves/latest/user/security.html)

- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/enclaves/latest/user/logging-enclaves-using-cloudtrail.html): Learn about logging EBS direct APIs API calls with AWS CloudTrail.


## [Nitro Enclaves CLI](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli.html)

- [Install the CLI on Linux](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli-install.html): Learn how to install the Nitro Enclaves CLI on Linux.
- [Install the CLI on Windows](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli-install-win.html): Learn how to install the Nitro Enclaves CLI on Windows.
- [Uninstall the CLI on Linux](https://docs.aws.amazon.com/enclaves/latest/user/uninstall-cli.html): Understand how to uninstall Nitro Enclaves CLI from Linux operating systems.
- [Uninstall the CLI on Windows](https://docs.aws.amazon.com/enclaves/latest/user/uninstall-cli-win.html): Understand how to uninstall AWS Nitro Enclaves CLI from Windows operating systems.

### [Nitro CLI Reference](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli-ref.html)

Learn what commands are available for the Nitro Enclaves Command Line Interface.

- [nitro-cli build-enclave](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-build-enclave.html): Learn about the build-enclave command.
- [nitro-cli run-enclave](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-run-enclave.html): Learn about the run-enclave command.
- [nitro-cli describe-enclaves](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-describe-enclaves.html): Learn about the describe-enclaves command.
- [nitro-cli console](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-console.html): Learn about the console command.
- [nitro-cli describe-eif](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-describe-eif.html): Learn about the describe-eif command.
- [nitro-cli sign-eif](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-sign-eif.html): Learn about the sign-eif command.
- [nitro-cli pcr](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-pcr.html): Learn about the pcr command.
- [nitro-cli terminate-enclave](https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-terminate-enclave.html): Learn about the terminate-enclave command.
- [Nitro Enclaves CLI error codes](https://docs.aws.amazon.com/enclaves/latest/user/cli-errors.html): Learn about the error codes the Nitro Enclaves CLI might return.
