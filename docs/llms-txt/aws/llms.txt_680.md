# Source: https://docs.aws.amazon.com/quick-setup/latest/APIReference/llms.txt

# Quick Setup API Reference

> Quick Setup helps you quickly configure frequently used services and features with recommended best practices. Quick Setup simplifies setting up services, including Systems Manager, by automating common or recommended tasks.

- [Welcome](https://docs.aws.amazon.com/quick-setup/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/quick-setup/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/quick-setup/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_Operations.html)

- [CreateConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_CreateConfigurationManager.html): Creates a Quick Setup configuration manager resource.
- [DeleteConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_DeleteConfigurationManager.html): Deletes a configuration manager.
- [GetConfiguration](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetConfiguration.html): Returns details about the specified configuration.
- [GetConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetConfigurationManager.html): Returns a configuration manager.
- [GetServiceSettings](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetServiceSettings.html): Returns settings configured for Quick Setup in the requesting AWS account and AWS Region.
- [ListConfigurationManagers](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListConfigurationManagers.html): Returns Quick Setup configuration managers that were created using the CreateConfigurationManager API action.
- [ListConfigurations](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListConfigurations.html): Returns configurations deployed by Quick Setup in the requesting AWS account and AWS Region.
- [ListQuickSetupTypes](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListQuickSetupTypes.html): Returns the available Quick Setup types.
- [ListTagsForResource](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListTagsForResource.html): Returns tags assigned to the resource.
- [TagResource](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_TagResource.html): Assigns key-value pairs of metadata to AWS resources.
- [UntagResource](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UntagResource.html): Removes tags from the specified resource.
- [UpdateConfigurationDefinition](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateConfigurationDefinition.html): Updates a Quick Setup configuration definition.
- [UpdateConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateConfigurationManager.html): Updates a Quick Setup configuration manager.
- [UpdateServiceSettings](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateServiceSettings.html): Updates settings configured for Quick Setup.


## [Data Types](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_Types.html)

- [ConfigurationDefinition](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationDefinition.html): The definition of a Quick Setup configuration.
- [ConfigurationDefinitionInput](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationDefinitionInput.html): Defines the preferences and options for a configuration definition.
- [ConfigurationDefinitionSummary](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationDefinitionSummary.html): A summarized definition of a Quick Setup configuration definition.
- [ConfigurationManagerSummary](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationManagerSummary.html): A summary of a Quick Setup configuration manager.
- [ConfigurationSummary](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationSummary.html): Details for a Quick Setup configuration.
- [Filter](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_Filter.html): A key-value pair to filter results.
- [QuickSetupTypeOutput](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_QuickSetupTypeOutput.html): Information about the Quick Setup type.
- [ServiceSettings](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ServiceSettings.html): Settings configured for Quick Setup.
- [StatusSummary](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_StatusSummary.html): A summarized description of the status.
- [TagEntry](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_TagEntry.html): Key-value pairs of metadata.
