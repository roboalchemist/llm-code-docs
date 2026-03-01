# Source: https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1

Title: automl package - google.golang.org/genproto/googleapis/cloud/automl/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1

Markdown Content:
Package automl aliases all exported identifiers in package "cloud.google.com/go/automl/apiv1/automlpb".

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb. Please read [https://github.com/googleapis/google-cloud-go/blob/main/migration.md](https://github.com/googleapis/google-cloud-go/blob/main/migration.md) for more details.

*   [Constants](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#pkg-constants)
*   [Variables](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#pkg-variables)
*   [func RegisterAutoMlServer(s *grpc.Server, srv AutoMlServer)](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#RegisterAutoMlServer)deprecated
*   [func RegisterPredictionServiceServer(s *grpc.Server, srv PredictionServiceServer)](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#RegisterPredictionServiceServer)deprecated
*   [type AnnotationPayload](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AnnotationPayload)deprecated
*   [type AnnotationPayload_Classification](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AnnotationPayload_Classification)
*   [type AnnotationPayload_ImageObjectDetection](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AnnotationPayload_ImageObjectDetection)
*   [type AnnotationPayload_TextExtraction](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AnnotationPayload_TextExtraction)
*   [type AnnotationPayload_TextSentiment](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AnnotationPayload_TextSentiment)
*   [type AnnotationPayload_Translation](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AnnotationPayload_Translation)
*   [type AnnotationSpec](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AnnotationSpec)deprecated
*   [type AutoMlClient](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AutoMlClient)deprecated
*       *   [func NewAutoMlClient(cc grpc.ClientConnInterface) AutoMlClient](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#NewAutoMlClient)deprecated

*   [type AutoMlServer](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#AutoMlServer)deprecated
*   [type BatchPredictInputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictInputConfig)deprecated
*   [type BatchPredictInputConfig_GcsSource](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictInputConfig_GcsSource)
*   [type BatchPredictOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictOperationMetadata)deprecated
*   [type BatchPredictOperationMetadata_BatchPredictOutputInfo](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictOperationMetadata_BatchPredictOutputInfo)deprecated
*   [type BatchPredictOperationMetadata_BatchPredictOutputInfo_GcsOutputDirectory](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictOperationMetadata_BatchPredictOutputInfo_GcsOutputDirectory)
*   [type BatchPredictOutputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictOutputConfig)deprecated
*   [type BatchPredictOutputConfig_GcsDestination](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictOutputConfig_GcsDestination)
*   [type BatchPredictRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictRequest)deprecated
*   [type BatchPredictResult](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictResult)deprecated
*   [type BoundingBoxMetricsEntry](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BoundingBoxMetricsEntry)deprecated
*   [type BoundingBoxMetricsEntry_ConfidenceMetricsEntry](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BoundingBoxMetricsEntry_ConfidenceMetricsEntry)deprecated
*   [type BoundingPoly](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BoundingPoly)deprecated
*   [type ClassificationAnnotation](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ClassificationAnnotation)deprecated
*   [type ClassificationEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ClassificationEvaluationMetrics)deprecated
*   [type ClassificationEvaluationMetrics_ConfidenceMetricsEntry](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ClassificationEvaluationMetrics_ConfidenceMetricsEntry)deprecated
*   [type ClassificationEvaluationMetrics_ConfusionMatrix](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ClassificationEvaluationMetrics_ConfusionMatrix)deprecated
*   [type ClassificationEvaluationMetrics_ConfusionMatrix_Row](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ClassificationEvaluationMetrics_ConfusionMatrix_Row)deprecated
*   [type ClassificationType](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ClassificationType)deprecated
*   [type CreateDatasetOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#CreateDatasetOperationMetadata)deprecated
*   [type CreateDatasetRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#CreateDatasetRequest)deprecated
*   [type CreateModelOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#CreateModelOperationMetadata)deprecated
*   [type CreateModelRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#CreateModelRequest)deprecated
*   [type Dataset](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Dataset)deprecated
*   [type Dataset_ImageClassificationDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Dataset_ImageClassificationDatasetMetadata)
*   [type Dataset_ImageObjectDetectionDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Dataset_ImageObjectDetectionDatasetMetadata)
*   [type Dataset_TextClassificationDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Dataset_TextClassificationDatasetMetadata)
*   [type Dataset_TextExtractionDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Dataset_TextExtractionDatasetMetadata)
*   [type Dataset_TextSentimentDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Dataset_TextSentimentDatasetMetadata)
*   [type Dataset_TranslationDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Dataset_TranslationDatasetMetadata)
*   [type DeleteDatasetRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DeleteDatasetRequest)deprecated
*   [type DeleteModelRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DeleteModelRequest)deprecated
*   [type DeleteOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DeleteOperationMetadata)deprecated
*   [type DeployModelOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DeployModelOperationMetadata)deprecated
*   [type DeployModelRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DeployModelRequest)deprecated
*   [type DeployModelRequest_ImageClassificationModelDeploymentMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DeployModelRequest_ImageClassificationModelDeploymentMetadata)
*   [type DeployModelRequest_ImageObjectDetectionModelDeploymentMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DeployModelRequest_ImageObjectDetectionModelDeploymentMetadata)
*   [type Document](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Document)deprecated
*   [type DocumentDimensions](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DocumentDimensions)deprecated
*   [type DocumentDimensions_DocumentDimensionUnit](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DocumentDimensions_DocumentDimensionUnit)deprecated
*   [type DocumentInputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#DocumentInputConfig)deprecated
*   [type Document_Layout](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Document_Layout)deprecated
*   [type Document_Layout_TextSegmentType](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Document_Layout_TextSegmentType)deprecated
*   [type ExamplePayload](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExamplePayload)deprecated
*   [type ExamplePayload_Document](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExamplePayload_Document)
*   [type ExamplePayload_Image](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExamplePayload_Image)
*   [type ExamplePayload_TextSnippet](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExamplePayload_TextSnippet)
*   [type ExportDataOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExportDataOperationMetadata)deprecated
*   [type ExportDataOperationMetadata_ExportDataOutputInfo](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExportDataOperationMetadata_ExportDataOutputInfo)deprecated
*   [type ExportDataOperationMetadata_ExportDataOutputInfo_GcsOutputDirectory](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExportDataOperationMetadata_ExportDataOutputInfo_GcsOutputDirectory)
*   [type ExportDataRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExportDataRequest)deprecated
*   [type ExportModelOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExportModelOperationMetadata)deprecated
*   [type ExportModelOperationMetadata_ExportModelOutputInfo](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExportModelOperationMetadata_ExportModelOutputInfo)deprecated
*   [type ExportModelRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ExportModelRequest)deprecated
*   [type GcsDestination](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#GcsDestination)deprecated
*   [type GcsSource](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#GcsSource)deprecated
*   [type GetAnnotationSpecRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#GetAnnotationSpecRequest)deprecated
*   [type GetDatasetRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#GetDatasetRequest)deprecated
*   [type GetModelEvaluationRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#GetModelEvaluationRequest)deprecated
*   [type GetModelRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#GetModelRequest)deprecated
*   [type Image](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Image)deprecated
*   [type ImageClassificationDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageClassificationDatasetMetadata)deprecated
*   [type ImageClassificationModelDeploymentMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageClassificationModelDeploymentMetadata)deprecated
*   [type ImageClassificationModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageClassificationModelMetadata)deprecated
*   [type ImageObjectDetectionAnnotation](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageObjectDetectionAnnotation)deprecated
*   [type ImageObjectDetectionDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageObjectDetectionDatasetMetadata)deprecated
*   [type ImageObjectDetectionEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageObjectDetectionEvaluationMetrics)deprecated
*   [type ImageObjectDetectionModelDeploymentMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageObjectDetectionModelDeploymentMetadata)deprecated
*   [type ImageObjectDetectionModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImageObjectDetectionModelMetadata)deprecated
*   [type Image_ImageBytes](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Image_ImageBytes)
*   [type ImportDataOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImportDataOperationMetadata)deprecated
*   [type ImportDataRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ImportDataRequest)deprecated
*   [type InputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#InputConfig)deprecated
*   [type InputConfig_GcsSource](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#InputConfig_GcsSource)
*   [type ListDatasetsRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ListDatasetsRequest)deprecated
*   [type ListDatasetsResponse](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ListDatasetsResponse)deprecated
*   [type ListModelEvaluationsRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ListModelEvaluationsRequest)deprecated
*   [type ListModelEvaluationsResponse](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ListModelEvaluationsResponse)deprecated
*   [type ListModelsRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ListModelsRequest)deprecated
*   [type ListModelsResponse](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ListModelsResponse)deprecated
*   [type Model](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model)deprecated
*   [type ModelEvaluation](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelEvaluation)deprecated
*   [type ModelEvaluation_ClassificationEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelEvaluation_ClassificationEvaluationMetrics)
*   [type ModelEvaluation_ImageObjectDetectionEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelEvaluation_ImageObjectDetectionEvaluationMetrics)
*   [type ModelEvaluation_TextExtractionEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelEvaluation_TextExtractionEvaluationMetrics)
*   [type ModelEvaluation_TextSentimentEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelEvaluation_TextSentimentEvaluationMetrics)
*   [type ModelEvaluation_TranslationEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelEvaluation_TranslationEvaluationMetrics)
*   [type ModelExportOutputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelExportOutputConfig)deprecated
*   [type ModelExportOutputConfig_GcsDestination](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelExportOutputConfig_GcsDestination)
*   [type Model_DeploymentState](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model_DeploymentState)deprecated
*   [type Model_ImageClassificationModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model_ImageClassificationModelMetadata)
*   [type Model_ImageObjectDetectionModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model_ImageObjectDetectionModelMetadata)
*   [type Model_TextClassificationModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model_TextClassificationModelMetadata)
*   [type Model_TextExtractionModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model_TextExtractionModelMetadata)
*   [type Model_TextSentimentModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model_TextSentimentModelMetadata)
*   [type Model_TranslationModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Model_TranslationModelMetadata)
*   [type NormalizedVertex](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#NormalizedVertex)deprecated
*   [type OperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata)deprecated
*   [type OperationMetadata_BatchPredictDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_BatchPredictDetails)
*   [type OperationMetadata_CreateDatasetDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_CreateDatasetDetails)
*   [type OperationMetadata_CreateModelDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_CreateModelDetails)
*   [type OperationMetadata_DeleteDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_DeleteDetails)
*   [type OperationMetadata_DeployModelDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_DeployModelDetails)
*   [type OperationMetadata_ExportDataDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_ExportDataDetails)
*   [type OperationMetadata_ExportModelDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_ExportModelDetails)
*   [type OperationMetadata_ImportDataDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_ImportDataDetails)
*   [type OperationMetadata_UndeployModelDetails](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OperationMetadata_UndeployModelDetails)
*   [type OutputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OutputConfig)deprecated
*   [type OutputConfig_GcsDestination](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OutputConfig_GcsDestination)
*   [type PredictRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#PredictRequest)deprecated
*   [type PredictResponse](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#PredictResponse)deprecated
*   [type PredictionServiceClient](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#PredictionServiceClient)deprecated
*       *   [func NewPredictionServiceClient(cc grpc.ClientConnInterface) PredictionServiceClient](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#NewPredictionServiceClient)deprecated

*   [type PredictionServiceServer](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#PredictionServiceServer)deprecated
*   [type TextClassificationDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextClassificationDatasetMetadata)deprecated
*   [type TextClassificationModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextClassificationModelMetadata)deprecated
*   [type TextExtractionAnnotation](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextExtractionAnnotation)deprecated
*   [type TextExtractionAnnotation_TextSegment](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextExtractionAnnotation_TextSegment)
*   [type TextExtractionDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextExtractionDatasetMetadata)deprecated
*   [type TextExtractionEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextExtractionEvaluationMetrics)deprecated
*   [type TextExtractionEvaluationMetrics_ConfidenceMetricsEntry](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextExtractionEvaluationMetrics_ConfidenceMetricsEntry)deprecated
*   [type TextExtractionModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextExtractionModelMetadata)deprecated
*   [type TextSegment](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextSegment)deprecated
*   [type TextSentimentAnnotation](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextSentimentAnnotation)deprecated
*   [type TextSentimentDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextSentimentDatasetMetadata)deprecated
*   [type TextSentimentEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextSentimentEvaluationMetrics)deprecated
*   [type TextSentimentModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextSentimentModelMetadata)deprecated
*   [type TextSnippet](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TextSnippet)deprecated
*   [type TranslationAnnotation](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TranslationAnnotation)deprecated
*   [type TranslationDatasetMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TranslationDatasetMetadata)deprecated
*   [type TranslationEvaluationMetrics](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TranslationEvaluationMetrics)deprecated
*   [type TranslationModelMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#TranslationModelMetadata)deprecated
*   [type UndeployModelOperationMetadata](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#UndeployModelOperationMetadata)deprecated
*   [type UndeployModelRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#UndeployModelRequest)deprecated
*   [type UnimplementedAutoMlServer](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#UnimplementedAutoMlServer)deprecated
*   [type UnimplementedPredictionServiceServer](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#UnimplementedPredictionServiceServer)deprecated
*   [type UpdateDatasetRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#UpdateDatasetRequest)deprecated
*   [type UpdateModelRequest](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#UpdateModelRequest)deprecated

Deprecated: Please use consts in: cloud.google.com/go/automl/apiv1/automlpb

Deprecated: Please use vars in: cloud.google.com/go/automl/apiv1/automlpb

Deprecated: Please use funcs in: cloud.google.com/go/automl/apiv1/automlpb

Deprecated: Please use funcs in: cloud.google.com/go/automl/apiv1/automlpb

Contains annotation information that is relevant to AutoML.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A definition of an annotation spec.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

AutoMlClient is the client API for AutoMl service. For semantics around ctx use and closing/ending streaming RPCs, please refer to [https://godoc.org/google.golang.org/grpc#ClientConn.NewStream](https://godoc.org/google.golang.org/grpc#ClientConn.NewStream).

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Deprecated: Please use funcs in: cloud.google.com/go/automl/apiv1/automlpb

AutoMlServer is the server API for AutoMl service.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Input configuration for BatchPredict Action. The format of input depends on the ML problem of the model used for prediction. As input source the [gcs_source][google.cloud.automl.v1.InputConfig.gcs_source] is expected, unless specified otherwise. The formats are represented in EBNF with commas being literal and with non-terminal symbols defined near the end of this comment. The formats are: <h4>AutoML Vision</h4><div class="ds-selector-tabs"><section><h5>Classification</h5> One or more CSV files where each line is a single column: GCS_FILE_PATH The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. This path is treated as the ID in the batch predict output. Sample rows: gs://folder/image1.jpeg gs://folder/image2.gif gs://folder/image3.png </section><section><h5>Object Detection</h5> One or more CSV files where each line is a single column: GCS_FILE_PATH The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. This path is treated as the ID in the batch predict output. Sample rows: gs://folder/image1.jpeg gs://folder/image2.gif gs://folder/image3.png </section></div><h4>AutoML Video Intelligence</h4><div class="ds-selector-tabs"><section><h5>Classification</h5> One or more CSV files where each line is a single column: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END `GCS_FILE_PATH` is the Google Cloud Storage location of video up to 50GB in size and up to 3h in duration duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. `TIME_SEGMENT_START` and `TIME_SEGMENT_END` must be within the length of the video, and the end time must be after the start time. Sample rows: gs://folder/video1.mp4,10,40 gs://folder/video1.mp4,20,60 gs://folder/vid2.mov,0,inf </section><section><h5>Object Tracking</h5> One or more CSV files where each line is a single column: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END `GCS_FILE_PATH` is the Google Cloud Storage location of video up to 50GB in size and up to 3h in duration duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. `TIME_SEGMENT_START` and `TIME_SEGMENT_END` must be within the length of the video, and the end time must be after the start time. Sample rows: gs://folder/video1.mp4,10,40 gs://folder/video1.mp4,20,60 gs://folder/vid2.mov,0,inf </section></div><h4>AutoML Natural Language</h4><div class="ds-selector-tabs"><section><h5>Classification</h5> One or more CSV files where each line is a single column: GCS_FILE_PATH `GCS_FILE_PATH` is the Google Cloud Storage location of a text file. Supported file extensions: .TXT, .PDF, .TIF, .TIFF Text files can be no larger than 10MB in size. Sample rows: gs://folder/text1.txt gs://folder/text2.pdf gs://folder/text3.tif </section><section><h5>Sentiment Analysis</h5> One or more CSV files where each line is a single column: GCS_FILE_PATH `GCS_FILE_PATH` is the Google Cloud Storage location of a text file. Supported file extensions: .TXT, .PDF, .TIF, .TIFF Text files can be no larger than 128kB in size. Sample rows: gs://folder/text1.txt gs://folder/text2.pdf gs://folder/text3.tif </section><section><h5>Entity Extraction</h5> One or more JSONL (JSON Lines) files that either provide inline text or documents. You can only use one format, either inline text or documents, for a single call to [AutoMl.BatchPredict]. Each JSONL file contains a per line a proto that wraps a temporary user-assigned TextSnippet ID (string up to 2000 characters long) called "id", a TextSnippet proto (in JSON representation) and zero or more TextFeature protos. Any given text snippet content must have 30,000 characters or less, and also be UTF-8 NFC encoded (ASCII already is). The IDs provided should be unique. Each document JSONL file contains, per line, a proto that wraps a Document proto with `input_config` set. Each document cannot exceed 2MB in size. Supported document extensions: .PDF, .TIF, .TIFF Each JSONL file must not exceed 100MB in size, and no more than 20 JSONL files may be passed. Sample inline JSONL file (Shown with artificial line breaks. Actual line breaks are denoted by "\n".): { "id": "my_first_id", "text_snippet": { "content": "dog car cat"}, "text_features": [ { "text_segment": {"start_offset": 4, "end_offset": 6}, "structural_type": PARAGRAPH, "bounding_poly": { "normalized_vertices": [ {"x": 0.1, "y": 0.1}, {"x": 0.1, "y": 0.3}, {"x": 0.3, "y": 0.3}, {"x": 0.3, "y": 0.1}, ] }, } ], }\n { "id": "2", "text_snippet": { "content": "Extended sample content", "mime_type": "text/plain" } } Sample document JSONL file (Shown with artificial line breaks. Actual line breaks are denoted by "\n".): { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ] } } } }\n { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document2.tif" ] } } } } </section></div><h4>AutoML Tables</h4><div class="ui-datasection-main"><section class="selected"> See [Preparing your training data]([https://cloud.google.com/automl-tables/docs/predict-batch](https://cloud.google.com/automl-tables/docs/predict-batch)) for more information. You can use either [gcs_source][google.cloud.automl.v1.BatchPredictInputConfig.gcs_source] or [bigquery_source][BatchPredictInputConfig.bigquery_source]. **For gcs_source:** CSV file(s), each by itself 10GB or smaller and total size must be 100GB or smaller, where first file must have a header containing column names. If the first row of a subsequent file is the same as the header, then it is also treated as a header. All other rows contain values for the corresponding columns. The column names must contain the model's [input_feature_column_specs'][google.cloud.automl.v1.TablesModelMetadata.input_feature_column_specs] [display_name-s][google.cloud.automl.v1.ColumnSpec.display_name] (order doesn't matter). The columns corresponding to the model's input feature column specs must contain values compatible with the column spec's data types. Prediction on all the rows, i.e. the CSV lines, will be attempted. Sample rows from a CSV file: <pre> "First Name","Last Name","Dob","Addresses" "John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]" "Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]} </pre> **For bigquery_source:** The URI of a BigQuery table. The user data size of the BigQuery table must be 100GB or smaller. The column names must contain the model's [input_feature_column_specs'][google.cloud.automl.v1.TablesModelMetadata.input_feature_column_specs] [display_name-s][google.cloud.automl.v1.ColumnSpec.display_name] (order doesn't matter). The columns corresponding to the model's input feature column specs must contain values compatible with the column spec's data types. Prediction on all the rows of the table will be attempted. </section></div> **Input field definitions:** `GCS_FILE_PATH` : The path to a file on Google Cloud Storage. For example, "gs://folder/video.avi". `TIME_SEGMENT_START` : (`TIME_OFFSET`) Expresses a beginning, inclusive, of a time segment within an example that has a time dimension (e.g. video). `TIME_SEGMENT_END` : (`TIME_OFFSET`) Expresses an end, exclusive, of a time segment within n example that has a time dimension (e.g. video). `TIME_OFFSET` : A number of seconds as measured from the start of an example (e.g. video). Fractions are allowed, up to a microsecond precision. "inf" is allowed, and it means the end of the example. **Errors:** If any of the provided CSV files can't be parsed or if more than certain percent of CSV rows cannot be processed then the operation fails and prediction does not happen. Regardless of overall success or failure the per-row failures, up to a certain count cap, will be listed in Operation.metadata.partial_failures.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of BatchPredict operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Further describes this batch predict's output. Supplements [BatchPredictOutputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#BatchPredictOutputConfig)[google.cloud.automl.v1.BatchPredictOutputConfig].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Output configuration for BatchPredict Action. As destination the [gcs_destination][google.cloud.automl.v1.BatchPredictOutputConfig.gcs_destination] must be set unless specified otherwise for a domain. If gcs_destination is set then in the given directory a new directory is created. Its name will be "prediction-<model-display-name>-<timestamp-of-prediction-call>", where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. The contents of it depends on the ML problem the predictions are made for. - For Image Classification: In the created directory files `image_classification_1.jsonl`, `image_classification_2.jsonl`,...,`image_classification_N.jsonl` will be created, where N may be 1, and depends on the total number of the successfully predicted images and annotations. A single image will be listed only once with all its annotations, and its annotations will never be split across files. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps image's "ID" : "<id_value>" followed by a list of zero or more AnnotationPayload protos (called annotations), which have classification detail populated. If prediction for any image failed (partially or completely), then an additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps the same "ID" : "<id_value>" but here followed by exactly one [`google.rpc.Status`]([https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto)) containing only `code` and `message`fields. - For Image Object Detection: In the created directory files `image_object_detection_1.jsonl`, `image_object_detection_2.jsonl`,...,`image_object_detection_N.jsonl` will be created, where N may be 1, and depends on the total number of the successfully predicted images and annotations. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps image's "ID" : "<id_value>" followed by a list of zero or more AnnotationPayload protos (called annotations), which have image_object_detection detail populated. A single image will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any image failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps the same "ID" : "<id_value>" but here followed by exactly one [`google.rpc.Status`]([https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto)) containing only `code` and `message`fields. - For Video Classification: In the created directory a video_classification.csv file, and a .JSON file per each video classification requested in the input (i.e. each line in given CSV(s)), will be created. The format of video_classification.csv is: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END,JSON_FILE_NAME,STATUS where: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END = matches 1 to 1 the prediction input lines (i.e. video_classification.csv has precisely the same number of lines as the prediction input had.) JSON_FILE_NAME = Name of .JSON file in the output directory, which contains prediction responses for the video time segment. STATUS = "OK" if prediction completed successfully, or an error code with message otherwise. If STATUS is not "OK" then the .JSON file for that line may not exist or be empty. Each .JSON file, assuming STATUS is "OK", will contain a list of AnnotationPayload protos in JSON format, which are the predictions for the video time segment the file is assigned to in the video_classification.csv. All AnnotationPayload protos will have video_classification field set, and will be sorted by video_classification.type field (note that the returned types are governed by `classifaction_types` parameter in [PredictService.BatchPredictRequest.params][]). - For Video Object Tracking: In the created directory a video_object_tracking.csv file will be created, and multiple files video_object_trackinng_1.json, video_object_trackinng_2.json,..., video_object_trackinng_N.json, where N is the number of requests in the input (i.e. the number of lines in given CSV(s)). The format of video_object_tracking.csv is: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END,JSON_FILE_NAME,STATUS where: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END = matches 1 to 1 the prediction input lines (i.e. video_object_tracking.csv has precisely the same number of lines as the prediction input had.) JSON_FILE_NAME = Name of .JSON file in the output directory, which contains prediction responses for the video time segment. STATUS = "OK" if prediction completed successfully, or an error code with message otherwise. If STATUS is not "OK" then the .JSON file for that line may not exist or be empty. Each .JSON file, assuming STATUS is "OK", will contain a list of AnnotationPayload protos in JSON format, which are the predictions for each frame of the video time segment the file is assigned to in video_object_tracking.csv. All AnnotationPayload protos will have video_object_tracking field set. - For Text Classification: In the created directory files `text_classification_1.jsonl`, `text_classification_2.jsonl`,...,`text_classification_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps input text file (or document) in the text snippet (or document) proto and a list of zero or more AnnotationPayload protos (called annotations), which have classification detail populated. A single text file (or document) will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any input file (or document) failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps input file followed by exactly one [`google.rpc.Status`]([https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto)) containing only `code` and `message`. - For Text Sentiment: In the created directory files `text_sentiment_1.jsonl`, `text_sentiment_2.jsonl`,...,`text_sentiment_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps input text file (or document) in the text snippet (or document) proto and a list of zero or more AnnotationPayload protos (called annotations), which have text_sentiment detail populated. A single text file (or document) will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any input file (or document) failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps input file followed by exactly one [`google.rpc.Status`]([https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto)) containing only `code` and `message`. - For Text Extraction: In the created directory files `text_extraction_1.jsonl`, `text_extraction_2.jsonl`,...,`text_extraction_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found. The contents of these .JSONL file(s) depend on whether the input used inline text, or documents. If input was inline, then each .JSONL file will contain, per line, a JSON representation of a proto that wraps given in request text snippet's "id" (if specified), followed by input text snippet, and a list of zero or more AnnotationPayload protos (called annotations), which have text_extraction detail populated. A single text snippet will be listed only once with all its annotations, and its annotations will never be split across files. If input used documents, then each .JSONL file will contain, per line, a JSON representation of a proto that wraps given in request document proto, followed by its OCR-ed representation in the form of a text snippet, finally followed by a list of zero or more AnnotationPayload protos (called annotations), which have text_extraction detail populated and refer, via their indices, to the OCR-ed text snippet. A single document (and its text snippet) will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any text snippet failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps either the "id" : "<id_value>" (in case of inline) or the document proto (in case of document) but here followed by exactly one [`google.rpc.Status`]([https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto)) containing only `code` and `message`. - For Tables: Output depends on whether [gcs_destination][google.cloud.automl.v1p1beta.BatchPredictOutputConfig.gcs_destination] or [bigquery_destination][google.cloud.automl.v1p1beta.BatchPredictOutputConfig.bigquery_destination] is set (either is allowed). Google Cloud Storage case: In the created directory files `tables_1.csv`, `tables_2.csv`,..., `tables_N.csv` will be created, where N may be 1, and depends on the total number of the successfully predicted rows. For all CLASSIFICATION [prediction_type-s][google.cloud.automl.v1p1beta.TablesModelMetadata.prediction_type]: Each .csv file will contain a header, listing all columns' [display_name-s][google.cloud.automl.v1p1beta.ColumnSpec.display_name] given on input followed by M target column names in the format of "<[target_column_specs][google.cloud.automl.v1p1beta.TablesModelMetadata.target_column_spec] [display_name][google.cloud.automl.v1p1beta.ColumnSpec.display_name]>_<target value> _score" where M is the number of distinct target values, i.e. number of distinct values in the target column of the table used to train the model. Subsequent lines will contain the respective values of successfully predicted rows, with the last, i.e. the target, columns having the corresponding prediction [scores][google.cloud.automl.v1p1beta.TablesAnnotation.score]. For REGRESSION and FORECASTING [prediction_type-s][google.cloud.automl.v1p1beta.TablesModelMetadata.prediction_type]: Each .csv file will contain a header, listing all columns' [display_name-s][google.cloud.automl.v1p1beta.display_name] given on input followed by the predicted target column with name in the format of "predicted_ <[target_column_specs][google.cloud.automl.v1p1beta.TablesModelMetadata.target_column_spec] [display_name][google.cloud.automl.v1p1beta.ColumnSpec.display_name]>" Subsequent lines will contain the respective values of successfully predicted rows, with the last, i.e. the target, column having the predicted target value. If prediction for any rows failed, then an additional `errors_1.csv`, `errors_2.csv`,..., `errors_N.csv` will be created (N depends on total number of failed rows). These files will have analogous format as `tables_*.csv`, but always with a single target column having [`google.rpc.Status`]([https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto)) represented as a JSON string, and containing only `code` and `message`. BigQuery case: [bigquery_destination][google.cloud.automl.v1p1beta.OutputConfig.bigquery_destination] pointing to a BigQuery project must be set. In the given project a new dataset will be created with name `prediction_<model-display-name>_<timestamp-of-prediction-call>` where <model-display-name> will be made BigQuery-dataset-name compatible (e.g. most special characters will become underscores), and timestamp will be in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. The `predictions` table's column names will be the input columns' [display_name-s][google.cloud.automl.v1p1beta.ColumnSpec.display_name] followed by the target column with name in the format of "predicted_<[target_column_specs][google.cloud.automl.v1p1beta.TablesModelMetadata.target_column_spec] [display_name][google.cloud.automl.v1p1beta.ColumnSpec.display_name]>" The input feature columns will contain the respective values of successfully predicted rows, with the target column having an ARRAY of [AnnotationPayloads][google.cloud.automl.v1p1beta.AnnotationPayload], represented as STRUCT-s, containing [TablesAnnotation][google.cloud.automl.v1p1beta.TablesAnnotation]. The `errors` table contains rows for which the prediction has failed, it has analogous input columns while the target column name is in the format of "errors_<[target_column_specs][google.cloud.automl.v1p1beta.TablesModelMetadata.target_column_spec] [display_name][google.cloud.automl.v1p1beta.ColumnSpec.display_name]>", and as a value has [`google.rpc.Status`]([https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto)) represented as a STRUCT, and containing only `code` and `message`.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [PredictionService.BatchPredict][google.cloud.automl.v1.PredictionService.BatchPredict].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Result of the Batch Predict. This message is returned in [response][google.longrunning.Operation.response] of the operation returned by the [PredictionService.BatchPredict][google.cloud.automl.v1.PredictionService.BatchPredict].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Bounding box matching model metrics for a single intersection-over-union threshold and multiple label match confidence thresholds.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Metrics for a single confidence threshold.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A bounding polygon of a detected object on a plane. On output both vertices and normalized_vertices are provided. The polygon is formed by connecting vertices in the order they are listed.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Contains annotation details specific to classification.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of "segment_classification" type.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Metrics for a single confidence threshold.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Confusion matrix of the model running the classification.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Output only. A row in the confusion matrix.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Type of the classification problem.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of CreateDataset operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.CreateDataset][google.cloud.automl.v1.AutoMl.CreateDataset].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of CreateModel operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.CreateModel][google.cloud.automl.v1.AutoMl.CreateModel].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A workspace for solving a single, particular machine learning (ML) problem. A workspace contains examples that may be annotated.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.DeleteDataset][google.cloud.automl.v1.AutoMl.DeleteDataset].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.DeleteModel][google.cloud.automl.v1.AutoMl.DeleteModel].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of operations that perform deletes of any entities.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of DeployModel operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.DeployModel][google.cloud.automl.v1.AutoMl.DeployModel].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A structured text document e.g. a PDF.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Message that describes dimension of a document.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Unit of the document dimension.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Input configuration of a [Document](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#Document)[google.cloud.automl.v1.Document].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Describes the layout information of a [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in the document.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

The type of TextSegment in the context of the original document.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Example data used for training or prediction.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of ExportData operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Further describes this export data's output. Supplements [OutputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#OutputConfig)[google.cloud.automl.v1.OutputConfig].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.ExportData][google.cloud.automl.v1.AutoMl.ExportData].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of ExportModel operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Further describes the output of model export. Supplements [ModelExportOutputConfig](https://pkg.go.dev/google.golang.org/genproto@v0.0.0-20260226221140-a57be14db171/googleapis/cloud/automl/v1#ModelExportOutputConfig)[google.cloud.automl.v1.ModelExportOutputConfig].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]. Models need to be enabled for exporting, otherwise an error code will be returned.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

The Google Cloud Storage location where the output is to be written to.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

The Google Cloud Storage location for the input content.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.GetAnnotationSpec][google.cloud.automl.v1.AutoMl.GetAnnotationSpec].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.GetDataset][google.cloud.automl.v1.AutoMl.GetDataset].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.GetModelEvaluation][google.cloud.automl.v1.AutoMl.GetModelEvaluation].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.GetModel][google.cloud.automl.v1.AutoMl.GetModel].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A representation of an image. Only images up to 30MB in size are supported.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Dataset metadata that is specific to image classification.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model deployment metadata specific to Image Classification.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model metadata for image classification.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Annotation details for image object detection.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Dataset metadata specific to image object detection.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model evaluation metrics for image object detection problems. Evaluates prediction quality of labeled bounding boxes.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model deployment metadata specific to Image Object Detection.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model metadata specific to image object detection.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of ImportData operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.ImportData][google.cloud.automl.v1.AutoMl.ImportData].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Input configuration for [AutoMl.ImportData][google.cloud.automl.v1.AutoMl.ImportData] action. The format of input depends on dataset_metadata the Dataset into which the import is happening has. As input source the [gcs_source][google.cloud.automl.v1.InputConfig.gcs_source] is expected, unless specified otherwise. Additionally any input .CSV file by itself must be 100MB or smaller, unless specified otherwise. If an "example" file (that is, image, video etc.) with identical content (even if it had different `GCS_FILE_PATH`) is mentioned multiple times, then its label, bounding boxes etc. are appended. The same file should be always provided with the same `ML_USE` and `GCS_FILE_PATH`, if it is not, then these values are nondeterministically selected from the given ones. The formats are represented in EBNF with commas being literal and with non-terminal symbols defined near the end of this comment. The formats are: <h4>AutoML Vision</h4><div class="ds-selector-tabs"><section><h5>Classification</h5> See [Preparing your training data]([https://cloud.google.com/vision/automl/docs/prepare](https://cloud.google.com/vision/automl/docs/prepare)) for more information. CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH,LABEL,LABEL,... * `ML_USE` - Identifies the data set that the current row (file) applies to. This value can be one of the following: * `TRAIN` - Rows in this file are used to train the model. * `TEST` - Rows in this file are used to test the model during training. * `UNASSIGNED` - Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing. - `GCS_FILE_PATH` - The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG, .WEBP, .BMP, .TIFF, .ICO. * `LABEL` - A label that identifies the object in the image. For the `MULTICLASS` classification type, at most one `LABEL` is allowed per image. If an image has not yet been labeled, then it should be mentioned just once with no `LABEL`. Some sample rows: TRAIN,gs://folder/image1.jpg,daisy TEST,gs://folder/image2.jpg,dandelion,tulip,rose UNASSIGNED,gs://folder/image3.jpg,daisy UNASSIGNED,gs://folder/image4.jpg </section><section><h5>Object Detection</h5> See [Preparing your training data]([https://cloud.google.com/vision/automl/object-detection/docs/prepare](https://cloud.google.com/vision/automl/object-detection/docs/prepare)) for more information. A CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH,[LABEL],(BOUNDING_BOX | ,,,,,,,) * `ML_USE` - Identifies the data set that the current row (file) applies to. This value can be one of the following: * `TRAIN` - Rows in this file are used to train the model. * `TEST` - Rows in this file are used to test the model during training. * `UNASSIGNED` - Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing. - `GCS_FILE_PATH` - The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. Each image is assumed to be exhaustively labeled. - `LABEL` - A label that identifies the object in the image specified by the `BOUNDING_BOX`. - `BOUNDING BOX` - The vertices of an object in the example image. The minimum allowed `BOUNDING_BOX` edge length is 0.01, and no more than 500 `BOUNDING_BOX` instances per image are allowed (one `BOUNDING_BOX` per line). If an image has no looked for objects then it should be mentioned just once with no LABEL and the ",,,,,,," in place of the `BOUNDING_BOX`. **Four sample rows:** TRAIN,gs://folder/image1.png,car,0.1,0.1,,,0.3,0.3,, TRAIN,gs://folder/image1.png,bike,.7,.6,,,.8,.9,, UNASSIGNED,gs://folder/im2.png,car,0.1,0.1,0.2,0.1,0.2,0.3,0.1,0.3 TEST,gs://folder/im3.png,,,,,,,,, </section></div><h4>AutoML Video Intelligence</h4><div class="ds-selector-tabs"><section><h5>Classification</h5> See [Preparing your training data]([https://cloud.google.com/video-intelligence/automl/docs/prepare](https://cloud.google.com/video-intelligence/automl/docs/prepare)) for more information. CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH For `ML_USE`, do not use `VALIDATE`. `GCS_FILE_PATH` is the path to another .csv file that describes training example for a given `ML_USE`, using the following row format: GCS_FILE_PATH,(LABEL,TIME_SEGMENT_START,TIME_SEGMENT_END | ,,) Here `GCS_FILE_PATH` leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. `TIME_SEGMENT_START` and `TIME_SEGMENT_END` must be within the length of the video, and the end time must be after the start time. Any segment of a video which has one or more labels on it, is considered a hard negative for all other labels. Any segment with no labels on it is considered to be unknown. If a whole video is unknown, then it should be mentioned just once with ",," in place of `LABEL, TIME_SEGMENT_START,TIME_SEGMENT_END`. Sample top level CSV file: TRAIN,gs://folder/train_videos.csv TEST,gs://folder/test_videos.csv UNASSIGNED,gs://folder/other_videos.csv Sample rows of a CSV file for a particular ML_USE: gs://folder/video1.avi,car,120,180.000021 gs://folder/video1.avi,bike,150,180.000021 gs://folder/vid2.avi,car,0,60.5 gs://folder/vid3.avi,,, </section><section><h5>Object Tracking</h5> See [Preparing your training data](/video-intelligence/automl/object-tracking/docs/prepare) for more information. CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH For `ML_USE`, do not use `VALIDATE`. `GCS_FILE_PATH` is the path to another .csv file that describes training example for a given `ML_USE`, using the following row format: GCS_FILE_PATH,LABEL,[INSTANCE_ID],TIMESTAMP,BOUNDING_BOX or GCS_FILE_PATH,,,,,,,,,, Here `GCS_FILE_PATH` leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. Providing `INSTANCE_ID`s can help to obtain a better model. When a specific labeled entity leaves the video frame, and shows up afterwards it is not required, albeit preferable, that the same `INSTANCE_ID` is given to it. `TIMESTAMP` must be within the length of the video, the `BOUNDING_BOX` is assumed to be drawn on the closest video's frame to the `TIMESTAMP`. Any mentioned by the `TIMESTAMP` frame is expected to be exhaustively labeled and no more than 500 `BOUNDING_BOX`-es per frame are allowed. If a whole video is unknown, then it should be mentioned just once with ",,,,,,,,,," in place of `LABEL, [INSTANCE_ID],TIMESTAMP,BOUNDING_BOX`. Sample top level CSV file: TRAIN,gs://folder/train_videos.csv TEST,gs://folder/test_videos.csv UNASSIGNED,gs://folder/other_videos.csv Seven sample rows of a CSV file for a particular ML_USE: gs://folder/video1.avi,car,1,12.10,0.8,0.8,0.9,0.8,0.9,0.9,0.8,0.9 gs://folder/video1.avi,car,1,12.90,0.4,0.8,0.5,0.8,0.5,0.9,0.4,0.9 gs://folder/video1.avi,car,2,12.10,.4,.2,.5,.2,.5,.3,.4,.3 gs://folder/video1.avi,car,2,12.90,.8,.2,,,.9,.3,, gs://folder/video1.avi,bike,,12.50,.45,.45,,,.55,.55,, gs://folder/video2.avi,car,1,0,.1,.9,,,.9,.1,, gs://folder/video2.avi,,,,,,,,,,, </section></div><h4>AutoML Natural Language</h4><div class="ds-selector-tabs"><section><h5>Entity Extraction</h5> See [Preparing your training data](/natural-language/automl/entity-analysis/docs/prepare) for more information. One or more CSV file(s) with each line in the following format: ML_USE,GCS_FILE_PATH * `ML_USE` - Identifies the data set that the current row (file) applies to. This value can be one of the following: * `TRAIN` - Rows in this file are used to train the model. * `TEST` - Rows in this file are used to test the model during training. * `UNASSIGNED` - Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.. - `GCS_FILE_PATH` - a Identifies JSON Lines (.JSONL) file stored in Google Cloud Storage that contains in-line text in-line as documents for model training. After the training data set has been determined from the `TRAIN` and `UNASSIGNED` CSV files, the training data is divided into train and validation data sets. 70% for training and 30% for validation. For example: TRAIN,gs://folder/file1.jsonl VALIDATE,gs://folder/file2.jsonl TEST,gs://folder/file3.jsonl **In-line JSONL files** In-line .JSONL files contain, per line, a JSON document that wraps a [`text_snippet`][google.cloud.automl.v1.TextSnippet] field followed by one or more [`annotations`][google.cloud.automl.v1.AnnotationPayload] fields, which have `display_name` and `text_extraction` fields to describe the entity from the text snippet. Multiple JSON documents can be separated using line breaks (\n). The supplied text must be annotated exhaustively. For example, if you include the text "horse", but do not label it as "animal", then "horse" is assumed to not be an "animal". Any given text snippet content must have 30,000 characters or less, and also be UTF-8 NFC encoded. ASCII is accepted as it is UTF-8 NFC encoded. For example: { "text_snippet": { "content": "dog car cat" }, "annotations": [ { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 0, "end_offset": 2} } }, { "display_name": "vehicle", "text_extraction": { "text_segment": {"start_offset": 4, "end_offset": 6} } }, { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 8, "end_offset": 10} } } ] }\n { "text_snippet": { "content": "This dog is good." }, "annotations": [ { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 5, "end_offset": 7} } } ] } **JSONL files that reference documents** .JSONL files contain, per line, a JSON document that wraps a `input_config` that contains the path to a source document. Multiple JSON documents can be separated using line breaks (\n). Supported document extensions: .PDF, .TIF, .TIFF For example: { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ] } } } }\n { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document2.tif" ] } } } } **In-line JSONL files with document layout information** **Note:** You can only annotate documents using the UI. The format described below applies to annotated documents exported using the UI or `exportData`. In-line .JSONL files for documents contain, per line, a JSON document that wraps a `document` field that provides the textual content of the document and the layout information. For example: { "document": { "document_text": { "content": "dog car cat" } "layout": [ { "text_segment": { "start_offset": 0, "end_offset": 11, }, "page_number": 1, "bounding_poly": { "normalized_vertices": [ {"x": 0.1, "y": 0.1}, {"x": 0.1, "y": 0.3}, {"x": 0.3, "y": 0.3}, {"x": 0.3, "y": 0.1}, ], }, "text_segment_type": TOKEN, } ], "document_dimensions": { "width": 8.27, "height": 11.69, "unit": INCH, } "page_count": 3, }, "annotations": [ { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 0, "end_offset": 3} } }, { "display_name": "vehicle", "text_extraction": { "text_segment": {"start_offset": 4, "end_offset": 7} } }, { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 8, "end_offset": 11} } }, ], </section><section><h5>Classification</h5> See [Preparing your training data]([https://cloud.google.com/natural-language/automl/docs/prepare](https://cloud.google.com/natural-language/automl/docs/prepare)) for more information. One or more CSV file(s) with each line in the following format: ML_USE,(TEXT_SNIPPET | GCS_FILE_PATH),LABEL,LABEL,... * `ML_USE` - Identifies the data set that the current row (file) applies to. This value can be one of the following: * `TRAIN` - Rows in this file are used to train the model. * `TEST` - Rows in this file are used to test the model during training. * `UNASSIGNED` - Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing. - `TEXT_SNIPPET` and `GCS_FILE_PATH` are distinguished by a pattern. If the column content is a valid Google Cloud Storage file path, that is, prefixed by "gs://", it is treated as a `GCS_FILE_PATH`. Otherwise, if the content is enclosed in double quotes (""), it is treated as a `TEXT_SNIPPET`. For `GCS_FILE_PATH`, the path must lead to a file with supported extension and UTF-8 encoding, for example, "gs://folder/content.txt" AutoML imports the file content as a text snippet. For `TEXT_SNIPPET`, AutoML imports the column content excluding quotes. In both cases, size of the content must be 10MB or less in size. For zip files, the size of each file inside the zip must be 10MB or less in size. For the `MULTICLASS` classification type, at most one `LABEL` is allowed. The `ML_USE` and `LABEL` columns are optional. Supported file extensions: .TXT, .PDF, .TIF, .TIFF, .ZIP A maximum of 100 unique labels are allowed per CSV row. Sample rows: TRAIN,"They have bad food and very rude",RudeService,BadFood gs://folder/content.txt,SlowService TEST,gs://folder/document.pdf VALIDATE,gs://folder/text_files.zip,BadFood </section><section><h5>Sentiment Analysis</h5> See [Preparing your training data]([https://cloud.google.com/natural-language/automl/docs/prepare](https://cloud.google.com/natural-language/automl/docs/prepare)) for more information. CSV file(s) with each line in format: ML_USE,(TEXT_SNIPPET | GCS_FILE_PATH),SENTIMENT * `ML_USE` - Identifies the data set that the current row (file) applies to. This value can be one of the following: * `TRAIN` - Rows in this file are used to train the model. * `TEST` - Rows in this file are used to test the model during training. * `UNASSIGNED` - Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing. - `TEXT_SNIPPET` and `GCS_FILE_PATH` are distinguished by a pattern. If the column content is a valid Google Cloud Storage file path, that is, prefixed by "gs://", it is treated as a `GCS_FILE_PATH`. Otherwise, if the content is enclosed in double quotes (""), it is treated as a `TEXT_SNIPPET`. For `GCS_FILE_PATH`, the path must lead to a file with supported extension and UTF-8 encoding, for example, "gs://folder/content.txt" AutoML imports the file content as a text snippet. For `TEXT_SNIPPET`, AutoML imports the column content excluding quotes. In both cases, size of the content must be 128kB or less in size. For zip files, the size of each file inside the zip must be 128kB or less in size. The `ML_USE` and `SENTIMENT` columns are optional. Supported file extensions: .TXT, .PDF, .TIF, .TIFF, .ZIP - `SENTIMENT` - An integer between 0 and Dataset.text_sentiment_dataset_metadata.sentiment_max (inclusive). Describes the ordinal of the sentiment - higher value means a more positive sentiment. All the values are completely relative, i.e. neither 0 needs to mean a negative or neutral sentiment nor sentiment_max needs to mean a positive one - it is just required that 0 is the least positive sentiment in the data, and sentiment_max is the most positive one. The SENTIMENT shouldn't be confused with "score" or "magnitude" from the previous Natural Language Sentiment Analysis API. All SENTIMENT values between 0 and sentiment_max must be represented in the imported data. On prediction the same 0 to sentiment_max range will be used. The difference between neighboring sentiment values needs not to be uniform, e.g. 1 and 2 may be similar whereas the difference between 2 and 3 may be large. Sample rows: TRAIN,"@freewrytin this is way too good for your product",2 gs://folder/content.txt,3 TEST,gs://folder/document.pdf VALIDATE,gs://folder/text_files.zip,2 </section></div><h4>AutoML Tables</h4><div class="ui-datasection-main"><section class="selected"> See [Preparing your training data]([https://cloud.google.com/automl-tables/docs/prepare](https://cloud.google.com/automl-tables/docs/prepare)) for more information. You can use either [gcs_source][google.cloud.automl.v1.InputConfig.gcs_source] or [bigquery_source][google.cloud.automl.v1.InputConfig.bigquery_source]. All input is concatenated into a single [primary_table_spec_id][google.cloud.automl.v1.TablesDatasetMetadata.primary_table_spec_id] **For gcs_source:** CSV file(s), where the first row of the first file is the header, containing unique column names. If the first row of a subsequent file is the same as the header, then it is also treated as a header. All other rows contain values for the corresponding columns. Each .CSV file by itself must be 10GB or smaller, and their total size must be 100GB or smaller. First three sample rows of a CSV file: <pre> "Id","First Name","Last Name","Dob","Addresses" "1","John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]" "2","Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]} </pre> **For bigquery_source:** An URI of a BigQuery table. The user data size of the BigQuery table must be 100GB or smaller. An imported table must have between 2 and 1,000 columns, inclusive, and between 1000 and 100,000,000 rows, inclusive. There are at most 5 import data running in parallel. </section></div> **Input field definitions:** `ML_USE` : ("TRAIN" | "VALIDATE" | "TEST" | "UNASSIGNED") Describes how the given example (file) should be used for model training. "UNASSIGNED" can be used when user has no preference. `GCS_FILE_PATH` : The path to a file on Google Cloud Storage. For example, "gs://folder/image1.png". `LABEL` : A display name of an object on an image, video etc., e.g. "dog". Must be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores(_), and ASCII digits 0-9. For each label an AnnotationSpec is created which display_name becomes the label; AnnotationSpecs are given back in predictions. `INSTANCE_ID` : A positive integer that identifies a specific instance of a labeled entity on an example. Used e.g. to track two cars on a video while being able to tell apart which one is which. `BOUNDING_BOX` : (`VERTEX,VERTEX,VERTEX,VERTEX` | `VERTEX,,,VERTEX,,`) A rectangle parallel to the frame of the example (image, video). If 4 vertices are given they are connected by edges in the order provided, if 2 are given they are recognized as diagonally opposite vertices of the rectangle. `VERTEX` : (`COORDINATE,COORDINATE`) First coordinate is horizontal (x), the second is vertical (y). `COORDINATE` : A float in 0 to 1 range, relative to total length of image or video in given dimension. For fractions the leading non-decimal 0 can be omitted (i.e. 0.3 = .3). Point 0,0 is in top left. `TIME_SEGMENT_START` : (`TIME_OFFSET`) Expresses a beginning, inclusive, of a time segment within an example that has a time dimension (e.g. video). `TIME_SEGMENT_END` : (`TIME_OFFSET`) Expresses an end, exclusive, of a time segment within n example that has a time dimension (e.g. video). `TIME_OFFSET` : A number of seconds as measured from the start of an example (e.g. video). Fractions are allowed, up to a microsecond precision. "inf" is allowed, and it means the end of the example. `TEXT_SNIPPET` : The content of a text snippet, UTF-8 encoded, enclosed within double quotes (""). `DOCUMENT` : A field that provides the textual content with document and the layout information. **Errors:** If any of the provided CSV files can't be parsed or if more than certain percent of CSV rows cannot be processed then the operation fails and nothing is imported. Regardless of overall success or failure the per-row failures, up to a certain count cap, is listed in Operation.metadata.partial_failures.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.ListDatasets][google.cloud.automl.v1.AutoMl.ListDatasets].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Response message for [AutoMl.ListDatasets][google.cloud.automl.v1.AutoMl.ListDatasets].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.ListModelEvaluations][google.cloud.automl.v1.AutoMl.ListModelEvaluations].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Response message for [AutoMl.ListModelEvaluations][google.cloud.automl.v1.AutoMl.ListModelEvaluations].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.ListModels][google.cloud.automl.v1.AutoMl.ListModels].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Response message for [AutoMl.ListModels][google.cloud.automl.v1.AutoMl.ListModels].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

API proto representing a trained machine learning model.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Evaluation results of a model.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Output configuration for ModelExport Action.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Deployment state of the model.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A vertex represents a 2D point in the image. The normalized vertex coordinates are between 0 to 1 fractions relative to the original plane (image, video). E.g. if the plane (e.g. whole image) would have size 10 x 20 then a point with normalized coordinates (0.1, 0.3) would be at the position (1, 6) on that plane.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Metadata used across all long running operations returned by AutoML API.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

- For Translation: CSV file `translation.csv`, with each line in format: ML_USE,GCS_FILE_PATH GCS_FILE_PATH leads to a .TSV file which describes examples that have given ML_USE, using the following row format per line: TEXT_SNIPPET (in source language) \t TEXT_SNIPPET (in target language) - For Tables: Output depends on whether the dataset was imported from Google Cloud Storage or BigQuery. Google Cloud Storage case: [gcs_destination][google.cloud.automl.v1p1beta.OutputConfig.gcs_destination] must be set. Exported are CSV file(s) `tables_1.csv`, `tables_2.csv`,...,`tables_N.csv` with each having as header line the table's column names, and all other lines contain values for the header columns. BigQuery case: [bigquery_destination][google.cloud.automl.v1p1beta.OutputConfig.bigquery_destination] pointing to a BigQuery project must be set. In the given project a new dataset will be created with name `export_data_<automl-dataset-display-name>_<timestamp-of-export-call>` where <automl-dataset-display-name> will be made BigQuery-dataset-name compatible (e.g. most special characters will become underscores), and timestamp will be in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In that dataset a new table called `primary_table` will be created, and filled with precisely the same data as this obtained on import.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [PredictionService.Predict][google.cloud.automl.v1.PredictionService.Predict].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Response message for [PredictionService.Predict][google.cloud.automl.v1.PredictionService.Predict].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

PredictionServiceClient is the client API for PredictionService service. For semantics around ctx use and closing/ending streaming RPCs, please refer to [https://godoc.org/google.golang.org/grpc#ClientConn.NewStream](https://godoc.org/google.golang.org/grpc#ClientConn.NewStream).

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Deprecated: Please use funcs in: cloud.google.com/go/automl/apiv1/automlpb

PredictionServiceServer is the server API for PredictionService service.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Dataset metadata for classification.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model metadata that is specific to text classification.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Annotation for identifying spans of text.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Dataset metadata that is specific to text extraction

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model evaluation metrics for text extraction problems.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Metrics for a single confidence threshold.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model metadata that is specific to text extraction.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A contiguous part of a text (string), assuming it has an UTF-8 NFC encoding.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Contains annotation details specific to text sentiment.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Dataset metadata for text sentiment.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model evaluation metrics for text sentiment problems.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model metadata that is specific to text sentiment.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

A representation of a text snippet.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Annotation details specific to translation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Dataset metadata that is specific to translation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Evaluation metrics for the dataset.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Model metadata that is specific to translation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Details of UndeployModel operation.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.UndeployModel][google.cloud.automl.v1.AutoMl.UndeployModel].

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

UnimplementedAutoMlServer can be embedded to have forward compatible implementations.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

UnimplementedPredictionServiceServer can be embedded to have forward compatible implementations.

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.UpdateDataset][google.cloud.automl.v1.AutoMl.UpdateDataset]

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb

Request message for [AutoMl.UpdateModel][google.cloud.automl.v1.AutoMl.UpdateModel]

Deprecated: Please use types in: cloud.google.com/go/automl/apiv1/automlpb
