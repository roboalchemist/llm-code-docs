# Source: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/llms.txt

# Amazon Route 53 Application Recovery Controller API Reference Guide for Zonal Shift and Zonal Autoshift

> Welcome to the API Reference Guide for zonal shift and zonal autoshift in Amazon Application Recovery Controller (ARC).

- [Welcome](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_Operations.html)

- [CancelPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelPracticeRun.html): Cancel an in-progress practice run zonal shift in Amazon Application Recovery Controller.
- [CancelZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelZonalShift.html): Cancel a zonal shift in Amazon Application Recovery Controller.
- [CreatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CreatePracticeRunConfiguration.html): A practice run configuration for zonal autoshift is required when you enable zonal autoshift.
- [DeletePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_DeletePracticeRunConfiguration.html): Deletes the practice run configuration for a resource.
- [GetAutoshiftObserverNotificationStatus](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetAutoshiftObserverNotificationStatus.html): Returns the status of the autoshift observer notification.
- [GetManagedResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetManagedResource.html): Get information about a resource that's been registered for zonal shifts with Amazon Application Recovery Controller in this AWS Region.
- [ListAutoshifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html): Returns the autoshifts for an AWS Region.
- [ListManagedResources](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html): Lists all the resources in your AWS account in this AWS Region that are managed for zonal shifts in Amazon Application Recovery Controller, and information about them.
- [ListZonalShifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListZonalShifts.html): By default, lists only active zonal shifts in Amazon Application Recovery Controller in your AWS account in this AWS Region.
- [StartPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartPracticeRun.html): Start an on-demand practice run zonal shift in Amazon Application Recovery Controller.
- [StartZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartZonalShift.html): You start a zonal shift to temporarily move load balancer traffic away from an Availability Zone in an AWS Region, to help your application recover immediately, for example, from a developer's bad code deployment or from an AWS infrastructure failure in a single Availability Zone.
- [UpdateAutoshiftObserverNotificationStatus](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateAutoshiftObserverNotificationStatus.html): Update the status of autoshift observer notification.
- [UpdatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdatePracticeRunConfiguration.html): Update a practice run configuration to change one or more of the following: add, change, or remove the blocking alarm; change the outcome alarm; or add, change, or remove blocking dates or time windows.
- [UpdateZonalAutoshiftConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalAutoshiftConfiguration.html): The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status.
- [UpdateZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalShift.html): Update an active zonal shift in Amazon Application Recovery Controller in your AWS account.


## [Data Types](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_Types.html)

- [AutoshiftInResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_AutoshiftInResource.html): A complex structure that lists an autoshift that is currently active for a managed resource and information about the autoshift.
- [AutoshiftSummary](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_AutoshiftSummary.html): Information about an autoshift.
- [ControlCondition](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ControlCondition.html): A control condition is an alarm that you specify for a practice run.
- [ManagedResourceSummary](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ManagedResourceSummary.html): A complex structure for a managed resource in an AWS account with information about zonal shifts and autoshifts.
- [PracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_PracticeRunConfiguration.html): A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run.
- [ZonalShiftInResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ZonalShiftInResource.html): A complex structure that lists the zonal shifts for a managed resource and their statuses for the resource.
- [ZonalShiftSummary](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ZonalShiftSummary.html): Lists information about zonal shifts in Amazon Application Recovery Controller, including zonal shifts that you start yourself and zonal shifts that ARC starts on your behalf for practice runs with zonal autoshift.
