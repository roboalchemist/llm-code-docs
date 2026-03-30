# Source: https://docs.aws.amazon.com/comprehend/latest/dg/llms.txt

# Amazon Comprehend Developer Guide

> Extract insights about a document with Amazon Comprehend.

- [What is Amazon Comprehend?](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)
- [Supported languages](https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html)
- [Setting up](https://docs.aws.amazon.com/comprehend/latest/dg/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/comprehend/latest/dg/getting-started.html)
- [Trust and safety](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html)
- [Guidelines and quotas](https://docs.aws.amazon.com/comprehend/latest/dg/guidelines-and-limits.html)
- [API reference](https://docs.aws.amazon.com/comprehend/latest/dg/api-ref.html)
- [Document history](https://docs.aws.amazon.com/comprehend/latest/dg/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/comprehend/latest/dg/glossary.html)

## [How it works](https://docs.aws.amazon.com/comprehend/latest/dg/how-it-works.html)

### [Insights](https://docs.aws.amazon.com/comprehend/latest/dg/concepts-insights.html)

Amazon Comprehend can analyze a document or set of documents to gather insights about it.

- [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html): An entity is a textual reference to the unique name of a real-world object such as people, places, and commercial items, and to precise references to measures such as dates and quantities.
- [Events](https://docs.aws.amazon.com/comprehend/latest/dg/how-events.html): Use event detection to analyze text documents for speciï¬c types of events and their related entities.
- [Key phrases](https://docs.aws.amazon.com/comprehend/latest/dg/how-key-phrases.html): A key phrase is a string containing a noun phrase that describes a particular thing.
- [Dominant language](https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html): You can use Amazon Comprehend to examine text to determine the dominant language.
- [Sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.html): Use Amazon Comprehend to determine the sentiment of content in UTF-8 encoded text documents.
- [Targeted sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html): Learn how to analyze documents for targeted sentiment.
- [Syntax analysis](https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html): Use Amazon Comprehend Syntax to parse the words in you documents and assign them to a part of speech.
- [Amazon Comprehend Custom](https://docs.aws.amazon.com/comprehend/latest/dg/concepts-custom.html): You can customize Amazon Comprehend for your specific requirements without the skillset required to build machine learning-based NLP solutions.
- [Topic modeling](https://docs.aws.amazon.com/comprehend/latest/dg/topic-modeling.html): You can use Amazon Comprehend to examine the content of a collection of documents to determine common themes.
- [Document processing modes](https://docs.aws.amazon.com/comprehend/latest/dg/concepts-processing-modes.html): Amazon Comprehend supports three document processing modes.


## [Using the console](https://docs.aws.amazon.com/comprehend/latest/dg/get-started-console.html)

- [Real-time analysis](https://docs.aws.amazon.com/comprehend/latest/dg/realtime-console-analysis.html): You can use the Amazon Comprehend console to run real-time analysis of a UTF-8 encoded text document.
- [Analysis jobs (console)](https://docs.aws.amazon.com/comprehend/latest/dg/analysis-jobs.html): Learn how to use analysis jobs using the Amazon Comprehend console.


## [Using the API](https://docs.aws.amazon.com/comprehend/latest/dg/using-the-api.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/comprehend/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Real-time analysis (API)](https://docs.aws.amazon.com/comprehend/latest/dg/using-api-sync.html): Learn how to use the Amazon Comprehend synchronous API operations for real-time analysis.

### [Async analysis jobs (API)](https://docs.aws.amazon.com/comprehend/latest/dg/api-async.html)

Learn how to use the async Amazon Comprehend API operations.

- [Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html): Learn how to use the Amazon Comprehend API operations.
- [Targeted sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/using-api-targeted-sentiment.html): For information about real-time analysis for Targeted sentiment, see .
- [Event detection](https://docs.aws.amazon.com/comprehend/latest/dg/get-started-api-events.html)
- [Topic modeling](https://docs.aws.amazon.com/comprehend/latest/dg/get-started-topics.html): To determine the topics in a document set, use the StartTopicsDetectionJob to start an asynchronous job.


## [Personally identifiable information (PII)](https://docs.aws.amazon.com/comprehend/latest/dg/pii.html)

- [Detecting PII entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html): Learn about locating and redacting Personally Identifiable Information (PII).
- [Labeling PII entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii-labels.html): Learn how to label the PII entities in your documents.
- [Real-time analysis (Console)](https://docs.aws.amazon.com/comprehend/latest/dg/realtime-pii-console.html): Learn how to use the console to detect Personally Identifiable Information (PII).
- [Async analysis jobs (Console)](https://docs.aws.amazon.com/comprehend/latest/dg/async-pii-console.html): Learn how to use the console to detect Personally Identifiable Information (PII).
- [Real-time analysis (API)](https://docs.aws.amazon.com/comprehend/latest/dg/realtime-pii-api.html): Learn how to use the synchronous API to detect Personally Identifiable Information (PII).

### [Async analysis jobs (API)](https://docs.aws.amazon.com/comprehend/latest/dg/get-started-api-pii.html)

Learn how to use the API to start asynchronous jobs to locate or redact PII entities.

- [Locating PII entities](https://docs.aws.amazon.com/comprehend/latest/dg/async-pii-api.html): Learn how to use the API to start asynchronous jobs to locate PII entities.
- [Redacting PII entities](https://docs.aws.amazon.com/comprehend/latest/dg/redact-api-pii.html): Learn how to use the asynchronous API to redact PII entities.


## [Document processing](https://docs.aws.amazon.com/comprehend/latest/dg/idp.html)

- [Inputs for real-time analysis](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html): Learn about the inputs for real-time analysis using custom models in Amazon Comprehend.
- [Inputs for async analysis](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-async.html): Learn learn about the inputs and output files for custom analysis jobs in Amazon Comprehend.
- [Setting text extraction options](https://docs.aws.amazon.com/comprehend/latest/dg/idp-set-textract-options.html): Learn about setting text extraction options in Amazon Comprehend.
- [Best practices for images](https://docs.aws.amazon.com/comprehend/latest/dg/idp-images-bp.html): Learn about best practices for images.


## [Custom classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html)

### [Preparing the training data](https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html)

Learn how to prepare data for models for custom classification in Amazon Comprehend.

- [Training file formats](https://docs.aws.amazon.com/comprehend/latest/dg/prep-class-data-format.html): Learn about formats of the training files in custom classification in Amazon Comprehend.
- [Multi-class mode](https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data-multi-class.html): Learn about multi-class mode for custom classification in Amazon Comprehend.
- [Multi-label mode](https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data-multi-label.html): Learn about multi-label mode for custom classification in Amazon Comprehend.

### [Training classification models](https://docs.aws.amazon.com/comprehend/latest/dg/training-classifier-model.html)

Learn how train models for custom classification in Amazon Comprehend.

- [Train custom classifiers (console)](https://docs.aws.amazon.com/comprehend/latest/dg/create-custom-classifier-console.html): Learn how to train the model for custom classification using the console.
- [Train custom classifiers (API)](https://docs.aws.amazon.com/comprehend/latest/dg/train-custom-classifier-api.html): Learn how to train the model for custom classification using the API.
- [Test the training data](https://docs.aws.amazon.com/comprehend/latest/dg/testing-the-model.html): Learn how to test the model for custom classification in Amazon Comprehend.
- [Classifier training output](https://docs.aws.amazon.com/comprehend/latest/dg/train-classifier-output.html): Details about the training output for custom classifiers in Amazon Comprehend.
- [Metrics](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html): Learn about metrics for custom classification in Amazon Comprehend.

### [Running real-time analysis](https://docs.aws.amazon.com/comprehend/latest/dg/running-class-sync.html)

Learn how run real-time analysis for custom classification in Amazon Comprehend.

- [Real-time analysis (console)](https://docs.aws.amazon.com/comprehend/latest/dg/custom-sync.html): Learn about real-time analysis for custom classification in Amazon Comprehend.
- [Real-time analysis (API)](https://docs.aws.amazon.com/comprehend/latest/dg/class-sync-api.html): Use the API for real-time analysis for custom classification in Amazon Comprehend.
- [Outputs for real-time analysis](https://docs.aws.amazon.com/comprehend/latest/dg/outputs-class-sync.html): Learn learn about the outputs for custom classification real-time analysis in Amazon Comprehend.

### [Running async analysis jobs](https://docs.aws.amazon.com/comprehend/latest/dg/running-classifiers.html)

Learn how run asynchronous analysis for custom classification in Amazon Comprehend.

- [Input file formats](https://docs.aws.amazon.com/comprehend/latest/dg/class-inputs-async.html): Learn learn about the file formats for custom classification analysis jobs in Amazon Comprehend.
- [Analysis jobs (console)](https://docs.aws.amazon.com/comprehend/latest/dg/analysis-jobs-custom-classifier.html): Use the console to run analysis for custom classification in Amazon Comprehend.
- [Analysis jobs (API)](https://docs.aws.amazon.com/comprehend/latest/dg/analysis-jobs-custom-class-api.html): Learn how to run analysis jobs for custom classification in Amazon Comprehend.
- [Outputs for analysis jobs](https://docs.aws.amazon.com/comprehend/latest/dg/outputs-class-async.html): Learn learn about the output files for custom classification analysis in Amazon Comprehend.


## [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html)

### [Preparing the training data](https://docs.aws.amazon.com/comprehend/latest/dg/prep-training-data-cer.html)

Describes how to prepare training data for custom entity recognition models.

- [Entity lists](https://docs.aws.amazon.com/comprehend/latest/dg/cer-entity-list.html): To train a model using an entity list, you provide two pieces of information: a list of the entity names with their corresponding custom entity types and a collection of unannotated documents in which you expect your entities to appear.

### [Annotations](https://docs.aws.amazon.com/comprehend/latest/dg/cer-annotation.html)

Describes how to prepare annotated training data for custom entity recognition models.

- [Plain-text annotations](https://docs.aws.amazon.com/comprehend/latest/dg/cer-annotation-csv.html): Describes how to prepare annotated training data for custom entity recognition models.
- [PDF annotations](https://docs.aws.amazon.com/comprehend/latest/dg/cer-annotation-manifest.html): Describes how to prepare annotated training data for custom entity recognition models.
- [Annotating PDF files](https://docs.aws.amazon.com/comprehend/latest/dg/cer-annotation-pdf.html): Describes how to prepare annotated training data for custom entity recognition models.

### [Training recognizer models](https://docs.aws.amazon.com/comprehend/latest/dg/training-recognizers.html)

Describes how to train custom models for entity recognition.

- [Train custom recognizers (console)](https://docs.aws.amazon.com/comprehend/latest/dg/realtime-analysis-cer.html): Describes how to train custom recognizers using the console.
- [Train custom recognizers (API)](https://docs.aws.amazon.com/comprehend/latest/dg/train-cer-model.html): Describes how to train custom recognizers using the API.
- [Metrics](https://docs.aws.amazon.com/comprehend/latest/dg/cer-metrics.html): Amazon Comprehend provides you with metrics to help you estimate how well an entity recognizer should work for your job.

### [Running real-time analysis](https://docs.aws.amazon.com/comprehend/latest/dg/running-cer-sync.html)

Learn how run real-time analysis for custom CER in Amazon Comprehend.

- [Real-time analysis (console)](https://docs.aws.amazon.com/comprehend/latest/dg/detecting-cer-real-time.html): Use your custom model to quickly detect entities in individual documents, such as social media posts, support tickets, or customer reviews.
- [Real-time analysis (API)](https://docs.aws.amazon.com/comprehend/latest/dg/detecting-cer-real-time-api.html): Use your custom model to quickly detect entities in individual documents, such as social media posts, support tickets, or customer reviews.
- [Outputs for real-time analysis](https://docs.aws.amazon.com/comprehend/latest/dg/outputs-cer-sync.html): Learn learn about the outputs for custom entity recognition analysis in Amazon Comprehend.

### [Running async analysis jobs](https://docs.aws.amazon.com/comprehend/latest/dg/detecting-cer.html)

Describes how to run analysis jobs for custom entity recognition using the console and API.

- [Analysis jobs (console)](https://docs.aws.amazon.com/comprehend/latest/dg/detecting-cer-async-console.html): Describes how to run analysis jobs for custom entity recognition using the console.
- [Analysis jobs (API)](https://docs.aws.amazon.com/comprehend/latest/dg/detecting-cer-async-api.html): Describes how to run analysis jobs for custom entity recognition using the API.
- [Outputs for analysis jobs](https://docs.aws.amazon.com/comprehend/latest/dg/outputs-cer-async.html): Learn about the outputs for custom entity recognition real-time analysis in Amazon Comprehend.


## [Managing custom models](https://docs.aws.amazon.com/comprehend/latest/dg/manage-models.html)

- [Model versioning with Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/model-versioning.html): Artificial intelligence and machine learning (AI/ML) is all about rapid experimentation.

### [Copying custom models between AWS accounts](https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy.html)

Learn how to share a model copy between AWS accounts.

- [Sharing a custom model](https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy-sharing.html): Learn how to share your custom models with users in other AWS accounts.
- [Importing a custom model](https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy-importing.html): Learn how to import and copy a custom model from another AWS account.


## [Flywheels](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels.html)

- [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html): Learn how to use Amazon Comprehend flywheels to orchestrate the training and evaluation of new model versions.
- [Flywheel data lakes](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-datalake.html): Learn how to use a data lake with Amazon Comprehend flywheels.
- [IAM policies and permissions](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-permissions.html): Learn about required IAM policies and permissions for using Amazon Comprehend flywheels.
- [Configuring flywheels (Console)](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-config-console.html): Learn how to create and configure Amazon Comprehend flywheels.
- [Configuring flywheels (API)](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-config-api.html): Learn how to create and configure Amazon Comprehend flywheels.
- [Configuring datasets](https://docs.aws.amazon.com/comprehend/latest/dg/datasets-config.html): Learn how to configure datasets for Amazon Comprehend flywheels.
- [Flywheel iterations](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-iterate.html): Learn how to use Amazon Comprehend flywheel iterations.
- [Using flywheels](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-inference.html): Learn how to use Amazon Comprehend flywheels to orchestrate training tasks for custom models.


## [Managing endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)

- [Endpoints overview](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-overview.html): Learn about Amazon Comprehend endpoints;.
- [Using endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/using-endpoints.html): Learn how use endpoints to run real-time analysis in Amazon Comprehend.
- [Monitoring endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-monitor.html): Learn about monitoring Amazon Comprehend endpoints;.
- [Updating endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-update.html): Learn about updating Amazon Comprehend endpoints;.
- [Using Trusted Advisor](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-trusted-advisor.html): Learn about managing Amazon Comprehend endpoints with Trusted Advisor.
- [Deleting endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-delete.html): Learn about deleting Amazon Comprehend endpoints;.

### [Auto scaling with endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-autoscaling.html)

Describes auto scaling for endpoints with examples.

- [Target tracking](https://docs.aws.amazon.com/comprehend/latest/dg/targettracking.html): With target tracking, you can adjust endpoint provisioning to fit your capacity needs based on usage.
- [Scheduled scaling](https://docs.aws.amazon.com/comprehend/latest/dg/ScheduledScaling.html): With scheduled scaling, you can adjust endpoint provisioning to fit your capacity needs on a specified schedule.


## [Tagging](https://docs.aws.amazon.com/comprehend/latest/dg/tagging.html)

- [Tagging a new resource](https://docs.aws.amazon.com/comprehend/latest/dg/tagging-newtags.html): You can add tags to an Analysis job, a Custom classification model, a Custom entity recognition model, or endpoints.
- [Viewing, editing, and deleting tags](https://docs.aws.amazon.com/comprehend/latest/dg/tagging-existingtags.html): You can view tags associated with an Analysis job, a Custom classification model, or a Custom entity recognition model.


## [Code examples](https://docs.aws.amazon.com/comprehend/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/comprehend/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Comprehend with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/comprehend/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Amazon Comprehend with AWS SDKs.

- [CreateDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_CreateDocumentClassifier_section.html): Use CreateDocumentClassifier with an AWS SDK or CLI
- [DeleteDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DeleteDocumentClassifier_section.html): Use DeleteDocumentClassifier with an AWS SDK or CLI
- [DescribeDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DescribeDocumentClassificationJob_section.html): Use DescribeDocumentClassificationJob with an AWS SDK or CLI
- [DescribeDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DescribeDocumentClassifier_section.html): Use DescribeDocumentClassifier with an AWS SDK or CLI
- [DescribeTopicsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DescribeTopicsDetectionJob_section.html): Use DescribeTopicsDetectionJob with an AWS SDK or CLI
- [DetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DetectDominantLanguage_section.html): Use DetectDominantLanguage with an AWS SDK or CLI
- [DetectEntities](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DetectEntities_section.html): Use DetectEntities with an AWS SDK or CLI
- [DetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DetectKeyPhrases_section.html): Use DetectKeyPhrases with an AWS SDK or CLI
- [DetectPiiEntities](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DetectPiiEntities_section.html): Use DetectPiiEntities with an AWS SDK or CLI
- [DetectSentiment](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DetectSentiment_section.html): Use DetectSentiment with an AWS SDK or CLI
- [DetectSyntax](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_DetectSyntax_section.html): Use DetectSyntax with an AWS SDK or CLI
- [ListDocumentClassificationJobs](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_ListDocumentClassificationJobs_section.html): Use ListDocumentClassificationJobs with an AWS SDK or CLI
- [ListDocumentClassifiers](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_ListDocumentClassifiers_section.html): Use ListDocumentClassifiers with an AWS SDK or CLI
- [ListTopicsDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_ListTopicsDetectionJobs_section.html): Use ListTopicsDetectionJobs with an AWS SDK or CLI
- [StartDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_StartDocumentClassificationJob_section.html): Use StartDocumentClassificationJob with an AWS SDK or CLI
- [StartTopicsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_StartTopicsDetectionJob_section.html): Use StartTopicsDetectionJob with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/comprehend/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Comprehend with AWS SDKs.

- [Build an Amazon Transcribe streaming app](https://docs.aws.amazon.com/comprehend/latest/dg/example_cross_TranscriptionStreamingApp_section.html): Build an Amazon Transcribe streaming app
- [Building an Amazon Lex chatbot](https://docs.aws.amazon.com/comprehend/latest/dg/example_cross_LexChatbotLanguages_section.html): Create an Amazon Lex chatbot to engage your website visitors
- [Create a messaging application](https://docs.aws.amazon.com/comprehend/latest/dg/example_cross_SQSMessageApp_section.html): Create a web application that sends and retrieves messages by using Amazon SQS
- [Create an application to analyze customer feedback](https://docs.aws.amazon.com/comprehend/latest/dg/example_cross_FSA_section.html): Create an application that analyzes customer feedback and synthesizes audio
- [Detect document elements](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_Usage_DetectApis_section.html): Detect document elements with Amazon Comprehend and an AWS SDK
- [Detect entities in text extracted from an image](https://docs.aws.amazon.com/comprehend/latest/dg/example_cross_TextractComprehendDetectEntities_section.html): Detect entities in text extracted from an image using an AWS SDK
- [Run a topic modeling job on sample data](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_Usage_TopicModeler_section.html): Run an Amazon Comprehend topic modeling job on sample data using an AWS SDK
- [Train a custom classifier and classify documents](https://docs.aws.amazon.com/comprehend/latest/dg/example_comprehend_Usage_ComprehendClassifier_section.html): Train a custom Amazon Comprehend classifier and classify documents using an AWS SDK


## [Security](https://docs.aws.amazon.com/comprehend/latest/dg/comp-security.html)

### [Data protection](https://docs.aws.amazon.com/comprehend/latest/dg/comp-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Comprehend.

- [KMS encryption in Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/kms-in-comprehend.html): Amazon Comprehend works with AWS Key Management Service (AWS KMS) to provide enhanced encryption for your data.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/comprehend/latest/dg/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Using a Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/comprehend/latest/dg/usingVPC.html): Amazon Comprehend uses a variety of security measures to ensure the safety of your data with our job containers where it's stored while being used by Amazon Comprehend.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/comprehend/latest/dg/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Comprehend without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.

### [Identity and Access Management](https://docs.aws.amazon.com/comprehend/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Amazon Comprehend resources.

- [How Amazon Comprehend works with IAM](https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Comprehend, learn what IAM features are available to use with Amazon Comprehend.
- [Identity-based policy examples](https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Comprehend resources.
- [AWS managed policies](https://docs.aws.amazon.com/comprehend/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Comprehend and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Comprehend and IAM.
- [Logging Amazon Comprehend API calls with AWS CloudTrail](https://docs.aws.amazon.com/comprehend/latest/dg/logging-using-cloudtrail.html): Amazon Comprehend is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Comprehend.
- [Compliance validation](https://docs.aws.amazon.com/comprehend/latest/dg/comp-compliance.html): Learn which compliance programs are in scope for Amazon Comprehend.
- [Resilience](https://docs.aws.amazon.com/comprehend/latest/dg/comp-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and which Amazon Comprehend features support data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/comprehend/latest/dg/comp-infrastructure-security.html): Learn how Amazon Comprehend isolates service traffic.


## [Tutorials](https://docs.aws.amazon.com/comprehend/latest/dg/resources.html)

### [Analyzing insights from reviews](https://docs.aws.amazon.com/comprehend/latest/dg/tutorial-reviews.html)

Learn how to perform sentiment and entities analysis with Amazon Comprehend and visualize the results.

- [Step 1: Adding documents to Amazon S3](https://docs.aws.amazon.com/comprehend/latest/dg/tutorial-reviews-add-docs.html): Before starting the Amazon Comprehend analysis jobs, you need to store a sample dataset of customer reviews in Amazon Simple Storage Service (Amazon S3).
- [Step 2: (CLI only) creating an IAM role](https://docs.aws.amazon.com/comprehend/latest/dg/tutorial-reviews-create-role.html): This step is necessary only if you are using the AWS Command Line Interface (AWS CLI) to complete this tutorial.
- [Step 3: Running analysis jobs](https://docs.aws.amazon.com/comprehend/latest/dg/tutorial-reviews-analysis.html): After storing the data in Amazon S3, you can begin running Amazon Comprehend analysis jobs.
- [Step 4: Preparing the output](https://docs.aws.amazon.com/comprehend/latest/dg/tutorial-reviews-tables.html): To prepare the results of the sentiment and entities analysis jobs for creating data visualizations, you use AWS Glue and Amazon Athena.
- [Step 5: Visualizing the output](https://docs.aws.amazon.com/comprehend/latest/dg/tutorial-reviews-visualize.html): After storing the Amazon Comprehend results in tables, you can connect to and visualize the data with Quick.
- [Using S3 object Lambda access points for PII](https://docs.aws.amazon.com/comprehend/latest/dg/using-access-points.html): In Amazon Comprehend, control access to documents that contain personally identifiable information (PII) or redact PII in documents that you analyze using Amazon S3 Object Lambda Access Points
- [Analyzing text with OpenSearch](https://docs.aws.amazon.com/comprehend/latest/dg/elasticsearch.html): Describes how to analyze text with Amazon Comprehend and OpenSearch Service.
