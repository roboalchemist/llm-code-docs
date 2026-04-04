# Source: https://docs.aws.amazon.com/servicecatalog/latest/dg/llms.txt

# AWS Service Catalog Developer Guide

- [What Is AWS Service Catalog?](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html)
- [API Overview](https://docs.aws.amazon.com/servicecatalog/latest/dg/service-catalog-api-overview.html)
- [Logging with CloudTrail](https://docs.aws.amazon.com/servicecatalog/latest/dg/logging-using-cloudtrail.html)

## [API Reference](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Operations.html)

The following actions are supported by Service Catalog:

### [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Operations_AWS_Service_Catalog.html)

The following actions are supported by Service Catalog:

- [AcceptPortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AcceptPortfolioShare.html): Accepts an offer to share the specified portfolio.
- [AssociateBudgetWithResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateBudgetWithResource.html): Associates the specified budget with the specified resource.
- [AssociatePrincipalWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociatePrincipalWithPortfolio.html): Associates the specified principal ARN with the specified portfolio.
- [AssociateProductWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateProductWithPortfolio.html): Associates the specified product with the specified portfolio.
- [AssociateServiceActionWithProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateServiceActionWithProvisioningArtifact.html): Associates a self-service action with a provisioning artifact.
- [AssociateTagOptionWithResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateTagOptionWithResource.html): Associate the specified TagOption with the specified portfolio or product.
- [BatchAssociateServiceActionWithProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_BatchAssociateServiceActionWithProvisioningArtifact.html): Associates multiple self-service actions with provisioning artifacts.
- [BatchDisassociateServiceActionFromProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_BatchDisassociateServiceActionFromProvisioningArtifact.html): Disassociates a batch of self-service actions from the specified provisioning artifact.
- [CopyProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CopyProduct.html): Copies the specified source product to the specified target product or a new product.
- [CreateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateConstraint.html): Creates a constraint.
- [CreatePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreatePortfolio.html): Creates a portfolio.
- [CreatePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreatePortfolioShare.html): Shares the specified portfolio with the specified account or organization node.
- [CreateProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateProduct.html): Creates a product.
- [CreateProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateProvisionedProductPlan.html): Creates a plan.
- [CreateProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateProvisioningArtifact.html): Creates a provisioning artifact (also known as a version) for the specified product.
- [CreateServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateServiceAction.html): Creates a self-service action.
- [CreateTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateTagOption.html): Creates a TagOption.
- [DeleteConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteConstraint.html): Deletes the specified constraint.
- [DeletePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeletePortfolio.html): Deletes the specified portfolio.
- [DeletePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeletePortfolioShare.html): Stops sharing the specified portfolio with the specified account or organization node.
- [DeleteProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteProduct.html): Deletes the specified product.
- [DeleteProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteProvisionedProductPlan.html): Deletes the specified plan.
- [DeleteProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteProvisioningArtifact.html): Deletes the specified provisioning artifact (also known as a version) for the specified product.
- [DeleteServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteServiceAction.html): Deletes a self-service action.
- [DeleteTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteTagOption.html): Deletes the specified TagOption.
- [DescribeConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeConstraint.html): Gets information about the specified constraint.
- [DescribeCopyProductStatus](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeCopyProductStatus.html): Gets the status of the specified copy product operation.
- [DescribePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribePortfolio.html): Gets information about the specified portfolio.
- [DescribePortfolioShares](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribePortfolioShares.html): Returns a summary of each of the portfolio shares that were created for the specified portfolio.
- [DescribePortfolioShareStatus](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribePortfolioShareStatus.html): Gets the status of the specified portfolio share operation.
- [DescribeProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProduct.html): Gets information about the specified product.
- [DescribeProductAsAdmin](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProductAsAdmin.html): Gets information about the specified product.
- [DescribeProductView](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProductView.html): Gets information about the specified product.
- [DescribeProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisionedProduct.html): Gets information about the specified provisioned product.
- [DescribeProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisionedProductPlan.html): Gets information about the resource changes for the specified plan.
- [DescribeProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisioningArtifact.html): Gets information about the specified provisioning artifact (also known as a version) for the specified product.
- [DescribeProvisioningParameters](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisioningParameters.html): Gets information about the configuration required to provision the specified product using the specified provisioning artifact.
- [DescribeRecord](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeRecord.html): Gets information about the specified request operation.
- [DescribeServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeServiceAction.html): Describes a self-service action.
- [DescribeServiceActionExecutionParameters](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeServiceActionExecutionParameters.html): Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.
- [DescribeTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeTagOption.html): Gets information about the specified TagOption.
- [DisableAWSOrganizationsAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisableAWSOrganizationsAccess.html): Disable portfolio sharing through the AWS Organizations service.
- [DisassociateBudgetFromResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateBudgetFromResource.html): Disassociates the specified budget from the specified resource.
- [DisassociatePrincipalFromPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociatePrincipalFromPortfolio.html): Disassociates a previously associated principal ARN from a specified portfolio.
- [DisassociateProductFromPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateProductFromPortfolio.html): Disassociates the specified product from the specified portfolio.
- [DisassociateServiceActionFromProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateServiceActionFromProvisioningArtifact.html): Disassociates the specified self-service action association from the specified provisioning artifact.
- [DisassociateTagOptionFromResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateTagOptionFromResource.html): Disassociates the specified TagOption from the specified resource.
- [EnableAWSOrganizationsAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_EnableAWSOrganizationsAccess.html): Enable portfolio sharing feature through AWS Organizations.
- [ExecuteProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ExecuteProvisionedProductPlan.html): Provisions or modifies a product based on the resource changes for the specified plan.
- [ExecuteProvisionedProductServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ExecuteProvisionedProductServiceAction.html): Executes a self-service action against a provisioned product.
- [GetAWSOrganizationsAccessStatus](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_GetAWSOrganizationsAccessStatus.html): Get the Access Status for AWS Organizations portfolio share feature.
- [GetProvisionedProductOutputs](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_GetProvisionedProductOutputs.html): This API takes either a ProvisonedProductId or a ProvisionedProductName, along with a list of one or more output keys, and responds with the key/value pairs of those outputs.
- [ImportAsProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ImportAsProvisionedProduct.html): Requests the import of a resource as an AWS Service Catalog provisioned product that is associated to an AWS Service Catalog product and provisioning artifact.
- [ListAcceptedPortfolioShares](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListAcceptedPortfolioShares.html): Lists all imported portfolios for which account-to-account shares were accepted by this account.
- [ListBudgetsForResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListBudgetsForResource.html): Lists all the budgets associated to the specified resource.
- [ListConstraintsForPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListConstraintsForPortfolio.html): Lists the constraints for the specified portfolio and product.
- [ListLaunchPaths](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html): Lists the paths to the specified product.
- [ListOrganizationPortfolioAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListOrganizationPortfolioAccess.html): Lists the organization nodes that have access to the specified portfolio.
- [ListPortfolioAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPortfolioAccess.html): Lists the account IDs that have access to the specified portfolio.
- [ListPortfolios](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPortfolios.html): Lists all portfolios in the catalog.
- [ListPortfoliosForProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPortfoliosForProduct.html): Lists all portfolios that the specified product is associated with.
- [ListPrincipalsForPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPrincipalsForPortfolio.html): Lists all PrincipalARNs and corresponding PrincipalTypes associated with the specified portfolio.
- [ListProvisionedProductPlans](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListProvisionedProductPlans.html): Lists the plans for the specified provisioned product or all plans to which the user has access.
- [ListProvisioningArtifacts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListProvisioningArtifacts.html): Lists all provisioning artifacts (also known as versions) for the specified product.
- [ListProvisioningArtifactsForServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListProvisioningArtifactsForServiceAction.html): Lists all provisioning artifacts (also known as versions) for the specified self-service action.
- [ListRecordHistory](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListRecordHistory.html): Lists the specified requests or all performed requests.
- [ListResourcesForTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListResourcesForTagOption.html): Lists the resources associated with the specified TagOption.
- [ListServiceActions](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListServiceActions.html): Lists all self-service actions.
- [ListServiceActionsForProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListServiceActionsForProvisioningArtifact.html): Returns a paginated list of self-service actions associated with the specified Product ID and Provisioning Artifact ID.
- [ListStackInstancesForProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListStackInstancesForProvisionedProduct.html): Returns summary information about stack instances that are associated with the specified CFN_STACKSET type provisioned product.
- [ListTagOptions](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListTagOptions.html): Lists the specified TagOptions or all TagOptions.
- [NotifyProvisionProductEngineWorkflowResult](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_NotifyProvisionProductEngineWorkflowResult.html): Notifies the result of the provisioning engine execution.
- [NotifyTerminateProvisionedProductEngineWorkflowResult](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_NotifyTerminateProvisionedProductEngineWorkflowResult.html): Notifies the result of the terminate engine execution.
- [NotifyUpdateProvisionedProductEngineWorkflowResult](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_NotifyUpdateProvisionedProductEngineWorkflowResult.html): Notifies the result of the update engine execution.
- [ProvisionProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisionProduct.html): Provisions the specified product.
- [RejectPortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_RejectPortfolioShare.html): Rejects an offer to share the specified portfolio.
- [ScanProvisionedProducts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ScanProvisionedProducts.html): Lists the provisioned products that are available (not terminated).
- [SearchProducts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SearchProducts.html): Gets information about the products to which the caller has access.
- [SearchProductsAsAdmin](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SearchProductsAsAdmin.html): Gets information about the products for the specified portfolio or all products.
- [SearchProvisionedProducts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SearchProvisionedProducts.html): Gets information about the provisioned products that meet the specified criteria.
- [TerminateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_TerminateProvisionedProduct.html): Terminates the specified provisioned product.
- [UpdateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateConstraint.html): Updates the specified constraint.
- [UpdatePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdatePortfolio.html): Updates the specified portfolio.
- [UpdatePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdatePortfolioShare.html): Updates the specified portfolio share.
- [UpdateProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProduct.html): Updates the specified product.
- [UpdateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisionedProduct.html): Requests updates to the configuration of the specified provisioned product.
- [UpdateProvisionedProductProperties](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisionedProductProperties.html): Requests updates to the properties of the specified provisioned product.
- [UpdateProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisioningArtifact.html): Updates the specified provisioning artifact (also known as a version) for the specified product.
- [UpdateServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateServiceAction.html): Updates a self-service action.
- [UpdateTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateTagOption.html): Updates the specified TagOption.

### [AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Operations_AWS_Service_Catalog_App_Registry.html)

The following actions are supported by AppRegistry:

- [AssociateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateAttributeGroup.html): Associates an attribute group with an application to augment the application's metadata with the group's attributes.
- [AssociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateResource.html): Associates a resource with an application.
- [CreateApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateApplication.html): Creates a new application that is the top-level node in a hierarchy of related cloud resource abstractions.
- [CreateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateAttributeGroup.html): Creates a new attribute group as a container for user-defined attributes.
- [DeleteApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DeleteApplication.html): Deletes an application that is specified either by its application ID, name, or ARN.
- [DeleteAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DeleteAttributeGroup.html): Deletes an attribute group, specified either by its attribute group ID, name, or ARN.
- [DisassociateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DisassociateAttributeGroup.html): Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application's metadata.
- [DisassociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DisassociateResource.html): Disassociates a resource from application.
- [GetApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetApplication.html): Retrieves metadata information about one of your applications.
- [GetAssociatedResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetAssociatedResource.html): Gets the resource associated with the application.
- [GetAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetAttributeGroup.html): Retrieves an attribute group by its ARN, ID, or name.
- [GetConfiguration](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetConfiguration.html): Retrieves a TagKey configuration from an account.
- [ListApplications](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListApplications.html): Retrieves a list of all of your applications.
- [ListAssociatedAttributeGroups](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAssociatedAttributeGroups.html): Lists all attribute groups that are associated with specified application.
- [ListAssociatedResources](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAssociatedResources.html): Lists all of the resources that are associated with the specified application.
- [ListAttributeGroups](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAttributeGroups.html): Lists all attribute groups which you have access to.
- [ListAttributeGroupsForApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAttributeGroupsForApplication.html): Lists the details of all attribute groups associated with a specific application.
- [ListTagsForResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListTagsForResource.html): Lists all of the tags on the resource.
- [PutConfiguration](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_PutConfiguration.html): Associates a TagKey configuration to an account.
- [SyncResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_SyncResource.html): Syncs the resource with current AppRegistry records.
- [TagResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_TagResource.html): Assigns one or more tags (key-value pairs) to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_UntagResource.html): Removes tags from a resource.
- [UpdateApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_UpdateApplication.html): Updates an existing application with new attributes.
- [UpdateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_UpdateAttributeGroup.html): Updates an existing attribute group with new details.

### [Data Types](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Types.html)

The following data types are supported by Service Catalog:

### [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Types_AWS_Service_Catalog.html)

The following data types are supported by Service Catalog:

- [AccessLevelFilter](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AccessLevelFilter.html): The access level to use to filter results.
- [BudgetDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_BudgetDetail.html): Information about a budget.
- [CloudWatchDashboard](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CloudWatchDashboard.html): Information about a CloudWatch dashboard.
- [CodeStarParameters](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CodeStarParameters.html): The subtype containing details about the Codestar connection Type.
- [ConstraintDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ConstraintDetail.html): Information about a constraint.
- [ConstraintSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ConstraintSummary.html): Summary information about a constraint.
- [EngineWorkflowResourceIdentifier](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_EngineWorkflowResourceIdentifier.html): The ID for the provisioned product resources that are part of a resource group.
- [ExecutionParameter](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ExecutionParameter.html): Details of an execution parameter value that is passed to a self-service action when executed on a provisioned product.
- [FailedServiceActionAssociation](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_FailedServiceActionAssociation.html): An object containing information about the error, along with identifying information about the self-service action and its associations.
- [LastSync](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_LastSync.html): Provides details about the product's connection sync and contains the following sub-fields.
- [LaunchPath](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_LaunchPath.html): A launch path object.
- [LaunchPathSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_LaunchPathSummary.html): Summary information about a product path for a user.
- [ListRecordHistorySearchFilter](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListRecordHistorySearchFilter.html): The search filter to use when listing history records.
- [ListTagOptionsFilters](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListTagOptionsFilters.html): Filters to use when listing TagOptions.
- [OrganizationNode](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_OrganizationNode.html): Information about the organization node.
- [ParameterConstraints](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ParameterConstraints.html): The constraints that the administrator has put on the parameter.
- [PortfolioDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_PortfolioDetail.html): Information about a portfolio.
- [PortfolioShareDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_PortfolioShareDetail.html): Information about the portfolio share.
- [Principal](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Principal.html): Information about a principal.
- [ProductViewAggregationValue](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProductViewAggregationValue.html): A single product view aggregation value/count pair, containing metadata about each product to which the calling user has access.
- [ProductViewDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProductViewDetail.html): Information about a product view.
- [ProductViewSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProductViewSummary.html): Summary information about a product view.
- [ProvisionedProductAttribute](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisionedProductAttribute.html): Information about a provisioned product.
- [ProvisionedProductDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisionedProductDetail.html): Information about a provisioned product.
- [ProvisionedProductPlanDetails](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisionedProductPlanDetails.html): Information about a plan.
- [ProvisionedProductPlanSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisionedProductPlanSummary.html): Summary information about a plan.
- [ProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifact.html): Information about a provisioning artifact.
- [ProvisioningArtifactDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactDetail.html): Information about a provisioning artifact (also known as a version) for a product.
- [ProvisioningArtifactOutput](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactOutput.html): Provisioning artifact output.
- [ProvisioningArtifactParameter](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactParameter.html): Information about a parameter used to provision a product.
- [ProvisioningArtifactPreferences](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactPreferences.html): The user-defined preferences that will be applied during product provisioning, unless overridden by ProvisioningPreferences or UpdateProvisioningPreferences.
- [ProvisioningArtifactProperties](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactProperties.html): Information about a provisioning artifact (also known as a version) for a product.
- [ProvisioningArtifactSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactSummary.html): Summary information about a provisioning artifact (also known as a version) for a product.
- [ProvisioningArtifactView](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactView.html): An object that contains summary information about a product view and a provisioning artifact.
- [ProvisioningParameter](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningParameter.html): Information about a parameter used to provision a product.
- [ProvisioningPreferences](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningPreferences.html): The user-defined preferences that will be applied when updating a provisioned product.
- [RecordDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_RecordDetail.html): Information about a request operation.
- [RecordError](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_RecordError.html): The error code and description resulting from an operation.
- [RecordOutput](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_RecordOutput.html): The output for the product created as the result of a request.
- [RecordTag](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_RecordTag.html): Information about a tag, which is a key-value pair.
- [ResourceChange](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ResourceChange.html): Information about a resource change that will occur when a plan is executed.
- [ResourceChangeDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ResourceChangeDetail.html): Information about a change to a resource attribute.
- [ResourceDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ResourceDetail.html): Information about a resource.
- [ResourceTargetDefinition](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ResourceTargetDefinition.html): Information about a change to a resource attribute.
- [ServiceActionAssociation](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ServiceActionAssociation.html): A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
- [ServiceActionDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ServiceActionDetail.html): An object containing detailed information about the self-service action.
- [ServiceActionSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ServiceActionSummary.html): Detailed information about the self-service action.
- [ShareDetails](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ShareDetails.html): Information about the portfolio share operation.
- [ShareError](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ShareError.html): Errors that occurred during the portfolio share operation.
- [SourceConnection](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SourceConnection.html): A top level ProductViewDetail response containing details about the productâs connection.
- [SourceConnectionDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SourceConnectionDetail.html): Provides details about the configured SourceConnection.
- [SourceConnectionParameters](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SourceConnectionParameters.html): Provides connection details.
- [StackInstance](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_StackInstance.html): An AWS CloudFormation stack, in a specific account and Region, that's part of a stack set operation.
- [Tag](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Tag.html): Information about a tag.
- [TagOptionDetail](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_TagOptionDetail.html): Information about a TagOption.
- [TagOptionSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_TagOptionSummary.html): Summary information about a TagOption.
- [UniqueTagResourceIdentifier](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UniqueTagResourceIdentifier.html): The unique key-value pair for a tag that identifies provisioned product resources.
- [UpdateProvisioningParameter](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisioningParameter.html): The parameter key-value pair used to update a provisioned product.
- [UpdateProvisioningPreferences](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisioningPreferences.html): The user-defined preferences that will be applied when updating a provisioned product.
- [UsageInstruction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UsageInstruction.html): Additional information provided by the administrator.

### [AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Types_AWS_Service_Catalog_App_Registry.html)

The following data types are supported by AppRegistry:

- [Application](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_Application.html): Represents a AWS Service Catalog AppRegistry application that is the top-level node in a hierarchy of related cloud resource abstractions.
- [ApplicationSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ApplicationSummary.html): Summary of a AWS Service Catalog AppRegistry application.
- [ApplicationTagResult](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ApplicationTagResult.html): The result of the application tag that's applied to a resource.
- [AppRegistryConfiguration](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AppRegistryConfiguration.html): Includes all of the AppRegistry settings.
- [AttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AttributeGroup.html): Represents a AWS Service Catalog AppRegistry attribute group that is rich metadata which describes an application and its components.
- [AttributeGroupDetails](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AttributeGroupDetails.html): The details related to a specific AttributeGroup.
- [AttributeGroupSummary](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AttributeGroupSummary.html): Summary of a AWS Service Catalog AppRegistry attribute group.
- [Integrations](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_Integrations.html): The information about the service integration.
- [Resource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_Resource.html): The information about the resource.
- [ResourceDetails](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ResourceDetails.html): The details related to the resource.
- [ResourceGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ResourceGroup.html): The information about the resource group integration.
- [ResourceInfo](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ResourceInfo.html): The information about the resource.
- [ResourceIntegrations](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ResourceIntegrations.html): The service integration information about the resource.
- [ResourcesListItem](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ResourcesListItem.html): The resource in a list of resources.
- [TagQueryConfiguration](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_TagQueryConfiguration.html): The definition of tagQuery.
