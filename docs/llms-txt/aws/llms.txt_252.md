# Source: https://docs.aws.amazon.com/controltower/latest/APIReference/llms.txt

# AWS Control Tower API Reference

> AWS Control Tower offers application programming interface (API) operations that support programmatic interaction with these types of resources:

- [Welcome](https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/controltower/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/controltower/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/controltower/latest/APIReference/API_Operations.html)

- [CreateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html): Creates a new landing zone.
- [DeleteLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DeleteLandingZone.html): Decommissions a landing zone.
- [DisableBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableBaseline.html): Disable an EnabledBaseline resource on the specified Target.
- [DisableControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableControl.html): This API call turns off a control.
- [EnableBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableBaseline.html): Enable (apply) a Baseline to a Target.
- [EnableControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html): This API call activates a control.
- [GetBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html): Retrieve details about an existing Baseline resource by specifying its identifier.
- [GetBaselineOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaselineOperation.html): Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: EnableBaseline, DisableBaseline, UpdateEnabledBaseline, ResetEnabledBaseline.
- [GetControlOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetControlOperation.html): Returns the status of a particular EnableControl or DisableControl operation.
- [GetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledBaseline.html): Retrieve details of an EnabledBaseline resource by specifying its identifier.
- [GetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledControl.html): Retrieves details about an enabled control.
- [GetLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZone.html): Returns details about the landing zone.
- [GetLandingZoneOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZoneOperation.html): Returns the status of the specified landing zone operation.
- [ListBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListBaselines.html): Returns a summary list of all available baselines.
- [ListControlOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListControlOperations.html): Provides a list of operations in progress or queued.
- [ListEnabledBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledBaselines.html): Returns a list of summaries describing EnabledBaseline resources.
- [ListEnabledControls](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledControls.html): Lists the controls enabled by AWS Control Tower on the specified organizational unit and the accounts it contains.
- [ListLandingZoneOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZoneOperations.html): Lists all landing zone operations from the past 90 days.
- [ListLandingZones](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZones.html): Returns the landing zone ARN for the landing zone deployed in your managed account.
- [ListTagsForResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListTagsForResource.html): Returns a list of tags associated with the resource.
- [ResetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledBaseline.html): Re-enables an EnabledBaseline resource.
- [ResetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html): Resets an enabled control.
- [ResetLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetLandingZone.html): This API call resets a landing zone.
- [TagResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_TagResource.html): Applies tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UntagResource.html): Removes tags from a resource.
- [UpdateEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledBaseline.html): Updates an EnabledBaseline resource's applied parameters or version.
- [UpdateEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledControl.html): Updates the configuration of an already enabled control.
- [UpdateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateLandingZone.html): This API call updates the landing zone.


## [Data Types](https://docs.aws.amazon.com/controltower/latest/APIReference/API_Types.html)

- [BaselineOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_BaselineOperation.html): An object of shape BaselineOperation, returning details about the specified Baseline operation ID.
- [BaselineSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_BaselineSummary.html): Returns a summary of information about a Baseline object.
- [ControlOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ControlOperation.html): An operation performed by the control.
- [ControlOperationFilter](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ControlOperationFilter.html): A filter object that lets you call ListControlOperations with a specific filter.
- [ControlOperationSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ControlOperationSummary.html): A summary of information about the specified control operation.
- [DriftStatusSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DriftStatusSummary.html): The drift summary of the enabled control.
- [EnabledBaselineDetails](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineDetails.html): Details of the EnabledBaseline resource.
- [EnabledBaselineDriftStatusSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineDriftStatusSummary.html): The drift summary of the enabled baseline.
- [EnabledBaselineDriftTypes](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineDriftTypes.html): The types of drift that can be detected for an enabled baseline.
- [EnabledBaselineFilter](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineFilter.html): A filter applied on the ListEnabledBaseline operation.
- [EnabledBaselineInheritanceDrift](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineInheritanceDrift.html): The inheritance drift summary for the enabled baseline.
- [EnabledBaselineParameter](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineParameter.html): A key-value parameter to an EnabledBaseline resource.
- [EnabledBaselineParameterSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineParameterSummary.html): Summary of an applied parameter to an EnabledBaseline resource.
- [EnabledBaselineSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineSummary.html): Returns a summary of information about an EnabledBaseline object.
- [EnabledControlDetails](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlDetails.html): Information about the enabled control.
- [EnabledControlDriftTypes](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlDriftTypes.html): Defines the various categories of drift that can occur for an enabled control resource.
- [EnabledControlFilter](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlFilter.html): A structure that returns a set of control identifiers, the control status for each control in the set, and the drift status for each control in the set.
- [EnabledControlInheritanceDrift](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlInheritanceDrift.html): Represents drift information related to control inheritance between organizational units.
- [EnabledControlParameter](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlParameter.html): A key/value pair, where Key is of type String and Value is of type Document.
- [EnabledControlParameterSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlParameterSummary.html): Returns a summary of information about the parameters of an enabled control.
- [EnabledControlResourceDrift](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlResourceDrift.html): Represents drift information related to the underlying AWS resources managed by the control.
- [EnabledControlSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlSummary.html): Returns a summary of information about an enabled control.
- [EnablementStatusSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnablementStatusSummary.html): The deployment summary of an EnabledControl or EnabledBaseline resource.
- [LandingZoneDetail](https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneDetail.html): Information about the landing zone.
- [LandingZoneDriftStatusSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneDriftStatusSummary.html): The drift status summary of the landing zone.
- [LandingZoneOperationDetail](https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneOperationDetail.html): Information about a landing zone operation.
- [LandingZoneOperationFilter](https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneOperationFilter.html): A filter object that lets you call ListLandingZoneOperations with a specific filter.
- [LandingZoneOperationSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneOperationSummary.html): Returns a summary of information about a landing zone operation.
- [LandingZoneSummary](https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneSummary.html): Returns a summary of information about a landing zone.
- [Region](https://docs.aws.amazon.com/controltower/latest/APIReference/API_Region.html): An AWS Region in which AWS Control Tower expects to find the control deployed.
