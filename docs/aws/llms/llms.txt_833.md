# Source: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/llms.txt

# AWS Trusted Advisor API Reference

> TrustedAdvisor Public API

- [Welcome](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_Operations.html)

- [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html): Update one or more exclusion statuses for a list of recommendation resources.
- [GetOrganizationRecommendation](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_GetOrganizationRecommendation.html): Get a specific recommendation within an AWS Organizations organization.
- [GetRecommendation](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_GetRecommendation.html): Get a specific Recommendation.
- [ListChecks](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListChecks.html): List a filterable set of Checks.
- [ListOrganizationRecommendationAccounts](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationAccounts.html): Lists the accounts that own the resources for an organization aggregate recommendation.
- [ListOrganizationRecommendationResources](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationResources.html): List Resources of a Recommendation within an Organization.
- [ListOrganizationRecommendations](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListOrganizationRecommendations.html): List a filterable set of Recommendations within an Organization.
- [ListRecommendationResources](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListRecommendationResources.html): List Resources of a Recommendation.
- [ListRecommendations](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListRecommendations.html): List a filterable set of Recommendations.
- [UpdateOrganizationRecommendationLifecycle](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_UpdateOrganizationRecommendationLifecycle.html): Update the lifecycle of a Recommendation within an Organization.
- [UpdateRecommendationLifecycle](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_UpdateRecommendationLifecycle.html): Update the lifecyle of a Recommendation.


## [Data Types](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_Types.html)

- [AccountRecommendationLifecycleSummary](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_AccountRecommendationLifecycleSummary.html): Summary of an AccountRecommendationLifecycle for an Organization Recommendation
- [CheckSummary](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_CheckSummary.html): A summary of an AWS Trusted Advisor Check
- [OrganizationRecommendation](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_OrganizationRecommendation.html): A Recommendation for accounts within an Organization
- [OrganizationRecommendationResourceSummary](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_OrganizationRecommendationResourceSummary.html): Organization Recommendation Resource Summary
- [OrganizationRecommendationSummary](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_OrganizationRecommendationSummary.html): Summary of recommendation for accounts within an Organization
- [Recommendation](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_Recommendation.html): A Recommendation for an Account
- [RecommendationCostOptimizingAggregates](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationCostOptimizingAggregates.html): Cost optimizing aggregates for a Recommendation
- [RecommendationPillarSpecificAggregates](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationPillarSpecificAggregates.html): Recommendation pillar aggregates
- [RecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationResourceExclusion.html): The request entry for Recommendation Resource exclusion.
- [RecommendationResourcesAggregates](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationResourcesAggregates.html): Aggregation of Recommendation Resources
- [RecommendationResourceSummary](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationResourceSummary.html): Summary of a Recommendation Resource
- [RecommendationSummary](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationSummary.html): Summary of Recommendation for an Account
- [UpdateRecommendationResourceExclusionError](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_UpdateRecommendationResourceExclusionError.html): The error entry for Recommendation Resource exclusion.
