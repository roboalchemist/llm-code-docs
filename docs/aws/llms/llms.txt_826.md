# Source: https://docs.aws.amazon.com/transcribe/latest/APIReference/llms.txt

# Amazon Transcribe API Reference

## [Amazon Transcribe Service](https://docs.aws.amazon.com/transcribe/latest/APIReference/Welcome_Amazon_Transcribe_Service.html)

Amazon Transcribe offers three main types of batch transcription: Standard, Medical, and Call Analytics.

- Standard transcriptionsare the most common option. Refer to for details.
- Medical transcriptionsare tailored to medical professionals and incorporate medical terms. A common use case for this service is transcribing doctor-patient dialogue into after-visit notes. Refer to for details.
- Call Analytics transcriptionsare designed for use with call center audio on two different channels; if you're looking for insight into customer service calls, use this option. Refer to for details.

### Actions

- [CreateCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateCallAnalyticsCategory.html): Creates a new Call Analytics category.
- [CreateLanguageModel](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateLanguageModel.html): Creates a new custom language model.
- [CreateMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateMedicalVocabulary.html): Creates a new custom medical vocabulary.
- [CreateVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateVocabulary.html): Creates a new custom vocabulary.
- [CreateVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateVocabularyFilter.html): Creates a new custom vocabulary filter.
- [DeleteCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteCallAnalyticsCategory.html): Deletes a Call Analytics category.
- [DeleteCallAnalyticsJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteCallAnalyticsJob.html): Deletes a Call Analytics job.
- [DeleteLanguageModel](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteLanguageModel.html): Deletes a custom language model.
- [DeleteMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteMedicalScribeJob.html): Deletes a Medical Scribe job.
- [DeleteMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteMedicalTranscriptionJob.html): Deletes a medical transcription job.
- [DeleteMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteMedicalVocabulary.html): Deletes a custom medical vocabulary.
- [DeleteTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteTranscriptionJob.html): Deletes a transcription job.
- [DeleteVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteVocabulary.html): Deletes a custom vocabulary.
- [DeleteVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteVocabularyFilter.html): Deletes a custom vocabulary filter.
- [DescribeLanguageModel](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DescribeLanguageModel.html): Provides information about the specified custom language model.
- [GetCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetCallAnalyticsCategory.html): Provides information about the specified Call Analytics category.
- [GetCallAnalyticsJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetCallAnalyticsJob.html): Provides information about the specified Call Analytics job.
- [GetMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetMedicalScribeJob.html): Provides information about the specified Medical Scribe job.
- [GetMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetMedicalTranscriptionJob.html): Provides information about the specified medical transcription job.
- [GetMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetMedicalVocabulary.html): Provides information about the specified custom medical vocabulary.
- [GetTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetTranscriptionJob.html): Provides information about the specified transcription job.
- [GetVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetVocabulary.html): Provides information about the specified custom vocabulary.
- [GetVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetVocabularyFilter.html): Provides information about the specified custom vocabulary filter.
- [ListCallAnalyticsCategories](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListCallAnalyticsCategories.html): Provides a list of Call Analytics categories, including all rules that make up each category.
- [ListCallAnalyticsJobs](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListCallAnalyticsJobs.html): Provides a list of Call Analytics jobs that match the specified criteria.
- [ListLanguageModels](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListLanguageModels.html): Provides a list of custom language models that match the specified criteria.
- [ListMedicalScribeJobs](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListMedicalScribeJobs.html): Provides a list of Medical Scribe jobs that match the specified criteria.
- [ListMedicalTranscriptionJobs](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListMedicalTranscriptionJobs.html): Provides a list of medical transcription jobs that match the specified criteria.
- [ListMedicalVocabularies](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListMedicalVocabularies.html): Provides a list of custom medical vocabularies that match the specified criteria.
- [ListTagsForResource](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListTagsForResource.html): Lists all tags associated with the specified transcription job, vocabulary, model, or resource.
- [ListTranscriptionJobs](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListTranscriptionJobs.html): Provides a list of transcription jobs that match the specified criteria.
- [ListVocabularies](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListVocabularies.html): Provides a list of custom vocabularies that match the specified criteria.
- [ListVocabularyFilters](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListVocabularyFilters.html): Provides a list of custom vocabulary filters that match the specified criteria.
- [StartCallAnalyticsJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartCallAnalyticsJob.html): Transcribes the audio from a customer service call and applies any additional Request Parameters you choose to include in your request.
- [StartMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartMedicalScribeJob.html): Transcribes patient-clinician conversations and generates clinical notes.
- [StartMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartMedicalTranscriptionJob.html): Transcribes the audio from a medical dictation or conversation and applies any additional Request Parameters you choose to include in your request.
- [StartTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartTranscriptionJob.html): Transcribes the audio from a media file and applies any additional Request Parameters you choose to include in your request.
- [TagResource](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TagResource.html): Adds one or more custom tags, each in the form of a key:value pair, to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified Amazon Transcribe resource.
- [UpdateCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateCallAnalyticsCategory.html): Updates the specified Call Analytics category with new rules.
- [UpdateMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateMedicalVocabulary.html): Updates an existing custom medical vocabulary with new values.
- [UpdateVocabulary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateVocabulary.html): Updates an existing custom vocabulary with new values.
- [UpdateVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateVocabularyFilter.html): Updates an existing custom vocabulary filter with a new list of words.

