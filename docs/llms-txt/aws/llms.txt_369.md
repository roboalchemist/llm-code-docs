# Source: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/llms.txt

# Amazon EMR Amazon EMR Release Guide

> Learn to install, configure, and optimize big-data applications such as Apache Hadoop, Spark, HBase, Presto, Flink, and more using Amazon EMR, the Amazon Web Services (AWS) managed framework for deploying big data solutions in the cloud on dynamically scalable Amazon EC2 instances. Use this guide together with the Amazon EMR Management Guide, which covers cluster planning, configuration, deployment, monitoring, and security.

- [Checking dependencies using the artifact repository](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-artifact-repository.html)
- [Run commands and scripts on a cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-commandrunner.html)
- [AWS Glossary](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/glossary.html)

## [About Amazon EMR Releases](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html)

- [Standard support](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-standard-support.html): Documents the standard support policy in Amazon EMR.

### [Apache Spark Upgrade Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-upgrades.html)

Documents the spark upgrade agent in Amazon EMR.

- [Setup for Upgrade Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-setup.html)
- [Using the Upgrade Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-using.html)
- [Features and Capabilities](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-features.html)
- [Troubleshooting and Q&A](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-troubleshooting.html): Common issues and frequently asked questions about the Apache Spark Upgrade Agent.
- [Spark Upgrade Agent Workflow In Details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-workflow-details.html): To initiate the upgrade process, you will need the Spark application code cloned to your developer environment (locally or EC2 or Amazon SageMaker Unified Studio IDE Spaces), preferably with Git version control initialized.
- [Enable Data Quality Validation](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-data-quality-validation.html): You can enable data quality checks by providing both source and target cluster IDs in your prompt.
- [Prompt Examples for the Spark Upgrade Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-prompt-examples.html): We list a few different prompt examples that can be used in the upgrade process.
- [Creating target EMR Cluster/EMR-S application from existing ones](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-target-cluster.html): If you already have an EMR-EC2 cluster running the source Spark version, you can clone it to create a new cluster with the same configuration but an updated EMR release version to run the validation steps during the Upgrade process.
- [IAM Role Setup](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-iam-role.html): The CloudFormation stack in Setup Instructions automates the IAM role setup for you.
- [VPC Endpoints Configuration](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-upgrade-agent-vpc-endpoints.html): You can establish a private connection between your VPC and Amazon SageMaker Unified Studio MCP service by creating an interface VPC endpoint.
- [Using Spark Upgrade Tools](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-tools.html)
- [Cross-region processing for the Apache Spark Upgrade Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-upgrade-agent-cross-region.html): The Apache Spark Upgrade Agent uses cross-region inference to process natural language requests and generate responses.
- [CloudTrail Logging](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-upgrade-cloudtrail-integration.html): Amazon SageMaker Unified Studio MCP Server is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon SageMaker Unified Studio MCP Server.
- [Service Improvements](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-agent-service-improvements.html): The Apache Spark agent for Amazon EMR may use content, for example, to help the Agent provide better responses to common questions, fix operational issues, or for debugging.

### [Amazon EMR 7.x release versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-7x.html)

Contains application versions, release notes, component versions, and configuration classifications available in each Amazon EMR7.x release version.

