# Source: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/llms.txt

# AMS Advanced Onboarding Guide AMS Advanced Account Onboarding Information

> Describes the AMS onboarding process and decisions you need to make, for multi-account landing zone and single-account landing zone.

- [Appendix: ActiveDirectory Federation Services (ADFS) claim rule and SAML settings](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/apx-adfs-claim-rule-saml.html)
- [Document history](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/doc-history.html)

## [AWS Managed Services Onboarding Introduction](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-intro.html)

- [Key terms](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/key-terms.html): Describes AMS key terms.

### [AMS modes](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes-og.html)

AWS Managed Services modes.

- [AMS modes and applications or workloads](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes-and-apps-og.html): Selecting the appropriate mode for your application or workload.
- [AMS post-account prescriptive guidance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-ob-prescriptive-guidance.html): AMS onboarding prescriptive guidance.
- [What we do, what we do not do](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-do-not-do.html): AMS gives you a standardized approach to deploying AWS infrastructure and provides the necessary ongoing operational management, and there are some things that we do not do.
- [AMS egress traffic management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/egress-traffic-mgmt.html): AMS egress traffic management.
- [IAM user role](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/defaults-user-role.html): Learn about IAM user roles in AMS.
- [Default Access Firewall Rules](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/firewall-default-access-rules.html): These are the default firewall rules required to access your instances.


## [Service management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/service-management.html)

- [Account governance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/apx-gov.html): Describes account governance in AWS Managed Services.
- [Service commencement](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/srv-mgmt-srv-commence.html): Describes service commencement in AWS Managed Services.
- [Customer relationship management (CRM)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/apx-crm.html): The purpose of AMS's customer relationship management (CRM) process is to ensure that a well-defined relationship is established and maintained with you.
- [Cost optimization](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/cost-optimization.html): Describs cost optimization for your AMS Advanced accounts.
- [Service hours](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/apx-gov-hours.html): Describes AMS contact hours
- [Getting help](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/faq-get-help.html): Describes how to get help in AWS Managed Services.


## [Change management modes](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/using-change-management.html)

### [Modes overview](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes-ug.html)

AWS Managed Services modes overview.

- [Types of modes and accounts in AMS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes-types.html): Different types of AMS modes.
- [AMS modes and applications or workloads](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes-and-apps-ug.html): Selecting the appropriate mode for your application or workload.
- [Real world use cases for AMS modes](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes-use-cases.html): Use cases for AMS modes.

### [RFC mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/rfc-mode.html)

AMS RFC mode.

### [Learn about RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-works.html)

In AWS Managed Services (AMS) requests for change, or RFCs, work in a two-fold manner: you configure the request and the parameters for the request.

- [What are RFCs?](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/what-r-rfcs.html): To order a new request for change (RFC) you first create it, and then submit it, using either the AMS console or the API commands CreateRfc and SubmitRfc.
- [Authenticate when using the AMS API/CLI](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-authentication.html): When using the AMS API/CLI you must authenticate with temporary credentials.
- [RFC security reviews](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/rfc-security.html): How RFC security works.
- [RFC change type classifications](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-csio.html): The change types that you use when submitting an RFC are divided into two broad classifications: Deployment for creating resources and Management for updating or deleting resources.

### [RFC action and activity states](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-action-state.html)

RfcActionState (API) / Activity State (console) help you understand the status of human intervention, or action, on an RFC.

- [RFC action states use case examples](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-action-state-examples.html): Examples of RFC action states.
- [RFC status codes](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-status-codes.html): RFC status codes help you track your requests.
- [RFC update CTs and CloudFormation template drift detection](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-updates-and-dd.html): Resources provisioned in AMS use a modified CloudFormation template.
- [Schedule RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-scheduling.html): Describes how to schedule an RFC or choose to have it run as soon as possible.
- [Approve or reject RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-approvals.html): RFCs submitted with approval-required (manual) CTs must be approved by you or by AMS.
- [Request RFC restricted run periods](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-restrict-execute.html): Formerly known as "blackout days", you can request that certain time periods be restricted so that no changes can be run whatsoever.

### [Create, clone, update, find, and cancel RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-use-examples.html)

These examples walk you through various RFC operations.

- [Create an RFC](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-create-col.html): The generic steps for how to create an RFC using the AMS console or the AMS API/CLI.
- [Clone RFCs (re-create) with the AMS console](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-clone-rfcs.html): You can use the AMS console to clone an existing RFC.
- [Update RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-update-rfcs.html): You can resubmit an RFC that has been rejected or that has not yet been submitted, by updating the RFC and then submitting it, or re-submitting it.
- [Find RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-find-col.html): Find an RFC using the AMS console or the AMS API/CLI.
- [Cancel RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-cancel-rfcs.html): You can cancel an RFC using the Console or the AMS API/CLI.

### [Use the AMS console with RFCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-gui.html)

Use the AMS console with RFCs

- [Configure RFC email notifications (console)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-email-notices.html): The AMS console Requests for Change create page provides you with an option to add email addresses to receive notifications of RFC state changes:
- [Common RFC parameters](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/rfc-common-params.html): RFC common parameters.
- [Sign up for the RFC daily email](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/rfc-digest.html): RFC digest allows you to sign up for a daily email summarizing all the active and recently completed RFCs in your account.

