# Source: https://docs.aws.amazon.com/recovery-readiness/latest/api/llms.txt

# Amazon Route 53 Application Recovery Controller Recovery Readiness API Reference Guide

> Amazon Route 53 Application Recovery Controller is a service that improves application availability by centrally coordinating failovers within an AWS Region or across multiple Regions. Recovery readiness in Application Recovery Controller provides continuous readiness checks to ensure that your applications are properly scaled to handle failover traffic and configured to route around failures.

- [What is recovery readiness in Amazon Application Recovery Controller (ARC)?](https://docs.aws.amazon.com/recovery-readiness/latest/api/what-is-recovery-readiness.html)
- [Document history](https://docs.aws.amazon.com/recovery-readiness/latest/api/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/recovery-readiness/latest/api/glossary.html)

## [Resources](https://docs.aws.amazon.com/recovery-readiness/latest/api/resources.html)

- [DeleteCrossAccountAuthorization](https://docs.aws.amazon.com/recovery-readiness/latest/api/crossaccountauthorizations-crossaccountauthorization.html)
- [GetArchitectureRecommendations](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname-architecturerecommendations.html)
- [GetCell, UpdateCell, DeleteCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html)
- [GetCellReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/cellreadiness-cellname.html)
- [GetReadinessCheck, UpdateReadinessCheck, DeleteReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html)
- [GetReadinessCheckResourceStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-resource-resourceidentifier-status.html)
- [GetReadinessCheckStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-status.html)
- [GetRecoveryGroup, UpdateRecoveryGroup, DeleteRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html)
- [GetRecoveryGroupReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroupreadiness-recoverygroupname.html)
- [GetResourceSet, UpdateResourceSet, DeleteResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html)
- [ListCells, CreateCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html)
- [ListCrossAccountAuthorizations, CreateCrossAccountAuthorization](https://docs.aws.amazon.com/recovery-readiness/latest/api/crossaccountauthorizations.html)
- [ListReadinessChecks, CreateReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html)
- [ListRecoveryGroups, CreateRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html)
- [ListResourceSets, CreateResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html)
- [ListRules](https://docs.aws.amazon.com/recovery-readiness/latest/api/rules.html)
- [ListTagsForResources, TagResource, UntagResource](https://docs.aws.amazon.com/recovery-readiness/latest/api/tags-resource-arn.html)


## [CLI examples](https://docs.aws.amazon.com/recovery-readiness/latest/api/examples-cli-readiness.html)

- [Create a cell](https://docs.aws.amazon.com/recovery-readiness/latest/api/create-cell.html): The following is an example of a request to create a cell, and the response.
- [Get a cell](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-cell.html): The following is an example of a request to get a cell, and the response.
- [Update a cell](https://docs.aws.amazon.com/recovery-readiness/latest/api/update-cell.html): The following is an example of a request to update a cell, and the response.
- [Delete a cell](https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-cell.html): The following is an example of a request to delete a cell.
- [List cells for an account](https://docs.aws.amazon.com/recovery-readiness/latest/api/list-cells.html): The following is an example of a request to list the cells in an account, and the response.
- [Create a recovery group](https://docs.aws.amazon.com/recovery-readiness/latest/api/create-recovery-group.html): The following is an example of a request to list the cells in an account, and the response.
- [Get a recovery group](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-recovery-group.html): The following is an example of a request to get a recovery group, and the response.
- [Update a recovery group](https://docs.aws.amazon.com/recovery-readiness/latest/api/update-recovery-group.html): The following is an example of a request to update a recovery group to add two cells, and the response.
- [Delete a recovery group](https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-recovery-group.html): The following is an example of a request to delete a recovery group.
- [List recovery groups](https://docs.aws.amazon.com/recovery-readiness/latest/api/list-recovery-groups.html): The following is an example of a request to list the recovery groups in an account, and the response.
- [Create a resource set](https://docs.aws.amazon.com/recovery-readiness/latest/api/create-resource-set.html): The following is an example of a request to create a resource set with two Amazon EBS volumes, and the response.
- [Get a resource set](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-resource-set.html): The following is an example of a request to get a resource set, and the response.
- [Update a resource set](https://docs.aws.amazon.com/recovery-readiness/latest/api/update-resource-set.html): The following is an example of a request to update a resource set, and the response.
- [Delete a resource set](https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-resource-set.html): The following is an example of a request to delete a resource set.
- [List resource sets](https://docs.aws.amazon.com/recovery-readiness/latest/api/list-resource-sets.html): The following is an example of a request to list the resource sets in an account, and the response.
- [Create a readiness check](https://docs.aws.amazon.com/recovery-readiness/latest/api/create-readiness-check.html): The following is an example of a request to create a readiness check for an Amazon EBS volume, and the response.
- [Get a readiness check](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-readiness-check.html): The following is an example of a request to get a readiness check, and the response.
- [Update a readiness check](https://docs.aws.amazon.com/recovery-readiness/latest/api/update-readiness-check.html): The following is an example of a request to update a readiness check, and the response.
- [Delete a readiness check](https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-readiness-check.html): The following is an example of a request to delete a readiness check.
- [List readiness checks](https://docs.aws.amazon.com/recovery-readiness/latest/api/list-readiness-checks.html): The following is an example of a request to list the readiness checks in an account, and the response.
- [Check the status of an entire readiness check](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-readiness-check-status.html): The following is an example of a request to list the roll-up status for an entire readiness check, and the response.
- [Check the readiness of a resource in a readiness check](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-readiness-check-resource-status.html): The following is an example of a request to check the readiness of an individual resource in a readiness check, and the response.
- [Check the readiness of a cell](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-cell-readiness-summary.html): The following is an example of a request to check cell readiness, and the response.
- [Check the readiness of a recovery group](https://docs.aws.amazon.com/recovery-readiness/latest/api/get-recovery-group-readiness-summary.html): The following is an example of a request to check a recovery group readiness, and the response.
