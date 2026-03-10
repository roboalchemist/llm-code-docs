# Source: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/llms.txt

# AWS Supply Chain API Reference

> AWS Supply Chain is a cloud-based application that works with your enterprise resource planning (ERP) and supply chain management systems. Using AWS Supply Chain, you can connect and extract your inventory, supply, and demand related data from existing ERP or supply chain systems into a single data model.

- [Welcome](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_Operations.html)

- [CreateBillOfMaterialsImportJob](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateBillOfMaterialsImportJob.html): CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of Materials (BOM) entity.
- [CreateDataIntegrationFlow](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateDataIntegrationFlow.html): Enables you to programmatically create a data pipeline to ingest data from source systems such as Amazon S3 buckets, to a predefined AWS Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.
- [CreateDataLakeDataset](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateDataLakeDataset.html): Enables you to programmatically create an AWS Supply Chain data lake dataset.
- [CreateDataLakeNamespace](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateDataLakeNamespace.html): Enables you to programmatically create an AWS Supply Chain data lake namespace.
- [CreateInstance](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateInstance.html): Enables you to programmatically create an AWS Supply Chain instance by applying KMS keys and relevant information associated with the API without using the AWS console.
- [DeleteDataIntegrationFlow](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DeleteDataIntegrationFlow.html): Enable you to programmatically delete an existing data pipeline for the provided AWS Supply Chain instance and DataIntegrationFlow name.
- [DeleteDataLakeDataset](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DeleteDataLakeDataset.html): Enables you to programmatically delete an AWS Supply Chain data lake dataset.
- [DeleteDataLakeNamespace](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DeleteDataLakeNamespace.html): Enables you to programmatically delete an AWS Supply Chain data lake namespace and its underling datasets.
- [DeleteInstance](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DeleteInstance.html): Enables you to programmatically delete an AWS Supply Chain instance by deleting the KMS keys and relevant information associated with the API without using the AWS console.
- [GetBillOfMaterialsImportJob](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetBillOfMaterialsImportJob.html): Get status and details of a BillOfMaterialsImportJob.
- [GetDataIntegrationEvent](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetDataIntegrationEvent.html): Enables you to programmatically view an AWS Supply Chain Data Integration Event.
- [GetDataIntegrationFlow](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetDataIntegrationFlow.html): Enables you to programmatically view a specific data pipeline for the provided AWS Supply Chain instance and DataIntegrationFlow name.
- [GetDataIntegrationFlowExecution](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetDataIntegrationFlowExecution.html): Get the flow execution.
- [GetDataLakeDataset](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetDataLakeDataset.html): Enables you to programmatically view an AWS Supply Chain data lake dataset.
- [GetDataLakeNamespace](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetDataLakeNamespace.html): Enables you to programmatically view an AWS Supply Chain data lake namespace.
- [GetInstance](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetInstance.html): Enables you to programmatically retrieve the information related to an AWS Supply Chain instance ID.
- [ListDataIntegrationEvents](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataIntegrationEvents.html): Enables you to programmatically list all data integration events for the provided AWS Supply Chain instance.
- [ListDataIntegrationFlowExecutions](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataIntegrationFlowExecutions.html): List flow executions.
- [ListDataIntegrationFlows](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataIntegrationFlows.html): Enables you to programmatically list all data pipelines for the provided AWS Supply Chain instance.
- [ListDataLakeDatasets](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataLakeDatasets.html): Enables you to programmatically view the list of AWS Supply Chain data lake datasets.
- [ListDataLakeNamespaces](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataLakeNamespaces.html): Enables you to programmatically view the list of AWS Supply Chain data lake namespaces.
- [ListInstances](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListInstances.html): List all AWS Supply Chain instances for a specific account.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListTagsForResource.html): List all the tags for an AWSSupply Chain resource.
- [SendDataIntegrationEvent](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_SendDataIntegrationEvent.html): Send the data payload for the event with real-time data for analysis or monitoring.
- [TagResource](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_TagResource.html): You can create tags during or after creating a resource such as instance, data flow, or dataset in AWS Supply chain.
- [UntagResource](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_UntagResource.html): You can delete tags for an AWS Supply chain resource such as instance, data flow, or dataset in AWS Supply Chain.
- [UpdateDataIntegrationFlow](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_UpdateDataIntegrationFlow.html): Enables you to programmatically update an existing data pipeline to ingest data from the source systems such as, Amazon S3 buckets, to a predefined AWS Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.
- [UpdateDataLakeDataset](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_UpdateDataLakeDataset.html): Enables you to programmatically update an AWS Supply Chain data lake dataset.
- [UpdateDataLakeNamespace](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_UpdateDataLakeNamespace.html): Enables you to programmatically update an AWS Supply Chain data lake namespace.
- [UpdateInstance](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_UpdateInstance.html): Enables you to programmatically update an AWS Supply Chain instance description by providing all the relevant information such as account ID, instance ID and so on without using the AWS console.


