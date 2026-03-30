# Source: https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/llms.txt

# Amazon Lookout for Equipment User Guide

> Provides a conceptual overview of Amazon Lookout for Equipment and offers detailed instructions for using various features.

- [What is Amazon Lookout for Equipment?](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/what-is.html)
- [Setting up your account](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/getting-started-brain.html)
- [Creating your project](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/create-project.html)
- [Formatting your data](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/formatting-data.html)
- [Adding your dataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/ingest-dataset.html)
- [Evaluating your model](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/view-model.html)
- [Viewing your ingestion history](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/viewing-ingestion-history.html)
- [Replacing your dataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/replacing-your-dataset.html)
- [Use case: fluid pump](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/use-case.html)
- [Quotas](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/guidelines-and-limits.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/creating-resources-with-cloudformation.html)
- [Python SDK examples](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/SDK-examples.html)
- [Document history](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/doc-history.html)

## [How it works](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/how-it-works.html)

- [Step by step](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/step-by-step.html): Overview of the Amazon Lookout for Equipment service, which monitors industrial equipment to detect abnormal equipment behavior and identify potential failures.


## [Reviewing data ingestion](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/understanding-ingestion-validation.html)

- [Reviewing the job](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/when-ingestion-jobs-fail.html): Few datasets are perfectly formed.
- [Checking the files](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/when-files-dont-get-ingested.html): Troubleshoot files that were not ingested.
- [Evaluating sensor grades](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/reading-details-by-sensor.html): Deciding which sensors to use when you trainin your model.


## [Training your model](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/create-model.html)

- [Specifying model details](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/specifying-model-details.html): Specify details about your ML model.

### [Configuring your input data](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/configuring-input-data.html)

- [Labeling your data](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/labeling-data.html): Applying labels to your data to indicate the presence of known anomalous events in the past.
- [Starting the training process](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/reviewing-settings.html): The Review and train page gives you a chance to change some of your settings before you start training your model.


## [Scheduling inference](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/inference.html)

- [Managing inference schedules](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/managing-inference-schedules.html)
- [Understanding the inference process](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/understanding-inference-process.html): When you're planning your use of Lookout for Equipment, it may be useful to understand exactly what happens at each step of the inference process.


## [Reviewing inference results](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/understanding-results.html)

- [In the console](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/understanding-results-console.html)
- [In a JSON file](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/understanding-results-json.html): The JSON file containing the inference results is stored in the Amazon Simple Storage Service (Amazon S3) bucket that you've specified.


## [Best practices](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/best-practices.html)

- [Choosing the right application](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/the-right-app.html): Choosing the right application of Lookout for Equipment involves finding the right combination of business value, equipment operations, and available data.
- [Choosing the right data](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/the-right-data.html): Your dataset should contain time-series data that's generated from an industrial asset such as a pump, compressor, motor, and so on.
- [Evaluating the output](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/evaluating-output.html): After a model is trained, Lookout for Equipment evaluates its performance on a subset of the dataset that you've specified for evaluation purposes.
- [Improving your results](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/improve-your-results.html): To improve the results, consider the following:
- [Consulting subject matter experts](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/sme.html): Lookout for Equipment identifies patterns in the dataset that help to detect critical issues, but it's the responsibility of a technician or subject matter expert (SME) to diagnose the problem and take corrective action, if needed.


## [Security](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Lookout for Equipment.

- [Encryption at rest](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/encryption-at-rest.html): Amazon Lookout for Equipment encrypts your data at rest with your choice of an encryption key.
- [Encryption in transit](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/encryption-in-transit.html): Amazon Lookout for Equipment copies data out of your account and processes it in an internal AWS system.
- [Key management](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/key-management.html): Amazon Lookout for Equipment encrypts your data using one of the following types of keys:

### [Identity and access management](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/security-iam.html)

Learn how to authenticate requests and manage access to your Amazon Lookout for Equipment resources.

- [AWS Identity and Access Management for Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Lookout for Equipment, learn what IAM features are available to use with Amazon Lookout for Equipment.
- [Identity-based policy examples](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Lookout for Equipment resources.
- [AWS managed policies](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Lookout for Equipment and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Lookout for Equipment and IAM.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Lookout for Equipment without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Compliance validation](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/SERVICENAME-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Lookout for Equipment features for data resiliency.


## [Monitoring Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/monitoring-cloudwatch.html): You can monitor Amazon Lookout for Equipment using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
