# Source: https://docs.aws.amazon.com/microservice-extractor/latest/userguide/llms.txt

# AWS Microservice Extractor for .NET User Guide

> AWS Microservice Extractor for .NET is a modernization tool that helps to reduce the time and effort required to break down large, monolithic applications running on the AWS Cloud or on premises into smaller, independent services. These services can be run in containers and be operated and managed independently.

- [AWS .NET Modernization Tools availability change](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/dotnet-modernization-tools-availability-change.html)
- [Security](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-security.html)
- [Troubleshooting](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-troubleshooting.html)
- [Version history](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-version-history.html)
- [Document History](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-doc-history.html)

## [What Is AWS Microservice Extractor for .NET?](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)

- [Primary features](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/drift-features.html): Describes the primary features of AWS Microservice Extractor for .NET.
- [Supported use cases](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-supported-versions.html): Describes use cases supported by AWS Microservice Extractor for .NET.
- [Concepts](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-concepts.html): Provides information to help you understand the AWS Microservice Extractor for .NET tool.
- [Access](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-access.html): AWS Microservice Extractor for .NET is a standalone tool that you download and install on your developer workstation.
- [Pricing](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-pricing.html): AWS Microservice Extractor for .NET is available for use at no cost.


## [How AWS Microservice Extractor for .NET works](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-how-it-works.html)

- [Overview](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-high-level.html): The following are the high-level steps for using AWS Microservice Extractor for .NET to modernize your monolithic application by extracting it into smaller services.
- [Application analysis and extraction](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-application-analysis.html): AWS Microservice Extractor for .NET analyzes the source code of a monolithic application and creates a visualization of the application, which includes nodes, dependencies, call flows, and relevant metrics.
- [Visualization](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-visualization.html): AWS Microservice Extractor for .NET creates a visualization of the monolithic application nodes, the metrics for each node, and the dependencies between them.
- [Runtime profiling](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/drfit-runtime-profiling.html): The AWS Microservice Extractor for .NET tool includes an application runtime profiler to provide call count data with dependency details in the visualization of the application.
- [Service limits](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-limits.html): AWS Microservice Extractor for .NET has the following limits.
- [Information collected](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-information-collected.html): You can choose to share data when you first set up the Microservice Extractor application.


## [Get started](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-get-started.html)

- [Prerequisites](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-prerequisites.html): This section describes the prerequisites for installing and using Microservice Extractor.
- [Install](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-install.html): This topic describes how to install AWS Microservice Extractor for .NET.

### [Use Microservice Extractor](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use.html)

This section contains information to help you get started with AWS Microservice Extractor for .NET after verifying that the required prerequisites are met.

- [Set up](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-set-use-set-up.html): Perform the following steps to set up AWS Microservice Extractor for .NET.
- [Onboard](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-onboard.html): To onboard your application, perform the following steps.
- [View details](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-details.html): When an application is successfully onboarded, you can view details about the application by choosing it from the Applications page.
- [APIs](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-apis.html): You can view which APIs your application utilizes as well as the classes where they are referenced by navigating to the APIs tab after onboarding and analyzing an application.
- [Launch visualization](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-launch.html): After you onboard an application, you can launch the visualization of the application from the Applications page to better conceptualize and group your application nodes.
- [Work with visualization](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-visualization.html): The Visualization tab displays the application nodes and dependencies in graphical format.
- [Extract as independent services](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-extract.html): Review the arrangement of the group or groups you selected and their individual nodes and dependencies on the main view of the Visualization (nodes and dependencies) page.
- [Manually deploy](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-deploy.html): To deploy parts of your application as smaller services, we recommend that you set up the following environment:
- [Failure modes](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-failure-modes.html): What used to be called a function call is now a network call.
- [Remove application](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-remove-application.html): To remove an application from Microservice Extractor, perform the following steps:
- [Edit details](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-edit-application-details.html): To edit the details of an application, perform the following steps.
- [Edit settings](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-edit-user-settings.html): To change your user settings, perform the following steps.
