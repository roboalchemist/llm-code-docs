# Source: https://docs.aws.amazon.com/privateca/latest/userguide/llms.txt

# AWS Private Certificate Authority User Guide

> AWS Private CA handles the complexity of creating and managing private certificate authorities (CAs) that you can use to issue and revoke private certificates inside of your organization.

- [What is the best certificate service for my needs?](https://docs.aws.amazon.com/privateca/latest/userguide/service-options.html)
- [Best practices](https://docs.aws.amazon.com/privateca/latest/userguide/ca-best-practices.html)
- [Service quotas](https://docs.aws.amazon.com/privateca/latest/userguide/PcaLimits.html)
- [Document History](https://docs.aws.amazon.com/privateca/latest/userguide/dochistory.html)

## [What is AWS Private CA?](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)

- [Terms and concepts for AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaTerms.html): Learn terms and concepts related to certificates and certificate authorities.


## [Use AWS Private CA with the AWS SDK for Java](https://docs.aws.amazon.com/privateca/latest/userguide/PcaApiIntro.html)

### [API examples](https://docs.aws.amazon.com/privateca/latest/userguide/PcaApiIntroActions.html)

The following code examples show how to use select AWS Private CA API actions and data types with the AWS SDK for Java.

- [Create and activate a root CA programmatically](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ActivateRootCA.html): Learn how to activate a root CA using API calls in Java.
- [Create and activate a subordinate CA programmatically](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ActivateSubordinateCA.html): Learn how to activate a subordinate CA using API calls in Java.
- [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-CreatePrivateCertificateAuthority.html): Learn how to create a Java sample for the CreateCertificateAuthority operation.
- [Using CreateCertificateAuthority to support Active Directory](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-CreatePrivateCertificateAuthorityAD.html): Learn how to use Java to create a certificate authority suitable for Active Directory authentication.
- [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-CreateCertificateAuthorityAuditReport.html): Learn how to create a Java sample for the CreateCertificateAuthorityAuditReport operation.
- [CreatePermission](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-CreatePermission.html): Learn how to create a Java sample for the CreatePermission operation.
- [DeleteCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-DeleteCertificateAuthority.html): Learn how to create a Java sample for the DeleteCertificateAuthority operation.
- [DeletePermission](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-DeletePermission.html): Learn how to create a Java sample for the DeletePermission operation.
- [DeletePolicy](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-DeletePolicy.html): Learn how to create a Java sample for the DeletePolicy operation.
- [DescribeCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-DescribeCertificateAuthority.html): Learn how to create a Java sample for the DescribeCertificateAuthority operation.
- [DescribeCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-DescribeCertificateAuthorityAuditReport.html): Learn how to create a Java sample for the DescribeCertificateAuthorityAuditReport operation.
- [GetCertificate](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-GetCertificate.html): Learn how to create a Java sample for the GetCertificate operation.
- [GetCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-GetCACertificate.html): Learn how to create a Java sample for the GetCertificateAuthorityCertificate operation.
- [GetCertificateAuthorityCsr](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-GetCertificateAuthorityCsr.html): Learn how to create a Java sample for the GetCertificateAuthorityCsr operation.
- [GetPolicy](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-GetPolicy.html): Learn how to create a Java sample for the GetPolicy operation.
- [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ImportCertificateAuthorityCertificate.html): Learn how to create a Java sample for the ImportCertificateAuthorityCertificate operation.
- [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-IssueCertificate.html): Learn how to create a Java sample for the IssueCertificate operation.
- [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ListCertificateAuthorities.html): Learn how to create a Java sample for the ListCertificateAuthorities operation.
- [ListPermissions](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ListPermissions.html): Learn how to create a Java sample for the ListPermissions operation.
- [ListTags](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ListTags.html): Learn how to create a Java sample for the ListTags operation.
- [PutPolicy](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-PutPolicy.html): Learn how to create a Java sample for the PutPolicy operation.
- [RestoreCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-RestoreCertificateAuthority.html): Learn how to create a Java sample for the RestoreCertificateAuthority operation.
- [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-RevokeCertificate.html): Learn how to create a Java sample for the RevokeCertificate operation.
- [TagCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-TagPCA.html): Learn how to create a Java sample for the TagCertificateAuthorities operation.
- [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-UnTagPCA.html): Learn how to create a Java sample for the UntagCertificateAuthority operation.
- [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-UpdateCertificateAuthority.html): Learn how to create a Java sample for the UpdateCertificateAuthority operation.
- [Create CAs and certificates with custom subject names](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-CustomAttributes.html): Learn how to create certificates and CAs with custom attributes.
- [Create certificates with custom extensions](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-CustomExtensions.html): Learn how to create certificates with custom X.509 extensions.

### [Matter examples](https://docs.aws.amazon.com/privateca/latest/userguide/API-CBR-intro.html)

Java code samples showing how to use the AWS Private CA API.

- [Activate a Product Attestation Authority (PAA)](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiCBC-ProductAttestationAuthorityActivation.html): Learn how to create and install a Matter Root CA certificate for product attestation.
- [Activate an Product Attestation Intermediate (PAI)](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiCBC-ProductAttestationIntermediateActivation.html): Learn how to create and install a Matter Subordinate CA certificate for product attestation.
- [Create a Device Attestation Certificate (DAC)](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiCBC-DeviceAttestationCertificate.html): Learn how to create a Device Attestation Certificate (DAC) for Matter.
- [Activate a Root CA for Node Operational Certificates (NOC).](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiCBC-ActivateRootCA.html): Learn how to create and install a Root CA certificate used to issue NOCs.
- [Activate a Subordinate CA for Node Operational Certificates (NOC)](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiCBC-IntermediateCAActivation.html): Learn how to create and install a Subordinate CA certificate used to issue NOCs.
- [Create a Node Operational Certificate (NOC)](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiCBC-NodeOperatingCertificate.html): Learn how to issue a Node Operational Certificate (NOC) for Matter.

### [mDL examples](https://docs.aws.amazon.com/privateca/latest/userguide/MDL-intro.html)

Java code samples showing how to use the AWS Private CA API.

- [Activate an issuing authority certificate authority (IACA) certificate](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiMDL-ActivateIACA.html): Learn how to create and install a mobile driving license (mDL) issuing authority certificate authority (IACA) certificate.
- [Create a document signer certificate](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApiMDL-IssueDS.html): Learn how to issue an mDL document signer.


## [Architect your solution for AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaPlanning.html)

- [Design a CA hierarchy](https://docs.aws.amazon.com/privateca/latest/userguide/ca-hierarchy.html): Design a CA hierarchy suited to your organizational needs.
- [Manage the CA lifecycle](https://docs.aws.amazon.com/privateca/latest/userguide/ca-lifecycle.html): Set client-side trust, expiration, and succession of CA certificates.

### [Plan certificate revocation](https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html)

Optional mechanisms for revoking certificates and notifying users of the revocation.

- [Set up CRL](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html): Learn how to prepare an S3 bucket for your CRLs, apply security policies, and encrypt the CRLs for use with AWS Private Certificate Authority.
- [Customize OCSP URL](https://docs.aws.amazon.com/privateca/latest/userguide/ocsp-customize.html): How to implement a custom OCSP endpoint name for use with AWS Private Certificate Authority.
- [CA mode](https://docs.aws.amazon.com/privateca/latest/userguide/short-lived-certificates.html): Learn how short-lived certificates can be used instead of an explicit revocation mechanism.
- [Plan for resilience](https://docs.aws.amazon.com/privateca/latest/userguide/disaster-recovery-resilience.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Private Certificate Authority features for data resiliency.


## [Certificate authorities](https://docs.aws.amazon.com/privateca/latest/userguide/creating-managing.html)

- [Set up](https://docs.aws.amazon.com/privateca/latest/userguide/setup-aws.html): Learn how to set up for AWS Private Certificate Authority and plan your private CA deployment.
- [Create a private CA](https://docs.aws.amazon.com/privateca/latest/userguide/create-CA.html): Learn about ways to create a private CA in AWS Private Certificate Authority.
- [Install CA certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PCACertInstall.html): Learn how to obtain and install a certificate for your private CA.

### [Control access](https://docs.aws.amazon.com/privateca/latest/userguide/granting-ca-access.html)

Provide access to private CAs for users and roles in your AWS account in other AWS accounts.

- [Create single-account permissions for an IAM user](https://docs.aws.amazon.com/privateca/latest/userguide/assign-permissions.html): Assign permissions when the CA administrator and the certificate issuer reside in the same account.
- [Attach a policy for cross-account access](https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html): Assign permissions when the CA administrator and the certificate issuer reside in different accounts.
- [List private CAs](https://docs.aws.amazon.com/privateca/latest/userguide/list-CAs.html): Use the console or AWS CLI to list private CAs.
- [View a private CA](https://docs.aws.amazon.com/privateca/latest/userguide/describe-CA.html): Use the console or AWS CLI to view details about your private CAs.
- [Add tags](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCaTagging.html): Learn how to manage tags for your private CA in AWS Private Certificate Authority.
- [CA status](https://docs.aws.amazon.com/privateca/latest/userguide/PcaUpdateStatus.html): Learn about CA statuses in AWS Private Certificate Authority.
- [Update a CA](https://docs.aws.amazon.com/privateca/latest/userguide/PCAUpdateCA.html): Learn how to update your private CA in AWS Private Certificate Authority.
- [Delete a CA](https://docs.aws.amazon.com/privateca/latest/userguide/PCADeleteCA.html): Learn how to delete your private CA in AWS Private CA.
- [Restore a CA](https://docs.aws.amazon.com/privateca/latest/userguide/PCARestoreCA.html): Learn how to restore a private CA after deletion.
- [Externally signed CA certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaExternalRoot.html): Learn how to use an external CA (on-premises or third-party) to sign a subordinate CA certificate managed by AWS Private CA.


## [Issue and manage certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaUsing.html)

- [Issue private end-entity certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaIssueCert.html): Learn how to issue private certificates from AWS Private CA.
- [Retrieve a private certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PcaGetCert.html): How to retrieve locally created private certificates.
- [List private certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaListCerts.html): List your certificates using an audit report and a parser.
- [Export a certificate](https://docs.aws.amazon.com/privateca/latest/userguide/export-in-acm.html): Learn how to export a private certificate, along with its secret key, using AWS Certificate Manager.
- [Revoke a private certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PcaRevokeCert.html): Learn how to revoke private certificates from AWS Private CA.
- [Automate export](https://docs.aws.amazon.com/privateca/latest/userguide/auto-export.html): Learn how to export renewed private PKI certificates using the ACM API and AWS Lambda.

### [Certificate templates](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html)

Learn about templates for creating certificates.

- [Template varieties](https://docs.aws.amazon.com/privateca/latest/userguide/template-varieties.html): Learn about the types of templates that AWS Private Certificate Authority offers.
- [Template order of operations](https://docs.aws.amazon.com/privateca/latest/userguide/template-order-of-operations.html): Learn about the order of operations for AWS Private Certificate Authority templates.
- [Template definitions](https://docs.aws.amazon.com/privateca/latest/userguide/template-definitions.html): Learn about AWS Private Certificate Authority template definitions.


## [Security](https://docs.aws.amazon.com/privateca/latest/userguide/security.html)

### [IAM](https://docs.aws.amazon.com/privateca/latest/userguide/security-iam.html)

Learn how to configure authentication and access to your AWS Private CA solution using AWS tools.

- [API permissions](https://docs.aws.amazon.com/privateca/latest/userguide/api-permissions.html): Learn about permissions required to access the AWS Private CA API.
- [AWS managed policies](https://docs.aws.amazon.com/privateca/latest/userguide/auth-AwsManagedPolicies.html): Learn about built-in AWS permissions policies for AWS Private CA.
- [Customer managed policies](https://docs.aws.amazon.com/privateca/latest/userguide/auth-CustManagedPolicies.html): Control access to AWS Private Certificate Authority (AWS Private CA) resources in your AWS account by attaching customer managed policies to users, groups, or roles.
- [Inline policies](https://docs.aws.amazon.com/privateca/latest/userguide/auth-InlinePolicies.html): Control access to AWS Private Certificate Authority (AWS Private CA) resources in your AWS account by attaching inline policies to users, groups, or roles.

### [Cross-account access](https://docs.aws.amazon.com/privateca/latest/userguide/pca-resource-sharing.html)

Learn how to use AWS Private CA efficiently and securely across multiple AWS accounts.

- [Resource-based policies](https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html): Resource-based permissions policies for cross-account access.
- [Data protection](https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Private Certificate Authority.

### [Compliance validation](https://docs.aws.amazon.com/privateca/latest/userguide/security-compliance-validation.html)

Learn what AWS services are in scope of a specific compliance program.

- [Create an audit report](https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html): Learn how to create and use AWS Private CA audit reports.

### [Infrastructure security](https://docs.aws.amazon.com/privateca/latest/userguide/infrastructure-security.html)

Learn how AWS storage and network infrastructure protects the integrity of your data.

- [VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/privateca/latest/userguide/vpc-endpoints.html): Use a VPC endpoint to create a private connection between your VPC and AWS Private Certificate Authority without requiring access over the internet or through a NAT instance, a VPN connection, or Direct Connect.
- [Dual-stack endpoint support](https://docs.aws.amazon.com/privateca/latest/userguide/dual-stack-endpoint-support.html): AWS Private Certificate Authority provides a dual-stack public endpoint that supports both IPv4 and IPv6 clients.
- [Using IPv6 addresses in IAM and AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/using-ipv6-iam.html): Before trying to access AWS Private Certificate Authority over IPv6, ensure any IAM policies containing IP address restrictions are updated to include IPv6 address ranges.
- [CP/CPS](https://docs.aws.amazon.com/privateca/latest/userguide/pca-customer-cpcps.html): AWS Private Certificate Authority provides infrastructure services that enable you to create certificate authority (CA) hierarchies, including root and subordinate CAs, without the investment and maintenance costs of operating an on-premise CA.


## [Monitor resources](https://docs.aws.amazon.com/privateca/latest/userguide/logging-and-monitoring.html)

- [AWS Private CA CloudWatch metrics](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCloudWatch.html): Learn what CloudWatch metrics are supported in AWS Private CA.
- [Monitor AWS Private CA with CloudWatch Events](https://docs.aws.amazon.com/privateca/latest/userguide/CloudWatchEvents.html): Enhance AWS Private CA by using Amazon CloudWatch Events and Amazon EventBridge to trigger actions in response to certificate-related events.
- [CloudTrail logs](https://docs.aws.amazon.com/privateca/latest/userguide/logging-using-cloudtrail-pca.html): Learn about logging AWS Private Certificate Authority with AWS CloudTrail.


## [Troubleshoot](https://docs.aws.amazon.com/privateca/latest/userguide/PcaTsIntro.html)

- [Certificate revocation issues](https://docs.aws.amazon.com/privateca/latest/userguide/troubleshoot-certificate-revocation.html): Troubleshoot issues related to the revocation of certificates issued by AWS Private CA.
- [Exception messages](https://docs.aws.amazon.com/privateca/latest/userguide/PCATsExceptions.html): Learn how to interpret service exceptions.
- [Matter-compliant certificate errors](https://docs.aws.amazon.com/privateca/latest/userguide/TroubleshootPcaMatter.html): Solve problems encountered when issuing Matter-compliant certificates with the API.


## [Secure Kubernetes with AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes.html)

- [Concepts](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-concepts.html): Learn the concepts that you need to know to use the AWS Private CA Connector for Kubernetes.
- [Considerations](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-considerations.html): Learn about the considerations for using the AWS Private CA Connector for Kubernetes.
- [Get started](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-get-started.html): Learn how to use AWS Private Certificate Authority to secure communications with your Kubernetes clusters.
- [Examples](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-examples.html): Example configuration for Kubernetes clusters.
- [Monitor](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-monitor.html): Learn how to monitor the private CA used by the AWS Private CA Connector for Kubernetes.
- [Troubleshoot](https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-troubleshoot.html): Learn how to use kubectl to check the status of your private CA issuer and certificate.


## [Connector for Active Directory](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad.html)

- [Set up](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad-getting-started-prerequisites.html): The steps in this section are prerequisites to using Connector for AD.
- [Get started](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad-getting-started.html): Learn how to set up and use Connector for AD

### [Connectors for Active Directory](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad-procedures.html)

Learn how to provision Active Directory resources with private PKI certificates issued by AWS Private CA.

- [Create connector](https://docs.aws.amazon.com/privateca/latest/userguide/create-connector-for-ad.html): Learn how to create a connector for Active Directory.
- [Create template](https://docs.aws.amazon.com/privateca/latest/userguide/create-ad-template.html): Learn how to create templates for a connector template to use when issuing certificates.
- [Update template](https://docs.aws.amazon.com/privateca/latest/userguide/update-template-connector-for-ad.html): Learn how to update a Connector for Active Directory template.
- [List connectors](https://docs.aws.amazon.com/privateca/latest/userguide/list-connector-for-ads.html): Use the console or AWS CLI to list your AWS Private CA Connectors for Active Directory.
- [List templates](https://docs.aws.amazon.com/privateca/latest/userguide/list-ad-templates.html): Use the console or AWS CLI to list templates for your connector.
- [View connector](https://docs.aws.amazon.com/privateca/latest/userguide/view-connector-for-ad.html): Learn how to view the details of a connector.
- [View template](https://docs.aws.amazon.com/privateca/latest/userguide/view-ad-template.html): Learn how to view the details of a connector template.
- [Directory registrations](https://docs.aws.amazon.com/privateca/latest/userguide/directory-registration.html): Learn how to manage directory registrations.
- [Template access control entries](https://docs.aws.amazon.com/privateca/latest/userguide/ad-groups-permissions.html): Learn how to manage permissions on AD groups to enroll certificates using a template.
- [Service principal name](https://docs.aws.amazon.com/privateca/latest/userguide/ad-spn.html): Learn how to configure the service principal name for the connector.
- [Tags](https://docs.aws.amazon.com/privateca/latest/userguide/ad-tags.html): Learn how to apply metadata tags to your Connector for AD resources.
- [Integrating with EventBridge](https://docs.aws.amazon.com/privateca/latest/userguide/eventbridge-integration.html): Receive notifications when specific Connector for AD events such as certificate creation or retrieval occur in an Connector for AD with EventBridge.

### [Troubleshoot Connector for Active Directory](https://docs.aws.amazon.com/privateca/latest/userguide/troubleshoot-connector-ad.html)

Troubleshoot issues related to AWS Private CA Connector for Active Directory.

- [Connector for AD error codes](https://docs.aws.amazon.com/privateca/latest/userguide/c4adTroubleshootingError.html): Troubleshoot error codes from Connector for AD.
- [Connector creation failure](https://docs.aws.amazon.com/privateca/latest/userguide/c4adTroubleshootingConnectorCreationFailure.html): Troubleshoot issues that occur when you try to create a connector.
- [SPN creation failure](https://docs.aws.amazon.com/privateca/latest/userguide/c4adTroubleshootingSpnFailure.html): Troubleshoot Service principal name (SPN) creation failures
- [Template update issues](https://docs.aws.amazon.com/privateca/latest/userguide/c4adTroubleshootingUpdatedTemplate.html): Troubleshoot Connector for AD template update issues.


## [Connector for SCEP](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep.html)

- [Concepts](https://docs.aws.amazon.com/privateca/latest/userguide/c4scep-concepts.html): Connector for SCEP is an add-on feature for AWS Private Certificate Authority.
- [Considerations and limitations](https://docs.aws.amazon.com/privateca/latest/userguide/c4scep-considerations-limitations.html): Considerations and limitations when working with Connector for SCEP.
- [Set up](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep-setting-up.html): Set up a private CA, RAM-sharing permissions, and create an IAM policy to get started with Connector for SCEP.
- [Get started](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep-getting-started.html): Learn how to set up and use AWS Private Certificate Authority Connector for SCEP.

### [Configure your MDM system](https://docs.aws.amazon.com/privateca/latest/userguide/using-connector-for-scep-with-mdm.html)

Describes how Connector for SCEP works, and how to configure your mobile device management (MDM) systems to work with AWS Private Certificate Authority SCEP connectors.

- [Configure Jamf Pro](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep-general-purpose.html): Describes how to configure Jamf Pro for use with AWS Private Certificate Authority Connector for SCEP.
- [Configure Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep-intune.html): You can use AWS Private CA as an external certificate authority (CA) with the Microsoft Intune mobile device management (MDM) system.
- [Configure Omnissa Workspace ONE](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep-omnissa.html): You can use AWS Private CA as an external certificate authority (CA) with the Omnissa Workspace ONE UEM (Unified Endpoint Management) system.

### [Monitor](https://docs.aws.amazon.com/privateca/latest/userguide/c4scep-monitoring-overview.html)

Learn how to use AWS monitoring tools to debug the use and performance of AWS Private CA Connector for SCEP solution.

- [Automate using EventBridge](https://docs.aws.amazon.com/privateca/latest/userguide/c4scep-monitor-eventbridge-events.html): Enhance Connector for SCEP by using Amazon EventBridge to trigger actions in response to conector events.
- [CloudTrail logs](https://docs.aws.amazon.com/privateca/latest/userguide/logging-using-cloudtrail-c4scep.html): Learn about logging AWS Private Certificate Authority Connector for SCEP with AWS CloudTrail.

### [Troubleshoot](https://docs.aws.amazon.com/privateca/latest/userguide/troubleshoot-connector-scep.html)

Troubleshoot issues related to AWS Private Certificate Authority Connector for SCEP.

- [HTTP errors](https://docs.aws.amazon.com/privateca/latest/userguide/c4scep-troubleshoot-http-error.html): Troubleshoot standard HTTP errors in Connector for SCEP.
- [Client errors](https://docs.aws.amazon.com/privateca/latest/userguide/troubleshoot-connector-scep-client-errors.html): Troubleshoot Connector for SCEP client errors
