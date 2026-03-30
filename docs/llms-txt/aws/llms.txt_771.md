# Source: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/llms.txt

# Service Quotas API Reference

> With Service Quotas, you can view and manage your quotas easily as your AWS workloads grow. Quotas, also referred to as limits, are the maximum number of resources that you can create in your AWS account. For more information, see the Service Quotas User Guide.

- [Welcome](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_Operations.html)

- [AssociateServiceQuotaTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_AssociateServiceQuotaTemplate.html): Associates your quota request template with your organization.
- [CreateSupportCase](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_CreateSupportCase.html): Creates a Support case for an existing quota increase request.
- [DeleteServiceQuotaIncreaseRequestFromTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_DeleteServiceQuotaIncreaseRequestFromTemplate.html): Deletes the quota increase request for the specified quota from your quota request template.
- [DisassociateServiceQuotaTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_DisassociateServiceQuotaTemplate.html): Disables your quota request template.
- [GetAssociationForServiceQuotaTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetAssociationForServiceQuotaTemplate.html): Retrieves the status of the association for the quota request template.
- [GetAutoManagementConfiguration](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetAutoManagementConfiguration.html): Retrieves information about your Service Quotas Automatic Management configuration.
- [GetAWSDefaultServiceQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetAWSDefaultServiceQuota.html): Retrieves the default value for the specified quota.
- [GetQuotaUtilizationReport](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetQuotaUtilizationReport.html): Retrieves the quota utilization report for your AWS account.
- [GetRequestedServiceQuotaChange](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetRequestedServiceQuotaChange.html): Retrieves information about the specified quota increase request.
- [GetServiceQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetServiceQuota.html): Retrieves the applied quota value for the specified account-level or resource-level quota.
- [GetServiceQuotaIncreaseRequestFromTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetServiceQuotaIncreaseRequestFromTemplate.html): Retrieves information about the specified quota increase request in your quota request template.
- [ListAWSDefaultServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListAWSDefaultServiceQuotas.html): Lists the default values for the quotas for the specified AWS service.
- [ListRequestedServiceQuotaChangeHistory](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.html): Retrieves the quota increase requests for the specified AWS service.
- [ListRequestedServiceQuotaChangeHistoryByQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.html): Retrieves the quota increase requests for the specified quota.
- [ListServiceQuotaIncreaseRequestsInTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotaIncreaseRequestsInTemplate.html): Lists the quota increase requests in the specified quota request template.
- [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html): Lists the applied quota values for the specified AWS service.
- [ListServices](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServices.html): Lists the names and codes for the AWS services integrated with Service Quotas.
- [ListTagsForResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListTagsForResource.html): Returns a list of the tags assigned to the specified applied quota.
- [PutServiceQuotaIncreaseRequestIntoTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_PutServiceQuotaIncreaseRequestIntoTemplate.html): Adds a quota increase request to your quota request template.
- [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html): Submits a quota increase request for the specified quota at the account or resource level.
- [StartAutoManagement](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StartAutoManagement.html): Starts Service Quotas Automatic Management for an AWS account, including notification preferences and excluded quotas configurations.
- [StartQuotaUtilizationReport](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StartQuotaUtilizationReport.html): Initiates the generation of a quota utilization report for your AWS account.
- [StopAutoManagement](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StopAutoManagement.html): Stops Service Quotas Automatic Management for an AWS account and removes all associated configurations.
- [TagResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_TagResource.html): Adds tags to the specified applied quota.
- [UntagResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_UntagResource.html): Removes tags from the specified applied quota.
- [UpdateAutoManagement](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_UpdateAutoManagement.html): Updates your Service Quotas Automatic Management configuration, including notification preferences and excluded quotas.


## [Data Types](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_Types.html)

- [ErrorReason](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ErrorReason.html): An error that explains why an action did not succeed.
- [MetricInfo](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_MetricInfo.html): Information about the CloudWatch metric that reflects quota usage.
- [QuotaContextInfo](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_QuotaContextInfo.html): A structure that describes the context for a resource-level quota.
- [QuotaInfo](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_QuotaInfo.html): Information on your Service Quotas for Service Quotas Automatic Management.
- [QuotaPeriod](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_QuotaPeriod.html): Information about the quota period.
- [QuotaUtilizationInfo](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_QuotaUtilizationInfo.html): Information about a quota's utilization, including the quota code, service information, current usage, and applied limits.
- [RequestedServiceQuotaChange](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestedServiceQuotaChange.html): Information about a quota increase request.
- [ServiceInfo](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ServiceInfo.html): Information about an AWS service.
- [ServiceQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ServiceQuota.html): Information about a quota.
- [ServiceQuotaIncreaseRequestInTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ServiceQuotaIncreaseRequestInTemplate.html): Information about a quota increase request.
- [Tag](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_Tag.html): A complex data type that contains a tag key and tag value.
