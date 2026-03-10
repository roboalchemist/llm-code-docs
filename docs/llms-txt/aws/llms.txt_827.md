# Source: https://docs.aws.amazon.com/transcribe/latest/dg/llms.txt

# Amazon Transcribe Developer Guide

> Convert speech to text with Amazon Transcribe.

- [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html)
- [Available features](https://docs.aws.amazon.com/transcribe/latest/dg/feature-matrix.html)
- [Job queueing](https://docs.aws.amazon.com/transcribe/latest/dg/job-queueing.html)
- [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html)
- [Alternative transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/alternatives.html)
- [Creating subtitles](https://docs.aws.amazon.com/transcribe/latest/dg/subtitles.html)
- [Transcribing Amazon Chime calls](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-chime.html)
- [Document history](https://docs.aws.amazon.com/transcribe/latest/dg/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/transcribe/latest/dg/glossary.html)

## [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html)

- [Character sets](https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html): Character sets for supported languages.


## [How it works](https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html)

- [Data input and output](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html): Learn about supported speech and audio input formats.
- [Transcribing numbers](https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html): Learn how Amazon Transcribe transcribes numbers and punctuation.


## [Getting started](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started.html)

- [Transcribing with the AWS Management Console](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-console.html): Describes how to get started with Amazon Transcribe using the AWS Management Console.
- [Transcribing with the AWS CLI](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-cli.html): Describes how to get started with Amazon Transcribe using the AWS CLI.
- [Transcribing with the AWS SDKs](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-sdk.html): Describes how to get started with Amazon Transcribe using HTTP and WebSockets.
- [Transcribing with HTTP or WebSockets](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-http-websocket.html): Describes how to get started with Amazon Transcribe using HTTP and WebSockets.


## [Streaming transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html)

- [Streaming and partial results](https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html): Streaming and partial results
- [Setting up a streaming transcription](https://docs.aws.amazon.com/transcribe/latest/dg/streaming-setting-up.html): Learn how to set up a transcription stream.


## [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html)

- [Example output](https://docs.aws.amazon.com/transcribe/latest/dg/diarization-output-batch.html): Here's an output example for a batch transcription with diarization enabled.


## [Transcribing multi-channel audio](https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html)

- [Example output](https://docs.aws.amazon.com/transcribe/latest/dg/channel-id-output-batch.html): Here's an output example for a batch transcription with channel identification enabled.


## [Identifying languages](https://docs.aws.amazon.com/transcribe/latest/dg/lang-id.html)

- [Batch language identification](https://docs.aws.amazon.com/transcribe/latest/dg/lang-id-batch.html): Use automatic language identification with batch transcription jobs.
- [Streaming language identification](https://docs.aws.amazon.com/transcribe/latest/dg/lang-id-stream.html): Use automatic language identification with streaming transcriptions.


## [Improving transcription accuracy](https://docs.aws.amazon.com/transcribe/latest/dg/improving-accuracy.html)

### [Custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html)

Learn how to create and use custom vocabularies with Amazon Transcribe.

- [Creating a custom vocabulary using a table](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html): Learn how to create and use custom vocabularies in table format with Amazon Transcribe.
- [Creating a custom vocabulary using a list](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-list.html): Learn how to create and use custom vocabularies in list format with Amazon Transcribe.
- [Using a custom vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-using.html): Learn how to create and use custom vocabularies in table format with Amazon Transcribe.

### [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html)

Train custom language models in order to improve transcription accuracy for domain-specific content.

- [Creating a custom language model](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models-create.html): Learn how to create custom language models with Amazon Transcribe.
- [Using a custom language model](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models-using.html): Learn how to create and use custom language models with Amazon Transcribe.


## [Filtering words](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html)

- [Creating a vocabulary filter](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filter-create.html): Learn how to create and use custom vocabulary filters with Amazon Transcribe.
- [Using a custom vocabulary filter](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filter-using.html): Learn how to create and use custom vocabulary filters with Amazon Transcribe.


## [Detecting toxic speech](https://docs.aws.amazon.com/transcribe/latest/dg/toxicity.html)

- [Using toxic speech detection](https://docs.aws.amazon.com/transcribe/latest/dg/toxicity-using.html): Learn how to flag and categorize toxic speech with Amazon Transcribe.


## [Redacting transcripts](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html)

- [Redacting PII in your batch job](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction-batch.html): Use redaction to mask or remove sensitive content, referred to as personally identifiable information (PII), from your batch transcription job.
- [Redacting or identifying PII in a real-time stream](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction-stream.html): Use redaction to mask or remove sensitive content, referred to as personally identifiable information (PII), from your streaming transcription.
- [Example output](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction-output.html): Use redaction to mask or remove sensitive content, referred to as personally identifiable information (PII), from your transcript.


## [Analyzing call center audio](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html)

### [Post-call analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics-batch.html)

Use custom Call Analytics to analyze spoken content in your media files.

- [Creating categories](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html): Create custom categories and rules with Amazon Transcribe Call Analytics.
- [Starting a transcription](https://docs.aws.amazon.com/transcribe/latest/dg/tca-start-batch.html): Use custom Call Analytics to analyze spoken content in your media files.
- [Post-call analytics output](https://docs.aws.amazon.com/transcribe/latest/dg/tca-output-batch.html): Example post-call analytics transcription output for Amazon Transcribe Call Analytics.
- [Enabling generative call summarization](https://docs.aws.amazon.com/transcribe/latest/dg/tca-enable-summarization.html): Example transcription output for post-call analytics from a real-time analytics request.

### [Real-time Call Analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics-streaming.html)

Use custom Call Analytics to analyze spoken content in your media streams.

- [Creating categories](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html): Create custom categories and rules with Amazon Transcribe Call Analytics.
- [Post-call analytics with real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html): Use post-call analytics to analyze spoken content in your media streams.
- [Starting a transcription](https://docs.aws.amazon.com/transcribe/latest/dg/tca-start-stream.html): Use custom Call Analytics to analyze spoken content in your media stream.
- [Real-time Call Analytics output](https://docs.aws.amazon.com/transcribe/latest/dg/tca-output-streaming.html): Example real-time Call Analytics transcription output for Amazon Transcribe Call Analytics.


## [Code examples](https://docs.aws.amazon.com/transcribe/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/transcribe/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Transcribe with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/transcribe/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Amazon Transcribe with AWS SDKs.

- [CreateVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_CreateVocabulary_section.html): Use CreateVocabulary with an AWS SDK or CLI
- [DeleteMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_DeleteMedicalTranscriptionJob_section.html): Use DeleteMedicalTranscriptionJob with an AWS SDK or CLI
- [DeleteTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_DeleteTranscriptionJob_section.html): Use DeleteTranscriptionJob with an AWS SDK or CLI
- [DeleteVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_DeleteVocabulary_section.html): Use DeleteVocabulary with an AWS SDK or CLI
- [GetTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_GetTranscriptionJob_section.html): Use GetTranscriptionJob with an AWS SDK or CLI
- [GetVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_GetVocabulary_section.html): Use GetVocabulary with an AWS SDK or CLI
- [ListMedicalTranscriptionJobs](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_ListMedicalTranscriptionJobs_section.html): Use ListMedicalTranscriptionJobs with an AWS SDK or CLI
- [ListTranscriptionJobs](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_ListTranscriptionJobs_section.html): Use ListTranscriptionJobs with an AWS SDK or CLI
- [ListVocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_ListVocabularies_section.html): Use ListVocabularies with an AWS SDK or CLI
- [StartMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_StartMedicalTranscriptionJob_section.html): Use StartMedicalTranscriptionJob with an AWS SDK or CLI
- [StartTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_StartTranscriptionJob_section.html): Use StartTranscriptionJob with an AWS SDK or CLI
- [UpdateVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_UpdateVocabulary_section.html): Use UpdateVocabulary with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/transcribe/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Transcribe with AWS SDKs.

- [Build an Amazon Transcribe streaming app](https://docs.aws.amazon.com/transcribe/latest/dg/example_cross_TranscriptionStreamingApp_section.html): Build an Amazon Transcribe streaming app
- [Convert text to speech and back to text](https://docs.aws.amazon.com/transcribe/latest/dg/example_cross_Telephone_section.html): Convert text to speech and back to text using an AWS SDK
- [Create and refine a custom vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_Scenario_CustomVocabulary_section.html): Create and refine an Amazon Transcribe custom vocabulary using an AWS SDK
- [Transcribe audio and get job data](https://docs.aws.amazon.com/transcribe/latest/dg/example_transcribe_Scenario_GettingStartedTranscriptionJobs_section.html): Transcribe audio and get job data with Amazon Transcribe using an AWS SDK


## [Security](https://docs.aws.amazon.com/transcribe/latest/dg/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/transcribe/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Amazon Transcribe resources.

- [How Amazon Transcribe works with IAM](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Transcribe, learn what IAM features are available to use with Amazon Transcribe.
- [Confused deputy prevention](https://docs.aws.amazon.com/transcribe/latest/dg/security-iam-confused-deputy.html): Confused deputy prevention when using multiple AWS services.
- [Identity-based policy examples](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html): Using identity-based policies with Amazon Transcribe.
- [Troubleshooting](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_troubleshoot.html): Troubleshooting Amazon Transcribe identity and access issues.

### [Data protection](https://docs.aws.amazon.com/transcribe/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Transcribe.

- [Data encryption](https://docs.aws.amazon.com/transcribe/latest/dg/data-encryption.html): Data encryption with Amazon Transcribe.
- [Opting out of using your data for service improvement](https://docs.aws.amazon.com/transcribe/latest/dg/opt-out.html): Opt out of allowing Amazon Transcribe to store your transcription output data and store it in your own Amazon S3 bucket instead.

### [Monitoring Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/monitoring-transcribe.html)

Monitor Amazon Transcribe to maintain reliability, availability, and performance.

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/transcribe/latest/dg/monitoring-cloudwatch.html): You can monitor Amazon Transcribe using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Monitoring Amazon Transcribe with CloudTrail](https://docs.aws.amazon.com/transcribe/latest/dg/monitoring-transcribe-cloud-trail.html): Amazon Transcribe is integrated with AWS CloudTrail, a service that provides a record of actions taken in Amazon Transcribe by an AWS Identity and Access Management (IAM) user or role, or by an AWS service.
- [Using Amazon EventBridge with Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/monitoring-events.html): Learn how to use Amazon EventBridge with Amazon Transcribe to route your transcription requests.
- [Compliance validation](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/transcribe/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Transcribe features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/transcribe/latest/dg/infrastructure-security.html): Learn how Amazon Transcribe isolates service traffic.
- [Vulnerability analysis and management](https://docs.aws.amazon.com/transcribe/latest/dg/vulnerability-analysis-and-management.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [Security best practices](https://docs.aws.amazon.com/transcribe/latest/dg/security-best-practices.html): Security Best Practices for Amazon Transcribe


## [Amazon Transcribe Medical](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-medical.html)

### [Medical specialties](https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works-med.html)

Learn how Amazon Transcribe Medical works.

- [Transcribing medical terms and measurements](https://docs.aws.amazon.com/transcribe/latest/dg/how-measurements-med.html): Amazon Transcribe Medical can transcribe medical terms and measurements.
- [Transcribing numbers](https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers-med.html): Amazon Transcribe Medical transcribes digits as numbers instead of words.

### [Transcribing a medical conversation](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-medical-conversation.html)

Use Amazon Transcribe Medical to transcribe a medical conversation between a clinician and a patient.

- [Transcribing an audio file](https://docs.aws.amazon.com/transcribe/latest/dg/batch-medical-conversation.html): Use Amazon Transcribe Medical to transcribe audio files of medical conversations.
- [Transcribing a real-time stream](https://docs.aws.amazon.com/transcribe/latest/dg/streaming-medical-conversation.html): Transcribe a real-time stream of a medical conversation in Amazon Transcribe Medical.

### [Enabling speaker partitioning](https://docs.aws.amazon.com/transcribe/latest/dg/conversation-diarization-med.html)

Use Amazon Transcribe Medical speaker diarization to enable speaker partitioning.

- [Enabling speaker partitioning in batch transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/conversation-diarization-batch-med.html): Use Amazon Transcribe Medical speaker diarization to partition the text per speaker and attribute the transcribed speech of those speakers when you transcribe audio files.
- [Partitioning speakers in real-time streams](https://docs.aws.amazon.com/transcribe/latest/dg/conversation-diarization-streaming-med.html): Use speaker diarization in Amazon Transcribe Medical to enable speaker partitioning in real-time streams.
- [Transcribing multi-channel audio](https://docs.aws.amazon.com/transcribe/latest/dg/conversation-channel-id-med.html): If you have an audio file or stream that has multiple channels, you can use channel identification to transcribe the speech from each of those channels.

### [Transcribing a medical dictation](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-medical-dictation.html)

Use Amazon Transcribe Medical to transcribe a clinician dictating notes after a patient visit.

- [Transcribing an audio file](https://docs.aws.amazon.com/transcribe/latest/dg/batch-medical-dictation.html): Use a batch transcription job to transcribe audio files of medical conversations.
- [Transcribing a streaming medical dictation](https://docs.aws.amazon.com/transcribe/latest/dg/streaming-medical-dictation.html): Transcribe a real-time stream of a medical dictation in Amazon Transcribe Medical.

### [Creating and using medical custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-med.html)

In Amazon Transcribe Medical, you can create and use medical custom vocabularies to improve transcription accuracy.

- [Creating a text file for your medical custom vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/create-med-vocab-text.html): To create a custom vocabulary, you create a text file that is in UTF-8 format.
- [Using a text file to create a medical custom vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/create-med-custom-vocabulary.html): To create a custom vocabulary, you must have prepared a text file that contains a collection a words or phrases.
- [Transcribing an audio file using a medical custom vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/start-med-custom-vocab-job.html): Use the StartMedicalTranscriptionJob or the AWS Management Console to start a transcription job that uses a custom vocabulary to improve transcription accuracy.
- [Transcribing a real-time stream using a medical custom vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/start-med-vocab-stream.html): To improve transcription accuracy in a real-time stream, you can use a custom vocabulary using either HTTP/2 or WebSocket streams.
- [Character set for Amazon Transcribe Medical](https://docs.aws.amazon.com/transcribe/latest/dg/charsets-med.html): To use custom vocabularies in Amazon Transcribe Medical, use the following character set.

### [Identifying PHI in a transcript](https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html)

Use Personal Health Information (PHI) Identification in Amazon Transcribe Medical to label information that could be used to identify a patient in the streaming transcription output.

- [Identifying PHI in an audio file](https://docs.aws.amazon.com/transcribe/latest/dg/phi-id-batch.html): Use a batch transcription job to transcribe audio files and identify the personal health information (PHI) within them.
- [Identifying PHI in a real-time stream](https://docs.aws.amazon.com/transcribe/latest/dg/phi-id-stream.html): You can identify Personal Health Information (PHI) in either HTTP/2 or WebSocket streams.
- [Generating alternative transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/alternative-med-transcriptions.html): You can generate alternative transcriptions in Amazon Transcribe Medical.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/transcribe/latest/dg/med-vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Transcribe Medical without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [AWS HealthScribe](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html)

- [Transcript file](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-transcript.html): In the transcript file, in addition to standard turn-by-turn transcription output with word level timestamps, AWS HealthScribe provides you with:
- [Clinical Documentation file](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-insights.html): AWS HealthScribe can use one of the following templates for the clinical note summary.

### [Transcription jobs](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-job.html)

An AWS HealthScribe transcription job processes media files from an Amazon S3 bucket.

- [Starting an AWS HealthScribe transcription job](https://docs.aws.amazon.com/transcribe/latest/dg/starting-health-scribe-job.html): You can start an AWS HealthScribe job using the AWS CLI or AWS SDKs.

### [Streaming](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-streaming.html)

Learn how AWS HealthScribe streaming works.

- [Starting AWS HealthScribe streaming transcription](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-streaming-setting-up.html): The following code example shows how to set up a AWS HealthScribe streaming transcription using the AWS SDKs.

### [Data Encryption at rest for AWS HealthScribe](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-encryption.html)

By default, AWS HealthScribe provides encryption at rest to protect sensitive customer data using AWS HealthScribe managed AWS Key Management Service (AWS KMS) keys.

- [Creating a customer managed key](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-encryption-customer.html): You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs.
