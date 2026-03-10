# Source: https://docs.aws.amazon.com/polly/latest/dg/llms.txt

# Amazon Polly Developer Guide

> Amazon Polly Developer Guide, a cloud service that converts text into lifelike speech.

- [Synthesizing speech example](https://docs.aws.amazon.com/polly/latest/dg/synthesize-example.html)
- [Quotas](https://docs.aws.amazon.com/polly/latest/dg/limits.html)
- [Logging Amazon Polly API calls with AWS CloudTrail](https://docs.aws.amazon.com/polly/latest/dg/logging-using-cloudtrail.html)
- [CloudWatch integration](https://docs.aws.amazon.com/polly/latest/dg/cloud-watch.html)
- [Document History](https://docs.aws.amazon.com/polly/latest/dg/doc-history.html)

## [What Is Amazon Polly?](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)

- [How it works](https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html): Overview of the Amazon Polly text-to-speech service.
- [Benefits](https://docs.aws.amazon.com/polly/latest/dg/benefits.html): Some of the benefits of using Amazon Polly include:
- [Are you a first-time user?](https://docs.aws.amazon.com/polly/latest/dg/first-time-user.html): If you're a first-time user of Amazon Polly, we recommend that you read the following sections in the listed order:
- [Working with AWS SDKs](https://docs.aws.amazon.com/polly/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Getting started](https://docs.aws.amazon.com/polly/latest/dg/getting-started.html)

- [Signing up for AWS](https://docs.aws.amazon.com/polly/latest/dg/signup.html): Before you can use any AWS service, including Amazon Polly, you must sign up for AWS.
- [Setting up the AWS CLI](https://docs.aws.amazon.com/polly/latest/dg/setup-cli.html): Follow these steps to download and configure the AWS CLI to work with Amazon Polly.
- [Reconfiguring the AWS CLI](https://docs.aws.amazon.com/polly/latest/dg/reconfigure-cli.html): If you've previously downloaded and configured the AWS CLI, Amazon Polly might be unavailable unless you reconfigure the AWS CLI.


## [Voices in Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/voices-in-polly.html)

- [Available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html): Amazon Polly provides a variety of lifelike voices in multiple languages for synthesizing speech from text.
- [Bilingual voices](https://docs.aws.amazon.com/polly/latest/dg/bilingual-voices.html): Amazon Polly has two ways of producing bilingual voices:
- [Applying the newscaster voice](https://docs.aws.amazon.com/polly/latest/dg/newscaster-voices.html): People use different speaking styles, depending on context.
- [Listening to voices](https://docs.aws.amazon.com/polly/latest/dg/listen-to-voices.html): Once you have set up Amazon Polly, you can test voices using custom text on the console.
- [Timing a voice speed](https://docs.aws.amazon.com/polly/latest/dg/voice-speed-vip.html): Because of the natural variation between voices, each available voice speaks at slightly different speeds.
- [Changing a voice speed](https://docs.aws.amazon.com/polly/latest/dg/voice-speed-change-vip.html): For certain applications, you may find that you'd prefer the voice you like be slowed down, or speeded up.


## [Languages in Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/supported-languages.html)

- [Arabic (arb)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-arabic.html): Arabic
- [Arabic (Gulf) (ar-AE)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-arabic-gulf.html): Arabic (Gulf)
- [Catalan (ca-ES)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-catalan.html): Catalan
- [Chinese (Cantonese) (yue-CN)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-cantonese.html): Chinese (Cantonese)
- [Chinese (Mandarin) (cmn-CN)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-mandarin.html): Chinese (Mandarin)
- [Czech (cs-CZ)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-czech-cs-cz.html): Czech (cs-CZ)
- [Danish (da-DK)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-danish.html): Danish
- [Dutch (Belgian) (nl-BE)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-dutch-belgian.html): Belgian Dutch (Flemish)
- [Dutch (nl-NL)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-dutch.html): Dutch
- [English (US) (en-US)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-us.html): English (US)
- [English (Australian) (en-AU)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-au.html): English (Australian)
- [English (British) (en-GB)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-uk.html): English (British)
- [English (Indian) (en-IN)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-in.html): English (Indian) (es-IN)
- [English (Ireland) (en-IE)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-ie.html): English (Ireland)
- [English (New Zealand) (en-NZ)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-nz.html): English (New Zealand)
- [English (Singaporean) (en-SG)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-sg.html): English (Singaporean)
- [English (South African) (en-ZA)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-za.html): English (South African)
- [English (Welsh) (en-GB-WLS)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-english-wls.html): English (Welsh)
- [Finnish (fi-FI)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-finnish.html): Finnish
- [French (fr-FR)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-french.html): French
- [French (Belgian) (fr-BE)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-french-be.html): French (Belgian)
- [French (Canadian) (fr-CA)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-french-ca.html): French (Canadian)
- [German (de-DE)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-german.html): German
- [German (Austrian) (de-AT)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-german-at.html): German (Austrian)
- [German (Swiss standard) (de-CH)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-german-ch.html): German (Swiss standard) (dh-CH)
- [Hindi (hi-IN)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-hindi.html): Hindi
- [Icelandic (is-IS)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-icelandic.html): Icelandic
- [Italian (it-IT)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-italian.html): Italian
- [Japanese (ja-JP)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-japanese.html): Japanese
- [Korean (ko-KR)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-korean.html): Korean
- [Norwegian (nb-NO)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-norwegian.html): Norwegian
- [Polish (pl-PL)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-polish.html): Polish
- [Portuguese (pt-PT)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-portuguese.html): Portuguese
- [Portuguese (Brazilian) (pt-BR)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-portuguese-br.html): Portuguese (Brazilian)
- [Romanian (ro-RO)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-romanian.html): Romanian
- [Russian (ru-RU)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-russian.html): Russian
- [Spanish (es-ES)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-spanish.html): Spanish
- [Spanish (Mexican) (es-MX)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-mexican.html): Spanish (Mexican)
- [Spanish (US) (es-US)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-spanish-us.html): Spanish (US)
- [Swedish (sv-SE)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-swedish.html): Swedish
- [Turkish (tr-TR)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-turkish.html): Turkish
- [Welsh (cy-GB)](https://docs.aws.amazon.com/polly/latest/dg/ph-table-welsh.html): Welsh


## [Voice engines](https://docs.aws.amazon.com/polly/latest/dg/voice-engines-polly.html)

- [Generative engine](https://docs.aws.amazon.com/polly/latest/dg/generative-voices.html): Amazon Polly's generative text-to-speech (TTS) engine offers the most human-like, emotionally engaged, and adaptive conversational voices available for the use via the Amazon Polly console.
- [Long-form engine](https://docs.aws.amazon.com/polly/latest/dg/long-form-voices.html): Amazon Polly has a Long-form engine that produces human-like, highly expressive, and emotionally adept voices.
- [Neural engine](https://docs.aws.amazon.com/polly/latest/dg/neural-voices.html): Amazon Polly has a Neural text-to-speech (NTTS) engine that can produce even higher quality voices than its standard voices.
- [Standard engine](https://docs.aws.amazon.com/polly/latest/dg/standard-voices.html): Overview of standard voices here, followed by feature overview, and available voices.
- [Choosing a voice engine](https://docs.aws.amazon.com/polly/latest/dg/using-voices.html): You can access Amazon Polly voices through the Amazon Polly console or AWS CLI.


## [Speech marks](https://docs.aws.amazon.com/polly/latest/dg/speechmarks.html)

- [Speech mark types](https://docs.aws.amazon.com/polly/latest/dg/using-speechmarks.html): Using speech marks with Amazon Polly
- [Visemes and Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/viseme.html): Visemes and Amazon Polly
- [Speech mark output](https://docs.aws.amazon.com/polly/latest/dg/output.html): Amazon Polly returns speech mark objects in a line-delimited JSON stream.
- [Requesting speech marks](https://docs.aws.amazon.com/polly/latest/dg/speechmarksconsole.html): Requesting Speech Marks Using the Amazon Polly console or AWS CLI
- [Speech marks without SSML example](https://docs.aws.amazon.com/polly/latest/dg/sp-mks-example1.html): The following example shows you what requested metadata looks like on your screen for the simple sentence: "Mary had a little lamb." For simplicity, we don't include SSML speech marks in this example.
- [Speech marks with SSML example](https://docs.aws.amazon.com/polly/latest/dg/sp-mks-example2.html): The process of generating speech marks from SSML-enhanced text is similar to the process when SSML is not present.


## [Using SSML](https://docs.aws.amazon.com/polly/latest/dg/ssml.html)

- [Reserved characters](https://docs.aws.amazon.com/polly/latest/dg/escapees.html): There are five predefined characters that can't normally be used within an SSML statement.
- [Using SSML on the console](https://docs.aws.amazon.com/polly/latest/dg/ssml-to-speech-console.html): In the following example, you use an SSML tag to tell Amazon Polly to substitute "World Wide Web Consortium" for "W3C" when it speaks a short paragraph.
- [Using SSML with the Synthesize-Speech command](https://docs.aws.amazon.com/polly/latest/dg/example-ssml-synthesize-speech-cli.html): This example shows how to use the synthesize-speech command with an SSML string.
- [Synthesizing an SSML-enhanced document](https://docs.aws.amazon.com/polly/latest/dg/example-ssml-synthesize-document.html): Learn how to use Amazon Polly to synthesize speech for a complete SSML-enhanced document.

### [Supported SSML tags](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html)

All tags except for <amazon:domain name="news"> are supported for Standard voices.

- [Identifying SSML-enhanced text](https://docs.aws.amazon.com/polly/latest/dg/speak-tag.html): <speak>
- [Adding a pause](https://docs.aws.amazon.com/polly/latest/dg/break-tag.html): <break>
- [Emphasizing words](https://docs.aws.amazon.com/polly/latest/dg/emphasis-tag.html): <emphasis>
- [Specifying another language for specific words](https://docs.aws.amazon.com/polly/latest/dg/lang-tag.html): <lang>
- [Placing a custom tag in your text](https://docs.aws.amazon.com/polly/latest/dg/custom-tag.html): <mark>
- [Adding a pause between paragraphs](https://docs.aws.amazon.com/polly/latest/dg/p-tag.html): <p>
- [Using phonetic pronunciation](https://docs.aws.amazon.com/polly/latest/dg/phoneme-tag.html): <phoneme>
- [Controlling volume, speaking rate, and pitch](https://docs.aws.amazon.com/polly/latest/dg/prosody-tag.html): <prosody>
- [Setting a maximum duration for synthesized speech](https://docs.aws.amazon.com/polly/latest/dg/maxduration-tag.html): <prosody amazon:max-duration>
- [Adding a pause between sentences](https://docs.aws.amazon.com/polly/latest/dg/s-tag.html): <s>
- [Controlling how special types of words are spoken](https://docs.aws.amazon.com/polly/latest/dg/say-as-tag.html): <say-as>
- [Pronouncing acronyms and abbreviations](https://docs.aws.amazon.com/polly/latest/dg/sub-tag.html): <sub>
- [Improving pronunciation by specifying parts of speech](https://docs.aws.amazon.com/polly/latest/dg/w-tag.html): <w>
- [Adding the sound of breathing](https://docs.aws.amazon.com/polly/latest/dg/breath-tag.html): <amazon:breath> and <amazon:auto-breaths>
- [Newscaster speaking style](https://docs.aws.amazon.com/polly/latest/dg/newscaster-tag.html): <amazon:domain name="news">
- [Adding dynamic range compression](https://docs.aws.amazon.com/polly/latest/dg/drc-tag.html): <amazon:effect name="drc">
- [Speaking softly](https://docs.aws.amazon.com/polly/latest/dg/phonation-tag.html): <amazon:effect phonation="soft">
- [Controlling timbre](https://docs.aws.amazon.com/polly/latest/dg/vocaltractlength-tag.html): <amazon:effect vocal-tract-length>
- [Whispering](https://docs.aws.amazon.com/polly/latest/dg/whispered-tag.html): <amazon:effect name="whispered">


## [Managing lexicons](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html)

- [Using multiple lexicons](https://docs.aws.amazon.com/polly/latest/dg/lexicons-applying.html): Instructions on applying pronunciation lexicons to Amazon Polly.
- [Uploading a lexicon](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons-console-upload.html): The lexicons you use must conform to the Pronunciation Lexicon Specification (PLS) W3C recommendation.
- [Applying lexicons (Synthesizing Speech)](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons-console-synthesize-speech.html): The lexicons you use must conform to the Pronunciation Lexicon Specification (PLS) W3C recommendation.
- [Filtering the lexicon list on the console](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons-console-filter.html): The following procedure describes how to filter the lexicons list so that only lexicons of a chosen language are displayed.
- [Downloading lexicons on the console](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons-console-download.html): The following process describes how to download one or more lexicons.
- [Deleting a lexicon](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons-console-delete.html): The following process describes how to delete a lexicon.


## [Long audio files](https://docs.aws.amazon.com/polly/latest/dg/asynchronous.html)

- [Setting up the IAM policy for asynchronous synthesis](https://docs.aws.amazon.com/polly/latest/dg/asynchronous-iam.html): In order to use the asynchronous synthesis functionality, you will need an IAM policy that allows the following:
- [Creating long audio files](https://docs.aws.amazon.com/polly/latest/dg/longer-console.html): You can use the Amazon Polly console to create long speeches using asynchronous synthesis with the same functionality as you can use with the AWS CLI.


## [Sample code and applications](https://docs.aws.amazon.com/polly/latest/dg/samples-and-examples.html)

### [Java samples](https://docs.aws.amazon.com/polly/latest/dg/java-samples.html)

The following code samples show how to use Java-based applications to accomplish various tasks with Amazon Polly.

- [DeleteLexicon](https://docs.aws.amazon.com/polly/latest/dg/DeleteLexiconSample.html): The following Java code sample show how to use Java-based applications to delete a specific lexicon stored in an AWS Region.
- [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/DescribeVoicesSample.html): The following Java code sample show how to use Java-based applications to produce a list of the voices that are available for use when requesting speech synthesis.
- [GetLexicon](https://docs.aws.amazon.com/polly/latest/dg/GetLexiconSample.html): The following Java code sample show how to use Java-based applications to produce the content of a specific pronunciation lexicon stored in a AWS Region.
- [ListLexicons](https://docs.aws.amazon.com/polly/latest/dg/ListLexiconsSample.html): The following Java code sample shows how to use Java-based applications to produce a list of pronunciation lexicons stored in an AWS Region.
- [PutLexicon](https://docs.aws.amazon.com/polly/latest/dg/PutLexiconSample.html): The following Java code sample show how to use Java-based applications to store a pronunciation lexicon in an AWS Region.
- [StartSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/StartSpeechSynthesisTask.html): The following Java code sample show how to use Java-based applications to synthesize a long speech (up to 100,000 billed characters) and store it directly in an Amazon S3 bucket.
- [Speech Marks](https://docs.aws.amazon.com/polly/latest/dg/SynthesizeSpeechMarksSample.html): The following code sample shows how to use Java-based applications to synthesize speech marks for inputed text.
- [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dg/SynthesizeSpeechSample.html): The following Java code sample show how to use Java-based applications to synthesize speech with shorter texts for near-real time processing.

### [Python samples](https://docs.aws.amazon.com/polly/latest/dg/python-samples.html)

The following code samples show how to use Python (boto3)-based applications to accomplish various tasks with Amazon Polly.

- [DeleteLexicon](https://docs.aws.amazon.com/polly/latest/dg/DeleteLexiconPython.html): The following Python code example uses the AWS SDK for Python (Boto) to delete a lexicon in the region specified in your local AWS configuration.
- [GetLexicon](https://docs.aws.amazon.com/polly/latest/dg/GetLexiconSamplePython.html): The following Python code uses the AWS SDK for Python (Boto) to retrieve all lexicons stored in an AWS Region.
- [ListLexicon](https://docs.aws.amazon.com/polly/latest/dg/ListLexiconSamplePython.html): The following Python code example uses the AWS SDK for Python (Boto) to list the lexicons in your account in the region specified in your local AWS configuration.
- [PutLexicon](https://docs.aws.amazon.com/polly/latest/dg/PutLexiconSamplePython.html): The following code sample show how to use Python (boto3)-based applications to store a pronunciation lexicon in an AWS Region.
- [StartSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/StartSpeechSynthesisTaskSamplePython.html): The following Python code example uses the AWS SDK for Python (Boto) to list the lexicons in your account in the region specified in your local AWS configuration.
- [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dg/SynthesizeSpeechSamplePython.html): The following Python code example uses the AWS SDK for Python (Boto) synthesize speech with shorter texts for near real-time processing.
- [Java example](https://docs.aws.amazon.com/polly/latest/dg/examples-java.html): This example shows how to use Amazon Polly to stream speech from a Java-based application.

### [Python example](https://docs.aws.amazon.com/polly/latest/dg/examples-python.html)

This example application consists of the following:

- [Python example: index.html](https://docs.aws.amazon.com/polly/latest/dg/example-html-app.html): This section provides the code for the HTML5 client described in .
- [Python example: server.py](https://docs.aws.amazon.com/polly/latest/dg/example-Python-server-code.html): This section provides the code for the Python server described in .
- [iOS example](https://docs.aws.amazon.com/polly/latest/dg/examples-ios.html): The following example uses the iOS SDK for Amazon Polly to read the specified text using a voice selected from a list of voices.
- [Android example](https://docs.aws.amazon.com/polly/latest/dg/examples-android.html): The following example uses the Android SDK for Amazon Polly to read the specified text using a voice selected from a list of voices.


## [Code examples](https://docs.aws.amazon.com/polly/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/polly/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Polly with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/polly/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Amazon Polly with AWS SDKs.

- [DeleteLexicon](https://docs.aws.amazon.com/polly/latest/dg/example_polly_DeleteLexicon_section.html): Use DeleteLexicon with an AWS SDK or CLI
- [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/example_polly_DescribeVoices_section.html): Use DescribeVoices with an AWS SDK
- [GetLexicon](https://docs.aws.amazon.com/polly/latest/dg/example_polly_GetLexicon_section.html): Use GetLexicon with an AWS SDK or CLI
- [GetSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/example_polly_GetSpeechSynthesisTask_section.html): Use GetSpeechSynthesisTask with an AWS SDK or CLI
- [ListLexicons](https://docs.aws.amazon.com/polly/latest/dg/example_polly_ListLexicons_section.html): Use ListLexicons with an AWS SDK or CLI
- [ListSpeechSynthesisTasks](https://docs.aws.amazon.com/polly/latest/dg/example_polly_ListSpeechSynthesisTasks_section.html): Use ListSpeechSynthesisTasks with an AWS SDK or CLI
- [PutLexicon](https://docs.aws.amazon.com/polly/latest/dg/example_polly_PutLexicon_section.html): Use PutLexicon with an AWS SDK or CLI
- [StartSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/example_polly_StartSpeechSynthesisTask_section.html): Use StartSpeechSynthesisTask with an AWS SDK or CLI
- [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dg/example_polly_SynthesizeSpeech_section.html): Use SynthesizeSpeech with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/polly/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Polly with AWS SDKs.

- [Convert text to speech and back to text](https://docs.aws.amazon.com/polly/latest/dg/example_cross_Telephone_section.html): Convert text to speech and back to text using an AWS SDK
- [Create a lip-sync application](https://docs.aws.amazon.com/polly/latest/dg/example_polly_LipSync_section.html): Create a lip-sync application with Amazon Polly using an AWS SDK
- [Create an application to analyze customer feedback](https://docs.aws.amazon.com/polly/latest/dg/example_cross_FSA_section.html): Create an application that analyzes customer feedback and synthesizes audio


## [Security](https://docs.aws.amazon.com/polly/latest/dg/security.html)

### [Data Protection](https://docs.aws.amazon.com/polly/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Polly.

- [Encryption at Rest](https://docs.aws.amazon.com/polly/latest/dg/encryption-at-rest.html): Output of your Amazon Polly voice synthesis can be saved on your own system.
- [Encryption in Transit](https://docs.aws.amazon.com/polly/latest/dg/encryption-in-transit.html): All text submissions are protected by TLS while in transit.
- [Internetwork Traffic Privacy](https://docs.aws.amazon.com/polly/latest/dg/internetwork-traffic-privacy.html): Access to Amazon Polly is via the AWS console, CLI, or SDKs.

### [Identity and Access Management](https://docs.aws.amazon.com/polly/latest/dg/security-iam.html)

How to authenticate requests and manage access your Amazon Polly resources.

- [How Amazon Polly works with IAM](https://docs.aws.amazon.com/polly/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Polly, learn what IAM features are available to use with Amazon Polly.
- [Identity-based policy examples](https://docs.aws.amazon.com/polly/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Polly resources.
- [Amazon Polly API Permissions Reference](https://docs.aws.amazon.com/polly/latest/dg/api-permissions-reference.html): Provides a complete list of the required API permissions you can use to control access to your Amazon Polly resources.
- [Troubleshooting](https://docs.aws.amazon.com/polly/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Polly and IAM.
- [Logging and Monitoring](https://docs.aws.amazon.com/polly/latest/dg/sec-logging.html): Learn how Amazon Polly supports logging and monitoring.
- [Compliance Validation](https://docs.aws.amazon.com/polly/latest/dg/AMAZON-POLLY-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/polly/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Polly features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/polly/latest/dg/infrastructure-security.html): Learn how Amazon Polly isolates service traffic.
- [Security Best Practices](https://docs.aws.amazon.com/polly/latest/dg/security-best-practices.html): Learn about security best practices in Amazon Polly.
- [Using Interface VPC Endpoints](https://docs.aws.amazon.com/polly/latest/dg/using-polly-with-vpc-endpoints.html): Learn how to use VPC Endpoints in Amazon Polly.


## [API Reference](https://docs.aws.amazon.com/polly/latest/dg/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/polly/latest/dg/API_Operations.html)

The following actions are supported:

- [DeleteLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_DeleteLexicon.html): Deletes the specified pronunciation lexicon stored in an AWS Region.
- [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html): Returns the list of voices that are available for use when requesting speech synthesis.
- [GetLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_GetLexicon.html): Returns the content of the specified pronunciation lexicon stored in an AWS Region.
- [GetSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/API_GetSpeechSynthesisTask.html): Retrieves a specific SpeechSynthesisTask object based on its TaskID.
- [ListLexicons](https://docs.aws.amazon.com/polly/latest/dg/API_ListLexicons.html): Returns a list of pronunciation lexicons stored in an AWS Region.
- [ListSpeechSynthesisTasks](https://docs.aws.amazon.com/polly/latest/dg/API_ListSpeechSynthesisTasks.html): Returns a list of SpeechSynthesisTask objects ordered by their creation date.
- [PutLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html): Stores a pronunciation lexicon in an AWS Region.
- [StartSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/API_StartSpeechSynthesisTask.html): Allows the creation of an asynchronous synthesis task, by starting a new SpeechSynthesisTask.
- [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html): Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes.

### [Data Types](https://docs.aws.amazon.com/polly/latest/dg/API_Types.html)

The following data types are supported:

- [Lexicon](https://docs.aws.amazon.com/polly/latest/dg/API_Lexicon.html): Provides lexicon name and lexicon content in string format.
- [LexiconAttributes](https://docs.aws.amazon.com/polly/latest/dg/API_LexiconAttributes.html): Contains metadata describing the lexicon such as the number of lexemes, language code, and so on.
- [LexiconDescription](https://docs.aws.amazon.com/polly/latest/dg/API_LexiconDescription.html): Describes the content of the lexicon.
- [SynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesisTask.html): SynthesisTask object that provides information about a speech synthesis task.
- [Voice](https://docs.aws.amazon.com/polly/latest/dg/API_Voice.html): Description of the voice.
- [Common Errors](https://docs.aws.amazon.com/polly/latest/dg/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/polly/latest/dg/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
