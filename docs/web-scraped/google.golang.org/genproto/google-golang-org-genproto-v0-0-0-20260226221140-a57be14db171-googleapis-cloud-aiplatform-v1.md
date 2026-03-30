# Source: https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/aiplatform/v1

Title: aiplatform package - google.golang.org/genproto/googleapis/cloud/aiplatform/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/aiplatform/v1

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
 
aiplatform
 
v1
aiplatform
package
Version: v0.0.0-...-a57be14 Latest 
Published: Feb 26, 2026 
License: Apache-2.0 
Imports: 2 
Imported by: 2
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
Overview
Index
Constants
Variables
Functions
Types
Source Files
Directories
 Documentation ¶
Overview ¶

Package aiplatform aliases all exported identifiers in package "cloud.google.com/go/aiplatform/apiv1/aiplatformpb".

Deprecated: Please use types in: cloud.google.com/go/aiplatform/apiv1/aiplatformpb. Please read https://github.com/googleapis/google-cloud-go/blob/main/migration.md for more details.

Index ¶
Constants
Variables
func RegisterDatasetServiceServer(s *grpc.Server, srv DatasetServiceServer)DEPRECATED
func RegisterEndpointServiceServer(s *grpc.Server, srv EndpointServiceServer)DEPRECATED
func RegisterFeaturestoreOnlineServingServiceServer(s *grpc.Server, srv FeaturestoreOnlineServingServiceServer)DEPRECATED
func RegisterFeaturestoreServiceServer(s *grpc.Server, srv FeaturestoreServiceServer)DEPRECATED
func RegisterIndexEndpointServiceServer(s *grpc.Server, srv IndexEndpointServiceServer)DEPRECATED
func RegisterIndexServiceServer(s *grpc.Server, srv IndexServiceServer)DEPRECATED
func RegisterJobServiceServer(s *grpc.Server, srv JobServiceServer)DEPRECATED
func RegisterMetadataServiceServer(s *grpc.Server, srv MetadataServiceServer)DEPRECATED
func RegisterMigrationServiceServer(s *grpc.Server, srv MigrationServiceServer)DEPRECATED
func RegisterModelServiceServer(s *grpc.Server, srv ModelServiceServer)DEPRECATED
func RegisterPipelineServiceServer(s *grpc.Server, srv PipelineServiceServer)DEPRECATED
func RegisterPredictionServiceServer(s *grpc.Server, srv PredictionServiceServer)DEPRECATED
func RegisterSpecialistPoolServiceServer(s *grpc.Server, srv SpecialistPoolServiceServer)DEPRECATED
func RegisterTensorboardServiceServer(s *grpc.Server, srv TensorboardServiceServer)DEPRECATED
func RegisterVizierServiceServer(s *grpc.Server, srv VizierServiceServer)DEPRECATED
type AcceleratorTypeDEPRECATED
type ActiveLearningConfigDEPRECATED
type ActiveLearningConfig_MaxDataItemCount
type ActiveLearningConfig_MaxDataItemPercentage
type AddContextArtifactsAndExecutionsRequestDEPRECATED
type AddContextArtifactsAndExecutionsResponseDEPRECATED
type AddContextChildrenRequestDEPRECATED
type AddContextChildrenResponseDEPRECATED
type AddExecutionEventsRequestDEPRECATED
type AddExecutionEventsResponseDEPRECATED
type AddTrialMeasurementRequestDEPRECATED
type AnnotationDEPRECATED
type AnnotationSpecDEPRECATED
type ArtifactDEPRECATED
type Artifact_StateDEPRECATED
type AttributionDEPRECATED
type AutomaticResourcesDEPRECATED
type AutoscalingMetricSpecDEPRECATED
type AvroSourceDEPRECATED
type BatchCreateFeaturesOperationMetadataDEPRECATED
type BatchCreateFeaturesRequestDEPRECATED
type BatchCreateFeaturesResponseDEPRECATED
type BatchCreateTensorboardRunsRequestDEPRECATED
type BatchCreateTensorboardRunsResponseDEPRECATED
type BatchCreateTensorboardTimeSeriesRequestDEPRECATED
type BatchCreateTensorboardTimeSeriesResponseDEPRECATED
type BatchDedicatedResourcesDEPRECATED
type BatchImportModelEvaluationSlicesRequestDEPRECATED
type BatchImportModelEvaluationSlicesResponseDEPRECATED
type BatchMigrateResourcesOperationMetadataDEPRECATED
type BatchMigrateResourcesOperationMetadata_PartialResultDEPRECATED
type BatchMigrateResourcesOperationMetadata_PartialResult_Dataset
type BatchMigrateResourcesOperationMetadata_PartialResult_Error
type BatchMigrateResourcesOperationMetadata_PartialResult_Model
type BatchMigrateResourcesRequestDEPRECATED
type BatchMigrateResourcesResponseDEPRECATED
type BatchPredictionJobDEPRECATED
type BatchPredictionJob_InputConfigDEPRECATED
type BatchPredictionJob_InputConfig_BigquerySource
type BatchPredictionJob_InputConfig_GcsSource
type BatchPredictionJob_OutputConfigDEPRECATED
type BatchPredictionJob_OutputConfig_BigqueryDestination
type BatchPredictionJob_OutputConfig_GcsDestination
type BatchPredictionJob_OutputInfoDEPRECATED
type BatchPredictionJob_OutputInfo_BigqueryOutputDataset
type BatchPredictionJob_OutputInfo_GcsOutputDirectory
type BatchReadFeatureValuesOperationMetadataDEPRECATED
type BatchReadFeatureValuesRequestDEPRECATED
type BatchReadFeatureValuesRequest_BigqueryReadInstances
type BatchReadFeatureValuesRequest_CsvReadInstances
type BatchReadFeatureValuesRequest_EntityTypeSpecDEPRECATED
type BatchReadFeatureValuesRequest_PassThroughFieldDEPRECATED
type BatchReadFeatureValuesResponseDEPRECATED
type BatchReadTensorboardTimeSeriesDataRequestDEPRECATED
type BatchReadTensorboardTimeSeriesDataResponseDEPRECATED
type BigQueryDestinationDEPRECATED
type BigQuerySourceDEPRECATED
type BlurBaselineConfigDEPRECATED
type BoolArrayDEPRECATED
type CancelBatchPredictionJobRequestDEPRECATED
type CancelCustomJobRequestDEPRECATED
type CancelDataLabelingJobRequestDEPRECATED
type CancelHyperparameterTuningJobRequestDEPRECATED
type CancelPipelineJobRequestDEPRECATED
type CancelTrainingPipelineRequestDEPRECATED
type CheckTrialEarlyStoppingStateMetatdataDEPRECATED
type CheckTrialEarlyStoppingStateRequestDEPRECATED
type CheckTrialEarlyStoppingStateResponseDEPRECATED
type CompleteTrialRequestDEPRECATED
type CompletionStatsDEPRECATED
type ContainerRegistryDestinationDEPRECATED
type ContainerSpecDEPRECATED
type ContextDEPRECATED
type CreateArtifactRequestDEPRECATED
type CreateBatchPredictionJobRequestDEPRECATED
type CreateContextRequestDEPRECATED
type CreateCustomJobRequestDEPRECATED
type CreateDataLabelingJobRequestDEPRECATED
type CreateDatasetOperationMetadataDEPRECATED
type CreateDatasetRequestDEPRECATED
type CreateEndpointOperationMetadataDEPRECATED
type CreateEndpointRequestDEPRECATED
type CreateEntityTypeOperationMetadataDEPRECATED
type CreateEntityTypeRequestDEPRECATED
type CreateExecutionRequestDEPRECATED
type CreateFeatureOperationMetadataDEPRECATED
type CreateFeatureRequestDEPRECATED
type CreateFeaturestoreOperationMetadataDEPRECATED
type CreateFeaturestoreRequestDEPRECATED
type CreateHyperparameterTuningJobRequestDEPRECATED
type CreateIndexEndpointOperationMetadataDEPRECATED
type CreateIndexEndpointRequestDEPRECATED
type CreateIndexOperationMetadataDEPRECATED
type CreateIndexRequestDEPRECATED
type CreateMetadataSchemaRequestDEPRECATED
type CreateMetadataStoreOperationMetadataDEPRECATED
type CreateMetadataStoreRequestDEPRECATED
type CreateModelDeploymentMonitoringJobRequestDEPRECATED
type CreatePipelineJobRequestDEPRECATED
type CreateSpecialistPoolOperationMetadataDEPRECATED
type CreateSpecialistPoolRequestDEPRECATED
type CreateStudyRequestDEPRECATED
type CreateTensorboardExperimentRequestDEPRECATED
type CreateTensorboardOperationMetadataDEPRECATED
type CreateTensorboardRequestDEPRECATED
type CreateTensorboardRunRequestDEPRECATED
type CreateTensorboardTimeSeriesRequestDEPRECATED
type CreateTrainingPipelineRequestDEPRECATED
type CreateTrialRequestDEPRECATED
type CsvDestinationDEPRECATED
type CsvSourceDEPRECATED
type CustomJobDEPRECATED
type CustomJobSpecDEPRECATED
type DataItemDEPRECATED
type DataLabelingJobDEPRECATED
type DatasetDEPRECATED
type DatasetServiceClientDEPRECATED
func NewDatasetServiceClient(cc grpc.ClientConnInterface) DatasetServiceClientDEPRECATED
type DatasetServiceServerDEPRECATED
type DedicatedResourcesDEPRECATED
type DeleteArtifactRequestDEPRECATED
type DeleteBatchPredictionJobRequestDEPRECATED
type DeleteContextRequestDEPRECATED
type DeleteCustomJobRequestDEPRECATED
type DeleteDataLabelingJobRequestDEPRECATED
type DeleteDatasetRequestDEPRECATED
type DeleteEndpointRequestDEPRECATED
type DeleteEntityTypeRequestDEPRECATED
type DeleteExecutionRequestDEPRECATED
type DeleteFeatureRequestDEPRECATED
type DeleteFeaturestoreRequestDEPRECATED
type DeleteHyperparameterTuningJobRequestDEPRECATED
type DeleteIndexEndpointRequestDEPRECATED
type DeleteIndexRequestDEPRECATED
type DeleteMetadataStoreOperationMetadataDEPRECATED
type DeleteMetadataStoreRequestDEPRECATED
type DeleteModelDeploymentMonitoringJobRequestDEPRECATED
type DeleteModelRequestDEPRECATED
type DeleteModelVersionRequestDEPRECATED
type DeleteOperationMetadataDEPRECATED
type DeletePipelineJobRequestDEPRECATED
type DeleteSpecialistPoolRequestDEPRECATED
type DeleteStudyRequestDEPRECATED
type DeleteTensorboardExperimentRequestDEPRECATED
type DeleteTensorboardRequestDEPRECATED
type DeleteTensorboardRunRequestDEPRECATED
type DeleteTensorboardTimeSeriesRequestDEPRECATED
type DeleteTrainingPipelineRequestDEPRECATED
type DeleteTrialRequestDEPRECATED
type DeployIndexOperationMetadataDEPRECATED
type DeployIndexRequestDEPRECATED
type DeployIndexResponseDEPRECATED
type DeployModelOperationMetadataDEPRECATED
type DeployModelRequestDEPRECATED
type DeployModelResponseDEPRECATED
type DeployedIndexDEPRECATED
type DeployedIndexAuthConfigDEPRECATED
type DeployedIndexAuthConfig_AuthProviderDEPRECATED
type DeployedIndexRefDEPRECATED
type DeployedModelDEPRECATED
type DeployedModelRefDEPRECATED
type DeployedModel_AutomaticResources
type DeployedModel_DedicatedResources
type DestinationFeatureSetting
type DiskSpecDEPRECATED
type DoubleArrayDEPRECATED
type EncryptionSpecDEPRECATED
type EndpointDEPRECATED
type EndpointServiceClientDEPRECATED
func NewEndpointServiceClient(cc grpc.ClientConnInterface) EndpointServiceClientDEPRECATED
type EndpointServiceServerDEPRECATED
type EntityTypeDEPRECATED
type EnvVarDEPRECATED
type EventDEPRECATED
type Event_TypeDEPRECATED
type ExamplesOverrideDEPRECATED
type ExamplesOverride_DataFormatDEPRECATED
type ExamplesRestrictionsNamespaceDEPRECATED
type ExecutionDEPRECATED
type Execution_StateDEPRECATED
type ExplainRequestDEPRECATED
type ExplainResponseDEPRECATED
type ExplanationDEPRECATED
type ExplanationMetadataDEPRECATED
type ExplanationMetadataOverrideDEPRECATED
type ExplanationMetadataOverride_InputMetadataOverrideDEPRECATED
type ExplanationMetadata_InputMetadataDEPRECATED
type ExplanationMetadata_InputMetadata_EncodingDEPRECATED
type ExplanationMetadata_InputMetadata_FeatureValueDomainDEPRECATED
type ExplanationMetadata_InputMetadata_VisualizationDEPRECATED
type ExplanationMetadata_InputMetadata_Visualization_ColorMapDEPRECATED
type ExplanationMetadata_InputMetadata_Visualization_OverlayTypeDEPRECATED
type ExplanationMetadata_InputMetadata_Visualization_PolarityDEPRECATED
type ExplanationMetadata_InputMetadata_Visualization_TypeDEPRECATED
type ExplanationMetadata_OutputMetadataDEPRECATED
type ExplanationMetadata_OutputMetadata_DisplayNameMappingKey
type ExplanationMetadata_OutputMetadata_IndexDisplayNameMapping
type ExplanationParametersDEPRECATED
type ExplanationParameters_IntegratedGradientsAttribution
type ExplanationParameters_SampledShapleyAttribution
type ExplanationParameters_XraiAttribution
type ExplanationSpecDEPRECATED
type ExplanationSpecOverrideDEPRECATED
type ExportDataConfigDEPRECATED
type ExportDataConfig_GcsDestination
type ExportDataOperationMetadataDEPRECATED
type ExportDataRequestDEPRECATED
type ExportDataResponseDEPRECATED
type ExportFeatureValuesOperationMetadataDEPRECATED
type ExportFeatureValuesRequestDEPRECATED
type ExportFeatureValuesRequest_FullExportDEPRECATED
type ExportFeatureValuesRequest_FullExport_
type ExportFeatureValuesRequest_SnapshotExportDEPRECATED
type ExportFeatureValuesRequest_SnapshotExport_
type ExportFeatureValuesResponseDEPRECATED
type ExportModelOperationMetadataDEPRECATED
type ExportModelOperationMetadata_OutputInfoDEPRECATED
type ExportModelRequestDEPRECATED
type ExportModelRequest_OutputConfigDEPRECATED
type ExportModelResponseDEPRECATED
type ExportTensorboardTimeSeriesDataRequestDEPRECATED
type ExportTensorboardTimeSeriesDataResponseDEPRECATED
type FeatureDEPRECATED
type FeatureNoiseSigmaDEPRECATED
type FeatureNoiseSigma_NoiseSigmaForFeatureDEPRECATED
type FeatureSelectorDEPRECATED
type FeatureStatsAnomalyDEPRECATED
type FeatureValueDEPRECATED
type FeatureValueDestinationDEPRECATED
type FeatureValueDestination_BigqueryDestination
type FeatureValueDestination_CsvDestination
type FeatureValueDestination_TfrecordDestination
type FeatureValueListDEPRECATED
type FeatureValue_BoolArrayValue
type FeatureValue_BoolValue
type FeatureValue_BytesValue
type FeatureValue_DoubleArrayValue
type FeatureValue_DoubleValue
type FeatureValue_Int64ArrayValue
type FeatureValue_Int64Value
type FeatureValue_MetadataDEPRECATED
type FeatureValue_StringArrayValue
type FeatureValue_StringValue
type Feature_MonitoringStatsAnomalyDEPRECATED
type Feature_MonitoringStatsAnomaly_ObjectiveDEPRECATED
type Feature_ValueTypeDEPRECATED
type FeaturestoreDEPRECATED
type FeaturestoreMonitoringConfigDEPRECATED
type FeaturestoreMonitoringConfig_ImportFeaturesAnalysisDEPRECATED
type FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_BaselineDEPRECATED
type FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_StateDEPRECATED
type FeaturestoreMonitoringConfig_SnapshotAnalysisDEPRECATED
type FeaturestoreMonitoringConfig_ThresholdConfigDEPRECATED
type FeaturestoreMonitoringConfig_ThresholdConfig_Value
type FeaturestoreOnlineServingServiceClientDEPRECATED
func NewFeaturestoreOnlineServingServiceClient(cc grpc.ClientConnInterface) FeaturestoreOnlineServingServiceClientDEPRECATED
type FeaturestoreOnlineServingServiceServerDEPRECATED
type FeaturestoreOnlineServingService_StreamingReadFeatureValuesClient
type FeaturestoreOnlineServingService_StreamingReadFeatureValuesServer
type FeaturestoreServiceClientDEPRECATED
func NewFeaturestoreServiceClient(cc grpc.ClientConnInterface) FeaturestoreServiceClientDEPRECATED
type FeaturestoreServiceServerDEPRECATED
type Featurestore_OnlineServingConfigDEPRECATED
type Featurestore_OnlineServingConfig_ScalingDEPRECATED
type Featurestore_StateDEPRECATED
type FilterSplitDEPRECATED
type FractionSplitDEPRECATED
type GcsDestinationDEPRECATED
type GcsSourceDEPRECATED
type GenericOperationMetadataDEPRECATED
type GetAnnotationSpecRequestDEPRECATED
type GetArtifactRequestDEPRECATED
type GetBatchPredictionJobRequestDEPRECATED
type GetContextRequestDEPRECATED
type GetCustomJobRequestDEPRECATED
type GetDataLabelingJobRequestDEPRECATED
type GetDatasetRequestDEPRECATED
type GetEndpointRequestDEPRECATED
type GetEntityTypeRequestDEPRECATED
type GetExecutionRequestDEPRECATED
type GetFeatureRequestDEPRECATED
type GetFeaturestoreRequestDEPRECATED
type GetHyperparameterTuningJobRequestDEPRECATED
type GetIndexEndpointRequestDEPRECATED
type GetIndexRequestDEPRECATED
type GetMetadataSchemaRequestDEPRECATED
type GetMetadataStoreRequestDEPRECATED
type GetModelDeploymentMonitoringJobRequestDEPRECATED
type GetModelEvaluationRequestDEPRECATED
type GetModelEvaluationSliceRequestDEPRECATED
type GetModelRequestDEPRECATED
type GetPipelineJobRequestDEPRECATED
type GetSpecialistPoolRequestDEPRECATED
type GetStudyRequestDEPRECATED
type GetTensorboardExperimentRequestDEPRECATED
type GetTensorboardRequestDEPRECATED
type GetTensorboardRunRequestDEPRECATED
type GetTensorboardTimeSeriesRequestDEPRECATED
type GetTrainingPipelineRequestDEPRECATED
type GetTrialRequestDEPRECATED
type HyperparameterTuningJobDEPRECATED
type IdMatcherDEPRECATED
type ImportDataConfigDEPRECATED
type ImportDataConfig_GcsSource
type ImportDataOperationMetadataDEPRECATED
type ImportDataRequestDEPRECATED
type ImportDataResponseDEPRECATED
type ImportFeatureValuesOperationMetadataDEPRECATED
type ImportFeatureValuesRequestDEPRECATED
type ImportFeatureValuesRequest_AvroSource
type ImportFeatureValuesRequest_BigquerySource
type ImportFeatureValuesRequest_CsvSource
type ImportFeatureValuesRequest_FeatureSpecDEPRECATED
type ImportFeatureValuesRequest_FeatureTime
type ImportFeatureValuesRequest_FeatureTimeField
type ImportFeatureValuesResponseDEPRECATED
type ImportModelEvaluationRequestDEPRECATED
type IndexDEPRECATED
type IndexDatapointDEPRECATED
type IndexDatapoint_CrowdingTagDEPRECATED
type IndexDatapoint_RestrictionDEPRECATED
type IndexEndpointDEPRECATED
type IndexEndpointServiceClientDEPRECATED
func NewIndexEndpointServiceClient(cc grpc.ClientConnInterface) IndexEndpointServiceClientDEPRECATED
type IndexEndpointServiceServerDEPRECATED
type IndexPrivateEndpointsDEPRECATED
type IndexServiceClientDEPRECATED
func NewIndexServiceClient(cc grpc.ClientConnInterface) IndexServiceClientDEPRECATED
type IndexServiceServerDEPRECATED
type IndexStatsDEPRECATED
type Index_IndexUpdateMethodDEPRECATED
type InputDataConfigDEPRECATED
type InputDataConfig_BigqueryDestination
type InputDataConfig_FilterSplit
type InputDataConfig_FractionSplit
type InputDataConfig_GcsDestination
type InputDataConfig_PredefinedSplit
type InputDataConfig_StratifiedSplit
type InputDataConfig_TimestampSplit
type Int64ArrayDEPRECATED
type IntegratedGradientsAttributionDEPRECATED
type JobServiceClientDEPRECATED
func NewJobServiceClient(cc grpc.ClientConnInterface) JobServiceClientDEPRECATED
type JobServiceServerDEPRECATED
type JobStateDEPRECATED
type LineageSubgraphDEPRECATED
type ListAnnotationsRequestDEPRECATED
type ListAnnotationsResponseDEPRECATED
type ListArtifactsRequestDEPRECATED
type ListArtifactsResponseDEPRECATED
type ListBatchPredictionJobsRequestDEPRECATED
type ListBatchPredictionJobsResponseDEPRECATED
type ListContextsRequestDEPRECATED
type ListContextsResponseDEPRECATED
type ListCustomJobsRequestDEPRECATED
type ListCustomJobsResponseDEPRECATED
type ListDataItemsRequestDEPRECATED
type ListDataItemsResponseDEPRECATED
type ListDataLabelingJobsRequestDEPRECATED
type ListDataLabelingJobsResponseDEPRECATED
type ListDatasetsRequestDEPRECATED
type ListDatasetsResponseDEPRECATED
type ListEndpointsRequestDEPRECATED
type ListEndpointsResponseDEPRECATED
type ListEntityTypesRequestDEPRECATED
type ListEntityTypesResponseDEPRECATED
type ListExecutionsRequestDEPRECATED
type ListExecutionsResponseDEPRECATED
type ListFeaturesRequestDEPRECATED
type ListFeaturesResponseDEPRECATED
type ListFeaturestoresRequestDEPRECATED
type ListFeaturestoresResponseDEPRECATED
type ListHyperparameterTuningJobsRequestDEPRECATED
type ListHyperparameterTuningJobsResponseDEPRECATED
type ListIndexEndpointsRequestDEPRECATED
type ListIndexEndpointsResponseDEPRECATED
type ListIndexesRequestDEPRECATED
type ListIndexesResponseDEPRECATED
type ListMetadataSchemasRequestDEPRECATED
type ListMetadataSchemasResponseDEPRECATED
type ListMetadataStoresRequestDEPRECATED
type ListMetadataStoresResponseDEPRECATED
type ListModelDeploymentMonitoringJobsRequestDEPRECATED
type ListModelDeploymentMonitoringJobsResponseDEPRECATED
type ListModelEvaluationSlicesRequestDEPRECATED
type ListModelEvaluationSlicesResponseDEPRECATED
type ListModelEvaluationsRequestDEPRECATED
type ListModelEvaluationsResponseDEPRECATED
type ListModelVersionsRequestDEPRECATED
type ListModelVersionsResponseDEPRECATED
type ListModelsRequestDEPRECATED
type ListModelsResponseDEPRECATED
type ListOptimalTrialsRequestDEPRECATED
type ListOptimalTrialsResponseDEPRECATED
type ListPipelineJobsRequestDEPRECATED
type ListPipelineJobsResponseDEPRECATED
type ListSavedQueriesRequestDEPRECATED
type ListSavedQueriesResponseDEPRECATED
type ListSpecialistPoolsRequestDEPRECATED
type ListSpecialistPoolsResponseDEPRECATED
type ListStudiesRequestDEPRECATED
type ListStudiesResponseDEPRECATED
type ListTensorboardExperimentsRequestDEPRECATED
type ListTensorboardExperimentsResponseDEPRECATED
type ListTensorboardRunsRequestDEPRECATED
type ListTensorboardRunsResponseDEPRECATED
type ListTensorboardTimeSeriesRequestDEPRECATED
type ListTensorboardTimeSeriesResponseDEPRECATED
type ListTensorboardsRequestDEPRECATED
type ListTensorboardsResponseDEPRECATED
type ListTrainingPipelinesRequestDEPRECATED
type ListTrainingPipelinesResponseDEPRECATED
type ListTrialsRequestDEPRECATED
type ListTrialsResponseDEPRECATED
type LookupStudyRequestDEPRECATED
type MachineSpecDEPRECATED
type ManualBatchTuningParametersDEPRECATED
type MeasurementDEPRECATED
type Measurement_MetricDEPRECATED
type MergeVersionAliasesRequestDEPRECATED
type MetadataSchemaDEPRECATED
type MetadataSchema_MetadataSchemaTypeDEPRECATED
type MetadataServiceClientDEPRECATED
func NewMetadataServiceClient(cc grpc.ClientConnInterface) MetadataServiceClientDEPRECATED
type MetadataServiceServerDEPRECATED
type MetadataStoreDEPRECATED
type MetadataStore_MetadataStoreStateDEPRECATED
type MigratableResourceDEPRECATED
type MigratableResource_AutomlDatasetDEPRECATED
type MigratableResource_AutomlDataset_
type MigratableResource_AutomlModelDEPRECATED
type MigratableResource_AutomlModel_
type MigratableResource_DataLabelingDatasetDEPRECATED
type MigratableResource_DataLabelingDataset_
type MigratableResource_DataLabelingDataset_DataLabelingAnnotatedDatasetDEPRECATED
type MigratableResource_MlEngineModelVersionDEPRECATED
type MigratableResource_MlEngineModelVersion_
type MigrateResourceRequestDEPRECATED
type MigrateResourceRequest_MigrateAutomlDatasetConfigDEPRECATED
type MigrateResourceRequest_MigrateAutomlDatasetConfig_
type MigrateResourceRequest_MigrateAutomlModelConfigDEPRECATED
type MigrateResourceRequest_MigrateAutomlModelConfig_
type MigrateResourceRequest_MigrateDataLabelingDatasetConfigDEPRECATED
type MigrateResourceRequest_MigrateDataLabelingDatasetConfig_
type MigrateResourceRequest_MigrateDataLabelingDatasetConfig_MigrateDataLabelingAnnotatedDatasetConfigDEPRECATED
type MigrateResourceRequest_MigrateMlEngineModelVersionConfigDEPRECATED
type MigrateResourceRequest_MigrateMlEngineModelVersionConfig_
type MigrateResourceResponseDEPRECATED
type MigrateResourceResponse_Dataset
type MigrateResourceResponse_Model
type MigrationServiceClientDEPRECATED
func NewMigrationServiceClient(cc grpc.ClientConnInterface) MigrationServiceClientDEPRECATED
type MigrationServiceServerDEPRECATED
type ModelDEPRECATED
type ModelContainerSpecDEPRECATED
type ModelDeploymentMonitoringBigQueryTableDEPRECATED
type ModelDeploymentMonitoringBigQueryTable_LogSourceDEPRECATED
type ModelDeploymentMonitoringBigQueryTable_LogTypeDEPRECATED
type ModelDeploymentMonitoringJobDEPRECATED
type ModelDeploymentMonitoringJob_LatestMonitoringPipelineMetadataDEPRECATED
type ModelDeploymentMonitoringJob_MonitoringScheduleStateDEPRECATED
type ModelDeploymentMonitoringObjectiveConfigDEPRECATED
type ModelDeploymentMonitoringObjectiveTypeDEPRECATED
type ModelDeploymentMonitoringScheduleConfigDEPRECATED
type ModelEvaluationDEPRECATED
type ModelEvaluationSliceDEPRECATED
type ModelEvaluationSlice_SliceDEPRECATED
type ModelEvaluation_ModelEvaluationExplanationSpec
type ModelExplanationDEPRECATED
type ModelMonitoringAlertConfig
type ModelMonitoringAlertConfig_EmailAlertConfigDEPRECATED
type ModelMonitoringAlertConfig_EmailAlertConfig_
type ModelMonitoringObjectiveConfigDEPRECATED
type ModelMonitoringObjectiveConfig_ExplanationConfigDEPRECATED
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaselineDEPRECATED
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Bigquery
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Gcs
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PredictionFormatDEPRECATED
type ModelMonitoringObjectiveConfig_PredictionDriftDetectionConfigDEPRECATED
type ModelMonitoringObjectiveConfig_TrainingDatasetDEPRECATED
type ModelMonitoringObjectiveConfig_TrainingDataset_BigquerySource
type ModelMonitoringObjectiveConfig_TrainingDataset_Dataset
type ModelMonitoringObjectiveConfig_TrainingDataset_GcsSource
type ModelMonitoringObjectiveConfig_TrainingPredictionSkewDetectionConfigDEPRECATED
type ModelMonitoringStatsAnomaliesDEPRECATED
type ModelMonitoringStatsAnomalies_FeatureHistoricStatsAnomaliesDEPRECATED
type ModelServiceClientDEPRECATED
func NewModelServiceClient(cc grpc.ClientConnInterface) ModelServiceClientDEPRECATED
type ModelServiceServerDEPRECATED
type ModelSourceInfoDEPRECATED
type ModelSourceInfo_ModelSourceTypeDEPRECATED
type Model_DeploymentResourcesTypeDEPRECATED
type Model_ExportFormatDEPRECATED
type Model_ExportFormat_ExportableContentDEPRECATED
type MutateDeployedIndexOperationMetadataDEPRECATED
type MutateDeployedIndexRequestDEPRECATED
type MutateDeployedIndexResponseDEPRECATED
type NearestNeighborSearchOperationMetadataDEPRECATED
type NearestNeighborSearchOperationMetadata_ContentValidationStats
type NearestNeighborSearchOperationMetadata_RecordError
type NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType
type NeighborDEPRECATED
type NfsMountDEPRECATED
type PauseModelDeploymentMonitoringJobRequestDEPRECATED
type PipelineFailurePolicyDEPRECATED
type PipelineJobDEPRECATED
type PipelineJobDetailDEPRECATED
type PipelineJob_RuntimeConfigDEPRECATED
type PipelineJob_RuntimeConfig_InputArtifactDEPRECATED
type PipelineJob_RuntimeConfig_InputArtifact_ArtifactId
type PipelineServiceClientDEPRECATED
func NewPipelineServiceClient(cc grpc.ClientConnInterface) PipelineServiceClientDEPRECATED
type PipelineServiceServerDEPRECATED
type PipelineStateDEPRECATED
type PipelineTaskDetailDEPRECATED
type PipelineTaskDetail_ArtifactListDEPRECATED
type PipelineTaskDetail_PipelineTaskStatusDEPRECATED
type PipelineTaskDetail_StateDEPRECATED
type PipelineTaskExecutorDetailDEPRECATED
type PipelineTaskExecutorDetail_ContainerDetailDEPRECATED
type PipelineTaskExecutorDetail_ContainerDetail_
type PipelineTaskExecutorDetail_CustomJobDetailDEPRECATED
type PipelineTaskExecutorDetail_CustomJobDetail_
type PipelineTemplateMetadataDEPRECATED
type PortDEPRECATED
type PredefinedSplitDEPRECATED
type PredictRequestDEPRECATED
type PredictRequestResponseLoggingConfigDEPRECATED
type PredictResponseDEPRECATED
type PredictSchemataDEPRECATED
type PredictionServiceClientDEPRECATED
func NewPredictionServiceClient(cc grpc.ClientConnInterface) PredictionServiceClientDEPRECATED
type PredictionServiceServerDEPRECATED
type PrivateEndpointsDEPRECATED
type PurgeArtifactsMetadataDEPRECATED
type PurgeArtifactsRequestDEPRECATED
type PurgeArtifactsResponseDEPRECATED
type PurgeContextsMetadataDEPRECATED
type PurgeContextsRequestDEPRECATED
type PurgeContextsResponseDEPRECATED
type PurgeExecutionsMetadataDEPRECATED
type PurgeExecutionsRequestDEPRECATED
type PurgeExecutionsResponseDEPRECATED
type PythonPackageSpecDEPRECATED
type QueryArtifactLineageSubgraphRequestDEPRECATED
type QueryContextLineageSubgraphRequestDEPRECATED
type QueryExecutionInputsAndOutputsRequestDEPRECATED
type RawPredictRequestDEPRECATED
type ReadFeatureValuesRequestDEPRECATED
type ReadFeatureValuesResponseDEPRECATED
type ReadFeatureValuesResponse_EntityViewDEPRECATED
type ReadFeatureValuesResponse_EntityView_DataDEPRECATED
type ReadFeatureValuesResponse_EntityView_Data_Value
type ReadFeatureValuesResponse_EntityView_Data_Values
type ReadFeatureValuesResponse_FeatureDescriptorDEPRECATED
type ReadFeatureValuesResponse_HeaderDEPRECATED
type ReadTensorboardBlobDataRequestDEPRECATED
type ReadTensorboardBlobDataResponseDEPRECATED
type ReadTensorboardTimeSeriesDataRequestDEPRECATED
type ReadTensorboardTimeSeriesDataResponseDEPRECATED
type RemoveContextChildrenRequestDEPRECATED
type RemoveContextChildrenResponseDEPRECATED
type RemoveDatapointsRequestDEPRECATED
type RemoveDatapointsResponseDEPRECATED
type ResourcesConsumedDEPRECATED
type ResumeModelDeploymentMonitoringJobRequestDEPRECATED
type SampleConfigDEPRECATED
type SampleConfig_FollowingBatchSamplePercentage
type SampleConfig_InitialBatchSamplePercentage
type SampleConfig_SampleStrategyDEPRECATED
type SampledShapleyAttributionDEPRECATED
type SamplingStrategyDEPRECATED
type SamplingStrategy_RandomSampleConfigDEPRECATED
type SavedQueryDEPRECATED
type ScalarDEPRECATED
type SchedulingDEPRECATED
type SearchFeaturesRequestDEPRECATED
type SearchFeaturesResponseDEPRECATED
type SearchMigratableResourcesRequestDEPRECATED
type SearchMigratableResourcesResponseDEPRECATED
type SearchModelDeploymentMonitoringStatsAnomaliesRequestDEPRECATED
type SearchModelDeploymentMonitoringStatsAnomaliesRequest_StatsAnomaliesObjectiveDEPRECATED
type SearchModelDeploymentMonitoringStatsAnomaliesResponseDEPRECATED
type SmoothGradConfigDEPRECATED
type SmoothGradConfig_FeatureNoiseSigma
type SmoothGradConfig_NoiseSigma
type SpecialistPoolDEPRECATED
type SpecialistPoolServiceClientDEPRECATED
func NewSpecialistPoolServiceClient(cc grpc.ClientConnInterface) SpecialistPoolServiceClientDEPRECATED
type SpecialistPoolServiceServerDEPRECATED
type StopTrialRequestDEPRECATED
type StratifiedSplitDEPRECATED
type StreamingReadFeatureValuesRequestDEPRECATED
type StringArrayDEPRECATED
type StudyDEPRECATED
type StudySpecDEPRECATED
type StudySpec_AlgorithmDEPRECATED
type StudySpec_ConvexAutomatedStoppingSpecDEPRECATED
type StudySpec_ConvexAutomatedStoppingSpec_
type StudySpec_DecayCurveAutomatedStoppingSpecDEPRECATED
type StudySpec_DecayCurveStoppingSpec
type StudySpec_MeasurementSelectionTypeDEPRECATED
type StudySpec_MedianAutomatedStoppingSpecDEPRECATED
type StudySpec_MedianAutomatedStoppingSpec_
type StudySpec_MetricSpecDEPRECATED
type StudySpec_MetricSpec_GoalTypeDEPRECATED
type StudySpec_ObservationNoiseDEPRECATED
type StudySpec_ParameterSpecDEPRECATED
type StudySpec_ParameterSpec_CategoricalValueSpecDEPRECATED
type StudySpec_ParameterSpec_CategoricalValueSpec_
type StudySpec_ParameterSpec_ConditionalParameterSpecDEPRECATED
type StudySpec_ParameterSpec_ConditionalParameterSpec_CategoricalValueConditionDEPRECATED
type StudySpec_ParameterSpec_ConditionalParameterSpec_DiscreteValueConditionDEPRECATED
type StudySpec_ParameterSpec_ConditionalParameterSpec_IntValueConditionDEPRECATED
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentCategoricalValues
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentDiscreteValues
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentIntValues
type StudySpec_ParameterSpec_DiscreteValueSpecDEPRECATED
type StudySpec_ParameterSpec_DiscreteValueSpec_
type StudySpec_ParameterSpec_DoubleValueSpecDEPRECATED
type StudySpec_ParameterSpec_DoubleValueSpec_
type StudySpec_ParameterSpec_IntegerValueSpecDEPRECATED
type StudySpec_ParameterSpec_IntegerValueSpec_
type StudySpec_ParameterSpec_ScaleTypeDEPRECATED
type Study_StateDEPRECATED
type SuggestTrialsMetadataDEPRECATED
type SuggestTrialsRequestDEPRECATED
type SuggestTrialsResponseDEPRECATED
type TFRecordDestinationDEPRECATED
type TensorboardDEPRECATED
type TensorboardBlobDEPRECATED
type TensorboardBlobSequenceDEPRECATED
type TensorboardExperimentDEPRECATED
type TensorboardRunDEPRECATED
type TensorboardServiceClientDEPRECATED
func NewTensorboardServiceClient(cc grpc.ClientConnInterface) TensorboardServiceClientDEPRECATED
type TensorboardServiceServerDEPRECATED
type TensorboardService_ReadTensorboardBlobDataClient
type TensorboardService_ReadTensorboardBlobDataServer
type TensorboardTensorDEPRECATED
type TensorboardTimeSeriesDEPRECATED
type TensorboardTimeSeries_MetadataDEPRECATED
type TensorboardTimeSeries_ValueTypeDEPRECATED
type ThresholdConfigDEPRECATED
type ThresholdConfig_Value
type TimeSeriesDataDEPRECATED
type TimeSeriesDataPointDEPRECATED
type TimeSeriesDataPoint_Blobs
type TimeSeriesDataPoint_Scalar
type TimeSeriesDataPoint_Tensor
type TimestampSplitDEPRECATED
type TrainingConfigDEPRECATED
type TrainingPipelineDEPRECATED
type TrialDEPRECATED
type Trial_ParameterDEPRECATED
type Trial_StateDEPRECATED
type UndeployIndexOperationMetadataDEPRECATED
type UndeployIndexRequestDEPRECATED
type UndeployIndexResponseDEPRECATED
type UndeployModelOperationMetadataDEPRECATED
type UndeployModelRequestDEPRECATED
type UndeployModelResponseDEPRECATED
type UnimplementedDatasetServiceServerDEPRECATED
type UnimplementedEndpointServiceServerDEPRECATED
type UnimplementedFeaturestoreOnlineServingServiceServerDEPRECATED
type UnimplementedFeaturestoreServiceServerDEPRECATED
type UnimplementedIndexEndpointServiceServerDEPRECATED
type UnimplementedIndexServiceServerDEPRECATED
type UnimplementedJobServiceServerDEPRECATED
type UnimplementedMetadataServiceServerDEPRECATED
type UnimplementedMigrationServiceServerDEPRECATED
type UnimplementedModelServiceServerDEPRECATED
type UnimplementedPipelineServiceServerDEPRECATED
type UnimplementedPredictionServiceServerDEPRECATED
type UnimplementedSpecialistPoolServiceServerDEPRECATED
type UnimplementedTensorboardServiceServerDEPRECATED
type UnimplementedVizierServiceServerDEPRECATED
type UnmanagedContainerModelDEPRECATED
type UpdateArtifactRequestDEPRECATED
type UpdateContextRequestDEPRECATED
type UpdateDatasetRequestDEPRECATED
type UpdateEndpointRequestDEPRECATED
type UpdateEntityTypeRequestDEPRECATED
type UpdateExecutionRequestDEPRECATED
type UpdateFeatureRequestDEPRECATED
type UpdateFeaturestoreOperationMetadataDEPRECATED
type UpdateFeaturestoreRequestDEPRECATED
type UpdateIndexEndpointRequestDEPRECATED
type UpdateIndexOperationMetadataDEPRECATED
type UpdateIndexRequestDEPRECATED
type UpdateModelDeploymentMonitoringJobOperationMetadataDEPRECATED
type UpdateModelDeploymentMonitoringJobRequestDEPRECATED
type UpdateModelRequestDEPRECATED
type UpdateSpecialistPoolOperationMetadataDEPRECATED
type UpdateSpecialistPoolRequestDEPRECATED
type UpdateTensorboardExperimentRequestDEPRECATED
type UpdateTensorboardOperationMetadataDEPRECATED
type UpdateTensorboardRequestDEPRECATED
type UpdateTensorboardRunRequestDEPRECATED
type UpdateTensorboardTimeSeriesRequestDEPRECATED
type UploadModelOperationMetadataDEPRECATED
type UploadModelRequestDEPRECATED
type UploadModelResponseDEPRECATED
type UpsertDatapointsRequestDEPRECATED
type UpsertDatapointsResponseDEPRECATED
type UserActionReferenceDEPRECATED
type UserActionReference_DataLabelingJob
type UserActionReference_Operation
type ValueDEPRECATED
type Value_DoubleValue
type Value_IntValue
type Value_StringValue
type VizierServiceClientDEPRECATED
func NewVizierServiceClient(cc grpc.ClientConnInterface) VizierServiceClientDEPRECATED
type VizierServiceServerDEPRECATED
type WorkerPoolSpecDEPRECATED
type WorkerPoolSpec_ContainerSpec
type WorkerPoolSpec_PythonPackageSpec
type WriteFeatureValuesPayloadDEPRECATED
type WriteFeatureValuesRequestDEPRECATED
type WriteFeatureValuesResponseDEPRECATED
type WriteTensorboardExperimentDataRequestDEPRECATED
type WriteTensorboardExperimentDataResponseDEPRECATED
type WriteTensorboardRunDataRequestDEPRECATED
type WriteTensorboardRunDataResponseDEPRECATED
type XraiAttributionDEPRECATED
Constants ¶
View Source
const (
	AcceleratorType_ACCELERATOR_TYPE_UNSPECIFIED                                                       = src.AcceleratorType_ACCELERATOR_TYPE_UNSPECIFIED
	AcceleratorType_NVIDIA_TESLA_A100                                                                  = src.AcceleratorType_NVIDIA_TESLA_A100
	AcceleratorType_NVIDIA_TESLA_K80                                                                   = src.AcceleratorType_NVIDIA_TESLA_K80
	AcceleratorType_NVIDIA_TESLA_P100                                                                  = src.AcceleratorType_NVIDIA_TESLA_P100
	AcceleratorType_NVIDIA_TESLA_P4                                                                    = src.AcceleratorType_NVIDIA_TESLA_P4
	AcceleratorType_NVIDIA_TESLA_T4                                                                    = src.AcceleratorType_NVIDIA_TESLA_T4
	AcceleratorType_NVIDIA_TESLA_V100                                                                  = src.AcceleratorType_NVIDIA_TESLA_V100
	AcceleratorType_TPU_V2                                                                             = src.AcceleratorType_TPU_V2
	AcceleratorType_TPU_V3                                                                             = src.AcceleratorType_TPU_V3
	Artifact_LIVE                                                                                      = src.Artifact_LIVE
	Artifact_PENDING                                                                                   = src.Artifact_PENDING
	Artifact_STATE_UNSPECIFIED                                                                         = src.Artifact_STATE_UNSPECIFIED
	Event_INPUT                                                                                        = src.Event_INPUT
	Event_OUTPUT                                                                                       = src.Event_OUTPUT
	Event_TYPE_UNSPECIFIED                                                                             = src.Event_TYPE_UNSPECIFIED
	ExamplesOverride_DATA_FORMAT_UNSPECIFIED                                                           = src.ExamplesOverride_DATA_FORMAT_UNSPECIFIED
	ExamplesOverride_EMBEDDINGS                                                                        = src.ExamplesOverride_EMBEDDINGS
	ExamplesOverride_INSTANCES                                                                         = src.ExamplesOverride_INSTANCES
	Execution_CACHED                                                                                   = src.Execution_CACHED
	Execution_CANCELLED                                                                                = src.Execution_CANCELLED
	Execution_COMPLETE                                                                                 = src.Execution_COMPLETE
	Execution_FAILED                                                                                   = src.Execution_FAILED
	Execution_NEW                                                                                      = src.Execution_NEW
	Execution_RUNNING                                                                                  = src.Execution_RUNNING
	Execution_STATE_UNSPECIFIED                                                                        = src.Execution_STATE_UNSPECIFIED
	ExplanationMetadata_InputMetadata_BAG_OF_FEATURES                                                  = src.ExplanationMetadata_InputMetadata_BAG_OF_FEATURES
	ExplanationMetadata_InputMetadata_BAG_OF_FEATURES_SPARSE                                           = src.ExplanationMetadata_InputMetadata_BAG_OF_FEATURES_SPARSE
	ExplanationMetadata_InputMetadata_COMBINED_EMBEDDING                                               = src.ExplanationMetadata_InputMetadata_COMBINED_EMBEDDING
	ExplanationMetadata_InputMetadata_CONCAT_EMBEDDING                                                 = src.ExplanationMetadata_InputMetadata_CONCAT_EMBEDDING
	ExplanationMetadata_InputMetadata_ENCODING_UNSPECIFIED                                             = src.ExplanationMetadata_InputMetadata_ENCODING_UNSPECIFIED
	ExplanationMetadata_InputMetadata_IDENTITY                                                         = src.ExplanationMetadata_InputMetadata_IDENTITY
	ExplanationMetadata_InputMetadata_INDICATOR                                                        = src.ExplanationMetadata_InputMetadata_INDICATOR
	ExplanationMetadata_InputMetadata_Visualization_BOTH                                               = src.ExplanationMetadata_InputMetadata_Visualization_BOTH
	ExplanationMetadata_InputMetadata_Visualization_COLOR_MAP_UNSPECIFIED                              = src.ExplanationMetadata_InputMetadata_Visualization_COLOR_MAP_UNSPECIFIED
	ExplanationMetadata_InputMetadata_Visualization_GRAYSCALE                                          = src.ExplanationMetadata_InputMetadata_Visualization_GRAYSCALE
	ExplanationMetadata_InputMetadata_Visualization_GREEN                                              = src.ExplanationMetadata_InputMetadata_Visualization_GREEN
	ExplanationMetadata_InputMetadata_Visualization_MASK_BLACK                                         = src.ExplanationMetadata_InputMetadata_Visualization_MASK_BLACK
	ExplanationMetadata_InputMetadata_Visualization_NEGATIVE                                           = src.ExplanationMetadata_InputMetadata_Visualization_NEGATIVE
	ExplanationMetadata_InputMetadata_Visualization_NONE                                               = src.ExplanationMetadata_InputMetadata_Visualization_NONE
	ExplanationMetadata_InputMetadata_Visualization_ORIGINAL                                           = src.ExplanationMetadata_InputMetadata_Visualization_ORIGINAL
	ExplanationMetadata_InputMetadata_Visualization_OUTLINES                                           = src.ExplanationMetadata_InputMetadata_Visualization_OUTLINES
	ExplanationMetadata_InputMetadata_Visualization_OVERLAY_TYPE_UNSPECIFIED                           = src.ExplanationMetadata_InputMetadata_Visualization_OVERLAY_TYPE_UNSPECIFIED
	ExplanationMetadata_InputMetadata_Visualization_PINK_GREEN                                         = src.ExplanationMetadata_InputMetadata_Visualization_PINK_GREEN
	ExplanationMetadata_InputMetadata_Visualization_PINK_WHITE_GREEN                                   = src.ExplanationMetadata_InputMetadata_Visualization_PINK_WHITE_GREEN
	ExplanationMetadata_InputMetadata_Visualization_PIXELS                                             = src.ExplanationMetadata_InputMetadata_Visualization_PIXELS
	ExplanationMetadata_InputMetadata_Visualization_POLARITY_UNSPECIFIED                               = src.ExplanationMetadata_InputMetadata_Visualization_POLARITY_UNSPECIFIED
	ExplanationMetadata_InputMetadata_Visualization_POSITIVE                                           = src.ExplanationMetadata_InputMetadata_Visualization_POSITIVE
	ExplanationMetadata_InputMetadata_Visualization_RED                                                = src.ExplanationMetadata_InputMetadata_Visualization_RED
	ExplanationMetadata_InputMetadata_Visualization_RED_GREEN                                          = src.ExplanationMetadata_InputMetadata_Visualization_RED_GREEN
	ExplanationMetadata_InputMetadata_Visualization_TYPE_UNSPECIFIED                                   = src.ExplanationMetadata_InputMetadata_Visualization_TYPE_UNSPECIFIED
	ExplanationMetadata_InputMetadata_Visualization_VIRIDIS                                            = src.ExplanationMetadata_InputMetadata_Visualization_VIRIDIS
	Feature_BOOL                                                                                       = src.Feature_BOOL
	Feature_BOOL_ARRAY                                                                                 = src.Feature_BOOL_ARRAY
	Feature_BYTES                                                                                      = src.Feature_BYTES
	Feature_DOUBLE                                                                                     = src.Feature_DOUBLE
	Feature_DOUBLE_ARRAY                                                                               = src.Feature_DOUBLE_ARRAY
	Feature_INT64                                                                                      = src.Feature_INT64
	Feature_INT64_ARRAY                                                                                = src.Feature_INT64_ARRAY
	Feature_MonitoringStatsAnomaly_IMPORT_FEATURE_ANALYSIS                                             = src.Feature_MonitoringStatsAnomaly_IMPORT_FEATURE_ANALYSIS
	Feature_MonitoringStatsAnomaly_OBJECTIVE_UNSPECIFIED                                               = src.Feature_MonitoringStatsAnomaly_OBJECTIVE_UNSPECIFIED
	Feature_MonitoringStatsAnomaly_SNAPSHOT_ANALYSIS                                                   = src.Feature_MonitoringStatsAnomaly_SNAPSHOT_ANALYSIS
	Feature_STRING                                                                                     = src.Feature_STRING
	Feature_STRING_ARRAY                                                                               = src.Feature_STRING_ARRAY
	Feature_VALUE_TYPE_UNSPECIFIED                                                                     = src.Feature_VALUE_TYPE_UNSPECIFIED
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_BASELINE_UNSPECIFIED                           = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_BASELINE_UNSPECIFIED
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_DEFAULT                                        = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_DEFAULT
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_DISABLED                                       = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_DISABLED
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_ENABLED                                        = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_ENABLED
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_LATEST_STATS                                   = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_LATEST_STATS
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_MOST_RECENT_SNAPSHOT_STATS                     = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_MOST_RECENT_SNAPSHOT_STATS
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_PREVIOUS_IMPORT_FEATURES_STATS                 = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_PREVIOUS_IMPORT_FEATURES_STATS
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_STATE_UNSPECIFIED                              = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_STATE_UNSPECIFIED
	Featurestore_STABLE                                                                                = src.Featurestore_STABLE
	Featurestore_STATE_UNSPECIFIED                                                                     = src.Featurestore_STATE_UNSPECIFIED
	Featurestore_UPDATING                                                                              = src.Featurestore_UPDATING
	Index_BATCH_UPDATE                                                                                 = src.Index_BATCH_UPDATE
	Index_INDEX_UPDATE_METHOD_UNSPECIFIED                                                              = src.Index_INDEX_UPDATE_METHOD_UNSPECIFIED
	Index_STREAM_UPDATE                                                                                = src.Index_STREAM_UPDATE
	JobState_JOB_STATE_CANCELLED                                                                       = src.JobState_JOB_STATE_CANCELLED
	JobState_JOB_STATE_CANCELLING                                                                      = src.JobState_JOB_STATE_CANCELLING
	JobState_JOB_STATE_EXPIRED                                                                         = src.JobState_JOB_STATE_EXPIRED
	JobState_JOB_STATE_FAILED                                                                          = src.JobState_JOB_STATE_FAILED
	JobState_JOB_STATE_PAUSED                                                                          = src.JobState_JOB_STATE_PAUSED
	JobState_JOB_STATE_PENDING                                                                         = src.JobState_JOB_STATE_PENDING
	JobState_JOB_STATE_QUEUED                                                                          = src.JobState_JOB_STATE_QUEUED
	JobState_JOB_STATE_RUNNING                                                                         = src.JobState_JOB_STATE_RUNNING
	JobState_JOB_STATE_SUCCEEDED                                                                       = src.JobState_JOB_STATE_SUCCEEDED
	JobState_JOB_STATE_UNSPECIFIED                                                                     = src.JobState_JOB_STATE_UNSPECIFIED
	JobState_JOB_STATE_UPDATING                                                                        = src.JobState_JOB_STATE_UPDATING
	MetadataSchema_ARTIFACT_TYPE                                                                       = src.MetadataSchema_ARTIFACT_TYPE
	MetadataSchema_CONTEXT_TYPE                                                                        = src.MetadataSchema_CONTEXT_TYPE
	MetadataSchema_EXECUTION_TYPE                                                                      = src.MetadataSchema_EXECUTION_TYPE
	MetadataSchema_METADATA_SCHEMA_TYPE_UNSPECIFIED                                                    = src.MetadataSchema_METADATA_SCHEMA_TYPE_UNSPECIFIED
	ModelDeploymentMonitoringBigQueryTable_EXPLAIN                                                     = src.ModelDeploymentMonitoringBigQueryTable_EXPLAIN
	ModelDeploymentMonitoringBigQueryTable_LOG_SOURCE_UNSPECIFIED                                      = src.ModelDeploymentMonitoringBigQueryTable_LOG_SOURCE_UNSPECIFIED
	ModelDeploymentMonitoringBigQueryTable_LOG_TYPE_UNSPECIFIED                                        = src.ModelDeploymentMonitoringBigQueryTable_LOG_TYPE_UNSPECIFIED
	ModelDeploymentMonitoringBigQueryTable_PREDICT                                                     = src.ModelDeploymentMonitoringBigQueryTable_PREDICT
	ModelDeploymentMonitoringBigQueryTable_SERVING                                                     = src.ModelDeploymentMonitoringBigQueryTable_SERVING
	ModelDeploymentMonitoringBigQueryTable_TRAINING                                                    = src.ModelDeploymentMonitoringBigQueryTable_TRAINING
	ModelDeploymentMonitoringJob_MONITORING_SCHEDULE_STATE_UNSPECIFIED                                 = src.ModelDeploymentMonitoringJob_MONITORING_SCHEDULE_STATE_UNSPECIFIED
	ModelDeploymentMonitoringJob_OFFLINE                                                               = src.ModelDeploymentMonitoringJob_OFFLINE
	ModelDeploymentMonitoringJob_PENDING                                                               = src.ModelDeploymentMonitoringJob_PENDING
	ModelDeploymentMonitoringJob_RUNNING                                                               = src.ModelDeploymentMonitoringJob_RUNNING
	ModelDeploymentMonitoringObjectiveType_FEATURE_ATTRIBUTION_DRIFT                                   = src.ModelDeploymentMonitoringObjectiveType_FEATURE_ATTRIBUTION_DRIFT
	ModelDeploymentMonitoringObjectiveType_FEATURE_ATTRIBUTION_SKEW                                    = src.ModelDeploymentMonitoringObjectiveType_FEATURE_ATTRIBUTION_SKEW
	ModelDeploymentMonitoringObjectiveType_MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED      = src.ModelDeploymentMonitoringObjectiveType_MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED
	ModelDeploymentMonitoringObjectiveType_RAW_FEATURE_DRIFT                                           = src.ModelDeploymentMonitoringObjectiveType_RAW_FEATURE_DRIFT
	ModelDeploymentMonitoringObjectiveType_RAW_FEATURE_SKEW                                            = src.ModelDeploymentMonitoringObjectiveType_RAW_FEATURE_SKEW
	ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_BIGQUERY                      = src.ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_BIGQUERY
	ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_JSONL                         = src.ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_JSONL
	ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PREDICTION_FORMAT_UNSPECIFIED = src.ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PREDICTION_FORMAT_UNSPECIFIED
	ModelSourceInfo_AUTOML                                                                             = src.ModelSourceInfo_AUTOML
	ModelSourceInfo_BQML                                                                               = src.ModelSourceInfo_BQML
	ModelSourceInfo_CUSTOM                                                                             = src.ModelSourceInfo_CUSTOM
	ModelSourceInfo_MODEL_SOURCE_TYPE_UNSPECIFIED                                                      = src.ModelSourceInfo_MODEL_SOURCE_TYPE_UNSPECIFIED
	Model_AUTOMATIC_RESOURCES                                                                          = src.Model_AUTOMATIC_RESOURCES
	Model_DEDICATED_RESOURCES                                                                          = src.Model_DEDICATED_RESOURCES
	Model_DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED                                                        = src.Model_DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED
	Model_ExportFormat_ARTIFACT                                                                        = src.Model_ExportFormat_ARTIFACT
	Model_ExportFormat_EXPORTABLE_CONTENT_UNSPECIFIED                                                  = src.Model_ExportFormat_EXPORTABLE_CONTENT_UNSPECIFIED
	Model_ExportFormat_IMAGE                                                                           = src.Model_ExportFormat_IMAGE
	Model_SHARED_RESOURCES                                                                             = src.Model_SHARED_RESOURCES
	NearestNeighborSearchOperationMetadata_RecordError_EMBEDDING_SIZE_MISMATCH                         = src.NearestNeighborSearchOperationMetadata_RecordError_EMBEDDING_SIZE_MISMATCH
	NearestNeighborSearchOperationMetadata_RecordError_EMPTY_LINE                                      = src.NearestNeighborSearchOperationMetadata_RecordError_EMPTY_LINE
	NearestNeighborSearchOperationMetadata_RecordError_ERROR_TYPE_UNSPECIFIED                          = src.NearestNeighborSearchOperationMetadata_RecordError_ERROR_TYPE_UNSPECIFIED
	NearestNeighborSearchOperationMetadata_RecordError_INVALID_AVRO_SYNTAX                             = src.NearestNeighborSearchOperationMetadata_RecordError_INVALID_AVRO_SYNTAX
	NearestNeighborSearchOperationMetadata_RecordError_INVALID_CSV_SYNTAX                              = src.NearestNeighborSearchOperationMetadata_RecordError_INVALID_CSV_SYNTAX
	NearestNeighborSearchOperationMetadata_RecordError_INVALID_EMBEDDING_ID                            = src.NearestNeighborSearchOperationMetadata_RecordError_INVALID_EMBEDDING_ID
	NearestNeighborSearchOperationMetadata_RecordError_INVALID_JSON_SYNTAX                             = src.NearestNeighborSearchOperationMetadata_RecordError_INVALID_JSON_SYNTAX
	NearestNeighborSearchOperationMetadata_RecordError_NAMESPACE_MISSING                               = src.NearestNeighborSearchOperationMetadata_RecordError_NAMESPACE_MISSING
	PipelineFailurePolicy_PIPELINE_FAILURE_POLICY_FAIL_FAST                                            = src.PipelineFailurePolicy_PIPELINE_FAILURE_POLICY_FAIL_FAST
	PipelineFailurePolicy_PIPELINE_FAILURE_POLICY_FAIL_SLOW                                            = src.PipelineFailurePolicy_PIPELINE_FAILURE_POLICY_FAIL_SLOW
	PipelineFailurePolicy_PIPELINE_FAILURE_POLICY_UNSPECIFIED                                          = src.PipelineFailurePolicy_PIPELINE_FAILURE_POLICY_UNSPECIFIED
	PipelineState_PIPELINE_STATE_CANCELLED                                                             = src.PipelineState_PIPELINE_STATE_CANCELLED
	PipelineState_PIPELINE_STATE_CANCELLING                                                            = src.PipelineState_PIPELINE_STATE_CANCELLING
	PipelineState_PIPELINE_STATE_FAILED                                                                = src.PipelineState_PIPELINE_STATE_FAILED
	PipelineState_PIPELINE_STATE_PAUSED                                                                = src.PipelineState_PIPELINE_STATE_PAUSED
	PipelineState_PIPELINE_STATE_PENDING                                                               = src.PipelineState_PIPELINE_STATE_PENDING
	PipelineState_PIPELINE_STATE_QUEUED                                                                = src.PipelineState_PIPELINE_STATE_QUEUED
	PipelineState_PIPELINE_STATE_RUNNING                                                               = src.PipelineState_PIPELINE_STATE_RUNNING
	PipelineState_PIPELINE_STATE_SUCCEEDED                                                             = src.PipelineState_PIPELINE_STATE_SUCCEEDED
	PipelineState_PIPELINE_STATE_UNSPECIFIED                                                           = src.PipelineState_PIPELINE_STATE_UNSPECIFIED
	PipelineTaskDetail_CANCELLED                                                                       = src.PipelineTaskDetail_CANCELLED
	PipelineTaskDetail_CANCELLING                                                                      = src.PipelineTaskDetail_CANCELLING
	PipelineTaskDetail_CANCEL_PENDING                                                                  = src.PipelineTaskDetail_CANCEL_PENDING
	PipelineTaskDetail_FAILED                                                                          = src.PipelineTaskDetail_FAILED
	PipelineTaskDetail_NOT_TRIGGERED                                                                   = src.PipelineTaskDetail_NOT_TRIGGERED
	PipelineTaskDetail_PENDING                                                                         = src.PipelineTaskDetail_PENDING
	PipelineTaskDetail_RUNNING                                                                         = src.PipelineTaskDetail_RUNNING
	PipelineTaskDetail_SKIPPED                                                                         = src.PipelineTaskDetail_SKIPPED
	PipelineTaskDetail_STATE_UNSPECIFIED                                                               = src.PipelineTaskDetail_STATE_UNSPECIFIED
	PipelineTaskDetail_SUCCEEDED                                                                       = src.PipelineTaskDetail_SUCCEEDED
	SampleConfig_SAMPLE_STRATEGY_UNSPECIFIED                                                           = src.SampleConfig_SAMPLE_STRATEGY_UNSPECIFIED
	SampleConfig_UNCERTAINTY                                                                           = src.SampleConfig_UNCERTAINTY
	StudySpec_ALGORITHM_UNSPECIFIED                                                                    = src.StudySpec_ALGORITHM_UNSPECIFIED
	StudySpec_BEST_MEASUREMENT                                                                         = src.StudySpec_BEST_MEASUREMENT
	StudySpec_GRID_SEARCH                                                                              = src.StudySpec_GRID_SEARCH
	StudySpec_HIGH                                                                                     = src.StudySpec_HIGH
	StudySpec_LAST_MEASUREMENT                                                                         = src.StudySpec_LAST_MEASUREMENT
	StudySpec_LOW                                                                                      = src.StudySpec_LOW
	StudySpec_MEASUREMENT_SELECTION_TYPE_UNSPECIFIED                                                   = src.StudySpec_MEASUREMENT_SELECTION_TYPE_UNSPECIFIED
	StudySpec_MetricSpec_GOAL_TYPE_UNSPECIFIED                                                         = src.StudySpec_MetricSpec_GOAL_TYPE_UNSPECIFIED
	StudySpec_MetricSpec_MAXIMIZE                                                                      = src.StudySpec_MetricSpec_MAXIMIZE
	StudySpec_MetricSpec_MINIMIZE                                                                      = src.StudySpec_MetricSpec_MINIMIZE
	StudySpec_OBSERVATION_NOISE_UNSPECIFIED                                                            = src.StudySpec_OBSERVATION_NOISE_UNSPECIFIED
	StudySpec_ParameterSpec_SCALE_TYPE_UNSPECIFIED                                                     = src.StudySpec_ParameterSpec_SCALE_TYPE_UNSPECIFIED
	StudySpec_ParameterSpec_UNIT_LINEAR_SCALE                                                          = src.StudySpec_ParameterSpec_UNIT_LINEAR_SCALE
	StudySpec_ParameterSpec_UNIT_LOG_SCALE                                                             = src.StudySpec_ParameterSpec_UNIT_LOG_SCALE
	StudySpec_ParameterSpec_UNIT_REVERSE_LOG_SCALE                                                     = src.StudySpec_ParameterSpec_UNIT_REVERSE_LOG_SCALE
	StudySpec_RANDOM_SEARCH                                                                            = src.StudySpec_RANDOM_SEARCH
	Study_ACTIVE                                                                                       = src.Study_ACTIVE
	Study_COMPLETED                                                                                    = src.Study_COMPLETED
	Study_INACTIVE                                                                                     = src.Study_INACTIVE
	Study_STATE_UNSPECIFIED                                                                            = src.Study_STATE_UNSPECIFIED
	TensorboardTimeSeries_BLOB_SEQUENCE                                                                = src.TensorboardTimeSeries_BLOB_SEQUENCE
	TensorboardTimeSeries_SCALAR                                                                       = src.TensorboardTimeSeries_SCALAR
	TensorboardTimeSeries_TENSOR                                                                       = src.TensorboardTimeSeries_TENSOR
	TensorboardTimeSeries_VALUE_TYPE_UNSPECIFIED                                                       = src.TensorboardTimeSeries_VALUE_TYPE_UNSPECIFIED
	Trial_ACTIVE                                                                                       = src.Trial_ACTIVE
	Trial_INFEASIBLE                                                                                   = src.Trial_INFEASIBLE
	Trial_REQUESTED                                                                                    = src.Trial_REQUESTED
	Trial_STATE_UNSPECIFIED                                                                            = src.Trial_STATE_UNSPECIFIED
	Trial_STOPPING                                                                                     = src.Trial_STOPPING
	Trial_SUCCEEDED                                                                                    = src.Trial_SUCCEEDED
)

