# Source: https://docs.envzero.com/guides/admin-guide/migration-strategy-guide/review-your-devops-process.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Assessing Your DevOps Process

> Evaluate your existing IaC provisioning and DevOps processes before migrating to env zero

## Intro

Evaluating your existing IaC provisioning process will help identify any pain points or areas for improvement. Consider factors such as collaboration, version control, infrastructure provisioning, and deployment. This analysis will help you identify key requirements for env zero, ensuring a better fit for your team's workflows and objectives.

## VCS

Depending on the company's security posture, the location of the code may be required to be within your (virtual) data center.  Others are happy with the level of security held in SaaS repositories.  The location of the code may push your solution one way or another.

### SaaS

env zero natively integrates with the most popular VCS (or SCM) providers; GitHub, GitLab, BitBucket, and AzureDevOps.  Our built-in CI/CD pipeline allows for Plan on PR (or merge requests if you're using GitLab), Continuous Deployment, and plans and applies from PRs using our PR comments feature.  All of these features are options as is the ability to primarily work from the VCS or UI.

If your favorite VCS isn't listed above don't worry, we regularly review which VCSs should be added to our platform.  In the meantime, we work with any VCS, with our "Other VCS" option.  The only drawback is the native CI/CD features within env zero won't work, but we can work with you to find the best way to trigger workflows.

### Self-Hosted

env zero also works with the self-hosted versions of the VCSs previously mentioned (except AzureDevOps).  In order, to connect to the self-hosted VCS providers, you will need to use the env zero self-hosted agent.

The decision to use the [env zero self-hosted agent](/guides/admin-guide/self-hosted-kubernetes-agent) does not only depend on the type of VCS you are using, it can be a preference for many reasons.  Perhaps your company has high-security requirements and you need all clones, runs, and logs within your (cloud) data center.  We can work with you to decide the best solution for your business.

## DevOps - Process

Depending on the DevOps maturity or preference, we see many of our customers fall into one of the scenarios discussed below.  It’s great to evaluate where you are and where you want to be… Where is your bottleneck? What are your pain points? Do you want self-service?

### Central team deploys the majority of IaC - aka Command & Control

Whether your team is deploying your IaC manually, or it is automated through some CI/CD tool, the DevOps team is the major actor in this setup. We’ve found that the majority of customers are in this bucket, not because they necessarily want to be, but that is simply the current state.  DevOps teams in this space typically are tasked through tickets, to create the infrastructure required by the application or teams they support.

* DevOps team provisions infrastructure through the TF code that they’ve written.
* DevOps responds to requests for infrastructure, and provision

### Self-Service w/ IaC

Either your application developers or your platform consumers know some IaC, and you’ve given them the ability to submit PRs to modify the infrastructure code.  You have a system that will create the IaC, through a PR process that creates the resources after the PR has been approved. You may have written a wrapper, to allow devs to “fill out a yaml/json form” to create the infra they require.

* Developers submit PR with TF code that they’ve modified or written
* PR approval ultimately results in the creation of resources
* **Status Quo or Your Preference**
  * Config as code
  * ALL infrastructure as code - even Developer Self-Service.
* **Pros**
  * Application teams take ownership of Infrastructure
  * PR Approval process creates a paper trail
* **Cons**
  * Some fundamental knowledge of IaC is still required or the wrapper code needs to be maintained and extended as use cases expand.
  * PR Approval Process is not always in line with the Infrastructure Approval Process.
  * Deleting or removing resources requires someone to submit another PR.

### Self-Service w/ UI

You know that not everyone can learn infrastructure code, nor do they really want to.  So you want a web UI, that will allow the engineers or developers to create new resources with some guardrails in place. The configuration is mostly configured in the UI, while you create a service catalog for your end-users to request or even create resources on-demand. Using IaC scanning tools and policy enforcement tools, you can create additional guardrails and approval policies while giving more engineers the ability to self-service.

* **You Prefer**
  * Users can request infrastructure through a UI
  * Guardrails like Security scans and Policy enforcement are in place
  * Approvals through UI
* **Pros**
  * No coding necessary
  * Unified view
* **Cons**
  * Click Ops
  * Configuration in UI

### Fully Distributed - Application Teams own the Infrastructure

It’s the wild-west, any team can choose whichever tools they desire, leading to different processes for different teams, and disparate tooling. There may be a lack of sharing across teams on how best to get into production, but that’s okay. The other team is still deploying to on-prem data centers, while your team is on the bleeding edge of managed K8s.

* **You Prefer**
  * Greatest flexibility
* **Pros:**
  * Fully customized toolset for the application team
  * Allowing fine-tuned control.
* **Cons:**
  * Disparate tooling
  * Higher cost in tooling
  * Multiple pipelines
  * Re-inventing the wheel
  * Application team maintaining CI/CD pipeline instead of focusing on the application

## CI/CD

Do you automate your TF deployments currently? or is it a manual process? What else are you doing in your CI/CD pipeline related to the infrastructure, and what does the handoff process look like?

\<insert diagram of env zero in a CI/CD workflow>

The basic integration of env zero involves connecting env zero to your VCS and (optionally) enabling the CD functions (Plan on PR and Deploy on Push).  This gives you the ability to trigger plans and deployments as your code changes.

env zero allows you to take it a step further with either [built-in](/guides/integrations/integrations) or [custom](/guides/admin-guide/custom-flows) integrations for steps you require as part of the deployment workflow. This includes (but is not limited to):

* Policy enforcement - You want to make sure that tags are in place.
* Security scanning - Using an IaC static code analysis tool to scan for security vulnerabilities in your code.
* Secret fetching - Perhaps you want to store your secrets in a secrets manager, and you want to manage that process in a pipeline.
* Configure resources - Use configuration mgmt. tools like Ansible or SaltStack to automatically configure resources after they are deployed.
* Testing - After your infrastructure has been provisioned, you want to run some basic functional or integration tests.
* Notification - You want to notify certain users when a deployment has failed, or waiting for approval.

The options are limitless!  What do you want to do or wish you could do before, during, or after resources are provisioned?  env zero allows you to inject custom steps at any stage of the build process.

### Scheduling

Do you currently have an automated scheduling of resources for creation and destruction, or automated drift detection?

env zero tries to minimize all those repetitive tasks as much as possible, and we are still building out ways to do so.  Our [scheduling](/guides/admin-guide/environments/scheduling) feature allows you to build and destroy resources at specific times of the day, week, or month, using cron expressions.  [Drift detection](/guides/admin-guide/environments/drift-detection) can run on the hour, every hour, or whenever you want!  Drifts can be flagged up with the env zero platform or we can let you know via [Teams or Slack](/guides/integrations/notifications).  We even have features such as workflow triggers allowing for automated promotions.

## Resource Structure and Environment Promotions

Are you currently promoting from a lower environment automatically, or manually?

Do you use a branching strategy (dev, stage, prod) to help manage the promotion of your infrastructure?

Or do you use a folder strategy for managing your various staging environments?

Whichever way you manage your environments through branches or folders, you can manage it in env zero.  With env zero, you can automate your deployments, and automate your promotions, or you can manually approve each deployment. The addition of approval policies allows for special edge cases to be reviewed for manual approval.

***

**Regardless of the way you work now, or the way you dreamt of working, env zero has the features and flexibility to allow you to meet your potential.  Reach out to our Sales Team if you'd like to discuss any of the above concepts further.**

Built with [Mintlify](https://mintlify.com).