### Data Types

- [AbsoluteTimeRange](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_AbsoluteTimeRange.html): A time range, in milliseconds, between two points in your media file.
- [CallAnalyticsJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CallAnalyticsJob.html): Provides detailed information about a Call Analytics job.
- [CallAnalyticsJobDetails](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CallAnalyticsJobDetails.html): Contains details about a call analytics job, including information about skipped analytics features.
- [CallAnalyticsJobSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CallAnalyticsJobSettings.html): Provides additional optional settings for your request, including content redaction, automatic language identification; allows you to apply custom language models, custom vocabulary filters, and custom vocabularies.
- [CallAnalyticsJobSummary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CallAnalyticsJobSummary.html): Provides detailed information about a specific Call Analytics job.
- [CallAnalyticsSkippedFeature](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CallAnalyticsSkippedFeature.html): Represents a skipped analytics feature during the analysis of a call analytics job.
- [CategoryProperties](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CategoryProperties.html): Provides you with the properties of the Call Analytics category you specified in your request.
- [ChannelDefinition](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ChannelDefinition.html): Makes it possible to specify which speaker is on which channel.
- [ClinicalNoteGenerationSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ClinicalNoteGenerationSettings.html): The output configuration for clinical note generation.
- [ContentRedaction](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ContentRedaction.html): Makes it possible to redact or flag specified personally identifiable information (PII) in your transcript.
- [InputDataConfig](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_InputDataConfig.html): Contains the Amazon S3 location of the training data you want to use to create a new custom language model, and permissions to access this location.
- [InterruptionFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_InterruptionFilter.html): Flag the presence or absence of interruptions in your Call Analytics transcription output.
- [JobExecutionSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_JobExecutionSettings.html): Makes it possible to control how your transcription job is processed.
- [LanguageCodeItem](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_LanguageCodeItem.html): Provides information on the speech contained in a discreet utterance when multi-language identification is enabled in your request.
- [LanguageIdSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_LanguageIdSettings.html): If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include LanguageIdSettings with the relevant sub-parameters (VocabularyName, LanguageModelName, and VocabularyFilterName).
- [LanguageModel](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_LanguageModel.html): Provides information about a custom language model, including:
- [Media](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Media.html): Describes the Amazon S3 location of the media file you want to use in your request.
- [MedicalScribeChannelDefinition](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribeChannelDefinition.html): Indicates which speaker is on which channel.
- [MedicalScribeContext](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribeContext.html): The MedicalScribeContext object that contains contextual information used to generate customized clinical notes.
- [MedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribeJob.html): Provides detailed information about a Medical Scribe job.
- [MedicalScribeJobSummary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribeJobSummary.html): Provides detailed information about a specific Medical Scribe job.
- [MedicalScribeOutput](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribeOutput.html): The location of the output of your Medical Scribe job.
- [MedicalScribePatientContext](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribePatientContext.html): Contains patient-specific information used to customize the clinical note generation.
- [MedicalScribeSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribeSettings.html): Makes it possible to control how your Medical Scribe job is processed using a MedicalScribeSettings object.
- [MedicalTranscript](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalTranscript.html): Provides you with the Amazon S3 URI you can use to access your transcript.
- [MedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalTranscriptionJob.html): Provides detailed information about a medical transcription job.
- [MedicalTranscriptionJobSummary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalTranscriptionJobSummary.html): Provides detailed information about a specific medical transcription job.
- [MedicalTranscriptionSetting](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalTranscriptionSetting.html): Allows additional optional settings in your request, including channel identification, alternative transcriptions, and speaker partitioning.
- [ModelSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ModelSettings.html): Provides the name of the custom language model that was included in the specified transcription job.
- [NonTalkTimeFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_NonTalkTimeFilter.html): Flag the presence or absence of periods of silence in your Call Analytics transcription output.
- [RelativeTimeRange](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_RelativeTimeRange.html): A time range, in percentage, between two points in your media file.
- [Rule](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Rule.html): A rule is a set of criteria that you can specify to flag an attribute in your Call Analytics output.
- [SentimentFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_SentimentFilter.html): Flag the presence or absence of specific sentiments detected in your Call Analytics transcription output.
- [Settings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Settings.html): Allows additional optional settings in your request, including channel identification, alternative transcriptions, and speaker partitioning.
- [Subtitles](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Subtitles.html): Generate subtitles for your media file with your transcription request.
- [SubtitlesOutput](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_SubtitlesOutput.html): Provides information about your subtitle file, including format, start index, and Amazon S3 location.
- [Summarization](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Summarization.html): Contains GenerateAbstractiveSummary, which is a required parameter if you want to enable Generative call summarization in your Call Analytics request.
- [Tag](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Tag.html): Adds metadata, in the form of a key:value pair, to the specified resource.
- [ToxicityDetectionSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ToxicityDetectionSettings.html): Contains ToxicityCategories, which is a required parameter if you want to enable toxicity detection (ToxicityDetection) in your transcription request.
- [Transcript](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Transcript.html): Provides you with the Amazon S3 URI you can use to access your transcript.
- [TranscriptFilter](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TranscriptFilter.html): Flag the presence or absence of specific words or phrases detected in your Call Analytics transcription output.
- [TranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TranscriptionJob.html): Provides detailed information about a transcription job.
- [TranscriptionJobSummary](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TranscriptionJobSummary.html): Provides detailed information about a specific transcription job.
- [VocabularyFilterInfo](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_VocabularyFilterInfo.html): Provides information about a custom vocabulary filter, including the language of the filter, when it was last modified, and its name.
- [VocabularyInfo](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_VocabularyInfo.html): Provides information about a custom vocabulary, including the language of the custom vocabulary, when it was last modified, its name, and the processing state.

