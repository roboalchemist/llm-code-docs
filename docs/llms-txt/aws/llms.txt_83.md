# Source: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/llms.txt

# AmplifyUIBuilder Welcome

> Welcome to the AWS Amplify UI Builder API documentation. This reference provides descriptions of the actions and data types for the Amplify UI Builder API.

- [Welcome](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Operations.html)

- [CreateComponent](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateComponent.html): Creates a new component for an Amplify app.
- [CreateForm](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateForm.html): Creates a new form for an Amplify app.
- [CreateTheme](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateTheme.html): Creates a theme to apply to the components in an Amplify app.
- [DeleteComponent](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_DeleteComponent.html): Deletes a component from an Amplify app.
- [DeleteForm](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_DeleteForm.html): Deletes a form from an Amplify app.
- [DeleteTheme](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_DeleteTheme.html): Deletes a theme from an Amplify app.
- [ExchangeCodeForToken](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ExchangeCodeForToken.html)
- [ExportComponents](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ExportComponents.html): Exports component configurations to code that is ready to integrate into an Amplify app.
- [ExportForms](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ExportForms.html): Exports form configurations to code that is ready to integrate into an Amplify app.
- [ExportThemes](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ExportThemes.html): Exports theme configurations to code that is ready to integrate into an Amplify app.
- [GetCodegenJob](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetCodegenJob.html): Returns an existing code generation job.
- [GetComponent](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetComponent.html): Returns an existing component for an Amplify app.
- [GetForm](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetForm.html): Returns an existing form for an Amplify app.
- [GetMetadata](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetMetadata.html): Returns existing metadata for an Amplify app.
- [GetTheme](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetTheme.html): Returns an existing theme for an Amplify app.
- [ListCodegenJobs](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ListCodegenJobs.html): Retrieves a list of code generation jobs for a specified Amplify app and backend environment.
- [ListComponents](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ListComponents.html): Retrieves a list of components for a specified Amplify app and backend environment.
- [ListForms](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ListForms.html): Retrieves a list of forms for a specified Amplify app and backend environment.
- [ListTagsForResource](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ListTagsForResource.html): Returns a list of tags for a specified Amazon Resource Name (ARN).
- [ListThemes](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ListThemes.html): Retrieves a list of themes for a specified Amplify app and backend environment.
- [PutMetadataFlag](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_PutMetadataFlag.html): Stores the metadata information about a feature on a form.
- [RefreshToken](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_RefreshToken.html)
- [StartCodegenJob](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_StartCodegenJob.html): Starts a code generation job for a specified Amplify app and backend environment.
- [TagResource](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_TagResource.html): Tags the resource with a tag key and value.
- [UntagResource](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UntagResource.html): Untags a resource with a specified Amazon Resource Name (ARN).
- [UpdateComponent](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateComponent.html): Updates an existing component.
- [UpdateForm](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateForm.html): Updates an existing form.
- [UpdateTheme](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateTheme.html): Updates an existing theme.


## [Data Types](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Types.html)