### [What are change types?](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/understanding-cts.html)

Change type refers to the action that an RFC performs and encompasses the change action itself, and the type of change â manual vs automated.

- [Automated and manual CTs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ug-automated-or-manual.html): A constraint on change types is whether they are automated or manual.
- [CT approval requirements](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/constrained-unconstrained-ctis.html): Change type approval requirements
- [Change type versions](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-versions.html): After selecting a change type using the AMS console, you have the option of opening the Additional configuration area and selecting a change type version.
- [Create change types](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-creates.html): Create change types are matched version-to-version with the Update change types.
- [Update change types](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-updates.html): Update change types are restricted in their usage to match version-to-version with the Create change type originally used to provision the resource.
- [Internal-only change types](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-internals.html): You can see change types that are for internal use only.
- [Change type schemas](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-schemas.html): All change types provide a JSON schema for your input in the creation, modification, or access, of resources.
- [Managing permissions for change types](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-permissions.html): You can use a custom policy to restrict which change types (CTs) are available to different groups or users.
- [Redacting sensitive information from change types](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-redaction.html): AMS change type schemas offer a parameter attribute, "metadata":"ams:sensitive":"true" that is used for parameters that would contain sensitive information, such as a password.
- [Finding a change type, using the query option](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ug-find-ct-ex-section.html): This example demonstrates how to use the AMS API/CLI to find the appropriate Change Type for the RFC that you want to submit.
- [Troubleshooting RFC errors](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/rfc-troubleshoot.html): Learn how to troubleshoot RFC errors in AMS Advanced.

### [Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/direct-change-mode-section.html)

Using AMS Direct Change mode.

- [Getting Started with Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/dcm-get-started.html): Getting Started with Direct Change mode.
- [Security and compliance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/dcm-security-n-compliance.html): Security and compliance in Direct Change mode.
- [Change management in Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/dcm-change-mgmt.html): Change management in Direct Change mode.
- [Creating stacks using Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/dcm-creating-stacks.html): Creating stacks using Direct Change mode
- [Direct Change Mode use cases](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/dcm-use-cases.html): Direct Change Mode use cases

### [Developer mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-section.html)

Describes AWS Managed Services Developer mode.

### [Getting started with Developer mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-implement.html)

Describes getting started with AMS Advanced Developer mode..

- [Before you begin](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-faqs.html): Describs some AMS Advanced Developer mode implementation tips.
- [Security and compliance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-security-and-compliance.html): Learn how security and compliance work in AMS Advanced Developer mode.
- [Change management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-change-management.html): Learn about change management in AMS Advanced Developer mode.
- [Provisioning infrastructure](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-provisioning.html): Learn about provisioning infrastructure in AMS Developer mode.
- [Detective controls](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-detective-controls.html): Learn about detective controls in AMS Developer mode.
- [Logging, monitoring, and event management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-logging.html): Learn about logging, monitoring, and event management in AMS Developer mode.
- [Incident management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-incident-management.html): Learn about incident management in AMS Developer mode.
- [Patch management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-patch-management.html): Learn about patch management in AMS Developer mode.
- [Continuity management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-continuity.html): Learn about continuity management in AMS Developer mode.
- [Security and access management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/developer-mode-security-and-access.html): Learn about security and access management in AMS Developer mode.

### [Self-Service Provisioning mode in AMS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/self-service-provisioning-section.html)

Describes the AMS Self-Service Provisioning mode.

