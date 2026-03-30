# Source: https://docs.aws.amazon.com/scheduler/latest/APIReference/llms.txt

# EventBridge Scheduler API Reference

> Amazon EventBridge Scheduler is a serverless scheduler that allows you to create, run, and manage tasks from one central, managed service. EventBridge Scheduler delivers your tasks reliably, with built-in mechanisms that adjust your schedules based on the availability of downstream targets. The following reference lists the available API actions, and data types for EventBridge Scheduler.

- [Welcome](https://docs.aws.amazon.com/scheduler/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/scheduler/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/scheduler/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_Operations.html)

- [CreateSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CreateSchedule.html): Creates the specified schedule.
- [CreateScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CreateScheduleGroup.html): Creates the specified schedule group.
- [DeleteSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeleteSchedule.html): Deletes the specified schedule.
- [DeleteScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeleteScheduleGroup.html): Deletes the specified schedule group.
- [GetSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_GetSchedule.html): Retrieves the specified schedule.
- [GetScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_GetScheduleGroup.html): Retrieves the specified schedule group.
- [ListScheduleGroups](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListScheduleGroups.html): Returns a paginated list of your schedule groups.
- [ListSchedules](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListSchedules.html): Returns a paginated list of your EventBridge Scheduler schedules.
- [ListTagsForResource](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListTagsForResource.html): Lists the tags associated with the Scheduler resource.
- [TagResource](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified EventBridge Scheduler resource.
- [UntagResource](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified EventBridge Scheduler schedule group.
- [UpdateSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_UpdateSchedule.html): Updates the specified schedule.


## [Data Types](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_Types.html)

- [AwsVpcConfiguration](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_AwsVpcConfiguration.html): This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used.
- [CapacityProviderStrategyItem](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CapacityProviderStrategyItem.html): The details of a capacity provider strategy.
- [DeadLetterConfig](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeadLetterConfig.html): An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule.
- [EcsParameters](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_EcsParameters.html): The templated target type for the Amazon ECS RunTask API operation.
- [EventBridgeParameters](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_EventBridgeParameters.html): The templated target type for the EventBridge PutEvents API operation.
- [FlexibleTimeWindow](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_FlexibleTimeWindow.html): Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.
- [KinesisParameters](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_KinesisParameters.html): The templated target type for the Amazon Kinesis PutRecord API operation.
- [NetworkConfiguration](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_NetworkConfiguration.html): Specifies the network configuration for an ECS task.
- [PlacementConstraint](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_PlacementConstraint.html): An object representing a constraint on task placement.
- [PlacementStrategy](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_PlacementStrategy.html): The task placement strategy for a task or service.
- [RetryPolicy](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_RetryPolicy.html): A RetryPolicy object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.
- [SageMakerPipelineParameter](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_SageMakerPipelineParameter.html): The name and value pair of a parameter to use to start execution of a SageMaker Model Building Pipeline.
- [SageMakerPipelineParameters](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_SageMakerPipelineParameters.html): The templated target type for the Amazon SageMaker StartPipelineExecution API operation.
- [ScheduleGroupSummary](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ScheduleGroupSummary.html): The details of a schedule group.
- [ScheduleSummary](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ScheduleSummary.html): The details of a schedule.
- [SqsParameters](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_SqsParameters.html): The templated target type for the Amazon SQS SendMessage API operation.
- [Tag](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_Tag.html): Tag to associate with a schedule group.
- [Target](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_Target.html): The schedule's target.
- [TargetSummary](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_TargetSummary.html): The details of a target.