- [ActionParameters](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ActionParameters.html): Represents the event action configuration for an element of a Component or ComponentChild.
- [ApiConfiguration](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ApiConfiguration.html): Describes the API configuration for a code generation job.
- [CodegenDependency](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenDependency.html): Dependency package that may be required for the project code to run.
- [CodegenFeatureFlags](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenFeatureFlags.html): Describes the feature flags that you can specify for a code generation job.
- [CodegenGenericDataEnum](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenGenericDataEnum.html): Describes the enums in a generic data schema.
- [CodegenGenericDataField](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenGenericDataField.html): Describes a field in a generic data schema.
- [CodegenGenericDataModel](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenGenericDataModel.html): Describes a model in a generic data schema.
- [CodegenGenericDataNonModel](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenGenericDataNonModel.html): Describes a non-model in a generic data schema.
- [CodegenGenericDataRelationshipType](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenGenericDataRelationshipType.html): Describes the relationship between generic data models.
- [CodegenJob](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJob.html): Describes the configuration for a code generation job that is associated with an Amplify app.
- [CodegenJobAsset](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJobAsset.html): Describes an asset for a code generation job.
- [CodegenJobGenericDataSchema](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJobGenericDataSchema.html): Describes the data schema for a code generation job.
- [CodegenJobRenderConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJobRenderConfig.html): Describes the configuration information for rendering the UI component associated with the code generation job.
- [CodegenJobSummary](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJobSummary.html): A summary of the basic information about the code generation job.
- [Component](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Component.html): Contains the configuration settings for a user interface (UI) element for an Amplify app.
- [ComponentBindingPropertiesValue](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentBindingPropertiesValue.html): Represents the data binding configuration for a component at runtime.
- [ComponentBindingPropertiesValueProperties](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentBindingPropertiesValueProperties.html): Represents the data binding configuration for a specific property using data stored in AWS.
- [ComponentChild](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentChild.html): A nested UI configuration within a parent Component.
- [ComponentConditionProperty](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentConditionProperty.html): Represents a conditional expression to set a component property.
- [ComponentDataConfiguration](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentDataConfiguration.html): Describes the configuration for binding a component's properties to data.
- [ComponentEvent](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentEvent.html): Describes the configuration of an event.
- [ComponentProperty](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentProperty.html): Describes the configuration for all of a component's properties.
- [ComponentPropertyBindingProperties](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentPropertyBindingProperties.html): Associates a component property to a binding property.
- [ComponentSummary](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentSummary.html): Contains a summary of a component.
- [ComponentVariant](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentVariant.html): Describes the style configuration of a unique variation of a main component.
- [CreateComponentData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateComponentData.html): Represents all of the information that is required to create a component.
- [CreateFormData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateFormData.html): Represents all of the information that is required to create a form.
- [CreateThemeData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateThemeData.html): Represents all of the information that is required to create a theme.
- [DataStoreRenderConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_DataStoreRenderConfig.html): Describes the DataStore configuration for an API for a code generation job.
- [ExchangeCodeForTokenRequestBody](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ExchangeCodeForTokenRequestBody.html): Describes the configuration of a request to exchange an access code for a token.
- [FieldConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FieldConfig.html): Describes the configuration information for a field in a table.
- [FieldInputConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FieldInputConfig.html): Describes the configuration for the default input values to display for a field.
- [FieldPosition](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FieldPosition.html): Describes the field position.
- [FieldValidationConfiguration](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FieldValidationConfiguration.html): Describes the validation configuration for a field.
- [FileUploaderFieldConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FileUploaderFieldConfig.html): Describes the configuration for the file uploader field.
- [Form](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Form.html): Contains the configuration settings for a Form user interface (UI) element for an Amplify app.
- [FormBindingElement](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormBindingElement.html): Describes how to bind a component property to form data.
- [FormButton](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormButton.html): Describes the configuration for a button UI element that is a part of a form.
- [FormCTA](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormCTA.html): Describes the call to action button configuration for the form.
- [FormDataTypeConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormDataTypeConfig.html): Describes the data type configuration for the data source associated with a form.
- [FormInputBindingPropertiesValue](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormInputBindingPropertiesValue.html): Represents the data binding configuration for a form's input fields at runtime.You can use FormInputBindingPropertiesValue to add exposed properties to a form to allow different values to be entered when a form is reused in different places in an app.
- [FormInputBindingPropertiesValueProperties](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormInputBindingPropertiesValueProperties.html): Represents the data binding configuration for a specific property using data stored in AWS.
- [FormInputValueProperty](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormInputValueProperty.html): Describes the configuration for an input field on a form.
- [FormInputValuePropertyBindingProperties](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormInputValuePropertyBindingProperties.html): Associates a form property to a binding property.
- [FormStyle](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormStyle.html): Describes the configuration for the form's style.
- [FormStyleConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormStyleConfig.html): Describes the configuration settings for the form's style properties.
- [FormSummary](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormSummary.html): Describes the basic information about a form.
- [GraphQLRenderConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GraphQLRenderConfig.html): Describes the GraphQL configuration for an API for a code generation job.
- [MutationActionSetStateParameter](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_MutationActionSetStateParameter.html): Represents the state configuration when an action modifies a property of another element within the same component.
- [NoApiRenderConfig](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_NoApiRenderConfig.html): Describes the configuration for an application with no API being used.
- [Predicate](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Predicate.html): Stores information for generating Amplify DataStore queries.
- [PutMetadataFlagBody](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_PutMetadataFlagBody.html): Stores the metadata information about a feature on a form.
- [ReactStartCodegenJobData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ReactStartCodegenJobData.html): Describes the code generation job configuration for a React project.
- [RefreshTokenRequestBody](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_RefreshTokenRequestBody.html): Describes a refresh token.
- [SectionalElement](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_SectionalElement.html): Stores the configuration information for a visual helper element for a form.
- [SortProperty](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_SortProperty.html): Describes how to sort the data that you bind to a component.
- [StartCodegenJobData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_StartCodegenJobData.html): The code generation job resource configuration.
- [Theme](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Theme.html): A theme is a collection of style settings that apply globally to the components associated with an Amplify application.
- [ThemeSummary](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ThemeSummary.html): Describes the basic information about a theme.
- [ThemeValue](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ThemeValue.html): Describes the configuration of a theme's properties.
- [ThemeValues](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ThemeValues.html): A key-value pair that defines a property of a theme.
- [UpdateComponentData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateComponentData.html): Updates and saves all of the information about a component, based on component ID.
- [UpdateFormData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateFormData.html): Updates and saves all of the information about a form, based on form ID.
- [UpdateThemeData](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateThemeData.html): Saves the data binding information for a theme.
- [ValueMapping](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ValueMapping.html): Associates a complex object with a display value.
- [ValueMappings](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ValueMappings.html): Represents the data binding configuration for a value map.
