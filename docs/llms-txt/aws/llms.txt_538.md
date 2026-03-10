# Source: https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/llms.txt

#  User Guide

> Provides a conceptual overview of Amazon Lookout for Equipment, offers detailed instructions for using various features, and includes a complete API reference for developers.

- [What is Amazon Lookout for Equipment?](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/what-is.html)
- [Setting up your account](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/getting-started-brain.html)
- [Creating your project](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/create-project.html)
- [Formatting your data](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/formatting-data.html)
- [Adding your dataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/ingest-dataset.html)
- [Understanding labeling](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html)
- [Evaluating your model](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/view-model.html)
- [Versioning your model](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html)
- [Retraining your model](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/retraining-model.html)
- [Viewing your ingestion history](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/viewing-ingestion-history.html)
- [Replacing your dataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/replacing-your-dataset.html)
- [Use case: fluid pump](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/use-case.html)
- [Quotas](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/guidelines-and-limits.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/creating-resources-with-cloudformation.html)
- [Python SDK examples](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/SDK-examples.html)
- [Document history](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/doc-history.html)

## [How it works](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/how-it-works.html)

- [Step by step](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/step-by-step.html): Overview of the Amazon Lookout for Equipment service, which monitors industrial equipment to detect abnormal equipment behavior and identify potential failures.


## [Reviewing data ingestion](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-ingestion-validation.html)

- [Reviewing the job](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/when-ingestion-jobs-fail.html): Few datasets are perfectly formed.
- [Checking the files](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/when-files-dont-get-ingested.html): Troubleshoot files that were not ingested.
- [Evaluating sensor grades](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/reading-details-by-sensor.html): Deciding which sensors to use when you trainin your model.


## [Training your model](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/create-model.html)

- [Specifying model details](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/specifying-model-details.html): Specify details about your ML model.

### [Configuring your input data](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/configuring-input-data.html)

- [Labeling your data](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/labeling-data.html): Applying labels to your data to indicate the presence of known anomalous events in the past.
- [Starting the training process](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/reviewing-settings.html): The Review and train page gives you a chance to change some of your settings before you start training your model.


## [Importing your resources](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/importing-resources.html)

- [Importing a model](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/importing-datasets-models.html)

### [Bulk importing resources](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/bulk-import-resources.html)

You can import Amazon Lookout for Equipment resources (datasets and models) from a source AWS account to a target AWS account by using the ImportDataset (datasets) or ImportModelVersion (models) operations.

- [Resource CSV file script](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/bulk-import-resources-resource-generation-script.html): The script scans the source AWS account to get a list of active datasets and their respective active model versions.
- [Resource configuration script](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/bulk-import-resources-resource-configuration-script.html): This script configures the resource policies to let the target AWS account bulk import the resources.
- [Bulk import script](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/bulk-import-trigger-script.html): This script scans the CSV file that the creates.


## [Scheduling inference](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/inference.html)

- [Managing inference schedules](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/managing-inference-schedules.html)
- [Understanding the inference process](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html): When you're planning your use of Lookout for Equipment, it may be useful to understand exactly what happens at each step of the inference process.


## [Reviewing inference results](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-results.html)

- [In the console](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-results-console.html)
- [In a JSON file](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-results-json.html): The JSON file containing the inference results is stored in the Amazon Simple Storage Service (Amazon S3) bucket that you've specified.


## [Best practices](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html)

- [Choosing the right application](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/the-right-app.html): Choosing the right application of Lookout for Equipment involves finding the right combination of business value, equipment operations, and available data.
- [Choosing the right data](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/the-right-data.html): Your dataset should contain time-series data that's generated from an industrial asset such as a pump, compressor, motor, and so on.
- [Evaluating the output](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/evaluating-output.html): After a model is trained, Lookout for Equipment evaluates its performance on a subset of the dataset that you've specified for evaluation purposes.
- [Improving your results](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/improve-your-results.html): To improve the results, consider the following:
- [Consulting subject matter experts](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/sme.html): Lookout for Equipment identifies patterns in the dataset that help to detect critical issues, but it's the responsibility of a technician or subject matter expert (SME) to diagnose the problem and take corrective action, if needed.


## [Security](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/security.html)

### [Data protection](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Lookout for Equipment.

- [Encryption at rest](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/encryption-at-rest.html): Amazon Lookout for Equipment encrypts your data at rest with your choice of an encryption key.
- [Encryption in transit](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/encryption-in-transit.html): Amazon Lookout for Equipment copies data out of your account and processes it in an internal AWS system.
- [Key management](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/key-management.html): Amazon Lookout for Equipment encrypts your data using one of the following types of keys:

### [Identity and access management](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/security-iam.html)

Learn how to authenticate requests and manage access to your Amazon Lookout for Equipment resources.

