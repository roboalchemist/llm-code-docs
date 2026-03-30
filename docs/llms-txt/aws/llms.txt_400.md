# Source: https://docs.aws.amazon.com/freertos/latest/userguide/llms.txt

# FreeRTOS User Guide

> Provides detailed information about the microcontroller operating system that makes small, low-powered edge devices easy to program, deploy, secure, and maintain.

- [AWS IoT Device SDK for Embedded C](https://docs.aws.amazon.com/freertos/latest/userguide/c-sdk.html)
- [Understand the FreeRTOS Common IO APIs](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-common-io.html)
- [Get started with FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-modular.html)
- [Amazon-FreeRTOS Github Repository Migration Guide](https://docs.aws.amazon.com/freertos/latest/userguide/github-repo-migration.html)

## [What is FreeRTOS?](https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html)

- [FreeRTOS versions](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-versioning.html): Learn how you can use FreeRTOS and its corresponding versions.
- [FreeRTOS architecture](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-architecture.html): Learn about FreeRTOS and its architecture in detail.
- [Development workflow](https://docs.aws.amazon.com/freertos/latest/userguide/development-workflow.html): Learn how you can use FreeRTOS and its development workflow.


## [FreeRTOS kernel fundamentals](https://docs.aws.amazon.com/freertos/latest/userguide/dev-guide-freertos-kernel.html)

- [The FreeRTOS kernel scheduler](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-kernel-scheduler.html): Learn the fundamentals of the FreeRTOS kernel scheduler.
- [Kernel memory allocation](https://docs.aws.amazon.com/freertos/latest/userguide/kernel-memory-allocation.html): Learn fundamentals of the kernel memory allocation .
- [Manage application memory](https://docs.aws.amazon.com/freertos/latest/userguide/application-memory-management.html): Learn the fundamentals of the FreeRTOS memory management.
- [Intertask coordination](https://docs.aws.amazon.com/freertos/latest/userguide/inter-task-coordination.html): Learn the fundamentals of the FreeRTOS Intertask coordination.
- [Symmetric multiprocessing (SMP) support](https://docs.aws.amazon.com/freertos/latest/userguide/smp-support.html): Learn symmetric multiprocessing (SMP) support.
- [Software timers](https://docs.aws.amazon.com/freertos/latest/userguide/software-timers.html): Learn about software timers.
- [Low power support](https://docs.aws.amazon.com/freertos/latest/userguide/low-power-support.html): Learn about low power support.
- [FreeRTOSConfig.h](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-config.html): Configure the kernel (FreeRTOSConfig.h).


## [AWS IoT Device Tester for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/device-tester-for-freertos-ug.html)

- [Supported versions of IDT for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html): The list of supported versions of AWS IoT Device Tester for FreeRTOS
- [Unsupported IDT versions](https://docs.aws.amazon.com/freertos/latest/userguide/idt-unsupported-versions-afr.html): The list of unsupported versions of AWS IoT Device Tester for FreeRTOS

### [Download IDT for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/idt-programmatic-download.html)

Describes options to download AWS IoT Device Tester for FreeRTOS.

- [Download IDT programmatically](https://docs.aws.amazon.com/freertos/latest/userguide/idt-programmatic-download-process.html): Describes options to download AWS IoT Device Tester with a program.

### [IDT with FreeRTOS qualification suite 2.0 (FRQ 2.0)](https://docs.aws.amazon.com/freertos/latest/userguide/lts-idt-freertos-qualification.html)

This talks about the LTS qualification suite

- [Set up the LTS qualification prerequisites](https://docs.aws.amazon.com/freertos/latest/userguide/lts-idt-dev-tester-prereqs.html): This talks about the LTS qualification prerequisites

### [First test of your microcontroller board](https://docs.aws.amazon.com/freertos/latest/userguide/lts-qual-steps.html)

First test of your microcontroller board

- [Create a device pool in IDT for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/lts-cfg-dt-dp.html): Create a device pool in IDT for FreeRTOS

### [Configure build, flash, and test settings](https://docs.aws.amazon.com/freertos/latest/userguide/lts-cfg-dt-ud.html)

Configure build, flash, and test settings

- [Configure settings for testing devices](https://docs.aws.amazon.com/freertos/latest/userguide/lts-config-settings-device.html): Configure settings for testing devices
- [IDT for FreeRTOS variables](https://docs.aws.amazon.com/freertos/latest/userguide/lts-dt-vars.html): IDT for FreeRTOS variables

### [Use the IDT UI to run the FreeRTOS qualification suite](https://docs.aws.amazon.com/freertos/latest/userguide/lts-device-tester-ui.html)

User interface to create and edit AWS IoT Device Tester configuration files

- [Configure AWS credentials to use the IDT UI](https://docs.aws.amazon.com/freertos/latest/userguide/lts-configure-aws-credentials.html): Configure AWS credentials in the configuration files
- [Open the IDT for FreeRTOS UI](https://docs.aws.amazon.com/freertos/latest/userguide/lts-open-idt-ui.html): Open the IDT for FreeRTOS UI
- [Create a new configuration](https://docs.aws.amazon.com/freertos/latest/userguide/lts-create-new-configuration.html): Create a new configuration
- [Modify an existing configuration](https://docs.aws.amazon.com/freertos/latest/userguide/lts-modify-existing-configuration.html): User interface prerequisites for configuration files
- [Run qualification tests](https://docs.aws.amazon.com/freertos/latest/userguide/lts-run-tests-from-ui.html): Run qualification tests for IDT in console
- [Run the FreeRTOS qualification 2.0 suite](https://docs.aws.amazon.com/freertos/latest/userguide/lts-run-tests.html): Run the FreeRTOS qualification 2.0 suite to interact with AWS IoT Device Tester.
- [View the IDT for FreeRTOSresults](https://docs.aws.amazon.com/freertos/latest/userguide/view-results-lts.html): Understand and view the results
- [Interpret the IDT for FreeRTOS results](https://docs.aws.amazon.com/freertos/latest/userguide/interpreting-results-lts.html): Interpreting IDT for FreeRTOS results
- [View the IDT for FreeRTOSlogs](https://docs.aws.amazon.com/freertos/latest/userguide/view-logs-lts.html): Understand and viewing the logs

### [IDT with FreeRTOS qualification suite 1.0 (FRQ 1.0)](https://docs.aws.amazon.com/freertos/latest/userguide/idt-freertos-qualification.html)

This talks about the FRQ 1.0 qualification suite

- [Setup the 1.0 qualification prerequisites](https://docs.aws.amazon.com/freertos/latest/userguide/dev-tester-prereqs.html): This talks about the 1.0 qualification prerequisites

### [First test of your microcontroller board](https://docs.aws.amazon.com/freertos/latest/userguide/qual-steps.html)

First test of your microcontroller board

- [Create a device pool in IDT for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/cfg-dt-dp.html): Create a device pool in IDT for FreeRTOS

### [Configure build, flash, and test settings](https://docs.aws.amazon.com/freertos/latest/userguide/cfg-dt-ud.html)

Configure build, flash, and test settings

- [Configure settings for testing devices](https://docs.aws.amazon.com/freertos/latest/userguide/config-settings-device.html): Configure settings for testing devices
- [IDT for FreeRTOS variables](https://docs.aws.amazon.com/freertos/latest/userguide/dt-vars.html): IDT for FreeRTOS variables

### [Use the IDT UI to run the FreeRTOS qualification suite](https://docs.aws.amazon.com/freertos/latest/userguide/device-tester-ui.html)

User interface to create and edit IDT configuration files.

- [Prerequisites](https://docs.aws.amazon.com/freertos/latest/userguide/dev-tester-ui-prereqs.html): User interface prerequisites for configuration files when running FreeRTOS qualification suite
- [Get started with the IDT-FreeRTOS UI](https://docs.aws.amazon.com/freertos/latest/userguide/dev-tester-ui-getting-started.html): Learn how to open and use the AWS IoT Device Tester for FreeRTOS user interface.
- [Run Bluetooth Low Energy tests](https://docs.aws.amazon.com/freertos/latest/userguide/afr-bridgekeeper-dt-bt.html): Run Bluetooth Low Energy tests
- [Run the FreeRTOS qualification suite](https://docs.aws.amazon.com/freertos/latest/userguide/run-tests.html): Run the FreeRTOS qualification suite to interact with AWS IoT Device Tester.
- [View the IDT for FreeRTOS results](https://docs.aws.amazon.com/freertos/latest/userguide/view-results-frq.html): Understand and view the results
- [Interpret the IDT for FreeRTOS results](https://docs.aws.amazon.com/freertos/latest/userguide/interpreting-results-frq.html): Interpreting IDT for FreeRTOS results
- [View the IDT for FreeRTOS logs](https://docs.aws.amazon.com/freertos/latest/userguide/view-logs-frq.html): Understand and viewing the logs

### [Develop and run your own IDT test suites](https://docs.aws.amazon.com/freertos/latest/userguide/idt-custom-tests.html)

Describes AWS IoT Device Tester custom test suites for device validation so you an develop and test.

### [Tutorial: Build and run the sample IDT test suite](https://docs.aws.amazon.com/freertos/latest/userguide/build-sample-suite.html)

Learn how to build and run the sample test suite included in the AWS IoT Device Tester download.

- [Set up the prerequisites for the sample test suite](https://docs.aws.amazon.com/freertos/latest/userguide/prereqs-tutorial-sample.html): Prerequisites to build and run the sample test suite included in the AWS IoT Device Tester download.
- [Configure device information for IDT](https://docs.aws.amazon.com/freertos/latest/userguide/configure-idt-sample.html): Configure device information for IDT
- [Build the sample test suite](https://docs.aws.amazon.com/freertos/latest/userguide/build-sample.html): Configure the sample test suite
- [Use IDT to run the sample test suite](https://docs.aws.amazon.com/freertos/latest/userguide/run-sample.html): Use IDT to run the sample test suite
- [Troubleshoot errors](https://docs.aws.amazon.com/freertos/latest/userguide/tutorial-troubleshooting-custom.html): Troubleshoot sample test suite included in the AWS IoT Device Tester (IDT) download.

### [Tutorial: Develop a simple IDT test suite](https://docs.aws.amazon.com/freertos/latest/userguide/create-custom-tests.html)

Use the test suite environment of IDT for FreeRTOS to develop a simple test suite.

- [Set up the prerequisites for a simple IDT test suite](https://docs.aws.amazon.com/freertos/latest/userguide/prereqs-tutorial-custom.html): Prerequisites for a simple IDT test suite environment.
- [Create a test suite directory](https://docs.aws.amazon.com/freertos/latest/userguide/test-suite-dir.html): Create a test suite directory for IDT for FreeRTOS to develop a simple test suite.
- [Create configuration files](https://docs.aws.amazon.com/freertos/latest/userguide/test-suite-json.html): Create a configuration file for IDT for FreeRTOS in a simple test suite.
- [Get the IDT client SDK](https://docs.aws.amazon.com/freertos/latest/userguide/add-idt-sdk.html): Get the IDT client SDK for IDT for FreeRTOS in a simple test suite.
- [Create the test case executable](https://docs.aws.amazon.com/freertos/latest/userguide/test-suite-exe.html): Create the test case executable in a simple test suite.
- [Configure device information for IDT](https://docs.aws.amazon.com/freertos/latest/userguide/configure-idt-sample2.html): Configure device information for IDT in a simple test suite.
- [Run the test suite](https://docs.aws.amazon.com/freertos/latest/userguide/run-test-suite.html): Run the test suite in the run folder
- [Troubleshoot errors](https://docs.aws.amazon.com/freertos/latest/userguide/tutorial-troubleshooting.html): Run the test suite in the run folder and troubleshoot errors
- [Create IDT test suite configuration files](https://docs.aws.amazon.com/freertos/latest/userguide/idt-json-config.html): Create IDT test suite configuration files
- [Configure the IDT test orchestrator](https://docs.aws.amazon.com/freertos/latest/userguide/idt-test-orchestrator.html): Describes the AWS IoT Device Tester test orchestrator.
- [Configure the IDT state machine](https://docs.aws.amazon.com/freertos/latest/userguide/idt-state-machine.html): Describes the AWS IoT Device Tester state machine that determines the flow of your test suite.
- [Create IDT test case executable](https://docs.aws.amazon.com/freertos/latest/userguide/test-executables.html): Describe how to write a test case executable and understand
- [Use the IDT context](https://docs.aws.amazon.com/freertos/latest/userguide/idt-context.html): Describes the IDT context and how to use it to access data during test execution.
- [Configure settings for test runners](https://docs.aws.amazon.com/freertos/latest/userguide/set-config-custom.html): Describes the configuration information that test runners provide.
- [Debug and run custom test suites](https://docs.aws.amazon.com/freertos/latest/userguide/run-tests-custom.html): Describes how to run IDT in debug mode and lists the CLI commands
- [Review IDT test results and logs](https://docs.aws.amazon.com/freertos/latest/userguide/idt-review-results-logs.html): View and interpret test results and logs generated by AWS IoT Device Tester.
- [Submit IDT usage metrics](https://docs.aws.amazon.com/freertos/latest/userguide/idt-usage-metrics.html): Learn how to submit IDT usage metrics to AWS.
- [Test suite versions](https://docs.aws.amazon.com/freertos/latest/userguide/idt-test-suite-versions.html): Use the test suites for AWS IoT Device Tester when working with FreeRTOS.
- [Troubleshoot errors](https://docs.aws.amazon.com/freertos/latest/userguide/dt-afr-troubleshooting.html): Troubleshoot errors for test suites for AWS IoT Device Tester when working with FreeRTOS.
- [AWS Managed policy for AWS IoT Device Tester](https://docs.aws.amazon.com/freertos/latest/userguide/security-iam-aws-managed-policies.html): Learn about AWS managed policies for AWS IoT Device Tester, and changes to these policies.
- [Support policy](https://docs.aws.amazon.com/freertos/latest/userguide/idt-support-policy.html): Support policy for AWS IoT Device Tester with FreeRTOS.


## [Security in AWS](https://docs.aws.amazon.com/freertos/latest/userguide/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/freertos/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your FreeRTOS resources.

- [How FreeRTOS works with IAM](https://docs.aws.amazon.com/freertos/latest/userguide/security_iam_service-with-iam.html): How FreeRTOS features available works with IAM.
- [Identity-based policy examples](https://docs.aws.amazon.com/freertos/latest/userguide/security_iam_id-based-policy-examples.html): How to identify the identity-based policy examples resources.
- [Troubleshooting](https://docs.aws.amazon.com/freertos/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with FreeRTOS and IAM.
- [Compliance validation](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/freertos/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/freertos/latest/userguide/infrastructure-security.html): Learn about how infrastructure security is managed in FreeRTOS managed services.


## [Archive](https://docs.aws.amazon.com/freertos/latest/userguide/archive-all.html)

- [FreeRTOS User Guide Archive](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ug-archive.html): Find older versions of the FreeRTOS user guide.

### [Previous FreeRTOS User Guide contents](https://docs.aws.amazon.com/freertos/latest/userguide/archive-previous.html)

Find previous content from the FreeRTOS user guide.

### [Get Started with FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started.html)

Follow the tutorial to download, configure and compile a demo application with FreeRTOS.

- [FreeRTOS demo application](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-demo.html)
- [First steps](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-prereqs.html): Learn how to get started with FreeRTOS.
- [Troubleshooting](https://docs.aws.amazon.com/freertos/latest/userguide/gsg-troubleshooting.html): How to troubleshoot issues that you encounter while getting started with FreeRTOS:
- [Using CMake with FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/getting-started-cmake.html): Learn how to use CMake to create project build files for FreeRTOS.
- [Developer-mode key provisioning](https://docs.aws.amazon.com/freertos/latest/userguide/dev-mode-key-provisioning.html): Learn how to get a trusted X.509 client certificate onto an IoT device running FreeRTOS.

### [Board-specific getting started guides](https://docs.aws.amazon.com/freertos/latest/userguide/getting-started-guides.html)

Learn how to get started using FreeRTOS on microcontroller boards.

- [Cypress CYW943907AEVAL1F Development Kit](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_cypress_43.html): Use the Cypress CYW943907AEVAL1F Development Kit with FreeRTOS.
- [Cypress CYW954907AEVAL1F Development Kit](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_cypress_54.html): Use the Cypress CYW954907AEVAL1F Development Kit with FreeRTOS.
- [Cypress CY8CKIT-064S0S2-4343W](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_cypress_psoc64.html): Use the Cypress CY8CKIT-064S0S2-4343W with FreeRTOS.
- [Microchip ATECC608A Secure Element with Windows simulator](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_atecc608a.html): Get started with the Microchip ATECC608A Secure Element using FreeRTOS.
- [Getting started with the Espressif ESP32-DevKitC and the ESP-WROVER-KIT](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_espressif.html)
- [Getting started with the Espressif ESP32-WROOM-32SE](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_esp32wroom-32se.html)
- [Getting started with the Espressif ESP32-S2](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_esp32-s2.html)
- [Infineon XMC4800 IoT Connectivity Kit](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_infineon.html): Learn how to use the Infineon XMC4800 IoT Connectivity Kit with FreeRTOS.
- [Infineon OPTIGA Trust X and XMC4800 IoT Connectivity Kit](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_infineon_trust_x.html): Learn how to use the Infineon OPTIGA Trust X and XMC4800 IoT Connectivity Kit with FreeRTOS.
- [Marvell MW32x AWS IoT Starter Kit](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_mw32x.html): Get started with the Marvell MW32x AWS IoT Starter Kit using FreeRTOS.
- [MediaTek MT7697Hx development kit](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_mediatek.html): Use the MediaTek MT7697Hx development board with FreeRTOS.
- [Microchip Curiosity PIC32MZ EF](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_mch.html): Use the Microchip Curiosity PIC32MZ EF with FreeRTOS.
- [Nordic nRF52840-DK](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_nordic.html): Get started with the Nordic nRF52840-DK development kit with FreeRTOS.
- [Nuvoton NuMaker-IoT-M487](https://docs.aws.amazon.com/freertos/latest/userguide/getting-started-nuvoton-m487.html): Use the Nuvoton NuMaker-IoT-M487 development board with FreeRTOS.
- [NXP LPC54018 IoT Module](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_nxp.html): Learn how to use the NXP LPC54018 IoT Module with FreeRTOS.
- [Renesas Starter Kit+ for RX65N-2MB](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_renesas.html): Learn how to use the Renesas Starter Kit+ for RX65N-2MB with FreeRTOS.
- [STMicroelectronics STM32L4 Discovery Kit IoT Node](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_st.html): Learn how to use the STMicroelectronics STM32L4 Discovery Kit IoT Node with FreeRTOS:
- [Texas Instruments CC3220SF-LAUNCHXL](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_ti.html): Learn how to use the Texas Instruments CC3220SF-LAUNCHXL with FreeRTOS.
- [Windows Device Simulator](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_windows.html): Learn how to use a Windows Device Simulator with FreeRTOS.
- [Xilinx Avnet MicroZed Industrial IoT Kit](https://docs.aws.amazon.com/freertos/latest/userguide/getting_started_xilinx.html): Learn how to use the Xilinx Avnet MicroZed Industrial IoT Kit with FreeRTOS.
- [Next steps with FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/getting-started-next-steps.html)

### [Over-the-Air Updates](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html)

Learn how to use over-the-air-updates for FreeRTOS Over-the-Air Updates.

### [OTA update prerequisites](https://docs.aws.amazon.com/freertos/latest/userguide/ota-prereqs.html)

Learn about the over-the-air update prerequisites for FreeRTOS.

- [Create an Amazon S3 bucket to store your update](https://docs.aws.amazon.com/freertos/latest/userguide/dg-ota-bucket.html): OTA update files are stored in Amazon S3 buckets.
- [Create an OTA Update service role](https://docs.aws.amazon.com/freertos/latest/userguide/create-service-role.html): The OTA Update service assumes this role to create and manage OTA update jobs on your behalf.
- [Create an OTA user policy](https://docs.aws.amazon.com/freertos/latest/userguide/create-ota-user-policy.html): You must grant your user permission to perform over-the-air updates.

### [Create a code-signing certificate](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert.html)

To digitally sign firmware images, you need a code-signing certificate and private key.

- [Creating a code-signing certificate for the Texas Instruments CC3220SF-LAUNCHXL](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert-ti.html): Create a code-signing certificate for FreeRTOS.
- [Creating a code-signing certificate for the Espressif ESP32](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert-esp.html)
- [Creating a code-signing certificate for the Nordic nrf52840-dk](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert-nordic.html)
- [Creating a code-signing certificate for the FreeRTOS Windows simulator](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert-win.html): The FreeRTOS Windows simulator requires a code-signing certificate with an ECDSA P-256 key and SHA-256 hash to perform OTA updates.
- [Creating a code-signing certificate for custom hardware](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert-other.html): Using an appropriate toolset, create a self-signed certificate and private key for your hardware.
- [Grant access to code signing for AWS IoT](https://docs.aws.amazon.com/freertos/latest/userguide/code-sign-policy.html): Grant access to code signing.
- [Download FreeRTOS with the OTA library](https://docs.aws.amazon.com/freertos/latest/userguide/ota-download-freertos.html): You can clone or download FreeRTOS from GitHub.
- [Prerequisites for OTA updates using MQTT](https://docs.aws.amazon.com/freertos/latest/userguide/ota-mqtt-freertos.html): This section describes the general requirements for using MQTT to perform over-the-air (OTA updates).
- [Prerequisites for OTA updates using HTTP](https://docs.aws.amazon.com/freertos/latest/userguide/ota-http-freertos.html): See the following prerequisites for OTA updates using the HTTP protocol for FreeRTOS.

### [OTA tutorial](https://docs.aws.amazon.com/freertos/latest/userguide/dev-guide-ota-workflow.html)

Learn how to update firmware on devices running FreeRTOS using OTA updates.

### [Installing the initial firmware](https://docs.aws.amazon.com/freertos/latest/userguide/dg-ota-initial-firmware.html)

To update firmware, you must install an initial version of the firmware that uses the OTA Agent library to listen for OTA update jobs.

- [Install the initial version of firmware on the Texas Instruments CC3220SF-LAUNCHXL](https://docs.aws.amazon.com/freertos/latest/userguide/burn-initial-firmware-ti.html)
- [Install the initial version of firmware on the Espressif ESP32](https://docs.aws.amazon.com/freertos/latest/userguide/burn-initial-firmware-esp.html)
- [Install the initial version of firmware on the Nordic nRF52840 DK](https://docs.aws.amazon.com/freertos/latest/userguide/burn-initial-firmware-nordic.html)
- [Initial firmware on the Windows simulator](https://docs.aws.amazon.com/freertos/latest/userguide/burn-initial-firmware-windows.html): When you use the Windows simulator, there is no need to flash an initial version of the firmware.
- [Install the initial version of firmware on a custom board](https://docs.aws.amazon.com/freertos/latest/userguide/burn-initial-firmware-other.html): Using your IDE, build the aws_demos project, making sure to include the OTA library.
- [Update the version of your firmware](https://docs.aws.amazon.com/freertos/latest/userguide/dg-ota-update-firmware.html): The OTA Agent included with FreeRTOS checks the version of any update and installs it only if it is more recent than the existing firmware version.
- [Creating an OTA update (AWS IoT console)](https://docs.aws.amazon.com/freertos/latest/userguide/ota-console-workflow.html)
- [Creating an OTA update with the AWS CLI](https://docs.aws.amazon.com/freertos/latest/userguide/ota-cli-workflow.html): When you use the AWS CLI to create an OTA update, you:
- [OTA Update Manager service](https://docs.aws.amazon.com/freertos/latest/userguide/ota-manager.html): Use the over-the-air update manager service for FreeRTOS.
- [Integrating the OTA Agent into your application](https://docs.aws.amazon.com/freertos/latest/userguide/integrate-ota-agent.html): Integrate the over-the-air agent into your application for FreeRTOS.
- [OTA security](https://docs.aws.amazon.com/freertos/latest/userguide/dev-guide-ota-security.html): Learn about the over-the-air security for FreeRTOS.

### [OTA troubleshooting](https://docs.aws.amazon.com/freertos/latest/userguide/ota-troubleshooting.html)

Troubleshoot OTA issues for FreeRTOS.

- [Set up CloudWatch Logs for OTA updates](https://docs.aws.amazon.com/freertos/latest/userguide/ota-logging.html): The OTA Update service supports logging with Amazon CloudWatch.
- [Log AWS IoT OTA API calls with AWS CloudTrail](https://docs.aws.amazon.com/freertos/latest/userguide/iot-using-cloudtrail-afr.html): FreeRTOS is integrated with CloudTrail, a service that captures AWS IoT OTA API calls and delivers the log files to an Amazon S3 bucket that you specify.
- [Get CreateOTAUpdate failure details using the AWS CLI](https://docs.aws.amazon.com/freertos/latest/userguide/ota-create-failure.html): If the process of creating an OTA update job fails, there may be actions you can take to remedy the problem.
- [Get OTA failure codes with the AWS CLI](https://docs.aws.amazon.com/freertos/latest/userguide/ota-failure-codes.html)
- [Troubleshoot OTA updates of multiple devices](https://docs.aws.amazon.com/freertos/latest/userguide/ota-troubleshooting-multi-thing.html): To perform OTAs on multiple devices (things) using the same firmware image, implement a function (for example getThingName()) that retrieves clientcredentialIOT_THING_NAME from non-volatile memory.
- [Troubleshoot OTA updates with the Texas Instruments CC3220SF Launchpad](https://docs.aws.amazon.com/freertos/latest/userguide/ota-troubleshooting-ti.html): The CC3220SF Launchpad platform provides a software tamper-detection mechanism.

### [FreeRTOS Libraries](https://docs.aws.amazon.com/freertos/latest/userguide/dev-guide-freertos-libraries.html)

Use the FreeRTOS libraries to add functionality to your applications, such as networking and security.

- [backoffAlgorithm](https://docs.aws.amazon.com/freertos/latest/userguide/backoffalgorithm-library.html): Learn about the backoffAlgorithm library for FreeRTOS.

### [Bluetooth Low Energy](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ble-library.html)

Learn how to use the Bluetooth low energy library for FreeRTOS.

- [Mobile SDKs for FreeRTOS Bluetooth devices](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ble-mobile.html): Use the Mobile SDKs for FreeRTOS for bluetooth devices to create mobile applications.
- [Cellular Interface](https://docs.aws.amazon.com/freertos/latest/userguide/cellular-interface.html): Learn how to use the Cellular Interface library with FreeRTOS.
- [Common I/O](https://docs.aws.amazon.com/freertos/latest/userguide/common-io.html): Learn how to use the common I/O hardware abstraction layer for FreeRTOS.
- [AWS IoT Device Defender](https://docs.aws.amazon.com/freertos/latest/userguide/afr-device-defender-library.html): Use the AWS IoT Device Defender library with FreeRTOS to send security metrics from your IoT devices to AWS IoT Device Defender.
- [AWS IoT Greengrass](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-gg-connectivity.html): Learn how to use the AWS IoT Greengrass discovery library with FreeRTOS.
- [coreHTTP](https://docs.aws.amazon.com/freertos/latest/userguide/core-http.html): Use the coreHTTP library for FreeRTOS.
- [coreJSON](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-corejson.html): The coreJSON library for FreeRTOS provides a parser that supports ECMA-404 Standard JSON Data Interchange syntax.
- [coreMQTT](https://docs.aws.amazon.com/freertos/latest/userguide/coremqtt.html): The coreMQTT library is a client implementation of the MQTT standard.
- [coreMQTT Agent](https://docs.aws.amazon.com/freertos/latest/userguide/coremqtt-agent.html): The coreMQTT Agent library is a thread-safe MQTT C client library for small IoT devices (MCU or small MPU).
- [Over the Air (OTA)](https://docs.aws.amazon.com/freertos/latest/userguide/ota-update-library.html): Learn about the over-the-air update library for FreeRTOS.
- [corePKCS11](https://docs.aws.amazon.com/freertos/latest/userguide/security-pkcs.html): Use the Public Key Cryptography Standard #11 (PKCS #11) cryptographic API with FreeRTOS.
- [Secure Sockets](https://docs.aws.amazon.com/freertos/latest/userguide/secure-sockets.html): Learn how to use the Secure Sockets library with FreeRTOS.
- [AWS IoT Device Shadow](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-cloud-shadows.html): Learn how to use the AWS IoT Device Shadow service with FreeRTOS.
- [AWS IoT Jobs](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-jobs.html): Use the AWS IoT Jobs library with FreeRTOS.
- [Transport Layer Security](https://docs.aws.amazon.com/freertos/latest/userguide/security-tls.html): Learn about the FreeRTOS Transport Layer Security interface.
- [Wi-Fi](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-wifi.html): Learn how to use the Wi-Fi library with FreeRTOS:

### [FreeRTOS demos](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-next-steps.html)

Use the FreeRTOS demos applications to learn more about the service.

- [Bluetooth Low Energy](https://docs.aws.amazon.com/freertos/latest/userguide/ble-demo.html): Learn how to use the Bluetooth Low Energy library with FreeRTOS.
- [Bootloader for the Microchip Curiosity PIC32MZEF](https://docs.aws.amazon.com/freertos/latest/userguide/microchip-bootloader.html): Learn how to use the bootloader for the microchip Curiosity PIC32MZEF with FreeRTOS.
- [AWS IoT Device Defender](https://docs.aws.amazon.com/freertos/latest/userguide/dd-demo.html): Use the AWS IoT Device Defender service with FreeRTOS.
- [AWS IoT Greengrass](https://docs.aws.amazon.com/freertos/latest/userguide/gg-demov1.html): Learn how to use the AWS IoT Greengrass discovery demo application with FreeRTOS.
- [AWS IoT Greengrass Version 2](https://docs.aws.amazon.com/freertos/latest/userguide/gg-demov2.html): Learn how to use the AWS IoT Greengrass V2 discovery demo application with FreeRTOS.

### [coreHTTP](https://docs.aws.amazon.com/freertos/latest/userguide/core-http-demo.html)

Use the coreHTTP library to connect to an HTTP server with FreeRTOS.

- [coreHTTP mutual authentication](https://docs.aws.amazon.com/freertos/latest/userguide/core-http-ma-demo.html): Use the coreHTTP library to connect to an HTTP server using TLS with mutual authentication with FreeRTOS.
- [coreHTTP Amazon S3 upload](https://docs.aws.amazon.com/freertos/latest/userguide/core-http-s3-upload-demo.html): Upload files to Amazon S3 with FreeRTOS.
- [coreHTTP S3 download](https://docs.aws.amazon.com/freertos/latest/userguide/core-http-s3-download-demo.html): Download files to Amazon S3 with FreeRTOS.
- [coreHTTP multithreaded](https://docs.aws.amazon.com/freertos/latest/userguide/core-http-bmt-demo.html): Use the coreHTTP library to connect to an HTTP server using a multithreaded application.
- [AWS IoT Jobs](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-jobs-demo.html): Use the AWS IoT Jobs library for FreeRTOS.

### [coreMQTT](https://docs.aws.amazon.com/freertos/latest/userguide/mqtt-demo.html)

Use the coreMQTT library to connect to an MQTT server with FreeRTOS.

- [coreMQTT mutual authentication](https://docs.aws.amazon.com/freertos/latest/userguide/mqtt-demo-ma.html): Learn how to establish a connection to an MQTT broker using TLS with mutual authentication.
- [coreMQTT Agent connection sharing](https://docs.aws.amazon.com/freertos/latest/userguide/mqtt-demo-cs.html): Establish a connection to an MQTT broker using a multithreaded application.

### [Over-the-air updates](https://docs.aws.amazon.com/freertos/latest/userguide/ota-demo.html)

Use the demo application for FreeRTOS to understand the features of the over-the-air library.

- [Over-the-air demo configurations](https://docs.aws.amazon.com/freertos/latest/userguide/ota-demo-specific-config.html): You can use the FreeRTOS over-the-air (OTA) demo configurations.
- [Texas Instruments CC3220SF-LAUNCHXL](https://docs.aws.amazon.com/freertos/latest/userguide/download-ota-ti.html)
- [Microchip Curiosity PIC32MZEF](https://docs.aws.amazon.com/freertos/latest/userguide/download-ota-mchip.html)
- [Espressif ESP32](https://docs.aws.amazon.com/freertos/latest/userguide/download-ota-esp.html)
- [Renesas RX65N](https://docs.aws.amazon.com/freertos/latest/userguide/download-rx65n-ota.html): Run the FreeRTOS OTA demo on the Renesas RX65N.
- [Tutorial: OTA updates on Espressif ESP32 using BLE](https://docs.aws.amazon.com/freertos/latest/userguide/ota-updates-esp32-ble.html)
- [AWS IoT Device Shadow](https://docs.aws.amazon.com/freertos/latest/userguide/shadow-demo.html): Learn how to use the AWS IoT Device Shadow library with FreeRTOS.
- [Secure Sockets](https://docs.aws.amazon.com/freertos/latest/userguide/secure-sockets-demo.html): Learn how to use the Secure Sockets echo client demo with FreeRTOS.
