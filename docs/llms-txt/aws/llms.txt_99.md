# Source: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/llms.txt

# Application Signals Welcome

> Use CloudWatch Application Signals for comprehensive observability of your cloud-based applications. It enables real-time service health dashboards and helps you track long-term performance trends against your business goals. The application-centric view provides you with unified visibility across your applications, services, and dependencies, so you can proactively monitor and efficiently triage any issues that may arise, ensuring optimal customer experience.

- [Welcome](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Operations.html)

- [BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html): Use this operation to retrieve one or more service level objective (SLO) budget reports.
- [BatchUpdateExclusionWindows](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindows.html): Add or remove time window exclusions for one or more Service Level Objectives (SLOs).
- [CreateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html): Creates a service level objective (SLO), which can help you ensure that your critical business operations are meeting customer expectations.
- [DeleteGroupingConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteGroupingConfiguration.html): Deletes the grouping configuration for this account.
- [DeleteServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html): Deletes the specified service level objective.
- [GetService](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html): Returns information about a service discovered by Application Signals.
- [GetServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetServiceLevelObjective.html): Returns information about one SLO created in the account.
- [ListAuditFindings](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListAuditFindings.html): Returns a list of audit findings that provide automated analysis of service behavior and root cause analysis.
- [ListEntityEvents](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListEntityEvents.html): Returns a list of change events for a specific entity, such as deployments, configuration changes, or other state-changing activities.
- [ListGroupingAttributeDefinitions](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListGroupingAttributeDefinitions.html): Returns the current grouping configuration for this account, including all custom grouping attribute definitions that have been configured.
- [ListServiceDependencies](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html): Returns a list of service dependencies of the service that you specify.
- [ListServiceDependents](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependents.html): Returns the list of dependents that invoked the specified service during the provided time range.
- [ListServiceLevelObjectiveExclusionWindows](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectiveExclusionWindows.html): Retrieves all exclusion windows configured for a specific SLO.
- [ListServiceLevelObjectives](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html): Returns a list of SLOs created in this account.
- [ListServiceOperations](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceOperations.html): Returns a list of the operations of this service that have been discovered by Application Signals.
- [ListServices](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html): Returns a list of services that have been discovered by Application Signals.
- [ListServiceStates](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceStates.html): Returns information about the last deployment and other change states of services.
- [ListTagsForResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListTagsForResource.html): Displays the tags associated with a CloudWatch resource.
- [PutGroupingConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_PutGroupingConfiguration.html): Creates or updates the grouping configuration for this account.
- [StartDiscovery](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html): Enables this AWS account to be able to use CloudWatch Application Signals by creating the AWSServiceRoleForCloudWatchApplicationSignals service-linked role.
- [TagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified CloudWatch resource, such as a service level objective.
- [UntagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified resource.
- [UpdateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html): Updates an existing service level objective (SLO).


## [Data Types](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Types.html)

- [AttributeFilter](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AttributeFilter.html): A structure that defines a filter for narrowing down results based on specific attribute values.
- [AuditFinding](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditFinding.html): A structure that contains information about an audit finding, which represents an automated analysis result about service behavior, performance issues, or potential problems identified through heuristic algorithms.
- [AuditorResult](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditorResult.html): A structure that contains the result of an automated audit analysis, including the auditor name, description of findings, additional data, and severity level.
- [AuditTarget](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditTarget.html): A structure that specifies the target entity for audit analysis, such as a service, SLO, service_operation, or canary.
- [AuditTargetEntity](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditTargetEntity.html): A union structure that contains the specific entity information for different types of audit targets.
- [BatchUpdateExclusionWindowsError](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindowsError.html): An array of structures, where each structure includes an error indicating that one of the requests in the array was not valid.
- [BurnRateConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BurnRateConfiguration.html): This object defines the length of the look-back window used to calculate one burn rate metric for this SLO.
- [CalendarInterval](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CalendarInterval.html): If the interval for this service level objective is a calendar interval, this structure contains the interval specifications.
- [CanaryEntity](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CanaryEntity.html): A structure that contains identifying information for a CloudWatch Synthetics canary entity used in audit targeting.
- [ChangeEvent](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ChangeEvent.html): A structure that contains information about a change event that occurred for a service, such as a deployment or configuration change.
- [DependencyConfig](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DependencyConfig.html): Identifies the dependency using the DependencyKeyAttributes and DependencyOperationName.
- [DependencyGraph](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DependencyGraph.html): A structure that represents the dependency relationships relevant to an audit finding, containing nodes and edges that show how services and resources are connected.
- [Dimension](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Dimension.html): A dimension is a name/value pair that is part of the identity of a metric.
- [Edge](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Edge.html): A structure that represents a connection between two nodes in a dependency graph, showing the relationship and characteristics of the connection.
- [ExclusionWindow](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ExclusionWindow.html): The core SLO time window exclusion object that includes Window, StartTime, RecurrenceRule, and Reason.
- [Goal](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Goal.html): This structure contains the attributes that determine the goal of an SLO.
- [GroupingAttributeDefinition](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GroupingAttributeDefinition.html): A structure that defines how services should be grouped based on specific attributes.
- [GroupingConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GroupingConfiguration.html): A structure that contains the complete grouping configuration for an account, including all defined grouping attributes and metadata about when it was last updated.
- [Interval](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Interval.html): The time period used to evaluate the SLO.
- [Metric](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Metric.html): This structure defines the metric used for a service level indicator, including the metric name, namespace, and dimensions
- [MetricDataQuery](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricDataQuery.html): Use this structure to define a metric or metric math expression that you want to use as for a service level objective.
- [MetricGraph](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricGraph.html): A structure that contains metric data queries and time range information that provides context for audit findings through relevant performance metrics.
- [MetricReference](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricReference.html): This structure contains information about one CloudWatch metric associated with this entity discovered by Application Signals.
- [MetricStat](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricStat.html): This structure defines the metric to be used as the service level indicator, along with the statistics, period, and unit.
- [MonitoredRequestCountMetricDataQueries](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MonitoredRequestCountMetricDataQueries.html): This structure defines the metric that is used as the "good request" or "bad request" value for a request-based SLO.
- [Node](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Node.html): A structure that represents a node in a dependency graph, containing information about a service, resource, or other entity and its characteristics.
- [RecurrenceRule](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RecurrenceRule.html): The recurrence rule for the SLO time window exclusion .
- [RequestBasedServiceLevelIndicator](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RequestBasedServiceLevelIndicator.html): This structure contains information about the performance metric that a request-based SLO monitors.
- [RequestBasedServiceLevelIndicatorConfig](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RequestBasedServiceLevelIndicatorConfig.html): This structure specifies the information about the service and the performance metric that a request-based SLO is to monitor.
- [RequestBasedServiceLevelIndicatorMetric](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RequestBasedServiceLevelIndicatorMetric.html): This structure contains the information about the metric that is used for a request-based SLO.
- [RequestBasedServiceLevelIndicatorMetricConfig](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RequestBasedServiceLevelIndicatorMetricConfig.html): Use this structure to specify the information for the metric that a period-based SLO will monitor.
- [RollingInterval](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RollingInterval.html): If the interval for this SLO is a rolling interval, this structure contains the interval specifications.
- [Service](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Service.html): This structure contains information about one of your services that was discovered by Application Signals.
- [ServiceDependency](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceDependency.html): This structure contains information about one dependency of this service.
- [ServiceDependent](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceDependent.html): This structure contains information about a service dependent that was discovered by Application Signals.
- [ServiceEntity](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceEntity.html): A structure that contains identifying information for a service entity.
- [ServiceGroup](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceGroup.html): A structure that represents a logical grouping of services based on shared attributes such as business unit, environment, or entry point.
- [ServiceLevelIndicator](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicator.html): This structure contains information about the performance metric that a period-based SLO monitors.
- [ServiceLevelIndicatorConfig](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicatorConfig.html): This structure specifies the information about the service and the performance metric that a period-based SLO is to monitor.
- [ServiceLevelIndicatorMetric](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicatorMetric.html): This structure contains the information about the metric that is used for a period-based SLO.
- [ServiceLevelIndicatorMetricConfig](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicatorMetricConfig.html): Use this structure to specify the information for the metric that a period-based SLO will monitor.
- [ServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjective.html): A structure containing information about one service level objective (SLO) that has been created in Application Signals.
- [ServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjectiveBudgetReport.html): A structure containing an SLO budget report that you have requested.
- [ServiceLevelObjectiveBudgetReportError](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjectiveBudgetReportError.html): A structure containing information about one error that occurred during a BatchGetServiceLevelObjectiveBudgetReport operation.
- [ServiceLevelObjectiveEntity](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjectiveEntity.html): A structure that contains identifying information for a service level objective entity.
- [ServiceLevelObjectiveSummary](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjectiveSummary.html): A structure that contains information about one service level objective (SLO) created in Application Signals.
- [ServiceOperation](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceOperation.html): This structure contains information about an operation discovered by Application Signals.
- [ServiceOperationEntity](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceOperationEntity.html): A structure that contains identifying information for a service operation entity.
- [ServiceState](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceState.html): A structure that contains information about the current state of a service, including its latest change events such as deployments and other state-changing activities.
- [ServiceSummary](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceSummary.html): This structure contains information about one of your services that was discovered by Application Signals
- [Tag](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Tag.html): A key-value pair associated with a resource.
- [Window](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Window.html): The object that defines the time length of an exclusion window.
