# Source: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/llms.txt

# AWS Diagnostic Tools AWS Diagnostic Tools API Reference

> AWS Diagnostic Tools provides an HTTP endpoint to self diagnose common troubleshooting issues with AWS Services.

- [Welcome](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Operations.html)

- [GetExecution](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_GetExecution.html): Retrieve an execution by its id.
- [GetExecutionOutput](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_GetExecutionOutput.html): Retrieve the output for an Execution using its ID.
- [GetTool](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_GetTool.html): Retrieve a tool (optionally a specific version) by its id and versionId.
- [ListExecutions](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ListExecutions.html): List all of the executions available for the current user.
- [ListTagsForResource](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ListTagsForResource.html): Returns a list of the tags assigned to the specified resource.
- [ListTools](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ListTools.html): List all of the available tools.
- [StartExecution](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_StartExecution.html): Triggers new execution of a specific tool.
- [TagResource](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_TagResource.html): Adds or overwrites one or more tags for the specified resource.
- [UntagResource](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_UntagResource.html): Removes tag keys from the specified resource.


## [Data Types](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Types.html)

- [Execution](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Execution.html): Information about Diagnostic Tool Execution.
- [ExecutionSummary](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ExecutionSummary.html): Information about the Execution.
- [Tag](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Tag.html): Tag is key and value pair that act as metadata for organizing your AWS resources.
- [Tool](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Tool.html): Information about a Diagnostic Tool.
- [ToolSummary](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ToolSummary.html): Information about the Diagnostic Tool.
- [ToolVersion](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ToolVersion.html): Information about the specific Diagnostic Tool Version.
- [ValidationExceptionField](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ValidationExceptionField.html): Returns information about a field passed inside a request that resulted in an exception.
