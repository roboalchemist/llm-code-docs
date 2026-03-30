# Source: https://docs.aws.amazon.com/internet-monitor/latest/api/llms.txt

# Internet Monitor API Reference

> Internet Monitor is a feature of Amazon CloudWatch Network Monitoring that provides visibility into how internet issues impact performance and availability between your applications hosted on AWS and your end users. Internet Monitor uses the connectivity data that AWS captures from its global networking footprint to calculate a baseline of performance and availability for internet traffic. This is the same data that AWS uses to monitor internet uptime and availability. With those measurements as a baseline, Internet Monitor raises awareness for you when there are significant problems for your end users in the different geographic locations where your application runs.

- [Welcome](https://docs.aws.amazon.com/internet-monitor/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/internet-monitor/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/internet-monitor/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/internet-monitor/latest/api/API_Operations.html)

- [CreateMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_CreateMonitor.html): Creates a monitor in Internet Monitor.
- [DeleteMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_DeleteMonitor.html): Deletes a monitor in Internet Monitor.
- [GetHealthEvent](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetHealthEvent.html): Gets information that Internet Monitor has created and stored about a health event for a specified monitor.
- [GetInternetEvent](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetInternetEvent.html): Gets information that Internet Monitor has generated about an internet event.
- [GetMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetMonitor.html): Gets information about a monitor in Internet Monitor based on a monitor name.
- [GetQueryResults](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryResults.html): Return the data for a query with the Internet Monitor query interface.
- [GetQueryStatus](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryStatus.html): Returns the current status of a query for the Internet Monitor query interface, for a specified query ID and monitor.
- [ListHealthEvents](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListHealthEvents.html): Lists all health events for a monitor in Internet Monitor.
- [ListInternetEvents](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListInternetEvents.html): Lists internet events that cause performance or availability issues for client locations.
- [ListMonitors](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListMonitors.html): Lists all of your monitors for Internet Monitor and their statuses, along with the Amazon Resource Name (ARN) and name of each monitor.
- [ListTagsForResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListTagsForResource.html): Lists the tags for a resource.
- [StartQuery](https://docs.aws.amazon.com/internet-monitor/latest/api/API_StartQuery.html): Start a query to return data for a specific query type for the Internet Monitor query interface.
- [StopQuery](https://docs.aws.amazon.com/internet-monitor/latest/api/API_StopQuery.html): Stop a query that is progress for a specific monitor.
- [TagResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_TagResource.html): Adds a tag to a resource.
- [UntagResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_UntagResource.html): Removes a tag from a resource.
- [UpdateMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_UpdateMonitor.html): Updates a monitor.


## [Data Types](https://docs.aws.amazon.com/internet-monitor/latest/api/API_Types.html)

- [AvailabilityMeasurement](https://docs.aws.amazon.com/internet-monitor/latest/api/API_AvailabilityMeasurement.html): Internet Monitor calculates measurements about the availability for your application's internet traffic between client locations and AWS.
- [ClientLocation](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ClientLocation.html): The impacted location, such as a city, that AWS clients access application resources from.
- [FilterParameter](https://docs.aws.amazon.com/internet-monitor/latest/api/API_FilterParameter.html): A filter that you use with the results of a Internet Monitor query that you created and ran.
- [HealthEvent](https://docs.aws.amazon.com/internet-monitor/latest/api/API_HealthEvent.html): Information about a health event created in a monitor in Internet Monitor.
- [HealthEventsConfig](https://docs.aws.amazon.com/internet-monitor/latest/api/API_HealthEventsConfig.html): A complex type with the configuration information that determines the threshold and other conditions for when Internet Monitor creates a health event for an overall performance or availability issue, across an application's geographies.
- [ImpactedLocation](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ImpactedLocation.html): Information about a location impacted by a health event in Internet Monitor.
- [InternetEventSummary](https://docs.aws.amazon.com/internet-monitor/latest/api/API_InternetEventSummary.html): A summary of information about an internet event in Internet Monitor.
- [InternetHealth](https://docs.aws.amazon.com/internet-monitor/latest/api/API_InternetHealth.html): Internet health includes measurements calculated by Internet Monitor about the performance and availability for your application on the internet.
- [InternetMeasurementsLogDelivery](https://docs.aws.amazon.com/internet-monitor/latest/api/API_InternetMeasurementsLogDelivery.html): Publish internet measurements to an Amazon S3 bucket in addition to CloudWatch Logs.
- [LocalHealthEventsConfig](https://docs.aws.amazon.com/internet-monitor/latest/api/API_LocalHealthEventsConfig.html): A complex type with the configuration information that determines the threshold and other conditions for when Internet Monitor creates a health event for a local performance or availability issue, when scores cross a threshold for one or more city-networks.
- [Monitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_Monitor.html): The description of and information about a monitor in Internet Monitor.
- [Network](https://docs.aws.amazon.com/internet-monitor/latest/api/API_Network.html): An internet service provider (ISP) or network (ASN) in Internet Monitor.
- [NetworkImpairment](https://docs.aws.amazon.com/internet-monitor/latest/api/API_NetworkImpairment.html): Information about the network impairment for a specific network measured by Internet Monitor.
- [PerformanceMeasurement](https://docs.aws.amazon.com/internet-monitor/latest/api/API_PerformanceMeasurement.html): Internet Monitor calculates measurements about the performance for your application's internet traffic between client locations and AWS.
- [QueryField](https://docs.aws.amazon.com/internet-monitor/latest/api/API_QueryField.html): Defines a field to query for your application's Internet Monitor data.
- [RoundTripTime](https://docs.aws.amazon.com/internet-monitor/latest/api/API_RoundTripTime.html): Round-trip time (RTT) is how long it takes for a request from the user to return a response to the user.
- [S3Config](https://docs.aws.amazon.com/internet-monitor/latest/api/API_S3Config.html): The configuration for publishing Internet Monitor internet measurements to Amazon S3.