## [Amazon Transcribe Streaming Service](https://docs.aws.amazon.com/transcribe/latest/APIReference/Welcome_Amazon_Transcribe_Streaming_Service.html)

Amazon Transcribe streaming offers four main types of real-time transcription: Standard, Medical, Call Analytics, and Health Scribe.

- Standard transcriptionsare the most common option. Refer to for details.
- Medical transcriptionsare tailored to medical professionals and incorporate medical terms. A common use case for this service is transcribing doctor-patient dialogue in real time, so doctors can focus on their patient instead of taking notes. Refer to for details.
- Call Analytics transcriptionsare designed for use with call center audio on two different channels; if you're looking for insight into customer service calls, use this option. Refer to for details.
- HealthScribe transcriptionsare designed to automatically create clinical notes from patient-clinician conversations using generative AI. Refer to [here] for details.

### Actions

- [GetMedicalScribeStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_GetMedicalScribeStream.html): Provides details about the specified AWS HealthScribe streaming session.
- [StartCallAnalyticsStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartCallAnalyticsStreamTranscription.html): Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe and the transcription results are streamed to your application.
- [StartMedicalScribeStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartMedicalScribeStream.html): Starts a bidirectional HTTP/2 stream, where audio is streamed to AWS HealthScribe and the transcription results are streamed to your application.
- [StartMedicalStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartMedicalStreamTranscription.html): Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe Medical and the transcription results are streamed to your application.
- [StartStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html): Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe and the transcription results are streamed to your application.

### Data Types

