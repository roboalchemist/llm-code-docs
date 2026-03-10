# Source: https://docs.aws.amazon.com/braket/latest/APIReference/llms.txt

# Amazon Braket API Reference

> The Amazon Braket API Reference provides information about the operations and structures supported by Amazon Braket.

- [Welcome](https://docs.aws.amazon.com/braket/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/braket/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/braket/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/braket/latest/APIReference/API_Operations.html)

- [CancelJob](https://docs.aws.amazon.com/braket/latest/APIReference/API_CancelJob.html): Cancels an Amazon Braket hybrid job.
- [CancelQuantumTask](https://docs.aws.amazon.com/braket/latest/APIReference/API_CancelQuantumTask.html): Cancels the specified task.
- [CreateJob](https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateJob.html): Creates an Amazon Braket hybrid job.
- [CreateQuantumTask](https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateQuantumTask.html): Creates a quantum task.
- [CreateSpendingLimit](https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateSpendingLimit.html): Creates a spending limit for a specified quantum device.
- [DeleteSpendingLimit](https://docs.aws.amazon.com/braket/latest/APIReference/API_DeleteSpendingLimit.html): Deletes an existing spending limit.
- [GetDevice](https://docs.aws.amazon.com/braket/latest/APIReference/API_GetDevice.html): Retrieves the devices available in Amazon Braket.
- [GetJob](https://docs.aws.amazon.com/braket/latest/APIReference/API_GetJob.html): Retrieves the specified Amazon Braket hybrid job.
- [GetQuantumTask](https://docs.aws.amazon.com/braket/latest/APIReference/API_GetQuantumTask.html): Retrieves the specified quantum task.
- [ListTagsForResource](https://docs.aws.amazon.com/braket/latest/APIReference/API_ListTagsForResource.html): Shows the tags associated with this resource.
- [SearchDevices](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchDevices.html): Searches for devices using the specified filters.
- [SearchJobs](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchJobs.html): Searches for Amazon Braket hybrid jobs that match the specified filter values.
- [SearchQuantumTasks](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchQuantumTasks.html): Searches for tasks that match the specified filter values.
- [SearchSpendingLimits](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchSpendingLimits.html): Searches and lists spending limits based on specified filters.
- [TagResource](https://docs.aws.amazon.com/braket/latest/APIReference/API_TagResource.html): Add a tag to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/braket/latest/APIReference/API_UntagResource.html): Remove tags from a resource.
- [UpdateSpendingLimit](https://docs.aws.amazon.com/braket/latest/APIReference/API_UpdateSpendingLimit.html): Updates an existing spending limit.


## [Data Types](https://docs.aws.amazon.com/braket/latest/APIReference/API_Types.html)

- [ActionMetadata](https://docs.aws.amazon.com/braket/latest/APIReference/API_ActionMetadata.html): Contains metadata about the quantum task action, including the action type and program statistics.
- [AlgorithmSpecification](https://docs.aws.amazon.com/braket/latest/APIReference/API_AlgorithmSpecification.html): Defines the Amazon Braket hybrid job to be created.
- [Association](https://docs.aws.amazon.com/braket/latest/APIReference/API_Association.html): The Amazon Braket resource and the association type.
- [ContainerImage](https://docs.aws.amazon.com/braket/latest/APIReference/API_ContainerImage.html): The container image used to create an Amazon Braket hybrid job.
- [DataSource](https://docs.aws.amazon.com/braket/latest/APIReference/API_DataSource.html): Information about the source of the input data used by the Amazon Braket hybrid job.
- [DeviceConfig](https://docs.aws.amazon.com/braket/latest/APIReference/API_DeviceConfig.html): Configures the primary device used to create and run an Amazon Braket hybrid job.
- [DeviceQueueInfo](https://docs.aws.amazon.com/braket/latest/APIReference/API_DeviceQueueInfo.html): Information about quantum tasks and hybrid jobs queued on a device.
- [DeviceSummary](https://docs.aws.amazon.com/braket/latest/APIReference/API_DeviceSummary.html): Includes information about the device.
- [ExperimentalCapabilities](https://docs.aws.amazon.com/braket/latest/APIReference/API_ExperimentalCapabilities.html): Enabled experimental capabilities for quantum hardware.
- [HybridJobQueueInfo](https://docs.aws.amazon.com/braket/latest/APIReference/API_HybridJobQueueInfo.html): Information about the queue for a specified hybrid job.
- [InputFileConfig](https://docs.aws.amazon.com/braket/latest/APIReference/API_InputFileConfig.html): A list of parameters that specify the input channels, type of input data, and where it is located.
- [InstanceConfig](https://docs.aws.amazon.com/braket/latest/APIReference/API_InstanceConfig.html): Configures the resource instances to use while running the Amazon Braket hybrid job on Amazon Braket.
- [JobCheckpointConfig](https://docs.aws.amazon.com/braket/latest/APIReference/API_JobCheckpointConfig.html): Contains information about the output locations for hybrid job checkpoint data.
- [JobEventDetails](https://docs.aws.amazon.com/braket/latest/APIReference/API_JobEventDetails.html): Details about the type and time events that occurred related to the Amazon Braket hybrid job.
- [JobOutputDataConfig](https://docs.aws.amazon.com/braket/latest/APIReference/API_JobOutputDataConfig.html): Specifies the path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.
- [JobStoppingCondition](https://docs.aws.amazon.com/braket/latest/APIReference/API_JobStoppingCondition.html): Specifies limits for how long an Amazon Braket hybrid job can run.
- [JobSummary](https://docs.aws.amazon.com/braket/latest/APIReference/API_JobSummary.html): Provides summary information about an Amazon Braket hybrid job.
- [ProgramSetValidationFailure](https://docs.aws.amazon.com/braket/latest/APIReference/API_ProgramSetValidationFailure.html): Contains information about validation failures that occurred during the processing of a program set in a quantum task.
- [QuantumTaskQueueInfo](https://docs.aws.amazon.com/braket/latest/APIReference/API_QuantumTaskQueueInfo.html): The queue information for the specified quantum task.
- [QuantumTaskSummary](https://docs.aws.amazon.com/braket/latest/APIReference/API_QuantumTaskSummary.html): Includes information about a quantum task.
- [S3DataSource](https://docs.aws.amazon.com/braket/latest/APIReference/API_S3DataSource.html): Information about the Amazon S3 storage used by the Amazon Braket hybrid job.
- [ScriptModeConfig](https://docs.aws.amazon.com/braket/latest/APIReference/API_ScriptModeConfig.html): Contains information about algorithm scripts used for the Amazon Braket hybrid job.
- [SearchDevicesFilter](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchDevicesFilter.html): The filter used to search for devices.
- [SearchJobsFilter](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchJobsFilter.html): A filter used to search for Amazon Braket hybrid jobs.
- [SearchQuantumTasksFilter](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchQuantumTasksFilter.html): A filter used to search for quantum tasks.
- [SearchSpendingLimitsFilter](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchSpendingLimitsFilter.html): Specifies filter criteria for searching spending limits.
- [SpendingLimitSummary](https://docs.aws.amazon.com/braket/latest/APIReference/API_SpendingLimitSummary.html): Contains summary information about a spending limit, including current spending status and configuration details.
- [TimePeriod](https://docs.aws.amazon.com/braket/latest/APIReference/API_TimePeriod.html): Defines a time range for spending limits, specifying when the limit is active.
