# Source: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/llms.txt

# Amazon CloudWatch Application Insights Welcome

> Amazon CloudWatch Application Insights is a service that helps you detect common problems with your applications. It enables you to pinpoint the source of issues in your applications (built with technologies such as Microsoft IIS, .NET, and Microsoft SQL Server), by providing key insights into detected problems.

- [Welcome](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Operations.html)

- [AddWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_AddWorkload.html): Adds a workload to a component.
- [CreateApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateApplication.html): Adds an application that is created from a resource group.
- [CreateComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateComponent.html): Creates a custom component by grouping similar standalone instances to monitor.
- [CreateLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateLogPattern.html): Adds an log pattern to a LogPatternSet.
- [DeleteApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteApplication.html): Removes the specified application from monitoring.
- [DeleteComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteComponent.html): Ungroups a custom component.
- [DeleteLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteLogPattern.html): Removes the specified log pattern from a LogPatternSet.
- [DescribeApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeApplication.html): Describes the application.
- [DescribeComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponent.html): Describes a component and lists the resources that are grouped together in a component.
- [DescribeComponentConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.html): Describes the monitoring configuration of the component.
- [DescribeComponentConfigurationRecommendation](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.html): Describes the recommended monitoring configuration of the component.
- [DescribeLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeLogPattern.html): Describe a specific log pattern from a LogPatternSet.
- [DescribeObservation](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeObservation.html): Describes an anomaly or error with the application.
- [DescribeProblem](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblem.html): Describes an application problem.
- [DescribeProblemObservations](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblemObservations.html): Describes the anomalies or errors associated with the problem.
- [DescribeWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeWorkload.html): Describes a workload and its configuration.
- [ListApplications](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListApplications.html): Lists the IDs of the applications that you are monitoring.
- [ListComponents](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListComponents.html): Lists the auto-grouped, standalone, and custom components of the application.
- [ListConfigurationHistory](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListConfigurationHistory.html): Lists the INFO, WARN, and ERROR events for periodic configuration updates performed by Application Insights.
- [ListLogPatterns](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatterns.html): Lists the log patterns in the specific log LogPatternSet.
- [ListLogPatternSets](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatternSets.html): Lists the log pattern sets in the specific application.
- [ListProblems](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListProblems.html): Lists the problems with your application.
- [ListTagsForResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListTagsForResource.html): Retrieve a list of the tags (keys and values) that are associated with a specified application.
- [ListWorkloads](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListWorkloads.html): Lists the workloads that are configured on a given component.
- [RemoveWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_RemoveWorkload.html): Remove workload from a component.
- [TagResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_TagResource.html): Add one or more tags (keys and values) to a specified application.
- [UntagResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UntagResource.html): Remove one or more tags (keys and values) from a specified application.
- [UpdateApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateApplication.html): Updates the application.
- [UpdateComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponent.html): Updates the custom component name and/or the list of resources that make up the component.
- [UpdateComponentConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.html): Updates the monitoring configurations for the component.
- [UpdateLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateLogPattern.html): Adds a log pattern to a LogPatternSet.
- [UpdateProblem](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateProblem.html): Updates the visibility of the problem or specifies the problem as RESOLVED.
- [UpdateWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateWorkload.html): Adds a workload to a component.


## [Data Types](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Types.html)

- [ApplicationComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ApplicationComponent.html): Describes a standalone resource or similarly grouped resources that the application is made up of.
- [ApplicationInfo](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ApplicationInfo.html): Describes the status of the application.
- [ConfigurationEvent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ConfigurationEvent.html): The event information.
- [LogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_LogPattern.html): An object that defines the log patterns that belongs to a LogPatternSet.
- [Observation](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Observation.html): Describes an anomaly or error with the application.
- [Problem](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Problem.html): Describes a problem that is detected by correlating observations.
- [RelatedObservations](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_RelatedObservations.html): Describes observations related to the problem.
- [Tag](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Tag.html): An object that defines the tags associated with an application.
- [Workload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Workload.html): Describes the workloads on a component.
- [WorkloadConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_WorkloadConfiguration.html): The configuration of the workload.