- [Alternative](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_Alternative.html): A list of possible alternative transcriptions for the input audio.
- [AudioEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_AudioEvent.html): A wrapper for your audio chunks.
- [AudioStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_AudioStream.html): An encoded stream of audio blobs.
- [CallAnalyticsEntity](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CallAnalyticsEntity.html): Contains entities identified as personally identifiable information (PII) in your transcription output, along with various associated attributes.
- [CallAnalyticsItem](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CallAnalyticsItem.html): A word, phrase, or punctuation mark in your Call Analytics transcription output, along with various associated attributes, such as confidence score, type, and start and end times.
- [CallAnalyticsLanguageWithScore](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CallAnalyticsLanguageWithScore.html): The language code that represents the language identified in your audio, including the associated confidence score.
- [CallAnalyticsTranscriptResultStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CallAnalyticsTranscriptResultStream.html): Contains detailed information about your real-time Call Analytics session.
- [CategoryEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CategoryEvent.html): Provides information on any TranscriptFilterType categories that matched your transcription output.
- [ChannelDefinition](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_ChannelDefinition.html): Makes it possible to specify which speaker is on which audio channel.
- [CharacterOffsets](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CharacterOffsets.html): Provides the location, using character count, in your transcript where a match is identified.
- [ClinicalNoteGenerationResult](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_ClinicalNoteGenerationResult.html): The details for clinical note generation, including status, and output locations for clinical note and aggregated transcript if the analytics completed, or failure reason if the analytics failed.
- [ClinicalNoteGenerationSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_ClinicalNoteGenerationSettings.html): The output configuration for aggregated transcript and clinical note generation.
- [ConfigurationEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_ConfigurationEvent.html): Allows you to set audio channel definitions and post-call analytics settings.
- [Entity](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_Entity.html): Contains entities identified as personally identifiable information (PII) in your transcription output, along with various associated attributes.
- [IssueDetected](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_IssueDetected.html): Lists the issues that were identified in your audio segment.
- [Item](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_Item.html): A word, phrase, or punctuation mark in your transcription output, along with various associated attributes, such as confidence score, type, and start and end times.
- [LanguageWithScore](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_LanguageWithScore.html): The language code that represents the language identified in your audio, including the associated confidence score.
- [MedicalAlternative](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalAlternative.html): A list of possible alternative transcriptions for the input audio.
- [MedicalEntity](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalEntity.html): Contains entities identified as personal health information (PHI) in your transcription output, along with various associated attributes.
- [MedicalItem](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalItem.html): A word, phrase, or punctuation mark in your transcription output, along with various associated attributes, such as confidence score, type, and start and end times.
- [MedicalResult](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalResult.html): The Result associated with a .
- [MedicalScribeAudioEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeAudioEvent.html): A wrapper for your audio chunks
- [MedicalScribeChannelDefinition](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeChannelDefinition.html): Makes it possible to specify which speaker is on which channel.
- [MedicalScribeConfigurationEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeConfigurationEvent.html): Specify details to configure the streaming session, including channel definitions, encryption settings, post-stream analytics settings, resource access role ARN and vocabulary settings.
- [MedicalScribeContext](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeContext.html): The MedicalScribeContext object that contains contextual information which is used during clinical note generation to add relevant context to the note.
- [MedicalScribeEncryptionSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeEncryptionSettings.html): Contains encryption related settings to be used for data encryption with AWS Key Management Service, including KmsEncryptionContext and KmsKeyId.
- [MedicalScribeInputStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeInputStream.html): An encoded stream of events.
- [MedicalScribePatientContext](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribePatientContext.html): Contains patient-specific information.
- [MedicalScribePostStreamAnalyticsResult](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribePostStreamAnalyticsResult.html): Contains details for the result of post-stream analytics.
- [MedicalScribePostStreamAnalyticsSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribePostStreamAnalyticsSettings.html): The settings for post-stream analytics.
- [MedicalScribeResultStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeResultStream.html): Result stream where you will receive the output events.
- [MedicalScribeSessionControlEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeSessionControlEvent.html): Specify the lifecycle of your streaming session.
- [MedicalScribeStreamDetails](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeStreamDetails.html): Contains details about a AWS HealthScribe streaming session.
- [MedicalScribeTranscriptEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeTranscriptEvent.html): The event associated with MedicalScribeResultStream.
- [MedicalScribeTranscriptItem](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeTranscriptItem.html): A word, phrase, or punctuation mark in your transcription output, along with various associated attributes, such as confidence score, type, and start and end times.
- [MedicalScribeTranscriptSegment](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeTranscriptSegment.html): Contains a set of transcription results, along with additional information of the segment.
- [MedicalTranscript](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalTranscript.html): The MedicalTranscript associated with a .
- [MedicalTranscriptEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalTranscriptEvent.html): The MedicalTranscriptEvent associated with a MedicalTranscriptResultStream.
- [MedicalTranscriptResultStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalTranscriptResultStream.html): Contains detailed information about your streaming session.
- [PointsOfInterest](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_PointsOfInterest.html): Contains the timestamps of matched categories.
- [PostCallAnalyticsSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_PostCallAnalyticsSettings.html): Allows you to specify additional settings for your Call Analytics post-call request, including output locations for your redacted transcript, which IAM role to use, and which encryption key to use.
- [Result](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_Result.html): The Result associated with a .
- [TimestampRange](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_TimestampRange.html): Contains the timestamp range (start time through end time) of a matched category.
- [Transcript](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_Transcript.html): The Transcript associated with a .
- [TranscriptEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_TranscriptEvent.html): The TranscriptEvent associated with a TranscriptResultStream.
- [TranscriptResultStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_TranscriptResultStream.html): Contains detailed information about your streaming session.
- [UtteranceEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_UtteranceEvent.html): Contains set of transcription results from one or more audio segments, along with additional information about the parameters included in your request.

## Common

- [Common Parameters](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html)