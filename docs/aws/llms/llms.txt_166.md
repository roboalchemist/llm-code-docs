# Source: https://docs.aws.amazon.com/billingconductor/latest/APIReference/llms.txt

# AWS Billing Conductor API Reference

> AWS Billing Conductor is a fully managed service that you can use to customize a pro forma version of your billing data each month, to accurately show or chargeback your end customers. AWS Billing Conductor doesn't change the way you're billed by AWS each month by design. Instead, it provides you with a mechanism to configure, generate, and display rates to certain customers over a given billing period. You can also analyze the difference between the rates you apply to your accounting groupings relative to your actual rates from AWS. As a result of your Billing Conductor configuration, the payer account can also see the custom rate applied on the billing details page of the Billing console, or configure a cost and usage report per billing group.

- [Welcome](https://docs.aws.amazon.com/billingconductor/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/billingconductor/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/billingconductor/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_Operations.html)

- [AssociateAccounts](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociateAccounts.html): Connects an array of account IDs in a consolidated billing family to a predefined billing group.
- [AssociatePricingRules](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociatePricingRules.html): Connects an array of PricingRuleArns to a defined PricingPlan.
- [BatchAssociateResourcesToCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BatchAssociateResourcesToCustomLineItem.html): Associates a batch of resources to a percentage custom line item.
- [BatchDisassociateResourcesFromCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BatchDisassociateResourcesFromCustomLineItem.html): Disassociates a batch of resources from a percentage custom line item.
- [CreateBillingGroup](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreateBillingGroup.html): Creates a billing group that resembles a consolidated billing family that AWS charges, based off of the predefined pricing plan computation.
- [CreateCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreateCustomLineItem.html): Creates a custom line item that can be used to create a one-time fixed charge that can be applied to a single billing group for the current or previous billing period.
- [CreatePricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreatePricingPlan.html): Creates a pricing plan that is used for computing AWS charges for billing groups.
- [CreatePricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreatePricingRule.html): Creates a pricing rule can be associated to a pricing plan, or a set of pricing plans.
- [DeleteBillingGroup](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeleteBillingGroup.html): Deletes a billing group.
- [DeleteCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeleteCustomLineItem.html): Deletes the custom line item identified by the given ARN in the current, or previous billing period.
- [DeletePricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeletePricingPlan.html): Deletes a pricing plan.
- [DeletePricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeletePricingRule.html): Deletes the pricing rule that's identified by the input Amazon Resource Name (ARN).
- [DisassociateAccounts](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DisassociateAccounts.html): Removes the specified list of account IDs from the given billing group.
- [DisassociatePricingRules](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DisassociatePricingRules.html): Disassociates a list of pricing rules from a pricing plan.
- [GetBillingGroupCostReport](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_GetBillingGroupCostReport.html): Retrieves the margin summary report, which includes the AWS cost and charged amount (pro forma cost) by AWS service for a specific billing group.
- [ListAccountAssociations](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListAccountAssociations.html): This is a paginated call to list linked accounts that are linked to the payer account for the specified time period.
- [ListBillingGroupCostReports](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupCostReports.html): A paginated call to retrieve a summary report of actual AWS charges and the calculated AWS charges based on the associated pricing plan of a billing group.
- [ListBillingGroups](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroups.html): A paginated call to retrieve a list of billing groups for the given billing period.
- [ListCustomLineItems](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItems.html): A paginated call to get a list of all custom line items (FFLIs) for the given billing period.
- [ListCustomLineItemVersions](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemVersions.html): A paginated call to get a list of all custom line item versions.
- [ListPricingPlans](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingPlans.html): A paginated call to get pricing plans for the given billing period.
- [ListPricingPlansAssociatedWithPricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingPlansAssociatedWithPricingRule.html): A list of the pricing plans that are associated with a pricing rule.
- [ListPricingRules](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingRules.html): Describes a pricing rule that can be associated to a pricing plan, or set of pricing plans.
- [ListPricingRulesAssociatedToPricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingRulesAssociatedToPricingPlan.html): Lists the pricing rules that are associated with a pricing plan.
- [ListResourcesAssociatedToCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListResourcesAssociatedToCustomLineItem.html): List the resources that are associated to a custom line item.
- [ListTagsForResource](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListTagsForResource.html): A list the tags for a resource.
- [TagResource](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_TagResource.html): Associates the specified tags to a resource with the specified resourceArn.
- [UntagResource](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UntagResource.html): Deletes specified tags from a resource.
- [UpdateBillingGroup](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateBillingGroup.html): This updates an existing billing group.
- [UpdateCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateCustomLineItem.html): Update an existing custom line item in the current or previous billing period.
- [UpdatePricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdatePricingPlan.html): This updates an existing pricing plan.
- [UpdatePricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdatePricingRule.html): Updates an existing pricing rule.


## [Data Types](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_Types.html)

- [AccountAssociationsListElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AccountAssociationsListElement.html): A representation of a linked account.
- [AccountGrouping](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AccountGrouping.html): The set of accounts that will be under the billing group.
- [AssociateResourceError](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociateResourceError.html): A representation of a resource association error.
- [AssociateResourceResponseElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociateResourceResponseElement.html): A resource association result for a percentage custom line item.
- [Attribute](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_Attribute.html): The key-value pair that represents the attribute by which the BillingGroupCostReportResults are grouped.
- [BillingGroupCostReportElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingGroupCostReportElement.html): A summary report of actual AWS charges and calculated AWS charges, based on the associated pricing plan of a billing group.
- [BillingGroupCostReportResultElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingGroupCostReportResultElement.html): A paginated call to retrieve a list of summary reports of actual AWS charges and the calculated AWS charges, broken down by attributes.
- [BillingGroupListElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingGroupListElement.html): A representation of a billing group.
- [BillingPeriodRange](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingPeriodRange.html): A time range for which the margin summary is effective.
- [ComputationPreference](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ComputationPreference.html): The preferences and settings that will be used to compute the AWS charges for a billing group.
- [CreateFreeTierConfig](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreateFreeTierConfig.html): The possible AWS Free Tier configurations.
- [CreateTieringInput](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreateTieringInput.html): The set of tiering configurations for the pricing rule.
- [CustomLineItemBillingPeriodRange](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemBillingPeriodRange.html): The billing period range in which the custom line item request will be applied.
- [CustomLineItemChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemChargeDetails.html): The charge details of a custom line item.
- [CustomLineItemFlatChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemFlatChargeDetails.html): A representation of the charge details that are associated with a flat custom line item.
- [CustomLineItemListElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemListElement.html): A representation of a custom line item.
- [CustomLineItemPercentageChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemPercentageChargeDetails.html): A representation of the charge details that are associated with a percentage custom line item.
- [CustomLineItemVersionListElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemVersionListElement.html): A representation of a custom line item version.
- [DisassociateResourceResponseElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DisassociateResourceResponseElement.html): A resource disassociation result for a percentage custom line item.
- [FreeTierConfig](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_FreeTierConfig.html): The possible AWS Free Tier configurations.
- [LineItemFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_LineItemFilter.html): A representation of the line item filter for your custom line item.
- [ListAccountAssociationsFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListAccountAssociationsFilter.html): The filter on the account ID of the linked account, or any of the following:
- [ListBillingGroupAccountGrouping](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupAccountGrouping.html): Specifies if the billing group has the following features enabled.
- [ListBillingGroupCostReportsFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupCostReportsFilter.html): The filter used to retrieve specific BillingGroupCostReportElements.
- [ListBillingGroupsFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupsFilter.html): The filter that specifies the billing groups and pricing plans to retrieve billing group information.
- [ListCustomLineItemChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemChargeDetails.html): A representation of the charge details of a custom line item.
- [ListCustomLineItemFlatChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemFlatChargeDetails.html): A representation of the charge details that are associated with a flat custom line item.
- [ListCustomLineItemPercentageChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemPercentageChargeDetails.html): A representation of the charge details that are associated with a percentage custom line item.
- [ListCustomLineItemsFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemsFilter.html): A filter that specifies the custom line items and billing groups to retrieve FFLI information.
- [ListCustomLineItemVersionsBillingPeriodRangeFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemVersionsBillingPeriodRangeFilter.html): A billing period filter that specifies the custom line item versions to retrieve.
- [ListCustomLineItemVersionsFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemVersionsFilter.html): A filter that specifies the billing period range where the custom line item versions reside.
- [ListPricingPlansFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingPlansFilter.html): The filter that specifies the Amazon Resource Names (ARNs) of pricing plans, to retrieve pricing plan information.
- [ListPricingRulesFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingRulesFilter.html): The filter that specifies criteria that the pricing rules returned by the ListPricingRules API will adhere to.
- [ListResourcesAssociatedToCustomLineItemFilter](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListResourcesAssociatedToCustomLineItemFilter.html): A filter that specifies the type of resource associations that should be retrieved for a custom line item.
- [ListResourcesAssociatedToCustomLineItemResponseElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListResourcesAssociatedToCustomLineItemResponseElement.html): A representation of a resource association for a custom line item.
- [PresentationObject](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_PresentationObject.html): An object that defines how custom line item charges are presented in the bill, containing specifications for service presentation.
- [PricingPlanListElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_PricingPlanListElement.html): A representation of a pricing plan.
- [PricingRuleListElement](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_PricingRuleListElement.html): A representation of a pricing rule.
- [StringSearch](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_StringSearch.html): A structure that defines string search parameters.
- [Tiering](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_Tiering.html): The set of tiering configurations for the pricing rule.
- [UpdateBillingGroupAccountGrouping](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateBillingGroupAccountGrouping.html): Specifies if the billing group has the following features enabled.
- [UpdateCustomLineItemChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateCustomLineItemChargeDetails.html): A representation of the new charge details of a custom line item.
- [UpdateCustomLineItemFlatChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateCustomLineItemFlatChargeDetails.html): A representation of the new charge details that are associated with a flat custom line item.
- [UpdateCustomLineItemPercentageChargeDetails](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateCustomLineItemPercentageChargeDetails.html): A representation of the new charge details that are associated with a percentage custom line item.
- [UpdateFreeTierConfig](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateFreeTierConfig.html): The possible AWS Free Tier configurations.
- [UpdateTieringInput](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateTieringInput.html): The set of tiering configurations for the pricing rule.
- [ValidationExceptionField](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ValidationExceptionField.html): The field's information of a request that resulted in an exception.