- [Getting started with SSP mode in AMS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ssp-mode-get-start.html): Describes how to get started with SSP mode in AMS.
- [Amazon API Gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/api-gateway.html): Describes Amazon API Gateway in AMS.
- [Alexa for Business](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/aws-alexa-bus.html): Describes Alexa for Business in AMS.
- [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-app-stream-2.0.html): Describes Amazon WorkSpaces Applications (WorkSpaces Applications) in AMS.
- [Amazon Athena](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/athena.html): Describes Amazon Athena in AMS.
- [Amazon Bedrock](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/bedrock.html): Describes Amazon Bedrock in AMS.
- [Amazon CloudSearch](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/cloud-search.html): Describes Amazon CloudSearch in AMS.
- [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/cloud-synth.html): Describes Amazon CloudWatch Synthetics in AMS.
- [Amazon Cognito](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/cognito-pool.html): Describes Amazon Cognito user pools in AMS.
- [Amazon Comprehend](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/comprehend.html): Describes Amazon Comprehend in AMS.
- [Amazon Connect](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/connect.html): Describes Amazon Connect in AMS.
- [Amazon Data Firehose](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/kdf.html): Describes Amazon Data Firehose (KDF) in AMS.
- [Amazon DevOpsÂ Guru](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/devops-guru.html): Describes Amazon DevOpsÂ Guru in AMS.
- [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/document-db.html): Describes Amazon DocumentDB (with MongoDB compatibility) in AMS.
- [Amazon DynamoDB](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/dynamo-db.html): Describes Amazon DynamoDB in AMS.
- [Amazon Elastic Container Registry](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ecr.html): Describes Amazon Elastic Container Registry in AMS.
- [EC2 Image Builder](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ec2-image-build.html): Describes EC2 Image Builder in AMS.
- [Amazon ECS on AWS Fargate](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-ecs-fargate.html): Describes AWS Fargate in AMS.
- [Amazon EKS on AWS Fargate](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-eks.html): Describes AWS Fargate in AMS.
- [Amazon EMR](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-emr.html): Describes Amazon EMR in AMS.
- [Amazon EventBridge](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-eventbridge.html): Describes Amazon EventBridge in AMS.
- [Amazon Forecast](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/forecast.html): Describes Amazon Forecast in AMS.
- [Amazon FSx](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-fsx.html): Describes Amazon FSx in AMS.
- [Amazon FSx for OpenZFS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-fsx-open-zfs.html): Describes Amazon FSx for OpenZFS in AMS.
- [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-fsx-netapp-ontap.html): Describes Amazon FSx in AMS.
- [Amazon Inspector Classic](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/inspector.html): Describes Amazon Inspector Classic in AMS.
- [Amazon Kendra](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/kendra.html): Describes Amazon Kendra in AMS.
- [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/kds.html): Describes Amazon Kinesis Data Streams in AMS.
- [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/kvs.html): Describes Amazon Kinesis Video Streams (KVS) in AMS.
- [Amazon Lex](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-lex.html): Describes Amazon Lex in AMS.
- [Amazon MQ](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/mq-comp.html): Describes Amazon MQ in AMS.
- [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/kda.html): Describes Managed Service for Apache Flink (KDA) Amazon Managed Service for Apache Flink in AMS.
- [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/msk.html): Describes Amazon MSK in AMS.
- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/pro.html): Describes Amazon Managed Service for Prometheus (AMP) in AMS.
- [Amazon Personalize](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/personalize.html): Describes Amazon Personalize in AMS.
- [Amazon Quick](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/quicksight.html): Describes Quick in AMS.
- [Amazon Rekognition](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/rekognition.html): Describes Amazon Rekognition in AMS.
- [Amazon SageMaker AI](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/sagemaker.html): Describes SageMaker AI in AMS.
- [Amazon Simple Email Service](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-ses.html): Describes Amazon Simple Email Service (Amazon SES) in AMS.
- [Amazon Simple Workflow Service](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/workflow.html): Describes Amazon Simple Workflow Service (Amazon SWF) in AMS.
- [Amazon Textract](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/textract.html): Describes Amazon Textract in AMS.
- [Amazon Transcribe](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/transcribe.html): Describes Amazon Transcribe in AMS.
- [Amazon WorkSpaces](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/workspaces.html): Describes WorkSpaces in AMS.
- [AMS Code services](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/code-services.html): Describes AMS Code services in AMS.
- [AWS Amplify](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amplify.html): Describes AWS Amplify in AMS.
- [AWS AppSync](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/app-sync.html): Describes AWS AppSync in AMS.
- [AWS App Mesh](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/app-mesh.html): Describes AWS App Mesh in AMS.
- [AWS Audit Manager](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/audit-mgr.html): Describes Audit Manager in AMS.
- [AWS Batch](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/batch.html): Describes AWS Batch in AMS.
- [AWS Certificate Manager](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/acm.html): Describes AWS Certificate Manager in AMS.
- [AWS Private Certificate Authority](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/acm-priv-ca.html): Describes AWS Private CA in AMS.
- [AWS CloudEndure](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/cloud-endure.html): Describes AWS CloudEndure in AMS.
- [AWS CloudHSM](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/cloud-hsm.html): Describes AWS CloudHSM in AMS.
- [AWS CodeBuild](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/code-build.html): Describes AWS CodeBuild in AMS.
- [AWS CodeCommit](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/codecommit.html): Describes AWS CodeCommit in AMS.
- [AWS CodeDeploy](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/code-deploy.html): Describes AWS CodeDeploy in AMS.
- [AWS CodePipeline](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/code-pipeline.html): Describes AWS CodePipeline in AMS.
- [AWS Compute Optimizer](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/compute-optimizer.html): Describes AWS Compute Optimizer in AMS.
- [AWS DataSync](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/data-sync.html): Describes AWS DataSync in AMS.
- [AWS Device Farm](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/device-farm.html): Learn about the AMS SSPS AWS Device Farm.
- [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/elastic-disaster-recovery.html): Learn about the AMS SSPS AWS Elastic Disaster Recovery.
- [AWS Elemental MediaConvert](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-elemental-media-convert.html): Describes AWS Elemental MediaConvert in AMS.
- [AWS Elemental MediaLive](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/elemental-media-live.html): Describes AWS Elemental MediaLive in AMS.
- [AWS Elemental MediaPackage](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-elemental-media-package.html): Describes AWS Elemental MediaPackage in AMS.
- [AWS Elemental MediaStore](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/elemental-media-store.html): Describes AWS Elemental MediaStore in AMS.
- [AWS Elemental MediaTailor](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/amz-elemental-media-tailor.html): Describes AWS Elemental MediaTailor in AMS.
- [AWS Global Accelerator](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/global-acc.html): Describes Global Accelerator in AMS.
- [AWS Glue](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/glue.html): Describes AWS Glue in AMS.
- [AWS Lake Formation](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/lake-formation.html): Describes AWS Lake Formation in AMS.
- [AWS Lambda](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/lambda.html): Describes AWS Lambda in AMS.
- [AWS License Manager](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/license-manager.html): Describes AWS License Manager in AMS.
- [AWS Migration Hub](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/migration-hub.html): Describes AWS Migration Hub in AMS.
- [AWS Outposts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/outposts.html): Describes AWS Outposts in AMS.
- [AWS Resilience Hub](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/res-hub.html): Describes AWS Resilience Hub in AMS.
- [AWS Secrets Manager](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/secrets-manager.html): Describes AWS Secrets Manager in AMS.
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/sec-hub.html): Describes AWS Security Hub CSPM in AMS.
- [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/service-catalog-appregistry.html): Describes AWS Service Catalog AppRegistry in AMS.
- [AWS Shield](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/aws-shield.html): Describes AWS Shield Advanced in AMS.
- [AWS Snowball Edge](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/snowball.html): Describes Snowball Edge in AMS.
- [AWS Step Functions](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/step.html): Describes AWS Step Functions in AMS.
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/sys-man-param-store.html): Describes AWS Systems Manager Parameter Store in AMS.
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/sys-man-runbook.html): Describes AWS Systems Manager automation runbook in AMS.
- [AWS Transfer Family](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/transfer-sftp.html): Describes AWS Transfer Family (Transfer Family) in AMS.
- [AWS Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/transit-gateway.html): Describes AWS Transit Gateway in AMS.
- [AWS WAF](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-waf.html): Describes AWS WAF in AMS.
- [AWS Well-Architected Tool](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/well-arch.html): Describes AWS Well-Architected Tool in AMS.
- [AWS X-Ray](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/comp-xray.html): Describes AWS X-Ray (X-Ray) in AMS.
- [VM Import/Export](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/vm-im-ex.html): Describes VM Import/Export in AMS.

