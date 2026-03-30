# Source: https://docs.aws.amazon.com/amplify/latest/APIReference/llms.txt

# Amplify Welcome

> Welcome to the AWS Amplify Hosting API documentation. This reference provides descriptions of the actions and data types for the Amplify Hosting API. If you are looking for the API documentation for the Amplify iOS, Amplify Android, and Amplify client libraries, see the open-source documentation for the Amplify Framework.

- [Welcome](https://docs.aws.amazon.com/amplify/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/amplify/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/amplify/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Operations.html)

- [CreateApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateApp.html): Creates a new Amplify app.
- [CreateBackendEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateBackendEnvironment.html): Creates a new backend environment for an Amplify app.
- [CreateBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateBranch.html): Creates a new branch for an Amplify app.
- [CreateDeployment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateDeployment.html): Creates a deployment for a manually deployed Amplify app.
- [CreateDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateDomainAssociation.html): Creates a new domain association for an Amplify app.
- [CreateWebhook](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateWebhook.html): Creates a new webhook on an Amplify app.
- [DeleteApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteApp.html): Deletes an existing Amplify app specified by an app ID.
- [DeleteBackendEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteBackendEnvironment.html): Deletes a backend environment for an Amplify app.
- [DeleteBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteBranch.html): Deletes a branch for an Amplify app.
- [DeleteDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteDomainAssociation.html): Deletes a domain association for an Amplify app.
- [DeleteJob](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteJob.html): Deletes a job for a branch of an Amplify app.
- [DeleteWebhook](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteWebhook.html): Deletes a webhook.
- [GenerateAccessLogs](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GenerateAccessLogs.html): Returns the website access logs for a specific time range using a presigned URL.
- [GetApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetApp.html): Returns an existing Amplify app specified by an app ID.
- [GetArtifactUrl](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetArtifactUrl.html): Returns the artifact info that corresponds to an artifact id.
- [GetBackendEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetBackendEnvironment.html): Returns a backend environment for an Amplify app.
- [GetBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetBranch.html): Returns a branch for an Amplify app.
- [GetDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetDomainAssociation.html): Returns the domain information for an Amplify app.
- [GetJob](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetJob.html): Returns a job for a branch of an Amplify app.
- [GetWebhook](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetWebhook.html): Returns the webhook information that corresponds to a specified webhook ID.
- [ListApps](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListApps.html): Returns a list of the existing Amplify apps.
- [ListArtifacts](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListArtifacts.html): Returns a list of end-to-end testing artifacts for a specified app, branch, and job.
- [ListBackendEnvironments](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListBackendEnvironments.html): Lists the backend environments for an Amplify app.
- [ListBranches](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListBranches.html): Lists the branches of an Amplify app.
- [ListDomainAssociations](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListDomainAssociations.html): Returns the domain associations for an Amplify app.
- [ListJobs](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListJobs.html): Lists the jobs for a branch of an Amplify app.
- [ListTagsForResource](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListTagsForResource.html): Returns a list of tags for a specified Amazon Resource Name (ARN).
- [ListWebhooks](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListWebhooks.html): Returns a list of webhooks for an Amplify app.
- [StartDeployment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_StartDeployment.html): Starts a deployment for a manually deployed app.
- [StartJob](https://docs.aws.amazon.com/amplify/latest/APIReference/API_StartJob.html): Starts a new job for a branch of an Amplify app.
- [StopJob](https://docs.aws.amazon.com/amplify/latest/APIReference/API_StopJob.html): Stops a job that is in progress for a branch of an Amplify app.
- [TagResource](https://docs.aws.amazon.com/amplify/latest/APIReference/API_TagResource.html): Tags the resource with a tag key and value.
- [UntagResource](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UntagResource.html): Untags a resource with a specified Amazon Resource Name (ARN).
- [UpdateApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateApp.html): Updates an existing Amplify app.
- [UpdateBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateBranch.html): Updates a branch for an Amplify app.
- [UpdateDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateDomainAssociation.html): Creates a new domain association for an Amplify app.
- [UpdateWebhook](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateWebhook.html): Updates a webhook.


## [Data Types](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Types.html)

- [App](https://docs.aws.amazon.com/amplify/latest/APIReference/API_App.html): Represents the different branches of a repository for building, deploying, and hosting an Amplify app.
- [Artifact](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Artifact.html): Describes an artifact.
- [AutoBranchCreationConfig](https://docs.aws.amazon.com/amplify/latest/APIReference/API_AutoBranchCreationConfig.html): Describes the automated branch creation configuration.
- [Backend](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Backend.html): Describes the backend associated with an Amplify Branch.
- [BackendEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_BackendEnvironment.html): Describes the backend environment associated with a Branch of a Gen 1 Amplify app.
- [Branch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Branch.html): The branch for an Amplify app, which maps to a third-party repository branch.
- [CacheConfig](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CacheConfig.html): Describes the cache configuration for an Amplify app.
- [Certificate](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Certificate.html): Describes the current SSL/TLS certificate that is in use for the domain.
- [CertificateSettings](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CertificateSettings.html): The type of SSL/TLS certificate to use for your custom domain.
- [CustomRule](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CustomRule.html): Describes a custom rewrite or redirect rule.
- [DomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DomainAssociation.html): Describes the association between a custom domain and an Amplify app.
- [Job](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Job.html): Describes an execution job for an Amplify app.
- [JobConfig](https://docs.aws.amazon.com/amplify/latest/APIReference/API_JobConfig.html): Describes the configuration details that apply to the jobs for an Amplify app.
- [JobSummary](https://docs.aws.amazon.com/amplify/latest/APIReference/API_JobSummary.html): Describes the summary for an execution job for an Amplify app.
- [ProductionBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ProductionBranch.html): Describes the information about a production branch for an Amplify app.
- [Step](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Step.html): Describes an execution step, for an execution job, for an Amplify app.
- [SubDomain](https://docs.aws.amazon.com/amplify/latest/APIReference/API_SubDomain.html): The subdomain for the domain association.
- [SubDomainSetting](https://docs.aws.amazon.com/amplify/latest/APIReference/API_SubDomainSetting.html): Describes the settings for the subdomain.
- [WafConfiguration](https://docs.aws.amazon.com/amplify/latest/APIReference/API_WafConfiguration.html): Describes the Firewall configuration for a hosted Amplify application.
- [Webhook](https://docs.aws.amazon.com/amplify/latest/APIReference/API_Webhook.html): Describes a webhook that connects repository events to an Amplify app.
