# Source: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/llms.txt

# Network Synthetic Monitor API Reference

> Network Synthetic Monitor is feature of Network Monitoring in Amazon CloudWatch that provides visibility into the performance of network flows for your workloads, between instances in VPC subnets, as well as to and from AWS. Network Synthetic Monitor can also identify if a network issue for your workload is caused by the AWS network or is within your own company network. To configure Network Synthetic Monitor, you choose source VPCs and subnets from the AWS network that you operate within, and then, destination IP addresses from your on-premises network. Using these sources and destinations, Network Synthetic Monitor creates a monitor with all the source and destination combinations, each of which is called a probe. These probes monitor your network traffic, to help you identify where network issues might be affecting your traffic, and if the cause is an AWS network impairment.

- [Welcome](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_Operations.html)

- [CreateMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateMonitor.html): Creates a monitor between a source subnet and destination IP address.
- [CreateProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateProbe.html): Create a probe within a monitor.
- [DeleteMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteMonitor.html): Deletes a specified monitor.
- [DeleteProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteProbe.html): Deletes the specified probe.
- [GetMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetMonitor.html): Returns details about a specific monitor.
- [GetProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetProbe.html): Returns the details about a probe.
- [ListMonitors](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListMonitors.html): Returns a list of all of your monitors.
- [ListTagsForResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListTagsForResource.html): Lists the tags assigned to this resource.
- [TagResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_TagResource.html): Adds key-value pairs to a monitor or probe.
- [UntagResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UntagResource.html): Removes a key-value pair from a monitor or probe.
- [UpdateMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateMonitor.html): Updates the aggregationPeriod for a monitor.
- [UpdateProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateProbe.html): Updates a monitor probe.


## [Data Types](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_Types.html)

- [CreateMonitorProbeInput](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateMonitorProbeInput.html): Creates a monitor probe.
- [MonitorSummary](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_MonitorSummary.html): Displays summary information about a monitor.
- [Probe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_Probe.html): Describes information about a network monitor probe.
- [ProbeInput](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ProbeInput.html): Defines a probe when creating a probe or monitor.