### [Customer Managed mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes-customer-section.html)

AMS Customer Managed mode description.

- [Getting started with Customer Managed mode](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/cust-man-mode-get-start.html): Describes how to get started with AMS Customer Managed mode.

### [AMS and AWS Service Catalog](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-service-catalog-section.html)

Describes how you can use Service Catalog in AWS Managed Services.

- [Getting started with Service Catalog](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/serv-cat-get-start.html): Describes how to get started with AWS Service Catalog in AMS.
- [Service Catalog in AMS before you begin](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-service-catalog-section-faq.html): In accounts where Service Catalog is enabled, it will act as the change management system in which you provision and update IT services in your AMS account through your predefined product catalog; AMS will provide a default portfolio/product catalog, and your IT admins can create and configure your own.


## [AMS Multi-account landing zone (MALZ) onboarding](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-intro-malz.html)

### [MALZ network architecture](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-net-arch-section.html)

AMS multi-account landing zone architecture.

### [Choosing single MALZ or multiple MALZs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-single-or-multi.html)

Single multi-account landing zone vs. multiple multi-account landing zones considerations.

- [Single multi-account landing zone vs. Multiple multi-account landing zone FAQs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/single-or-multi-malz-faq.html): Some commonly asked questions when choosing to set up a single multi-account landing zone or multiple multi-account landing zones.

### [Multi-Account Landing Zone accounts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-net-arch-accounts.html)

Multi-account landing zone accounts.

- [Management account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/management-account.html): The management account is your initial AWS account when you begin onboarding with AMS.

### [Networking account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-account.html)

The Networking account serves as the central hub for network routing.

### [Networking account architecture](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-network-arch.html)

The following diagram depicts the AMS multi-account landing zone environment, showcasing network traffic flows across account, and is an example of a highly-available setup.

### [Private network connectivity to AMS Multi-account landing zone environment](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-net-arch-private-net.html)

AWS offers private connectivity via either virtual private network (VPN) connectivity, or dedicated lines with AWS Direct Connect.

- [Centralized edge connectivity using transit gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-net-arch-cent-edge.html): AWS Transit Gateway is a service that enables you to connect your VPCs and your on-premises networks to a single gateway.
- [Connecting DX or VPN to account VPCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-net-arch-dx-vpn.html): With this option, the VPCs in your AMS multi-account landing zone environments are directly connected to Direct Connect or VPN.

### [Resources in the networking account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-account-resources.html)

Resources in the networking account.

- [AWS Network Manager](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-manager.html): AWS Network Manager.
- [Egress VPC](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-vpc.html): Insert abstract here.
- [Managed Palo Alto egress firewall](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-palo-alto.html): AMS provides a Managed Palo Alto egress firewall solution.
- [Perimeter (DMZ) VPC](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-dmz.html): Perimeter (DMZ) VPC.
- [AWS Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-transit-gateway.html): AWS Transit Gateway (TGW) is a service that enables you to connect your Amazon Virtual Private Clouds (VPCs) and your on-premises networks to a single gateway.

### [Shared Services account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/shared-services-account.html)

