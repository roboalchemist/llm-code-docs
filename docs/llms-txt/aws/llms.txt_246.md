# Source: https://docs.aws.amazon.com/connecthealth/latest/APIReference/llms.txt

# Amazon Connect Health API Reference

> Health Agent for healthcare providers and patient engagement

- [Welcome](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/connecthealth/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/connecthealth/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_Operations.html)

- [ActivateSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ActivateSubscription.html): Activates a Subscription to enable billing for a user.
- [CreateDomain](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateDomain.html): Creates a new Domain for managing HealthAgent resources.
- [CreateSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateSubscription.html): Creates a new Subscription within a Domain for billing and user management.
- [DeactivateSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DeactivateSubscription.html): Deactivates a Subscription to stop billing for a user.
- [DeleteDomain](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DeleteDomain.html): Deletes a Domain and all associated resources.
- [GetDomain](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetDomain.html): Retrieves information about a Domain.
- [GetMedicalScribeListeningSession](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetMedicalScribeListeningSession.html): Retrieves details about an existing Medical Scribe listening session
- [GetPatientInsightsJob](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetPatientInsightsJob.html): Get details of a started patient insights job.
- [GetSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetSubscription.html): Retrieves information about a Subscription.
- [ListDomains](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListDomains.html): Lists Domains for a given account.
- [ListSubscriptions](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListSubscriptions.html): Lists all Subscriptions within a Domain.
- [ListTagsForResource](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListTagsForResource.html): Lists the tags associated with the specified resource
- [StartMedicalScribeListeningSession](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_StartMedicalScribeListeningSession.html): Starts a new Medical Scribe listening session for real-time audio transcription
- [StartPatientInsightsJob](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_StartPatientInsightsJob.html): Starts a new patient insights job.
- [TagResource](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_TagResource.html): Associates the specified tags with the specified resource
- [UntagResource](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified resource


## [Data Types](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_Types.html)

- [ArtifactDetails](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ArtifactDetails.html): Details about a generated artifact including location and status
- [ClinicalNoteGenerationResult](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ClinicalNoteGenerationResult.html): Results of clinical note generation including note, transcript, and summary
- [ClinicalNoteGenerationSettings](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ClinicalNoteGenerationSettings.html): Settings for generating clinical notes from the audio stream
- [ClinicalNoteGenerationSettingsResponse](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ClinicalNoteGenerationSettingsResponse.html): Response containing settings for clinical note generation
- [CreateWebAppConfiguration](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateWebAppConfiguration.html): Input configuration for creating a Pulse web application.
- [CustomTemplate](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CustomTemplate.html): Configuration for using a custom note template with specific instructions
- [CustomTemplateResponse](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CustomTemplateResponse.html): Response containing custom template information
- [DomainSummary](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DomainSummary.html): Summary information about a Domain.
- [EncounterContext](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_EncounterContext.html): Context information about the clinical encounter
- [EncryptionContext](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_EncryptionContext.html): Encryption context for a Domain.
- [FHIRServer](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_FHIRServer.html): FHIR server configuration for input data source
- [InputDataConfig](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_InputDataConfig.html): Configuration details for input patient data
- [InsightsContext](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_InsightsContext.html): Details for insights that user wants to generate
- [InsightsOutput](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_InsightsOutput.html): Output of patient insights job
- [ManagedTemplate](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ManagedTemplate.html): Configuration for using a managed note template
- [ManagedTemplateResponse](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ManagedTemplateResponse.html): Response containing managed template information
- [MedicalScribeAudioEvent](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeAudioEvent.html): An event containing audio data for the Medical Scribe stream
- [MedicalScribeChannelDefinition](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeChannelDefinition.html): Defines a channel in the audio stream
- [MedicalScribeConfigurationEvent](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeConfigurationEvent.html): An event containing configuration for the Medical Scribe session
- [MedicalScribeInputStream](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeInputStream.html): Input stream for Medical Scribe containing audio and configuration events
- [MedicalScribeListeningSessionDetails](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeListeningSessionDetails.html): Detailed information about a Medical Scribe listening session
- [MedicalScribeOutputStream](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeOutputStream.html): Output stream from Medical Scribe containing transcript events and errors
- [MedicalScribePostStreamActionSettings](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribePostStreamActionSettings.html): Settings for actions to perform after the audio stream ends
- [MedicalScribePostStreamActionSettingsResponse](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribePostStreamActionSettingsResponse.html): Response containing settings for post-stream actions
- [MedicalScribePostStreamActionsResult](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribePostStreamActionsResult.html): Results of post-stream actions performed after the audio stream ended
- [MedicalScribeSessionControlEvent](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeSessionControlEvent.html): An event for controlling the Medical Scribe session
- [MedicalScribeTranscriptEvent](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeTranscriptEvent.html): An event containing transcript data from the Medical Scribe stream
- [MedicalScribeTranscriptSegment](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeTranscriptSegment.html): A segment of transcript text with timing and channel information
- [NoteTemplateSettings](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_NoteTemplateSettings.html): Settings for the note template to use for clinical note generation
- [NoteTemplateSettingsResponse](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_NoteTemplateSettingsResponse.html): Response containing note template settings
- [OutputDataConfig](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_OutputDataConfig.html): Configuration details for insights output.
- [PatientInsightsEncounterContext](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_PatientInsightsEncounterContext.html): Details for an encounter
- [PatientInsightsPatientContext](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_PatientInsightsPatientContext.html): Details for a patient
- [S3Source](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_S3Source.html): S3 uri for input data source
- [SubscriptionDescription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_SubscriptionDescription.html): Complete subscription resource data.
- [TemplateSectionInstruction](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_TemplateSectionInstruction.html): Instructions for generating a specific section of a clinical note
- [UserContext](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_UserContext.html): Details for user initiating insights job
- [WebAppConfiguration](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_WebAppConfiguration.html): Configuration for the Domain web application, including Identity Center settings.
