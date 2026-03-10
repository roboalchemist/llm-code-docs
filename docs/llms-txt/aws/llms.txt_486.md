# Source: https://docs.aws.amazon.com/iot/latest/apireference/llms.txt

# AWS IoT API Reference

## [AWS IoT](https://docs.aws.amazon.com/iot/latest/apireference/Welcome_AWS_IoT.html)

AWS IoT provides secure, bi-directional communication between Internet-connected devices (such as sensors, actuators, embedded devices, or smart appliances) and the AWS cloud. You can discover your custom IoT-Data endpoint to communicate with, configure rules for data processing and integration with other services, organize resources associated with each device (Registry), configure logging, and create and manage policies and credentials to authenticate devices.

The service endpoints that expose this API are listed in [AWS IoT Core Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html). You must use the endpoint for the region that has the resources you want to access.

The service name used by [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html)to sign the request is: execute-api.

For more information about how AWS IoT works, see the [Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-how-it-works.html).

For information about how to use the credentials provider for AWS IoT, see [Authorizing Direct Calls to AWS Services](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html).

### Actions

- [AcceptCertificateTransfer](https://docs.aws.amazon.com/iot/latest/apireference/API_AcceptCertificateTransfer.html): Accepts a pending certificate transfer.
- [AddThingToBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_AddThingToBillingGroup.html): Adds a thing to a billing group.
- [AddThingToThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_AddThingToThingGroup.html): Adds a thing to a thing group.
- [AssociateSbomWithPackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_AssociateSbomWithPackageVersion.html): Associates the selected software bill of materials (SBOM) with a specific software package version.
- [AssociateTargetsWithJob](https://docs.aws.amazon.com/iot/latest/apireference/API_AssociateTargetsWithJob.html): Associates a group with a continuous job.
- [AttachPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachPolicy.html): Attaches the specified policy to the specified principal (certificate or other credential).
- [AttachPrincipalPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachPrincipalPolicy.html): Attaches the specified policy to the specified principal (certificate or other credential).
- [AttachSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachSecurityProfile.html): Associates a Device Defender security profile with a thing group or this account.
- [AttachThingPrincipal](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachThingPrincipal.html): Attaches the specified principal to the specified thing.
- [CancelAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelAuditMitigationActionsTask.html): Cancels a mitigation action task that is in progress.
- [CancelAuditTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelAuditTask.html): Cancels an audit that is in progress.
- [CancelCertificateTransfer](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelCertificateTransfer.html): Cancels a pending transfer for the specified certificate.
- [CancelDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelDetectMitigationActionsTask.html): Cancels a Device Defender ML Detect mitigation action.
- [CancelJob](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelJob.html): Cancels a job.
- [CancelJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelJobExecution.html): Cancels the execution of a job for a given thing.
- [ClearDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_ClearDefaultAuthorizer.html): Clears the default authorizer.
- [ConfirmTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_ConfirmTopicRuleDestination.html): Confirms a topic rule destination.
- [CreateAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateAuditSuppression.html): Creates a Device Defender audit suppression.
- [CreateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateAuthorizer.html): Creates an authorizer.
- [CreateBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateBillingGroup.html): Creates a billing group.
- [CreateCertificateFromCsr](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html): Creates an X.509 certificate using the specified certificate signing request.
- [CreateCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateProvider.html): Creates an AWS IoT Core certificate provider.
- [CreateCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCommand.html): Creates a command.
- [CreateCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCustomMetric.html): Use this API to define a Custom Metric published by your devices to Device Defender.
- [CreateDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDimension.html): Create a dimension that you can use to limit the scope of a metric used in a security profile for AWS IoT Device Defender.
- [CreateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDomainConfiguration.html): Creates a domain configuration.
- [CreateDynamicThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDynamicThingGroup.html): Creates a dynamic thing group.
- [CreateFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateFleetMetric.html): Creates a fleet metric.
- [CreateJob](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateJob.html): Creates a job.
- [CreateJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateJobTemplate.html): Creates a job template.
- [CreateKeysAndCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html): Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key.
- [CreateMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateMitigationAction.html): Defines an action that can be applied to audit findings by using StartAuditMitigationActionsTask.
- [CreateOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateOTAUpdate.html): Creates an AWS IoT OTA update on a target group of things or groups.
- [CreatePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackage.html): Creates an AWS IoT software package that can be deployed to your fleet.
- [CreatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackageVersion.html): Creates a new version for an existing AWS IoT software package.
- [CreatePolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePolicy.html): Creates an AWS IoT policy.
- [CreatePolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePolicyVersion.html): Creates a new version of the specified AWS IoT policy.
- [CreateProvisioningClaim](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningClaim.html): Creates a provisioning claim.
- [CreateProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplate.html): Creates a provisioning template.
- [CreateProvisioningTemplateVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplateVersion.html): Creates a new version of a provisioning template.
- [CreateRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateRoleAlias.html): Creates a role alias.
- [CreateScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateScheduledAudit.html): Creates a scheduled audit that is run at a specified time interval.
- [CreateSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateSecurityProfile.html): Creates a Device Defender security profile.
- [CreateStream](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateStream.html): Creates a stream for delivering one or more large files in chunks over MQTT.
- [CreateThing](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThing.html): Creates a thing record in the registry.
- [CreateThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThingGroup.html): Create a thing group.
- [CreateThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThingType.html): Creates a new thing type.
- [CreateTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRule.html): Creates a rule.
- [CreateTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRuleDestination.html): Creates a topic rule destination.
- [DeleteAccountAuditConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAccountAuditConfiguration.html): Restores the default settings for Device Defender audits for this account.
- [DeleteAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuditSuppression.html): Deletes a Device Defender audit suppression.
- [DeleteAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuthorizer.html): Deletes an authorizer.
- [DeleteBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteBillingGroup.html): Deletes the billing group.
- [DeleteCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCACertificate.html): Deletes a registered CA certificate.
- [DeleteCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCertificate.html): Deletes the specified certificate.
- [DeleteCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCertificateProvider.html): Deletes a certificate provider.
- [DeleteCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCommand.html): Delete a command resource.
- [DeleteCommandExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCommandExecution.html): Delete a command execution.
- [DeleteCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCustomMetric.html): Deletes a Device Defender detect custom metric.
- [DeleteDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteDimension.html): Removes the specified dimension from your AWS accounts.
- [DeleteDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteDomainConfiguration.html): Deletes the specified domain configuration.
- [DeleteDynamicThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteDynamicThingGroup.html): Deletes a dynamic thing group.
- [DeleteFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteFleetMetric.html): Deletes the specified fleet metric.
- [DeleteJob](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteJob.html): Deletes a job and its related job executions.
- [DeleteJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteJobExecution.html): Deletes a job execution.
- [DeleteJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteJobTemplate.html): Deletes the specified job template.
- [DeleteMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteMitigationAction.html): Deletes a defined mitigation action from your AWS accounts.
- [DeleteOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteOTAUpdate.html): Delete an OTA update.
- [DeletePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackage.html): Deletes a specific version from a software package.
- [DeletePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackageVersion.html): Deletes a specific version from a software package.
- [DeletePolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePolicy.html): Deletes the specified policy.
- [DeletePolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePolicyVersion.html): Deletes the specified version of the specified policy.
- [DeleteProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteProvisioningTemplate.html): Deletes a provisioning template.
- [DeleteProvisioningTemplateVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteProvisioningTemplateVersion.html): Deletes a provisioning template version.
- [DeleteRegistrationCode](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteRegistrationCode.html): Deletes a CA certificate registration code.
- [DeleteRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteRoleAlias.html): Deletes a role alias
- [DeleteScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteScheduledAudit.html): Deletes a scheduled audit.
- [DeleteSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteSecurityProfile.html): Deletes a Device Defender security profile.
- [DeleteStream](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteStream.html): Deletes a stream.
- [DeleteThing](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThing.html): Deletes the specified thing.
- [DeleteThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThingGroup.html): Deletes a thing group.
- [DeleteThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThingType.html): Deletes the specified thing type.
- [DeleteTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteTopicRule.html): Deletes the rule.
- [DeleteTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteTopicRuleDestination.html): Deletes a topic rule destination.
- [DeleteV2LoggingLevel](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteV2LoggingLevel.html): Deletes a logging level.
- [DeprecateThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_DeprecateThingType.html): Deprecates a thing type.
- [DescribeAccountAuditConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAccountAuditConfiguration.html): Gets information about the Device Defender audit settings for this account.
- [DescribeAuditFinding](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditFinding.html): Gets information about a single audit finding.
- [DescribeAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditMitigationActionsTask.html): Gets information about an audit mitigation task that is used to apply mitigation actions to a set of audit findings.
- [DescribeAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditSuppression.html): Gets information about a Device Defender audit suppression.
- [DescribeAuditTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditTask.html): Gets information about a Device Defender audit.
- [DescribeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuthorizer.html): Describes an authorizer.
- [DescribeBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeBillingGroup.html): Returns information about a billing group.
- [DescribeCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCACertificate.html): Describes a registered CA certificate.
- [DescribeCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCertificate.html): Gets information about the specified certificate.
- [DescribeCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCertificateProvider.html): Describes a certificate provider.
- [DescribeCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCustomMetric.html): Gets information about a Device Defender detect custom metric.
- [DescribeDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDefaultAuthorizer.html): Describes the default authorizer.
- [DescribeDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDetectMitigationActionsTask.html): Gets information about a Device Defender ML Detect mitigation action.
- [DescribeDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDimension.html): Provides details about a dimension that is defined in your AWS accounts.
- [DescribeDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDomainConfiguration.html): Gets summary information about a domain configuration.
- [DescribeEncryptionConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEncryptionConfiguration.html): Retrieves the encryption configuration for resources and data of your AWS account in AWS IoT Core.
- [DescribeEndpoint](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEndpoint.html): Returns or creates a unique endpoint specific to the AWS account making the call.
- [DescribeEventConfigurations](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEventConfigurations.html): Describes event configurations.
- [DescribeFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeFleetMetric.html): Gets information about the specified fleet metric.
- [DescribeIndex](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeIndex.html): Describes a search index.
- [DescribeJob](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJob.html): Describes a job.
- [DescribeJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJobExecution.html): Describes a job execution.
- [DescribeJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJobTemplate.html): Returns information about a job template.
- [DescribeManagedJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeManagedJobTemplate.html): View details of a managed job template.
- [DescribeMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeMitigationAction.html): Gets information about a mitigation action.
- [DescribeProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeProvisioningTemplate.html): Returns information about a provisioning template.
- [DescribeProvisioningTemplateVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeProvisioningTemplateVersion.html): Returns information about a provisioning template version.
- [DescribeRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeRoleAlias.html): Describes a role alias.
- [DescribeScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeScheduledAudit.html): Gets information about a scheduled audit.
- [DescribeSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeSecurityProfile.html): Gets information about a Device Defender security profile.
- [DescribeStream](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeStream.html): Gets information about a stream.
- [DescribeThing](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThing.html): Gets information about the specified thing.
- [DescribeThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingGroup.html): Describe a thing group.
- [DescribeThingRegistrationTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingRegistrationTask.html): Describes a bulk thing provisioning task.
- [DescribeThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingType.html): Gets information about the specified thing type.
- [DetachPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachPolicy.html): Detaches a policy from the specified target.
- [DetachPrincipalPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachPrincipalPolicy.html): Removes the specified policy from the specified certificate.
- [DetachSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachSecurityProfile.html): Disassociates a Device Defender security profile from a thing group or from this account.
- [DetachThingPrincipal](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachThingPrincipal.html): Detaches the specified principal from the specified thing.
- [DisableTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_DisableTopicRule.html): Disables the rule.
- [DisassociateSbomFromPackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DisassociateSbomFromPackageVersion.html): Disassociates the selected software bill of materials (SBOM) from a specific software package version.
- [EnableTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_EnableTopicRule.html): Enables the rule.
- [GetBehaviorModelTrainingSummaries](https://docs.aws.amazon.com/iot/latest/apireference/API_GetBehaviorModelTrainingSummaries.html): Returns a Device Defender's ML Detect Security Profile training model's status.
- [GetBucketsAggregation](https://docs.aws.amazon.com/iot/latest/apireference/API_GetBucketsAggregation.html): Aggregates on indexed data with search queries pertaining to particular fields.
- [GetCardinality](https://docs.aws.amazon.com/iot/latest/apireference/API_GetCardinality.html): Returns the approximate count of unique values that match the query.
- [GetCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_GetCommand.html): Gets information about the specified command.
- [GetCommandExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_GetCommandExecution.html): Gets information about the specific command execution on a single device.
- [GetEffectivePolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_GetEffectivePolicies.html): Gets a list of the policies that have an effect on the authorization behavior of the specified device when it connects to the AWS IoT device gateway.
- [GetIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_GetIndexingConfiguration.html): Gets the indexing configuration.
- [GetJobDocument](https://docs.aws.amazon.com/iot/latest/apireference/API_GetJobDocument.html): Gets a job document.
- [GetLoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_GetLoggingOptions.html): Gets the logging options.
- [GetOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_GetOTAUpdate.html): Gets an OTA update.
- [GetPackage](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackage.html): Gets information about the specified software package.
- [GetPackageConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackageConfiguration.html): Gets information about the specified software package's configuration.
- [GetPackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackageVersion.html): Gets information about the specified package version.
- [GetPercentiles](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPercentiles.html): Groups the aggregated values that match the query into percentile groupings.
- [GetPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPolicy.html): Gets information about the specified policy with the policy document of the default version.
- [GetPolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPolicyVersion.html): Gets information about the specified policy version.
- [GetRegistrationCode](https://docs.aws.amazon.com/iot/latest/apireference/API_GetRegistrationCode.html): Gets a registration code used to register a CA certificate with AWS IoT.
- [GetStatistics](https://docs.aws.amazon.com/iot/latest/apireference/API_GetStatistics.html): Returns the count, average, sum, minimum, maximum, sum of squares, variance, and standard deviation for the specified aggregated field.
- [GetThingConnectivityData](https://docs.aws.amazon.com/iot/latest/apireference/API_GetThingConnectivityData.html): Retrieves the live connectivity status per device.
- [GetTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_GetTopicRule.html): Gets information about the rule.
- [GetTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_GetTopicRuleDestination.html): Gets information about a topic rule destination.
- [GetV2LoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_GetV2LoggingOptions.html): Gets the fine grained logging options.
- [ListActiveViolations](https://docs.aws.amazon.com/iot/latest/apireference/API_ListActiveViolations.html): Lists the active violations for a given Device Defender security profile.
- [ListAttachedPolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAttachedPolicies.html): Lists the policies attached to the specified thing group.
- [ListAuditFindings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditFindings.html): Lists the findings (results) of a Device Defender audit or of the audits performed during a specified time period. (Findings are retained for 90 days.)
- [ListAuditMitigationActionsExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsExecutions.html): Gets the status of audit mitigation action tasks that were executed.
- [ListAuditMitigationActionsTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsTasks.html): Gets a list of audit mitigation action tasks that match the specified filters.
- [ListAuditSuppressions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditSuppressions.html): Lists your Device Defender audit listings.
- [ListAuditTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditTasks.html): Lists the Device Defender audits that have been performed during a given time period.
- [ListAuthorizers](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuthorizers.html): Lists the authorizers registered in your account.
- [ListBillingGroups](https://docs.aws.amazon.com/iot/latest/apireference/API_ListBillingGroups.html): Lists the billing groups you have created.
- [ListCACertificates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCACertificates.html): Lists the CA certificates registered for your AWS account.
- [ListCertificateProviders](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificateProviders.html): Lists all your certificate providers in your AWS account.
- [ListCertificates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificates.html): Lists the certificates registered in your AWS account.
- [ListCertificatesByCA](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificatesByCA.html): List the device certificates signed by the specified CA certificate.
- [ListCommandExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCommandExecutions.html): List all command executions.
- [ListCommands](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCommands.html): List all commands in your account.
- [ListCustomMetrics](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCustomMetrics.html): Lists your Device Defender detect custom metrics.
- [ListDetectMitigationActionsExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsExecutions.html): Lists mitigation actions executions for a Device Defender ML Detect Security Profile.
- [ListDetectMitigationActionsTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsTasks.html): List of Device Defender ML Detect mitigation actions tasks.
- [ListDimensions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDimensions.html): List the set of dimensions that are defined for your AWS accounts.
- [ListDomainConfigurations](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDomainConfigurations.html): Gets a list of domain configurations for the user.
- [ListFleetMetrics](https://docs.aws.amazon.com/iot/latest/apireference/API_ListFleetMetrics.html): Lists all your fleet metrics.
- [ListIndices](https://docs.aws.amazon.com/iot/latest/apireference/API_ListIndices.html): Lists the search indices.
- [ListJobExecutionsForJob](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobExecutionsForJob.html): Lists the job executions for a job.
- [ListJobExecutionsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobExecutionsForThing.html): Lists the job executions for the specified thing.
- [ListJobs](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobs.html): Lists jobs.
- [ListJobTemplates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobTemplates.html): Returns a list of job templates.
- [ListManagedJobTemplates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListManagedJobTemplates.html): Returns a list of managed job templates.
- [ListMetricValues](https://docs.aws.amazon.com/iot/latest/apireference/API_ListMetricValues.html): Lists the values reported for an AWS IoT Device Defender metric (device-side metric, cloud-side metric, or custom metric) by the given thing during the specified time period.
- [ListMitigationActions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListMitigationActions.html): Gets a list of all mitigation actions that match the specified filter criteria.
- [ListOTAUpdates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListOTAUpdates.html): Lists OTA updates.
- [ListOutgoingCertificates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListOutgoingCertificates.html): Lists certificates that are being transferred but not yet accepted.
- [ListPackages](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPackages.html): Lists the software packages associated to the account.
- [ListPackageVersions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPackageVersions.html): Lists the software package versions associated to the account.
- [ListPolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPolicies.html): Lists your policies.
- [ListPolicyPrincipals](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPolicyPrincipals.html): Lists the principals associated with the specified policy.
- [ListPolicyVersions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPolicyVersions.html): Lists the versions of the specified policy and identifies the default version.
- [ListPrincipalPolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalPolicies.html): Lists the policies attached to the specified principal.
- [ListPrincipalThings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalThings.html): Lists the things associated with the specified principal.
- [ListPrincipalThingsV2](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalThingsV2.html): Lists the things associated with the specified principal.
- [ListProvisioningTemplates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListProvisioningTemplates.html): Lists the provisioning templates in your AWS account.
- [ListProvisioningTemplateVersions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListProvisioningTemplateVersions.html): A list of provisioning template versions.
- [ListRelatedResourcesForAuditFinding](https://docs.aws.amazon.com/iot/latest/apireference/API_ListRelatedResourcesForAuditFinding.html): The related resources of an Audit finding.
- [ListRoleAliases](https://docs.aws.amazon.com/iot/latest/apireference/API_ListRoleAliases.html): Lists the role aliases registered in your account.
- [ListSbomValidationResults](https://docs.aws.amazon.com/iot/latest/apireference/API_ListSbomValidationResults.html): The validation results for all software bill of materials (SBOM) attached to a specific software package version.
- [ListScheduledAudits](https://docs.aws.amazon.com/iot/latest/apireference/API_ListScheduledAudits.html): Lists all of your scheduled audits.
- [ListSecurityProfiles](https://docs.aws.amazon.com/iot/latest/apireference/API_ListSecurityProfiles.html): Lists the Device Defender security profiles you've created.
- [ListSecurityProfilesForTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_ListSecurityProfilesForTarget.html): Lists the Device Defender security profiles attached to a target (thing group).
- [ListStreams](https://docs.aws.amazon.com/iot/latest/apireference/API_ListStreams.html): Lists all of the streams in your AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTagsForResource.html): Lists the tags (metadata) you have assigned to the resource.
- [ListTargetsForPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTargetsForPolicy.html): List targets for the specified policy.
- [ListTargetsForSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTargetsForSecurityProfile.html): Lists the targets (thing groups) associated with a given Device Defender security profile.
- [ListThingGroups](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingGroups.html): List the thing groups in your account.
- [ListThingGroupsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingGroupsForThing.html): List the thing groups to which the specified thing belongs.
- [ListThingPrincipals](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingPrincipals.html): Lists the principals associated with the specified thing.
- [ListThingPrincipalsV2](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingPrincipalsV2.html): Lists the principals associated with the specified thing.
- [ListThingRegistrationTaskReports](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingRegistrationTaskReports.html): Information about the thing registration tasks.
- [ListThingRegistrationTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingRegistrationTasks.html): List bulk thing provisioning tasks.
- [ListThings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThings.html): Lists your things.
- [ListThingsInBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingsInBillingGroup.html): Lists the things you have added to the given billing group.
- [ListThingsInThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingsInThingGroup.html): Lists the things in the specified group.
- [ListThingTypes](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingTypes.html): Lists the existing thing types.
- [ListTopicRuleDestinations](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTopicRuleDestinations.html): Lists all the topic rule destinations in your AWS account.
- [ListTopicRules](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTopicRules.html): Lists the rules for the specific topic.
- [ListV2LoggingLevels](https://docs.aws.amazon.com/iot/latest/apireference/API_ListV2LoggingLevels.html): Lists logging levels.
- [ListViolationEvents](https://docs.aws.amazon.com/iot/latest/apireference/API_ListViolationEvents.html): Lists the Device Defender security profile violations discovered during the given time period.
- [PutVerificationStateOnViolation](https://docs.aws.amazon.com/iot/latest/apireference/API_PutVerificationStateOnViolation.html): Set a verification state and provide a description of that verification state on a violation (detect alarm).
- [RegisterCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCACertificate.html): Registers a CA certificate with AWS IoT Core.
- [RegisterCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificate.html): Registers a device certificate with AWS IoT in the same certificate mode as the signing CA.
- [RegisterCertificateWithoutCA](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificateWithoutCA.html): Register a certificate that does not have a certificate authority (CA).
- [RegisterThing](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterThing.html): Provisions a thing in the device registry.
- [RejectCertificateTransfer](https://docs.aws.amazon.com/iot/latest/apireference/API_RejectCertificateTransfer.html): Rejects a pending certificate transfer.
- [RemoveThingFromBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_RemoveThingFromBillingGroup.html): Removes the given thing from the billing group.
- [RemoveThingFromThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_RemoveThingFromThingGroup.html): Remove the specified thing from the specified group.
- [ReplaceTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_ReplaceTopicRule.html): Replaces the rule.
- [SearchIndex](https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html): The query search index.
- [SetDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_SetDefaultAuthorizer.html): Sets the default authorizer.
- [SetDefaultPolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_SetDefaultPolicyVersion.html): Sets the specified version of the specified policy as the policy's default (operative) version.
- [SetLoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_SetLoggingOptions.html): Sets the logging options.
- [SetV2LoggingLevel](https://docs.aws.amazon.com/iot/latest/apireference/API_SetV2LoggingLevel.html): Sets the logging level.
- [SetV2LoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_SetV2LoggingOptions.html): Sets the logging options for the V2 logging service.
- [StartAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartAuditMitigationActionsTask.html): Starts a task that applies a set of mitigation actions to the specified target.
- [StartDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartDetectMitigationActionsTask.html): Starts a Device Defender ML Detect mitigation actions task.
- [StartOnDemandAuditTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartOnDemandAuditTask.html): Starts an on-demand Device Defender audit.
- [StartThingRegistrationTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartThingRegistrationTask.html): Creates a bulk thing provisioning task.
- [StopThingRegistrationTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StopThingRegistrationTask.html): Cancels a bulk thing provisioning task.
- [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_TagResource.html): Adds to or modifies the tags of the given resource.
- [TestAuthorization](https://docs.aws.amazon.com/iot/latest/apireference/API_TestAuthorization.html): Tests if a specified principal is authorized to perform an AWS IoT action on a specified resource.
- [TestInvokeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_TestInvokeAuthorizer.html): Tests a custom authorization behavior by invoking a specified custom authorizer.
- [TransferCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_TransferCertificate.html): Transfers the specified certificate to the specified AWS account.
- [UntagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_UntagResource.html): Removes the given tags (metadata) from the resource.
- [UpdateAccountAuditConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAccountAuditConfiguration.html): Configures or reconfigures the Device Defender audit settings for this account.
- [UpdateAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuditSuppression.html): Updates a Device Defender audit suppression.
- [UpdateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuthorizer.html): Updates an authorizer.
- [UpdateBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateBillingGroup.html): Updates information about the billing group.
- [UpdateCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCACertificate.html): Updates a registered CA certificate.
- [UpdateCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificate.html): Updates the status of the specified certificate.
- [UpdateCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificateProvider.html): Updates a certificate provider.
- [UpdateCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCommand.html): Update information about a command or mark a command for deprecation.
- [UpdateCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCustomMetric.html): Updates a Device Defender detect custom metric.
- [UpdateDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDimension.html): Updates the definition for a dimension.
- [UpdateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDomainConfiguration.html): Updates values stored in the domain configuration.
- [UpdateDynamicThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDynamicThingGroup.html): Updates a dynamic thing group.
- [UpdateEncryptionConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateEncryptionConfiguration.html): Updates the encryption configuration.
- [UpdateEventConfigurations](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateEventConfigurations.html): Updates the event configurations.
- [UpdateFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateFleetMetric.html): Updates the data for a fleet metric.
- [UpdateIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateIndexingConfiguration.html): Updates the search configuration.
- [UpdateJob](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateJob.html): Updates supported fields of the specified job.
- [UpdateMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateMitigationAction.html): Updates the definition for the specified mitigation action.
- [UpdatePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackage.html): Updates the supported fields for a specific software package.
- [UpdatePackageConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageConfiguration.html): Updates the software package configuration.
- [UpdatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageVersion.html): Updates the supported fields for a specific package version.
- [UpdateProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateProvisioningTemplate.html): Updates a provisioning template.
- [UpdateRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateRoleAlias.html): Updates a role alias.
- [UpdateScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateScheduledAudit.html): Updates a scheduled audit, including which checks are performed and how often the audit takes place.
- [UpdateSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateSecurityProfile.html): Updates a Device Defender security profile.
- [UpdateStream](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateStream.html): Updates an existing stream.
- [UpdateThing](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThing.html): Updates the data for a thing.
- [UpdateThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingGroup.html): Update a thing group.
- [UpdateThingGroupsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingGroupsForThing.html): Updates the groups to which the thing belongs.
- [UpdateThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingType.html): Updates a thing type.
- [UpdateTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateTopicRuleDestination.html): Updates a topic rule destination.
- [ValidateSecurityProfileBehaviors](https://docs.aws.amazon.com/iot/latest/apireference/API_ValidateSecurityProfileBehaviors.html): Validates a Device Defender security profile behaviors specification.

### Data Types

- [AbortConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_AbortConfig.html): The criteria that determine when and how a job abort takes place.
- [AbortCriteria](https://docs.aws.amazon.com/iot/latest/apireference/API_AbortCriteria.html): The criteria that determine when and how a job abort takes place.
- [Action](https://docs.aws.amazon.com/iot/latest/apireference/API_Action.html): Describes the actions associated with a rule.
- [ActiveViolation](https://docs.aws.amazon.com/iot/latest/apireference/API_ActiveViolation.html): Information about an active Device Defender security profile behavior violation.
- [AddThingsToThingGroupParams](https://docs.aws.amazon.com/iot/latest/apireference/API_AddThingsToThingGroupParams.html): Parameters used when defining a mitigation action that move a set of things to a thing group.
- [AggregationType](https://docs.aws.amazon.com/iot/latest/apireference/API_AggregationType.html): The type of aggregation queries.
- [AlertTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_AlertTarget.html): A structure containing the alert target ARN and the role ARN.
- [Allowed](https://docs.aws.amazon.com/iot/latest/apireference/API_Allowed.html): Contains information that allowed the authorization.
- [AssetPropertyTimestamp](https://docs.aws.amazon.com/iot/latest/apireference/API_AssetPropertyTimestamp.html): An asset property timestamp entry containing the following information.
- [AssetPropertyValue](https://docs.aws.amazon.com/iot/latest/apireference/API_AssetPropertyValue.html): An asset property value entry containing the following information.
- [AssetPropertyVariant](https://docs.aws.amazon.com/iot/latest/apireference/API_AssetPropertyVariant.html): Contains an asset property value (of a single type).
- [AttributePayload](https://docs.aws.amazon.com/iot/latest/apireference/API_AttributePayload.html): The attribute payload.
- [AuditCheckConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditCheckConfiguration.html): Which audit checks are enabled and disabled for this account.
- [AuditCheckDetails](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditCheckDetails.html): Information about the audit check.
- [AuditFinding](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditFinding.html): The findings (results) of the audit.
- [AuditMitigationActionExecutionMetadata](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditMitigationActionExecutionMetadata.html): Returned by ListAuditMitigationActionsTask, this object contains information that describes a mitigation action that has been started.
- [AuditMitigationActionsTaskMetadata](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditMitigationActionsTaskMetadata.html): Information about an audit mitigation actions task that is returned by ListAuditMitigationActionsTasks.
- [AuditMitigationActionsTaskTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditMitigationActionsTaskTarget.html): Used in MitigationActionParams, this information identifies the target findings to which the mitigation actions are applied.
- [AuditNotificationTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditNotificationTarget.html): Information about the targets to which audit notifications are sent.
- [AuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditSuppression.html): Filters out specific findings of a Device Defender audit.
- [AuditTaskMetadata](https://docs.aws.amazon.com/iot/latest/apireference/API_AuditTaskMetadata.html): The audits that were performed.
- [AuthInfo](https://docs.aws.amazon.com/iot/latest/apireference/API_AuthInfo.html): A collection of authorization information.
- [AuthorizerConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_AuthorizerConfig.html): An object that specifies the authorization service for a domain.
- [AuthorizerDescription](https://docs.aws.amazon.com/iot/latest/apireference/API_AuthorizerDescription.html): The authorizer description.
- [AuthorizerSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_AuthorizerSummary.html): The authorizer summary.
- [AuthResult](https://docs.aws.amazon.com/iot/latest/apireference/API_AuthResult.html): The authorizer result.
- [AwsJobAbortConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobAbortConfig.html): The criteria that determine when and how a job abort takes place.
- [AwsJobAbortCriteria](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobAbortCriteria.html): The criteria that determine when and how a job abort takes place.
- [AwsJobExecutionsRolloutConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobExecutionsRolloutConfig.html): Configuration for the rollout of OTA updates.
- [AwsJobExponentialRolloutRate](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobExponentialRolloutRate.html): The rate of increase for a job rollout.
- [AwsJobPresignedUrlConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobPresignedUrlConfig.html): Configuration information for pre-signed URLs.
- [AwsJobRateIncreaseCriteria](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobRateIncreaseCriteria.html): The criteria to initiate the increase in rate of rollout for a job.
- [AwsJobTimeoutConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobTimeoutConfig.html): Specifies the amount of time each device has to finish its execution of the job.
- [AwsJsonSubstitutionCommandPreprocessorConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJsonSubstitutionCommandPreprocessorConfig.html): Configures the command to treat the payloadTemplate as a JSON document for preprocessing.
- [BatchConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_BatchConfig.html): Configuration settings for batching.
- [Behavior](https://docs.aws.amazon.com/iot/latest/apireference/API_Behavior.html): A Device Defender security profile behavior.
- [BehaviorCriteria](https://docs.aws.amazon.com/iot/latest/apireference/API_BehaviorCriteria.html): The criteria by which the behavior is determined to be normal.
- [BehaviorModelTrainingSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_BehaviorModelTrainingSummary.html): The summary of an ML Detect behavior model.
- [BillingGroupMetadata](https://docs.aws.amazon.com/iot/latest/apireference/API_BillingGroupMetadata.html): Additional information about the billing group.
- [BillingGroupProperties](https://docs.aws.amazon.com/iot/latest/apireference/API_BillingGroupProperties.html): The properties of a billing group.
- [Bucket](https://docs.aws.amazon.com/iot/latest/apireference/API_Bucket.html): A count of documents that meets a specific aggregation criteria.
- [BucketsAggregationType](https://docs.aws.amazon.com/iot/latest/apireference/API_BucketsAggregationType.html): The type of bucketed aggregation performed.
- [CACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_CACertificate.html): A CA certificate.
- [CACertificateDescription](https://docs.aws.amazon.com/iot/latest/apireference/API_CACertificateDescription.html): Describes a CA certificate.
- [Certificate](https://docs.aws.amazon.com/iot/latest/apireference/API_Certificate.html): Information about a certificate.
- [CertificateDescription](https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateDescription.html): Describes a certificate.
- [CertificateProviderSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateProviderSummary.html): The certificate provider summary.
- [CertificateValidity](https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateValidity.html): When the certificate is valid.
- [ClientCertificateConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_ClientCertificateConfig.html): An object that speciï¬es the client certificate conï¬guration for a domain.
- [CloudwatchAlarmAction](https://docs.aws.amazon.com/iot/latest/apireference/API_CloudwatchAlarmAction.html): Describes an action that updates a CloudWatch alarm.
- [CloudwatchLogsAction](https://docs.aws.amazon.com/iot/latest/apireference/API_CloudwatchLogsAction.html): Describes an action that sends data to CloudWatch Logs.
- [CloudwatchMetricAction](https://docs.aws.amazon.com/iot/latest/apireference/API_CloudwatchMetricAction.html): Describes an action that captures a CloudWatch metric.
- [CodeSigning](https://docs.aws.amazon.com/iot/latest/apireference/API_CodeSigning.html): Describes the method to use when code signing a file.
- [CodeSigningCertificateChain](https://docs.aws.amazon.com/iot/latest/apireference/API_CodeSigningCertificateChain.html): Describes the certificate chain being used when code signing a file.
- [CodeSigningSignature](https://docs.aws.amazon.com/iot/latest/apireference/API_CodeSigningSignature.html): Describes the signature for a file.
- [CommandExecutionResult](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandExecutionResult.html): The result value of the command execution.
- [CommandExecutionSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandExecutionSummary.html): Summary information about a particular command execution.
- [CommandParameter](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameter.html): A map of key-value pairs that describe the command.
- [CommandParameterValue](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameterValue.html): The value of a command parameter used to create a command execution.
- [CommandParameterValueComparisonOperand](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameterValueComparisonOperand.html): The comparison operand used to compare the defined value against the value supplied in request.
- [CommandParameterValueCondition](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameterValueCondition.html): A condition for the command parameter that must be evaluated to true for successful creation of a command execution.
- [CommandParameterValueNumberRange](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameterValueNumberRange.html): The numerical range value type to compare a command parameter value against.
- [CommandPayload](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandPayload.html): The command payload object that contains the instructions for the device to process.
- [CommandPreprocessor](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandPreprocessor.html): Configuration that determines how the payloadTemplate is processed by the service to generate the final payload sent to devices at StartCommandExecution API invocation.
- [CommandSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_CommandSummary.html): Summary information about a particular command resource.
- [Configuration](https://docs.aws.amazon.com/iot/latest/apireference/API_Configuration.html): Configuration.
- [ConfigurationDetails](https://docs.aws.amazon.com/iot/latest/apireference/API_ConfigurationDetails.html): The encryption configuration details that include the status information of the AWS Key Management Service (AWS KMS) key and the AWS KMS access role.
- [CustomCodeSigning](https://docs.aws.amazon.com/iot/latest/apireference/API_CustomCodeSigning.html): Describes a custom method used to code sign a file.
- [Denied](https://docs.aws.amazon.com/iot/latest/apireference/API_Denied.html): Contains information that denied the authorization.
- [Destination](https://docs.aws.amazon.com/iot/latest/apireference/API_Destination.html): Describes the location of the updated firmware.
- [DetectMitigationActionExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_DetectMitigationActionExecution.html): Describes which mitigation actions should be executed.
- [DetectMitigationActionsTaskStatistics](https://docs.aws.amazon.com/iot/latest/apireference/API_DetectMitigationActionsTaskStatistics.html): The statistics of a mitigation action task.
- [DetectMitigationActionsTaskSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_DetectMitigationActionsTaskSummary.html): The summary of the mitigation action tasks.
- [DetectMitigationActionsTaskTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_DetectMitigationActionsTaskTarget.html): The target of a mitigation action task.
- [DocumentParameter](https://docs.aws.amazon.com/iot/latest/apireference/API_DocumentParameter.html): A map of key-value pairs containing the patterns that need to be replaced in a managed template job document schema.
- [DomainConfigurationSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_DomainConfigurationSummary.html): The summary of a domain configuration.
- [DynamoDBAction](https://docs.aws.amazon.com/iot/latest/apireference/API_DynamoDBAction.html): Describes an action to write to a DynamoDB table.
- [DynamoDBv2Action](https://docs.aws.amazon.com/iot/latest/apireference/API_DynamoDBv2Action.html): Describes an action to write to a DynamoDB table.
- [EffectivePolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_EffectivePolicy.html): The policy that has the effect on the authorization results.
- [ElasticsearchAction](https://docs.aws.amazon.com/iot/latest/apireference/API_ElasticsearchAction.html): Describes an action that writes data to an Amazon OpenSearch Service domain.
- [EnableIoTLoggingParams](https://docs.aws.amazon.com/iot/latest/apireference/API_EnableIoTLoggingParams.html): Parameters used when defining a mitigation action that enable AWS IoT Core logging.
- [ErrorInfo](https://docs.aws.amazon.com/iot/latest/apireference/API_ErrorInfo.html): Error information.
- [ExplicitDeny](https://docs.aws.amazon.com/iot/latest/apireference/API_ExplicitDeny.html): Information that explicitly denies authorization.
- [ExponentialRolloutRate](https://docs.aws.amazon.com/iot/latest/apireference/API_ExponentialRolloutRate.html): Allows you to create an exponential rate of rollout for a job.
- [Field](https://docs.aws.amazon.com/iot/latest/apireference/API_Field.html): Describes the name and data type at a field.
- [FileLocation](https://docs.aws.amazon.com/iot/latest/apireference/API_FileLocation.html): The location of the OTA update.
- [FirehoseAction](https://docs.aws.amazon.com/iot/latest/apireference/API_FirehoseAction.html): Describes an action that writes data to an Amazon Kinesis Firehose stream.
- [FleetMetricNameAndArn](https://docs.aws.amazon.com/iot/latest/apireference/API_FleetMetricNameAndArn.html): The name and ARN of a fleet metric.
- [GeoLocationTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_GeoLocationTarget.html): A geolocation target that you select to index.
- [GroupNameAndArn](https://docs.aws.amazon.com/iot/latest/apireference/API_GroupNameAndArn.html): The name and ARN of a group.
- [HttpAction](https://docs.aws.amazon.com/iot/latest/apireference/API_HttpAction.html): Send data to an HTTPS endpoint.
- [HttpActionHeader](https://docs.aws.amazon.com/iot/latest/apireference/API_HttpActionHeader.html): The HTTP action header.
- [HttpAuthorization](https://docs.aws.amazon.com/iot/latest/apireference/API_HttpAuthorization.html): The authorization method used to send messages.
- [HttpContext](https://docs.aws.amazon.com/iot/latest/apireference/API_HttpContext.html): Specifies the HTTP context to use for the test authorizer request.
- [HttpUrlDestinationConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_HttpUrlDestinationConfiguration.html): HTTP URL destination configuration used by the topic rule's HTTP action.
- [HttpUrlDestinationProperties](https://docs.aws.amazon.com/iot/latest/apireference/API_HttpUrlDestinationProperties.html): HTTP URL destination properties.
- [HttpUrlDestinationSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_HttpUrlDestinationSummary.html): Information about an HTTP URL destination.
- [ImplicitDeny](https://docs.aws.amazon.com/iot/latest/apireference/API_ImplicitDeny.html): Information that implicitly denies authorization.
- [IndexingFilter](https://docs.aws.amazon.com/iot/latest/apireference/API_IndexingFilter.html): Provides additional selections for named shadows and geolocation data.
- [IotAnalyticsAction](https://docs.aws.amazon.com/iot/latest/apireference/API_IotAnalyticsAction.html): Sends message data to an AWS IoT Analytics channel.
- [IotEventsAction](https://docs.aws.amazon.com/iot/latest/apireference/API_IotEventsAction.html): Sends an input to an AWS IoT Events detector.
- [IotSiteWiseAction](https://docs.aws.amazon.com/iot/latest/apireference/API_IotSiteWiseAction.html): Describes an action to send data from an MQTT message that triggered the rule to AWS IoT SiteWise asset properties.
- [IssuerCertificateIdentifier](https://docs.aws.amazon.com/iot/latest/apireference/API_IssuerCertificateIdentifier.html): The certificate issuer indentifier.
- [Job](https://docs.aws.amazon.com/iot/latest/apireference/API_Job.html): The Job object contains details about a job.
- [JobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecution.html): The job execution object represents the execution of a job on a particular device.
- [JobExecutionsRetryConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionsRetryConfig.html): The configuration that determines how many retries are allowed for each failure type for a job.
- [JobExecutionsRolloutConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionsRolloutConfig.html): Allows you to create a staged rollout of a job.
- [JobExecutionStatusDetails](https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionStatusDetails.html): Details of the job execution status.
- [JobExecutionSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionSummary.html): The job execution summary.
- [JobExecutionSummaryForJob](https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionSummaryForJob.html): Contains a summary of information about job executions for a specific job.
- [JobExecutionSummaryForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionSummaryForThing.html): The job execution summary for a thing.
- [JobProcessDetails](https://docs.aws.amazon.com/iot/latest/apireference/API_JobProcessDetails.html): The job process details.
- [JobSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_JobSummary.html): The job summary.
- [JobTemplateSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_JobTemplateSummary.html): An object that contains information about the job template.
- [KafkaAction](https://docs.aws.amazon.com/iot/latest/apireference/API_KafkaAction.html): Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.
- [KafkaActionHeader](https://docs.aws.amazon.com/iot/latest/apireference/API_KafkaActionHeader.html): Specifies a Kafka header using key-value pairs when you create a Ruleâs Kafka Action.
- [KeyPair](https://docs.aws.amazon.com/iot/latest/apireference/API_KeyPair.html): Describes a key pair.
- [KinesisAction](https://docs.aws.amazon.com/iot/latest/apireference/API_KinesisAction.html): Describes an action to write data to an Amazon Kinesis stream.
- [LambdaAction](https://docs.aws.amazon.com/iot/latest/apireference/API_LambdaAction.html): Describes an action to invoke a Lambda function.
- [LocationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_LocationAction.html): The Amazon Location rule action sends device location updates from an MQTT message to an Amazon Location tracker resource.
- [LocationTimestamp](https://docs.aws.amazon.com/iot/latest/apireference/API_LocationTimestamp.html): Describes how to interpret an application-defined timestamp value from an MQTT message payload and the precision of that value.
- [LogEventConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_LogEventConfiguration.html): Configuration for event-based logging that specifies which event types to log and their logging settings.
- [LoggingOptionsPayload](https://docs.aws.amazon.com/iot/latest/apireference/API_LoggingOptionsPayload.html): Describes the logging options payload.
- [LogTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_LogTarget.html): A log target.
- [LogTargetConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_LogTargetConfiguration.html): The target configuration.
- [MachineLearningDetectionConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_MachineLearningDetectionConfig.html): The configuration of an ML Detect Security Profile.
- [MaintenanceWindow](https://docs.aws.amazon.com/iot/latest/apireference/API_MaintenanceWindow.html): An optional configuration within the SchedulingConfig to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.
- [ManagedJobTemplateSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_ManagedJobTemplateSummary.html): An object that contains information about the managed template.
- [MetricDatum](https://docs.aws.amazon.com/iot/latest/apireference/API_MetricDatum.html): A metric.
- [MetricDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_MetricDimension.html): The dimension of a metric.
- [MetricsExportConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_MetricsExportConfig.html): Set configurations for metrics export.
- [MetricToRetain](https://docs.aws.amazon.com/iot/latest/apireference/API_MetricToRetain.html): The metric you want to retain.
- [MetricValue](https://docs.aws.amazon.com/iot/latest/apireference/API_MetricValue.html): The value to be compared with the metric.
- [MitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_MitigationAction.html): Describes which changes should be applied as part of a mitigation action.
- [MitigationActionIdentifier](https://docs.aws.amazon.com/iot/latest/apireference/API_MitigationActionIdentifier.html): Information that identifies a mitigation action.
- [MitigationActionParams](https://docs.aws.amazon.com/iot/latest/apireference/API_MitigationActionParams.html): The set of parameters for this mitigation action.
- [Mqtt5Configuration](https://docs.aws.amazon.com/iot/latest/apireference/API_Mqtt5Configuration.html): The configuration to add user-defined properties to enrich MQTT 5 messages.
- [MqttContext](https://docs.aws.amazon.com/iot/latest/apireference/API_MqttContext.html): Specifies the MQTT context to use for the test authorizer request
- [MqttHeaders](https://docs.aws.amazon.com/iot/latest/apireference/API_MqttHeaders.html): Specifies MQTT Version 5.0 headers information.
- [NonCompliantResource](https://docs.aws.amazon.com/iot/latest/apireference/API_NonCompliantResource.html): Information about the resource that was noncompliant with the audit check.
- [OpenSearchAction](https://docs.aws.amazon.com/iot/latest/apireference/API_OpenSearchAction.html): Describes an action that writes data to an Amazon OpenSearch Service domain.
- [OTAUpdateFile](https://docs.aws.amazon.com/iot/latest/apireference/API_OTAUpdateFile.html): Describes a file to be associated with an OTA update.
- [OTAUpdateInfo](https://docs.aws.amazon.com/iot/latest/apireference/API_OTAUpdateInfo.html): Information about an OTA update.
- [OTAUpdateSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_OTAUpdateSummary.html): An OTA update summary.
- [OutgoingCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_OutgoingCertificate.html): A certificate that has been transferred but not yet accepted.
- [PackageSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_PackageSummary.html): A summary of information about a software package.
- [PackageVersionArtifact](https://docs.aws.amazon.com/iot/latest/apireference/API_PackageVersionArtifact.html): A specific package version artifact associated with a software package version.
- [PackageVersionSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_PackageVersionSummary.html): A summary of information about a package version.
- [PercentPair](https://docs.aws.amazon.com/iot/latest/apireference/API_PercentPair.html): Describes the percentile and percentile value.
- [Policy](https://docs.aws.amazon.com/iot/latest/apireference/API_Policy.html): Describes an AWS IoT policy.
- [PolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_PolicyVersion.html): Describes a policy version.
- [PolicyVersionIdentifier](https://docs.aws.amazon.com/iot/latest/apireference/API_PolicyVersionIdentifier.html): Information about the version of the policy associated with the resource.
- [PresignedUrlConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_PresignedUrlConfig.html): Configuration for pre-signed S3 URLs.
- [PrincipalThingObject](https://docs.aws.amazon.com/iot/latest/apireference/API_PrincipalThingObject.html): An object that represents the thing and the type of relation it has with the principal.
- [PropagatingAttribute](https://docs.aws.amazon.com/iot/latest/apireference/API_PropagatingAttribute.html): An object that represents the connection attribute, thing attribute, and the user property key.
- [ProvisioningHook](https://docs.aws.amazon.com/iot/latest/apireference/API_ProvisioningHook.html): Structure that contains payloadVersion and targetArn.
- [ProvisioningTemplateSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_ProvisioningTemplateSummary.html): A summary of information about a provisioning template.
- [ProvisioningTemplateVersionSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_ProvisioningTemplateVersionSummary.html): A summary of information about a fleet provision template version.
- [PublishFindingToSnsParams](https://docs.aws.amazon.com/iot/latest/apireference/API_PublishFindingToSnsParams.html): Parameters to define a mitigation action that publishes findings to Amazon SNS.
- [PutAssetPropertyValueEntry](https://docs.aws.amazon.com/iot/latest/apireference/API_PutAssetPropertyValueEntry.html): An asset property value entry containing the following information.
- [PutItemInput](https://docs.aws.amazon.com/iot/latest/apireference/API_PutItemInput.html): The input for the DynamoActionVS action that specifies the DynamoDB table to which the message data will be written.
- [RateIncreaseCriteria](https://docs.aws.amazon.com/iot/latest/apireference/API_RateIncreaseCriteria.html): Allows you to define a criteria to initiate the increase in rate of rollout for a job.
- [RegistrationConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_RegistrationConfig.html): The registration configuration.
- [RelatedResource](https://docs.aws.amazon.com/iot/latest/apireference/API_RelatedResource.html): Information about a related resource.
- [ReplaceDefaultPolicyVersionParams](https://docs.aws.amazon.com/iot/latest/apireference/API_ReplaceDefaultPolicyVersionParams.html): Parameters to define a mitigation action that adds a blank policy to restrict permissions.
- [RepublishAction](https://docs.aws.amazon.com/iot/latest/apireference/API_RepublishAction.html): Describes an action to republish to another topic.
- [ResourceIdentifier](https://docs.aws.amazon.com/iot/latest/apireference/API_ResourceIdentifier.html): Information that identifies the noncompliant resource.
- [RetryCriteria](https://docs.aws.amazon.com/iot/latest/apireference/API_RetryCriteria.html): The criteria that determines how many retries are allowed for each failure type for a job.
- [RoleAliasDescription](https://docs.aws.amazon.com/iot/latest/apireference/API_RoleAliasDescription.html): Role alias description.
- [S3Action](https://docs.aws.amazon.com/iot/latest/apireference/API_S3Action.html): Describes an action to write data to an Amazon S3 bucket.
- [S3Destination](https://docs.aws.amazon.com/iot/latest/apireference/API_S3Destination.html): Describes the location of updated firmware in S3.
- [S3Location](https://docs.aws.amazon.com/iot/latest/apireference/API_S3Location.html): The S3 location.
- [SalesforceAction](https://docs.aws.amazon.com/iot/latest/apireference/API_SalesforceAction.html): Describes an action to write a message to a Salesforce IoT Cloud Input Stream.
- [Sbom](https://docs.aws.amazon.com/iot/latest/apireference/API_Sbom.html): A specific software bill of matrerials associated with a software package version.
- [SbomValidationResultSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_SbomValidationResultSummary.html): A summary of the validation results for a specific software bill of materials (SBOM) attached to a software package version.
- [ScheduledAuditMetadata](https://docs.aws.amazon.com/iot/latest/apireference/API_ScheduledAuditMetadata.html): Information about the scheduled audit.
- [ScheduledJobRollout](https://docs.aws.amazon.com/iot/latest/apireference/API_ScheduledJobRollout.html): Displays the next seven maintenance window occurrences and their start times.
- [SchedulingConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_SchedulingConfig.html): Specifies the date and time that a job will begin the rollout of the job document to all devices in the target group.
- [SecurityProfileIdentifier](https://docs.aws.amazon.com/iot/latest/apireference/API_SecurityProfileIdentifier.html): Identifying information for a Device Defender security profile.
- [SecurityProfileTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_SecurityProfileTarget.html): A target to which an alert is sent when a security profile behavior is violated.
- [SecurityProfileTargetMapping](https://docs.aws.amazon.com/iot/latest/apireference/API_SecurityProfileTargetMapping.html): Information about a security profile and the target associated with it.
- [ServerCertificateConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_ServerCertificateConfig.html): The server certificate configuration.
- [ServerCertificateSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_ServerCertificateSummary.html): An object that contains information about a server certificate.
- [SigningProfileParameter](https://docs.aws.amazon.com/iot/latest/apireference/API_SigningProfileParameter.html): Describes the code-signing profile.
- [SigV4Authorization](https://docs.aws.amazon.com/iot/latest/apireference/API_SigV4Authorization.html): For more information, see Signature Version 4 signing process.
- [SnsAction](https://docs.aws.amazon.com/iot/latest/apireference/API_SnsAction.html): Describes an action to publish to an Amazon SNS topic.
- [SqsAction](https://docs.aws.amazon.com/iot/latest/apireference/API_SqsAction.html): Describes an action to publish data to an Amazon SQS queue.
- [StartSigningJobParameter](https://docs.aws.amazon.com/iot/latest/apireference/API_StartSigningJobParameter.html): Information required to start a signing job.
- [StatisticalThreshold](https://docs.aws.amazon.com/iot/latest/apireference/API_StatisticalThreshold.html): A statistical ranking (percentile) that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
- [Statistics](https://docs.aws.amazon.com/iot/latest/apireference/API_Statistics.html): A map of key-value pairs for all supported statistics.
- [StatusReason](https://docs.aws.amazon.com/iot/latest/apireference/API_StatusReason.html): Provide additional context about the status of a command execution using a reason code and description.
- [StepFunctionsAction](https://docs.aws.amazon.com/iot/latest/apireference/API_StepFunctionsAction.html): Starts execution of a Step Functions state machine.
- [Stream](https://docs.aws.amazon.com/iot/latest/apireference/API_Stream.html): Describes a group of files that can be streamed.
- [StreamFile](https://docs.aws.amazon.com/iot/latest/apireference/API_StreamFile.html): Represents a file to stream.
- [StreamInfo](https://docs.aws.amazon.com/iot/latest/apireference/API_StreamInfo.html): Information about a stream.
- [StreamSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_StreamSummary.html): A summary of a stream.
- [Tag](https://docs.aws.amazon.com/iot/latest/apireference/API_Tag.html): A set of key/value pairs that are used to manage the resource.
- [TaskStatistics](https://docs.aws.amazon.com/iot/latest/apireference/API_TaskStatistics.html): Statistics for the checks performed during the audit.
- [TaskStatisticsForAuditCheck](https://docs.aws.amazon.com/iot/latest/apireference/API_TaskStatisticsForAuditCheck.html): Provides summary counts of how many tasks for findings are in a particular state.
- [TermsAggregation](https://docs.aws.amazon.com/iot/latest/apireference/API_TermsAggregation.html): Performs an aggregation that will return a list of buckets.
- [ThingAttribute](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingAttribute.html): The properties of the thing, including thing name, thing type name, and a list of thing attributes.
- [ThingConnectivity](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingConnectivity.html): The connectivity status of the thing.
- [ThingDocument](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingDocument.html): The thing search index document.
- [ThingGroupDocument](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingGroupDocument.html): The thing group search index document.
- [ThingGroupIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingGroupIndexingConfiguration.html): Thing group indexing configuration.
- [ThingGroupMetadata](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingGroupMetadata.html): Thing group metadata.
- [ThingGroupProperties](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingGroupProperties.html): Thing group properties.
- [ThingIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingIndexingConfiguration.html): The thing indexing configuration.
- [ThingPrincipalObject](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingPrincipalObject.html): An object that represents the principal and the type of relation it has with the thing.
- [ThingTypeDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingTypeDefinition.html): The definition of the thing type, including thing type name and description.
- [ThingTypeMetadata](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingTypeMetadata.html): The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when time was deprecated.
- [ThingTypeProperties](https://docs.aws.amazon.com/iot/latest/apireference/API_ThingTypeProperties.html): The ThingTypeProperties contains information about the thing type including: a thing type description, and a list of searchable thing attribute names.
- [TimeFilter](https://docs.aws.amazon.com/iot/latest/apireference/API_TimeFilter.html): A filter that can be used to list command executions for a device that started or completed before or after a particular date and time.
- [TimeoutConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_TimeoutConfig.html): Specifies the amount of time each device has to finish its execution of the job.
- [TimestreamAction](https://docs.aws.amazon.com/iot/latest/apireference/API_TimestreamAction.html): The Timestream rule action writes attributes (measures) from an MQTT message into an Amazon Timestream table.
- [TimestreamDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_TimestreamDimension.html): Metadata attributes of the time series that are written in each measure record.
- [TimestreamTimestamp](https://docs.aws.amazon.com/iot/latest/apireference/API_TimestreamTimestamp.html): Describes how to interpret an application-defined timestamp value from an MQTT message payload and the precision of that value.
- [TlsConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_TlsConfig.html): An object that specifies the TLS configuration for a domain.
- [TlsContext](https://docs.aws.amazon.com/iot/latest/apireference/API_TlsContext.html): Specifies the TLS context to use for the test authorizer request.
- [TopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRule.html): Describes a rule.
- [TopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRuleDestination.html): A topic rule destination.
- [TopicRuleDestinationConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRuleDestinationConfiguration.html): Configuration of the topic rule destination.
- [TopicRuleDestinationSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRuleDestinationSummary.html): Information about the topic rule destination.
- [TopicRuleListItem](https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRuleListItem.html): Describes a rule.
- [TopicRulePayload](https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRulePayload.html): Describes a rule.
- [TransferData](https://docs.aws.amazon.com/iot/latest/apireference/API_TransferData.html): Data used to transfer a certificate to an AWS account.
- [UpdateCACertificateParams](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCACertificateParams.html): Parameters to define a mitigation action that changes the state of the CA certificate to inactive.
- [UpdateDeviceCertificateParams](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDeviceCertificateParams.html): Parameters to define a mitigation action that changes the state of the device certificate to inactive.
- [UserProperty](https://docs.aws.amazon.com/iot/latest/apireference/API_UserProperty.html): A key-value pair that you define in the header.
- [ValidationError](https://docs.aws.amazon.com/iot/latest/apireference/API_ValidationError.html): Information about an error found in a behavior specification.
- [VersionUpdateByJobsConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_VersionUpdateByJobsConfig.html): Configuration to manage IoT Job's package version reporting.
- [ViolationEvent](https://docs.aws.amazon.com/iot/latest/apireference/API_ViolationEvent.html): Information about a Device Defender security profile behavior violation.
- [ViolationEventAdditionalInfo](https://docs.aws.amazon.com/iot/latest/apireference/API_ViolationEventAdditionalInfo.html): The details of a violation event.
- [ViolationEventOccurrenceRange](https://docs.aws.amazon.com/iot/latest/apireference/API_ViolationEventOccurrenceRange.html): Specifies the time period of which violation events occurred between.
- [VpcDestinationConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_VpcDestinationConfiguration.html): The configuration information for a virtual private cloud (VPC) destination.
- [VpcDestinationProperties](https://docs.aws.amazon.com/iot/latest/apireference/API_VpcDestinationProperties.html): The properties of a virtual private cloud (VPC) destination.
- [VpcDestinationSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_VpcDestinationSummary.html): The summary of a virtual private cloud (VPC) destination.

## [AWS IoT data](https://docs.aws.amazon.com/iot/latest/apireference/Welcome_AWS_IoT_Data_Plane.html)

AWS IoT data enables secure, bi-directional communication between Internet-connected things (such as sensors, actuators, embedded devices, or smart appliances) and the AWS cloud. It implements a broker for applications and things to publish messages over HTTP (Publish) and retrieve, update, and delete shadows. A shadow is a persistent representation of your things and their state in the AWS cloud.

Find the endpoint address for actions in AWS IoT data by running this CLI command:

`aws iot describe-endpoint --endpoint-type iot:Data-ATS`

The service name used by [AWSSignature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html)to sign requests is: iotdevicegateway.

### Actions

- [DeleteConnection](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_DeleteConnection.html): Disconnects a connected MQTT client from AWS IoT Core.
- [DeleteThingShadow](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_DeleteThingShadow.html): Deletes the shadow for the specified thing.
- [GetRetainedMessage](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetRetainedMessage.html): Gets the details of a single retained message for the specified topic.
- [GetThingShadow](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetThingShadow.html): Gets the shadow for the specified thing.
- [ListNamedShadowsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListNamedShadowsForThing.html): Lists the shadows for the specified thing.
- [ListRetainedMessages](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListRetainedMessages.html): Lists summary information about the retained messages stored for the account.
- [Publish](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_Publish.html): Publishes an MQTT message.
- [UpdateThingShadow](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_UpdateThingShadow.html): Updates the shadow for the specified thing.

### Data Types

- [RetainedMessageSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_RetainedMessageSummary.html): Information about a single retained message.

## [AWS IoT jobs data](https://docs.aws.amazon.com/iot/latest/apireference/Welcome_AWS_IoT_Jobs_Data_Plane.html)

AWS IoT Jobs is a service that allows you to define a set of jobs â remote operations that are sent to and executed on one or more devices connected to AWS IoT Core. For example, you can define a job that instructs a set of devices to download and install application or firmware updates, reboot, rotate certificates, or perform remote troubleshooting operations.

Find the endpoint address for actions in the AWS IoT jobs data plane by running this CLI command:

`aws iot describe-endpoint --endpoint-type iot:Jobs`

The service name used by [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html)to sign requests is: iot-jobs-data.

To create a job, you make a job document which is a description of the remote operations to be performed, and you specify a list of targets that should perform the operations. The targets can be individual things, thing groups or both.

AWS IoT Jobs sends a message to inform the targets that a job is available. The target starts the execution of the job by downloading the job document, performing the operations it specifies, and reporting its progress to AWS IoT Core. The Jobs service provides commands to track the progress of a job on a specific target and for all the targets of the job

### Actions

- [DescribeJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_DescribeJobExecution.html): Gets details of a job execution.
- [GetPendingJobExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_GetPendingJobExecutions.html): Gets the list of all jobs for a thing that are not in a terminal status.
- [StartCommandExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_StartCommandExecution.html): Using the command created with the CreateCommand API, start a command execution on a specific device.
- [StartNextPendingJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_StartNextPendingJobExecution.html): Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution for a thing.
- [UpdateJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_UpdateJobExecution.html): Updates the status of a job execution.

### Data Types

- [CommandParameterValue](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_CommandParameterValue.html): The list of values used to describe a specific command parameter.
- [JobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_JobExecution.html): Contains data about a job execution.
- [JobExecutionState](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_JobExecutionState.html): Contains data about the state of a job execution.
- [JobExecutionSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_JobExecutionSummary.html): Contains a subset of information about a job execution.

## [AWS IoT Core Device Advisor](https://docs.aws.amazon.com/iot/latest/apireference/Welcome_AWS_IoT_Core_Device_Advisor.html)

AWS IoT Core Device Advisor is a cloud-based, fully managed test capability for validating IoT devices during device software development. Device Advisor provides pre-built tests that you can use to validate IoT devices for reliable and secure connectivity with AWS IoT Core before deploying devices to production. By using Device Advisor, you can confirm that your devices can connect to AWS IoT Core, follow security best practices and, if applicable, receive software updates from IoT Device Management. You can also download signed qualification reports to submit to the AWS Partner Network to get your device qualified for the AWS Partner Device Catalog without the need to send your device in and wait for it to be tested.

### Actions

- [CreateSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_CreateSuiteDefinition.html): Creates a Device Advisor test suite.
- [DeleteSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeleteSuiteDefinition.html): Deletes a Device Advisor test suite.
- [GetEndpoint](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetEndpoint.html): Gets information about an Device Advisor endpoint.
- [GetSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteDefinition.html): Gets information about a Device Advisor test suite.
- [GetSuiteRun](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteRun.html): Gets information about a Device Advisor test suite run.
- [GetSuiteRunReport](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteRunReport.html): Gets a report download link for a successful Device Advisor qualifying test suite run.
- [ListSuiteDefinitions](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteDefinitions.html): Lists the Device Advisor test suites you have created.
- [ListSuiteRuns](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteRuns.html): Lists runs of the specified Device Advisor test suite.
- [ListTagsForResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListTagsForResource.html): Lists the tags attached to an IoT Device Advisor resource.
- [StartSuiteRun](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_StartSuiteRun.html): Starts a Device Advisor test suite run.
- [StopSuiteRun](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_StopSuiteRun.html): Stops a Device Advisor test suite run that is currently running.
- [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TagResource.html): Adds to and modifies existing tags of an IoT Device Advisor resource.
- [UntagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_UntagResource.html): Removes tags from an IoT Device Advisor resource.
- [UpdateSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_UpdateSuiteDefinition.html): Updates a Device Advisor test suite.

### Data Types

- [DeviceUnderTest](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeviceUnderTest.html): Information of a test device.
- [GroupResult](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GroupResult.html): Show Group Result.
- [SuiteDefinitionConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteDefinitionConfiguration.html): Gets the suite definition configuration.
- [SuiteDefinitionInformation](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteDefinitionInformation.html): Information about the suite definition.
- [SuiteRunConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteRunConfiguration.html): Gets suite run configuration.
- [SuiteRunInformation](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteRunInformation.html): Information about the suite run.
- [TestCaseRun](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TestCaseRun.html): Provides the test case run.
- [TestCaseScenario](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TestCaseScenario.html): Provides test case scenario.
- [TestResult](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TestResult.html): Show each group result.

## [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/apireference/Welcome_AWS_IoT_Secure_Tunneling.html)

AWS IoT Secure Tunneling creates remote connections to devices deployed in the field.

For more information about how AWS IoT Secure Tunneling works, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html).

### Actions

- [CloseTunnel](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_CloseTunnel.html): Closes a tunnel identified by the unique tunnel id.
- [DescribeTunnel](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_DescribeTunnel.html): Gets information about a tunnel identified by the unique tunnel id.
- [ListTagsForResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_ListTagsForResource.html): Lists the tags for the specified resource.
- [ListTunnels](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_ListTunnels.html): List all tunnels for an AWS account.
- [OpenTunnel](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_OpenTunnel.html): Creates a new tunnel, and returns two client access tokens for clients to use to connect to the AWS IoT Secure Tunneling proxy server.
- [RotateTunnelAccessToken](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_RotateTunnelAccessToken.html): Revokes the current client access token (CAT) and returns new CAT for clients to use when reconnecting to secure tunneling to access the same tunnel.
- [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_TagResource.html): A resource tag.
- [UntagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_UntagResource.html): Removes a tag from a resource.

### Data Types

- [ConnectionState](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_ConnectionState.html): The state of a connection.
- [DestinationConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_DestinationConfig.html): The destination configuration.
- [Tag](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_Tag.html): An arbitary key/value pair used to add searchable metadata to secure tunnel resources.
- [TimeoutConfig](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_TimeoutConfig.html): Tunnel timeout configuration.
- [Tunnel](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_Tunnel.html): A connection between a source computer and a destination device.
- [TunnelSummary](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_TunnelSummary.html): Information about the tunnel.

## Common

- [Common Parameters](https://docs.aws.amazon.com/iot/latest/apireference/CommonParameters.html)