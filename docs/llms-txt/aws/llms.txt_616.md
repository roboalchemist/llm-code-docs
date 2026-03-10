# Source: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/llms.txt

# Network Flow Monitor API Reference

> Network Flow Monitor is a feature of Amazon CloudWatch Network Monitoring that provides visibility into the performance of network flows for your AWS workloads, between instances in subnets, as well as to and from AWS. Lightweight agents that you install on the instances capture performance metrics for your network flows, such as packet loss and latency, and send them to the Network Flow Monitor backend. Then, you can view and analyze metrics from the top contributors for each metric type, to help troubleshoot issues.

- [Welcome](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_Operations.html)

- [CreateMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateMonitor.html): Create a monitor for specific network flows between local and remote resources, so that you can monitor network performance for one or several of your workloads.
- [CreateScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateScope.html): In Network Flow Monitor, you specify a scope for the service to generate metrics for.
- [DeleteMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteMonitor.html): Deletes a monitor in Network Flow Monitor.
- [DeleteScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteScope.html): Deletes a scope that has been defined.
- [GetMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetMonitor.html): Gets information about a monitor in Network Flow Monitor based on a monitor name.
- [GetQueryResultsMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.html): Return the data for a query with the Network Flow Monitor query interface.
- [GetQueryResultsWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html): Return the data for a query with the Network Flow Monitor query interface.
- [GetQueryResultsWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributorsData.html): Return the data for a query with the Network Flow Monitor query interface.
- [GetQueryStatusMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorTopContributors.html): Returns the current status of a query for the Network Flow Monitor query interface, for a specified query ID and monitor.
- [GetQueryStatusWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributors.html): Return the data for a query with the Network Flow Monitor query interface.
- [GetQueryStatusWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributorsData.html): Returns the current status of a query for the Network Flow Monitor query interface, for a specified query ID and monitor.
- [GetScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetScope.html): Gets information about a scope, including the name, status, tags, and target details.
- [ListMonitors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListMonitors.html): List all monitors in an account.
- [ListScopes](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListScopes.html): List all the scopes for an account.
- [ListTagsForResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListTagsForResource.html): Returns all the tags for a resource.
- [StartQueryMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryMonitorTopContributors.html): Create a query that you can use with the Network Flow Monitor query interface to return the top contributors for a monitor.
- [StartQueryWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributors.html): Create a query with the Network Flow Monitor query interface that you can run to return workload insights top contributors.
- [StartQueryWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributorsData.html): Create a query with the Network Flow Monitor query interface that you can run to return data for workload insights top contributors.
- [StopQueryMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryMonitorTopContributors.html): Stop a top contributors query for a monitor.
- [StopQueryWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributors.html): Stop a top contributors query for workload insights.
- [StopQueryWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributorsData.html): Stop a top contributors data query for workload insights.
- [TagResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TagResource.html): Adds a tag to a resource.
- [UntagResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UntagResource.html): Removes a tag from a resource.
- [UpdateMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateMonitor.html): Update a monitor to add or remove local or remote resources.
- [UpdateScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateScope.html): Update a scope to add or remove resources that you want to be available for Network Flow Monitor to generate metrics for, when you have active agents on those resources sending metrics reports to the Network Flow Monitor backend.


## [Data Types](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_Types.html)

- [KubernetesMetadata](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_KubernetesMetadata.html): Meta data about Kubernetes resources.
- [MonitorLocalResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorLocalResource.html): A local resource is the host where the agent is installed.
- [MonitorRemoteResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorRemoteResource.html): A remote resource is the other endpoint in a network flow.
- [MonitorSummary](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorSummary.html): A summary of information about a monitor, including the ARN, the name, and the status.
- [MonitorTopContributorsRow](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorTopContributorsRow.html): A set of information for a top contributor network flow in a monitor.
- [ScopeSummary](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ScopeSummary.html): A summary of information about a scope, including the ARN, target ID, and AWS Region.
- [TargetId](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TargetId.html): A target ID is an internally-generated identifier for a target.
- [TargetIdentifier](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TargetIdentifier.html): A target identifier is a pair of identifying information for a scope that is included in a target.
- [TargetResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TargetResource.html): A target resource in a scope.
- [TraversedComponent](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TraversedComponent.html): A section of the network that a network flow has traveled through.
- [WorkloadInsightsTopContributorsDataPoint](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_WorkloadInsightsTopContributorsDataPoint.html): A data point for a top contributor network flow in a scope.
- [WorkloadInsightsTopContributorsRow](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_WorkloadInsightsTopContributorsRow.html): A row for a top contributor for a scope.
