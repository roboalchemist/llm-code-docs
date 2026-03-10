# Source: https://docs.aws.amazon.com/neptune/latest/data-api/llms.txt

# Neptune Data API Welcome

> The Amazon Neptune data API provides SDK support for more than 40 of Neptune's data operations, including data loading, query execution, data inquiry, and machine learning. It supports the Gremlin and openCypher query languages, and is available in all SDK languages. It automatically signs API requests and greatly simplifies integrating Neptune into your applications.

- [Welcome](https://docs.aws.amazon.com/neptune/latest/data-api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/neptune/latest/data-api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/neptune/latest/data-api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/neptune/latest/data-api/API_Operations.html)

- [CancelGremlinQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelGremlinQuery.html): Cancels a Gremlin query.
- [CancelLoaderJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelLoaderJob.html): Cancels a specified load job.
- [CancelMLDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelMLDataProcessingJob.html): Cancels a Neptune ML data processing job.
- [CancelMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelMLModelTrainingJob.html): Cancels a Neptune ML model training job.
- [CancelMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelMLModelTransformJob.html): Cancels a specified model transform job.
- [CancelOpenCypherQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelOpenCypherQuery.html): Cancels a specified openCypher query.
- [CreateMLEndpoint](https://docs.aws.amazon.com/neptune/latest/data-api/API_CreateMLEndpoint.html): Creates a new Neptune ML inference endpoint that lets you query one specific model that the model-training process constructed.
- [DeleteMLEndpoint](https://docs.aws.amazon.com/neptune/latest/data-api/API_DeleteMLEndpoint.html): Cancels the creation of a Neptune ML inference endpoint.
- [DeletePropertygraphStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_DeletePropertygraphStatistics.html): Deletes statistics for Gremlin and openCypher (property graph) data.
- [DeleteSparqlStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_DeleteSparqlStatistics.html): Deletes SPARQL statistics
- [ExecuteFastReset](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteFastReset.html): The fast reset REST API lets you reset a Neptune graph quicky and easily, removing all of its data.
- [ExecuteGremlinExplainQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteGremlinExplainQuery.html): Executes a Gremlin Explain query.
- [ExecuteGremlinProfileQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteGremlinProfileQuery.html): Executes a Gremlin Profile query, which runs a specified traversal, collects various metrics about the run, and produces a profile report as output.
- [ExecuteGremlinQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteGremlinQuery.html): This commands executes a Gremlin query.
- [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteOpenCypherExplainQuery.html): Executes an openCypher explain request.
- [ExecuteOpenCypherQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteOpenCypherQuery.html): Executes an openCypher query.
- [GetEngineStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetEngineStatus.html): Retrieves the status of the graph database on the host.
- [GetGremlinQueryStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetGremlinQueryStatus.html): Gets the status of a specified Gremlin query.
- [GetLoaderJobStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetLoaderJobStatus.html): Gets status information about a specified load job.
- [GetMLDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLDataProcessingJob.html): Retrieves information about a specified data processing job.
- [GetMLEndpoint](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLEndpoint.html): Retrieves details about an inference endpoint.
- [GetMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLModelTrainingJob.html): Retrieves information about a Neptune ML model training job.
- [GetMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLModelTransformJob.html): Gets information about a specified model transform job.
- [GetOpenCypherQueryStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetOpenCypherQueryStatus.html): Retrieves the status of a specified openCypher query.
- [GetPropertygraphStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetPropertygraphStatistics.html): Gets property graph statistics (Gremlin and openCypher).
- [GetPropertygraphStream](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetPropertygraphStream.html): Gets a stream for a property graph.
- [GetPropertygraphSummary](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetPropertygraphSummary.html): Gets a graph summary for a property graph.
- [GetRDFGraphSummary](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetRDFGraphSummary.html): Gets a graph summary for an RDF graph.
- [GetSparqlStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetSparqlStatistics.html): Gets RDF statistics (SPARQL).
- [GetSparqlStream](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetSparqlStream.html): Gets a stream for an RDF graph.
- [ListGremlinQueries](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListGremlinQueries.html): Lists active Gremlin queries.
- [ListLoaderJobs](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListLoaderJobs.html): Retrieves a list of the loadIds for all active loader jobs.
- [ListMLDataProcessingJobs](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListMLDataProcessingJobs.html): Returns a list of Neptune ML data processing jobs.
- [ListMLEndpoints](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListMLEndpoints.html): Lists existing inference endpoints.
- [ListMLModelTrainingJobs](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListMLModelTrainingJobs.html): Lists Neptune ML model-training jobs.
- [ListMLModelTransformJobs](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListMLModelTransformJobs.html): Returns a list of model transform job IDs.
- [ListOpenCypherQueries](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListOpenCypherQueries.html): Lists active openCypher queries.
- [ManagePropertygraphStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_ManagePropertygraphStatistics.html): Manages the generation and use of property graph statistics.
- [ManageSparqlStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_ManageSparqlStatistics.html): Manages the generation and use of RDF graph statistics.
- [StartLoaderJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartLoaderJob.html): Starts a Neptune bulk loader job to load data from an Amazon S3 bucket into a Neptune DB instance.
- [StartMLDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartMLDataProcessingJob.html): Creates a new Neptune ML data processing job for processing the graph data exported from Neptune for training.
- [StartMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartMLModelTrainingJob.html): Creates a new Neptune ML model training job.
- [StartMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartMLModelTransformJob.html): Creates a new model transform job.


## [Data Types](https://docs.aws.amazon.com/neptune/latest/data-api/API_Types.html)

- [CustomModelTrainingParameters](https://docs.aws.amazon.com/neptune/latest/data-api/API_CustomModelTrainingParameters.html): Contains custom model training parameters.
- [CustomModelTransformParameters](https://docs.aws.amazon.com/neptune/latest/data-api/API_CustomModelTransformParameters.html): Contains custom model transform parameters.
- [DeleteStatisticsValueMap](https://docs.aws.amazon.com/neptune/latest/data-api/API_DeleteStatisticsValueMap.html): The payload for DeleteStatistics.
- [EdgeStructure](https://docs.aws.amazon.com/neptune/latest/data-api/API_EdgeStructure.html): An edge structure.
- [FastResetToken](https://docs.aws.amazon.com/neptune/latest/data-api/API_FastResetToken.html): A structure containing the fast reset token used to initiate a fast reset.
- [GremlinQueryStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GremlinQueryStatus.html): Captures the status of a Gremlin query (see the Gremlin query status API page).
- [GremlinQueryStatusAttributes](https://docs.aws.amazon.com/neptune/latest/data-api/API_GremlinQueryStatusAttributes.html): Contains status components of a Gremlin query.
- [LoaderIdResult](https://docs.aws.amazon.com/neptune/latest/data-api/API_LoaderIdResult.html): Contains a list of load IDs.
- [MlConfigDefinition](https://docs.aws.amazon.com/neptune/latest/data-api/API_MlConfigDefinition.html): Contains a Neptune ML configuration.
- [MlResourceDefinition](https://docs.aws.amazon.com/neptune/latest/data-api/API_MlResourceDefinition.html): Defines a Neptune ML resource.
- [NodeStructure](https://docs.aws.amazon.com/neptune/latest/data-api/API_NodeStructure.html): A node structure.
- [PropertygraphData](https://docs.aws.amazon.com/neptune/latest/data-api/API_PropertygraphData.html): A Gremlin or openCypher change record.
- [PropertygraphRecord](https://docs.aws.amazon.com/neptune/latest/data-api/API_PropertygraphRecord.html): Structure of a property graph record.
- [PropertygraphSummary](https://docs.aws.amazon.com/neptune/latest/data-api/API_PropertygraphSummary.html): The graph summary API returns a read-only list of node and edge labels and property keys, along with counts of nodes, edges, and properties.
- [PropertygraphSummaryValueMap](https://docs.aws.amazon.com/neptune/latest/data-api/API_PropertygraphSummaryValueMap.html): Payload for the property graph summary response.
- [QueryEvalStats](https://docs.aws.amazon.com/neptune/latest/data-api/API_QueryEvalStats.html): Structure to capture query statistics such as how many queries are running, accepted or waiting and their details.
- [QueryLanguageVersion](https://docs.aws.amazon.com/neptune/latest/data-api/API_QueryLanguageVersion.html): Structure for expressing the query language version.
- [RDFGraphSummary](https://docs.aws.amazon.com/neptune/latest/data-api/API_RDFGraphSummary.html): The RDF graph summary API returns a read-only list of classes and predicate keys, along with counts of quads, subjects, and predicates.
- [RDFGraphSummaryValueMap](https://docs.aws.amazon.com/neptune/latest/data-api/API_RDFGraphSummaryValueMap.html): Payload for an RDF graph summary response.
- [RefreshStatisticsIdMap](https://docs.aws.amazon.com/neptune/latest/data-api/API_RefreshStatisticsIdMap.html): Statistics for REFRESH mode.
- [SparqlData](https://docs.aws.amazon.com/neptune/latest/data-api/API_SparqlData.html): Neptune logs are converted to SPARQL quads in the graph using the Resource Description Framework (RDF) N-QUADS language defined in the W3C RDF 1.1 N-Quads specification
- [SparqlRecord](https://docs.aws.amazon.com/neptune/latest/data-api/API_SparqlRecord.html): A serialized SPARQL stream record capturing a change-log entry for the RDF graph.
- [Statistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_Statistics.html): Contains statistics information.
- [StatisticsSummary](https://docs.aws.amazon.com/neptune/latest/data-api/API_StatisticsSummary.html): Information about the characteristic sets generated in the statistics.
- [SubjectStructure](https://docs.aws.amazon.com/neptune/latest/data-api/API_SubjectStructure.html): A subject structure.
