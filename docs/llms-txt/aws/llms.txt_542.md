# Source: https://docs.aws.amazon.com/machine-learning/latest/APIReference/llms.txt

# MachineLearning API Reference

> Definition of the public APIs exposed by Amazon Machine Learning

- [Welcome](https://docs.aws.amazon.com/machine-learning/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/machine-learning/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/machine-learning/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Operations.html)

- [AddTags](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_AddTags.html): Adds one or more tags to an object, up to a limit of 10.
- [CreateBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateBatchPrediction.html): Generates predictions for a group of observations.
- [CreateDataSourceFromRDS](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromRDS.html): Creates a DataSource object from an Amazon Relational Database Service (Amazon RDS).
- [CreateDataSourceFromRedshift](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromRedshift.html): Creates a DataSource from a database hosted on an Amazon Redshift cluster.
- [CreateDataSourceFromS3](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromS3.html): Creates a DataSource object.
- [CreateEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateEvaluation.html): Creates a new Evaluation of an MLModel.
- [CreateMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateMLModel.html): Creates a new MLModel using the DataSource and the recipe as information sources.
- [CreateRealtimeEndpoint](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateRealtimeEndpoint.html): Creates a real-time endpoint for the MLModel.
- [DeleteBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteBatchPrediction.html): Assigns the DELETED status to a BatchPrediction, rendering it unusable.
- [DeleteDataSource](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteDataSource.html): Assigns the DELETED status to a DataSource, rendering it unusable.
- [DeleteEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteEvaluation.html): Assigns the DELETED status to an Evaluation, rendering it unusable.
- [DeleteMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteMLModel.html): Assigns the DELETED status to an MLModel, rendering it unusable.
- [DeleteRealtimeEndpoint](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteRealtimeEndpoint.html): Deletes a real time endpoint of an MLModel.
- [DeleteTags](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteTags.html): Deletes the specified tags associated with an ML object.
- [DescribeBatchPredictions](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeBatchPredictions.html): Returns a list of BatchPrediction operations that match the search criteria in the request.
- [DescribeDataSources](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeDataSources.html): Returns a list of DataSource that match the search criteria in the request.
- [DescribeEvaluations](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeEvaluations.html): Returns a list of DescribeEvaluations that match the search criteria in the request.
- [DescribeMLModels](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeMLModels.html): Returns a list of MLModel that match the search criteria in the request.
- [DescribeTags](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeTags.html): Describes one or more of the tags for your Amazon ML object.
- [GetBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetBatchPrediction.html): Returns a BatchPrediction that includes detailed metadata, status, and data file information for a Batch Prediction request.
- [GetDataSource](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetDataSource.html): Returns a DataSource that includes metadata and data file information, as well as the current status of the DataSource.
- [GetEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetEvaluation.html): Returns an Evaluation that includes metadata as well as the current status of the Evaluation.
- [GetMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetMLModel.html): Returns an MLModel that includes detailed metadata, data source information, and the current status of the MLModel.
- [Predict](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Predict.html): Generates a prediction for the observation using the specified ML Model.
- [UpdateBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateBatchPrediction.html): Updates the BatchPredictionName of a BatchPrediction.
- [UpdateDataSource](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateDataSource.html): Updates the DataSourceName of a DataSource.
- [UpdateEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateEvaluation.html): Updates the EvaluationName of an Evaluation.
- [UpdateMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateMLModel.html): Updates the MLModelName and the ScoreThreshold of an MLModel.


## [Data Types](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Types.html)

- [BatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_BatchPrediction.html): Represents the output of a GetBatchPrediction operation.
- [DataSource](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DataSource.html): Represents the output of the GetDataSource operation.
- [Evaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Evaluation.html): Represents the output of GetEvaluation operation.
- [MLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_MLModel.html): Represents the output of a GetMLModel operation.
- [PerformanceMetrics](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_PerformanceMetrics.html): Measurements of how well the MLModel performed on known observations.
- [Prediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Prediction.html): The output from a Predict operation:
- [RDSDatabase](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RDSDatabase.html): The database details of an Amazon RDS database.
- [RDSDatabaseCredentials](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RDSDatabaseCredentials.html): The database credentials to connect to a database on an RDS DB instance.
- [RDSDataSpec](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RDSDataSpec.html): The data specification of an Amazon Relational Database Service (Amazon RDS) DataSource.
- [RDSMetadata](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RDSMetadata.html): The datasource details that are specific to Amazon RDS.
- [RealtimeEndpointInfo](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RealtimeEndpointInfo.html): Describes the real-time endpoint information for an MLModel.
- [RedshiftDatabase](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RedshiftDatabase.html): Describes the database details required to connect to an Amazon Redshift database.
- [RedshiftDatabaseCredentials](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RedshiftDatabaseCredentials.html): Describes the database credentials for connecting to a database on an Amazon Redshift cluster.
- [RedshiftDataSpec](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RedshiftDataSpec.html): Describes the data specification of an Amazon Redshift DataSource.
- [RedshiftMetadata](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RedshiftMetadata.html): Describes the DataSource details specific to Amazon Redshift.
- [S3DataSpec](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_S3DataSpec.html): Describes the data specification of a DataSource.
- [Tag](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Tag.html): A custom key-value pair associated with an ML object, such as an ML model.
