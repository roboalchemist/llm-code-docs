# Source: https://docs.aws.amazon.com/ssmsap/latest/APIReference/llms.txt

# AWS Systems Manager for SAP API Reference Guide

> This API reference provides descriptions, syntax, and other details about each of the actions and data types for AWS Systems Manager for SAP. The topic for each action shows the API request parameters and responses.

- [Welcome](https://docs.aws.amazon.com/ssmsap/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ssmsap/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ssmsap/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Operations.html)

- [DeleteResourcePermission](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_DeleteResourcePermission.html): Removes permissions associated with the target database.
- [DeregisterApplication](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_DeregisterApplication.html): Deregister an SAP application with AWS Systems Manager for SAP.
- [GetApplication](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetApplication.html): Gets an application registered with AWS Systems Manager for SAP.
- [GetComponent](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetComponent.html): Gets the component of an application registered with AWS Systems Manager for SAP.
- [GetConfigurationCheckOperation](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetConfigurationCheckOperation.html): Gets the details of a configuration check operation by specifying the operation ID.
- [GetDatabase](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetDatabase.html): Gets the SAP HANA database of an application registered with AWS Systems Manager for SAP.
- [GetOperation](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetOperation.html): Gets the details of an operation by specifying the operation ID.
- [GetResourcePermission](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetResourcePermission.html): Gets permissions associated with the target database.
- [ListApplications](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListApplications.html): Lists all the applications registered with AWS Systems Manager for SAP.
- [ListComponents](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListComponents.html): Lists all the components registered with AWS Systems Manager for SAP.
- [ListConfigurationCheckDefinitions](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListConfigurationCheckDefinitions.html): Lists all configuration check types supported by AWS Systems Manager for SAP.
- [ListConfigurationCheckOperations](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListConfigurationCheckOperations.html): Lists the configuration check operations performed by AWS Systems Manager for SAP.
- [ListDatabases](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListDatabases.html): Lists the SAP HANA databases of an application registered with AWS Systems Manager for SAP.
- [ListOperationEvents](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListOperationEvents.html): Returns a list of operations events.
- [ListOperations](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListOperations.html): Lists the operations performed by AWS Systems Manager for SAP.
- [ListSubCheckResults](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListSubCheckResults.html): Lists the sub-check results of a specified configuration check operation.
- [ListSubCheckRuleResults](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListSubCheckRuleResults.html): Lists the rules of a specified sub-check belonging to a configuration check operation.
- [ListTagsForResource](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListTagsForResource.html): Lists all tags on an SAP HANA application and/or database registered with AWS Systems Manager for SAP.
- [PutResourcePermission](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_PutResourcePermission.html): Adds permissions to the target database.
- [RegisterApplication](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_RegisterApplication.html): Register an SAP application with AWS Systems Manager for SAP.
- [StartApplication](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_StartApplication.html): Request is an operation which starts an application.
- [StartApplicationRefresh](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_StartApplicationRefresh.html): Refreshes a registered application.
- [StartConfigurationChecks](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_StartConfigurationChecks.html): Initiates configuration check operations against a specified application.
- [StopApplication](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_StopApplication.html): Request is an operation to stop an application.
- [TagResource](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_TagResource.html): Creates tag for a resource by specifying the ARN.
- [UntagResource](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_UntagResource.html): Delete the tags for a resource.
- [UpdateApplicationSettings](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_UpdateApplicationSettings.html): Updates the settings of an application registered with AWS Systems Manager for SAP.


## [Data Types](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Types.html)

- [Application](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Application.html): An SAP application registered with AWS Systems Manager for SAP.
- [ApplicationCredential](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ApplicationCredential.html): The credentials of your SAP application.
- [ApplicationSummary](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ApplicationSummary.html): The summary of the SAP application registered with AWS Systems Manager for SAP.
- [AssociatedHost](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_AssociatedHost.html): Describes the properties of the associated host.
- [BackintConfig](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_BackintConfig.html): Configuration parameters for AWS Backint Agent for SAP HANA.
- [Component](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Component.html): The SAP component of your application.
- [ComponentInfo](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ComponentInfo.html): This is information about the component of your SAP application, such as Web Dispatcher.
- [ComponentSummary](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ComponentSummary.html): The summary of the component.
- [ConfigurationCheckDefinition](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ConfigurationCheckDefinition.html): Represents a configuration check definition supported by AWS Systems Manager for SAP.
- [ConfigurationCheckOperation](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ConfigurationCheckOperation.html): Represents a configuration check operation that has been executed against an application.
- [Database](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Database.html): The SAP HANA database of the application registered with AWS Systems Manager for SAP.
- [DatabaseConnection](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_DatabaseConnection.html): The connection specifications for the database.
- [DatabaseSummary](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_DatabaseSummary.html): The summary of the database.
- [Filter](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Filter.html): A specific result obtained by specifying the name, value, and operator.
- [Host](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Host.html): Describes the properties of the Dedicated Host.
- [IpAddressMember](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_IpAddressMember.html): Provides information of the IP address.
- [Operation](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Operation.html): The operations performed by AWS Systems Manager for SAP.
- [OperationEvent](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_OperationEvent.html): An operation event returns details for an operation, including key milestones which can be used to monitor and track operations in progress.
- [Resilience](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Resilience.html): Details of the SAP HANA system replication for the instance.
- [Resource](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Resource.html): The resource contains a ResourceArn and the ResourceType.
- [RuleResult](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_RuleResult.html): Represents the result of a single rule within a configuration check.
- [RuleStatusCounts](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_RuleStatusCounts.html): A summary of rule results, providing counts for each status type.
- [SubCheckResult](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_SubCheckResult.html): Represents the result of a sub-check within a configuration check operation.