Deprecated: Please use consts in: cloud.google.com/go/aiplatform/apiv1/aiplatformpb

Variables ¶
View Source
var (
	AcceleratorType_name                                                                        = src.AcceleratorType_name
	AcceleratorType_value                                                                       = src.AcceleratorType_value
	Artifact_State_name                                                                         = src.Artifact_State_name
	Artifact_State_value                                                                        = src.Artifact_State_value
	Event_Type_name                                                                             = src.Event_Type_name
	Event_Type_value                                                                            = src.Event_Type_value
	ExamplesOverride_DataFormat_name                                                            = src.ExamplesOverride_DataFormat_name
	ExamplesOverride_DataFormat_value                                                           = src.ExamplesOverride_DataFormat_value
	Execution_State_name                                                                        = src.Execution_State_name
	Execution_State_value                                                                       = src.Execution_State_value
	ExplanationMetadata_InputMetadata_Encoding_name                                             = src.ExplanationMetadata_InputMetadata_Encoding_name
	ExplanationMetadata_InputMetadata_Encoding_value                                            = src.ExplanationMetadata_InputMetadata_Encoding_value
	ExplanationMetadata_InputMetadata_Visualization_ColorMap_name                               = src.ExplanationMetadata_InputMetadata_Visualization_ColorMap_name
	ExplanationMetadata_InputMetadata_Visualization_ColorMap_value                              = src.ExplanationMetadata_InputMetadata_Visualization_ColorMap_value
	ExplanationMetadata_InputMetadata_Visualization_OverlayType_name                            = src.ExplanationMetadata_InputMetadata_Visualization_OverlayType_name
	ExplanationMetadata_InputMetadata_Visualization_OverlayType_value                           = src.ExplanationMetadata_InputMetadata_Visualization_OverlayType_value
	ExplanationMetadata_InputMetadata_Visualization_Polarity_name                               = src.ExplanationMetadata_InputMetadata_Visualization_Polarity_name
	ExplanationMetadata_InputMetadata_Visualization_Polarity_value                              = src.ExplanationMetadata_InputMetadata_Visualization_Polarity_value
	ExplanationMetadata_InputMetadata_Visualization_Type_name                                   = src.ExplanationMetadata_InputMetadata_Visualization_Type_name
	ExplanationMetadata_InputMetadata_Visualization_Type_value                                  = src.ExplanationMetadata_InputMetadata_Visualization_Type_value
	Feature_MonitoringStatsAnomaly_Objective_name                                               = src.Feature_MonitoringStatsAnomaly_Objective_name
	Feature_MonitoringStatsAnomaly_Objective_value                                              = src.Feature_MonitoringStatsAnomaly_Objective_value
	Feature_ValueType_name                                                                      = src.Feature_ValueType_name
	Feature_ValueType_value                                                                     = src.Feature_ValueType_value
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_Baseline_name                           = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_Baseline_name
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_Baseline_value                          = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_Baseline_value
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_State_name                              = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_State_name
	FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_State_value                             = src.FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_State_value
	Featurestore_State_name                                                                     = src.Featurestore_State_name
	Featurestore_State_value                                                                    = src.Featurestore_State_value
	File_google_cloud_aiplatform_v1_accelerator_type_proto                                      = src.File_google_cloud_aiplatform_v1_accelerator_type_proto
	File_google_cloud_aiplatform_v1_annotation_proto                                            = src.File_google_cloud_aiplatform_v1_annotation_proto
	File_google_cloud_aiplatform_v1_annotation_spec_proto                                       = src.File_google_cloud_aiplatform_v1_annotation_spec_proto
	File_google_cloud_aiplatform_v1_artifact_proto                                              = src.File_google_cloud_aiplatform_v1_artifact_proto
	File_google_cloud_aiplatform_v1_batch_prediction_job_proto                                  = src.File_google_cloud_aiplatform_v1_batch_prediction_job_proto
	File_google_cloud_aiplatform_v1_completion_stats_proto                                      = src.File_google_cloud_aiplatform_v1_completion_stats_proto
	File_google_cloud_aiplatform_v1_context_proto                                               = src.File_google_cloud_aiplatform_v1_context_proto
	File_google_cloud_aiplatform_v1_custom_job_proto                                            = src.File_google_cloud_aiplatform_v1_custom_job_proto
	File_google_cloud_aiplatform_v1_data_item_proto                                             = src.File_google_cloud_aiplatform_v1_data_item_proto
	File_google_cloud_aiplatform_v1_data_labeling_job_proto                                     = src.File_google_cloud_aiplatform_v1_data_labeling_job_proto
	File_google_cloud_aiplatform_v1_dataset_proto                                               = src.File_google_cloud_aiplatform_v1_dataset_proto
	File_google_cloud_aiplatform_v1_dataset_service_proto                                       = src.File_google_cloud_aiplatform_v1_dataset_service_proto
	File_google_cloud_aiplatform_v1_deployed_index_ref_proto                                    = src.File_google_cloud_aiplatform_v1_deployed_index_ref_proto
	File_google_cloud_aiplatform_v1_deployed_model_ref_proto                                    = src.File_google_cloud_aiplatform_v1_deployed_model_ref_proto
	File_google_cloud_aiplatform_v1_encryption_spec_proto                                       = src.File_google_cloud_aiplatform_v1_encryption_spec_proto
	File_google_cloud_aiplatform_v1_endpoint_proto                                              = src.File_google_cloud_aiplatform_v1_endpoint_proto
	File_google_cloud_aiplatform_v1_endpoint_service_proto                                      = src.File_google_cloud_aiplatform_v1_endpoint_service_proto
	File_google_cloud_aiplatform_v1_entity_type_proto                                           = src.File_google_cloud_aiplatform_v1_entity_type_proto
	File_google_cloud_aiplatform_v1_env_var_proto                                               = src.File_google_cloud_aiplatform_v1_env_var_proto
	File_google_cloud_aiplatform_v1_event_proto                                                 = src.File_google_cloud_aiplatform_v1_event_proto
	File_google_cloud_aiplatform_v1_execution_proto                                             = src.File_google_cloud_aiplatform_v1_execution_proto
	File_google_cloud_aiplatform_v1_explanation_metadata_proto                                  = src.File_google_cloud_aiplatform_v1_explanation_metadata_proto
	File_google_cloud_aiplatform_v1_explanation_proto                                           = src.File_google_cloud_aiplatform_v1_explanation_proto
	File_google_cloud_aiplatform_v1_feature_monitoring_stats_proto                              = src.File_google_cloud_aiplatform_v1_feature_monitoring_stats_proto
	File_google_cloud_aiplatform_v1_feature_proto                                               = src.File_google_cloud_aiplatform_v1_feature_proto
	File_google_cloud_aiplatform_v1_feature_selector_proto                                      = src.File_google_cloud_aiplatform_v1_feature_selector_proto
	File_google_cloud_aiplatform_v1_featurestore_monitoring_proto                               = src.File_google_cloud_aiplatform_v1_featurestore_monitoring_proto
	File_google_cloud_aiplatform_v1_featurestore_online_service_proto                           = src.File_google_cloud_aiplatform_v1_featurestore_online_service_proto
	File_google_cloud_aiplatform_v1_featurestore_proto                                          = src.File_google_cloud_aiplatform_v1_featurestore_proto
	File_google_cloud_aiplatform_v1_featurestore_service_proto                                  = src.File_google_cloud_aiplatform_v1_featurestore_service_proto
	File_google_cloud_aiplatform_v1_hyperparameter_tuning_job_proto                             = src.File_google_cloud_aiplatform_v1_hyperparameter_tuning_job_proto
	File_google_cloud_aiplatform_v1_index_endpoint_proto                                        = src.File_google_cloud_aiplatform_v1_index_endpoint_proto
	File_google_cloud_aiplatform_v1_index_endpoint_service_proto                                = src.File_google_cloud_aiplatform_v1_index_endpoint_service_proto
	File_google_cloud_aiplatform_v1_index_proto                                                 = src.File_google_cloud_aiplatform_v1_index_proto
	File_google_cloud_aiplatform_v1_index_service_proto                                         = src.File_google_cloud_aiplatform_v1_index_service_proto
	File_google_cloud_aiplatform_v1_io_proto                                                    = src.File_google_cloud_aiplatform_v1_io_proto
	File_google_cloud_aiplatform_v1_job_service_proto                                           = src.File_google_cloud_aiplatform_v1_job_service_proto
	File_google_cloud_aiplatform_v1_job_state_proto                                             = src.File_google_cloud_aiplatform_v1_job_state_proto
	File_google_cloud_aiplatform_v1_lineage_subgraph_proto                                      = src.File_google_cloud_aiplatform_v1_lineage_subgraph_proto
	File_google_cloud_aiplatform_v1_machine_resources_proto                                     = src.File_google_cloud_aiplatform_v1_machine_resources_proto
	File_google_cloud_aiplatform_v1_manual_batch_tuning_parameters_proto                        = src.File_google_cloud_aiplatform_v1_manual_batch_tuning_parameters_proto
	File_google_cloud_aiplatform_v1_metadata_schema_proto                                       = src.File_google_cloud_aiplatform_v1_metadata_schema_proto
	File_google_cloud_aiplatform_v1_metadata_service_proto                                      = src.File_google_cloud_aiplatform_v1_metadata_service_proto
	File_google_cloud_aiplatform_v1_metadata_store_proto                                        = src.File_google_cloud_aiplatform_v1_metadata_store_proto
	File_google_cloud_aiplatform_v1_migratable_resource_proto                                   = src.File_google_cloud_aiplatform_v1_migratable_resource_proto
	File_google_cloud_aiplatform_v1_migration_service_proto                                     = src.File_google_cloud_aiplatform_v1_migration_service_proto
	File_google_cloud_aiplatform_v1_model_deployment_monitoring_job_proto                       = src.File_google_cloud_aiplatform_v1_model_deployment_monitoring_job_proto
	File_google_cloud_aiplatform_v1_model_evaluation_proto                                      = src.File_google_cloud_aiplatform_v1_model_evaluation_proto
	File_google_cloud_aiplatform_v1_model_evaluation_slice_proto                                = src.File_google_cloud_aiplatform_v1_model_evaluation_slice_proto
	File_google_cloud_aiplatform_v1_model_monitoring_proto                                      = src.File_google_cloud_aiplatform_v1_model_monitoring_proto
	File_google_cloud_aiplatform_v1_model_proto                                                 = src.File_google_cloud_aiplatform_v1_model_proto
	File_google_cloud_aiplatform_v1_model_service_proto                                         = src.File_google_cloud_aiplatform_v1_model_service_proto
	File_google_cloud_aiplatform_v1_operation_proto                                             = src.File_google_cloud_aiplatform_v1_operation_proto
	File_google_cloud_aiplatform_v1_pipeline_failure_policy_proto                               = src.File_google_cloud_aiplatform_v1_pipeline_failure_policy_proto
	File_google_cloud_aiplatform_v1_pipeline_job_proto                                          = src.File_google_cloud_aiplatform_v1_pipeline_job_proto
	File_google_cloud_aiplatform_v1_pipeline_service_proto                                      = src.File_google_cloud_aiplatform_v1_pipeline_service_proto
	File_google_cloud_aiplatform_v1_pipeline_state_proto                                        = src.File_google_cloud_aiplatform_v1_pipeline_state_proto
	File_google_cloud_aiplatform_v1_prediction_service_proto                                    = src.File_google_cloud_aiplatform_v1_prediction_service_proto
	File_google_cloud_aiplatform_v1_saved_query_proto                                           = src.File_google_cloud_aiplatform_v1_saved_query_proto
	File_google_cloud_aiplatform_v1_specialist_pool_proto                                       = src.File_google_cloud_aiplatform_v1_specialist_pool_proto
	File_google_cloud_aiplatform_v1_specialist_pool_service_proto                               = src.File_google_cloud_aiplatform_v1_specialist_pool_service_proto
	File_google_cloud_aiplatform_v1_study_proto                                                 = src.File_google_cloud_aiplatform_v1_study_proto
	File_google_cloud_aiplatform_v1_tensorboard_data_proto                                      = src.File_google_cloud_aiplatform_v1_tensorboard_data_proto
	File_google_cloud_aiplatform_v1_tensorboard_experiment_proto                                = src.File_google_cloud_aiplatform_v1_tensorboard_experiment_proto
	File_google_cloud_aiplatform_v1_tensorboard_proto                                           = src.File_google_cloud_aiplatform_v1_tensorboard_proto
	File_google_cloud_aiplatform_v1_tensorboard_run_proto                                       = src.File_google_cloud_aiplatform_v1_tensorboard_run_proto
	File_google_cloud_aiplatform_v1_tensorboard_service_proto                                   = src.File_google_cloud_aiplatform_v1_tensorboard_service_proto
	File_google_cloud_aiplatform_v1_tensorboard_time_series_proto                               = src.File_google_cloud_aiplatform_v1_tensorboard_time_series_proto
	File_google_cloud_aiplatform_v1_training_pipeline_proto                                     = src.File_google_cloud_aiplatform_v1_training_pipeline_proto
	File_google_cloud_aiplatform_v1_types_proto                                                 = src.File_google_cloud_aiplatform_v1_types_proto
	File_google_cloud_aiplatform_v1_unmanaged_container_model_proto                             = src.File_google_cloud_aiplatform_v1_unmanaged_container_model_proto
	File_google_cloud_aiplatform_v1_user_action_reference_proto                                 = src.File_google_cloud_aiplatform_v1_user_action_reference_proto
	File_google_cloud_aiplatform_v1_value_proto                                                 = src.File_google_cloud_aiplatform_v1_value_proto
	File_google_cloud_aiplatform_v1_vizier_service_proto                                        = src.File_google_cloud_aiplatform_v1_vizier_service_proto
	Index_IndexUpdateMethod_name                                                                = src.Index_IndexUpdateMethod_name
	Index_IndexUpdateMethod_value                                                               = src.Index_IndexUpdateMethod_value
	JobState_name                                                                               = src.JobState_name
	JobState_value                                                                              = src.JobState_value
	MetadataSchema_MetadataSchemaType_name                                                      = src.MetadataSchema_MetadataSchemaType_name
	MetadataSchema_MetadataSchemaType_value                                                     = src.MetadataSchema_MetadataSchemaType_value
	ModelDeploymentMonitoringBigQueryTable_LogSource_name                                       = src.ModelDeploymentMonitoringBigQueryTable_LogSource_name
	ModelDeploymentMonitoringBigQueryTable_LogSource_value                                      = src.ModelDeploymentMonitoringBigQueryTable_LogSource_value
	ModelDeploymentMonitoringBigQueryTable_LogType_name                                         = src.ModelDeploymentMonitoringBigQueryTable_LogType_name
	ModelDeploymentMonitoringBigQueryTable_LogType_value                                        = src.ModelDeploymentMonitoringBigQueryTable_LogType_value
	ModelDeploymentMonitoringJob_MonitoringScheduleState_name                                   = src.ModelDeploymentMonitoringJob_MonitoringScheduleState_name
	ModelDeploymentMonitoringJob_MonitoringScheduleState_value                                  = src.ModelDeploymentMonitoringJob_MonitoringScheduleState_value
	ModelDeploymentMonitoringObjectiveType_name                                                 = src.ModelDeploymentMonitoringObjectiveType_name
	ModelDeploymentMonitoringObjectiveType_value                                                = src.ModelDeploymentMonitoringObjectiveType_value
	ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PredictionFormat_name  = src.ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PredictionFormat_name
	ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PredictionFormat_value = src.ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PredictionFormat_value
	ModelSourceInfo_ModelSourceType_name                                                        = src.ModelSourceInfo_ModelSourceType_name
	ModelSourceInfo_ModelSourceType_value                                                       = src.ModelSourceInfo_ModelSourceType_value
	Model_DeploymentResourcesType_name                                                          = src.Model_DeploymentResourcesType_name
	Model_DeploymentResourcesType_value                                                         = src.Model_DeploymentResourcesType_value
	Model_ExportFormat_ExportableContent_name                                                   = src.Model_ExportFormat_ExportableContent_name
	Model_ExportFormat_ExportableContent_value                                                  = src.Model_ExportFormat_ExportableContent_value
	NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType_name                     = src.NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType_name
	NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType_value                    = src.NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType_value
	PipelineFailurePolicy_name                                                                  = src.PipelineFailurePolicy_name
	PipelineFailurePolicy_value                                                                 = src.PipelineFailurePolicy_value
	PipelineState_name                                                                          = src.PipelineState_name
	PipelineState_value                                                                         = src.PipelineState_value
	PipelineTaskDetail_State_name                                                               = src.PipelineTaskDetail_State_name
	PipelineTaskDetail_State_value                                                              = src.PipelineTaskDetail_State_value
	SampleConfig_SampleStrategy_name                                                            = src.SampleConfig_SampleStrategy_name
	SampleConfig_SampleStrategy_value                                                           = src.SampleConfig_SampleStrategy_value
	StudySpec_Algorithm_name                                                                    = src.StudySpec_Algorithm_name
	StudySpec_Algorithm_value                                                                   = src.StudySpec_Algorithm_value
	StudySpec_MeasurementSelectionType_name                                                     = src.StudySpec_MeasurementSelectionType_name
	StudySpec_MeasurementSelectionType_value                                                    = src.StudySpec_MeasurementSelectionType_value
	StudySpec_MetricSpec_GoalType_name                                                          = src.StudySpec_MetricSpec_GoalType_name
	StudySpec_MetricSpec_GoalType_value                                                         = src.StudySpec_MetricSpec_GoalType_value
	StudySpec_ObservationNoise_name                                                             = src.StudySpec_ObservationNoise_name
	StudySpec_ObservationNoise_value                                                            = src.StudySpec_ObservationNoise_value
	StudySpec_ParameterSpec_ScaleType_name                                                      = src.StudySpec_ParameterSpec_ScaleType_name
	StudySpec_ParameterSpec_ScaleType_value                                                     = src.StudySpec_ParameterSpec_ScaleType_value
	Study_State_name                                                                            = src.Study_State_name
	Study_State_value                                                                           = src.Study_State_value
	TensorboardTimeSeries_ValueType_name                                                        = src.TensorboardTimeSeries_ValueType_name
	TensorboardTimeSeries_ValueType_value                                                       = src.TensorboardTimeSeries_ValueType_value
	Trial_State_name                                                                            = src.Trial_State_name
	Trial_State_value                                                                           = src.Trial_State_value
)

