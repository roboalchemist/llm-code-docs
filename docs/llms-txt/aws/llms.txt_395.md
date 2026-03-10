# Source: https://docs.aws.amazon.com/frauddetector/latest/ug/llms.txt

# Amazon Fraud Detector User Guide

> Describes Amazon Fraud Detector

- [Amazon Fraud Detector availability change](https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-availability-change.html)
- [Set up for Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/set-up.html)
- [Event dataset](https://docs.aws.amazon.com/frauddetector/latest/ug/create-event-dataset.html)
- [Troubleshoot](https://docs.aws.amazon.com/frauddetector/latest/ug/troubleshoot.html)
- [Quotas](https://docs.aws.amazon.com/frauddetector/latest/ug/limits.html)
- [Document history](https://docs.aws.amazon.com/frauddetector/latest/ug/doc-history.html)

## [What is Amazon Fraud Detector?](https://docs.aws.amazon.com/frauddetector/latest/ug/what-is-frauddetector.html)

- [Benefits](https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-benefits.html): Amazon Fraud Detector provides the following benefits.
- [Core concepts and terms](https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-ml-concepts.html): The following is a list of core concepts and terms that are used in Amazon Fraud Detector:
- [How Amazon Fraud Detector works](https://docs.aws.amazon.com/frauddetector/latest/ug/how-frauddetector-works.html): Amazon Fraud Detector builds a machine learning model that is customized to detect potential fraudulent online activities in your business.
- [Detecting fraud with Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-workflow.html): This section describes a typical workflow for detecting fraud with Amazon Fraud Detector.
- [Accessing Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/how-to-access-frauddetector.html): Amazon Fraud Detector is available in multiple AWS Regions and can be accessed using AWS interfaces.
- [Pricing](https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-pricing.html): With Amazon Fraud Detector, you pay only for what you use.


## [Get started with Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/get-started.html)

- [Get and upload example dataset](https://docs.aws.amazon.com/frauddetector/latest/ug/step-1-get-s3-data.html): The example dataset you use in this tutorial provides details of online account registrations.

### [Tutorial: Get started using the Amazon Fraud Detector console](https://docs.aws.amazon.com/frauddetector/latest/ug/get-started-console.html)

This tutorial consists of two parts.

- [Part A: Build, train, and deploy an Amazon Fraud Detector model](https://docs.aws.amazon.com/frauddetector/latest/ug/part-a.html): In part A, you define your business use case, define your event, build a model, train the model, evaluate model's performance, and deploy the model.
- [Part B: Generate fraud predictions](https://docs.aws.amazon.com/frauddetector/latest/ug/part-b.html): Fraud prediction is an evaluation of fraud for a business activity (event).
- [Tutorial: Get started using the AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/frauddetector/latest/ug/getting-started-python.html): Getting started exercise with the AWS SDK for Python (Boto3).
- [Next steps](https://docs.aws.amazon.com/frauddetector/latest/ug/next-steps-get-started-console.html): Now that you created a model and a detector, you can take a deeper dive and start to create models and detectors and generate fraud predictions.


## [Event type](https://docs.aws.amazon.com/frauddetector/latest/ug/event-type.html)

- [Create an event type](https://docs.aws.amazon.com/frauddetector/latest/ug/create-event-type.html): Before you create your fraud detection model, you must first create an event type.
- [Delete an event or event type](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-event.html): Permanently delete an event, including all event data, in Amazon Fraud Detector.


## [Event data storage](https://docs.aws.amazon.com/frauddetector/latest/ug/event-data-storage.html)

### [Store your event data externally with Amazon S3](https://docs.aws.amazon.com/frauddetector/latest/ug/uploading-event-data-to-an-s3-bucket.html)

If you are training an Online Fraud Insights model, you can choose to store your event data externally with Amazon S3.

- [Create CSV file](https://docs.aws.amazon.com/frauddetector/latest/ug/creating-csv-file.html): Amazon Fraud Detector requires that the first row of your CSV file contain column headers.
- [Upload your event data to an Amazon S3 bucket](https://docs.aws.amazon.com/frauddetector/latest/ug/uploading-to-an-s3-bucket.html): After you create a CSV file with your event data, upload the file to your Amazon S3 bucket.

### [Store your event data internally with Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/storing-event-data-afd.html)

You can choose to store event data in Amazon Fraud Detector and use the stored data later to train your models.

- [Prepare event data for storage](https://docs.aws.amazon.com/frauddetector/latest/ug/prepare-storage-event-data.html): Event data that is stored internally with Amazon Fraud Detector is stored at the Event Type resource level.
- [Store event data using batch import](https://docs.aws.amazon.com/frauddetector/latest/ug/storing-events-batch-import.html): With the batch import feature, you can quickly and easily upload large historical event datasets in Amazon Fraud Detector using the console, the API, or the AWS SDK.
- [Store event data using the GetEventPredictions API operation](https://docs.aws.amazon.com/frauddetector/latest/ug/storing-events-geteventprediction-api.html): By default, all events sent to the GetEventPrediction API for evaluation are stored in Amazon Fraud Detector.
- [Store event data using the SendEvent API operation](https://docs.aws.amazon.com/frauddetector/latest/ug/storing-events-sendevent-api.html): You can use the SendEvent API operation to store events in Amazon Fraud Detector without generating fraud predictions for those events.
- [Get details of a stored event data](https://docs.aws.amazon.com/frauddetector/latest/ug/get-stored-event-details.html): After you store event data in Amazon Fraud Detector, you can check the latest data that was stored for an event using the GetEvent API.
- [View metrics of stored event dataset](https://docs.aws.amazon.com/frauddetector/latest/ug/view-stored-event-metrics.html): For each event type, you can view metrics such as, number of stored events, total size of your stored events, and timestamps of the earliest and the latest stored events, in the Amazon Fraud Detector console.


## [Event orchestration](https://docs.aws.amazon.com/frauddetector/latest/ug/event-orchestration.html)

- [Setting up event orchestration](https://docs.aws.amazon.com/frauddetector/latest/ug/setting-up-event-orchestration.html): Setting up event orchestration for your events requires you to set up processes in your target service, configure Amazon EventBridge to receive and send event data, and create rules in Amazon EventBridge that specifies the conditions for starting the downstream processes.
- [Enable event orchestration in Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/enable-event-orchestration.html): You can enable event orchestration for an event either when you are creating your event type or after you have created your event type.
- [Disable event orchestration in Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/disable-event-orchestration.html): You can disable event orchestration for an event anytime in the Amazon Fraud Detector console, using the put-event-type command, using the PutEventType API, or using the AWS SDK for Python (Boto3).


## [Model](https://docs.aws.amazon.com/frauddetector/latest/ug/create-model.html)

### [Choose a model type](https://docs.aws.amazon.com/frauddetector/latest/ug/choosing-model-type.html)

The following model types are available in Amazon Fraud Detector.

- [Online fraud insights](https://docs.aws.amazon.com/frauddetector/latest/ug/online-fraud-insights.html): Online Fraud Insights is a supervised machine learning model, which means that it uses historical examples of fraudulent and legitimate transactions to train the model.
- [Transaction fraud insights](https://docs.aws.amazon.com/frauddetector/latest/ug/transaction-fraud-insights.html): The Transaction Fraud Insights model type is designed to detect online, or card-not-present, transaction fraud.
- [Account takeover insights](https://docs.aws.amazon.com/frauddetector/latest/ug/account-takeover-insights.html): The Account Takeover Insights (ATI) model type identifies fraudulent online activity by detecting if accounts were compromised through malicious takeovers, phishing, or from credentials being stolen.
- [Build a model](https://docs.aws.amazon.com/frauddetector/latest/ug/building-a-model.html): Amazon Fraud Detector models learn to detect fraud for a specific event type.
- [Model scores](https://docs.aws.amazon.com/frauddetector/latest/ug/model-scores.html): Amazon Fraud Detector generates model scores differently for different model types.
- [Model performance metrics](https://docs.aws.amazon.com/frauddetector/latest/ug/training-performance-metrics.html): After model training is complete, Amazon Fraud Detector validates model performance using 15% of your data that was not used to train the model.
- [Model variable importance](https://docs.aws.amazon.com/frauddetector/latest/ug/model-variable-importance.html): Model variable importance is a feature of Amazon Fraud Detector that ranks model variables within a model version.
- [Import a SageMaker AI model](https://docs.aws.amazon.com/frauddetector/latest/ug/import-an-amazon-sagemaker-model.html): You can optionally import SageMaker AI-hosted models to Amazon Fraud Detector.
- [Delete a model or model version](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-model.html): Delete models and model versions, including SageMaker AI models, that are not associated with a detector version in Amazon Fraud Detector.


## [Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/detector.html)

- [Create a detector](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-detector.html): You create a detector by specifying the event type that you have already defined.
- [Create a detector version](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-detector-version.html): A detector version defines the rules, rule execution order, and optionally a model version, that will be used as part of the request for generating fraud predictions.
- [Delete a detector, detector version, or rule version](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-detector.html): Delete all detector versions and rule versions before deleting a detector in Amazon Fraud Detector.


## [Resources](https://docs.aws.amazon.com/frauddetector/latest/ug/create-resources.html)

### [Variables](https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html)

Variables represent data elements that you want to use in a fraud prediction.

- [Create a variable](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html): You can create variables in the Amazon Fraud Detector console, using the create-variable command, using the CreateVariable, or using the AWS SDK for Python (Boto3)
- [Delete a variable](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-variable.html): Delete variables in Amazon Fraud Detector.

### [Labels](https://docs.aws.amazon.com/frauddetector/latest/ug/labels.html)

A label classifies an event as fraudulent or legitimate.

- [Create label](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-label.html): You can create labels in the Amazon Fraud Detector console, using the put-label command, using the PutLabel API, or using the AWS SDK for Python (Boto3).
- [Update label](https://docs.aws.amazon.com/frauddetector/latest/ug/update-label.html): If your event dataset is stored with Amazon Fraud Detector, you might need to add or update labels for the stored events, such as when you perform an offline fraud investigation for an event and want to close the machine learning feed back loop.
- [Updating event labels in event data stored in Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/update-event-labels.html): You might need to add or update fraud labels for events that are already stored in Amazon Fraud Detector, such as when you perform an offline fraud investigation for an event and want to close the machine learning feed back loop.
- [Delete label](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-label.html): Delete labels in Amazon Fraud Detector.

### [Rules](https://docs.aws.amazon.com/frauddetector/latest/ug/rules.html)

A rule is a condition that tells Amazon Fraud Detector how to interpret variable values during a fraud prediction.

- [Rule language reference](https://docs.aws.amazon.com/frauddetector/latest/ug/rule-language-reference.html): The following section outlines the expression (that is, rule writing) capabilities in Amazon Fraud Detector.
- [Create rules](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-rule.html): You can create rules in Amazon Fraud Detector console, using the create-rule command, using the CreateRule API, or using the AWS SDK for Python (Boto3).
- [Update rule](https://docs.aws.amazon.com/frauddetector/latest/ug/update-rule.html): You can update a rule anytime by adding or updating the rule description, updating the rule expression, or adding or removing the outcome for the rule.

### [Lists](https://docs.aws.amazon.com/frauddetector/latest/ug/lists.html)

A list is a set of input data for a variable in your event dataset.

- [Create a list](https://docs.aws.amazon.com/frauddetector/latest/ug/create-list.html): You can create a list containing input data (entries) of a variable in your event dataset and use the list in rule expression.
- [Add entries in a list](https://docs.aws.amazon.com/frauddetector/latest/ug/add-entries-in-list.html): After you created your list you can add or append entries in your list at any time.
- [Assign a variable type to a list](https://docs.aws.amazon.com/frauddetector/latest/ug/assign-variable-type-list.html): Every list you use in a rule must be associated with an Amazon Fraud Detector's variable type.
- [Delete a list](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-list.html): You can delete a list that isn't used in any rule.
- [Delete entries from a list](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-entries-list.html): You can delete one or more entries from your lists at any time.
- [Delete all entries from a list](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-all-entries-list.html): You can delete all entries in your list, if the list isnât being used in a rule.

### [Outcomes](https://docs.aws.amazon.com/frauddetector/latest/ug/outcomes.html)

An outcome is the result of a fraud prediction.

- [Create an outcome](https://docs.aws.amazon.com/frauddetector/latest/ug/create-an-outcome.html): You can create outcomes in the Amazon Fraud Detector console, using the put-outcome command, using the PutOutcome API, or using the AWS SDK for Python (Boto3).
- [Delete an outcome](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-outcome.html): Delete an outcome in Amazon Fraud Detector.

### [Entity](https://docs.aws.amazon.com/frauddetector/latest/ug/entity.html)

An entity represents a person or thing that's performing the event.

- [Create an entity type](https://docs.aws.amazon.com/frauddetector/latest/ug/create-an-entity-type.html): You can create an entity type in the Amazon Fraud Detector console, using the put-entity-type command, using the PutEntityType API, or using the AWS SDK for Python (Boto3).
- [Delete an entity type](https://docs.aws.amazon.com/frauddetector/latest/ug/delete-entity-type.html): Delete an entity type in Amazon Fraud Detector.
- [Manage resources using AWS CloudFormation](https://docs.aws.amazon.com/frauddetector/latest/ug/managing-resources-using-cloudformation.html): Learn how to manage resources for Amazon Fraud Detector using an AWS CloudFormation template.


## [Fraud predictions](https://docs.aws.amazon.com/frauddetector/latest/ug/getting-fraud-predictions.html)

- [Real time prediction](https://docs.aws.amazon.com/frauddetector/latest/ug/real-time-fraud-prediction.html): Get fraud predictions in real time for a single event using Amazon Fraud Detector
- [Batch predictions](https://docs.aws.amazon.com/frauddetector/latest/ug/batch-predictions.html): Get predictions for a set of events that don't require real-time scoring in Amazon Fraud Detector using a batch predictions job.
- [Prediction explanations](https://docs.aws.amazon.com/frauddetector/latest/ug/prediction-explanation.html): Use prediction explanations to get insight into how each event variable impacts your model's fraud prediction scores using Amazon Fraud Detector console.


## [Security](https://docs.aws.amazon.com/frauddetector/latest/ug/security.html)

### [Data Protection](https://docs.aws.amazon.com/frauddetector/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Fraud Detector.

- [Encryption at rest](https://docs.aws.amazon.com/frauddetector/latest/ug/encryption-at-rest.html): Learn how Amazon Fraud Detector encrypts your data at rest using AWS shared responsibility model.
- [Encryption in transit](https://docs.aws.amazon.com/frauddetector/latest/ug/encryption-in-transit.html): Learn how Amazon Fraud Detector encrypts your data in transit using AWS shared responsibility model.
- [Key management](https://docs.aws.amazon.com/frauddetector/latest/ug/key-management.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Fraud Detector.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/frauddetector/latest/ug/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Fraud Detector without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Opting out](https://docs.aws.amazon.com/frauddetector/latest/ug/opting-out-of-using-your-data-for-service-improvement.html): Learn how to opt out of using your data to be used to develop or improve the quality of Amazon Fraud Detector.

### [Identity and access management](https://docs.aws.amazon.com/frauddetector/latest/ug/security-iam.html)

How to authenticate requests and manage access your Amazon Fraud Detector resources.

- [How Amazon Fraud Detector works with IAM](https://docs.aws.amazon.com/frauddetector/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Fraud Detector, you should understand what IAM features are available to use with Amazon Fraud Detector.
- [Identity-based policy examples](https://docs.aws.amazon.com/frauddetector/latest/ug/security_iam_id-based-policy-examples.html): By default, users and IAM roles don't have permission to create or modify Amazon Fraud Detector resources.
- [Confused deputy prevention](https://docs.aws.amazon.com/frauddetector/latest/ug/confused-deputy-prevention.html): The confused deputy problem occurs when an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Troubleshooting](https://docs.aws.amazon.com/frauddetector/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Fraud Detector and IAM.
- [Monitoring Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/security-logging-and-monitoring.html): Monitor Amazon Fraud Detector to maintain reliability, availability, and performance.
- [Compliance validation](https://docs.aws.amazon.com/frauddetector/latest/ug/SERVICENAME-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/frauddetector/latest/ug/disaster-recovery-resiliency.html): The AWS global infrastructure is built around AWS Regions and Availability Zones.
- [Infrastructure Security](https://docs.aws.amazon.com/frauddetector/latest/ug/infrastructure-security.html): Learn how Amazon Fraud Detector isolates service traffic.


## [Monitor Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/frauddetector/latest/ug/monitoring-cloudwatch.html): You can monitor Amazon Fraud Detector using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Logging Amazon Fraud Detector API Calls with AWS CloudTrail](https://docs.aws.amazon.com/frauddetector/latest/ug/logging-using-cloudtrail.html): Learn about logging Amazon Fraud Detector with AWS CloudTrail.
