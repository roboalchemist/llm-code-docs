# Source: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/llms.txt

# AWS Control Catalog Welcome

> Welcome to the Control Catalog API reference. This guide is for developers who need detailed information about how to programmatically identify and filter the common controls and related metadata that are available to AWS customers. This API reference provides descriptions, syntax, and usage examples for each of the actions and data types that are supported by Control Catalog.

- [Welcome](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_Operations.html)

- [GetControl](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_GetControl.html): Returns details about a specific control, most notably a list of AWS Regions where this control is supported.
- [ListCommonControls](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html): Returns a paginated list of common controls from the AWS Control Catalog.
- [ListControlMappings](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControlMappings.html): Returns a paginated list of control mappings from the Control Catalog.
- [ListControls](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControls.html): Returns a paginated list of all available controls in the Control Catalog library.
- [ListDomains](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html): Returns a paginated list of domains from the Control Catalog.
- [ListObjectives](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListObjectives.html): Returns a paginated list of objectives from the Control Catalog.


## [Data Types](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_Types.html)

- [AssociatedDomainSummary](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_AssociatedDomainSummary.html): A summary of the domain that a common control or an objective belongs to.
- [AssociatedObjectiveSummary](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_AssociatedObjectiveSummary.html): A summary of the objective that a common control supports.
- [CommonControlFilter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_CommonControlFilter.html): An optional filter that narrows the results to a specific objective.
- [CommonControlMappingDetails](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_CommonControlMappingDetails.html): A structure that contains details about a common control mapping.
- [CommonControlSummary](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_CommonControlSummary.html): A summary of metadata for a common control.
- [ControlFilter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlFilter.html): A structure that defines filtering criteria for the ListControls operation.
- [ControlMapping](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlMapping.html): A structure that contains information about a control mapping, including the control ARN, mapping type, and mapping details.
- [ControlMappingFilter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlMappingFilter.html): A structure that defines filtering criteria for the ListControlMappings operation.
- [ControlParameter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlParameter.html): Five types of control parameters are supported.
- [ControlSummary](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlSummary.html): Overview of information about a control.
- [DomainResourceFilter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_DomainResourceFilter.html): The domain resource that's being used as a filter.
- [DomainSummary](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_DomainSummary.html): A summary of metadata for a domain.
- [FrameworkMappingDetails](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_FrameworkMappingDetails.html): A structure that contains details about a framework mapping, including the framework name and specific item within the framework that the control maps to.
- [ImplementationDetails](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ImplementationDetails.html): An object that describes the implementation type for a control.
- [ImplementationFilter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ImplementationFilter.html): A structure that defines filtering criteria for control implementations.
- [ImplementationSummary](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ImplementationSummary.html): A summary of how the control is implemented, including the AWS service that enforces the control and its service-specific identifier.
- [Mapping](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_Mapping.html): A structure that contains the details of a mapping relationship, which can be either to a framework or to a common control.
- [ObjectiveFilter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveFilter.html): An optional filter that narrows the list of objectives to a specific domain.
- [ObjectiveResourceFilter](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveResourceFilter.html): The objective resource that's being used as a filter.
- [ObjectiveSummary](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveSummary.html): A summary of metadata for an objective.
- [RegionConfiguration](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_RegionConfiguration.html): Returns information about the control, including the scope of the control, if enabled, and the Regions in which the control is available for deployment.
- [RelatedControlMappingDetails](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_RelatedControlMappingDetails.html): A structure that describes a control's relationship status with other controls.