## [Data Types](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_Types.html)

- [BillOfMaterialsImportJob](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_BillOfMaterialsImportJob.html): The BillOfMaterialsImportJob details.
- [DataIntegrationEvent](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationEvent.html): The data integration event details.
- [DataIntegrationEventDatasetLoadExecutionDetails](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationEventDatasetLoadExecutionDetails.html): The target dataset load execution details.
- [DataIntegrationEventDatasetTargetConfiguration](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationEventDatasetTargetConfiguration.html): The target dataset configuration for a DATASET event type.
- [DataIntegrationEventDatasetTargetDetails](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationEventDatasetTargetDetails.html): The target dataset details for a DATASET event type.
- [DataIntegrationFlow](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlow.html): The DataIntegrationFlow details.
- [DataIntegrationFlowDatasetOptions](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowDatasetOptions.html): The dataset options used in dataset source and target configurations.
- [DataIntegrationFlowDatasetSource](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowDatasetSource.html): The details of a flow execution with dataset source.
- [DataIntegrationFlowDatasetSourceConfiguration](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowDatasetSourceConfiguration.html): The dataset DataIntegrationFlow source configuration parameters.
- [DataIntegrationFlowDatasetTargetConfiguration](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowDatasetTargetConfiguration.html): The dataset DataIntegrationFlow target configuration parameters.
- [DataIntegrationFlowDedupeStrategy](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowDedupeStrategy.html): The deduplication strategy details.
- [DataIntegrationFlowExecution](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowExecution.html): The flow execution details.
- [DataIntegrationFlowExecutionOutputMetadata](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowExecutionOutputMetadata.html): The output metadata of the flow execution.
- [DataIntegrationFlowExecutionSourceInfo](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowExecutionSourceInfo.html): The source information of a flow execution.
- [DataIntegrationFlowFieldPriorityDedupeField](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowFieldPriorityDedupeField.html): The field used in the field priority deduplication strategy.
- [DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration.html): The field priority deduplication strategy details.
- [DataIntegrationFlowS3Options](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowS3Options.html): The Amazon S3 options used in S3 source and target configurations.
- [DataIntegrationFlowS3Source](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowS3Source.html): The details of a flow execution with S3 source.
- [DataIntegrationFlowS3SourceConfiguration](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowS3SourceConfiguration.html): The S3 DataIntegrationFlow source configuration parameters.
- [DataIntegrationFlowS3TargetConfiguration](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowS3TargetConfiguration.html): The S3 DataIntegrationFlow target configuration parameters.
- [DataIntegrationFlowSource](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowSource.html): The DataIntegrationFlow source parameters.
- [DataIntegrationFlowSQLTransformationConfiguration](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowSQLTransformationConfiguration.html): The SQL DataIntegrationFlow transformation configuration parameters.
- [DataIntegrationFlowTarget](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowTarget.html): The DataIntegrationFlow target parameters.
- [DataIntegrationFlowTransformation](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowTransformation.html): The DataIntegrationFlow transformation parameters.
- [DataLakeDataset](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDataset.html): The data lake dataset details.
- [DataLakeDatasetPartitionField](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetPartitionField.html): The detail of the partition field.
- [DataLakeDatasetPartitionFieldTransform](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetPartitionFieldTransform.html): The detail of the partition field transformation.
- [DataLakeDatasetPartitionSpec](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetPartitionSpec.html): The partition specification for a dataset.
- [DataLakeDatasetPrimaryKeyField](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetPrimaryKeyField.html): The detail of the primary key field.
- [DataLakeDatasetSchema](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetSchema.html): The schema details of the dataset.
- [DataLakeDatasetSchemaField](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetSchemaField.html): The dataset field details.
- [DataLakeNamespace](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeNamespace.html): The data lake namespace details.
- [Instance](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_Instance.html): The details of the instance.