The Shared Services account serves as the central hub for most AMS data plane services.

- [Updates to shared services: Multi-Account Landing Zone](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-dp-release-process.html): AMS applies data plane releases to managed accounts on a monthly basis, without prior notice.
- [Log Archive account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/logging-account.html): The Log Archive account serves as the central hub for archiving logs across your AMS multi-account landing zone environment.
- [Security account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/security-account.html): The Security account is the central hub for housing security related operations.

### [Application account types](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/application-account.html)

AMS offers three types of Application accounts with different operational models, responsibilities and features.

- [AMS-managed application accounts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/application-account-ams-managed.html): Application accounts that are fully managed by AMS are referred to as AMS-managed application accounts, where all operational tasks are performed by AMS.
- [AMS Accelerate accounts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-accelerate-account.html): You can have AMS Accelerate enabled in a multi-account landing zone AMS Advanced account.

### [Customer Managed application accounts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/application-account-cust-man.html)

You can create accounts that AMS doesn't manage in the standard way.

- [Accessing your Customer Managed account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/application-account-cust-man-access.html): After you provision a Customer Managed account in multi-account landing zone is in the account for you to assume to configure the account.
- [Connecting your CMA with Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/application-account-cust-man-connect-tg.html): AMS does not manage the network setup of Customer Managed accounts.
- [Getting operational help with your Customer Managed accounts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/application-account-cust-man-op-help.html): Getting operational help with your Customer Managed accounts.

### [Tools account (migrating workloads)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/tools-account.html)

Learn about migrating workloads in AMS with a Tools account.

- [AWS Application Migration Service (AWS MGN)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/tools-account-mgn.html): Learn about the AWS Application Migration Service and AMS
- [Enable access to the new Tools account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/tools-account-enable.html): Describes how to enable access to the new AMS Tools account.
- [Example IAM CloudEndure policy](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/tools-account-ex-policy.html): See an AMS pre-approved IAM CloudEndure policy.
- [Testing connectivity and end-to-end setup](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/tools-account-test.html): Describes how to test the AMS Tools account connectivity and end-to-end setup.
- [Tools account hygiene](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/tools-account-hygiene.html): Learn about AMS Tools account hygiene.
- [Migration at scale - Migration Factory](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/migration-factory.html): Learn about AWS Migration at scale - Migration Factory

### [MALZ: Core account onboarding](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-acc.html)

Core account onboarding.

- [Create an AWS multi-account landing zone core account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-acc-create-account.html): Describes how to create an AWS core account in AMS.

### [Create an IAM role for AMS to access your account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/create-iam-role-for-ams.html)

Describes how to create an IAM role for AMS to access your account.

- [Activate IAM access to the AWS console](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/activate-iam-access-to-console.html): Describes how to activate IAM access to the AWS console.
- [Create an IAM Role for AMS to use](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/create-an-iam-role-for-ams-to-use.html): Describes how to create an IAM Role for AMS to use.
- [Secure the new account with multi-factor authentication (MFA) for the root user](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/mfa-root-user.html): Describes how to secure the new account with multi-factor authentication (MFA) for the root user in AMS.
- [Subscribe to AWS Marketplace for EPS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-subscribe-eps.html): Describes how to subscribe to AWS Marketplace for Trend Micro Endpoint Protection (EPS).

### [Set up networking](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net.html)

Set up core account networking.

- [Allocating IP space for your AMS environment](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-ip-space.html): You should have already worked with your Cloud Architect in defining the IP space for your AMS environment while filling out the onboarding questionnaire.

### [Establishing private network connectivity to AWS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-private.html)

Describes how to establish private network connectivity to AWS.

### [Centralized edge connectivity using Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-tg.html)

AWS Transit Gateway is a service that enables you to connect your Amazon Virtual Private Clouds (VPCs) and your on-premises networks to a single gateway.

- [Connecting Direct Connect to Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-to-tg.html): You can use your existing Direct Connect connection or create a new Direct Connect connection in one of your existing AWS accounts.
- [Connecting VPN to Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-vpn-to-tg.html): To attach a VPN connection to your transit gateway, you must specify the customer gateway.

### [Connecting Direct Connect and/or VPN to account VPCs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-dx-vpn.html)

You can also directly connect your VPCs to Direct Connect or VPN.

- [Direct Connect setup](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-dc.html): Describes Direct Connect setup in AMS.
- [VPN setup](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-vpn.html): The basic steps for setting up a VPN to communicate between your AMS-managed VPC and your internal network.

### [Set up access management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-access-mgmt.html)

Set up access management.

### [Establish an Active Directory Trust](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-access-mgmt-ad-trust.html)

To set up a trust, AMS requires your domain controller Local Policies -> Security Options -> Network Access: Named Pipes that can be accessed anonymously, have the Netlogon and lsarpc pipes listed.