Deprecated: Please use vars in: cloud.google.com/go/aiplatform/apiv1/aiplatformpb

Functions ¶
func
RegisterDatasetServiceServer
DEPRECATED
func
RegisterEndpointServiceServer
DEPRECATED
func
RegisterFeaturestoreOnlineServingServiceServer
DEPRECATED
func
RegisterFeaturestoreServiceServer
DEPRECATED
func
RegisterIndexEndpointServiceServer
DEPRECATED
func
RegisterIndexServiceServer
DEPRECATED
func
RegisterJobServiceServer
DEPRECATED
func
RegisterMetadataServiceServer
DEPRECATED
func
RegisterMigrationServiceServer
DEPRECATED
func
RegisterModelServiceServer
DEPRECATED
func
RegisterPipelineServiceServer
DEPRECATED
func
RegisterPredictionServiceServer
DEPRECATED
func
RegisterSpecialistPoolServiceServer
DEPRECATED
func
RegisterTensorboardServiceServer
DEPRECATED
func
RegisterVizierServiceServer
DEPRECATED
Types ¶
type
AcceleratorType
DEPRECATED
type
ActiveLearningConfig
DEPRECATED
type ActiveLearningConfig_MaxDataItemCount ¶
type ActiveLearningConfig_MaxDataItemCount = src.ActiveLearningConfig_MaxDataItemCount
type ActiveLearningConfig_MaxDataItemPercentage ¶
type ActiveLearningConfig_MaxDataItemPercentage = src.ActiveLearningConfig_MaxDataItemPercentage
type
AddContextArtifactsAndExecutionsRequest
DEPRECATED
type
AddContextArtifactsAndExecutionsResponse
DEPRECATED
type
AddContextChildrenRequest
DEPRECATED
type
AddContextChildrenResponse
DEPRECATED
type
AddExecutionEventsRequest
DEPRECATED
type
AddExecutionEventsResponse
DEPRECATED
type
AddTrialMeasurementRequest
DEPRECATED
type
Annotation
DEPRECATED
type
AnnotationSpec
DEPRECATED
type
Artifact
DEPRECATED
type
Artifact_State
DEPRECATED
type
Attribution
DEPRECATED
type
AutomaticResources
DEPRECATED
type
AutoscalingMetricSpec
DEPRECATED
type
AvroSource
DEPRECATED
type
BatchCreateFeaturesOperationMetadata
DEPRECATED
type
BatchCreateFeaturesRequest
DEPRECATED
type
BatchCreateFeaturesResponse
DEPRECATED
type
BatchCreateTensorboardRunsRequest
DEPRECATED
type
BatchCreateTensorboardRunsResponse
DEPRECATED
type
BatchCreateTensorboardTimeSeriesRequest
DEPRECATED
type
BatchCreateTensorboardTimeSeriesResponse
DEPRECATED
type
BatchDedicatedResources
DEPRECATED
type
BatchImportModelEvaluationSlicesRequest
DEPRECATED
type
BatchImportModelEvaluationSlicesResponse
DEPRECATED
type
BatchMigrateResourcesOperationMetadata
DEPRECATED
type
BatchMigrateResourcesOperationMetadata_PartialResult
DEPRECATED
type BatchMigrateResourcesOperationMetadata_PartialResult_Dataset ¶
type BatchMigrateResourcesOperationMetadata_PartialResult_Dataset = src.BatchMigrateResourcesOperationMetadata_PartialResult_Dataset
type BatchMigrateResourcesOperationMetadata_PartialResult_Error ¶
type BatchMigrateResourcesOperationMetadata_PartialResult_Error = src.BatchMigrateResourcesOperationMetadata_PartialResult_Error
type BatchMigrateResourcesOperationMetadata_PartialResult_Model ¶
type BatchMigrateResourcesOperationMetadata_PartialResult_Model = src.BatchMigrateResourcesOperationMetadata_PartialResult_Model
type
BatchMigrateResourcesRequest
DEPRECATED
type
BatchMigrateResourcesResponse
DEPRECATED
type
BatchPredictionJob
DEPRECATED
type
BatchPredictionJob_InputConfig
DEPRECATED
type BatchPredictionJob_InputConfig_BigquerySource ¶
type BatchPredictionJob_InputConfig_BigquerySource = src.BatchPredictionJob_InputConfig_BigquerySource
type BatchPredictionJob_InputConfig_GcsSource ¶
type BatchPredictionJob_InputConfig_GcsSource = src.BatchPredictionJob_InputConfig_GcsSource
type
BatchPredictionJob_OutputConfig
DEPRECATED
type BatchPredictionJob_OutputConfig_BigqueryDestination ¶
type BatchPredictionJob_OutputConfig_BigqueryDestination = src.BatchPredictionJob_OutputConfig_BigqueryDestination
type BatchPredictionJob_OutputConfig_GcsDestination ¶
type BatchPredictionJob_OutputConfig_GcsDestination = src.BatchPredictionJob_OutputConfig_GcsDestination
type
BatchPredictionJob_OutputInfo
DEPRECATED
type BatchPredictionJob_OutputInfo_BigqueryOutputDataset ¶
type BatchPredictionJob_OutputInfo_BigqueryOutputDataset = src.BatchPredictionJob_OutputInfo_BigqueryOutputDataset
type BatchPredictionJob_OutputInfo_GcsOutputDirectory ¶
type BatchPredictionJob_OutputInfo_GcsOutputDirectory = src.BatchPredictionJob_OutputInfo_GcsOutputDirectory
type
BatchReadFeatureValuesOperationMetadata
DEPRECATED
type
BatchReadFeatureValuesRequest
DEPRECATED
type BatchReadFeatureValuesRequest_BigqueryReadInstances ¶
type BatchReadFeatureValuesRequest_BigqueryReadInstances = src.BatchReadFeatureValuesRequest_BigqueryReadInstances
type BatchReadFeatureValuesRequest_CsvReadInstances ¶
type BatchReadFeatureValuesRequest_CsvReadInstances = src.BatchReadFeatureValuesRequest_CsvReadInstances
type
BatchReadFeatureValuesRequest_EntityTypeSpec
DEPRECATED
type
BatchReadFeatureValuesRequest_PassThroughField
DEPRECATED
type
BatchReadFeatureValuesResponse
DEPRECATED
type
BatchReadTensorboardTimeSeriesDataRequest
DEPRECATED
type
BatchReadTensorboardTimeSeriesDataResponse
DEPRECATED
type
BigQueryDestination
DEPRECATED
type
BigQuerySource
DEPRECATED
type
BlurBaselineConfig
DEPRECATED
type
BoolArray
DEPRECATED
type
CancelBatchPredictionJobRequest
DEPRECATED
type
CancelCustomJobRequest
DEPRECATED
type
CancelDataLabelingJobRequest
DEPRECATED
type
CancelHyperparameterTuningJobRequest
DEPRECATED
type
CancelPipelineJobRequest
DEPRECATED
type
CancelTrainingPipelineRequest
DEPRECATED
type
CheckTrialEarlyStoppingStateMetatdata
DEPRECATED
type
CheckTrialEarlyStoppingStateRequest
DEPRECATED
type
CheckTrialEarlyStoppingStateResponse
DEPRECATED
type
CompleteTrialRequest
DEPRECATED
type
CompletionStats
DEPRECATED
type
ContainerRegistryDestination
DEPRECATED
type
ContainerSpec
DEPRECATED
type
Context
DEPRECATED
type
CreateArtifactRequest
DEPRECATED
type
CreateBatchPredictionJobRequest
DEPRECATED
type
CreateContextRequest
DEPRECATED
type
CreateCustomJobRequest
DEPRECATED
type
CreateDataLabelingJobRequest
DEPRECATED
type
CreateDatasetOperationMetadata
DEPRECATED
type
CreateDatasetRequest
DEPRECATED
type
CreateEndpointOperationMetadata
DEPRECATED
type
CreateEndpointRequest
DEPRECATED
type
CreateEntityTypeOperationMetadata
DEPRECATED
type
CreateEntityTypeRequest
DEPRECATED
type
CreateExecutionRequest
DEPRECATED
type
CreateFeatureOperationMetadata
DEPRECATED
type
CreateFeatureRequest
DEPRECATED
type
CreateFeaturestoreOperationMetadata
DEPRECATED
type
CreateFeaturestoreRequest
DEPRECATED
type
CreateHyperparameterTuningJobRequest
DEPRECATED
type
CreateIndexEndpointOperationMetadata
DEPRECATED
type
CreateIndexEndpointRequest
DEPRECATED
type
CreateIndexOperationMetadata
DEPRECATED
type
CreateIndexRequest
DEPRECATED
type
CreateMetadataSchemaRequest
DEPRECATED
type
CreateMetadataStoreOperationMetadata
DEPRECATED
type
CreateMetadataStoreRequest
DEPRECATED
type
CreateModelDeploymentMonitoringJobRequest
DEPRECATED
type
CreatePipelineJobRequest
DEPRECATED
type
CreateSpecialistPoolOperationMetadata
DEPRECATED
type
CreateSpecialistPoolRequest
DEPRECATED
type
CreateStudyRequest
DEPRECATED
type
CreateTensorboardExperimentRequest
DEPRECATED
type
CreateTensorboardOperationMetadata
DEPRECATED
type
CreateTensorboardRequest
DEPRECATED
type
CreateTensorboardRunRequest
DEPRECATED
type
CreateTensorboardTimeSeriesRequest
DEPRECATED
type
CreateTrainingPipelineRequest
DEPRECATED
type
CreateTrialRequest
DEPRECATED
type
CsvDestination
DEPRECATED
type
CsvSource
DEPRECATED
type
CustomJob
DEPRECATED
type
CustomJobSpec
DEPRECATED
type
DataItem
DEPRECATED
type
DataLabelingJob
DEPRECATED
type
Dataset
DEPRECATED
type
DatasetServiceClient
DEPRECATED
type
DatasetServiceServer
DEPRECATED
type
DedicatedResources
DEPRECATED
type
DeleteArtifactRequest
DEPRECATED
type
DeleteBatchPredictionJobRequest
DEPRECATED
type
DeleteContextRequest
DEPRECATED
type
DeleteCustomJobRequest
DEPRECATED
type
DeleteDataLabelingJobRequest
DEPRECATED
type
DeleteDatasetRequest
DEPRECATED
type
DeleteEndpointRequest
DEPRECATED
type
DeleteEntityTypeRequest
DEPRECATED
type
DeleteExecutionRequest
DEPRECATED
type
DeleteFeatureRequest
DEPRECATED
type
DeleteFeaturestoreRequest
DEPRECATED
type
DeleteHyperparameterTuningJobRequest
DEPRECATED
type
DeleteIndexEndpointRequest
DEPRECATED
type
DeleteIndexRequest
DEPRECATED
type
DeleteMetadataStoreOperationMetadata
DEPRECATED
type
DeleteMetadataStoreRequest
DEPRECATED
type
DeleteModelDeploymentMonitoringJobRequest
DEPRECATED
type
DeleteModelRequest
DEPRECATED
type
DeleteModelVersionRequest
DEPRECATED
type
DeleteOperationMetadata
DEPRECATED
type
DeletePipelineJobRequest
DEPRECATED
type
DeleteSpecialistPoolRequest
DEPRECATED
type
DeleteStudyRequest
DEPRECATED
type
DeleteTensorboardExperimentRequest
DEPRECATED
type
DeleteTensorboardRequest
DEPRECATED
type
DeleteTensorboardRunRequest
DEPRECATED
type
DeleteTensorboardTimeSeriesRequest
DEPRECATED
type
DeleteTrainingPipelineRequest
DEPRECATED
type
DeleteTrialRequest
DEPRECATED
type
DeployIndexOperationMetadata
DEPRECATED
type
DeployIndexRequest
DEPRECATED
type
DeployIndexResponse
DEPRECATED
type
DeployModelOperationMetadata
DEPRECATED
type
DeployModelRequest
DEPRECATED
type
DeployModelResponse
DEPRECATED
type
DeployedIndex
DEPRECATED
type
DeployedIndexAuthConfig
DEPRECATED
type
DeployedIndexAuthConfig_AuthProvider
DEPRECATED
type
DeployedIndexRef
DEPRECATED
type
DeployedModel
DEPRECATED
type
DeployedModelRef
DEPRECATED
type DeployedModel_AutomaticResources ¶
type DeployedModel_AutomaticResources = src.DeployedModel_AutomaticResources
type DeployedModel_DedicatedResources ¶
type DeployedModel_DedicatedResources = src.DeployedModel_DedicatedResources
type DestinationFeatureSetting ¶
type DestinationFeatureSetting = src.DestinationFeatureSetting
type
DiskSpec
DEPRECATED
type
DoubleArray
DEPRECATED
type
EncryptionSpec
DEPRECATED
type
Endpoint
DEPRECATED
type
EndpointServiceClient
DEPRECATED
type
EndpointServiceServer
DEPRECATED
type
EntityType
DEPRECATED
type
EnvVar
DEPRECATED
type
Event
DEPRECATED
type
Event_Type
DEPRECATED
type
ExamplesOverride
DEPRECATED
type
ExamplesOverride_DataFormat
DEPRECATED
type
ExamplesRestrictionsNamespace
DEPRECATED
type
Execution
DEPRECATED
type
Execution_State
DEPRECATED
type
ExplainRequest
DEPRECATED
type
ExplainResponse
DEPRECATED
type
Explanation
DEPRECATED
type
ExplanationMetadata
DEPRECATED
type
ExplanationMetadataOverride
DEPRECATED
type
ExplanationMetadataOverride_InputMetadataOverride
DEPRECATED
type
ExplanationMetadata_InputMetadata
DEPRECATED
type
ExplanationMetadata_InputMetadata_Encoding
DEPRECATED
type
ExplanationMetadata_InputMetadata_FeatureValueDomain
DEPRECATED
type
ExplanationMetadata_InputMetadata_Visualization
DEPRECATED
type
ExplanationMetadata_InputMetadata_Visualization_ColorMap
DEPRECATED
type
ExplanationMetadata_InputMetadata_Visualization_OverlayType
DEPRECATED
type
ExplanationMetadata_InputMetadata_Visualization_Polarity
DEPRECATED
type
ExplanationMetadata_InputMetadata_Visualization_Type
DEPRECATED
type
ExplanationMetadata_OutputMetadata
DEPRECATED
type ExplanationMetadata_OutputMetadata_DisplayNameMappingKey ¶
type ExplanationMetadata_OutputMetadata_DisplayNameMappingKey = src.ExplanationMetadata_OutputMetadata_DisplayNameMappingKey
type ExplanationMetadata_OutputMetadata_IndexDisplayNameMapping ¶
type ExplanationMetadata_OutputMetadata_IndexDisplayNameMapping = src.ExplanationMetadata_OutputMetadata_IndexDisplayNameMapping
type
ExplanationParameters
DEPRECATED
type ExplanationParameters_IntegratedGradientsAttribution ¶
type ExplanationParameters_IntegratedGradientsAttribution = src.ExplanationParameters_IntegratedGradientsAttribution
type ExplanationParameters_SampledShapleyAttribution ¶
type ExplanationParameters_SampledShapleyAttribution = src.ExplanationParameters_SampledShapleyAttribution
type ExplanationParameters_XraiAttribution ¶
type ExplanationParameters_XraiAttribution = src.ExplanationParameters_XraiAttribution
type
ExplanationSpec
DEPRECATED
type
ExplanationSpecOverride
DEPRECATED
type
ExportDataConfig
DEPRECATED
type ExportDataConfig_GcsDestination ¶
type ExportDataConfig_GcsDestination = src.ExportDataConfig_GcsDestination
type
ExportDataOperationMetadata
DEPRECATED
type
ExportDataRequest
DEPRECATED
type
ExportDataResponse
DEPRECATED
type
ExportFeatureValuesOperationMetadata
DEPRECATED
type
ExportFeatureValuesRequest
DEPRECATED
type
ExportFeatureValuesRequest_FullExport
DEPRECATED
type ExportFeatureValuesRequest_FullExport_ ¶
type ExportFeatureValuesRequest_FullExport_ = src.ExportFeatureValuesRequest_FullExport_
type
ExportFeatureValuesRequest_SnapshotExport
DEPRECATED
type ExportFeatureValuesRequest_SnapshotExport_ ¶
type ExportFeatureValuesRequest_SnapshotExport_ = src.ExportFeatureValuesRequest_SnapshotExport_
type
ExportFeatureValuesResponse
DEPRECATED
type
ExportModelOperationMetadata
DEPRECATED
type
ExportModelOperationMetadata_OutputInfo
DEPRECATED
type
ExportModelRequest
DEPRECATED
type
ExportModelRequest_OutputConfig
DEPRECATED
type
ExportModelResponse
DEPRECATED
type
ExportTensorboardTimeSeriesDataRequest
DEPRECATED
type
ExportTensorboardTimeSeriesDataResponse
DEPRECATED
type
Feature
DEPRECATED
type
FeatureNoiseSigma
DEPRECATED
type
FeatureNoiseSigma_NoiseSigmaForFeature
DEPRECATED
type
FeatureSelector
DEPRECATED
type
FeatureStatsAnomaly
DEPRECATED
type
FeatureValue
DEPRECATED
type
FeatureValueDestination
DEPRECATED
type FeatureValueDestination_BigqueryDestination ¶
type FeatureValueDestination_BigqueryDestination = src.FeatureValueDestination_BigqueryDestination
type FeatureValueDestination_CsvDestination ¶
type FeatureValueDestination_CsvDestination = src.FeatureValueDestination_CsvDestination
type FeatureValueDestination_TfrecordDestination ¶
type FeatureValueDestination_TfrecordDestination = src.FeatureValueDestination_TfrecordDestination
type
FeatureValueList
DEPRECATED
type FeatureValue_BoolArrayValue ¶
type FeatureValue_BoolArrayValue = src.FeatureValue_BoolArrayValue
type FeatureValue_BoolValue ¶
type FeatureValue_BoolValue = src.FeatureValue_BoolValue
type FeatureValue_BytesValue ¶
type FeatureValue_BytesValue = src.FeatureValue_BytesValue
type FeatureValue_DoubleArrayValue ¶
type FeatureValue_DoubleArrayValue = src.FeatureValue_DoubleArrayValue
type FeatureValue_DoubleValue ¶
type FeatureValue_DoubleValue = src.FeatureValue_DoubleValue
type FeatureValue_Int64ArrayValue ¶
type FeatureValue_Int64ArrayValue = src.FeatureValue_Int64ArrayValue
type FeatureValue_Int64Value ¶
type FeatureValue_Int64Value = src.FeatureValue_Int64Value
type
FeatureValue_Metadata
DEPRECATED
type FeatureValue_StringArrayValue ¶
type FeatureValue_StringArrayValue = src.FeatureValue_StringArrayValue
type FeatureValue_StringValue ¶
type FeatureValue_StringValue = src.FeatureValue_StringValue
type
Feature_MonitoringStatsAnomaly
DEPRECATED
type
Feature_MonitoringStatsAnomaly_Objective
DEPRECATED
type
Feature_ValueType
DEPRECATED
type
Featurestore
DEPRECATED
type
FeaturestoreMonitoringConfig
DEPRECATED
type
FeaturestoreMonitoringConfig_ImportFeaturesAnalysis
DEPRECATED
type
FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_Baseline
DEPRECATED
type
FeaturestoreMonitoringConfig_ImportFeaturesAnalysis_State
DEPRECATED
type
FeaturestoreMonitoringConfig_SnapshotAnalysis
DEPRECATED
type
FeaturestoreMonitoringConfig_ThresholdConfig
DEPRECATED
type FeaturestoreMonitoringConfig_ThresholdConfig_Value ¶
type FeaturestoreMonitoringConfig_ThresholdConfig_Value = src.FeaturestoreMonitoringConfig_ThresholdConfig_Value
type
FeaturestoreOnlineServingServiceClient
DEPRECATED
type
FeaturestoreOnlineServingServiceServer
DEPRECATED
type FeaturestoreOnlineServingService_StreamingReadFeatureValuesClient ¶
type FeaturestoreOnlineServingService_StreamingReadFeatureValuesClient = src.FeaturestoreOnlineServingService_StreamingReadFeatureValuesClient
type FeaturestoreOnlineServingService_StreamingReadFeatureValuesServer ¶
type FeaturestoreOnlineServingService_StreamingReadFeatureValuesServer = src.FeaturestoreOnlineServingService_StreamingReadFeatureValuesServer
type
FeaturestoreServiceClient
DEPRECATED
type
FeaturestoreServiceServer
DEPRECATED
type
Featurestore_OnlineServingConfig
DEPRECATED
type
Featurestore_OnlineServingConfig_Scaling
DEPRECATED
type
Featurestore_State
DEPRECATED
type
FilterSplit
DEPRECATED
type
FractionSplit
DEPRECATED
type
GcsDestination
DEPRECATED
type
GcsSource
DEPRECATED
type
GenericOperationMetadata
DEPRECATED
type
GetAnnotationSpecRequest
DEPRECATED
type
GetArtifactRequest
DEPRECATED
type
GetBatchPredictionJobRequest
DEPRECATED
type
GetContextRequest
DEPRECATED
type
GetCustomJobRequest
DEPRECATED
type
GetDataLabelingJobRequest
DEPRECATED
type
GetDatasetRequest
DEPRECATED
type
GetEndpointRequest
DEPRECATED
type
GetEntityTypeRequest
DEPRECATED
type
GetExecutionRequest
DEPRECATED
type
GetFeatureRequest
DEPRECATED
type
GetFeaturestoreRequest
DEPRECATED
type
GetHyperparameterTuningJobRequest
DEPRECATED
type
GetIndexEndpointRequest
DEPRECATED
type
GetIndexRequest
DEPRECATED
type
GetMetadataSchemaRequest
DEPRECATED
type
GetMetadataStoreRequest
DEPRECATED
type
GetModelDeploymentMonitoringJobRequest
DEPRECATED
type
GetModelEvaluationRequest
DEPRECATED
type
GetModelEvaluationSliceRequest
DEPRECATED
type
GetModelRequest
DEPRECATED
type
GetPipelineJobRequest
DEPRECATED
type
GetSpecialistPoolRequest
DEPRECATED
type
GetStudyRequest
DEPRECATED
type
GetTensorboardExperimentRequest
DEPRECATED
type
GetTensorboardRequest
DEPRECATED
type
GetTensorboardRunRequest
DEPRECATED
type
GetTensorboardTimeSeriesRequest
DEPRECATED
type
GetTrainingPipelineRequest
DEPRECATED
type
GetTrialRequest
DEPRECATED
type
HyperparameterTuningJob
DEPRECATED
type
IdMatcher
DEPRECATED
type
ImportDataConfig
DEPRECATED
type ImportDataConfig_GcsSource ¶
type ImportDataConfig_GcsSource = src.ImportDataConfig_GcsSource
type
ImportDataOperationMetadata
DEPRECATED
type
ImportDataRequest
DEPRECATED
type
ImportDataResponse
DEPRECATED
type
ImportFeatureValuesOperationMetadata
DEPRECATED
type
ImportFeatureValuesRequest
DEPRECATED
type ImportFeatureValuesRequest_AvroSource ¶
type ImportFeatureValuesRequest_AvroSource = src.ImportFeatureValuesRequest_AvroSource
type ImportFeatureValuesRequest_BigquerySource ¶
type ImportFeatureValuesRequest_BigquerySource = src.ImportFeatureValuesRequest_BigquerySource
type ImportFeatureValuesRequest_CsvSource ¶
type ImportFeatureValuesRequest_CsvSource = src.ImportFeatureValuesRequest_CsvSource
type
ImportFeatureValuesRequest_FeatureSpec
DEPRECATED
type ImportFeatureValuesRequest_FeatureTime ¶
type ImportFeatureValuesRequest_FeatureTime = src.ImportFeatureValuesRequest_FeatureTime
type ImportFeatureValuesRequest_FeatureTimeField ¶
type ImportFeatureValuesRequest_FeatureTimeField = src.ImportFeatureValuesRequest_FeatureTimeField
type
ImportFeatureValuesResponse
DEPRECATED
type
ImportModelEvaluationRequest
DEPRECATED
type
Index
DEPRECATED
type
IndexDatapoint
DEPRECATED
type
IndexDatapoint_CrowdingTag
DEPRECATED
type
IndexDatapoint_Restriction
DEPRECATED
type
IndexEndpoint
DEPRECATED
type
IndexEndpointServiceClient
DEPRECATED
type
IndexEndpointServiceServer
DEPRECATED
type
IndexPrivateEndpoints
DEPRECATED
type
IndexServiceClient
DEPRECATED
type
IndexServiceServer
DEPRECATED
type
IndexStats
DEPRECATED
type
Index_IndexUpdateMethod
DEPRECATED
type
InputDataConfig
DEPRECATED
type InputDataConfig_BigqueryDestination ¶
type InputDataConfig_BigqueryDestination = src.InputDataConfig_BigqueryDestination
type InputDataConfig_FilterSplit ¶
type InputDataConfig_FilterSplit = src.InputDataConfig_FilterSplit
type InputDataConfig_FractionSplit ¶
type InputDataConfig_FractionSplit = src.InputDataConfig_FractionSplit
type InputDataConfig_GcsDestination ¶
type InputDataConfig_GcsDestination = src.InputDataConfig_GcsDestination
type InputDataConfig_PredefinedSplit ¶
type InputDataConfig_PredefinedSplit = src.InputDataConfig_PredefinedSplit
type InputDataConfig_StratifiedSplit ¶
type InputDataConfig_StratifiedSplit = src.InputDataConfig_StratifiedSplit
type InputDataConfig_TimestampSplit ¶
type InputDataConfig_TimestampSplit = src.InputDataConfig_TimestampSplit
type
Int64Array
DEPRECATED
type
IntegratedGradientsAttribution
DEPRECATED
type
JobServiceClient
DEPRECATED
type
JobServiceServer
DEPRECATED
type
JobState
DEPRECATED
type
LineageSubgraph
DEPRECATED
type
ListAnnotationsRequest
DEPRECATED
type
ListAnnotationsResponse
DEPRECATED
type
ListArtifactsRequest
DEPRECATED
type
ListArtifactsResponse
DEPRECATED
type
ListBatchPredictionJobsRequest
DEPRECATED
type
ListBatchPredictionJobsResponse
DEPRECATED
type
ListContextsRequest
DEPRECATED
type
ListContextsResponse
DEPRECATED
type
ListCustomJobsRequest
DEPRECATED
type
ListCustomJobsResponse
DEPRECATED
type
ListDataItemsRequest
DEPRECATED
type
ListDataItemsResponse
DEPRECATED
type
ListDataLabelingJobsRequest
DEPRECATED
type
ListDataLabelingJobsResponse
DEPRECATED
type
ListDatasetsRequest
DEPRECATED
type
ListDatasetsResponse
DEPRECATED
type
ListEndpointsRequest
DEPRECATED
type
ListEndpointsResponse
DEPRECATED
type
ListEntityTypesRequest
DEPRECATED
type
ListEntityTypesResponse
DEPRECATED
type
ListExecutionsRequest
DEPRECATED
type
ListExecutionsResponse
DEPRECATED
type
ListFeaturesRequest
DEPRECATED
type
ListFeaturesResponse
DEPRECATED
type
ListFeaturestoresRequest
DEPRECATED
type
ListFeaturestoresResponse
DEPRECATED
type
ListHyperparameterTuningJobsRequest
DEPRECATED
type
ListHyperparameterTuningJobsResponse
DEPRECATED
type
ListIndexEndpointsRequest
DEPRECATED
type
ListIndexEndpointsResponse
DEPRECATED
type
ListIndexesRequest
DEPRECATED
type
ListIndexesResponse
DEPRECATED
type
ListMetadataSchemasRequest
DEPRECATED
type
ListMetadataSchemasResponse
DEPRECATED
type
ListMetadataStoresRequest
DEPRECATED
type
ListMetadataStoresResponse
DEPRECATED
type
ListModelDeploymentMonitoringJobsRequest
DEPRECATED
type
ListModelDeploymentMonitoringJobsResponse
DEPRECATED
type
ListModelEvaluationSlicesRequest
DEPRECATED
type
ListModelEvaluationSlicesResponse
DEPRECATED
type
ListModelEvaluationsRequest
DEPRECATED
type
ListModelEvaluationsResponse
DEPRECATED
type
ListModelVersionsRequest
DEPRECATED
type
ListModelVersionsResponse
DEPRECATED
type
ListModelsRequest
DEPRECATED
type
ListModelsResponse
DEPRECATED
type
ListOptimalTrialsRequest
DEPRECATED
type
ListOptimalTrialsResponse
DEPRECATED
type
ListPipelineJobsRequest
DEPRECATED
type
ListPipelineJobsResponse
DEPRECATED
type
ListSavedQueriesRequest
DEPRECATED
type
ListSavedQueriesResponse
DEPRECATED
type
ListSpecialistPoolsRequest
DEPRECATED
type
ListSpecialistPoolsResponse
DEPRECATED
type
ListStudiesRequest
DEPRECATED
type
ListStudiesResponse
DEPRECATED
type
ListTensorboardExperimentsRequest
DEPRECATED
type
ListTensorboardExperimentsResponse
DEPRECATED
type
ListTensorboardRunsRequest
DEPRECATED
type
ListTensorboardRunsResponse
DEPRECATED
type
ListTensorboardTimeSeriesRequest
DEPRECATED
type
ListTensorboardTimeSeriesResponse
DEPRECATED
type
ListTensorboardsRequest
DEPRECATED
type
ListTensorboardsResponse
DEPRECATED
type
ListTrainingPipelinesRequest
DEPRECATED
type
ListTrainingPipelinesResponse
DEPRECATED
type
ListTrialsRequest
DEPRECATED
type
ListTrialsResponse
DEPRECATED
type
LookupStudyRequest
DEPRECATED
type
MachineSpec
DEPRECATED
type
ManualBatchTuningParameters
DEPRECATED
type
Measurement
DEPRECATED
type
Measurement_Metric
DEPRECATED
type
MergeVersionAliasesRequest
DEPRECATED
type
MetadataSchema
DEPRECATED
type
MetadataSchema_MetadataSchemaType
DEPRECATED
type
MetadataServiceClient
DEPRECATED
type
MetadataServiceServer
DEPRECATED
type
MetadataStore
DEPRECATED
type
MetadataStore_MetadataStoreState
DEPRECATED
type
MigratableResource
DEPRECATED
type
MigratableResource_AutomlDataset
DEPRECATED
type MigratableResource_AutomlDataset_ ¶
type MigratableResource_AutomlDataset_ = src.MigratableResource_AutomlDataset_
type
MigratableResource_AutomlModel
DEPRECATED
type MigratableResource_AutomlModel_ ¶
type MigratableResource_AutomlModel_ = src.MigratableResource_AutomlModel_
type
MigratableResource_DataLabelingDataset
DEPRECATED
type MigratableResource_DataLabelingDataset_ ¶
type MigratableResource_DataLabelingDataset_ = src.MigratableResource_DataLabelingDataset_
type
MigratableResource_DataLabelingDataset_DataLabelingAnnotatedDataset
DEPRECATED
type
MigratableResource_MlEngineModelVersion
DEPRECATED
type MigratableResource_MlEngineModelVersion_ ¶
type MigratableResource_MlEngineModelVersion_ = src.MigratableResource_MlEngineModelVersion_
type
MigrateResourceRequest
DEPRECATED
type
MigrateResourceRequest_MigrateAutomlDatasetConfig
DEPRECATED
type MigrateResourceRequest_MigrateAutomlDatasetConfig_ ¶
type MigrateResourceRequest_MigrateAutomlDatasetConfig_ = src.MigrateResourceRequest_MigrateAutomlDatasetConfig_
type
MigrateResourceRequest_MigrateAutomlModelConfig
DEPRECATED
type MigrateResourceRequest_MigrateAutomlModelConfig_ ¶
type MigrateResourceRequest_MigrateAutomlModelConfig_ = src.MigrateResourceRequest_MigrateAutomlModelConfig_
type
MigrateResourceRequest_MigrateDataLabelingDatasetConfig
DEPRECATED
type MigrateResourceRequest_MigrateDataLabelingDatasetConfig_ ¶
type MigrateResourceRequest_MigrateDataLabelingDatasetConfig_ = src.MigrateResourceRequest_MigrateDataLabelingDatasetConfig_
type
MigrateResourceRequest_MigrateDataLabelingDatasetConfig_MigrateDataLabelingAnnotatedDatasetConfig
DEPRECATED
type
MigrateResourceRequest_MigrateMlEngineModelVersionConfig
DEPRECATED
type MigrateResourceRequest_MigrateMlEngineModelVersionConfig_ ¶
type MigrateResourceRequest_MigrateMlEngineModelVersionConfig_ = src.MigrateResourceRequest_MigrateMlEngineModelVersionConfig_
type
MigrateResourceResponse
DEPRECATED
type MigrateResourceResponse_Dataset ¶
type MigrateResourceResponse_Dataset = src.MigrateResourceResponse_Dataset
type MigrateResourceResponse_Model ¶
type MigrateResourceResponse_Model = src.MigrateResourceResponse_Model
type
MigrationServiceClient
DEPRECATED
type
MigrationServiceServer
DEPRECATED
type
Model
DEPRECATED
type
ModelContainerSpec
DEPRECATED
type
ModelDeploymentMonitoringBigQueryTable
DEPRECATED
type
ModelDeploymentMonitoringBigQueryTable_LogSource
DEPRECATED
type
ModelDeploymentMonitoringBigQueryTable_LogType
DEPRECATED
type
ModelDeploymentMonitoringJob
DEPRECATED
type
ModelDeploymentMonitoringJob_LatestMonitoringPipelineMetadata
DEPRECATED
type
ModelDeploymentMonitoringJob_MonitoringScheduleState
DEPRECATED
type
ModelDeploymentMonitoringObjectiveConfig
DEPRECATED
type
ModelDeploymentMonitoringObjectiveType
DEPRECATED
type
ModelDeploymentMonitoringScheduleConfig
DEPRECATED
type
ModelEvaluation
DEPRECATED
type
ModelEvaluationSlice
DEPRECATED
type
ModelEvaluationSlice_Slice
DEPRECATED
type ModelEvaluation_ModelEvaluationExplanationSpec ¶
type ModelEvaluation_ModelEvaluationExplanationSpec = src.ModelEvaluation_ModelEvaluationExplanationSpec
type
ModelExplanation
DEPRECATED
type ModelMonitoringAlertConfig ¶
type ModelMonitoringAlertConfig = src.ModelMonitoringAlertConfig
type
ModelMonitoringAlertConfig_EmailAlertConfig
DEPRECATED
type ModelMonitoringAlertConfig_EmailAlertConfig_ ¶
type ModelMonitoringAlertConfig_EmailAlertConfig_ = src.ModelMonitoringAlertConfig_EmailAlertConfig_
type
ModelMonitoringObjectiveConfig
DEPRECATED
type
ModelMonitoringObjectiveConfig_ExplanationConfig
DEPRECATED
type
ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline
DEPRECATED
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Bigquery ¶
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Bigquery = src.ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Bigquery
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Gcs ¶
type ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Gcs = src.ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_Gcs
type
ModelMonitoringObjectiveConfig_ExplanationConfig_ExplanationBaseline_PredictionFormat
DEPRECATED
type
ModelMonitoringObjectiveConfig_PredictionDriftDetectionConfig
DEPRECATED
type
ModelMonitoringObjectiveConfig_TrainingDataset
DEPRECATED
type ModelMonitoringObjectiveConfig_TrainingDataset_BigquerySource ¶
type ModelMonitoringObjectiveConfig_TrainingDataset_BigquerySource = src.ModelMonitoringObjectiveConfig_TrainingDataset_BigquerySource
type ModelMonitoringObjectiveConfig_TrainingDataset_Dataset ¶
type ModelMonitoringObjectiveConfig_TrainingDataset_Dataset = src.ModelMonitoringObjectiveConfig_TrainingDataset_Dataset
type ModelMonitoringObjectiveConfig_TrainingDataset_GcsSource ¶
type ModelMonitoringObjectiveConfig_TrainingDataset_GcsSource = src.ModelMonitoringObjectiveConfig_TrainingDataset_GcsSource
type
ModelMonitoringObjectiveConfig_TrainingPredictionSkewDetectionConfig
DEPRECATED
type
ModelMonitoringStatsAnomalies
DEPRECATED
type
ModelMonitoringStatsAnomalies_FeatureHistoricStatsAnomalies
DEPRECATED
type
ModelServiceClient
DEPRECATED
type
ModelServiceServer
DEPRECATED
type
ModelSourceInfo
DEPRECATED
type
ModelSourceInfo_ModelSourceType
DEPRECATED
type
Model_DeploymentResourcesType
DEPRECATED
type
Model_ExportFormat
DEPRECATED
type
Model_ExportFormat_ExportableContent
DEPRECATED
type
MutateDeployedIndexOperationMetadata
DEPRECATED
type
MutateDeployedIndexRequest
DEPRECATED
type
MutateDeployedIndexResponse
DEPRECATED
type
NearestNeighborSearchOperationMetadata
DEPRECATED
type NearestNeighborSearchOperationMetadata_ContentValidationStats ¶
type NearestNeighborSearchOperationMetadata_ContentValidationStats = src.NearestNeighborSearchOperationMetadata_ContentValidationStats
type NearestNeighborSearchOperationMetadata_RecordError ¶
type NearestNeighborSearchOperationMetadata_RecordError = src.NearestNeighborSearchOperationMetadata_RecordError
type NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType ¶
type NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType = src.NearestNeighborSearchOperationMetadata_RecordError_RecordErrorType
type
Neighbor
DEPRECATED
type
NfsMount
DEPRECATED
type
PauseModelDeploymentMonitoringJobRequest
DEPRECATED
type
PipelineFailurePolicy
DEPRECATED
type
PipelineJob
DEPRECATED
type
PipelineJobDetail
DEPRECATED
type
PipelineJob_RuntimeConfig
DEPRECATED
type
PipelineJob_RuntimeConfig_InputArtifact
DEPRECATED
type PipelineJob_RuntimeConfig_InputArtifact_ArtifactId ¶
type PipelineJob_RuntimeConfig_InputArtifact_ArtifactId = src.PipelineJob_RuntimeConfig_InputArtifact_ArtifactId
type
PipelineServiceClient
DEPRECATED
type
PipelineServiceServer
DEPRECATED
type
PipelineState
DEPRECATED
type
PipelineTaskDetail
DEPRECATED
type
PipelineTaskDetail_ArtifactList
DEPRECATED
type
PipelineTaskDetail_PipelineTaskStatus
DEPRECATED
type
PipelineTaskDetail_State
DEPRECATED
type
PipelineTaskExecutorDetail
DEPRECATED
type
PipelineTaskExecutorDetail_ContainerDetail
DEPRECATED
type PipelineTaskExecutorDetail_ContainerDetail_ ¶
type PipelineTaskExecutorDetail_ContainerDetail_ = src.PipelineTaskExecutorDetail_ContainerDetail_
type
PipelineTaskExecutorDetail_CustomJobDetail
DEPRECATED
type PipelineTaskExecutorDetail_CustomJobDetail_ ¶
type PipelineTaskExecutorDetail_CustomJobDetail_ = src.PipelineTaskExecutorDetail_CustomJobDetail_
type
PipelineTemplateMetadata
DEPRECATED
type
Port
DEPRECATED
type
PredefinedSplit
DEPRECATED
type
PredictRequest
DEPRECATED
type
PredictRequestResponseLoggingConfig
DEPRECATED
type
PredictResponse
DEPRECATED
type
PredictSchemata
DEPRECATED
type
PredictionServiceClient
DEPRECATED
type
PredictionServiceServer
DEPRECATED
type
PrivateEndpoints
DEPRECATED
type
PurgeArtifactsMetadata
DEPRECATED
type
PurgeArtifactsRequest
DEPRECATED
type
PurgeArtifactsResponse
DEPRECATED
type
PurgeContextsMetadata
DEPRECATED
type
PurgeContextsRequest
DEPRECATED
type
PurgeContextsResponse
DEPRECATED
type
PurgeExecutionsMetadata
DEPRECATED
type
PurgeExecutionsRequest
DEPRECATED
type
PurgeExecutionsResponse
DEPRECATED
type
PythonPackageSpec
DEPRECATED
type
QueryArtifactLineageSubgraphRequest
DEPRECATED
type
QueryContextLineageSubgraphRequest
DEPRECATED
type
QueryExecutionInputsAndOutputsRequest
DEPRECATED
type
RawPredictRequest
DEPRECATED
type
ReadFeatureValuesRequest
DEPRECATED
type
ReadFeatureValuesResponse
DEPRECATED
type
ReadFeatureValuesResponse_EntityView
DEPRECATED
type
ReadFeatureValuesResponse_EntityView_Data
DEPRECATED
type ReadFeatureValuesResponse_EntityView_Data_Value ¶
type ReadFeatureValuesResponse_EntityView_Data_Value = src.ReadFeatureValuesResponse_EntityView_Data_Value
type ReadFeatureValuesResponse_EntityView_Data_Values ¶
type ReadFeatureValuesResponse_EntityView_Data_Values = src.ReadFeatureValuesResponse_EntityView_Data_Values
type
ReadFeatureValuesResponse_FeatureDescriptor
DEPRECATED
type
ReadFeatureValuesResponse_Header
DEPRECATED
type
ReadTensorboardBlobDataRequest
DEPRECATED
type
ReadTensorboardBlobDataResponse
DEPRECATED
type
ReadTensorboardTimeSeriesDataRequest
DEPRECATED
type
ReadTensorboardTimeSeriesDataResponse
DEPRECATED
type
RemoveContextChildrenRequest
DEPRECATED
type
RemoveContextChildrenResponse
DEPRECATED
type
RemoveDatapointsRequest
DEPRECATED
type
RemoveDatapointsResponse
DEPRECATED
type
ResourcesConsumed
DEPRECATED
type
ResumeModelDeploymentMonitoringJobRequest
DEPRECATED
type
SampleConfig
DEPRECATED
type SampleConfig_FollowingBatchSamplePercentage ¶
type SampleConfig_FollowingBatchSamplePercentage = src.SampleConfig_FollowingBatchSamplePercentage
type SampleConfig_InitialBatchSamplePercentage ¶
type SampleConfig_InitialBatchSamplePercentage = src.SampleConfig_InitialBatchSamplePercentage
type
SampleConfig_SampleStrategy
DEPRECATED
type
SampledShapleyAttribution
DEPRECATED
type
SamplingStrategy
DEPRECATED
type
SamplingStrategy_RandomSampleConfig
DEPRECATED
type
SavedQuery
DEPRECATED
type
Scalar
DEPRECATED
type
Scheduling
DEPRECATED
type
SearchFeaturesRequest
DEPRECATED
type
SearchFeaturesResponse
DEPRECATED
type
SearchMigratableResourcesRequest
DEPRECATED
type
SearchMigratableResourcesResponse
DEPRECATED
type
SearchModelDeploymentMonitoringStatsAnomaliesRequest
DEPRECATED
type
SearchModelDeploymentMonitoringStatsAnomaliesRequest_StatsAnomaliesObjective
DEPRECATED
type
SearchModelDeploymentMonitoringStatsAnomaliesResponse
DEPRECATED
type
SmoothGradConfig
DEPRECATED
type SmoothGradConfig_FeatureNoiseSigma ¶
type SmoothGradConfig_FeatureNoiseSigma = src.SmoothGradConfig_FeatureNoiseSigma
type SmoothGradConfig_NoiseSigma ¶
type SmoothGradConfig_NoiseSigma = src.SmoothGradConfig_NoiseSigma
type
SpecialistPool
DEPRECATED
type
SpecialistPoolServiceClient
DEPRECATED
type
SpecialistPoolServiceServer
DEPRECATED
type
StopTrialRequest
DEPRECATED
type
StratifiedSplit
DEPRECATED
type
StreamingReadFeatureValuesRequest
DEPRECATED
type
StringArray
DEPRECATED
type
Study
DEPRECATED
type
StudySpec
DEPRECATED
type
StudySpec_Algorithm
DEPRECATED
type
StudySpec_ConvexAutomatedStoppingSpec
DEPRECATED
type StudySpec_ConvexAutomatedStoppingSpec_ ¶
type StudySpec_ConvexAutomatedStoppingSpec_ = src.StudySpec_ConvexAutomatedStoppingSpec_
type
StudySpec_DecayCurveAutomatedStoppingSpec
DEPRECATED
type StudySpec_DecayCurveStoppingSpec ¶
type StudySpec_DecayCurveStoppingSpec = src.StudySpec_DecayCurveStoppingSpec
type
StudySpec_MeasurementSelectionType
DEPRECATED
type
StudySpec_MedianAutomatedStoppingSpec
DEPRECATED
type StudySpec_MedianAutomatedStoppingSpec_ ¶
type StudySpec_MedianAutomatedStoppingSpec_ = src.StudySpec_MedianAutomatedStoppingSpec_
type
StudySpec_MetricSpec
DEPRECATED
type
StudySpec_MetricSpec_GoalType
DEPRECATED
type
StudySpec_ObservationNoise
DEPRECATED
type
StudySpec_ParameterSpec
DEPRECATED
type
StudySpec_ParameterSpec_CategoricalValueSpec
DEPRECATED
type StudySpec_ParameterSpec_CategoricalValueSpec_ ¶
type StudySpec_ParameterSpec_CategoricalValueSpec_ = src.StudySpec_ParameterSpec_CategoricalValueSpec_
type
StudySpec_ParameterSpec_ConditionalParameterSpec
DEPRECATED
type
StudySpec_ParameterSpec_ConditionalParameterSpec_CategoricalValueCondition
DEPRECATED
type
StudySpec_ParameterSpec_ConditionalParameterSpec_DiscreteValueCondition
DEPRECATED
type
StudySpec_ParameterSpec_ConditionalParameterSpec_IntValueCondition
DEPRECATED
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentCategoricalValues ¶
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentCategoricalValues = src.StudySpec_ParameterSpec_ConditionalParameterSpec_ParentCategoricalValues
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentDiscreteValues ¶
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentDiscreteValues = src.StudySpec_ParameterSpec_ConditionalParameterSpec_ParentDiscreteValues
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentIntValues ¶
type StudySpec_ParameterSpec_ConditionalParameterSpec_ParentIntValues = src.StudySpec_ParameterSpec_ConditionalParameterSpec_ParentIntValues
type
StudySpec_ParameterSpec_DiscreteValueSpec
DEPRECATED
type StudySpec_ParameterSpec_DiscreteValueSpec_ ¶
type StudySpec_ParameterSpec_DiscreteValueSpec_ = src.StudySpec_ParameterSpec_DiscreteValueSpec_
type
StudySpec_ParameterSpec_DoubleValueSpec
DEPRECATED
type StudySpec_ParameterSpec_DoubleValueSpec_ ¶
type StudySpec_ParameterSpec_DoubleValueSpec_ = src.StudySpec_ParameterSpec_DoubleValueSpec_
type
StudySpec_ParameterSpec_IntegerValueSpec
DEPRECATED
type StudySpec_ParameterSpec_IntegerValueSpec_ ¶
type StudySpec_ParameterSpec_IntegerValueSpec_ = src.StudySpec_ParameterSpec_IntegerValueSpec_
type
StudySpec_ParameterSpec_ScaleType
DEPRECATED
type
Study_State
DEPRECATED
type
SuggestTrialsMetadata
DEPRECATED
type
SuggestTrialsRequest
DEPRECATED
type
SuggestTrialsResponse
DEPRECATED
type
TFRecordDestination
DEPRECATED
type
Tensorboard
DEPRECATED
type
TensorboardBlob
DEPRECATED
type
TensorboardBlobSequence
DEPRECATED
type
TensorboardExperiment
DEPRECATED
type
TensorboardRun
DEPRECATED
type
TensorboardServiceClient
DEPRECATED
type
TensorboardServiceServer
DEPRECATED
type TensorboardService_ReadTensorboardBlobDataClient ¶
type TensorboardService_ReadTensorboardBlobDataClient = src.TensorboardService_ReadTensorboardBlobDataClient
type TensorboardService_ReadTensorboardBlobDataServer ¶
type TensorboardService_ReadTensorboardBlobDataServer = src.TensorboardService_ReadTensorboardBlobDataServer
type
TensorboardTensor
DEPRECATED
type
TensorboardTimeSeries
DEPRECATED
type
TensorboardTimeSeries_Metadata
DEPRECATED
type
TensorboardTimeSeries_ValueType
DEPRECATED
type
ThresholdConfig
DEPRECATED
type ThresholdConfig_Value ¶
type ThresholdConfig_Value = src.ThresholdConfig_Value
type
TimeSeriesData
DEPRECATED
type
TimeSeriesDataPoint
DEPRECATED
type TimeSeriesDataPoint_Blobs ¶
type TimeSeriesDataPoint_Blobs = src.TimeSeriesDataPoint_Blobs
type TimeSeriesDataPoint_Scalar ¶
type TimeSeriesDataPoint_Scalar = src.TimeSeriesDataPoint_Scalar
type TimeSeriesDataPoint_Tensor ¶
type TimeSeriesDataPoint_Tensor = src.TimeSeriesDataPoint_Tensor
type
TimestampSplit
DEPRECATED
type
TrainingConfig
DEPRECATED
type
TrainingPipeline
DEPRECATED
type
Trial
DEPRECATED
type
Trial_Parameter
DEPRECATED
type
Trial_State
DEPRECATED
type
UndeployIndexOperationMetadata
DEPRECATED
type
UndeployIndexRequest
DEPRECATED
type
UndeployIndexResponse
DEPRECATED
type
UndeployModelOperationMetadata
DEPRECATED
type
UndeployModelRequest
DEPRECATED
type
UndeployModelResponse
DEPRECATED
type
UnimplementedDatasetServiceServer
DEPRECATED
type
UnimplementedEndpointServiceServer
DEPRECATED
type
UnimplementedFeaturestoreOnlineServingServiceServer
DEPRECATED
type
UnimplementedFeaturestoreServiceServer
DEPRECATED
type
UnimplementedIndexEndpointServiceServer
DEPRECATED
type
UnimplementedIndexServiceServer
DEPRECATED
type
UnimplementedJobServiceServer
DEPRECATED
type
UnimplementedMetadataServiceServer
DEPRECATED
type
UnimplementedMigrationServiceServer
DEPRECATED
type
UnimplementedModelServiceServer
DEPRECATED
type
UnimplementedPipelineServiceServer
DEPRECATED
type
UnimplementedPredictionServiceServer
DEPRECATED
type
UnimplementedSpecialistPoolServiceServer
DEPRECATED
type
UnimplementedTensorboardServiceServer
DEPRECATED
type
UnimplementedVizierServiceServer
DEPRECATED
type
UnmanagedContainerModel
DEPRECATED
type
UpdateArtifactRequest
DEPRECATED
type
UpdateContextRequest
DEPRECATED
type
UpdateDatasetRequest
DEPRECATED
type
UpdateEndpointRequest
DEPRECATED
type
UpdateEntityTypeRequest
DEPRECATED
type
UpdateExecutionRequest
DEPRECATED
type
UpdateFeatureRequest
DEPRECATED
type
UpdateFeaturestoreOperationMetadata
DEPRECATED
type
UpdateFeaturestoreRequest
DEPRECATED
type
UpdateIndexEndpointRequest
DEPRECATED
type
UpdateIndexOperationMetadata
DEPRECATED
type
UpdateIndexRequest
DEPRECATED
type
UpdateModelDeploymentMonitoringJobOperationMetadata
DEPRECATED
type
UpdateModelDeploymentMonitoringJobRequest
DEPRECATED
type
UpdateModelRequest
DEPRECATED
type
UpdateSpecialistPoolOperationMetadata
DEPRECATED
type
UpdateSpecialistPoolRequest
DEPRECATED
type
UpdateTensorboardExperimentRequest
DEPRECATED
type
UpdateTensorboardOperationMetadata
DEPRECATED
type
UpdateTensorboardRequest
DEPRECATED
type
UpdateTensorboardRunRequest
DEPRECATED
type
UpdateTensorboardTimeSeriesRequest
DEPRECATED
type
UploadModelOperationMetadata
DEPRECATED
type
UploadModelRequest
DEPRECATED
type
UploadModelResponse
DEPRECATED
type
UpsertDatapointsRequest
DEPRECATED
type
UpsertDatapointsResponse
DEPRECATED
type
UserActionReference
DEPRECATED
type UserActionReference_DataLabelingJob ¶
type UserActionReference_DataLabelingJob = src.UserActionReference_DataLabelingJob
type UserActionReference_Operation ¶
type UserActionReference_Operation = src.UserActionReference_Operation
type
Value
DEPRECATED
type Value_DoubleValue ¶
type Value_DoubleValue = src.Value_DoubleValue
type Value_IntValue ¶
type Value_IntValue = src.Value_IntValue
type Value_StringValue ¶
type Value_StringValue = src.Value_StringValue
type
VizierServiceClient
DEPRECATED
type
VizierServiceServer
DEPRECATED
type
WorkerPoolSpec
DEPRECATED
type WorkerPoolSpec_ContainerSpec ¶
type WorkerPoolSpec_ContainerSpec = src.WorkerPoolSpec_ContainerSpec
type WorkerPoolSpec_PythonPackageSpec ¶
type WorkerPoolSpec_PythonPackageSpec = src.WorkerPoolSpec_PythonPackageSpec
type
WriteFeatureValuesPayload
DEPRECATED
type
WriteFeatureValuesRequest
DEPRECATED
type
WriteFeatureValuesResponse
DEPRECATED
type
WriteTensorboardExperimentDataRequest
DEPRECATED
type
WriteTensorboardExperimentDataResponse
DEPRECATED
type
WriteTensorboardRunDataRequest
DEPRECATED
type
WriteTensorboardRunDataResponse
DEPRECATED
type
XraiAttribution
DEPRECATED
 Source Files ¶
View all Source files
alias.go
 Directories ¶
Expand all
schema
	
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
