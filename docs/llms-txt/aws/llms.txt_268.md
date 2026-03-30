# Source: https://docs.aws.amazon.com/datapipeline/latest/APIReference/llms.txt

# AWS Data Pipeline API Reference

> AWS Data Pipeline configures and manages a data-driven workflow called a pipeline. AWS Data Pipeline handles the details of scheduling and ensuring that data dependencies are met so that your application can focus on processing the data.

- [Welcome](https://docs.aws.amazon.com/datapipeline/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/datapipeline/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/datapipeline/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Operations.html)

- [ActivatePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ActivatePipeline.html): Validates the specified pipeline and starts processing pipeline tasks.
- [AddTags](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_AddTags.html): Adds or modifies tags for the specified pipeline.
- [CreatePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_CreatePipeline.html): Creates a new, empty pipeline.
- [DeactivatePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DeactivatePipeline.html): Deactivates the specified running pipeline.
- [DeletePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DeletePipeline.html): Deletes a pipeline, its pipeline definition, and its run history.
- [DescribeObjects](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DescribeObjects.html): Gets the object definitions for a set of objects associated with the pipeline.
- [DescribePipelines](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DescribePipelines.html): Retrieves metadata about one or more pipelines.
- [EvaluateExpression](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_EvaluateExpression.html): Task runners call EvaluateExpression to evaluate a string in the context of the specified object.
- [GetPipelineDefinition](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_GetPipelineDefinition.html): Gets the definition of the specified pipeline.
- [ListPipelines](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ListPipelines.html): Lists the pipeline identifiers for all active pipelines that you have permission to access.
- [PollForTask](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PollForTask.html): Task runners call PollForTask to receive a task to perform from AWS Data Pipeline.
- [PutPipelineDefinition](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PutPipelineDefinition.html): Adds tasks, schedules, and preconditions to the specified pipeline.
- [QueryObjects](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_QueryObjects.html): Queries the specified pipeline for the names of objects that match the specified set of conditions.
- [RemoveTags](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_RemoveTags.html): Removes existing tags from the specified pipeline.
- [ReportTaskProgress](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ReportTaskProgress.html): Task runners call ReportTaskProgress when assigned a task to acknowledge that it has the task.
- [ReportTaskRunnerHeartbeat](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ReportTaskRunnerHeartbeat.html): Task runners call ReportTaskRunnerHeartbeat every 15 minutes to indicate that they are operational.
- [SetStatus](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_SetStatus.html): Requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline.
- [SetTaskStatus](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_SetTaskStatus.html): Task runners call SetTaskStatus to notify AWS Data Pipeline that a task is completed and provide information about the final status.
- [ValidatePipelineDefinition](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ValidatePipelineDefinition.html): Validates the specified pipeline definition to ensure that it is well formed and can be run without error.


## [Data Types](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Types.html)

- [Field](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Field.html): A key-value pair that describes a property of a pipeline object.
- [InstanceIdentity](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_InstanceIdentity.html): Identity information for the EC2 instance that is hosting the task runner.
- [Operator](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Operator.html): Contains a logical operation for comparing the value of a field with a specified value.
- [ParameterAttribute](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ParameterAttribute.html): The attributes allowed or specified with a parameter object.
- [ParameterObject](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ParameterObject.html): Contains information about a parameter object.
- [ParameterValue](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ParameterValue.html): A value or list of parameter values.
- [PipelineDescription](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PipelineDescription.html): Contains pipeline metadata.
- [PipelineIdName](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PipelineIdName.html): Contains the name and identifier of a pipeline.
- [PipelineObject](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PipelineObject.html): Contains information about a pipeline object.
- [Query](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Query.html): Defines the query to run against an object.
- [Selector](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Selector.html): A comparison that is used to determine whether a query should return this object.
- [Tag](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Tag.html): Tags are key/value pairs defined by a user and associated with a pipeline to control access.
- [TaskObject](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_TaskObject.html): Contains information about a pipeline task that is assigned to a task runner.
- [ValidationError](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ValidationError.html): Defines a validation error.
- [ValidationWarning](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ValidationWarning.html): Defines a validation warning.
