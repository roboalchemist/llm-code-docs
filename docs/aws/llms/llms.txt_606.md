# Source: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/llms.txt

# NeptuneAnalyticsAPI Welcome

> Neptune Analytics is a new analytics database engine for Amazon Neptune that helps customers get to insights faster by quickly processing large amounts of graph data, invoking popular graph analytic algorithms in low-latency queries, and getting analytics results in seconds.

- [Welcome](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_Operations.html)

- [CancelExportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelExportTask.html): Cancel the specified export task.
- [CancelImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelImportTask.html): Deletes the specified import task.
- [CancelQuery](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelQuery.html): Cancels a specified query.
- [CreateGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraph.html): Creates a new Neptune Analytics graph.
- [CreateGraphSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphSnapshot.html): Creates a snapshot of the specific graph.
- [CreateGraphUsingImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphUsingImportTask.html): Creates a new Neptune Analytics graph and imports data into it, either from Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune database snapshot.
- [CreatePrivateGraphEndpoint](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreatePrivateGraphEndpoint.html): Create a private graph endpoint to allow private access from to the graph from within a VPC.
- [DeleteGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraph.html): Deletes the specified graph.
- [DeleteGraphSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraphSnapshot.html): Deletes the specifed graph snapshot.
- [DeletePrivateGraphEndpoint](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeletePrivateGraphEndpoint.html): Deletes a private graph endpoint.
- [ExecuteQuery](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExecuteQuery.html): Execute an openCypher query.
- [GetExportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetExportTask.html): Retrieves a specified export task.
- [GetGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraph.html): Gets information about a specified graph.
- [GetGraphSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraphSnapshot.html): Retrieves a specified graph snapshot.
- [GetGraphSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraphSummary.html): Gets a graph summary for a property graph.
- [GetImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetImportTask.html): Retrieves a specified import task.
- [GetPrivateGraphEndpoint](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetPrivateGraphEndpoint.html): Retrieves information about a specified private endpoint.
- [GetQuery](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetQuery.html): Retrieves the status of a specified query.
- [ListExportTasks](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListExportTasks.html): Retrieves a list of export tasks.
- [ListGraphs](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListGraphs.html): Lists available Neptune Analytics graphs.
- [ListGraphSnapshots](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListGraphSnapshots.html): Lists available snapshots of a specified Neptune Analytics graph.
- [ListImportTasks](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListImportTasks.html): Lists import tasks.
- [ListPrivateGraphEndpoints](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListPrivateGraphEndpoints.html): Lists private endpoints for a specified Neptune Analytics graph.
- [ListQueries](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListQueries.html): Lists active openCypher queries.
- [ListTagsForResource](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListTagsForResource.html): Lists tags associated with a specified resource.
- [ResetGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ResetGraph.html): Empties the data from a specified Neptune Analytics graph.
- [RestoreGraphFromSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_RestoreGraphFromSnapshot.html): Restores a graph from a snapshot.
- [StartExportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartExportTask.html): Export data from an existing Neptune Analytics graph to Amazon S3.
- [StartGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartGraph.html): Starts the specific graph.
- [StartImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartImportTask.html): Import data into existing Neptune Analytics graph from Amazon Simple Storage Service (S3).
- [StopGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StopGraph.html): Stops the specific graph.
- [TagResource](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_TagResource.html): Adds tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UntagResource.html): Removes the specified tags from the specified resource.
- [UpdateGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UpdateGraph.html): Updates the configuration of a specified Neptune Analytics graph


## [Data Types](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_Types.html)

- [EdgeStructure](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_EdgeStructure.html): Contains information about an edge in a Neptune Analytics graph.
- [ExportFilter](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportFilter.html): This is the top-level field for specifying vertex or edge filters.
- [ExportFilterElement](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportFilterElement.html): Specifies whihc properties of that label should be included in the export.
- [ExportFilterPropertyAttributes](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportFilterPropertyAttributes.html): A structure representing a property's attributes.
- [ExportTaskDetails](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportTaskDetails.html): Contains details about the specified export task.
- [ExportTaskSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportTaskSummary.html): Provides details about an export task.
- [GraphDataSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GraphDataSummary.html): Summary information about the graph.
- [GraphSnapshotSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GraphSnapshotSummary.html): Details about a graph snapshot.
- [GraphSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GraphSummary.html): Summary details about a graph.
- [ImportOptions](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ImportOptions.html): Options for how to perform an import.
- [ImportTaskDetails](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ImportTaskDetails.html): Contains details about an import task.
- [ImportTaskSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ImportTaskSummary.html): Details about an import task.
- [NeptuneImportOptions](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_NeptuneImportOptions.html): Options for how to import Neptune data.
- [NodeStructure](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_NodeStructure.html): Information about a node.
- [PrivateGraphEndpointSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_PrivateGraphEndpointSummary.html): Details about a private graph endpoint.
- [QuerySummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_QuerySummary.html): Details of the query listed.
- [VectorSearchConfiguration](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_VectorSearchConfiguration.html): Specifies the number of dimensions for vector embeddings loaded into the graph.
