# Source: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/llms.txt

# Amazon SageMaker Unified Studio Administrator Guide

- [What is Amazon SageMaker Unified Studio?](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/what-is-sagemaker-unified-studio.html)
- [Terminology and concepts](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/concepts.html)
- [Prerequisites](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/prerequisites.html)
- [Setting up](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setting-up.html)
- [Supported Regions](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/supported-regions.html)
- [User management](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/user-management.html)
- [Associated accounts](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/associated-accounts.html)
- [Onboarding data](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/data-onboarding.html)
- [Git connections](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/git-connections.html)
- [Amazon Q](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/amazonq.html)
- [Amazon Bedrock in SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/amazon-bedrock.html)
- [Amazon Quicksight in SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/amazon-quicksight.html)
- [Quotas and limits](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/doc-history.html)

## [Domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/working-with-domains.html)

### [Identity Center-based domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/identity-center-based-domains.html)

Create and manage domains that use AWS IAM Identity Center for authentication.

- [Create a Amazon SageMaker Unified Studio domain - quick setup](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/create-domain-sagemaker-unified-studio-quick.html): Complete the following procedure to create an Amazon SageMaker unified domain with the Quick setup option.
- [Create a Amazon SageMaker Unified Studio domain - manual setup](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/create-domain-sagemaker-unified-studio-manual.html): Complete the following procedure to create a Amazon SageMaker Unified Studio domain with the quick setup option.
- [Create an Amazon DataZone domain](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/create-domain-datazone.html): Complete the following procedure to create a Amazon SageMaker Unified Studio domain with the quick setup option.
- [Edit domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/edit-domain.html): After you create a domain, you can edit its description or further customize your domain settings, including SSO, project profiles, blueprints, account associations, Amazon Bedrock models, connections, and AmazonQ.
- [Delete domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/delete-domain.html): When deleting a domain, note that the act of deleting a domain is final.
- [Upgrade Amazon DataZone domains to Amazon SageMaker unified domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/upgrade-domain.html)
- [Trusted identity propagation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/trusted-identity-propagation.html): Trusted identity propagation in IAM Identity Center enables administrators of AWS services to grant permissions based on user attributes, such as user ID or group associations.

### [IAM-based domains and projects](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/iam-based-domains.html)

Create and manage domains that use AWS Identity and Access Management (IAM) roles for authentication and access control.

- [Overview of IAM-based domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/iam-based-domains-overview.html): IAM-based domains provide the following capabilities:
- [Set up IAM-based domains in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setup-iam-based-domains.html): Setting up an IAM-based domain in Amazon SageMaker Unified Studio requires an IAM roles used for domain administration tasks.
- [Manage data encryption in IAM-based domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/manage-data-encryption-iam-based-domains.html): Data encryption in IAM-based domains protects your data at rest and in transit within Amazon SageMaker Unified Studio.
- [Access the Domain Administration Page](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/access-domain-administration-page.html): The domain administration page in Amazon SageMaker Unified Studio provides administrators with centralized management capabilities for domains, projects, and settings.

### [Configure VPC Networking for Amazon SageMaker Unified Studio Domain](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/vpc-networking-iam-based-domains.html)

- [Network settings in IAM-based domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configure-vpc-networking-iam-based-domains.html): Amazon Virtual Private Cloud (Amazon VPC) networking with subnets is required when using certain compute services within Amazon SageMaker Unified Studio.
- [Update Individual Projects with VPC Configuration](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/update-individual-projects-vpc.html): When you configure VPC networking for your domain with the "Update projects separately" option, existing projects are not automatically updated with the VPC configuration.
- [View VPC Networking Details for Your Domain](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/view-vpc-networking-details.html): After configuring VPC networking for your Amazon SageMaker Unified Studio domain, you can view the VPC and subnet details from the domain settings.
- [Manage Projects from Domain Administration](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/manage-projects-domain-administration.html): The Projects section in domain administration provides centralized management of all projects within your Amazon SageMaker Unified Studio domain.
- [Configure Domain Settings](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configure-domain-settings-iam-based.html): The Settings section in domain administration provides access to domain-level configuration options that apply across all projects in your Amazon SageMaker Unified Studio domain.

### [Projects in IAM-based domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/projects-iam-based-domains.html)

Create and manage projects within IAM-based domains using IAM roles for authentication and access control.

