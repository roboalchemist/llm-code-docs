# Source: https://docs.aws.amazon.com/devicefarm/latest/testgrid/llms.txt

# Device Farm desktop browser testing Guide for Desktop Browser Testing

- [What is Device Farm desktop browser testing?](https://docs.aws.amazon.com/devicefarm/latest/testgrid/what-is-testgrid.html)
- [Tagging in Device Farm](https://docs.aws.amazon.com/devicefarm/latest/testgrid/tagging.html)
- [Troubleshooting](https://docs.aws.amazon.com/devicefarm/latest/testgrid/troubleshooting.html)
- [Quotas](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-limits.html)
- [Document history](https://docs.aws.amazon.com/devicefarm/latest/testgrid/document-history.html)

## [Getting started](https://docs.aws.amazon.com/devicefarm/latest/testgrid/getting-started.html)

- [Migrating from Selenium Grid](https://docs.aws.amazon.com/devicefarm/latest/testgrid/getting-started-migration.html): Learn how to migrate tests from Selenium Grid to the desktop browser testing feature.
- [Migrating from local Selenium WebDrivers](https://docs.aws.amazon.com/devicefarm/latest/testgrid/getting-started-local.html): Learn how to use the desktop browser testing feature with Selenium tests written for the WebDriver framework.


## [Migrating Selenium tests to Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/testing-frameworks.html)

- [JUnit](https://docs.aws.amazon.com/devicefarm/latest/testgrid/testing-frameworks-java.html): Learn how to migrate to Device Farm desktop browser testing in Java tests.
- [Python](https://docs.aws.amazon.com/devicefarm/latest/testgrid/testing-frameworks-python.html): Learn how to migrate Python unit tests to Device Farm desktop browser testing.
- [Node.js](https://docs.aws.amazon.com/devicefarm/latest/testgrid/testing-frameworks-nodejs.html): Learn how to migrate tests written in NodeJS to Device Farm desktop browser testing.
- [Ruby](https://docs.aws.amazon.com/devicefarm/latest/testgrid/testing-frameworks-ruby.html): Learn how to migrate Ruby unit tests to Device Farm desktop browser testing.


## [Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing.html)

### [Projects](https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing-projects.html)

Selenium projects created, organized, and managed separately from native testing projects in Device Farm.

- [Creating a project](https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing-project-create.html): You can use the Device Farm console or the AWS CLI to create a project.
- [Deleting a project](https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing-projects-deleting.html): To delete a project using the AWS CLI, you need the project ARN.
- [Sessions](https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing-sessions.html): Learn how to work with desktop browser testing sessions.
- [Actions](https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing-actions.html): Learn how to use the SDK to work with actions.
- [Artifacts](https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing-artifacts.html): Artifacts are created automatically in Device Farm when your tests perform actions like opening or closing a session.


## [Technical reference](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref.html)

- [Browser support](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-support.html): This topic lists the supported configurations of browsers and operating systems.
- [Limitations](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-limitations.html): Keep these limitations in mind when you use the desktop browser testing feature:
- [API reference](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-api-reference.html): The Device Farm API includes both native application and web application testing.
- [Using Amazon VPC with Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-vpc.html): Device Farm desktop browser testing supports using Amazon VPC to connect your browser testing to a VPC endpoint.


## [Security](https://docs.aws.amazon.com/devicefarm/latest/testgrid/security.html)

- [Access control and IAM](https://docs.aws.amazon.com/devicefarm/latest/testgrid/security-acl-iam.html): Be aware of the following when you use the desktop browser testing feature:
- [Using service-linked roles](https://docs.aws.amazon.com/devicefarm/latest/testgrid/using-service-linked-roles.html): How to use service-linked roles to give Device Farm access to resources in your AWS account.