- [Configure the Conditional Forwarder](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-access-mgmt-con-for.html): In the AD DNS Manager -> Create a New Conditional Forwarder, under DNS Domain: Use the domain name AMS supplied to you; for example, A523434123.amazonaws.com (change this to the domain name selected in the onboarding questionnaire.
- [Configure the AD trust](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-access-mgmt-con-trust.html): Configure the AD trust
- [Active Directory sites and services](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-ad-sites.html): To reduce login latency, add the VPC CIDR range to your Active Directory sites and services.
- [Active Directory name suffix routing](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-ad-routing.html): Active Directory name suffix routing

### [Federate your Active Directory with the AMS IAM roles](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate.html)

Federate your Active Directory with the AMS IAM roles.

- [Federation process example](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-ex.html): Federation process example.
- [Configuring federation to the AMS console (MALZ)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-console.html): Configuring Federation to the AMS console.
- [Verify console access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ma-verify-console-access.html): Verify console access.
- [Verify API access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ma-verify-api-access.html): Verify API access.

### [MALZ: Application account onboarding](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/app-acc.html)

You must have a multi-account AWS Managed Services (AMS) environment set up with core accounts, before requesting a new application account.

- [Requesting a new application account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/request-new-app-acc.html): Requesting a new application account.

### [Setting up Active Directory to federate access to AMS IAM roles](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-ad-to-federate-iam-roles.html)

Setting up Active Directory to federate access to AMS IAM roles.

- [Federation process example](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-example.html): This example uses Active Directory Federation Services (ADFS).

### [Configuring federation to the AMS console](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-example-ams-console.html)

The IAM roles and SAML identity provider (Trusted Entity) detailed in the following table are provisioned in your new application account.

- [Submitting the federation request to AMS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-example-ams-console-submit.html): Submitting the federation request to AMS.
- [Verify Console Access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-example-verify-console.html): After you are set up with AD FS, and have the AMS URL to use for authentication, you can perform the following procedure.
- [Verify API Access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-example-verify-api.html): AMS uses the AWS API, with some AMS-specific operations that you can read about in the AMS API Reference.

### [Setting up networking with the new Application account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-net-app-acc.html)

Setting up networking with the new Application account.

### [Setting up your firewall](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/net-app-acc-firewall.html)

To use the applications deployed in your AMS environment, you must create some firewall rules.

- [Firewall Rules for Application Access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/net-app-acc-firewall-rules.html): You must open the following ports for traffic through your firewall:
- [Setting up additional transit gateway application route tables](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-transit-gateway.html): Setting up additional transit gateway application route tables.
- [Setting up additional VPCs in the Application account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-additional-vpcs.html): Setting up additional VPCs in the Application account.

### [Appendix: multi-account landing zone (MALZ) onboarding consideration list](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/apx-malz-questions.html)

Describes AMS multi-account landing zone deployment elements and structure.

- [Account configuration](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-questions-account.html): Describes AMS multi-account landing zone account configuration set up considerations.
- [AMS multi-account landing zone monitoring alerts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-ma-monitoring-alerts.html): Describes AMS multi-account landing zone monitoring alerts set up considerations.
- [Network configuration](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-questions-network.html): Describes multi-account landing zone network configuration set up considerations.
- [Active Directory configuration](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-questions-ad.html): Describes AMS Active Directory set up considerations.
- [Trend Micro Endpoint Protection (EPS)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-questions-eps.html): Describes AMS Trend Micro EPS set up considerations.
- [Access: Bastions, SSH and RDP](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-questions-bastion.html): Describes AMS access set up considerations.
- [Federation](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/core-questions-federation.html): Describes AMS federation set up considerations.


## [AMS Single-account landing zone (SALZ) onboarding](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-intro-salz.html)

### [SALZ network architecture](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/salz-net-arch-section.html)

AMS single-account landing zone network architecture.

- [AMS Single-account landing zone shared services](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/salz-shared-services.html): Shared services subnets contain AMS Directory Services, the Management Host that automates provisioning and common tasks, antivirus (TrendMicro) management server, and internal bastion hosts:

### [SALZ: Create a new AWS account for AMS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-new-account.html)

Describes creating a new single-account landing zone AWS account for AMS.

- [Create an AWS account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/create-account.html): Describes creating an AWS account for AMS
- [Set up consolidated billingâlink new account to Payer account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-consolidated-billing.html): Link your new AWS account to an existing Payer account.

### [Configure your AWS account for AMS access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/configure-aws-account-for-sent.html)

Describes how to configure your AWS account for AMS access.

- [Activate access to the AWS website](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/activate-access-to-aws-web.html): Describes how to activate access to the AWS website.
- [Create an IAM role with access to the AWS website](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/create-iam-role.html): Describes how to create an IAM role with access to the AWS website.

### [Subscribe to AWS Marketplace for EPS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/subscribe-to-marketplace-for-eps.html)

Describes how to subscribe to AWS Marketplace for EPS.

- [Enable IDS and IPS in Trend Micro Deep Security](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-enable-IPSIDS.html): You can request that AMS enable Trend Micro Intrusion Detection System (IDS) and Intrusion Protection Systems (IPS) non-default features for your account.
- [Subscribe to AWS Marketplace for CentOS 7.6](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/centOS-subscribe.html): Describes how to ssubscribe to AWS Marketplace for CentOS 7.6.
- [Secure the new account with multi-factor authentication (MFA) for the root user](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/sog-secure-new-account-with-mfa.html): Describes where to learn how to secure the new account with multi-factor authentication (MFA) for the root user in AMS

### [SALZ: Set up networking](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-set-networking.html)

There are several processes that need to be completed to set up networking for AWS Managed Services (AMS):

- [Allocate IP Space for your AMS Environment](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/allocate-ip-space.html): AMS was designed and tested using a /16 CIDR block as the recommended network allocation.

### [Establish Private Network Connectivity to AWS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/establish-private-net-connect.html)

Add AMS to your corporate Active Directory to establish connectivity.

- [VPN Setup](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/vpn-setup.html): This section describes the basic steps for setting up a VPN to communicate between your AMS-managed VPC and your internal network.
- [Direct Connect Setup](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/direct-connect.html): This section describes the basic steps for setting up a Direct Connect (DX) to communicate between your AMS-managed VPC and your internal network.
- [Set up your Firewall](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-firewall.html): These firewall rules allow safe access to your network.
- [AMS Bastion Options during Application Migrations/Onboarding](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/bastion-options.html): In order to provide you with the best experience during migration efforts, below are the potential options AMS could currently leverage:

### [SALZ: Set up access management](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-set-access-mgmt.html)

Set up single-account landing zone access management.

### [Establish an Active Directory (AD) trust](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/establish-ad-trust.html)

Establish an Active Directory (AD) trust.

- [Configure the conditional forwarder](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/configure-conditional-forwarder.html): Configure the conditional forwarder.
- [Configure the trust](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/configure-trust.html): Configure the trust.
- [Active Directory sites and services](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ad-sites-and-services.html): Active Directory sites and services.
- [Active Directory name suffix routing](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ad-dir-config.html): After the one-way forest trust has been established, please complete the additional steps.
- [Troubleshooting](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/troubleshooting.html): Some things to try if you run into trouble.
- [AMS Managed Active Directory](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-managed-AD.html): Describes AMS Managed Active Directory (aka Managed AD).

### [Federate your Active Directory with the AMS AWS Identity and Access Management roles](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/federate-dir-with-sent-iam-roles.html)

The purpose of federating your directory with the AMS IAM roles is to enable corporate users to use their corporate credentials to interact with the AWS Management Console and the AWS APIs, and therefore the AMS console and APIs.

- [Federation process example](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-process-ex.html): This example uses Active Directory Federation Services (AD FS); however, any technology that supports AWS IAM Federation is supported.

### [Configuring federation to the AMS console (SALZ)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-with-console.html)

The IAM roles and SAML identity provider (Trusted Entity) detailed in the following table have been provisioned as part of your account onboarding.

- [Submitting the federation request to AMS](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-with-console-submit.html): Submitting the federation request to AMS.
- [Verify console access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/verify-console-access.html): Verify console access.

### [Verify API access](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/verify-api-access.html)

AMS uses the AWS API, with some AMS-specific operations that you can read about in the AMS API Reference.

- [Install the AMS CLIs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/install-cli.html): Install the AMS CLIs.
- [Scheduling AMS backups at the VPC level](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/schedule-backups.html): Scheduling AMS backups at the VPC level.

### [SALZ: Default settings](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-understand-defaults.html)

Your AWS Managed Services (AMS) network is configured in a standardized manner with defaults for most services.

- [Endpoint Security (EPS)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/eps-defaults.html): Resources that you provision in your AMS Advanced environment automatically include the installation of an EPS monitoring client.
- [Security groups](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/about-security-groups.html): In AWS Virtual Private Clouds (VPCs), AWS Security Groups act as virtual firewalls, controlling the traffic for one or more stacks (an instance or a set of instances).
- [EC2 IAM instance profile](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/defaults-instance-profile.html): An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts.
- [Monitored metrics defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/monitoring-default-metrics.html): The following table shows what is monitored and the default alerting thresholds.
- [Log retention and rotation defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/log-defaults.html): This section describes AMS log management defaults.

### [Continuity management defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/backup-defaults.html)

This section describes AMS continuity management defaults; for more information on AMS backups, see the AMS User Guide Continuity Management chapter.

- [VPC tag and defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/vpc-tag-and-defaults.html): Insert abstract text.
- [EC2 instance tag and defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ec2-instance-tag-and-defaults.html): The EC2 stack backup tag specifies whether the stack requires a snapshot of the attached EBS volumes or not.
- [RDS instance backup and defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/rds-instance-backup-defaults.html): The Amazon Relational Database Service (RDS) default values are defined in the stack templates:
- [Patching defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/patching-defaults.html): This section describes AMS patching defaults; for more information on AMS patching, see the AMS User Guide Patch Management chapter.

### [Validate the AMS service (SALZ)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-validate-service.html)

To validate that the AWS Managed Services (AMS) service is working as expected, some exercise that you can do are described in this chapter.

### [Find account settings](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/find-your-settings.html)

Learn how to find your AMS account settings.

- [Find FQDNs](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/find-FQDN.html): Learn how to find your FQDN in AWS Managed Services.
- [Find availability zones (AZs)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/find-AZs.html): Learn how to find your availability zones (AZs) in AWS Managed Services.
- [Find SNS topics](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/find-SNS-settings.html): Learn how to find your SNS topics in AWS Managed Services.
- [Find backup settings](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/find-backup-settings.html): Learn how to find your backup settings in AWS Managed Services.
- [Finding an instance ID or IP address](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/find-instance-id.html): You need an instance IP address to log into the instance.
- [EC2 instances: Creating](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-create-ec2.html): You can use the AMS console or API/CLI to create an Amazon EC2 and an Amazon EC2 with additional volumes.
- [Access, requesting](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-access-request.html): Insert abstract text
- [Other | Other RFC, creating (CLI)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-other-other.html): Insert abstract text
- [Any stack: deleting, rebooting, starting, stopping](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-delete-reboot-start-stop-stack.html): You can use the AMS console or API/CLI to delete, reboot, start, or stop, an AMS stack.

### [Access examples](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/access-examples.html)

These examples show how to log in to an instance via a bastion once you have been granted access through an RFC.

- [Linux computer to Linux instance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/linux-to-linux.html): Use SSH to connect to the SSH bastion and then to the Linux instance.
- [Linux computer to Windows instance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/linux-to-windows.html): Use an SSH tunnel and an RDP client to connect to a Windows instance from your Linux computer.
- [Windows computer to Windows instance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/windows-to-windows.html): Use Windows Remote Desktop Connection client to connect to a Windows instance from your Windows computer.
- [Windows computer to Linux instance](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/windows-to-linux.html): To RDP to an SSH bastion from a Windows environment, follow these steps.
- [Reporting an incident](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-ex-report-incident.html): Insert abstract text
- [Creating a service request](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/serv-req-mgmt-examples.html): For billing-related queries, use the Other Category in the AMS console; the ChangeTypeId ct-1e1xtak34nx76 in the AMS CM API, or the IssueType=AMS in the AWS Support API.
- [Post-onboarding steps](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-next-steps.html): Now that you've on boarded an AMS account, you'll want to read more AMS documentation.

### [Tutorials](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/change-mgmt-tutorials.html)

The following tutorials detail the steps to creating a two-tier stack with the High Availability (advanced) CT (ct-06mjngx5flwto), using the CLI and using the Console.

### [CLI Tutorial: High Availability Two-Tier Stack (Linux/RHEL)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/tut-create-ha-stack.html)

This section describes how to deploy a high availability (HA) two-tier stack into an AMS environment using the AMS CLI.

- [Before You Begin](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ha-stack-ex-before-begin.html): The Deployment | Advanced Stack Components | High Availability Two Tier Stack Advanced | Create CT creates an Auto Scaling group, a load balancer, a database, and a CodeDeploy application name and deployment group (with the same name that you give the application).
- [Create the Infrastructure](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-create-ha-infra-deploy.html): Gathering the following data before you begin will make the deployment go more quickly.
- [Create, Upload, and Deploy the Application](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-create-app.html): First, create a WordPress application bundle, and then use the CodeDeploy CTs to create and deploy the application.
- [Validate the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-validate-app-deploy.html): Navigate to the endpoint (ELB CName) of the previously-created load balancer, with the WordPress deployed path: /WordPress.
- [Tear Down the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-tear-down-app-deploy.html): Once you are finished with the tutorial, you will want to tear down the deployment so you are not charged for the resources.

### [Console Tutorial: High Availability Two Tier Stack (Linux/RHEL)](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-ex-create-ha-stack.html)

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS console.

- [Before You Begin](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-ha-stack-ex-before-begin.html): The Deployment | Advanced Stack Components | High Availability Two Tier Stack | Create CT creates an Auto Scaling group, a load balancer, a database, and a CodeDeploy application name and deployment group (with the same name that you give the application).
- [Create the Infrastructure](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-ex-create-ha-rfc.html): This procedure utilizes the High availability two-tier stack CT followed by the Create S3 storage CT.
- [Create, Upload, and Deploy the Application](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-ex-create-app.html): First, create a WordPress application bundle, and then use the CodeDeploy CTs to create and deploy the application.
- [Validate the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-ex-validate-app-deploy.html): Navigate to the endpoint (LoadBalancerCName) of the previously-created load balancer, with the WordPress deployed path: /WordPress.
- [Tear Down the High Availability Deployment](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/gui-ex-delete-ha-deploy.html): To tear down the deployment, you submit the Delete Stack CT against the HA Two-Tier stack, and the S3 bucket, and you can request that RDS snapshots be deleted.

### [Appendix: SALZ onboarding questionnaire](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/apx-og-questions.html)

This section describes some of the information that you will need to think about before onboarding an account.

- [Deployment summary](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/deployment-summary.html): Learn about the AMS deployment summary.
- [Environment architecture considerations](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-questions-environment-level.html): Describes AMS environment and architecture considerations.
- [Single-Account Landing Zone Monitoring Alerts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-monitoring-alerts.html): AMS provides a way for you to be directly alerted (versus getting AMS service notifications) for certain monitoring alerts.
- [Maintenance Window](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-maintenance-window.html): Learn AMS considerations when creating a maintenance window.
- [Next Steps](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-get-started-next-steps.html): Learn AMS onboarding next steps.
