# Source: https://docs.aws.amazon.com/devicefarm/latest/developerguide/llms.txt

# AWS Device Farm Developer Guide

- [What is AWS Device Farm?](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)
- [Setting up](https://docs.aws.amazon.com/devicefarm/latest/developerguide/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/devicefarm/latest/developerguide/getting-started.html)
- [Tagging in Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/tagging.html)
- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/devicefarm/latest/developerguide/logging-using-cloudtrail.html)
- [Integrating with AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/codepipeline.html)
- [AWS CLI reference](https://docs.aws.amazon.com/devicefarm/latest/developerguide/cli-ref.html)
- [Windows PowerShell reference](https://docs.aws.amazon.com/devicefarm/latest/developerguide/powershell-ref.html)
- [Automating Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/api-ref.html)
- [Limits](https://docs.aws.amazon.com/devicefarm/latest/developerguide/limits.html)
- [Document history](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html)
- [AWS Glossary](https://docs.aws.amazon.com/devicefarm/latest/developerguide/glossary.html)

## [Purchasing device slots](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-purchase-device-slots.html)

- [Cancelling a device slot](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-cancel-device-slots.html): You can cancel the number of device slots for both automated testing and remote access.


## [Concepts](https://docs.aws.amazon.com/devicefarm/latest/developerguide/concepts.html)

- [Devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/devices.html): Learn about device support in AWS Device Farm.
- [Test environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-environments.html): Learn about test environments in AWS Device Farm.
- [Runs](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-runs.html): Learn about testing support in AWS Device Farm.
- [Apps](https://docs.aws.amazon.com/devicefarm/latest/developerguide/apps.html): Learn about app behaviors in AWS Device Farm.
- [Reports](https://docs.aws.amazon.com/devicefarm/latest/developerguide/reports.html): Learn about reports support in AWS Device Farm.
- [Sessions](https://docs.aws.amazon.com/devicefarm/latest/developerguide/sessions.html): Learn about interactive app sessions for Android and iOS apps in AWS Device Farm.


## [Projects](https://docs.aws.amazon.com/devicefarm/latest/developerguide/projects.html)

- [Creating a project](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-project.html): Learn how to create a project in AWS Device Farm.
- [Viewing the projects list](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-view-projects-list.html): Learn how to view a list of available projects in AWS Device Farm.


## [Test runs](https://docs.aws.amazon.com/devicefarm/latest/developerguide/runs.html)

- [Creating a test run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html): Learn how to create a run in Device Farm and verify that the run is complete.
- [Setting execution timeout](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-set-default-timeout-for-test-runs.html): Learn how to set the execution timeout for test runs in AWS Device Farm.
- [Simulating network connections and conditions](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-simulate-network-connections-and-conditions.html): Learn how to create a run that uses network shaping in AWS Device Farm.
- [Stopping a run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-stop-test-runs.html): Learn how to stop a run in AWS Device Farm.
- [Viewing a list of runs](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-view-runs-list.html): Learn how to view a list of runs in AWS Device Farm.
- [Creating a device pool](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-device-pool.html): Learn how to create a device pool in AWS Device Farm.

### [Analyzing results](https://docs.aws.amazon.com/devicefarm/latest/developerguide/analyzing-results.html)

Analyzing test run results.

### [Viewing test reports](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-use-reports.html)

Learn to use test reports in Device Farm.

- [Test result statuses](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-use-reports-displaying-results.html): The Device Farm console displays icons that help you quickly assess the state of your completed test run.

### [Downloading artifacts](https://docs.aws.amazon.com/devicefarm/latest/developerguide/artifacts.html)

Find, view, and download artifacts in Device Farm.

- [Downloading artifacts in a custom test environment](https://docs.aws.amazon.com/devicefarm/latest/developerguide/using-artifacts-custom.html): Download artifacts in a custom test environment.


## [Test frameworks and built-in tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types.html)

### [Automatic Appium tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium.html)

Learn how to bring your Appium tests to run automatically in AWS Device Farm.

- [Integrating with Appium tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium-integrate.html): Learn how to bring your Appium tests to AWS Device Farm.

### [Android tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-tests.html)

Learn about how to use industry-standard test frameworks in AWS Device Farm.

### [Instrumentation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-instrumentation.html)

Learn how to use Instrumentation for Android with AWS Device Farm test types.

- [Integrating with Android instrumentation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-instrumentation-integrate.html): Learn how to use Instrumentation for Android with AWS Device Farm test types.

### [iOS tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-ios-tests.html)

Learn about how to use industry-standard test frameworks in AWS Device Farm.

- [XCTest](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-ios-xctest.html): Learn about how to use XCTest for iOS with AWS Device Farm test types.
- [XCTest UI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-ios-xctest-ui.html): Learn about how to use XCTest UI testing framework for iOS with AWS Device Farm test types.
- [Web app tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-web-app-tests.html): Learn about how to use industry-standard test frameworks for web apps in AWS Device Farm.

### [Built-in tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-built-in-tests.html)

Learn about how to use industry-standard test frameworks in AWS Device Farm.

- [Built-in: fuzz (Android and iOS)](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-built-in-fuzz.html): Learn how to use the built-in fuzz test with Device Farm test types.


## [Custom test environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html)

- [Test spec reference](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-test-spec.html): The test spec syntax.

### [Test host environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts.html)

Device Farm supports a set of operating systems with pre-configured software through the use of a test host environment.

### [Supported software](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software.html)

Device Farm uses host machines that are pre-installed with many of the necessary software libraries to run test frameworks supported on our service, providing a ready testing environment on launch.

- [Using the devicefarm-cli tool in custom test environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software-cli.html): The test host uses a standardized version management tool called devicefarm-cli to select software versions.

### [Android test environment](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-android.html)

Learn about how Amazon Linux 2 works with AWS Device Farm.

- [Supported IP ranges for the Amazon Linux 2 test environment](https://docs.aws.amazon.com/devicefarm/latest/developerguide/amazon-linux-2-ip-ranges.html): Customers often need to know the IP range from which Device Farm's traffic originates, particularly for configuring their firewalls and security settings.

### [iOS test environment](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-ios.html)

Device Farm utilizes Amazon-managed macOS instances (hosts) that dynamically connect to the iOS device during the test run.

- [Migrating to new iOS test host](https://docs.aws.amazon.com/devicefarm/latest/developerguide/ios-host-migration.html): To migrate existing tests from the legacy host to the new macOS test host, you will need to develop new test spec files based on your pre-existing ones.
- [Accessing other AWS resources](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-iam-roles.html): Device Farm supports specifying an IAM role that will be assumed by the custom test runtime environment during test execution.
- [Environment variables](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html): Common environment variables.
- [Best practices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-best-practices.html): The following topics cover recommended best practices for using custom test execution with Device Farm.
- [Migrating tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-migration.html): Migrating Device Farm tests from a standard environment to a custom test environment.

### [Extending custom mode](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-extending.html)

Learn how to configure custom test environments using custom mode.

- [Setting a device PIN](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-extending-set-pin.html): Some applications require that you set a PIN on the device.
- [Speeding up Appium-based tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-extending-speed.html): When using Appium, you might find that the standard mode test suite is very slow.
- [Using Webhooks and other APIs](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-extending-webhooks.html): You can have Device Farm call a webhook after every test suite finishes using curl.
- [Adding extra files to your test package](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-extending-files.html): You may want to use additional files as a part of your tests either as extra configuration files or additional test data.


## [Remote access](https://docs.aws.amazon.com/devicefarm/latest/developerguide/remote-access.html)

- [Creating a session](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-session.html): Learn how to create a remote access session in AWS Device Farm.
- [Using a session](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-use-session.html): Learn how to use a remote access session in AWS Device Farm.
- [Retrieving session results](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-access-session-results.html): Learn how to access logs and captured video of a remote access session in AWS Device Farm.


## [Appium testing](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint.html)

- [Getting started with Appium testing](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-getting-started.html): Learn how to get started with Appium testing in Device Farm
- [Interacting with the device using Appium](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-interaction.html): Learn how to interact with devices using Device Farm's Appium endpoint.
- [Reviewing your Appium server logs](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-server-logs.html): Learn how to view and download Appium server logs in AWS Device Farm.
- [Supported Appium capabilities and commands](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-supported-caps-and-commands.html): Learn about supported and unsupported Appium capabilities and commands in AWS Device Farm.


## [Private devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/working-with-private-devices.html)

- [Creating an instance profile](https://docs.aws.amazon.com/devicefarm/latest/developerguide/set-up-private-devices-account-settings.html): You can set up a fleet that contains one or more private devices.
- [Request additional private devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/managing-private-device-instance.html): In AWS Device Farm, you can request an additional private device instances to be added to your fleet.
- [Creating a test run or remote access session](https://docs.aws.amazon.com/devicefarm/latest/developerguide/create-test-run-using-private-devices.html): In AWS Device Farm, after you set up a private device fleet, you can create test runs or start remote access sessions with one or more private devices in your fleet.
- [Selecting private devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/selecting-private-devices.html): Learn about configuring private devices in device pools in AWS Device Farm.
- [Skipping app re-signing](https://docs.aws.amazon.com/devicefarm/latest/developerguide/skip-app-re-signing-on-private-devices.html): Learn how to skip app re-signing when you create test runs or remote access sessions with private devices.
- [Amazon VPC across Regions](https://docs.aws.amazon.com/devicefarm/latest/developerguide/amazon-vpc-cross-region.html): Learn how to use Amazon VPC across AWS Regions with Device Farm.
- [Terminating private devices in Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/terminate-private-device.html): To terminate a private device after your initial agreed term, you must provide a 30-day notice of non-renewal via our email at aws-devicefarm-support@amazon.com.


## [VPC connectivity](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni.html)

- [AWS access control and IAM](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni-access-control.html): AWS Device Farm allows you to use AWS Identity and Access Management (IAM) to create policies granting or restricting access to Device Farm's features.
- [Service-linked roles](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni-service-linked-role.html): AWS Device Farm uses AWS Identity and Access Management (IAM) service-linked roles.
- [Prerequisites](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni-prerequisites.html): The following list describes some requirements and suggestions to review when creating VPC-ENI configurations:
- [Connecting to Amazon VPC](https://docs.aws.amazon.com/devicefarm/latest/developerguide/connecting-to-amazon-vpc.html): You can configure and update your project to use Amazon VPC endpoints.
- [Limits](https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni-limits.html): The following limitations are applicable to the VPC-ENI feature:
- [Using VPC endpoint services - Legacy](https://docs.aws.amazon.com/devicefarm/latest/developerguide/amazon-vpc-endpoints.html): Learn how to use Amazon VPC endpoint services with Device Farm.


## [Troubleshooting](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting.html)

- [Troubleshooting Android applications](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-android-applications.html): Learn more about Android application errors in Device Farm.
- [Troubleshooting Appium Java JUnit](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-java-junit.html): Learn more about Appium Java JUnit errors in Device Farm.
- [Troubleshooting Appium Java JUnit web](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-web-java-junit-tests.html): Learn more about Appium Java JUnit web app errors in Device Farm.
- [Troubleshooting Appium Java TestNG](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-java-testng.html): Learn about the various Appium errors in Device Farm.
- [Troubleshooting Appium Java TestNG web](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-web-java-testng.html): Learn more about Appium Java TestNG web app errors in Device Farm.
- [Troubleshooting Appium Python](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-python.html): Learn more about Appium Python errors in Device Farm.
- [Troubleshooting Appium Python web](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-web-python.html): The following topic lists error messages that occur during the upload of Appium Python Web application tests and recommends workarounds to resolve each error.
- [Troubleshooting instrumentation tests](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-instrumentation-tests.html): The following topic lists error messages that occur during the upload of Instrumentation tests and recommends workarounds to resolve each error.
- [Troubleshooting iOS applications](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-ios-applications.html): The following topic lists error messages that occur during the upload of iOS application tests and recommends workarounds to resolve each error.
- [Troubleshooting XCTest](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-xctest.html): Learn about the various XCtest errors in Device Farm.
- [Troubleshooting XCTest UI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-xctest-ui.html): Learn about the different XCTest UI test errors and how to fix them.


## [Security](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security.html)

### [Identity and access management](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security-iam.html)

Learn how to provide access permissions to IAM users for AWS Device Farm actions and resources.

- [How AWS Device Farm works with IAM](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Device Farm, you should understand which IAM features are available to use with Device Farm.
- [Identity-based policy examples](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify Device Farm resources.
- [Troubleshooting](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Device Farm and IAM.
- [Compliance validation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/ATP-compliance.html): Learn which AWS services are in scope of a specific compliance program.
- [Data protection](https://docs.aws.amazon.com/devicefarm/latest/developerguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Device Farm.
- [Resilience](https://docs.aws.amazon.com/devicefarm/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about AWS Device Farm features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/devicefarm/latest/developerguide/infrastructure-security.html): Learn how AWS Device Farm isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security-vulnerability-analysis-and-management.html): Device Farm allows you to run software that is not actively maintained or patched by the vendor, such as the OS vendor, hardware vendor, or phone carrier.
- [Incident response](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security-incident-response.html): Device Farm continuously monitors devices for behaviors that might indicate security issues.
- [Logging and monitoring](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security-logging-monitoring.html): This service supports AWS CloudTrail, which is a service that records AWS calls for your AWS account and delivers log files to an Amazon S3 bucket.
- [Security best practices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/security-best-practices.html): Device Farm provides a number of security features to consider as you develop and implement your own security policies.


## [Tools and plugins](https://docs.aws.amazon.com/devicefarm/latest/developerguide/aws-device-farm-tools-plugins.html)

- [Jenkins CI plug-in](https://docs.aws.amazon.com/devicefarm/latest/developerguide/continuous-integration-jenkins-plugin.html): Learn about AWS Device Farm integration with the Jenkins CI
- [Device Farm Gradle plugin](https://docs.aws.amazon.com/devicefarm/latest/developerguide/aws-device-farm-android-gradle-plugin.html): Learn about setting up and using the Device Farm Gradle Plugin for use with the Android Studio build system.