- [Set up projects within an IAM-based domain](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setup-projects-iam-based-domains.html): To create a project within an IAM-based domain you assign Member IAM role or user and Execution IAM role, configure execution permissions for the execution role, and set up storage options.
- [View and Manage Project Details](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/view-manage-project-details-iam-based.html): The project details page provides domain administrators with comprehensive information about project configuration, members, and networking settings.
- [Edit Project Configuration](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/edit-project-configuration-iam-based.html): Domain administrators can modify project settings including the project description and member IAM roles.
- [Share Project Information](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/share-project-information-iam-based.html): The share project information feature generates a welcome message that domain administrators can send to project members.
- [Delete a Project](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/delete-project-iam-based.html): Domain administrators can permanently delete projects from the domain administration page.


## [Domain units and authorization policies](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/domain-units.html)

- [Create domain units](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/create-domain-unit.html): In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Edit domain units](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/edit-domain-unit.html): In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Delete domain units](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/delete-domain-unit.html): In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Manage domain unit owners](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/add-domain-unit-owners.html): In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Assign authorization policies to users and groups within a domain unit](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/assign-authorization-policies-to-users-in-domain-unit.html): In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Assign authorization policies to projects within a domain unit](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/assign-authorization-policies-to-projects-in-domain-unit.html): In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Assign authorization policies to asset types](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/assign-authorization-policies-to-asset-types.html): In Amazon SageMaker Unified Studio, asset types define how assets are represented in the Amazon SageMaker catalog.


## [Local IDE Support](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/local-ide-support.html)

### [Configuring Amazon SageMaker Unified Studio for Remote Access](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-sagemaker-unified-studio-remote-access.html)

- [Network Configuration for Remote Access](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/network-config-remote-access.html)


## [Unified storage](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/smus-admin-storage-guide.html)

- [Configuring project storage options](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-project-storage.html)
- [Performance and cost optimization](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/performance-cost-optimization.html)
- [Feature comparison matrix](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/feature-comparison.html): The following table provides a comprehensive comparison of key features between Git-based and S3 storage options to help you make informed decisions when configuring storage for your Amazon SageMaker Unified Studio projects.


## [Project profiles](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/project-profiles.html)

- [All capabilities project profile](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/all-capabilities.html): The All capabilities project profile enables your Amazon SageMaker Unified Studio users to analyze data and build machine learning and generative AI models and applications powered by Amazon Bedrock, Amazon EMR, AWS Glue, Amazon Athena, Amazon SageMaker AI, and Amazon SageMaker Lakehouse.
- [Generative AI application development project profile](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/genai-application-development.html): A Generative AI application development project profile enables generative AI solutions from Amazon Bedrock for your Amazon SageMaker unified domains.
- [SQL analytics project profile](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sql-analytics.html): The SQL analytics project profiles enables your users to query Amazon SageMaker Lakehouse, Amazon Redshift and Amazon Athena data in their Amazon SageMaker Unified Studio projects.
- [Custom project profile](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/custom.html): Complete the following procedure to create a custom project profile for your Amazon SageMaker unified domain.
- [Update project profiles](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/update-project-profile.html): Complete the following procedure to update a project profile for your domain.
- [Disable or enable project profiles](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/disable-enable-project-profile.html): Complete the following procedure to disable or enable a project profile for your domain.
- [Delete project profiles](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/delete-project-profile.html): Complete the following procedure to delete a project profile for your domain.
- [Edit blueprint deployment settings](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/edit-blueprint-deployment-settings.html): Blueprint deployment settings contain parameters used to create project profiles for Amazon SageMaker Unified Studio projects.
- [Add blueprint deployment settings](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/add-blueprint-deployment-settings.html): Blueprint deployment settings contain parameters used to create project profiles for Amazon SageMaker Unified Studio projects.
- [Project resource tags](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/project-resource-tags.html): Learn about project resource tags in Amazon SageMaker Unified Studio.


## [Blueprints](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/blueprints.html)

- [Supported blueprints](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/supported-blueprints.html): In the current release of Amazon SageMaker Unified Studio, the following default blueprints are supported:
- [Custom blueprints](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/custom-blueprint.html): Custom blueprints in Amazon SageMaker Unified Studio enable organizations to standardize and accelerate how data projects get set up.
- [Enable or disable blueprints](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-disable-blueprints.html): You can complete the following procedure to enable or disable blueprints in the Amazon SageMaker management console:
- [Specify PEM certificate for EmrOnEc2 blueprint](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-emr-on-ec2-blueprint.html): In order to successfully enable the EmrOnEc2 blueprint, you must specify the location of your PEM certificate.