- [AWS Identity and Access Management for Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Lookout for Equipment, learn what IAM features are available to use with Amazon Lookout for Equipment.
- [Identity-based policy examples](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Lookout for Equipment resources.
- [Amazon Web Services managed policies](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for Lookout for Equipment and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Lookout for Equipment and IAM.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Lookout for Equipment without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Compliance validation](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/SERVICENAME-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Lookout for Equipment features for data resiliency.


## [Monitoring Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/monitoring-cloudwatch.html): You can monitor Lookout for Equipment using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.


## [API Reference](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_Operations.html)

The following actions are supported:

- [CreateDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateDataset.html): Creates a container for a collection of data being ingested for analysis.
- [CreateInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateInferenceScheduler.html): Creates a scheduled inference.
- [CreateLabel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateLabel.html): Creates a label for an event.
- [CreateLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateLabelGroup.html): Creates a group of labels.
- [CreateModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateModel.html): Creates a machine learning model for data inference.
- [CreateRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateRetrainingScheduler.html): Creates a retraining scheduler on the specified model.
- [DeleteDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteDataset.html): Deletes a dataset and associated artifacts.
- [DeleteInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteInferenceScheduler.html): Deletes an inference scheduler that has been set up.
- [DeleteLabel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteLabel.html): Deletes a label.
- [DeleteLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteLabelGroup.html): Deletes a group of labels.
- [DeleteModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteModel.html): Deletes a machine learning model currently available for Amazon Lookout for Equipment.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteResourcePolicy.html): Deletes the resource policy attached to the resource.
- [DeleteRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteRetrainingScheduler.html): Deletes a retraining scheduler from a model.
- [DescribeDataIngestionJob](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeDataIngestionJob.html): Provides information on a specific data ingestion job such as creation time, dataset ARN, and status.
- [DescribeDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeDataset.html): Provides a JSON description of the data in each time series dataset, including names, column names, and data types.
- [DescribeInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeInferenceScheduler.html): Specifies information about the inference scheduler being used, including name, model, status, and associated metadata
- [DescribeLabel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeLabel.html): Returns the name of the label.
- [DescribeLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeLabelGroup.html): Returns information about the label group.
- [DescribeModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeModel.html): Provides a JSON containing the overall information about a specific machine learning model, including model name and ARN, dataset, training and evaluation information, status, and so on.
- [DescribeModelVersion](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeModelVersion.html): Retrieves information about a specific machine learning model version.
- [DescribeResourcePolicy](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeResourcePolicy.html): Provides the details of a resource policy attached to a resource.
- [DescribeRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeRetrainingScheduler.html): Provides a description of the retraining scheduler, including information such as the model name and retraining parameters.
- [ImportDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ImportDataset.html): Imports a dataset.
- [ImportModelVersion](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ImportModelVersion.html): Imports a model that has been trained successfully.
- [ListDataIngestionJobs](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListDataIngestionJobs.html): Provides a list of all data ingestion jobs, including dataset name and ARN, S3 location of the input data, status, and so on.
- [ListDatasets](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListDatasets.html): Lists all datasets currently available in your account, filtering on the dataset name.
- [ListInferenceEvents](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListInferenceEvents.html): Lists all inference events that have been found for the specified inference scheduler.
- [ListInferenceExecutions](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListInferenceExecutions.html): Lists all inference executions that have been performed by the specified inference scheduler.
- [ListInferenceSchedulers](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListInferenceSchedulers.html): Retrieves a list of all inference schedulers currently available for your account.
- [ListLabelGroups](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListLabelGroups.html): Returns a list of the label groups.
- [ListLabels](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListLabels.html): Provides a list of labels.
- [ListModels](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListModels.html): Generates a list of all models in the account, including model name and ARN, dataset, and status.
- [ListModelVersions](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListModelVersions.html): Generates a list of all model versions for a given model, including the model version, model version ARN, and status.
- [ListRetrainingSchedulers](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListRetrainingSchedulers.html): Lists all retraining schedulers in your account, filtering by model name prefix and status.
- [ListSensorStatistics](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListSensorStatistics.html): Lists statistics about the data collected for each of the sensors that have been successfully ingested in the particular dataset.
- [ListTagsForResource](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListTagsForResource.html): Lists all the tags for a specified resource, including key and value.
- [PutResourcePolicy](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_PutResourcePolicy.html): Creates a resource control policy for a given resource.
- [StartDataIngestionJob](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StartDataIngestionJob.html): Starts a data ingestion job.
- [StartInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StartInferenceScheduler.html): Starts an inference scheduler.
- [StartRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StartRetrainingScheduler.html): Starts a retraining scheduler.
- [StopInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StopInferenceScheduler.html): Stops an inference scheduler.
- [StopRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StopRetrainingScheduler.html): Stops a retraining scheduler.
- [TagResource](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_TagResource.html): Associates a given tag to a resource in your account.
- [UntagResource](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UntagResource.html): Removes a specific tag from a given resource.
- [UpdateActiveModelVersion](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateActiveModelVersion.html): Sets the active model version for a given machine learning model.
- [UpdateInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateInferenceScheduler.html): Updates an inference scheduler.
- [UpdateLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateLabelGroup.html): Updates the label group.
- [UpdateModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateModel.html): Updates a model in the account.
- [UpdateRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateRetrainingScheduler.html): Updates a retraining scheduler.

### [Data Types](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_Types.html)

The following data types are supported:

- [CategoricalValues](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CategoricalValues.html): Entity that comprises information on categorical values in data.
- [CountPercent](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CountPercent.html): Entity that comprises information of count and percentage.
- [DataIngestionJobSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DataIngestionJobSummary.html): Provides information about a specified data ingestion job, including dataset information, data ingestion configuration, and status.
- [DataPreProcessingConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DataPreProcessingConfiguration.html): The configuration is the TargetSamplingRate, which is the sampling rate of the data after post processing by Amazon Lookout for Equipment.
- [DataQualitySummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DataQualitySummary.html): DataQualitySummary gives aggregated statistics over all the sensors about a completed ingestion job.
- [DatasetSchema](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DatasetSchema.html): Provides information about the data schema used with the given dataset.
- [DatasetSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DatasetSummary.html): Contains information about the specific data set, including name, ARN, and status.
- [DuplicateTimestamps](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DuplicateTimestamps.html): Entity that comprises information abount duplicate timestamps in the dataset.
- [InferenceEventSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceEventSummary.html): Contains information about the specific inference event, including start and end time, diagnostics information, event duration and so on.
- [InferenceExecutionSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceExecutionSummary.html): Contains information about the specific inference execution, including input and output data configuration, inference scheduling information, status, and so on.
- [InferenceInputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceInputConfiguration.html): Specifies configuration information for the input data for the inference, including Amazon S3 location of input data..
- [InferenceInputNameConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceInputNameConfiguration.html): Specifies configuration information for the input data for the inference, including timestamp format and delimiter.
- [InferenceOutputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceOutputConfiguration.html): Specifies configuration information for the output results from for the inference, including KMS key ID and output S3 location.
- [InferenceS3InputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceS3InputConfiguration.html): Specifies configuration information for the input data for the inference, including input data S3 location.
- [InferenceS3OutputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceS3OutputConfiguration.html): Specifies configuration information for the output results from the inference, including output S3 location.
- [InferenceSchedulerSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InferenceSchedulerSummary.html): Contains information about the specific inference scheduler, including data delay offset, model name and ARN, status, and so on.
- [IngestedFilesSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_IngestedFilesSummary.html): Gives statistics about how many files have been ingested, and which files have not been ingested, for a particular ingestion job.
- [IngestionInputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_IngestionInputConfiguration.html): Specifies configuration information for the input data for the data ingestion job, including input data S3 location.
- [IngestionS3InputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_IngestionS3InputConfiguration.html): Specifies S3 configuration information for the input data for the data ingestion job.
- [InsufficientSensorData](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InsufficientSensorData.html): Entity that comprises aggregated information on sensors having insufficient data.
- [InvalidSensorData](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_InvalidSensorData.html): Entity that comprises aggregated information on sensors having insufficient data.
- [LabelGroupSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_LabelGroupSummary.html): Contains information about the label group.
- [LabelsInputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_LabelsInputConfiguration.html): Contains the configuration information for the S3 location being used to hold label data.
- [LabelsS3InputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_LabelsS3InputConfiguration.html): The location information (prefix and bucket name) for the s3 location being used for label data.
- [LabelSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_LabelSummary.html): Information about the label.
- [LargeTimestampGaps](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_LargeTimestampGaps.html): Entity that comprises information on large gaps between consecutive timestamps in data.
- [MissingCompleteSensorData](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_MissingCompleteSensorData.html): Entity that comprises information on sensors that have sensor data completely missing.
- [MissingSensorData](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_MissingSensorData.html): Entity that comprises aggregated information on sensors having missing data.
- [ModelDiagnosticsOutputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ModelDiagnosticsOutputConfiguration.html): Output configuration information for the pointwise model diagnostics for an Amazon Lookout for Equipment model.
- [ModelDiagnosticsS3OutputConfiguration](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ModelDiagnosticsS3OutputConfiguration.html): The Amazon S3 location for the pointwise model diagnostics for an Amazon Lookout for Equipment model.
- [ModelSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ModelSummary.html): Provides information about the specified machine learning model, including dataset and model names and ARNs, as well as status.
- [ModelVersionSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ModelVersionSummary.html): Contains information about the specific model version.
- [MonotonicValues](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_MonotonicValues.html): Entity that comprises information on monotonic values in the data.
- [MultipleOperatingModes](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_MultipleOperatingModes.html): Entity that comprises information on operating modes in data.
- [RetrainingSchedulerSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_RetrainingSchedulerSummary.html): Provides information about the specified retraining scheduler, including model name, status, start date, frequency, and lookback window.
- [S3Object](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_S3Object.html): Contains information about an S3 bucket.
- [SensorStatisticsSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_SensorStatisticsSummary.html): Summary of ingestion statistics like whether data exists, number of missing values, number of invalid values and so on related to the particular sensor.
- [SensorsWithShortDateRange](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_SensorsWithShortDateRange.html): Entity that comprises information on sensors that have shorter date range.
- [Tag](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_Tag.html): A tag is a key-value pair that can be added to a resource as metadata.
- [UnsupportedTimestamps](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UnsupportedTimestamps.html): Entity that comprises information abount unsupported timestamps in the dataset.
- [Common Errors](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
