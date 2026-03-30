# Source: https://docs.aws.amazon.com/translate/latest/dg/llms.txt

# Amazon Translate Developer Guide

> Translate text with Amazon Translate.

- [What is Amazon Translate?](https://docs.aws.amazon.com/translate/latest/dg/what-is.html)
- [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)
- [How it works](https://docs.aws.amazon.com/translate/latest/dg/how-it-works.html)
- [Guidelines and quotas](https://docs.aws.amazon.com/translate/latest/dg/what-is-limits.html)
- [Document history](https://docs.aws.amazon.com/translate/latest/dg/doc-history.html)
- [API reference](https://docs.aws.amazon.com/translate/latest/dg/api_reference.html)
- [AWS Glossary](https://docs.aws.amazon.com/translate/latest/dg/glossary.html)

## [Setting up](https://docs.aws.amazon.com/translate/latest/dg/setting-up.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/translate/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Getting started](https://docs.aws.amazon.com/translate/latest/dg/getting-started.html)

- [Getting started (console)](https://docs.aws.amazon.com/translate/latest/dg/get-started-console.html): The easiest way to get started with Amazon Translate is to use the console to translate some text.
- [Getting started (AWS CLI)](https://docs.aws.amazon.com/translate/latest/dg/get-started-cli.html): In the following exercise, you use the AWS command line interface (AWS CLI) to translate text.
- [Getting started (SDK)](https://docs.aws.amazon.com/translate/latest/dg/get-started-sdk.html): AWS provides SDKs for various computer languages.


## [Translation processing modes](https://docs.aws.amazon.com/translate/latest/dg/processing.html)

### [Real-time translation](https://docs.aws.amazon.com/translate/latest/dg/sync.html)

Amazon Translate provides real-time document and text translation operations that immediately return the translations.

- [Real-time translation (console)](https://docs.aws.amazon.com/translate/latest/dg/sync-console.html): To use the console for real-time translations, paste input text into the Source language text box or provide the input text as a file.
- [Real-time translation (API)](https://docs.aws.amazon.com/translate/latest/dg/sync-api.html): Amazon Translate provides the following real-time translation operations to support interactive applications:

### [Asynchronous batch processing](https://docs.aws.amazon.com/translate/latest/dg/async.html)

To translate large collections of documents (up to 5 GB in size), use the Amazon Translate asynchronous batch processing operation, StartTextTranslationJob.

- [Prerequisites](https://docs.aws.amazon.com/translate/latest/dg/async-prereqs.html): The following prerequisites must be met in order for Amazon Translate to perform a successful batch translation job:
- [Running a job](https://docs.aws.amazon.com/translate/latest/dg/async-start.html): Learn how to run a batch translation job.
- [Monitoring and analyzing](https://docs.aws.amazon.com/translate/latest/dg/async-monitor.html): You can use a job's ID to monitor its progress and get the Amazon S3 location of its output documents.
- [Getting results](https://docs.aws.amazon.com/translate/latest/dg/async-results.html): Once the job's status is COMPLETED or COMPLETED_WITH_ERROR, your output documents are available in the Amazon S3 folder you specified.


## [Customizing your translations](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations.html)

- [Using do-not-translate tags](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-tags.html): Learn how to use do-not-translate tags in Amazon Translate.

### [Customizing with custom terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html)

Use custom terminologies along with your translation requests to make sure that your brand names, character names, model names, and other unique content get translated to the desired result.

- [Creating a custom terminology](https://docs.aws.amazon.com/translate/latest/dg/creating-custom-terminology.html): You define custom terminology by creating a terminology file.
- [Using custom terminologies](https://docs.aws.amazon.com/translate/latest/dg/using-ct.html): To use a Custom Terminology when translating text with the TranslateText operation, include the optional TerminologyNames parameter.
- [Example using SDK for Python](https://docs.aws.amazon.com/translate/latest/dg/examples-ct.html): The following example shows how to use the Custom Terminology operations in Python.
- [Encrypting your terminology](https://docs.aws.amazon.com/translate/latest/dg/protect-terminology.html): Amazon Translate endeavors to protect all your data and your custom terminologies are no different.
- [Best practices](https://docs.aws.amazon.com/translate/latest/dg/ct-best-practices.html): Use following general best practices when using custom terminologies:
- [Using brevity](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-brevity.html): When translating between languages, there are times when the translation output is longer (in character count) than desired.
- [Masking profanity](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-profanity.html): When you run translations with Amazon Translate, you can enable the profanity setting to mask profane words and phrases in your translation output.
- [Setting formality](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html): Learn how to specify the formality level of your translation output.

### [Customizing with parallel data](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data.html)

Influence the translations from Amazon Translate by providing parallel data, which contains example segments of source text and their translations.

- [Parallel data input files for Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data-input-files.html): Format your translation examples in an input file so that you can add parallel data to Amazon Translate.
- [Adding parallel data](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data-adding.html): Add parallel data to Amazon Translate by importing a file that contains translation examples.
- [Viewing and managing parallel data](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data-managing.html): Use Amazon Translate to view your parallel data resources, access detailed summaries of them, and update them.


## [Code examples](https://docs.aws.amazon.com/translate/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/translate/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Translate with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/translate/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Amazon Translate with AWS SDKs.

- [DescribeTextTranslationJob](https://docs.aws.amazon.com/translate/latest/dg/example_translate_DescribeTextTranslationJob_section.html): Use DescribeTextTranslationJob with an AWS SDK
- [ListTextTranslationJobs](https://docs.aws.amazon.com/translate/latest/dg/example_translate_ListTextTranslationJobs_section.html): Use ListTextTranslationJobs with an AWS SDK
- [StartTextTranslationJob](https://docs.aws.amazon.com/translate/latest/dg/example_translate_StartTextTranslationJob_section.html): Use StartTextTranslationJob with an AWS SDK
- [StopTextTranslationJob](https://docs.aws.amazon.com/translate/latest/dg/example_translate_StopTextTranslationJob_section.html): Use StopTextTranslationJob with an AWS SDK
- [TranslateText](https://docs.aws.amazon.com/translate/latest/dg/example_translate_TranslateText_section.html): Use TranslateText with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/translate/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Translate with AWS SDKs.

- [Build an Amazon Transcribe streaming app](https://docs.aws.amazon.com/translate/latest/dg/example_cross_TranscriptionStreamingApp_section.html): Build an Amazon Transcribe streaming app
- [Building an Amazon Lex chatbot](https://docs.aws.amazon.com/translate/latest/dg/example_cross_LexChatbotLanguages_section.html): Create an Amazon Lex chatbot to engage your website visitors
- [Building an Amazon SNS application](https://docs.aws.amazon.com/translate/latest/dg/example_cross_SnsPublishSubscription_section.html): Build a publish and subscription application that translates messages
- [Create an application to analyze customer feedback](https://docs.aws.amazon.com/translate/latest/dg/example_cross_FSA_section.html): Create an application that analyzes customer feedback and synthesizes audio
- [Get started with translate jobs](https://docs.aws.amazon.com/translate/latest/dg/example_translate_Scenario_GettingStarted_section.html): Get started with Amazon Translate jobs using an AWS SDK


## [Tagging](https://docs.aws.amazon.com/translate/latest/dg/tagging.html)

- [Tagging a new resource](https://docs.aws.amazon.com/translate/latest/dg/tagging-newtags.html): Learn how to modify or delete tags in a resource in Amazon Translate.
- [Viewing, editing, and deleting tags](https://docs.aws.amazon.com/translate/latest/dg/tagging-existingtags.html): Learn how to add tags to your resources in Amazon Translate.


## [Security](https://docs.aws.amazon.com/translate/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/translate/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Translate.

- [Encryption at rest](https://docs.aws.amazon.com/translate/latest/dg/encryption-at-rest.html): For the batch translation jobs that you run with Amazon Translate, your translation input and output are both encrypted at rest.
- [Encryption in transit](https://docs.aws.amazon.com/translate/latest/dg/encryption-in-transit.html): To encrypt data in transit, Amazon Translate uses TLS 1.2 with AWS certificates.

### [Identity and Access Management](https://docs.aws.amazon.com/translate/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Amazon Translate resources.

- [How Amazon Translate works with IAM](https://docs.aws.amazon.com/translate/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Translate, learn what IAM features are available to use with Amazon Translate.
- [Identity-based policy examples](https://docs.aws.amazon.com/translate/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Translate resources.
- [AWS managed policies](https://docs.aws.amazon.com/translate/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Translate.
- [Troubleshooting](https://docs.aws.amazon.com/translate/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Translate and IAM.

### [Monitoring](https://docs.aws.amazon.com/translate/latest/dg/monitoring-translate.html)

Learn how to monitor the performance of your Amazon Translate solution.

- [Logging Amazon Translate API calls with AWS CloudTrail](https://docs.aws.amazon.com/translate/latest/dg/logging-using-cloudtrail.html): Learn about logging Amazon Translate API calls with AWS CloudTrail.
- [CloudWatch metrics and dimensions for Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/translate-cloudwatch.html): To monitor your solution's performance, use the Amazon CloudWatch metrics and dimensions for Amazon Translate.
- [Monitoring with EventBridge](https://docs.aws.amazon.com/translate/latest/dg/monitoring-with-eventbridge.html): Automate Amazon Translate with other AWS services by using EventBridge.
- [Compliance validation](https://docs.aws.amazon.com/translate/latest/dg/compliance.html): Learn which compliance programs are in scope for Amazon Translate.
- [Resilience](https://docs.aws.amazon.com/translate/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and which Amazon Translate features support data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/translate/latest/dg/infrastructure-security.html): Learn how Amazon Translate isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/translate/latest/dg/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Translate without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
