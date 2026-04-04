# Source: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/llms.txt

# AWS Toolkit for .NET Refactoring User Guide

> Provides a conceptual overview of the Toolkit for .NET Refactoring extension for Microsoft Visual Studio and includes information about how to run a code assessment, port the solution, and test the application on AWS.

- [What is AWS Toolkit for .NET Refactoring?](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.html)
- [AWS .NET Modernization Tools availability change](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-modernization-tools-availability-change.html)
- [Debugging](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/debugging.html)
- [Troubleshooting](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/getting-started-prerequisites.html): The sections below describe the prerequisites that you must verify before you run an assessment with Toolkit for .NET Refactoring.

### [Set up for testing on AWS](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/setup-for-testing.html)

Required configuration, roles, and permissions to run a test deployment on AWS.

- [Prerequisites for testing on AWS](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/test-prerequisites.html): Verify the prerequisites below before you test your application on AWS.
- [Roles and managed policies](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/roles-and-policies.html): To test your application on AWS using Toolkit for .NET Refactoring, you must have the required permissions.
- [Active Directory setup](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/ad-setup.html): The application that you use for the test deployment can use Microsoft Active Directory authentication against its dependencies, such as a Microsoft SQL Server database that is joined into an Active Directory domain.
- [Installation](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-installation.html): You can install Toolkit for .NET Refactoring within Microsoft Visual Studio, or the extension is available as part of license included Visual Studio Amazon Machine Images (AMIs) on Amazon EC2.
- [Pricing](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-pricing.html): The Toolkit for .NET Refactoring extension for Microsoft Visual Studio is available for use at no cost.


## [Toolkit for .NET Refactoring extension](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/toolkit-dotnet-refactoring.html)

- [Run an assessment](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/compatibility-assessment.html): After the extension is installed, you can run a compatibility assessment with Toolkit for .NET Refactoring to find Microsoft Windows dependencies and incompatibilities between your application and newer .NET Core versions.
- [Analyze the results](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/analyze-assessment.html): When the assessment is complete, you can view the results in the dashboard.
- [Port the solution](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/port-solution.html): Toolkit for .NET Refactoring provides the following features to help you port the solution.

### [Test the application](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/test-application-on-aws.html)

After you run the assessment and made code changes, you can run a test deployment to verify the changes to your application on AWS.

- [What is a test deployment?](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/test-deployment.html): A test deployment is a simplified application deployment into AWS that allows you to deploy the application and validate code changes quickly.
- [Create a deployment](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/create-deployment.html): Create a deployment to test your application on AWS.
- [Delete a deployment](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/delete-deployment.html): Toolkit for .NET Refactoring does not delete deployments automatically.


## [Security](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-security.html)

- [AWS Identity and Access Management](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-iam.html): If you use Toolkit for .NET Refactoring with a license included Visual Studio Amazon Machine Image (AMI) on Amazon EC2, you can use the refactoringtoolkit-RefactoringToolkitCallerRole without providing credentials or modifying configuration files.
- [EULA](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/eula.html): AWS Toolkit for .NET Refactoring is licensed as AWS Content under the terms and conditions of the AWS Customer Agreement.
- [Data protection](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Toolkit for .NET Refactoring.
- [AWS managed policies](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Toolkit for .NET Refactoring and recent changes to those policies.