### [Getting started with Amazon EMR on EKS](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/getting-started-with-emr-on-eks.html)

Before you begin with Amazon EMR on EKS, you must have a compatible Amazon EKS cluster.

- [Enable Amazon EKS cluster access for Amazon EMR on EKS and Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-eks-cluster-access-for-emr-on-eks-and-sagemaker-unified-studio.html): Amazon EMR on EKS and Amazon SageMaker Unified Studio require access to the Kubernetes service running on the Amazon EKS cluster.
- [Enable cross-account access using associated domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-cross-account-access-using-associated-domains.html): Amazon EMR on EKS virtual clusters require an Amazon EKS cluster residing in the same account.
- [Enable cross-network access using VPC peering connections](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-cross-network-access-using-vpc-peering.html)
- [Configuring monitoring with Spark History Server](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-monitoring-with-spark-history-server-for-emr-on-eks.html): Amazon EMR on EKS requires additional IAM permissions to enable monitoring with Spark History Server.
- [Configuring fine-grained access controls](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-fine-grained-access-controls-for-emr-on-eks.html): Amazon EMR on EKS requires additional IAM permissions to enable fine-grained access controls.
- [Configuring trusted identity propagation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-trusted-identity-propagation-for-emr-on-eks.html): Amazon EMR on EKS requires additional IAM permissions to enable trusted identity propagation.
- [Configuring user background sessions](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-user-background-sessions-for-emr-on-eks.html)
- [Manage blueprint authorization](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/authorization-for-blueprints.html): You can perform the following procedure to manage the authorization configuration of a blueprint.
- [Enable Tooling blueprint](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-tooling-blueprint.html): The tooling blueprint creates resources for the project, including IAM user roles, security groups, and Amazon SageMaker unified domains.
- [Manage Tooling blueprint parameters](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/manage-tooling-blueprint.html): The tooling blueprint creates resources for the project, including IAM user roles, security groups, and Amazon SageMaker unified domains.
- [Modify the OnDemandWorkflows blueprint for creating workflow environments in a shared VPC](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/modify-on-demand-workflows-blueprint.html): In order to support creating workflow environments in a shared VPC setup, where the VPC is in one AWS account and the project and the Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environment are in another AWS account, the domain administrator must complete the following procedure to modify the endpointManagement parameter of the OnDemand Workflows blueprint.


## [Account pools](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools.html)

- [Considerations](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-considerations.html): The following considerations apply for account pools in Amazon SageMaker Unified Studio.
- [Use cases](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-usecases.html): Account pools allow administrators to perform the following tasks.

### [Create an account pool](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-create.html)

To use the AWS CLI to create an account pool, you run the create-account-pool command and provide the source.

- [Create an account pool with a custom handler source](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-create-handler.html): You can create an account pool where the account authentication is provided by a custom Lambda handler.
- [Create an account pool with a static list of account and region pairs](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-create-static.html): You can create an account pool where the accounts are provided as a list of static accounts.
- [View an account pool](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-view.html): To use the AWS CLI to view the accounts in an account pool, use the get-account-pool command.
- [List account pools for a domain](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-list.html): To use the AWS CLI to view the account pools in a domain, use the list-account-pools command.
- [View the list of accounts in an account pool](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-list-accounts.html): To use the AWS CLI to view the accounts in an account pool where the source is a list of static accounts, use the list-accounts-in-account-pool command.
- [Delete an account pool](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-delete.html): To use the AWS CLI to delete an account pool, use the delete-account-pool command.
- [Create a project profile with an account pool](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-create-profile.html): You can create a project profile that has your account pool associated such that you can choose accounts and regions from it when creating a project with the profile.


## [Security](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security.html)

### [Identity and access management](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam.html)

How to authenticate requests and manage access your Amazon SageMaker Unified Studio resources.

