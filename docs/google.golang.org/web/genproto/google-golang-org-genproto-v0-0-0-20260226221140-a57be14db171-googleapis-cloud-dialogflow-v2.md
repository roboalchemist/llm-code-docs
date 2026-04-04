# Source: https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/dialogflow/v2

Title: dialogflow package - google.golang.org/genproto/googleapis/cloud/dialogflow/v2 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/dialogflow/v2

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/genproto
 
googleapis
 
cloud
 
dialogflow
 
v2
dialogflow
package
Version: v0.0.0-...-a57be14 Latest 
Published: Feb 26, 2026 
License: Apache-2.0 
Imports: 2 
Imported by: 75
Details
 Valid go.mod file 
 Redistributable license 
 Tagged version 
 Stable version 
Learn more about best practices
Repository
github.com/googleapis/go-genproto
Links
 Open Source Insights
Jump to ...
Documentation
Source Files
 Documentation ¶
Overview ¶

Package dialogflow aliases all exported identifiers in package "cloud.google.com/go/dialogflow/apiv2/dialogflowpb".

Deprecated: Please use types in: cloud.google.com/go/dialogflow/apiv2/dialogflowpb. Please read https://github.com/googleapis/google-cloud-go/blob/main/migration.md for more details.

Index ¶
Constants
Variables
func RegisterAgentsServer(s *grpc.Server, srv AgentsServer)DEPRECATED
func RegisterAnswerRecordsServer(s *grpc.Server, srv AnswerRecordsServer)DEPRECATED
func RegisterContextsServer(s *grpc.Server, srv ContextsServer)DEPRECATED
func RegisterConversationDatasetsServer(s *grpc.Server, srv ConversationDatasetsServer)DEPRECATED
func RegisterConversationModelsServer(s *grpc.Server, srv ConversationModelsServer)DEPRECATED
func RegisterConversationProfilesServer(s *grpc.Server, srv ConversationProfilesServer)DEPRECATED
func RegisterConversationsServer(s *grpc.Server, srv ConversationsServer)DEPRECATED
func RegisterDocumentsServer(s *grpc.Server, srv DocumentsServer)DEPRECATED
func RegisterEntityTypesServer(s *grpc.Server, srv EntityTypesServer)DEPRECATED
func RegisterEnvironmentsServer(s *grpc.Server, srv EnvironmentsServer)DEPRECATED
func RegisterFulfillmentsServer(s *grpc.Server, srv FulfillmentsServer)DEPRECATED
func RegisterIntentsServer(s *grpc.Server, srv IntentsServer)DEPRECATED
func RegisterKnowledgeBasesServer(s *grpc.Server, srv KnowledgeBasesServer)DEPRECATED
func RegisterParticipantsServer(s *grpc.Server, srv ParticipantsServer)DEPRECATED
func RegisterSessionEntityTypesServer(s *grpc.Server, srv SessionEntityTypesServer)DEPRECATED
func RegisterSessionsServer(s *grpc.Server, srv SessionsServer)DEPRECATED
func RegisterVersionsServer(s *grpc.Server, srv VersionsServer)DEPRECATED
type AgentDEPRECATED
type AgentAssistantFeedbackDEPRECATED
type AgentAssistantFeedback_AnswerRelevanceDEPRECATED
type AgentAssistantFeedback_DocumentCorrectnessDEPRECATED
type AgentAssistantFeedback_DocumentEfficiencyDEPRECATED
type AgentAssistantRecordDEPRECATED
type AgentAssistantRecord_ArticleSuggestionAnswer
type AgentAssistantRecord_FaqAnswer
type Agent_ApiVersionDEPRECATED
type Agent_MatchModeDEPRECATED
type Agent_TierDEPRECATED
type AgentsClientDEPRECATED
func NewAgentsClient(cc grpc.ClientConnInterface) AgentsClientDEPRECATED
type AgentsServerDEPRECATED
type AnalyzeContentRequestDEPRECATED
type AnalyzeContentRequest_EventInput
type AnalyzeContentRequest_TextInput
type AnalyzeContentResponseDEPRECATED
type AnnotatedMessagePartDEPRECATED
type AnswerFeedbackDEPRECATED
type AnswerFeedback_AgentAssistantDetailFeedback
type AnswerFeedback_CorrectnessLevelDEPRECATED
type AnswerRecordDEPRECATED
type AnswerRecord_AgentAssistantRecord
type AnswerRecordsClientDEPRECATED
func NewAnswerRecordsClient(cc grpc.ClientConnInterface) AnswerRecordsClientDEPRECATED
type AnswerRecordsServerDEPRECATED
type ArticleAnswerDEPRECATED
type ArticleSuggestionModelMetadataDEPRECATED
type AssistQueryParametersDEPRECATED
type AudioEncodingDEPRECATED
type AutomatedAgentConfigDEPRECATED
type AutomatedAgentReplyDEPRECATED
type AutomatedAgentReply_AutomatedAgentReplyTypeDEPRECATED
type BatchCreateEntitiesRequestDEPRECATED
type BatchDeleteEntitiesRequestDEPRECATED
type BatchDeleteEntityTypesRequestDEPRECATED
type BatchDeleteIntentsRequestDEPRECATED
type BatchUpdateEntitiesRequestDEPRECATED
type BatchUpdateEntityTypesRequestDEPRECATED
type BatchUpdateEntityTypesRequest_EntityTypeBatchInline
type BatchUpdateEntityTypesRequest_EntityTypeBatchUri
type BatchUpdateEntityTypesResponseDEPRECATED
type BatchUpdateIntentsRequest
type BatchUpdateIntentsRequest_IntentBatchInline
type BatchUpdateIntentsRequest_IntentBatchUri
type BatchUpdateIntentsResponseDEPRECATED
type ClearSuggestionFeatureConfigOperationMetadataDEPRECATED
type ClearSuggestionFeatureConfigRequestDEPRECATED
type CompleteConversationRequestDEPRECATED
type ContextDEPRECATED
type ContextsClientDEPRECATED
func NewContextsClient(cc grpc.ClientConnInterface) ContextsClientDEPRECATED
type ContextsServerDEPRECATED
type ConversationDEPRECATED
type ConversationDatasetDEPRECATED
type ConversationDatasetsClientDEPRECATED
func NewConversationDatasetsClient(cc grpc.ClientConnInterface) ConversationDatasetsClientDEPRECATED
type ConversationDatasetsServerDEPRECATED
type ConversationEventDEPRECATED
type ConversationEvent_NewMessagePayload
type ConversationEvent_TypeDEPRECATED
type ConversationInfoDEPRECATED
type ConversationModelDEPRECATED
type ConversationModelEvaluationDEPRECATED
type ConversationModelEvaluation_SmartReplyMetrics
type ConversationModel_ArticleSuggestionModelMetadata
type ConversationModel_ModelTypeDEPRECATED
type ConversationModel_SmartReplyModelMetadata
type ConversationModel_StateDEPRECATED
type ConversationModelsClientDEPRECATED
func NewConversationModelsClient(cc grpc.ClientConnInterface) ConversationModelsClientDEPRECATED
type ConversationModelsServerDEPRECATED
type ConversationPhoneNumberDEPRECATED
type ConversationProfileDEPRECATED
type ConversationProfilesClientDEPRECATED
func NewConversationProfilesClient(cc grpc.ClientConnInterface) ConversationProfilesClientDEPRECATED
type ConversationProfilesServerDEPRECATED
type Conversation_ConversationStageDEPRECATED
type Conversation_LifecycleStateDEPRECATED
type ConversationsClientDEPRECATED
func NewConversationsClient(cc grpc.ClientConnInterface) ConversationsClientDEPRECATED
type ConversationsServerDEPRECATED
type CreateContextRequestDEPRECATED
type CreateConversationDatasetOperationMetadataDEPRECATED
type CreateConversationDatasetRequestDEPRECATED
type CreateConversationModelEvaluationOperationMetadataDEPRECATED
type CreateConversationModelEvaluationOperationMetadata_StateDEPRECATED
type CreateConversationModelEvaluationRequestDEPRECATED
type CreateConversationModelOperationMetadataDEPRECATED
type CreateConversationModelOperationMetadata_StateDEPRECATED
type CreateConversationModelRequestDEPRECATED
type CreateConversationProfileRequestDEPRECATED
type CreateConversationRequestDEPRECATED
type CreateDocumentRequestDEPRECATED
type CreateEntityTypeRequestDEPRECATED
type CreateEnvironmentRequestDEPRECATED
type CreateIntentRequestDEPRECATED
type CreateKnowledgeBaseRequestDEPRECATED
type CreateParticipantRequestDEPRECATED
type CreateSessionEntityTypeRequestDEPRECATED
type CreateVersionRequestDEPRECATED
type DeleteAgentRequestDEPRECATED
type DeleteAllContextsRequestDEPRECATED
type DeleteContextRequestDEPRECATED
type DeleteConversationDatasetOperationMetadataDEPRECATED
type DeleteConversationDatasetRequestDEPRECATED
type DeleteConversationModelOperationMetadataDEPRECATED
type DeleteConversationModelRequestDEPRECATED
type DeleteConversationProfileRequestDEPRECATED
type DeleteDocumentRequestDEPRECATED
type DeleteEntityTypeRequestDEPRECATED
type DeleteEnvironmentRequestDEPRECATED
type DeleteIntentRequestDEPRECATED
type DeleteKnowledgeBaseRequestDEPRECATED
type DeleteSessionEntityTypeRequestDEPRECATED
type DeleteVersionRequestDEPRECATED
type DeployConversationModelOperationMetadataDEPRECATED
type DeployConversationModelRequestDEPRECATED
type DetectIntentRequestDEPRECATED
type DetectIntentResponseDEPRECATED
type DocumentDEPRECATED
type Document_ContentUri
type Document_KnowledgeTypeDEPRECATED
type Document_RawContent
type Document_ReloadStatusDEPRECATED
type Document_StateDEPRECATED
type DocumentsClientDEPRECATED
func NewDocumentsClient(cc grpc.ClientConnInterface) DocumentsClientDEPRECATED
type DocumentsServerDEPRECATED
type DtmfParametersDEPRECATED
type EntityTypeDEPRECATED
type EntityTypeBatchDEPRECATED
type EntityType_AutoExpansionModeDEPRECATED
type EntityType_EntityDEPRECATED
type EntityType_KindDEPRECATED
type EntityTypesClientDEPRECATED
func NewEntityTypesClient(cc grpc.ClientConnInterface) EntityTypesClientDEPRECATED
type EntityTypesServerDEPRECATED
type EnvironmentDEPRECATED
type EnvironmentHistoryDEPRECATED
type EnvironmentHistory_EntryDEPRECATED
type Environment_StateDEPRECATED
type EnvironmentsClientDEPRECATED
func NewEnvironmentsClient(cc grpc.ClientConnInterface) EnvironmentsClientDEPRECATED
type EnvironmentsServerDEPRECATED
type EvaluationConfigDEPRECATED
type EvaluationConfig_SmartComposeConfigDEPRECATED
type EvaluationConfig_SmartComposeConfig_
type EvaluationConfig_SmartReplyConfigDEPRECATED
type EvaluationConfig_SmartReplyConfig_
type EventInputDEPRECATED
type ExportAgentRequestDEPRECATED
type ExportAgentResponseDEPRECATED
type ExportAgentResponse_AgentContent
type ExportAgentResponse_AgentUri
type ExportDocumentRequestDEPRECATED
type ExportDocumentRequest_GcsDestination
type ExportOperationMetadataDEPRECATED
type FaqAnswerDEPRECATED
type FulfillmentDEPRECATED
type Fulfillment_FeatureDEPRECATED
type Fulfillment_Feature_TypeDEPRECATED
type Fulfillment_GenericWebServiceDEPRECATED
type Fulfillment_GenericWebService_
type FulfillmentsClientDEPRECATED
func NewFulfillmentsClient(cc grpc.ClientConnInterface) FulfillmentsClientDEPRECATED
type FulfillmentsServerDEPRECATED
type GcsDestinationDEPRECATED
type GcsSourcesDEPRECATED
type GetAgentRequestDEPRECATED
type GetContextRequestDEPRECATED
type GetConversationDatasetRequestDEPRECATED
type GetConversationModelEvaluationRequestDEPRECATED
type GetConversationModelRequestDEPRECATED
type GetConversationProfileRequestDEPRECATED
type GetConversationRequestDEPRECATED
type GetDocumentRequestDEPRECATED
type GetEntityTypeRequestDEPRECATED
type GetEnvironmentHistoryRequestDEPRECATED
type GetEnvironmentRequestDEPRECATED
type GetFulfillmentRequestDEPRECATED
type GetIntentRequestDEPRECATED
type GetKnowledgeBaseRequestDEPRECATED
type GetParticipantRequestDEPRECATED
type GetSessionEntityTypeRequestDEPRECATED
type GetValidationResultRequestDEPRECATED
type GetVersionRequestDEPRECATED
type HumanAgentAssistantConfigDEPRECATED
type HumanAgentAssistantConfig_ConversationModelConfigDEPRECATED
type HumanAgentAssistantConfig_ConversationProcessConfigDEPRECATED
type HumanAgentAssistantConfig_MessageAnalysisConfigDEPRECATED
type HumanAgentAssistantConfig_SuggestionConfigDEPRECATED
type HumanAgentAssistantConfig_SuggestionFeatureConfigDEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfigDEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_ContextFilterSettingsDEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_DialogflowQuerySourceDEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_DialogflowQuerySource_
type HumanAgentAssistantConfig_SuggestionQueryConfig_DocumentQuerySourceDEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_DocumentQuerySource_
type HumanAgentAssistantConfig_SuggestionQueryConfig_KnowledgeBaseQuerySourceDEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_KnowledgeBaseQuerySource_
type HumanAgentAssistantConfig_SuggestionTriggerSettingsDEPRECATED
type HumanAgentAssistantEventDEPRECATED
type HumanAgentHandoffConfigDEPRECATED
type HumanAgentHandoffConfig_LivePersonConfigDEPRECATED
type HumanAgentHandoffConfig_LivePersonConfig_
type HumanAgentHandoffConfig_SalesforceLiveAgentConfigDEPRECATED
type HumanAgentHandoffConfig_SalesforceLiveAgentConfig_
type ImportAgentRequestDEPRECATED
type ImportAgentRequest_AgentContent
type ImportAgentRequest_AgentUri
type ImportConversationDataOperationMetadataDEPRECATED
type ImportConversationDataOperationResponseDEPRECATED
type ImportConversationDataRequestDEPRECATED
type ImportDocumentTemplateDEPRECATED
type ImportDocumentsRequestDEPRECATED
type ImportDocumentsRequest_GcsSource
type ImportDocumentsResponseDEPRECATED
type InputAudioConfigDEPRECATED
type InputConfigDEPRECATED
type InputConfig_GcsSource
type InputDatasetDEPRECATED
type IntentDEPRECATED
type IntentBatchDEPRECATED
type IntentViewDEPRECATED
type Intent_FollowupIntentInfoDEPRECATED
type Intent_MessageDEPRECATED
type Intent_Message_BasicCardDEPRECATED
type Intent_Message_BasicCard_
type Intent_Message_BasicCard_ButtonDEPRECATED
type Intent_Message_BasicCard_Button_OpenUriActionDEPRECATED
type Intent_Message_BrowseCarouselCardDEPRECATED
type Intent_Message_BrowseCarouselCard_
type Intent_Message_BrowseCarouselCard_BrowseCarouselCardItemDEPRECATED
type Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlActionDEPRECATED
type Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_UrlTypeHintDEPRECATED
type Intent_Message_BrowseCarouselCard_ImageDisplayOptionsDEPRECATED
type Intent_Message_CardDEPRECATED
type Intent_Message_Card_
type Intent_Message_Card_ButtonDEPRECATED
type Intent_Message_CarouselSelectDEPRECATED
type Intent_Message_CarouselSelect_
type Intent_Message_CarouselSelect_ItemDEPRECATED
type Intent_Message_ColumnPropertiesDEPRECATED
type Intent_Message_ColumnProperties_HorizontalAlignmentDEPRECATED
type Intent_Message_ImageDEPRECATED
type Intent_Message_Image_
type Intent_Message_LinkOutSuggestionDEPRECATED
type Intent_Message_LinkOutSuggestion_
type Intent_Message_ListSelectDEPRECATED
type Intent_Message_ListSelect_
type Intent_Message_ListSelect_ItemDEPRECATED
type Intent_Message_MediaContentDEPRECATED
type Intent_Message_MediaContent_
type Intent_Message_MediaContent_ResponseMediaObjectDEPRECATED
type Intent_Message_MediaContent_ResponseMediaObject_Icon
type Intent_Message_MediaContent_ResponseMediaObject_LargeImage
type Intent_Message_MediaContent_ResponseMediaTypeDEPRECATED
type Intent_Message_Payload
type Intent_Message_PlatformDEPRECATED
type Intent_Message_QuickRepliesDEPRECATED
type Intent_Message_QuickReplies_
type Intent_Message_SelectItemInfoDEPRECATED
type Intent_Message_SimpleResponseDEPRECATED
type Intent_Message_SimpleResponsesDEPRECATED
type Intent_Message_SimpleResponses_
type Intent_Message_SuggestionDEPRECATED
type Intent_Message_SuggestionsDEPRECATED
type Intent_Message_Suggestions_
type Intent_Message_TableCardDEPRECATED
type Intent_Message_TableCardCellDEPRECATED
type Intent_Message_TableCardRowDEPRECATED
type Intent_Message_TableCard_
type Intent_Message_TextDEPRECATED
type Intent_Message_Text_
type Intent_ParameterDEPRECATED
type Intent_TrainingPhraseDEPRECATED
type Intent_TrainingPhrase_PartDEPRECATED
type Intent_TrainingPhrase_TypeDEPRECATED
type Intent_WebhookStateDEPRECATED
type IntentsClientDEPRECATED
func NewIntentsClient(cc grpc.ClientConnInterface) IntentsClientDEPRECATED
type IntentsServerDEPRECATED
type KnowledgeBaseDEPRECATED
type KnowledgeBasesClientDEPRECATED
func NewKnowledgeBasesClient(cc grpc.ClientConnInterface) KnowledgeBasesClientDEPRECATED
type KnowledgeBasesServerDEPRECATED
type KnowledgeOperationMetadataDEPRECATED
type KnowledgeOperationMetadata_ExportOperationMetadata
type KnowledgeOperationMetadata_StateDEPRECATED
type ListAnswerRecordsRequestDEPRECATED
type ListAnswerRecordsResponseDEPRECATED
type ListContextsRequestDEPRECATED
type ListContextsResponseDEPRECATED
type ListConversationDatasetsRequestDEPRECATED
type ListConversationDatasetsResponseDEPRECATED
type ListConversationModelEvaluationsRequestDEPRECATED
type ListConversationModelEvaluationsResponseDEPRECATED
type ListConversationModelsRequestDEPRECATED
type ListConversationModelsResponseDEPRECATED
type ListConversationProfilesRequestDEPRECATED
type ListConversationProfilesResponseDEPRECATED
type ListConversationsRequestDEPRECATED
type ListConversationsResponseDEPRECATED
type ListDocumentsRequestDEPRECATED
type ListDocumentsResponseDEPRECATED
type ListEntityTypesRequestDEPRECATED
type ListEntityTypesResponseDEPRECATED
type ListEnvironmentsRequestDEPRECATED
type ListEnvironmentsResponseDEPRECATED
type ListIntentsRequestDEPRECATED
type ListIntentsResponseDEPRECATED
type ListKnowledgeBasesRequestDEPRECATED
type ListKnowledgeBasesResponseDEPRECATED
type ListMessagesRequestDEPRECATED
type ListMessagesResponseDEPRECATED
type ListParticipantsRequestDEPRECATED
type ListParticipantsResponseDEPRECATED
type ListSessionEntityTypesRequestDEPRECATED
type ListSessionEntityTypesResponseDEPRECATED
type ListVersionsRequestDEPRECATED
type ListVersionsResponseDEPRECATED
type LoggingConfigDEPRECATED
type MessageDEPRECATED
type MessageAnnotationDEPRECATED
type NotificationConfigDEPRECATED
type NotificationConfig_MessageFormatDEPRECATED
type OriginalDetectIntentRequestDEPRECATED
type OutputAudioDEPRECATED
type OutputAudioConfigDEPRECATED
type OutputAudioEncodingDEPRECATED
type ParticipantDEPRECATED
type Participant_RoleDEPRECATED
type ParticipantsClientDEPRECATED
func NewParticipantsClient(cc grpc.ClientConnInterface) ParticipantsClientDEPRECATED
type ParticipantsServerDEPRECATED
type QueryInputDEPRECATED
type QueryInput_AudioConfig
type QueryInput_Event
type QueryInput_Text
type QueryParametersDEPRECATED
type QueryResultDEPRECATED
type ReloadDocumentRequestDEPRECATED
type ReloadDocumentRequest_ContentUri
type RestoreAgentRequestDEPRECATED
type RestoreAgentRequest_AgentContent
type RestoreAgentRequest_AgentUri
type SearchAgentsRequestDEPRECATED
type SearchAgentsResponseDEPRECATED
type SentimentDEPRECATED
type SentimentAnalysisRequestConfigDEPRECATED
type SentimentAnalysisResultDEPRECATED
type SessionEntityTypeDEPRECATED
type SessionEntityType_EntityOverrideModeDEPRECATED
type SessionEntityTypesClientDEPRECATED
func NewSessionEntityTypesClient(cc grpc.ClientConnInterface) SessionEntityTypesClientDEPRECATED
type SessionEntityTypesServerDEPRECATED
type SessionsClientDEPRECATED
func NewSessionsClient(cc grpc.ClientConnInterface) SessionsClientDEPRECATED
type SessionsServerDEPRECATED
type Sessions_StreamingDetectIntentClient
type Sessions_StreamingDetectIntentServer
type SetAgentRequestDEPRECATED
type SetSuggestionFeatureConfigOperationMetadataDEPRECATED
type SetSuggestionFeatureConfigRequestDEPRECATED
type SmartReplyAnswerDEPRECATED
type SmartReplyMetricsDEPRECATED
type SmartReplyMetrics_TopNMetricsDEPRECATED
type SmartReplyModelMetadataDEPRECATED
type SpeechContextDEPRECATED
type SpeechModelVariantDEPRECATED
type SpeechToTextConfigDEPRECATED
type SpeechWordInfoDEPRECATED
type SsmlVoiceGenderDEPRECATED
type StreamingDetectIntentRequestDEPRECATED
type StreamingDetectIntentResponseDEPRECATED
type StreamingRecognitionResultDEPRECATED
type StreamingRecognitionResult_MessageTypeDEPRECATED
type SuggestArticlesRequestDEPRECATED
type SuggestArticlesResponseDEPRECATED
type SuggestFaqAnswersRequestDEPRECATED
type SuggestFaqAnswersResponseDEPRECATED
type SuggestSmartRepliesRequestDEPRECATED
type SuggestSmartRepliesResponseDEPRECATED
type SuggestionFeatureDEPRECATED
type SuggestionFeature_TypeDEPRECATED
type SuggestionResultDEPRECATED
type SuggestionResult_Error
type SuggestionResult_SuggestArticlesResponse
type SuggestionResult_SuggestFaqAnswersResponse
type SuggestionResult_SuggestSmartRepliesResponse
type SynthesizeSpeechConfigDEPRECATED
type TextInputDEPRECATED
type TextToSpeechSettingsDEPRECATED
type TrainAgentRequestDEPRECATED
type UndeployConversationModelOperationMetadataDEPRECATED
type UndeployConversationModelRequestDEPRECATED
type UnimplementedAgentsServerDEPRECATED
type UnimplementedAnswerRecordsServerDEPRECATED
type UnimplementedContextsServerDEPRECATED
type UnimplementedConversationDatasetsServerDEPRECATED
type UnimplementedConversationModelsServerDEPRECATED
type UnimplementedConversationProfilesServerDEPRECATED
type UnimplementedConversationsServerDEPRECATED
type UnimplementedDocumentsServerDEPRECATED
type UnimplementedEntityTypesServerDEPRECATED
type UnimplementedEnvironmentsServerDEPRECATED
type UnimplementedFulfillmentsServerDEPRECATED
type UnimplementedIntentsServerDEPRECATED
type UnimplementedKnowledgeBasesServerDEPRECATED
type UnimplementedParticipantsServerDEPRECATED
type UnimplementedSessionEntityTypesServerDEPRECATED
type UnimplementedSessionsServerDEPRECATED
type UnimplementedVersionsServerDEPRECATED
type UpdateAnswerRecordRequestDEPRECATED
type UpdateContextRequestDEPRECATED
type UpdateConversationProfileRequestDEPRECATED
type UpdateDocumentRequestDEPRECATED
type UpdateEntityTypeRequestDEPRECATED
type UpdateEnvironmentRequestDEPRECATED
type UpdateFulfillmentRequestDEPRECATED
type UpdateIntentRequestDEPRECATED
type UpdateKnowledgeBaseRequestDEPRECATED
type UpdateParticipantRequestDEPRECATED
type UpdateSessionEntityTypeRequestDEPRECATED
type UpdateVersionRequestDEPRECATED
type ValidationErrorDEPRECATED
type ValidationError_SeverityDEPRECATED
type ValidationResultDEPRECATED
type VersionDEPRECATED
type Version_VersionStatusDEPRECATED
type VersionsClientDEPRECATED
func NewVersionsClient(cc grpc.ClientConnInterface) VersionsClientDEPRECATED
type VersionsServerDEPRECATED
type VoiceSelectionParamsDEPRECATED
type WebhookRequestDEPRECATED
type WebhookResponseDEPRECATED
Constants ¶
View Source
const (
	AgentAssistantFeedback_ANSWER_RELEVANCE_UNSPECIFIED                                              = src.AgentAssistantFeedback_ANSWER_RELEVANCE_UNSPECIFIED
	AgentAssistantFeedback_CORRECT                                                                   = src.AgentAssistantFeedback_CORRECT
	AgentAssistantFeedback_DOCUMENT_CORRECTNESS_UNSPECIFIED                                          = src.AgentAssistantFeedback_DOCUMENT_CORRECTNESS_UNSPECIFIED
	AgentAssistantFeedback_DOCUMENT_EFFICIENCY_UNSPECIFIED                                           = src.AgentAssistantFeedback_DOCUMENT_EFFICIENCY_UNSPECIFIED
	AgentAssistantFeedback_EFFICIENT                                                                 = src.AgentAssistantFeedback_EFFICIENT
	AgentAssistantFeedback_INCORRECT                                                                 = src.AgentAssistantFeedback_INCORRECT
	AgentAssistantFeedback_INEFFICIENT                                                               = src.AgentAssistantFeedback_INEFFICIENT
	AgentAssistantFeedback_IRRELEVANT                                                                = src.AgentAssistantFeedback_IRRELEVANT
	AgentAssistantFeedback_RELEVANT                                                                  = src.AgentAssistantFeedback_RELEVANT
	Agent_API_VERSION_UNSPECIFIED                                                                    = src.Agent_API_VERSION_UNSPECIFIED
	Agent_API_VERSION_V1                                                                             = src.Agent_API_VERSION_V1
	Agent_API_VERSION_V2                                                                             = src.Agent_API_VERSION_V2
	Agent_API_VERSION_V2_BETA_1                                                                      = src.Agent_API_VERSION_V2_BETA_1
	Agent_MATCH_MODE_HYBRID                                                                          = src.Agent_MATCH_MODE_HYBRID
	Agent_MATCH_MODE_ML_ONLY                                                                         = src.Agent_MATCH_MODE_ML_ONLY
	Agent_MATCH_MODE_UNSPECIFIED                                                                     = src.Agent_MATCH_MODE_UNSPECIFIED
	Agent_TIER_ENTERPRISE                                                                            = src.Agent_TIER_ENTERPRISE
	Agent_TIER_ENTERPRISE_PLUS                                                                       = src.Agent_TIER_ENTERPRISE_PLUS
	Agent_TIER_STANDARD                                                                              = src.Agent_TIER_STANDARD
	Agent_TIER_UNSPECIFIED                                                                           = src.Agent_TIER_UNSPECIFIED
	AnswerFeedback_CORRECTNESS_LEVEL_UNSPECIFIED                                                     = src.AnswerFeedback_CORRECTNESS_LEVEL_UNSPECIFIED
	AnswerFeedback_FULLY_CORRECT                                                                     = src.AnswerFeedback_FULLY_CORRECT
	AnswerFeedback_NOT_CORRECT                                                                       = src.AnswerFeedback_NOT_CORRECT
	AnswerFeedback_PARTIALLY_CORRECT                                                                 = src.AnswerFeedback_PARTIALLY_CORRECT
	AudioEncoding_AUDIO_ENCODING_AMR                                                                 = src.AudioEncoding_AUDIO_ENCODING_AMR
	AudioEncoding_AUDIO_ENCODING_AMR_WB                                                              = src.AudioEncoding_AUDIO_ENCODING_AMR_WB
	AudioEncoding_AUDIO_ENCODING_FLAC                                                                = src.AudioEncoding_AUDIO_ENCODING_FLAC
	AudioEncoding_AUDIO_ENCODING_LINEAR_16                                                           = src.AudioEncoding_AUDIO_ENCODING_LINEAR_16
	AudioEncoding_AUDIO_ENCODING_MULAW                                                               = src.AudioEncoding_AUDIO_ENCODING_MULAW
	AudioEncoding_AUDIO_ENCODING_OGG_OPUS                                                            = src.AudioEncoding_AUDIO_ENCODING_OGG_OPUS
	AudioEncoding_AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE                                              = src.AudioEncoding_AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE
	AudioEncoding_AUDIO_ENCODING_UNSPECIFIED                                                         = src.AudioEncoding_AUDIO_ENCODING_UNSPECIFIED
	AutomatedAgentReply_AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED                                       = src.AutomatedAgentReply_AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED
	AutomatedAgentReply_FINAL                                                                        = src.AutomatedAgentReply_FINAL
	AutomatedAgentReply_PARTIAL                                                                      = src.AutomatedAgentReply_PARTIAL
	ConversationEvent_CONVERSATION_FINISHED                                                          = src.ConversationEvent_CONVERSATION_FINISHED
	ConversationEvent_CONVERSATION_STARTED                                                           = src.ConversationEvent_CONVERSATION_STARTED
	ConversationEvent_HUMAN_INTERVENTION_NEEDED                                                      = src.ConversationEvent_HUMAN_INTERVENTION_NEEDED
	ConversationEvent_NEW_MESSAGE                                                                    = src.ConversationEvent_NEW_MESSAGE
	ConversationEvent_TYPE_UNSPECIFIED                                                               = src.ConversationEvent_TYPE_UNSPECIFIED
	ConversationEvent_UNRECOVERABLE_ERROR                                                            = src.ConversationEvent_UNRECOVERABLE_ERROR
	ConversationModel_CREATING                                                                       = src.ConversationModel_CREATING
	ConversationModel_DELETING                                                                       = src.ConversationModel_DELETING
	ConversationModel_DEPLOYED                                                                       = src.ConversationModel_DEPLOYED
	ConversationModel_DEPLOYING                                                                      = src.ConversationModel_DEPLOYING
	ConversationModel_FAILED                                                                         = src.ConversationModel_FAILED
	ConversationModel_MODEL_TYPE_UNSPECIFIED                                                         = src.ConversationModel_MODEL_TYPE_UNSPECIFIED
	ConversationModel_PENDING                                                                        = src.ConversationModel_PENDING
	ConversationModel_SMART_REPLY_BERT_MODEL                                                         = src.ConversationModel_SMART_REPLY_BERT_MODEL
	ConversationModel_SMART_REPLY_DUAL_ENCODER_MODEL                                                 = src.ConversationModel_SMART_REPLY_DUAL_ENCODER_MODEL
	ConversationModel_STATE_UNSPECIFIED                                                              = src.ConversationModel_STATE_UNSPECIFIED
	ConversationModel_UNDEPLOYED                                                                     = src.ConversationModel_UNDEPLOYED
	ConversationModel_UNDEPLOYING                                                                    = src.ConversationModel_UNDEPLOYING
	Conversation_COMPLETED                                                                           = src.Conversation_COMPLETED
	Conversation_CONVERSATION_STAGE_UNSPECIFIED                                                      = src.Conversation_CONVERSATION_STAGE_UNSPECIFIED
	Conversation_HUMAN_ASSIST_STAGE                                                                  = src.Conversation_HUMAN_ASSIST_STAGE
	Conversation_IN_PROGRESS                                                                         = src.Conversation_IN_PROGRESS
	Conversation_LIFECYCLE_STATE_UNSPECIFIED                                                         = src.Conversation_LIFECYCLE_STATE_UNSPECIFIED
	Conversation_VIRTUAL_AGENT_STAGE                                                                 = src.Conversation_VIRTUAL_AGENT_STAGE
	CreateConversationModelEvaluationOperationMetadata_CANCELLED                                     = src.CreateConversationModelEvaluationOperationMetadata_CANCELLED
	CreateConversationModelEvaluationOperationMetadata_FAILED                                        = src.CreateConversationModelEvaluationOperationMetadata_FAILED
	CreateConversationModelEvaluationOperationMetadata_INITIALIZING                                  = src.CreateConversationModelEvaluationOperationMetadata_INITIALIZING
	CreateConversationModelEvaluationOperationMetadata_RUNNING                                       = src.CreateConversationModelEvaluationOperationMetadata_RUNNING
	CreateConversationModelEvaluationOperationMetadata_STATE_UNSPECIFIED                             = src.CreateConversationModelEvaluationOperationMetadata_STATE_UNSPECIFIED
	CreateConversationModelEvaluationOperationMetadata_SUCCEEDED                                     = src.CreateConversationModelEvaluationOperationMetadata_SUCCEEDED
	CreateConversationModelOperationMetadata_CANCELLED                                               = src.CreateConversationModelOperationMetadata_CANCELLED
	CreateConversationModelOperationMetadata_CANCELLING                                              = src.CreateConversationModelOperationMetadata_CANCELLING
	CreateConversationModelOperationMetadata_FAILED                                                  = src.CreateConversationModelOperationMetadata_FAILED
	CreateConversationModelOperationMetadata_PENDING                                                 = src.CreateConversationModelOperationMetadata_PENDING
	CreateConversationModelOperationMetadata_STATE_UNSPECIFIED                                       = src.CreateConversationModelOperationMetadata_STATE_UNSPECIFIED
	CreateConversationModelOperationMetadata_SUCCEEDED                                               = src.CreateConversationModelOperationMetadata_SUCCEEDED
	CreateConversationModelOperationMetadata_TRAINING                                                = src.CreateConversationModelOperationMetadata_TRAINING
	Document_ACTIVE                                                                                  = src.Document_ACTIVE
	Document_AGENT_FACING_SMART_REPLY                                                                = src.Document_AGENT_FACING_SMART_REPLY
	Document_ARTICLE_SUGGESTION                                                                      = src.Document_ARTICLE_SUGGESTION
	Document_CREATING                                                                                = src.Document_CREATING
	Document_DELETING                                                                                = src.Document_DELETING
	Document_EXTRACTIVE_QA                                                                           = src.Document_EXTRACTIVE_QA
	Document_FAQ                                                                                     = src.Document_FAQ
	Document_KNOWLEDGE_TYPE_UNSPECIFIED                                                              = src.Document_KNOWLEDGE_TYPE_UNSPECIFIED
	Document_RELOADING                                                                               = src.Document_RELOADING
	Document_STATE_UNSPECIFIED                                                                       = src.Document_STATE_UNSPECIFIED
	Document_UPDATING                                                                                = src.Document_UPDATING
	EntityType_AUTO_EXPANSION_MODE_DEFAULT                                                           = src.EntityType_AUTO_EXPANSION_MODE_DEFAULT
	EntityType_AUTO_EXPANSION_MODE_UNSPECIFIED                                                       = src.EntityType_AUTO_EXPANSION_MODE_UNSPECIFIED
	EntityType_KIND_LIST                                                                             = src.EntityType_KIND_LIST
	EntityType_KIND_MAP                                                                              = src.EntityType_KIND_MAP
	EntityType_KIND_REGEXP                                                                           = src.EntityType_KIND_REGEXP
	EntityType_KIND_UNSPECIFIED                                                                      = src.EntityType_KIND_UNSPECIFIED
	Environment_LOADING                                                                              = src.Environment_LOADING
	Environment_RUNNING                                                                              = src.Environment_RUNNING
	Environment_STATE_UNSPECIFIED                                                                    = src.Environment_STATE_UNSPECIFIED
	Environment_STOPPED                                                                              = src.Environment_STOPPED
	Fulfillment_Feature_SMALLTALK                                                                    = src.Fulfillment_Feature_SMALLTALK
	Fulfillment_Feature_TYPE_UNSPECIFIED                                                             = src.Fulfillment_Feature_TYPE_UNSPECIFIED
	IntentView_INTENT_VIEW_FULL                                                                      = src.IntentView_INTENT_VIEW_FULL
	IntentView_INTENT_VIEW_UNSPECIFIED                                                               = src.IntentView_INTENT_VIEW_UNSPECIFIED
	Intent_Message_ACTIONS_ON_GOOGLE                                                                 = src.Intent_Message_ACTIONS_ON_GOOGLE
	Intent_Message_BrowseCarouselCard_BLURRED_BACKGROUND                                             = src.Intent_Message_BrowseCarouselCard_BLURRED_BACKGROUND
	Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_AMP_ACTION                = src.Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_AMP_ACTION
	Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_AMP_CONTENT               = src.Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_AMP_CONTENT
	Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_URL_TYPE_HINT_UNSPECIFIED = src.Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_URL_TYPE_HINT_UNSPECIFIED
	Intent_Message_BrowseCarouselCard_CROPPED                                                        = src.Intent_Message_BrowseCarouselCard_CROPPED
	Intent_Message_BrowseCarouselCard_GRAY                                                           = src.Intent_Message_BrowseCarouselCard_GRAY
	Intent_Message_BrowseCarouselCard_IMAGE_DISPLAY_OPTIONS_UNSPECIFIED                              = src.Intent_Message_BrowseCarouselCard_IMAGE_DISPLAY_OPTIONS_UNSPECIFIED
	Intent_Message_BrowseCarouselCard_WHITE                                                          = src.Intent_Message_BrowseCarouselCard_WHITE
	Intent_Message_ColumnProperties_CENTER                                                           = src.Intent_Message_ColumnProperties_CENTER
	Intent_Message_ColumnProperties_HORIZONTAL_ALIGNMENT_UNSPECIFIED                                 = src.Intent_Message_ColumnProperties_HORIZONTAL_ALIGNMENT_UNSPECIFIED
	Intent_Message_ColumnProperties_LEADING                                                          = src.Intent_Message_ColumnProperties_LEADING
	Intent_Message_ColumnProperties_TRAILING                                                         = src.Intent_Message_ColumnProperties_TRAILING
	Intent_Message_FACEBOOK                                                                          = src.Intent_Message_FACEBOOK
	Intent_Message_GOOGLE_HANGOUTS                                                                   = src.Intent_Message_GOOGLE_HANGOUTS
	Intent_Message_KIK                                                                               = src.Intent_Message_KIK
	Intent_Message_LINE                                                                              = src.Intent_Message_LINE
	Intent_Message_MediaContent_AUDIO                                                                = src.Intent_Message_MediaContent_AUDIO
	Intent_Message_MediaContent_RESPONSE_MEDIA_TYPE_UNSPECIFIED                                      = src.Intent_Message_MediaContent_RESPONSE_MEDIA_TYPE_UNSPECIFIED
	Intent_Message_PLATFORM_UNSPECIFIED                                                              = src.Intent_Message_PLATFORM_UNSPECIFIED
	Intent_Message_SKYPE                                                                             = src.Intent_Message_SKYPE
	Intent_Message_SLACK                                                                             = src.Intent_Message_SLACK
	Intent_Message_TELEGRAM                                                                          = src.Intent_Message_TELEGRAM
	Intent_Message_VIBER                                                                             = src.Intent_Message_VIBER
	Intent_TrainingPhrase_EXAMPLE                                                                    = src.Intent_TrainingPhrase_EXAMPLE
	Intent_TrainingPhrase_TEMPLATE                                                                   = src.Intent_TrainingPhrase_TEMPLATE
	Intent_TrainingPhrase_TYPE_UNSPECIFIED                                                           = src.Intent_TrainingPhrase_TYPE_UNSPECIFIED
	Intent_WEBHOOK_STATE_ENABLED                                                                     = src.Intent_WEBHOOK_STATE_ENABLED
	Intent_WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING                                                    = src.Intent_WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING
	Intent_WEBHOOK_STATE_UNSPECIFIED                                                                 = src.Intent_WEBHOOK_STATE_UNSPECIFIED
	KnowledgeOperationMetadata_DONE                                                                  = src.KnowledgeOperationMetadata_DONE
	KnowledgeOperationMetadata_PENDING                                                               = src.KnowledgeOperationMetadata_PENDING
	KnowledgeOperationMetadata_RUNNING                                                               = src.KnowledgeOperationMetadata_RUNNING
	KnowledgeOperationMetadata_STATE_UNSPECIFIED                                                     = src.KnowledgeOperationMetadata_STATE_UNSPECIFIED
	NotificationConfig_JSON                                                                          = src.NotificationConfig_JSON
	NotificationConfig_MESSAGE_FORMAT_UNSPECIFIED                                                    = src.NotificationConfig_MESSAGE_FORMAT_UNSPECIFIED
	NotificationConfig_PROTO                                                                         = src.NotificationConfig_PROTO
	OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_LINEAR_16                                              = src.OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_LINEAR_16
	OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_MP3                                                    = src.OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_MP3
	OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_MP3_64_KBPS                                            = src.OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_MP3_64_KBPS
	OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_MULAW                                                  = src.OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_MULAW
	OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_OGG_OPUS                                               = src.OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_OGG_OPUS
	OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_UNSPECIFIED                                            = src.OutputAudioEncoding_OUTPUT_AUDIO_ENCODING_UNSPECIFIED
	Participant_AUTOMATED_AGENT                                                                      = src.Participant_AUTOMATED_AGENT
	Participant_END_USER                                                                             = src.Participant_END_USER
	Participant_HUMAN_AGENT                                                                          = src.Participant_HUMAN_AGENT
	Participant_ROLE_UNSPECIFIED                                                                     = src.Participant_ROLE_UNSPECIFIED
	SessionEntityType_ENTITY_OVERRIDE_MODE_OVERRIDE                                                  = src.SessionEntityType_ENTITY_OVERRIDE_MODE_OVERRIDE
	SessionEntityType_ENTITY_OVERRIDE_MODE_SUPPLEMENT                                                = src.SessionEntityType_ENTITY_OVERRIDE_MODE_SUPPLEMENT
	SessionEntityType_ENTITY_OVERRIDE_MODE_UNSPECIFIED                                               = src.SessionEntityType_ENTITY_OVERRIDE_MODE_UNSPECIFIED
	SpeechModelVariant_SPEECH_MODEL_VARIANT_UNSPECIFIED                                              = src.SpeechModelVariant_SPEECH_MODEL_VARIANT_UNSPECIFIED
	SpeechModelVariant_USE_BEST_AVAILABLE                                                            = src.SpeechModelVariant_USE_BEST_AVAILABLE
	SpeechModelVariant_USE_ENHANCED                                                                  = src.SpeechModelVariant_USE_ENHANCED
	SpeechModelVariant_USE_STANDARD                                                                  = src.SpeechModelVariant_USE_STANDARD
	SsmlVoiceGender_SSML_VOICE_GENDER_FEMALE                                                         = src.SsmlVoiceGender_SSML_VOICE_GENDER_FEMALE
	SsmlVoiceGender_SSML_VOICE_GENDER_MALE                                                           = src.SsmlVoiceGender_SSML_VOICE_GENDER_MALE
	SsmlVoiceGender_SSML_VOICE_GENDER_NEUTRAL                                                        = src.SsmlVoiceGender_SSML_VOICE_GENDER_NEUTRAL
	SsmlVoiceGender_SSML_VOICE_GENDER_UNSPECIFIED                                                    = src.SsmlVoiceGender_SSML_VOICE_GENDER_UNSPECIFIED
	StreamingRecognitionResult_END_OF_SINGLE_UTTERANCE                                               = src.StreamingRecognitionResult_END_OF_SINGLE_UTTERANCE
	StreamingRecognitionResult_MESSAGE_TYPE_UNSPECIFIED                                              = src.StreamingRecognitionResult_MESSAGE_TYPE_UNSPECIFIED
	StreamingRecognitionResult_TRANSCRIPT                                                            = src.StreamingRecognitionResult_TRANSCRIPT
	SuggestionFeature_ARTICLE_SUGGESTION                                                             = src.SuggestionFeature_ARTICLE_SUGGESTION
	SuggestionFeature_FAQ                                                                            = src.SuggestionFeature_FAQ
	SuggestionFeature_SMART_REPLY                                                                    = src.SuggestionFeature_SMART_REPLY
	SuggestionFeature_TYPE_UNSPECIFIED                                                               = src.SuggestionFeature_TYPE_UNSPECIFIED
	ValidationError_CRITICAL                                                                         = src.ValidationError_CRITICAL
	ValidationError_ERROR                                                                            = src.ValidationError_ERROR
	ValidationError_INFO                                                                             = src.ValidationError_INFO
	ValidationError_SEVERITY_UNSPECIFIED                                                             = src.ValidationError_SEVERITY_UNSPECIFIED
	ValidationError_WARNING                                                                          = src.ValidationError_WARNING
	Version_FAILED                                                                                   = src.Version_FAILED
	Version_IN_PROGRESS                                                                              = src.Version_IN_PROGRESS
	Version_READY                                                                                    = src.Version_READY
	Version_VERSION_STATUS_UNSPECIFIED                                                               = src.Version_VERSION_STATUS_UNSPECIFIED
)