- [Application versions in Amazon EMR 7.x releases](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-7.x.html): Contains information about the application versions that are available in each Amazon EMR 7.x release.
- [emr-7.12.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7120-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.12.0.
- [emr-7.11.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7110-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.11.0.

### [emr-7.10.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7100-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.10.0.

- [7.10.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/7100-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.10.0.

### [emr-7.9.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-790-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.9.0.

- [7.9.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/790-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.9.0.

### [emr-7.8.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-780-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.8.0.

- [7.8.0 release components details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-780-release-components-details.html): See the following table for more information about the Extras packages in Amazon EMR 7.7.0.
- [7.8.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/780-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.8.0.

### [emr-7.7.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-770-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.7.0.

- [7.7.0 release components details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-770-release-components-details.html): See the following table for more information about the Extras packages in Amazon EMR 7.7.0.
- [7.7.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/770-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.7.0.

### [emr-7.6.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-760-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.6.0.

- [7.6.0 release components details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-760-release-components-details.html): See the following table for more information about the Extras packages in Amazon EMR 7.6.0.
- [7.6.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/760-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.6.0.

### [emr-7.5.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-750-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.5.0.

- [7.5.0 release components details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-750-release-components-details.html): See the following table for more information about the Extras packages in Amazon EMR 7.5.0.
- [7.5.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/750-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.5.0.

### [emr-7.4.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-740-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.4.0.

- [7.4.0 release components details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-740-release-components-details.html): See the following table for more information about the Extras packages in Amazon EMR 7.4.0.
- [7.4.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/740-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.4.0.

### [emr-7.3.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-730-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.3.0.

- [7.3.0 release components details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-730-release-components-details.html): See the following table for more information about the Extras packages in Amazon EMR 7.3.0.
- [7.3.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/730-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.3.0.

### [emr-7.2.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-720-release.html)

Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.2.0.

- [7.2.0 release components details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-720-release-components-details.html): Lists all of the release components in Amazon EMR 7.2.0, their packages, and package versions.
- [7.2.0 common vulnerabilities and exposures](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/720-common-vulnerabilities-exposures.html): The following table lists all CVEs that don't impact EMR clusters that run on recommended configurations of Amazon EMR 7.2.0.
- [emr-7.1.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-710-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.1.0.
- [emr-7.0.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-700-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 7.0.0.

### [Amazon EMR 6.x release versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-6x.html)

Contains application versions, release notes, component versions, and configuration classifications available in each Amazon EMR6.x release version.

- [Application versions in Amazon EMR 6.x releases](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-6.x.html): Contains information about the application versions that are available in each Amazon EMR 6.x release.
- [emr-6.15.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6150-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.15.0.
- [emr-6.14.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6140-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.14.0.
- [emr-6.13.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6130-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.13.0.
- [emr-6.12.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6120-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.12.0.
- [emr-6.11.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6111-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.11.1.
- [emr-6.11.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6110-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.11.0.
- [emr-6.10.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6101-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.10.1.
- [emr-6.10.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6100-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.10.0.
- [emr-6.9.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-691-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.9.1.
- [emr-6.9.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-690-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.9.0.
- [emr-6.8.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-681-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.8.1.
- [emr-6.8.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-680-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.8.0.
- [emr-6.7.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-670-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.7.0.
- [emr-6.6.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-660-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.6.0.
- [emr-6.5.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-650-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.5.0.
- [emr-6.4.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-640-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.4.0.
- [emr-6.3.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-631-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.3.1.
- [emr-6.3.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-630-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.3.0.
- [emr-6.2.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-621-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.2.1.
- [emr-6.2.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-620-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.2.0.
- [emr-6.1.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-611-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.1.1.
- [emr-6.1.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-610-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.1.0.
- [emr-6.0.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-601-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.0.1.
- [emr-6.0.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-600-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 6.0.0.

### [Amazon EMR 5.x release versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-5x.html)

Contains application versions, release notes, component versions, and configuration classifications available in each Amazon EMR5.x release version.

- [Application versions in Amazon EMR 5.x releases](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-5.x.html): Contains information about the application versions that are available in each Amazon EMR 5.x release.
- [emr-5.36.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5362-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.36.2.
- [emr-5.36.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5361-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.36.1.
- [emr-5.36.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5360-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.36.0.
- [emr-5.35.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5350-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.35.0.
- [emr-5.34.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5340-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.34.0.
- [emr-5.33.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5331-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.33.1.
- [emr-5.33.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5330-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.33.0.
- [emr-5.32.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5321-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.32.1.
- [emr-5.32.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5320-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.32.0.
- [emr-5.31.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5311-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.31.1.
- [emr-5.31.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5310-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.31.0.
- [emr-5.30.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5302-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.30.2.
- [emr-5.30.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5301-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.30.1.
- [emr-5.30.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5300-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.30.0.
- [emr-5.29.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5290-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.29.0.
- [emr-5.28.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5281-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.28.1.
- [emr-5.28.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5280-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.28.0.
- [emr-5.27.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5271-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.27.1.
- [emr-5.27.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5270-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.27.0.
- [emr-5.26.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5260-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.26.0.
- [emr-5.25.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5250-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.25.0.
- [emr-5.24.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5241-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.24.1.
- [emr-5.24.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5240-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.24.0.
- [emr-5.23.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5231-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.23.1.
- [emr-5.23.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5230-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.23.0.
- [emr-5.22.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5220-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.22.0.
- [emr-5.21.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5212-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.21.2.
- [emr-5.21.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5211-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.21.1.
- [emr-5.21.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5210-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.21.0.
- [emr-5.20.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5201-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.20.1.
- [emr-5.20.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5200-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.20.0.
- [emr-5.19.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5191-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.19.1.
- [emr-5.19.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5190-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.19.0.
- [emr-5.18.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5181-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.18.1.
- [emr-5.18.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5180-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.18.0.
- [emr-5.17.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5172-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.17.2.
- [emr-5.17.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5171-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.17.1.
- [emr-5.17.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5170-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.17.0.
- [emr-5.16.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5161-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.16.1.
- [emr-5.16.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5160-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.16.0.
- [emr-5.15.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5151-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.15.1.
- [emr-5.15.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5150-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.15.0.
- [emr-5.14.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5142-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.14.2.
- [emr-5.14.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5141-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.14.1.
- [emr-5.14.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5140-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.14.0.
- [emr-5.13.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5131-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.13.1.
- [emr-5.13.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5130-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.13.0.
- [emr-5.12.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5123-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.12.3.
- [emr-5.12.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5122-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.12.2.
- [emr-5.12.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5121-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.12.1.
- [emr-5.12.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5120-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.12.0.
- [emr-5.11.4](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5114-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.11.4.
- [emr-5.11.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5113-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.11.3.
- [emr-5.11.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5112-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.11.2.
- [emr-5.11.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5111-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.11.1.
- [emr-5.11.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5110-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.11.0.
- [emr-5.10.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5101-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.10.1.
- [emr-5.10.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5100-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.10.0.
- [emr-5.9.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-591-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.9.1.
- [emr-5.9.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-590-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.9.0.
- [emr-5.8.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-583-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.8.3.
- [emr-5.8.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-582-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.8.2.
- [emr-5.8.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-581-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.8.1.
- [emr-5.8.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-580-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.8.0.
- [emr-5.7.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-571-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.7.1.
- [emr-5.7.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-570-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.7.0.
- [emr-5.6.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-561-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.6.1.
- [emr-5.6.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-560-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.6.0.
- [emr-5.5.4](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-554-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.5.4.
- [emr-5.5.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-553-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.5.3.
- [emr-5.5.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-552-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.5.2.
- [emr-5.5.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-551-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.5.1.
- [emr-5.5.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-550-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.5.0.
- [emr-5.4.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-541-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.4.1.
- [emr-5.4.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-540-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.4.0.
- [emr-5.3.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-532-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.3.2.
- [emr-5.3.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-531-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.3.1.
- [emr-5.3.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-530-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.3.0.
- [emr-5.2.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-523-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.2.3.
- [emr-5.2.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-522-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.2.2.
- [emr-5.2.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-521-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.2.1.
- [emr-5.2.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-520-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.2.0.
- [emr-5.1.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-511-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.1.1.
- [emr-5.1.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-510-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.1.0.
- [emr-5.0.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-503-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.0.3.
- [emr-5.0.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-502-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.0.2.
- [emr-5.0.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-501-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.0.1.
- [emr-5.0.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-500-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 5.0.0.

### [Amazon EMR 4.x release versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-4x.html)

Contains application versions, release notes, component versions, and configuration classifications available in each Amazon EMR4.x release version.

- [Application versions in Amazon EMR 4.x releases](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-4.x.html): Contains information about the application versions that are available in each Amazon EMR 4.x release.

### [Release version differences](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-differences-4x.html)

Documentation for Amazon EMR features in the Amazon EMR Management Guide specify the Amazon EMR release version that a feature became available, as well as applicable differences between Amazon EMR features dating back to 4.0.0.

- [Sandbox applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-sandbox-apps-4x.html): When using Amazon EMR 4.x release versions, some applications are considered sandbox applications.
- [Considerations for using Hive on Amazon EMR 4.x](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-Hive-4x.html): This section covers differences to consider when using Hive version 1.0.0 on Amazon EMR 4.x release versions, as compared to Hive 2.x on Amazon EMR 5.x release versions.
- [Considerations for using Pig on Amazon EMR 4.x](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-Pig-4x.html): Pig version 0.14.0 is installed on clusters created using Amazon EMR 4.x release versions.
- [emr-4.9.6](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-496-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.9.6.
- [emr-4.9.5](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-495-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.9.5.
- [emr-4.9.4](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-494-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.9.4.
- [emr-4.9.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-493-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.9.3.
- [emr-4.9.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-492-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.9.2.
- [emr-4.9.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-491-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.9.1.
- [emr-4.8.5](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-485-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.8.5.
- [emr-4.8.4](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-484-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.8.4.
- [emr-4.8.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-483-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.8.3.
- [emr-4.8.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-482-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.8.2.
- [emr-4.8.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-481-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.8.1.
- [emr-4.8.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-480-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.8.0.
- [emr-4.7.4](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-474-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.7.4.
- [emr-4.7.3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-473-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.7.3.
- [emr-4.7.2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-472-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.7.2.
- [emr-4.7.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-471-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.7.1.
- [emr-4.7.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-470-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.7.0.
- [emr-4.6.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-461-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.6.1.
- [emr-4.6.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-460-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.6.0.
- [emr-4.5.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-450-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.5.0.
- [emr-4.4.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-440-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.4.0.
- [emr-4.3.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-430-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.3.0.
- [emr-4.2.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-420-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.2.0.
- [emr-4.1.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-410-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.1.0.
- [emr-4.0.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-400-release.html): Lists application versions, release notes, component versions, and configuration classifications available in Amazon EMR 4.0.0.

### [2.x and 3.x AMI versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-3x.html)

Differences between more recent Amazon EMR releases and 2.x and 3.x AMI versions.

- [Creating a cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-create.html): Amazon EMR 2.x and 3.x releases are referenced by AMI version.
- [Installing applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-install-apps.html): Guidance for installing applications when using 2.x and 3.x AMI versions of Amazon EMR.
- [Customizing configurations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-customizeappconfig.html): Amazon EMR release version 4.0.0 introduced a simplified method of configuring applications using configuration classifications.
- [Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-hive.html)
- [HBase](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-hbase.html)
- [Pig](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-pig.html): Guidance for using Pig in 2.x and 3.x AMI version of Amazon EMR.
- [Spark](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-spark.html)
- [S3DistCp](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-3x-s3distcp.html)


## [What's new?](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html)

- [Approach to mitigate CVE-2021-44228](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-log4j-vulnerability.html): Approach to mitigate CVE-2021-44228.
- [Archive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew-history.html): Release notes for all Amazon EMR releases are available below.


## [Configure applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html)

- [Configure applications when you create a cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps-create-cluster.html): Configure applications for Amazon EMR when you create a cluster.
- [Reconfigure an instance group in a running cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps-running-cluster.html): Reconfigure applications in a running Amazon EMR cluster, and troubleshoot reconfiguration issues.
- [Store sensitive configuration data in AWS Secrets Manager](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/storing-sensitive-data.html): The Amazon EMR describe and list API operations that emit custom configuration data (such as DescribeCluster and ListInstanceGroups) do so in plaintext.
- [Configure applications to use a specific Java Virtual Machine](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/configuring-java8.html): Override or customize the default Java Virtual Machine (JVM) for Amazon EMR cluster instances.


## [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs.html)

### [Consistent view](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-plan-consistent-view.html)

How to turn off consistent view for EMRFS

- [Enable consistent view](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/enable-consistent-view.html): You can enable Amazon S3 server-side encryption or consistent view for EMRFS using the AWS Management Console, AWS CLI, or the emrfs-site configuration classification.
- [Understanding how EMRFS consistent view tracks objects in Amazon S3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrfs-files-tracked.html): EMRFS creates a consistent view of objects in Amazon S3 by adding information about those objects to the EMRFS metadata.
- [Retry logic](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrfs-retry-logic.html): EMRFS tries to verify list consistency for objects tracked in its metadata for a specific number of retries.
- [EMRFS consistent view metadata](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrfs-metadata.html): EMRFS consistent view tracks consistency using a DynamoDB table to track objects in Amazon S3 that have been synced with or created by EMRFS.
- [Configure consistency notifications for CloudWatch and Amazon SQS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrfs-configure-sqs-cw.html): You can enable CloudWatch metrics and Amazon SQS messages in EMRFS for Amazon S3 eventual consistency issues.
- [Configure consistent view](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrfs-configure-consistent-view.html): You can configure additional settings for consistent view by providing them using configuration properties for emrfs-site properties.
- [EMRFS CLI Command Reference](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrfs-cli-reference.html): The EMRFS CLI is installed by default on all cluster master nodes created using Amazon EMR release version 3.2.1 or later.
- [Authorizing access to EMRFS data in Amazon S3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-plan-credentialsprovider.html): By default, the EMR role for EC2 determines the permissions for accessing EMRFS data in Amazon S3.
- [Managing the default AWS Security Token Service endpoint](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-emrfs-sts-endpoint.html): Manage the AWS STS endpoint used by EMRFS to request security credentials.

### [Specifying Amazon S3 encryption using EMRFS properties](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-emrfs-encryption.html)

Learn how to apply settings for data encryption in Amazon EMR using cluster configuration objects.

- [Amazon S3 client-side encryption](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-emrfs-encryption-cse.html): With Amazon S3 client-side encryption, the Amazon S3 encryption and decryption takes place in the EMRFS client on your cluster.


## [S3A file system](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-file.html)

- [S3A MagicV2 Committer](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/s3a-magicv2-committer.html): With the EMR-6.15.0 release, Amazon EMR introduces a new S3A committer type known as the MagicV2 committer.
- [Migration Guide: EMRFS to S3A Filesystem](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-migrate.html): Starting with the EMR-7.10.0 release, S3A Filesystem is the default filesystem/s3 connector for EMR clusters for all S3 file schemes, including the following:


## [Amazon S3 client-side encryption with S3A](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a.html)

- [Setup CSE-KMS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-cse-kms.html): Enable client-side encryption using AWS KMS
- [Setup CSE-CUSTOM](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-cse-custom.html): To use CSE-CUSTOM, you must create a custom key provider by implementing the Keyring interface.
- [Properties for Amazon S3 client-side encryption with S3A](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-encryption-s3a-properties.html): To configure client-side encryption with S3A, there are several configuration properties that must be set in your core-site.xml settings.


## [Amazon CloudWatch agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-AmazonCloudWatchAgent.html)

- [Create a cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-create.html): The procedures in this section describe the steps to create a cluster in Amazon EMR with Amazon CloudWatch agent from the AWS Management Console and the AWS CLI.
- [Default metrics](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-metrics.html): When you install the Amazon CloudWatch agent on Amazon EMR, the default configuration publishes the following system metrics for all of the instances in your cluster unless you configure the agent differently.

### [Configuration](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-config.html)

Amazon EMR 7.0.0 and higher include the Amazon CloudWatch agent.

- [Amazon EMR 7.1.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-config-710.html): Configure CloudWatch agent to work with Amazon EMR 7.1.0.
- [Amazon EMR 7.0.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-config-700.html): Configure CloudWatch agent to work with Amazon EMR 7.0.0.
- [Considerations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-considerations.html): Considerations for using native CloudWatch agent with Amazon EMR.
- [History](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-release-history.html): The following table lists the version of AmazonCloudWatchAgent included in each release version of Amazon EMR, along with the components installed with the application.


## [Delta Lake](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-delta.html)

- [Introduction](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltaintro.html): Delta Lake is an open-source project that helps implement modern data lake architectures commonly built on Amazon S3.

### [Using Delta Lake clusters](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltausing-cluster.html)

- [Delta Lake with Flink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltacluster-flink.html): With Amazon EMR release 6.11 and higher, you can use Delta Lake with your Flink cluster.
- [Delta Lake with Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltacluster-trino.html): With Amazon EMR releases 6.9.0 and higher, you can use Delta Lake with your Trino cluster.
- [Delta Lake with Spark](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltausing-cluster-spark.html): Starting with Amazon EMR version 6.9.0, you can use Delta Lake with your Spark cluster without the need for bootstrap actions.
- [Delta Lake with Spark and Glue](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltacluster-spark-glue.html): To use the AWS Glue Catalog as the Metastore for Delta Lake tables, create a cluster with following steps.
- [Considerations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltaconsiderations-limitations.html)
- [History](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Delta-release-history.html): The following table lists the version of Delta included in each release version of Amazon EMR, along with the components installed with the application.


## [Flink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-flink.html)

- [Creating a cluster with Flink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-create-cluster.html): You can launch a cluster with the AWS Management Console, AWS CLI, or an AWS SDK.
- [Configure Flink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-configure.html)
- [Flink jobs](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-jobs.html): There are several ways to interact with Flink on Amazon EMR: through the console, the Flink interface found on the ResourceManager Tracking UI, and at the command line.
- [Flink Scala shell](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-scala.html): The Flink Scala shell for EMR clusters is only configured to start new YARN sessions.
- [Flink UI](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-web-interface.html): The Application Master that belongs to the Flink application hosts the Flink web interface.
- [Flink autoscaler](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-autoscaler.html): The Flink autoscaler automatically adjusts parallelism to autoscale complex streaming applications.
- [Optimize restart times](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-restart.html): Amazon EMR Flink can improve the job restart time during task recovery or scaling operations.
- [Flink with Zeppelin](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-zeppelin.html)

### [Flink release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history.html)

The following table lists the version of Flink included in each release version of Amazon EMR, along with the components installed with the application.

### [Flink release notes by version](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-versions.html)

See the following sections for the full release notes.

- [Amazon EMR 7.10.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-7100.html): Amazon EMR 7.10.0 - Flink Changes
- [Amazon EMR 7.9.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-790.html): Amazon EMR 7.9.0 - Flink Changes
- [Amazon EMR 7.8.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-780.html): Configuration â EMR Flink works out of the box with S3A in all AWS regions/partitions.
- [Amazon EMR 7.7.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-770.html)
- [Amazon EMR 7.6.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-760.html)
- [Amazon EMR 7.5.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-750.html)
- [Amazon EMR 7.4.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-740.html)
- [Amazon EMR 7.3.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-730.html)
- [Amazon EMR 7.2.0 - Flink release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-720.html)


## [Ganglia](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-ganglia.html)

- [Create a cluster with Ganglia](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/init_Ganglia.html)
- [View Ganglia metrics](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/view_Ganglia.html)
- [Hadoop and Spark metrics in Ganglia](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoopmetrics_Ganglia.html)
- [Ganglia release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Ganglia-release-history.html)


## [Hadoop](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop.html)

### [Configure Hadoop](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-config.html)

The following sections give default configuration settings for Hadoop daemons, tasks, and HDFS.

- [Task configuration](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-task-config.html): Configure task-related settings to tune the performance of MapReduce jobs.
- [Hadoop daemon configuration settings](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-daemons.html): Hadoop daemon settings are different depending on the EC2 instance type that a cluster node uses.
- [HDFS configuration](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hdfs-config.html): The following table describes the default Hadoop Distributed File System (HDFS) parameters and their settings.
- [Transparent encryption in HDFS on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-encryption-tdehdfs.html): Learn how to apply settings for transparent data encryption for HDFS with Amazon EMR.

### [Create or run a Hadoop application](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-application.html)

- [Build binaries using Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-build-binaries.html): Build binaries using Amazon Elastic MapReduce to compile programs for use in your cluster.

### [Process data with streaming](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/UseCase_Streaming.html)

Process data with Hadoop streaming, a utility that comes with Hadoop that enables you to develop MapReduce executables in languages other than Java.

- [Submit a streaming step](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/CLI_CreateStreaming.html): Learn the basics of launching a cluster and running a streaming application using Amazon EMR.

### [Process data with a custom JAR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/UseCase_CustomJar.html)

Process data with a custom JAR that runs a compiled Java program to upload to Amazon S3.

- [Submit a custom JAR step](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-launch-custom-jar-cli.html): Learn the basics of creating a cluster using a custom JAR file in Amazon EMR.
- [Read restored objects](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-read-restore-objects.html): With Amazon EMR release 7.2.0 and higher, you can read restored Glacier objects from the S3 location of the table with the S3A protocol.
- [Turn on non-uniform memory access awareness for YARN containers](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hadoop-numa.html): With Amazon EMR versions 6.x and later, you can use non-uniform memory access (NUMA) for multiprocessing your data on clusters.
- [YARN container bin packing](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-container-yarn.html): Information about YARN container bin-packing policy for Amazon EMR version 7.9.0 and later.

### [Hadoop version history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history.html)

The following table lists the version of Hadoop included in each release version of Amazon EMR, along with the components installed with the application.

### [Hadoop release notes by version](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-versions.html)

- [Amazon EMR 7.10.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-7100.html)
- [Amazon EMR 7.9.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-790.html)
- [Amazon EMR 7.8.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-780.html)
- [Amazon EMR 7.7.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-770.html)
- [Amazon EMR 7.6.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-760.html)
- [Amazon EMR 7.5.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-750.html)
- [Amazon EMR 7.4.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-740.html)
- [Amazon EMR 7.3.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-730.html)
- [Amazon EMR 7.2.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-720.html)
- [Amazon EMR 6.6.0 - Hadoop release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-660.html)


## [HBase](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase.html)

- [Creating a cluster with HBase](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-create.html): The procedures in this section cover the basics of launching a cluster using the AWS Management Console and the AWS CLI.
- [HBase on Amazon S3 (Amazon S3 storage mode)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-s3.html): Learn to use HBase on Amazon S3 with Amazon EMR.

### [Write-ahead logs (WAL) for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal.html)

Write your Apache HBase write-ahead logs (WAL) to the Amazon EMR WAL service

- [WAL workspaces](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-workspaces.html): Each write-ahead log in Amazon EMR WAL are encapsulated by a WAL workspace.
- [Required permissions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-permissions.html): For your cluster to connect to Amazon EMR WAL, the instance profile for the cluster requires certain IAM permissions:
- [Enabling WAL](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-enabling.html): Enable writing to the Amazon EMR WAL when you create a cluster with the AWS Command Line Interface.
- [Restoring from WAL](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-restoring.html): You can reuse the WAL workspace for a cluster with a newly-created cluster within 30 days.
- [Security configurations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-security.html): Use a security configuration to bring your own keys from AWS Key Management Service (KMS) service and encrypt the data that you store in Amazon EMR WAL.
- [Using AWS PrivateLink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-privatelink.html): Use AWS PrivateLink to privately connect to Amazon EMR WAL.
- [WAL pricing and metrics](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-metrics.html): Understanding Amazon EMR WAL metrics
- [Tagging WAL workspaces](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-tagging.html): Add, remove, or list tags from an active Amazon EMR WAL workspace.
- [EMR WAL cross-cluster replication](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-cross-cluster.html): EMR WAL cross-cluster replication.
- [Considerations and availability](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal-considerations.html): Important considerations and limitations of Amazon EMR WAL.
- [EMRWAL CLI reference](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrwalcli-ref.html): EMRWAL CLI command reference guide.
- [Using the HBase shell](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-connect.html): Connect to an HBase cluster using the command line so you can begin reading and writing data.
- [Access HBase tables with Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-access-hive.html): Access HBase data with Hive running on separate clusters to improve performance.
- [Using HBase snapshots](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-snapshot.html): HBase uses a built-in snapshot functionality to create lightweight backups of tables.
- [Configure HBase](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-configure.html): Configure your HBase setting if you want to modify the default settings, although most applications will work with the default settings.
- [View the HBase user interface](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hbase-web-ui.html): View the HBase user interface to monitor your HBase cluster.
- [View HBase log files](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-log-files.html): View the HBase log files to help you track performance and debug issues.
- [Monitor HBase with Ganglia](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-ganglia.html): Monitor your HBase with Ganglia, a scalable, distributed system that monitors clusters and grids while minimizing the impact on their performance.

### [Monitoring EMR HBase with Amazon CloudWatch](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-cw.html)

Amazon EMR provides the Amazon CloudWatch Agent to send metrics to CloudWatch or Prometheus.

- [Set up metrics](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-setting-up-metrics.html): To monitor the HBase Master, you can set up Amazon CloudWatch Agent to collect specific metrics.
- [Using the Metrics Destination](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-using-metrics.html): You have the option to send your metrics data to Amazon CloudWatch or Amazon Managed Service for Prometheus
- [Migrating from previous HBase versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-migrate.html): To migrate data from a previous HBase version, see Upgrading and HBase version number and compatibility in the Apache HBase Reference Guide.

### [HBase release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/HBase-release-history.html)

The following table lists the version of HBase included in each release version of Amazon EMR, along with the components installed with the application.

- [7.9.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/HBase-release-history-changes-790.html): HBase changes:


## [HCatalog](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hcatalog.html)

- [Creating a cluster with HCatalog](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hcatalog-create-cluster.html): Although HCatalog is included in the Hive project, you must install it as its own application.
- [Using HCatalog](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hcatalog-using.html): You can use HCatalog within various applications that use the Hive metastore.
- [Example: Create an HCatalog table and write to it using Pig](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hcatalog-pig.html): You can create an HCatalog table and use Apache Pig to write to it by way of HCatStorer using a data source in Amazon S3.
- [HCatalog release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/HCatalog-release-history.html): The following table lists the version of HCatalog included in each release version of Amazon EMR, along with the components installed with the application.


## [Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive.html)

- [Differences and considerations for Hive on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-differences.html): Describes the differences between different versions of Apache Hive on Amazon EMR and default Apache Hive.

### [Configure an external metastore for Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-metastore-external-hive.html)

Create a metastore located outside of the cluster so the data persists when a cluster terminates.

- [Using the AWS Glue Data Catalog as the metastore for Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-metastore-glue.html): Using Amazon EMR release 5.8.0 or later, you can configure Hive to use the AWS Glue Data Catalog as its metastore.
- [Using an external MySQL database or Amazon Aurora](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-metastore-external.html): To use an external MySQL database or Amazon Aurora as your Hive metastore, you override the default configuration values for the metastore in Hive to specify the external database location, either on an Amazon RDS MySQL instance or an Amazon Aurora PostgreSQLinstance.
- [Use the Hive JDBC driver](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/HiveJDBCDriver.html): Use the Hive JDBC driver to connect to Hive and query data.

### [Improve Hive performance](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-s3-performance.html)

Amazon EMR offers features to help optimize performance when using Hive to query, read and write data saved in Amazon S3.

- [Enabling Hive EMRFS S3 optimized committer](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hive-optimized-committer.html): The Hive EMRFS S3 Optimized Committer is an alternative way using which EMR Hive writes files for insert queries when using EMRFS.
- [Using S3 Select](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-s3select.html)
- [MSCK Optimization](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-msck-optimization.html): Hive stores a list of partitions for each table in its metastore.
- [Use Hive LLAP](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-llap.html): Amazon EMR 6.0.0 supports the Live Long and Process (LLAP) functionality for Hive.

### [Encryption in Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hive-encryption.html)

This section describes the encryption types Amazon EMR supports.

- [Parquet modular encryption in Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hive-parquet-modular-encryption.html): Parquet modular encryption provides columnar level access control and encryption to enhance privacy and data integrity for data stored in Parquet file format.
- [In-transit encryption in HS2](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hs2-encryption-intransit.html): HS2 is TLS/SSL enabled as part of in-transit encryption security configuration.

### [Hive release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history.html)

The following table lists the version of Hive included in each release version of Amazon EMR, along with the components installed with the application.

### [Hive release notes by version](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-versions.html)

- [7.10.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-7100.html)
- [7.9.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-790.html)
- [7.8.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-780.html)
- [7.7.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-770.html)
- [7.6.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-760.html)
- [7.5.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-750.html)
- [7.4.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-740.html)
- [7.3.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-730.html)
- [7.2.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-720.html)
- [7.1.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-710.html)
- [7.0.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-700.html)
- [6.15.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-6150.html)
- [6.14.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-6140.html)
- [6.13.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-6130.html)
- [6.12.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-6120.html)
- [6.11.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-6110.html)
- [6.10.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-6100.html)
- [6.9.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-690.html)
- [6.8.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-680.html)
- [6.7.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-670.html)
- [6.6.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-660.html)


## [Hudi](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi.html)

- [How Hudi works](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi-how-it-works.html): When using Hudi with Amazon EMR, you can write data to the dataset using the Spark Data Source API or the Hudi DeltaStreamer utility.
- [Considerations and limitations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi-considerations.html)
- [Create a cluster with Hudi installed](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi-installation-and-configuration.html): With Amazon EMR release version 5.28.0 and later, Amazon EMR installs Hudi components by default when Spark, Hive, or Presto is installed.
- [Work with a Hudi dataset](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi-work-with-dataset.html): Hudi supports inserting, updating, and deleting data in Hudi datasets through Spark.
- [Use the Hudi CLI](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi-cli.html): You can use the Hudi CLI to administer Hudi datasets to view information about commits, the filesystem, statistics, and more.
- [Hudi release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hudi-release-history.html): The following table lists the version of Hudi included in each release version of Amazon EMR, along with the components installed with the application.


## [Hue](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hue.html)

- [Supported and unsupported features of Hue on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hue-supported-features.html): With Amazon EMR 7.0.0 and higher, Hue requires Python 3.9 or higher.
- [Considerations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hue-considerations.html): Consider the following limitations when you use Hue on Amazon EMR.
- [Connecting to the Hue web user interface](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/accessing-hue.html): Connecting to the Hue web user interface is the same as connecting to any HTTP interface hosted on the master node of a cluster.
- [Using Hue with a remote database in Amazon RDS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hue-rds.html): By default, Hue user information and query histories are stored in a local MySQL database on the master node.

### [Advanced configurations for Hue](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/advanced-configurations.html)

This section includes the following topics.

- [Configure Hue for LDAP users](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/hue-ldap.html): Integration with LDAP allows users to log into Hue using existing credentials stored in an LDAP directory.
- [Hue release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hue-release-history.html): The following table lists the version of Hue included in each release version of Amazon EMR, along with the components installed with the application.


## [Iceberg](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg.html)

- [How Iceberg works](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-how-it-works.html): Describes Apache Iceberg features implemented on Amazon EMR 6.5.0 and later.

### [Use an Iceberg cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)

Procedures and example syntax for creating an Amazon EMR cluster and installing Iceberg by using the AWS CLI or the Amazon EMR API.

- [Use an Iceberg cluster with Spark](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-spark-cluster.html): Starting with Amazon EMR version 6.5.0, you can use Iceberg with your Spark cluster with no requirement to include bootstrap actions.
- [Use an Iceberg cluster with Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-trino-cluster.html): Starting with Amazon EMR version 6.6.0, you can use Iceberg with your Trino cluster.
- [Use an Iceberg cluster with Flink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-flink-cluster.html): Starting with Amazon EMR version 6.9.0, you can use Iceberg with a Flink cluster without the setup steps required when using the open source Iceberg Flink Integration.
- [Use an Iceberg cluster with Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-hive-cluster.html): With Amazon EMR releases 6.9.0 and higher, you can use Iceberg with a Hive cluster without having to perform the setup steps that are required for Open Source Iceberg Hive Integration.

### [Iceberg release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Iceberg-release-history.html)

Iceberg versions and components.

### [Iceberg release notes by version](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Iceberg-release-history-versions.html)

- [Amazon EMR 6.9.0 - Iceberg release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Iceberg-release-history-690.html)


## [Jupyter Notebook](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyter.html)

- [EMR Studio](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-studio-jupyter.html): Amazon EMR Studio is a web-based integrated development environment (IDE) for fully managed Jupyter notebooks that run on Amazon EMR clusters.
- [EMR Notebook](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyter-emr-managed-notebooks.html): Use EMR Notebooks to quickly create Jupyter notebooks that you can attach to Amazon EMR clusters to remotely execute queries and code.

### [JupyterHub](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub.html)

Use JupyterHub on Amazon EMR to host multiple instances of a single-user Jupyter notebook server for multiple users.

- [Create a cluster with JupyterHub](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-launch.html): You can create an Amazon EMR cluster with JupyterHub using the AWS Management Console, AWS Command Line Interface, or the Amazon EMR API.
- [Considerations when using JupyterHub on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-considerations.html): Consider the following when using JupyterHub on Amazon EMR.
- [Configuring JupyterHub](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-configure.html): You can customize the configuration of JupyterHub on Amazon EMR and individual user notebooks by connecting to the cluster master node and editing configuration files.
- [Configuring persistence for notebooks in Amazon S3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-s3.html): You can configure a JupyterHub cluster in Amazon EMR so that notebooks saved by a user persist in Amazon S3, outside of ephemeral storage on cluster EC2 instances.
- [Connecting to the master node and Notebook servers](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-connect.html): JupyterHub administrators and notebook users must connect to the cluster master node using an SSH tunnel and then connecting to web interfaces served by JupyterHub on the master node.
- [JupyterHub configuration and administration](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-administer.html): JupyterHub and related components run inside a Docker container named jupyterhub that runs the Ubuntu operating system.

### [Adding Jupyter Notebook users and administrators](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-user-access.html)

You can use one of two methods for users to authenticate to JupyterHub so that they can create notebooks and, optionally, administer JupyterHub.

- [Using PAM authentication](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-pam-users.html): Creating PAM users in JupyterHub on Amazon EMR is a two-step process.
- [Using LDAP authentication](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-ldap-users.html): Lightweight Directory Access Protocol (LDAP) is an application protocol for querying and modifying objects that correspond to resources such as users and computers stored in an LDAP-compatible directory service provider such as Active Directory or an OpenLDAP server.
- [User impersonation](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-user-impersonation.html): A Spark job running inside a Jupyter notebook traverses multiple applications during its execution on Amazon EMR.
- [Installing additional kernels and libraries](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-install-kernels-libs.html): When you create a cluster with JupyterHub on Amazon EMR, the default Python 3 kernel for Jupyter along with the PySpark and Spark kernels for Sparkmagic are installed on the Docker container.
- [JupyterHub release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/JupyterHub-release-history.html): The following table lists the version of JupyterHub included in each release version of Amazon EMR, along with the components installed with the application.


## [Livy](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-livy.html)

- [Enabling HTTPS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/enabling-https.html): This topic is relevant if you are running Amazon EMR 7.3.0 or an earlier release.
- [Livy release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Livy-release-history.html): The following table lists the version of Livy included in each release version of Amazon EMR, along with the components installed with the application.


## [MXNet](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-mxnet.html)

- [MXNet release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/MXNet-release-history.html): The following table lists the version of MXNet included in each release version of Amazon EMR, along with the components installed with the application.


## [Oozie](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-oozie.html)

- [Using Oozie with a remote database in Amazon RDS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/oozie-rds.html): By default, Oozie user information and query histories are stored in a local MySQL database on the master node.
- [Configure Java version for Oozie](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/oozie-java.html): Oozie runs multiple Java Virtual Machine (JVM) processes.

### [Oozie release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history.html)

The following table lists the version of Oozie included in each release version of Amazon EMR, along with the components installed with the application.

### [Oozie release notes by version](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-versions.html)

- [7.10.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-7100.html): Oozie known issues:
- [7.9.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-790.html): Oozie changes:
- [7.6.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-760.html): Oozie known issues:
- [7.5.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-750.html)
- [7.4.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-740.html): Oozie changes : NO CHANGES
- [7.3.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-730.html)
- [7.1.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-710.html)
- [7.0.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-700.html)


## [Phoenix](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-phoenix.html)

- [Creating a cluster with Phoenix](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/phoenix-create-cluster.html): You install Phoenix by choosing the application when you create a cluster in the console or using the AWS CLI.
- [Phoenix clients](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-phoenix-clients.html): You connect to Phoenix using either a JDBC client built with full dependencies or using the "thin client" that uses the Phoenix Query Server and can only be run on a master node of a cluster (e.g. by using an SQL client, a step, command line, SSH port forwarding, etc.).
- [Phoenix release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Phoenix-release-history.html): The following table lists the version of Phoenix included in each release version of Amazon EMR, along with the components installed with the application.


## [Pig](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-pig.html)

- [Submit Pig work](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-pig-launch.html): Create and launch a cluster using Pig in Amazon EMR using the console, CLI, or API.
- [Call user-defined functions from Pig](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-pig-udf.html): Call user-defined functions from within Pig scripts to implement custom processing.
- [Pig release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Pig-release-history.html): The following table lists the version of Pig included in each release version of Amazon EMR, along with the components installed with the application.


## [Presto](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto.html)

- [Using Presto with the AWS Glue Data Catalog](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto-glue.html): Using Amazon EMR release version 5.10.0 and later, you can specify the AWS Glue Data Catalog as the default Hive metastore for Presto.
- [Using S3 Select Pushdown](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto-s3select.html)
- [Adding database connectors](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/presto-adding-db-connectors.html): You can use configuration classifications to configure JDBC connector properties when you create a cluster.

### [Using SSL/TLS and LDAPS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/presto-ssl.html)

With Amazon EMR release version 5.6.0 and later, you can enable SSL/TLS to help secure internal communication between Presto nodes.

- [Using LDAP authentication](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto-ldap.html): Follow the steps in this section to configure LDAP.
- [Activating Presto strict mode](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/presto-strict-mode.html): In certain situations, long-running queries can lead to high costs and cause Amazon EMR to use more cluster resources.
- [Handling Spot Instance loss in Presto](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/presto-spot-loss.html): With Spot Instances in Amazon EMR, you can run big data workloads on spare Amazon EC2 capacity at a reduced cost.
- [Using Presto automatic scaling with Graceful Decommission](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/presto-graceful-autoscale.html): Amazon EMR release versions 5.30.0 and later include a feature you can use to set a grace period for certain scaling actions.
- [Considerations with Presto on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto-considerations.html): Consider the following limitations when you run Presto on Amazon EMR.
- [Presto release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Presto-release-history.html): The following table lists the version of Presto included in each release version of Amazon EMR, along with the components installed with the application.


## [Spark](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark.html)

- [Create a Spark cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-launch.html): The following procedure creates a cluster with Spark installed using Quick Options in the Amazon EMR console.
- [Run Spark applications with Docker on Amazon EMR 6.x](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-docker.html)
- [Use AWS Glue Data Catalog catalog with Spark on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-glue.html): Using Amazon EMR release 5.8.0 or later, you can configure Spark to use the AWS Glue Data Catalog as its Apache Hive metastore.
- [Working with a multi-catalog hierarchy in AWS Glue Data Catalog](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-multi-catalog.html): You can register your Amazon EMR cluster to access the AWS Glue Data Catalog, which makes tables and other catalog resources available to various consumers.
- [Configure Spark](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-configure.html): You can configure Spark on Amazon EMR with configuration classifications.

### [Use Spark Troubleshooting Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshoot.html)

- [Setup for Troubleshooting Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-setup.html)
- [Using the Troubleshooting Agent](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-using-troubleshooting-agent.html)
- [Features and Capabilities](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-features.html)
- [Troubleshooting and Q&A](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-troubleshooting.html)
- [Workflow Details](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-workflow.html): To initiate the troubleshooting process, you will need access to your failed Spark application identifiers running on supported platforms (EMR-EC2, EMR Serverless, AWS Glue, or Amazon SageMaker Data Notebooks).
- [Prompt Examples](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-prompt-examples.html): Here is a list of prompt examples that can be used in the troubleshooting experience.
- [IAM Role Setup](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-iam-setup.html): The CloudFormation stack in Setup Instructions automates the IAM role setup for you.
- [Using Tools](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-using-tools.html)
- [VPC Endpoints Configuration](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-vpc-endpoints.html): You can establish a private connection between your VPC and Amazon SageMaker Unified Studio MCP service by creating an interface VPC endpoint.
- [Cross-Region Processing](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-cross-region-processing.html): The Apache Spark Troubleshooting Agent uses cross-region inference to process natural language requests and generate responses.
- [CloudTrail Logging](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-cloudtrail-integration.html): Amazon SageMaker Unified Studio MCP Server is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon SageMaker Unified Studio MCP Server.
- [Service Improvements](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-agents-service-improvements.html): The Apache Spark agent for Amazon EMR may use content, for example, to help the Agent provide better responses to common questions, fix operational issues, or for debugging.
- [Optimize Spark performance](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-performance.html): Amazon EMR provides multiple performance optimization features for Spark.
- [Result Fragment Caching](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-fragment-result-caching.html): Use Spark Result Fragment Caching to speed up queries that repeatedly target a static subset of your data.
- [Use RAPIDS Accelerator](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-rapids.html): With Amazon EMR release 6.2.0 and later, you can use the RAPIDS Accelerator for Apache Spark plugin by Nvidia to accelerate Spark using EC2 graphics processing unit (GPU) instance types.
- [Access the Spark shell](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-shell.html): The Spark shell is based on the Scala REPL (Read-Eval-Print-Loop).
- [Use Amazon SageMaker Spark for machine learning](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-sagemaker.html): When using Amazon EMR release 5.11.0 and later, the aws-sagemaker-spark-sdk component is installed along with Spark.
- [Write a Spark application](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-application.html): Spark applications can be written in Scala, Java, or Python.

### [Improve Spark performance with S3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-s3-performance.html)

Amazon EMR offers features to help optimize performance when using Spark to query, read and write data saved in Amazon S3.

- [Use S3 Select](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-s3select.html)
- [EMR Spark MagicCommitProtocol](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-magic-commit-protocol.html): From EMR 6.15.0 onwards, MagicCommitProtocol becomes the default FileCommitProtocol for Spark when utilizing the S3A filesystem.

### [EMRFS S3-optimized committer](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-s3-optimized-committer.html)

The EMRFS S3-optimized committer is an alternative OutputCommitter implementation that is optimized for writing files to Amazon S3 when using EMRFS.

- [Requirements](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-committer-reqs.html): The EMRFS S3-optimized committer is used when the following conditions are met:
- [Multipart uploads](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-committer-multipart.html): To use the EMRFS S3-optimized committer, you must enable multipart uploads for Amazon EMR .
- [Job tuning considerations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-committer-tuning.html): The EMRFS S3-optimized committer consumes a small amount of memory for each file written by a task attempt until the task gets committed or aborted.
- [Enable the EMRFS S3-optimized committer for 5.19](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-committer-enable.html): If you are using Amazon EMR 5.19.0 , you can manually set the spark.sql.parquet.fs.optimized.committer.optimization-enabled property to true when you create a cluster or from within Spark if you are using Amazon EMR .

### [Use the EMRFS S3-optimized commit protocol](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-s3-optimized-commit-protocol.html)

The EMRFS S3-optimized commit protocol is an alternative FileCommitProtocol implementation that is optimized for writing files with Spark dynamic partition overwrite to Amazon S3 when using EMRFS.

- [Requirements for the EMRFS S3-optimized commit protocol](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-commit-protocol-reqs.html): The EMRFS S3-optimized commit protocol is used when the following conditions are met:
- [The EMRFS S3-optimized commit protocol and multipart uploads](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-commit-protocol-multipart.html): To use make use of the optimization for dynamic partition overwrite in the EMRFS S3-optimized commit protocol, multipart uploads must be enabled in Amazon EMR .
- [Job tuning considerations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-commit-protocol-tuning.html): On Spark executors, the EMRFS S3-optimized commit protocol consumes a small amount of memory for each file written by a task attempt until the task gets committed or aborted.
- [Retry S3 requests](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-emrfs-retry.html): Use an EMRFS retry strategy with Spark on Amazon EMR to retry Amazon S3 requests.
- [Add a Spark step](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-submit-step.html): You can use Amazon EMR steps to submit work to the Spark framework installed on an EMR cluster.
- [View Spark application history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-application-history.html): You can view Spark, YARN application, and Tez UI details using the Application user interfaces tab of a cluster's detail page in the console.
- [Access the Spark web UIs](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-webui.html): You can view the Spark web UIs by following the procedures to create an SSH tunnel or create a proxy in the section called Connect to the cluster in the Amazon EMR Management Guide and then navigating to the YARN ResourceManager for your cluster.
- [Using Spark with Amazon Kinesis Data Streams](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-structured-streaming-kinesis.html): Amazon EMR releases 7.1.0 and higher include a spark structured streaming Amazon Kinesis Data Streams connector in the release image.

### [Using Spark on Amazon Redshift](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-redshift.html)

With Amazon EMR release 6.4.0 and later, every release image includes a connector between Apache Spark and Amazon Redshift.

- [Launch a Spark application](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-redshift-launch.html): For Amazon EMR releases 6.4 through 6.9, you must use the --jars or --packages option to specify which of the following JAR files you want to use.
- [Authenticate to Amazon Redshift](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-redshift-auth.html)
- [Read and write to Amazon Redshift](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-redshift-readwrite.html): The following code examples use PySpark to read and write sample data from and to an Amazon Redshift database with data source API and using SparkSQL.
- [Considerations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-redshift-considerations.html)
- [Spark release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Spark-release-history.html): The following table lists the version of Spark included in each release version of Amazon EMR, along with the components installed with the application.
- [Materialized views](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-materialized-views.html): Create and manage Apache Iceberg materialized views in the AWS Glue Data Catalog using Spark on Amazon EMR clusters.


## [Sqoop](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-sqoop.html)

- [Considerations with Sqoop on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-sqoop-considerations.html): Consider the following items when you run Sqoop on Amazon EMR.
- [Sqoop release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Sqoop-release-history.html): The following table lists the version of Sqoop included in each release version of Amazon EMR, along with the components installed with the application.


## [TensorFlow](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-tensorflow.html)

- [TensorFlow release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/TensorFlow-release-history.html): The following table lists the version of TensorFlow included in each release version of Amazon EMR, along with the components installed with the application.


## [Tez](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-tez.html)

- [Creating a cluster with Tez](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/tez-create-cluster.html): To install Tez, choose Apache Tez as an application when you create your cluster.
- [Configuring Tez](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/tez-configure.html): You can customize Tez by setting values using the tez-site configuration classification, which configures settings in the tez-site.xml configuration file.
- [Tez web UI](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/tez-web-ui.html): Tez has its own web user interface.
- [Timeline Server](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/tez-timeline-server.html): The YARN Timeline Server is configured to run when Tez is installed.

### [Tez release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history.html)

The following table lists the version of Tez included in each release version of Amazon EMR, along with the components installed with the application.

### [Tez release notes by version](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-versions.html)

- [7.10.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-7100.html)
- [7.9.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-790.html)
- [7.8.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-780.html)
- [7.7.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-770.html)
- [7.6.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-760.html)
- [7.5.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-750.html)
- [7.4.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-740.html)
- [7.3.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-730.html)
- [7.2.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-720.html)
- [7.1.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-710.html)
- [7.0.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-700.html): Amazon EMR 7.0.0 Tez contains all the changes and updates made up to and including Amazon EMR-6.15.0 Tez.
- [6.15.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-6150.html)
- [6.14.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-6140.html)
- [6.13.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-6130.html)
- [6.12.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-6120.html)
- [6.11.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-6110.html)
- [6.10.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-6100.html)
- [6.9.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-690.html)
- [6.8.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-680.html)
- [6.7.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-670.html)
- [6.6.0 release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-660.html)


## [Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino.html)

- [Trino history and design](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-intro-history.html): Trino is specialized for querying large datasets from many different sources.

### [Getting started with Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-getting-started.html)

The procedures in this section show you how to set up an Amazon EMR cluster in order to query metastore data sources with Trino.

- [Complete prerequisite steps for using Amazon EMR with Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-getting-started-pre.html): If you haven't used AWS, or if you haven't created an Amazon EMR cluster, complete these prerequisite steps before you create an Amazon EMR cluster with Trino.
- [Launch an Amazon EMR cluster with Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-getting-started-launch.html): The following describes the correct configuration choices when you create a cluster with Trino.
- [Connect to the primary node and run queries](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-getting-started-connect.html)
- [Configuring Trino on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-config.html)

### [Best practices for Trino on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-advanced.html)

Trinoâs architecture is designed for fast, distributed SQL queries on large datasets across multiple data sources, following a coordinator-worker model, where each component has a specialized role in query execution.

- [Key areas of focus for performance improvement](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-performance-areas.html): Trino maximizes query parallelism and memory optimization.
- [Collect and Utilize table statistics](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-performance-areas-collect-stats.html): Collecting table statistics allows Trinoâs cost-based optimizer to make informed decisions about join orders, filter pushdown, and partition pruning, resulting in better performance.
- [Common challenges when scaling Trino workloads](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-common-issues.html): The primary benefits of using Amazon S3 with Trino are S3's ability to scale for large data volumes and S3's cost effectiveness.
- [Trino Considerations](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Trino-considerations.html): Consider the following when you run Trino on Amazon EMR.

### [Trino release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Trino-release-history.html)

The release notes sections detail changes and updates for specific version of Trino on Amazon EMR.

- [Amazon EMR 7.6.0 - Trino release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Trino-release-history-760.html)
- [Amazon EMR 7.3.0 - Trino release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Trino-release-history-730.html)
- [Amazon EMR 6.9.0 - Trino release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Trino-release-history-690.html)


## [Zeppelin](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-zeppelin.html)

- [Considerations when using Zeppelin on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/zeppelin-considerations.html)
- [Zeppelin release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Zeppelin-release-history.html): The following table lists the version of Zeppelin included in each release version of Amazon EMR, along with the components installed with the application.


## [ZooKeeper](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-zookeeper.html)

- [ZooKeeper release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ZooKeeper-release-history.html): The following table lists the version of ZooKeeper included in each release version of Amazon EMR, along with the components installed with the application.

### [ZooKeeper release notes by version](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ZooKeeper-release-history-versions.html)

See the following sections for the full release notes.

- [Amazon EMR 7.8.0 - ZooKeeper release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ZooKeeper-release-history-780.html)
- [Amazon EMR 7.5.0 - ZooKeeper release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ZooKeeper-release-history-750.html)
- [Amazon EMR 7.4.0 - ZooKeeper release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ZooKeeper-release-history-740.html)


## [Connectors and utilities](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-connectors.html)

### [Export, query, and join tables in DynamoDB](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/EMRforDynamoDB.html)

Export, import, and query data, and join tables in Amazon DynamoDB using Amazon Elastic MapReduce with a customized version of Hive.

- [Set up a Hive table to run Hive commands](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/EMR_Interactive_Hive.html): Follow these steps to set up a Hive table and run Hive commands when you integrate Amazon EMR with Amazon DynamoDB.
- [Hive command examples for exporting, importing, and querying data](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/EMR_Hive_Commands.html): Use these examples to understand Hive commands for Amazon EMR and Amazon DynamoDB integration.
- [Optimizing performance](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/EMR_Hive_Optimizing.html): Follow these tips to get the most out of Amazon EMR performance when integrating with Amazon DynamoDB.

### [Kinesis](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-kinesis.html)

Amazon EMR clusters can read and process Amazon Kinesis streams directly, using familiar tools in the Hadoop ecosystem such as Hive, Pig, MapReduce, the Hadoop Streaming API, and Cascading.

- [Migrating Spark Kinesis connector to SDK 2.x for Amazon EMR 7.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/migrating-spark-kinesis.html): The AWS SDK provides a rich set of APIs and libraries to interact with AWS cloud computing services, such as managing credentials, connecting to S3 and Kinesis services.
- [S3DistCp (s3-dist-cp)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/UsingEMR_s3distcp.html): Copy large amounts of data using SCDistCp in a distributed manner, sharing the tasks across several servers.