- [How Amazon SageMaker Unified Studio works with IAM](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon SageMaker Unified Studio, learn what IAM features are available to use with Amazon SageMaker Unified Studio.
- [Identity-based policy examples](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon SageMaker Unified Studio resources.

### [AWS managed policies](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol.html)

Learn about AWS managed policies for Amazon SageMaker Unified Studio and recent changes to those policies.

- [SageMakerStudioFullAccess](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioFullAccess.html): This policy provides full access to Amazon SageMaker Unified Studio via the Amazon SageMaker management console.
- [SageMakerStudioProjectUserRolePermissionsBoundary](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioProjectUserRolePermissionsBoundary.html): Amazon SageMaker Unified Studio creates IAM roles for Projects users to perform data analytics, artificial intelligence, and machine learning actions, and uses this policy when creating these roles to define the boundary of their permissions.
- [SageMakerStudioDomainExecutionRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.html): Default policy for the SageMakerUnifiedStudioDomainExecutionRole service role.
- [SageMakerStudioProjectUserRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.html): Amazon SageMaker Unified Studio creates IAM roles for projects users to perform data analytics, artificial intelligence, and machine learning actions, and uses this policy when creating these roles to define the permissions.
- [SageMakerStudioProjectRoleMachineLearningPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioProjectRoleMachineLearningPolicy.html): Amazon SageMaker Unified Studio creates IAM roles for projects users to perform data analytics, artificial intelligence, and machine learning actions, and uses this policy when creating these roles to define the permissions related to Amazon SageMaker.
- [SageMakerStudioDomainServiceRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioDomainServiceRolePolicy.html): This is the default policy for the SageMakerUnifiedStudioDomainServiceRole service role.
- [SageMakerStudioProjectProvisioningRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioProjectProvisioningRolePolicy.html): Amazon SageMaker Unified Studio uses this policy to provision and manage resources in your account.
- [AmazonDataZoneBedrockModelManagementPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-AmazonDataZoneBedrockModelManagementPolicy.html): Provides permissions to manage Amazon Bedrock model access, including creating, tagging and deleting application inference profiles.
- [SageMakerStudioQueryExecutionRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioQueryExecutionRolePolicy.html): This is the default policy for the SageMakerQueryExecutionRole role.
- [SageMakerStudioEMRServiceRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioEMRServiceRolePolicy.html): Amazon SageMaker Unified Studio creates IAM roles for project users to perform data analytics, artificial intelligence, and machine learning actions, and uses this policy when creating these roles to define the permissions related to EMR.
- [AmazonDataZoneBedrockModelConsumptionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-AmazonDataZoneBedrockModelConsumptionPolicy.html): Provides permissions to consume Amazon Bedrock models, including invoking Amazon Bedrock application inference profile created for particular Amazon DataZone domain.
- [SageMakerStudioEMRInstanceRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioEMRInstanceRolePolicy.html): Amazon SageMaker Unified Studio creates IAM roles for project users to perform data analytics, artificial intelligence, and machine learning actions and uses this policy when creating these roles to define the permissions related to EMR.
- [SageMakerStudioBedrockAgentServiceRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockAgentServiceRolePolicy.html): This policy allows Amazon Bedrock Agents to access Amazon Bedrock models and other resources attached to an agent in Amazon SageMaker Unified Studio.
- [SageMakerStudioBedrockChatAgentUserRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockChatAgentUserRolePolicy.html): This policy provides access to an Amazon Bedrock chat agent app's configuration and Amazon Bedrock agent in Amazon SageMaker Unified Studio.
- [SageMakerStudioBedrockPromptUserRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockPromptUserRolePolicy.html): This policy provides access to an Amazon Bedrock prompt and its configuration in Amazon SageMaker Unified Studio.
- [SageMakerStudioBedrockFlowServiceRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockFlowServiceRolePolicy.html): This policy allows Amazon Bedrock Flows to access Amazon Bedrock models and other resources attached to a flow in Amazon SageMaker Unified Studio.
- [SageMakerStudioBedrockEvaluationJobServiceRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockEvaluationJobServiceRolePolicy.html): This policy allows Amazon Bedrock to access Amazon Bedrock models and datasets for evaluation jobs in Amazon SageMaker Unified Studio.
- [SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy.html): This policy provides access to configure vector stores and Amazon Bedrock knowledge bases in Amazon SageMaker Unified Studio.
- [SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy.html): This policy allows Amazon Bedrock Knowledge Bases to access Amazon Bedrock models and data sources in Amazon SageMaker Unified Studio.
- [SageMakerStudioBedrockFunctionExecutionRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockFunctionExecutionRolePolicy.html): This policy allows AWS Lambda to access an Amazon Bedrock function component's configuration in Amazon SageMaker Unified Studio.
- [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html): This policy provides individual setup privileges for Amazon SageMaker Unified Studio using the AWS Management Console and SDK.
- [SageMakerStudioUserIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.html): This is the default execution policy for using IAM roles with Amazon SageMaker Unified Studio.
- [SageMakerStudioUserIAMPermissiveExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMPermissiveExecutionPolicy.html): This is an execution policy for using IAM roles with Amazon SageMaker Unified Studio.
- [SageMakerStudioAdminIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioAdminIAMConsolePolicy.html): This policy provides initial administrative and individual setup privileges for Amazon SageMaker Unified Studio via the AWS Management Console and SDK.
- [SageMakerStudioAdminIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioAdminIAMDefaultExecutionPolicy.html): This is the administrative execution policy for using IAM roles with Amazon SageMaker Unified Studio.
- [SageMakerStudioAdminIAMPermissiveExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioAdminIAMPermissiveExecutionPolicy.html): This is an administrative execution policy for using IAM roles with Amazon SageMaker Unified Studio.
- [SageMakerStudioAdminProjectUserRolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioAdminProjectUserRolePolicy.html): This IAM policy grants an IAM role full access to AWS Glue Data Catalog (metadata) and Amazon S3 (actual data) for data lake operations, with access scoped by account, and role tags.
- [Policy updates](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-updates.html)

### [IAM roles for Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-roles.html)

- [AmazonSageMakerDomainExecution role](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainExecution.html): The AmazonSageMakerDomainExecution role has the attached.
- [AmazonSageMakerDomainService role](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainService.html): The AmazonSageMakerDomainService role has the attached.
- [AmazonSageMakerManageAccess-<region>-<domainId> role](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerManageAccess.html): AmazonSageMakerManageAccess-<region>-<domainId> role grants Amazon SageMaker Unified Studio permissions to publish, grant access, and revoke access to Amazon SageMaker Lakehouse, AWS Glue Data Catalog and Amazon Redshift data.
- [AmazonSageMakerProvisioning-<domainAccountId> role](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerProvisioning.html): AmazonSageMakerProvisioning-<domainAccountId> role is used by Amazon SageMaker Unified Studio to provision and manage resources defined in the selected blueprints in your account.
- [AmazonDataZoneBedrockModelManagementRole](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonDataZoneBedrockModelManagementRole.html): Amazon SageMaker Unified Studio uses this role to create an inference profile for an Amazon Bedrock model in a project.
- [AmazonDataZoneBedrockFMConsumptionRole](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonDataZoneBedrockFMConsumptionRole.html): A consumption role is required for each Amazon Bedrock model that you want to enable in the playground for non-builders.
- [AmazonSageMakerQueryExecution](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerQueryExecution.html): This role is used while running a query execution.
- [Access control patterns Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-accesss-control-patterns.html): Effective data management and governance are crucial to deriving value from data assets while maintaining compliance and security.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon SageMaker Unified Studio and IAM.

### [Data protection](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon SageMaker Unified Studio.

- [KMS Permissions for resources provisioned by Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-provisioned-resources-key-permissions.html): You can encrypt the resources provisioned by Amazon SageMaker Unified Studio with your customer managed AWS KMS keys.
- [KMS permissions for exporting asset metadata in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.html)
- [Amazon Bedrock in SageMaker Unified Studio KMS Permissions](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/amazon-bedrock-key-permissions.html)
- [Authorization in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-authorization.html): Learn about Authorization in Amazon SageMaker Unified Studio
- [Compliance validation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Security Best Practices](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-best-practices.html): Amazon SageMaker Unified Studio provides a number of security features to consider as you develop and implement your own security policies.
- [Resilience](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon SageMaker Unified Studio features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/infrastructure-security.html): Learn how Amazon SageMaker Unified Studio isolates service traffic.
- [Network isolation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/network-isolation.html): Configure Amazon SageMaker Unified Studio to limit data access and reduce exposure over the public internet by using Amazon VPC interface endpoints.
- [Configuration and vulnerability analysis in for Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/vulnerability-analysis-and-management.html): Learn what configuration and vulnerability analysis is for Amazon SageMaker Unified Studio.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