Deprecated: Please use consts in: cloud.google.com/go/dialogflow/apiv2/dialogflowpb

Variables ¶
View Source
var (
	AgentAssistantFeedback_AnswerRelevance_name                                              = src.AgentAssistantFeedback_AnswerRelevance_name
	AgentAssistantFeedback_AnswerRelevance_value                                             = src.AgentAssistantFeedback_AnswerRelevance_value
	AgentAssistantFeedback_DocumentCorrectness_name                                          = src.AgentAssistantFeedback_DocumentCorrectness_name
	AgentAssistantFeedback_DocumentCorrectness_value                                         = src.AgentAssistantFeedback_DocumentCorrectness_value
	AgentAssistantFeedback_DocumentEfficiency_name                                           = src.AgentAssistantFeedback_DocumentEfficiency_name
	AgentAssistantFeedback_DocumentEfficiency_value                                          = src.AgentAssistantFeedback_DocumentEfficiency_value
	Agent_ApiVersion_name                                                                    = src.Agent_ApiVersion_name
	Agent_ApiVersion_value                                                                   = src.Agent_ApiVersion_value
	Agent_MatchMode_name                                                                     = src.Agent_MatchMode_name
	Agent_MatchMode_value                                                                    = src.Agent_MatchMode_value
	Agent_Tier_name                                                                          = src.Agent_Tier_name
	Agent_Tier_value                                                                         = src.Agent_Tier_value
	AnswerFeedback_CorrectnessLevel_name                                                     = src.AnswerFeedback_CorrectnessLevel_name
	AnswerFeedback_CorrectnessLevel_value                                                    = src.AnswerFeedback_CorrectnessLevel_value
	AudioEncoding_name                                                                       = src.AudioEncoding_name
	AudioEncoding_value                                                                      = src.AudioEncoding_value
	AutomatedAgentReply_AutomatedAgentReplyType_name                                         = src.AutomatedAgentReply_AutomatedAgentReplyType_name
	AutomatedAgentReply_AutomatedAgentReplyType_value                                        = src.AutomatedAgentReply_AutomatedAgentReplyType_value
	ConversationEvent_Type_name                                                              = src.ConversationEvent_Type_name
	ConversationEvent_Type_value                                                             = src.ConversationEvent_Type_value
	ConversationModel_ModelType_name                                                         = src.ConversationModel_ModelType_name
	ConversationModel_ModelType_value                                                        = src.ConversationModel_ModelType_value
	ConversationModel_State_name                                                             = src.ConversationModel_State_name
	ConversationModel_State_value                                                            = src.ConversationModel_State_value
	Conversation_ConversationStage_name                                                      = src.Conversation_ConversationStage_name
	Conversation_ConversationStage_value                                                     = src.Conversation_ConversationStage_value
	Conversation_LifecycleState_name                                                         = src.Conversation_LifecycleState_name
	Conversation_LifecycleState_value                                                        = src.Conversation_LifecycleState_value
	CreateConversationModelEvaluationOperationMetadata_State_name                            = src.CreateConversationModelEvaluationOperationMetadata_State_name
	CreateConversationModelEvaluationOperationMetadata_State_value                           = src.CreateConversationModelEvaluationOperationMetadata_State_value
	CreateConversationModelOperationMetadata_State_name                                      = src.CreateConversationModelOperationMetadata_State_name
	CreateConversationModelOperationMetadata_State_value                                     = src.CreateConversationModelOperationMetadata_State_value
	Document_KnowledgeType_name                                                              = src.Document_KnowledgeType_name
	Document_KnowledgeType_value                                                             = src.Document_KnowledgeType_value
	Document_State_name                                                                      = src.Document_State_name
	Document_State_value                                                                     = src.Document_State_value
	EntityType_AutoExpansionMode_name                                                        = src.EntityType_AutoExpansionMode_name
	EntityType_AutoExpansionMode_value                                                       = src.EntityType_AutoExpansionMode_value
	EntityType_Kind_name                                                                     = src.EntityType_Kind_name
	EntityType_Kind_value                                                                    = src.EntityType_Kind_value
	Environment_State_name                                                                   = src.Environment_State_name
	Environment_State_value                                                                  = src.Environment_State_value
	File_google_cloud_dialogflow_v2_agent_proto                                              = src.File_google_cloud_dialogflow_v2_agent_proto
	File_google_cloud_dialogflow_v2_answer_record_proto                                      = src.File_google_cloud_dialogflow_v2_answer_record_proto
	File_google_cloud_dialogflow_v2_audio_config_proto                                       = src.File_google_cloud_dialogflow_v2_audio_config_proto
	File_google_cloud_dialogflow_v2_context_proto                                            = src.File_google_cloud_dialogflow_v2_context_proto
	File_google_cloud_dialogflow_v2_conversation_dataset_proto                               = src.File_google_cloud_dialogflow_v2_conversation_dataset_proto
	File_google_cloud_dialogflow_v2_conversation_event_proto                                 = src.File_google_cloud_dialogflow_v2_conversation_event_proto
	File_google_cloud_dialogflow_v2_conversation_model_proto                                 = src.File_google_cloud_dialogflow_v2_conversation_model_proto
	File_google_cloud_dialogflow_v2_conversation_profile_proto                               = src.File_google_cloud_dialogflow_v2_conversation_profile_proto
	File_google_cloud_dialogflow_v2_conversation_proto                                       = src.File_google_cloud_dialogflow_v2_conversation_proto
	File_google_cloud_dialogflow_v2_document_proto                                           = src.File_google_cloud_dialogflow_v2_document_proto
	File_google_cloud_dialogflow_v2_entity_type_proto                                        = src.File_google_cloud_dialogflow_v2_entity_type_proto
	File_google_cloud_dialogflow_v2_environment_proto                                        = src.File_google_cloud_dialogflow_v2_environment_proto
	File_google_cloud_dialogflow_v2_fulfillment_proto                                        = src.File_google_cloud_dialogflow_v2_fulfillment_proto
	File_google_cloud_dialogflow_v2_gcs_proto                                                = src.File_google_cloud_dialogflow_v2_gcs_proto
	File_google_cloud_dialogflow_v2_human_agent_assistant_event_proto                        = src.File_google_cloud_dialogflow_v2_human_agent_assistant_event_proto
	File_google_cloud_dialogflow_v2_intent_proto                                             = src.File_google_cloud_dialogflow_v2_intent_proto
	File_google_cloud_dialogflow_v2_knowledge_base_proto                                     = src.File_google_cloud_dialogflow_v2_knowledge_base_proto
	File_google_cloud_dialogflow_v2_participant_proto                                        = src.File_google_cloud_dialogflow_v2_participant_proto
	File_google_cloud_dialogflow_v2_session_entity_type_proto                                = src.File_google_cloud_dialogflow_v2_session_entity_type_proto
	File_google_cloud_dialogflow_v2_session_proto                                            = src.File_google_cloud_dialogflow_v2_session_proto
	File_google_cloud_dialogflow_v2_validation_result_proto                                  = src.File_google_cloud_dialogflow_v2_validation_result_proto
	File_google_cloud_dialogflow_v2_version_proto                                            = src.File_google_cloud_dialogflow_v2_version_proto
	File_google_cloud_dialogflow_v2_webhook_proto                                            = src.File_google_cloud_dialogflow_v2_webhook_proto
	Fulfillment_Feature_Type_name                                                            = src.Fulfillment_Feature_Type_name
	Fulfillment_Feature_Type_value                                                           = src.Fulfillment_Feature_Type_value
	IntentView_name                                                                          = src.IntentView_name
	IntentView_value                                                                         = src.IntentView_value
	Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_UrlTypeHint_name  = src.Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_UrlTypeHint_name
	Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_UrlTypeHint_value = src.Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_UrlTypeHint_value
	Intent_Message_BrowseCarouselCard_ImageDisplayOptions_name                               = src.Intent_Message_BrowseCarouselCard_ImageDisplayOptions_name
	Intent_Message_BrowseCarouselCard_ImageDisplayOptions_value                              = src.Intent_Message_BrowseCarouselCard_ImageDisplayOptions_value
	Intent_Message_ColumnProperties_HorizontalAlignment_name                                 = src.Intent_Message_ColumnProperties_HorizontalAlignment_name
	Intent_Message_ColumnProperties_HorizontalAlignment_value                                = src.Intent_Message_ColumnProperties_HorizontalAlignment_value
	Intent_Message_MediaContent_ResponseMediaType_name                                       = src.Intent_Message_MediaContent_ResponseMediaType_name
	Intent_Message_MediaContent_ResponseMediaType_value                                      = src.Intent_Message_MediaContent_ResponseMediaType_value
	Intent_Message_Platform_name                                                             = src.Intent_Message_Platform_name
	Intent_Message_Platform_value                                                            = src.Intent_Message_Platform_value
	Intent_TrainingPhrase_Type_name                                                          = src.Intent_TrainingPhrase_Type_name
	Intent_TrainingPhrase_Type_value                                                         = src.Intent_TrainingPhrase_Type_value
	Intent_WebhookState_name                                                                 = src.Intent_WebhookState_name
	Intent_WebhookState_value                                                                = src.Intent_WebhookState_value
	KnowledgeOperationMetadata_State_name                                                    = src.KnowledgeOperationMetadata_State_name
	KnowledgeOperationMetadata_State_value                                                   = src.KnowledgeOperationMetadata_State_value
	NotificationConfig_MessageFormat_name                                                    = src.NotificationConfig_MessageFormat_name
	NotificationConfig_MessageFormat_value                                                   = src.NotificationConfig_MessageFormat_value
	OutputAudioEncoding_name                                                                 = src.OutputAudioEncoding_name
	OutputAudioEncoding_value                                                                = src.OutputAudioEncoding_value
	Participant_Role_name                                                                    = src.Participant_Role_name
	Participant_Role_value                                                                   = src.Participant_Role_value
	SessionEntityType_EntityOverrideMode_name                                                = src.SessionEntityType_EntityOverrideMode_name
	SessionEntityType_EntityOverrideMode_value                                               = src.SessionEntityType_EntityOverrideMode_value
	SpeechModelVariant_name                                                                  = src.SpeechModelVariant_name
	SpeechModelVariant_value                                                                 = src.SpeechModelVariant_value
	SsmlVoiceGender_name                                                                     = src.SsmlVoiceGender_name
	SsmlVoiceGender_value                                                                    = src.SsmlVoiceGender_value
	StreamingRecognitionResult_MessageType_name                                              = src.StreamingRecognitionResult_MessageType_name
	StreamingRecognitionResult_MessageType_value                                             = src.StreamingRecognitionResult_MessageType_value
	SuggestionFeature_Type_name                                                              = src.SuggestionFeature_Type_name
	SuggestionFeature_Type_value                                                             = src.SuggestionFeature_Type_value
	ValidationError_Severity_name                                                            = src.ValidationError_Severity_name
	ValidationError_Severity_value                                                           = src.ValidationError_Severity_value
	Version_VersionStatus_name                                                               = src.Version_VersionStatus_name
	Version_VersionStatus_value                                                              = src.Version_VersionStatus_value
)

Deprecated: Please use vars in: cloud.google.com/go/dialogflow/apiv2/dialogflowpb

Functions ¶
func
RegisterAgentsServer
DEPRECATED
func
RegisterAnswerRecordsServer
DEPRECATED
func
RegisterContextsServer
DEPRECATED
func
RegisterConversationDatasetsServer
DEPRECATED
func
RegisterConversationModelsServer
DEPRECATED
func
RegisterConversationProfilesServer
DEPRECATED
func
RegisterConversationsServer
DEPRECATED
func
RegisterDocumentsServer
DEPRECATED
func
RegisterEntityTypesServer
DEPRECATED
func
RegisterEnvironmentsServer
DEPRECATED
func
RegisterFulfillmentsServer
DEPRECATED
func
RegisterIntentsServer
DEPRECATED
func
RegisterKnowledgeBasesServer
DEPRECATED
func
RegisterParticipantsServer
DEPRECATED
func
RegisterSessionEntityTypesServer
DEPRECATED
func
RegisterSessionsServer
DEPRECATED
func
RegisterVersionsServer
DEPRECATED
Types ¶
type
Agent
DEPRECATED
type
AgentAssistantFeedback
DEPRECATED
type
AgentAssistantFeedback_AnswerRelevance
DEPRECATED
type
AgentAssistantFeedback_DocumentCorrectness
DEPRECATED
type
AgentAssistantFeedback_DocumentEfficiency
DEPRECATED
type
AgentAssistantRecord
DEPRECATED
type AgentAssistantRecord_ArticleSuggestionAnswer ¶
type AgentAssistantRecord_ArticleSuggestionAnswer = src.AgentAssistantRecord_ArticleSuggestionAnswer
type AgentAssistantRecord_FaqAnswer ¶
type AgentAssistantRecord_FaqAnswer = src.AgentAssistantRecord_FaqAnswer
type
Agent_ApiVersion
DEPRECATED
type
Agent_MatchMode
DEPRECATED
type
Agent_Tier
DEPRECATED
type
AgentsClient
DEPRECATED
type
AgentsServer
DEPRECATED
type
AnalyzeContentRequest
DEPRECATED
type AnalyzeContentRequest_EventInput ¶
type AnalyzeContentRequest_EventInput = src.AnalyzeContentRequest_EventInput
type AnalyzeContentRequest_TextInput ¶
type AnalyzeContentRequest_TextInput = src.AnalyzeContentRequest_TextInput
type
AnalyzeContentResponse
DEPRECATED
type
AnnotatedMessagePart
DEPRECATED
type
AnswerFeedback
DEPRECATED
type AnswerFeedback_AgentAssistantDetailFeedback ¶
type AnswerFeedback_AgentAssistantDetailFeedback = src.AnswerFeedback_AgentAssistantDetailFeedback
type
AnswerFeedback_CorrectnessLevel
DEPRECATED
type
AnswerRecord
DEPRECATED
type AnswerRecord_AgentAssistantRecord ¶
type AnswerRecord_AgentAssistantRecord = src.AnswerRecord_AgentAssistantRecord
type
AnswerRecordsClient
DEPRECATED
type
AnswerRecordsServer
DEPRECATED
type
ArticleAnswer
DEPRECATED
type
ArticleSuggestionModelMetadata
DEPRECATED
type
AssistQueryParameters
DEPRECATED
type
AudioEncoding
DEPRECATED
type
AutomatedAgentConfig
DEPRECATED
type
AutomatedAgentReply
DEPRECATED
type
AutomatedAgentReply_AutomatedAgentReplyType
DEPRECATED
type
BatchCreateEntitiesRequest
DEPRECATED
type
BatchDeleteEntitiesRequest
DEPRECATED
type
BatchDeleteEntityTypesRequest
DEPRECATED
type
BatchDeleteIntentsRequest
DEPRECATED
type
BatchUpdateEntitiesRequest
DEPRECATED
type
BatchUpdateEntityTypesRequest
DEPRECATED
type BatchUpdateEntityTypesRequest_EntityTypeBatchInline ¶
type BatchUpdateEntityTypesRequest_EntityTypeBatchInline = src.BatchUpdateEntityTypesRequest_EntityTypeBatchInline
type BatchUpdateEntityTypesRequest_EntityTypeBatchUri ¶
type BatchUpdateEntityTypesRequest_EntityTypeBatchUri = src.BatchUpdateEntityTypesRequest_EntityTypeBatchUri
type
BatchUpdateEntityTypesResponse
DEPRECATED
type BatchUpdateIntentsRequest ¶
type BatchUpdateIntentsRequest = src.BatchUpdateIntentsRequest
type BatchUpdateIntentsRequest_IntentBatchInline ¶
type BatchUpdateIntentsRequest_IntentBatchInline = src.BatchUpdateIntentsRequest_IntentBatchInline
type BatchUpdateIntentsRequest_IntentBatchUri ¶
type BatchUpdateIntentsRequest_IntentBatchUri = src.BatchUpdateIntentsRequest_IntentBatchUri
type
BatchUpdateIntentsResponse
DEPRECATED
type
ClearSuggestionFeatureConfigOperationMetadata
DEPRECATED
type
ClearSuggestionFeatureConfigRequest
DEPRECATED
type
CompleteConversationRequest
DEPRECATED
type
Context
DEPRECATED
type
ContextsClient
DEPRECATED
type
ContextsServer
DEPRECATED
type
Conversation
DEPRECATED
type
ConversationDataset
DEPRECATED
type
ConversationDatasetsClient
DEPRECATED
type
ConversationDatasetsServer
DEPRECATED
type
ConversationEvent
DEPRECATED
type ConversationEvent_NewMessagePayload ¶
type ConversationEvent_NewMessagePayload = src.ConversationEvent_NewMessagePayload
type
ConversationEvent_Type
DEPRECATED
type
ConversationInfo
DEPRECATED
type
ConversationModel
DEPRECATED
type
ConversationModelEvaluation
DEPRECATED
type ConversationModelEvaluation_SmartReplyMetrics ¶
type ConversationModelEvaluation_SmartReplyMetrics = src.ConversationModelEvaluation_SmartReplyMetrics
type ConversationModel_ArticleSuggestionModelMetadata ¶
type ConversationModel_ArticleSuggestionModelMetadata = src.ConversationModel_ArticleSuggestionModelMetadata
type
ConversationModel_ModelType
DEPRECATED
type ConversationModel_SmartReplyModelMetadata ¶
type ConversationModel_SmartReplyModelMetadata = src.ConversationModel_SmartReplyModelMetadata
type
ConversationModel_State
DEPRECATED
type
ConversationModelsClient
DEPRECATED
type
ConversationModelsServer
DEPRECATED
type
ConversationPhoneNumber
DEPRECATED
type
ConversationProfile
DEPRECATED
type
ConversationProfilesClient
DEPRECATED
type
ConversationProfilesServer
DEPRECATED
type
Conversation_ConversationStage
DEPRECATED
type
Conversation_LifecycleState
DEPRECATED
type
ConversationsClient
DEPRECATED
type
ConversationsServer
DEPRECATED
type
CreateContextRequest
DEPRECATED
type
CreateConversationDatasetOperationMetadata
DEPRECATED
type
CreateConversationDatasetRequest
DEPRECATED
type
CreateConversationModelEvaluationOperationMetadata
DEPRECATED
type
CreateConversationModelEvaluationOperationMetadata_State
DEPRECATED
type
CreateConversationModelEvaluationRequest
DEPRECATED
type
CreateConversationModelOperationMetadata
DEPRECATED
type
CreateConversationModelOperationMetadata_State
DEPRECATED
type
CreateConversationModelRequest
DEPRECATED
type
CreateConversationProfileRequest
DEPRECATED
type
CreateConversationRequest
DEPRECATED
type
CreateDocumentRequest
DEPRECATED
type
CreateEntityTypeRequest
DEPRECATED
type
CreateEnvironmentRequest
DEPRECATED
type
CreateIntentRequest
DEPRECATED
type
CreateKnowledgeBaseRequest
DEPRECATED
type
CreateParticipantRequest
DEPRECATED
type
CreateSessionEntityTypeRequest
DEPRECATED
type
CreateVersionRequest
DEPRECATED
type
DeleteAgentRequest
DEPRECATED
type
DeleteAllContextsRequest
DEPRECATED
type
DeleteContextRequest
DEPRECATED
type
DeleteConversationDatasetOperationMetadata
DEPRECATED
type
DeleteConversationDatasetRequest
DEPRECATED
type
DeleteConversationModelOperationMetadata
DEPRECATED
type
DeleteConversationModelRequest
DEPRECATED
type
DeleteConversationProfileRequest
DEPRECATED
type
DeleteDocumentRequest
DEPRECATED
type
DeleteEntityTypeRequest
DEPRECATED
type
DeleteEnvironmentRequest
DEPRECATED
type
DeleteIntentRequest
DEPRECATED
type
DeleteKnowledgeBaseRequest
DEPRECATED
type
DeleteSessionEntityTypeRequest
DEPRECATED
type
DeleteVersionRequest
DEPRECATED
type
DeployConversationModelOperationMetadata
DEPRECATED
type
DeployConversationModelRequest
DEPRECATED
type
DetectIntentRequest
DEPRECATED
type
DetectIntentResponse
DEPRECATED
type
Document
DEPRECATED
type Document_ContentUri ¶
type Document_ContentUri = src.Document_ContentUri
type
Document_KnowledgeType
DEPRECATED
type Document_RawContent ¶
type Document_RawContent = src.Document_RawContent
type
Document_ReloadStatus
DEPRECATED
type
Document_State
DEPRECATED
type
DocumentsClient
DEPRECATED
type
DocumentsServer
DEPRECATED
type
DtmfParameters
DEPRECATED
type
EntityType
DEPRECATED
type
EntityTypeBatch
DEPRECATED
type
EntityType_AutoExpansionMode
DEPRECATED
type
EntityType_Entity
DEPRECATED
type
EntityType_Kind
DEPRECATED
type
EntityTypesClient
DEPRECATED
type
EntityTypesServer
DEPRECATED
type
Environment
DEPRECATED
type
EnvironmentHistory
DEPRECATED
type
EnvironmentHistory_Entry
DEPRECATED
type
Environment_State
DEPRECATED
type
EnvironmentsClient
DEPRECATED
type
EnvironmentsServer
DEPRECATED
type
EvaluationConfig
DEPRECATED
type
EvaluationConfig_SmartComposeConfig
DEPRECATED
type EvaluationConfig_SmartComposeConfig_ ¶
type EvaluationConfig_SmartComposeConfig_ = src.EvaluationConfig_SmartComposeConfig_
type
EvaluationConfig_SmartReplyConfig
DEPRECATED
type EvaluationConfig_SmartReplyConfig_ ¶
type EvaluationConfig_SmartReplyConfig_ = src.EvaluationConfig_SmartReplyConfig_
type
EventInput
DEPRECATED
type
ExportAgentRequest
DEPRECATED
type
ExportAgentResponse
DEPRECATED
type ExportAgentResponse_AgentContent ¶
type ExportAgentResponse_AgentContent = src.ExportAgentResponse_AgentContent
type ExportAgentResponse_AgentUri ¶
type ExportAgentResponse_AgentUri = src.ExportAgentResponse_AgentUri
type
ExportDocumentRequest
DEPRECATED
type ExportDocumentRequest_GcsDestination ¶
type ExportDocumentRequest_GcsDestination = src.ExportDocumentRequest_GcsDestination
type
ExportOperationMetadata
DEPRECATED
type
FaqAnswer
DEPRECATED
type
Fulfillment
DEPRECATED
type
Fulfillment_Feature
DEPRECATED
type
Fulfillment_Feature_Type
DEPRECATED
type
Fulfillment_GenericWebService
DEPRECATED
type Fulfillment_GenericWebService_ ¶
type Fulfillment_GenericWebService_ = src.Fulfillment_GenericWebService_
type
FulfillmentsClient
DEPRECATED
type
FulfillmentsServer
DEPRECATED
type
GcsDestination
DEPRECATED
type
GcsSources
DEPRECATED
type
GetAgentRequest
DEPRECATED
type
GetContextRequest
DEPRECATED
type
GetConversationDatasetRequest
DEPRECATED
type
GetConversationModelEvaluationRequest
DEPRECATED
type
GetConversationModelRequest
DEPRECATED
type
GetConversationProfileRequest
DEPRECATED
type
GetConversationRequest
DEPRECATED
type
GetDocumentRequest
DEPRECATED
type
GetEntityTypeRequest
DEPRECATED
type
GetEnvironmentHistoryRequest
DEPRECATED
type
GetEnvironmentRequest
DEPRECATED
type
GetFulfillmentRequest
DEPRECATED
type
GetIntentRequest
DEPRECATED
type
GetKnowledgeBaseRequest
DEPRECATED
type
GetParticipantRequest
DEPRECATED
type
GetSessionEntityTypeRequest
DEPRECATED
type
GetValidationResultRequest
DEPRECATED
type
GetVersionRequest
DEPRECATED
type
HumanAgentAssistantConfig
DEPRECATED
type
HumanAgentAssistantConfig_ConversationModelConfig
DEPRECATED
type
HumanAgentAssistantConfig_ConversationProcessConfig
DEPRECATED
type
HumanAgentAssistantConfig_MessageAnalysisConfig
DEPRECATED
type
HumanAgentAssistantConfig_SuggestionConfig
DEPRECATED
type
HumanAgentAssistantConfig_SuggestionFeatureConfig
DEPRECATED
type
HumanAgentAssistantConfig_SuggestionQueryConfig
DEPRECATED
type
HumanAgentAssistantConfig_SuggestionQueryConfig_ContextFilterSettings
DEPRECATED
type
HumanAgentAssistantConfig_SuggestionQueryConfig_DialogflowQuerySource
DEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_DialogflowQuerySource_ ¶
type HumanAgentAssistantConfig_SuggestionQueryConfig_DialogflowQuerySource_ = src.HumanAgentAssistantConfig_SuggestionQueryConfig_DialogflowQuerySource_
type
HumanAgentAssistantConfig_SuggestionQueryConfig_DocumentQuerySource
DEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_DocumentQuerySource_ ¶
type HumanAgentAssistantConfig_SuggestionQueryConfig_DocumentQuerySource_ = src.HumanAgentAssistantConfig_SuggestionQueryConfig_DocumentQuerySource_
type
HumanAgentAssistantConfig_SuggestionQueryConfig_KnowledgeBaseQuerySource
DEPRECATED
type HumanAgentAssistantConfig_SuggestionQueryConfig_KnowledgeBaseQuerySource_ ¶
type HumanAgentAssistantConfig_SuggestionQueryConfig_KnowledgeBaseQuerySource_ = src.HumanAgentAssistantConfig_SuggestionQueryConfig_KnowledgeBaseQuerySource_
type
HumanAgentAssistantConfig_SuggestionTriggerSettings
DEPRECATED
type
HumanAgentAssistantEvent
DEPRECATED
type
HumanAgentHandoffConfig
DEPRECATED
type
HumanAgentHandoffConfig_LivePersonConfig
DEPRECATED
type HumanAgentHandoffConfig_LivePersonConfig_ ¶
type HumanAgentHandoffConfig_LivePersonConfig_ = src.HumanAgentHandoffConfig_LivePersonConfig_
type
HumanAgentHandoffConfig_SalesforceLiveAgentConfig
DEPRECATED
type HumanAgentHandoffConfig_SalesforceLiveAgentConfig_ ¶
type HumanAgentHandoffConfig_SalesforceLiveAgentConfig_ = src.HumanAgentHandoffConfig_SalesforceLiveAgentConfig_
type
ImportAgentRequest
DEPRECATED
type ImportAgentRequest_AgentContent ¶
type ImportAgentRequest_AgentContent = src.ImportAgentRequest_AgentContent
type ImportAgentRequest_AgentUri ¶
type ImportAgentRequest_AgentUri = src.ImportAgentRequest_AgentUri
type
ImportConversationDataOperationMetadata
DEPRECATED
type
ImportConversationDataOperationResponse
DEPRECATED
type
ImportConversationDataRequest
DEPRECATED
type
ImportDocumentTemplate
DEPRECATED
type
ImportDocumentsRequest
DEPRECATED
type ImportDocumentsRequest_GcsSource ¶
type ImportDocumentsRequest_GcsSource = src.ImportDocumentsRequest_GcsSource
type
ImportDocumentsResponse
DEPRECATED
type
InputAudioConfig
DEPRECATED
type
InputConfig
DEPRECATED
type InputConfig_GcsSource ¶
type InputConfig_GcsSource = src.InputConfig_GcsSource
type
InputDataset
DEPRECATED
type
Intent
DEPRECATED
type
IntentBatch
DEPRECATED
type
IntentView
DEPRECATED
type
Intent_FollowupIntentInfo
DEPRECATED
type
Intent_Message
DEPRECATED
type
Intent_Message_BasicCard
DEPRECATED
type Intent_Message_BasicCard_ ¶
type Intent_Message_BasicCard_ = src.Intent_Message_BasicCard_
type
Intent_Message_BasicCard_Button
DEPRECATED
type
Intent_Message_BasicCard_Button_OpenUriAction
DEPRECATED
type
Intent_Message_BrowseCarouselCard
DEPRECATED
type Intent_Message_BrowseCarouselCard_ ¶
type Intent_Message_BrowseCarouselCard_ = src.Intent_Message_BrowseCarouselCard_
type
Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem
DEPRECATED
type
Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction
DEPRECATED
type
Intent_Message_BrowseCarouselCard_BrowseCarouselCardItem_OpenUrlAction_UrlTypeHint
DEPRECATED
type
Intent_Message_BrowseCarouselCard_ImageDisplayOptions
DEPRECATED
type
Intent_Message_Card
DEPRECATED
type Intent_Message_Card_ ¶
type Intent_Message_Card_ = src.Intent_Message_Card_
type
Intent_Message_Card_Button
DEPRECATED
type
Intent_Message_CarouselSelect
DEPRECATED
type Intent_Message_CarouselSelect_ ¶
type Intent_Message_CarouselSelect_ = src.Intent_Message_CarouselSelect_
type
Intent_Message_CarouselSelect_Item
DEPRECATED
type
Intent_Message_ColumnProperties
DEPRECATED
type
Intent_Message_ColumnProperties_HorizontalAlignment
DEPRECATED
type
Intent_Message_Image
DEPRECATED
type Intent_Message_Image_ ¶
type Intent_Message_Image_ = src.Intent_Message_Image_
type
Intent_Message_LinkOutSuggestion
DEPRECATED
type Intent_Message_LinkOutSuggestion_ ¶
type Intent_Message_LinkOutSuggestion_ = src.Intent_Message_LinkOutSuggestion_
type
Intent_Message_ListSelect
DEPRECATED
type Intent_Message_ListSelect_ ¶
type Intent_Message_ListSelect_ = src.Intent_Message_ListSelect_
type
Intent_Message_ListSelect_Item
DEPRECATED
type
Intent_Message_MediaContent
DEPRECATED
type Intent_Message_MediaContent_ ¶
type Intent_Message_MediaContent_ = src.Intent_Message_MediaContent_
type
Intent_Message_MediaContent_ResponseMediaObject
DEPRECATED
type Intent_Message_MediaContent_ResponseMediaObject_Icon ¶
type Intent_Message_MediaContent_ResponseMediaObject_Icon = src.Intent_Message_MediaContent_ResponseMediaObject_Icon
type Intent_Message_MediaContent_ResponseMediaObject_LargeImage ¶
type Intent_Message_MediaContent_ResponseMediaObject_LargeImage = src.Intent_Message_MediaContent_ResponseMediaObject_LargeImage
type
Intent_Message_MediaContent_ResponseMediaType
DEPRECATED
type Intent_Message_Payload ¶
type Intent_Message_Payload = src.Intent_Message_Payload
type
Intent_Message_Platform
DEPRECATED
type
Intent_Message_QuickReplies
DEPRECATED
type Intent_Message_QuickReplies_ ¶
type Intent_Message_QuickReplies_ = src.Intent_Message_QuickReplies_
type
Intent_Message_SelectItemInfo
DEPRECATED
type
Intent_Message_SimpleResponse
DEPRECATED
type
Intent_Message_SimpleResponses
DEPRECATED
type Intent_Message_SimpleResponses_ ¶
type Intent_Message_SimpleResponses_ = src.Intent_Message_SimpleResponses_
type
Intent_Message_Suggestion
DEPRECATED
type
Intent_Message_Suggestions
DEPRECATED
type Intent_Message_Suggestions_ ¶
type Intent_Message_Suggestions_ = src.Intent_Message_Suggestions_
type
Intent_Message_TableCard
DEPRECATED
type
Intent_Message_TableCardCell
DEPRECATED
type
Intent_Message_TableCardRow
DEPRECATED
type Intent_Message_TableCard_ ¶
type Intent_Message_TableCard_ = src.Intent_Message_TableCard_
type
Intent_Message_Text
DEPRECATED
type Intent_Message_Text_ ¶
type Intent_Message_Text_ = src.Intent_Message_Text_
type
Intent_Parameter
DEPRECATED
type
Intent_TrainingPhrase
DEPRECATED
type
Intent_TrainingPhrase_Part
DEPRECATED
type
Intent_TrainingPhrase_Type
DEPRECATED
type
Intent_WebhookState
DEPRECATED
type
IntentsClient
DEPRECATED
type
IntentsServer
DEPRECATED
type
KnowledgeBase
DEPRECATED
type
KnowledgeBasesClient
DEPRECATED
type
KnowledgeBasesServer
DEPRECATED
type
KnowledgeOperationMetadata
DEPRECATED
type KnowledgeOperationMetadata_ExportOperationMetadata ¶
type KnowledgeOperationMetadata_ExportOperationMetadata = src.KnowledgeOperationMetadata_ExportOperationMetadata
type
KnowledgeOperationMetadata_State
DEPRECATED
type
ListAnswerRecordsRequest
DEPRECATED
type
ListAnswerRecordsResponse
DEPRECATED
type
ListContextsRequest
DEPRECATED
type
ListContextsResponse
DEPRECATED
type
ListConversationDatasetsRequest
DEPRECATED
type
ListConversationDatasetsResponse
DEPRECATED
type
ListConversationModelEvaluationsRequest
DEPRECATED
type
ListConversationModelEvaluationsResponse
DEPRECATED
type
ListConversationModelsRequest
DEPRECATED
type
ListConversationModelsResponse
DEPRECATED
type
ListConversationProfilesRequest
DEPRECATED
type
ListConversationProfilesResponse
DEPRECATED
type
ListConversationsRequest
DEPRECATED
type
ListConversationsResponse
DEPRECATED
type
ListDocumentsRequest
DEPRECATED
type
ListDocumentsResponse
DEPRECATED
type
ListEntityTypesRequest
DEPRECATED
type
ListEntityTypesResponse
DEPRECATED
type
ListEnvironmentsRequest
DEPRECATED
type
ListEnvironmentsResponse
DEPRECATED
type
ListIntentsRequest
DEPRECATED
type
ListIntentsResponse
DEPRECATED
type
ListKnowledgeBasesRequest
DEPRECATED
type
ListKnowledgeBasesResponse
DEPRECATED
type
ListMessagesRequest
DEPRECATED
type
ListMessagesResponse
DEPRECATED
type
ListParticipantsRequest
DEPRECATED
type
ListParticipantsResponse
DEPRECATED
type
ListSessionEntityTypesRequest
DEPRECATED
type
ListSessionEntityTypesResponse
DEPRECATED
type
ListVersionsRequest
DEPRECATED
type
ListVersionsResponse
DEPRECATED
type
LoggingConfig
DEPRECATED
type
Message
DEPRECATED
type
MessageAnnotation
DEPRECATED
type
NotificationConfig
DEPRECATED
type
NotificationConfig_MessageFormat
DEPRECATED
type
OriginalDetectIntentRequest
DEPRECATED
type
OutputAudio
DEPRECATED
type
OutputAudioConfig
DEPRECATED
type
OutputAudioEncoding
DEPRECATED
type
Participant
DEPRECATED
type
Participant_Role
DEPRECATED
type
ParticipantsClient
DEPRECATED
type
ParticipantsServer
DEPRECATED
type
QueryInput
DEPRECATED
type QueryInput_AudioConfig ¶
type QueryInput_AudioConfig = src.QueryInput_AudioConfig
type QueryInput_Event ¶
type QueryInput_Event = src.QueryInput_Event
type QueryInput_Text ¶
type QueryInput_Text = src.QueryInput_Text
type
QueryParameters
DEPRECATED
type
QueryResult
DEPRECATED
type
ReloadDocumentRequest
DEPRECATED
type ReloadDocumentRequest_ContentUri ¶
type ReloadDocumentRequest_ContentUri = src.ReloadDocumentRequest_ContentUri
type
RestoreAgentRequest
DEPRECATED
type RestoreAgentRequest_AgentContent ¶
type RestoreAgentRequest_AgentContent = src.RestoreAgentRequest_AgentContent
type RestoreAgentRequest_AgentUri ¶
type RestoreAgentRequest_AgentUri = src.RestoreAgentRequest_AgentUri
type
SearchAgentsRequest
DEPRECATED
type
SearchAgentsResponse
DEPRECATED
type
Sentiment
DEPRECATED
type
SentimentAnalysisRequestConfig
DEPRECATED
type
SentimentAnalysisResult
DEPRECATED
type
SessionEntityType
DEPRECATED
type
SessionEntityType_EntityOverrideMode
DEPRECATED
type
SessionEntityTypesClient
DEPRECATED
type
SessionEntityTypesServer
DEPRECATED
type
SessionsClient
DEPRECATED
type
SessionsServer
DEPRECATED
type Sessions_StreamingDetectIntentClient ¶
type Sessions_StreamingDetectIntentClient = src.Sessions_StreamingDetectIntentClient
type Sessions_StreamingDetectIntentServer ¶
type Sessions_StreamingDetectIntentServer = src.Sessions_StreamingDetectIntentServer
type
SetAgentRequest
DEPRECATED
type
SetSuggestionFeatureConfigOperationMetadata
DEPRECATED
type
SetSuggestionFeatureConfigRequest
DEPRECATED
type
SmartReplyAnswer
DEPRECATED
type
SmartReplyMetrics
DEPRECATED
type
SmartReplyMetrics_TopNMetrics
DEPRECATED
type
SmartReplyModelMetadata
DEPRECATED
type
SpeechContext
DEPRECATED
type
SpeechModelVariant
DEPRECATED
type
SpeechToTextConfig
DEPRECATED
type
SpeechWordInfo
DEPRECATED
type
SsmlVoiceGender
DEPRECATED
type
StreamingDetectIntentRequest
DEPRECATED
type
StreamingDetectIntentResponse
DEPRECATED
type
StreamingRecognitionResult
DEPRECATED
type
StreamingRecognitionResult_MessageType
DEPRECATED
type
SuggestArticlesRequest
DEPRECATED
type
SuggestArticlesResponse
DEPRECATED
type
SuggestFaqAnswersRequest
DEPRECATED
type
SuggestFaqAnswersResponse
DEPRECATED
type
SuggestSmartRepliesRequest
DEPRECATED
type
SuggestSmartRepliesResponse
DEPRECATED
type
SuggestionFeature
DEPRECATED
type
SuggestionFeature_Type
DEPRECATED
type
SuggestionResult
DEPRECATED
type SuggestionResult_Error ¶
type SuggestionResult_Error = src.SuggestionResult_Error
type SuggestionResult_SuggestArticlesResponse ¶
type SuggestionResult_SuggestArticlesResponse = src.SuggestionResult_SuggestArticlesResponse
type SuggestionResult_SuggestFaqAnswersResponse ¶
type SuggestionResult_SuggestFaqAnswersResponse = src.SuggestionResult_SuggestFaqAnswersResponse
type SuggestionResult_SuggestSmartRepliesResponse ¶
type SuggestionResult_SuggestSmartRepliesResponse = src.SuggestionResult_SuggestSmartRepliesResponse
type
SynthesizeSpeechConfig
DEPRECATED
type
TextInput
DEPRECATED
type
TextToSpeechSettings
DEPRECATED
type
TrainAgentRequest
DEPRECATED
type
UndeployConversationModelOperationMetadata
DEPRECATED
type
UndeployConversationModelRequest
DEPRECATED
type
UnimplementedAgentsServer
DEPRECATED
type
UnimplementedAnswerRecordsServer
DEPRECATED
type
UnimplementedContextsServer
DEPRECATED
type
UnimplementedConversationDatasetsServer
DEPRECATED
type
UnimplementedConversationModelsServer
DEPRECATED
type
UnimplementedConversationProfilesServer
DEPRECATED
type
UnimplementedConversationsServer
DEPRECATED
type
UnimplementedDocumentsServer
DEPRECATED
type
UnimplementedEntityTypesServer
DEPRECATED
type
UnimplementedEnvironmentsServer
DEPRECATED
type
UnimplementedFulfillmentsServer
DEPRECATED
type
UnimplementedIntentsServer
DEPRECATED
type
UnimplementedKnowledgeBasesServer
DEPRECATED
type
UnimplementedParticipantsServer
DEPRECATED
type
UnimplementedSessionEntityTypesServer
DEPRECATED
type
UnimplementedSessionsServer
DEPRECATED
type
UnimplementedVersionsServer
DEPRECATED
type
UpdateAnswerRecordRequest
DEPRECATED
type
UpdateContextRequest
DEPRECATED
type
UpdateConversationProfileRequest
DEPRECATED
type
UpdateDocumentRequest
DEPRECATED
type
UpdateEntityTypeRequest
DEPRECATED
type
UpdateEnvironmentRequest
DEPRECATED
type
UpdateFulfillmentRequest
DEPRECATED
type
UpdateIntentRequest
DEPRECATED
type
UpdateKnowledgeBaseRequest
DEPRECATED
type
UpdateParticipantRequest
DEPRECATED
type
UpdateSessionEntityTypeRequest
DEPRECATED
type
UpdateVersionRequest
DEPRECATED
type
ValidationError
DEPRECATED
type
ValidationError_Severity
DEPRECATED
type
ValidationResult
DEPRECATED
type
Version
DEPRECATED
type
Version_VersionStatus
DEPRECATED
type
VersionsClient
DEPRECATED
type
VersionsServer
DEPRECATED
type
VoiceSelectionParams
DEPRECATED
type
WebhookRequest
DEPRECATED
type
WebhookResponse
DEPRECATED
 Source Files ¶
View all Source files
alias.go
Why Go
Use Cases
Case Studies
Get Started
Playground
Tour
Stack Overflow
Help
Packages
Standard Library
Sub-repositories
About Go Packages
About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct
Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly
Copyright
Terms of Service
Privacy Policy
Report an Issue

Theme Toggle

Shortcuts Modal
