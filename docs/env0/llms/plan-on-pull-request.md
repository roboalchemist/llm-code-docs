# Source: https://docs.envzero.com/guides/admin-guide/environments/plan-on-pull-request.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running Plan on Pull Requests

> Automatically run a Terraform plan on every pull request to review infrastructure changes before merging

## Pull Request Plan in env zero

env zero allows you to control and monitor your infrastructure code changes with pull request automation. When setting Pull Request Plan (PR Plan), your environment will automatically run a deployment consisting of only the Plan phase (without applying any infrastructure changes) and share the results with you via a comment on your pull request. Pull Request Plan will run on every push to an open pull request.

#### For a PR Plan to run automatically, the following prerequisites must be met

1. The environment has Pull Request Plan enabled
2. The environment originated from a VCS-integrated template, and its configured revision is the same as the branch (target) of the pull request
   * [GitHub Integration](/guides/admin-guide/templates/github-templates) - is currently the only VCS supporting forks (from private repositories only)

## Enable Pull Request Plan

Go to your existing Environment in env zero and head to the Settings tab.\
Under Continuous Deployment, enable Run Terraform Plan on Pull Requests targeting this branch.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/ccf9004-screen_shot_2022-05-01_at_13.jpeg?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=cb49da250f2d9f92042d3e0279a68ab3" alt="" width="1610" height="803" data-path="images/guides/admin-guide/environments/ccf9004-screen_shot_2022-05-01_at_13.jpeg" />

**You can choose to run by the following options:**

* Any change - your environment will receive a PR Plan on every push to the repository.
* Changes on Template Directory files - your environment will receive a PR Plan on every push that contains file changes under the Template folder
* Changes by file filter pattern - your environment will receive a PR Plan on every push containing file changes by matching them to the pattern. See below how to configure the glob pattern.

You can track the Deployment history for deployments by PR Plan type:

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/9ccc1dd-ee170a7-screen_shot_2020-11-23_at_17.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=1cc8f2c67528fcf8a459e7417af8e2af" alt="" width="1413" height="470" data-path="images/guides/admin-guide/environments/9ccc1dd-ee170a7-screen_shot_2020-11-23_at_17.png" />

<Info>
  **[Glob pattern](https://en.wikipedia.org/wiki/Glob_\(programming\))**

  Glob patterns specify sets of filenames with wildcard characters. For example, \*.txt or my\_folder/\*\*

  It means you can configure pattern by git repository which re-deploy environment only if the push contains files that change by free pattern.

  You can configure patterns by Git repository which re-deploy an environment only if the push contains files that change by free pattern.

  For example, to configure a pattern like src/project\_1/\*\*
  you should re-deploy only if the push contains files that start with src/project\_1/...

  env zero also supports [extglob](https://github.com/micromatch/extglob?tab=readme-ov-file#extglob-cheatsheet) patterns. These allow you to write a pattern that ignores files or uses a list of folders.

  When using **OR/AND** statements with extglob, make sure to:

* Wrap each option in parentheses
* Avoid unnecessary spaces - do not add spaces between the different glob pattern options

  Examples:

* `!(third/path/\*\*)+(first/path/**|second/path/myfile.txt)`
    This means we will match any change in first/path and second/path/myfile.txt, and ignore changes under third/path. (It is recommended to add exclusions first)
* `+(Terraform/!(prod)**|Terragrunt/dev/**)`
    Match any changes in `Terraform` or `Terragrunt/dev` but ignore any changes in `Terraform/prod`
</Info>

<Info>
  **PR Plans Concurrency**

  PR Plans do not lock the Terraform state, and can be in parallel. If a bunch of PR Plans are queued in sequence, they will all run simultaneously.
</Info>

<Info>
  **Status Checks**

  When the PR Plan completes, aside from commenting with the plan itself, your commit will be marked with a passing status check. In case the PR Plan failed, the commit status will be failure.

  If the PR Plan doesn't run because the push didn't contain changed files, env zero will mark the latest commit as skipped ( if the Version Control supports it). Additional policy configuration can be found under [Do Not Report Skipped Status Check](/guides/policies-governance/do-not-report-skipped-status-check).
</Info>

<Info>
  **PR Plans from Merge Commits**

  In order to control whether Merge Commits will trigger PR Plans, see [Skip PR Plan on Merge Commits](/guides/policies-governance/skip-pr-plan-on-merge-commits)
</Info>

## Pull Request Comments

env zero will make a comment on your pull request for three different reasons:

1. When a PR Plan has started:

<Frame caption="GitLab">
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/gitlab_pr_plan_started.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=23267354365dc3df3a7ec29ac1eb6900" alt="GitLab PR plan started" width="1013" height="188" data-path="images/guides/admin-guide/environments/gitlab_pr_plan_started.png" />
</Frame>

<Frame caption="Azure DevOps">
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/azure_devops_pr_plan_started.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=b4e68416b252caf29d2f9974e643e0af" alt="Azure DevOps PR plan started" width="1194" height="270" data-path="images/guides/admin-guide/environments/azure_devops_pr_plan_started.png" />
</Frame>

1. When a PR Plan has finished successfully (full log is attached under Plan Details)

<Frame caption="GitHub">
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/github_pr_plan_finished_successfully.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=d93abf8acbca040d939f58146a45d685" alt="GitHub PR plan finished successfully" width="942" height="257" data-path="images/guides/admin-guide/environments/github_pr_plan_finished_successfully.png" />
</Frame>

<Frame caption="GitLab">
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/gitlab_pr_plan_finished_successfully.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=72dee81feaca684ff7ad58c9a22c580d" alt="GitLab PR plan finished successfully" width="987" height="266" data-path="images/guides/admin-guide/environments/gitlab_pr_plan_finished_successfully.png" />
</Frame>

<Frame caption="Bitbucket">
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/bitbucket_pr_plan_finished_successfully.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=a04aee584651d9f1ecbab353f687bafb" alt="Bitbucket PR plan finished successfully" width="1892" height="366" data-path="images/guides/admin-guide/environments/bitbucket_pr_plan_finished_successfully.png" />
</Frame>

<Frame caption="Azure DevOps">
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/azure_devops_pr_plan_finished_successfully.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=99fc1970eb6569aa3017c86a401b274e" alt="Azure DevOps PR plan finished successfully" width="1193" height="350" data-path="images/guides/admin-guide/environments/azure_devops_pr_plan_finished_successfully.png" />
</Frame>

1. When a PR Plan has failed:

<Frame caption="GitHub">
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/github_pr_plan_failed.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=8c1af48ac6012a13275b7e9fce44d7f7" alt="GitHub PR plan failed" width="929" height="335" data-path="images/guides/admin-guide/environments/github_pr_plan_failed.png" />
</Frame>

<Frame caption="GitLab">
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/gitlab_pr_plan_failed.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=f602a6de583080682cf89e885b12ce56" alt="GitLab PR plan failed" width="993" height="298" data-path="images/guides/admin-guide/environments/gitlab_pr_plan_failed.png" />
</Frame>

<Frame caption="Bitbucket">
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/bitbucket_pr_plan_failed.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=dc6eb58bc1b8f04ec405b30c2315ab47" alt="Bitbucket PR plan failed" width="1894" height="988" data-path="images/guides/admin-guide/environments/bitbucket_pr_plan_failed.png" />
</Frame>

<Frame caption="Azure DevOps">
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/azure_devops_pr_plan_failed.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=2f22b39edc72171765007e2d973ded9b" alt="Azure DevOps PR plan failed" width="1186" height="498" data-path="images/guides/admin-guide/environments/azure_devops_pr_plan_failed.png" />
</Frame>

1. Rerun a PR Plan:
   You can rerun a PR plan deployment. The newly created deployment will be an exact snapshot in terms of commits and code source of the original PR plan.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/c118443-screen_shot_2021-12-26_at_10.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=bae3723618226eb1b9a78f04e4f2d484" alt="" width="2958" height="684" data-path="images/guides/admin-guide/environments/c118443-screen_shot_2021-12-26_at_10.png" />

## GitHub Commit Status Checks

env zero will set a status check on the commit you want to merge in the pull request. The status will be changed to 'failed' when the run had failed to generate a Terraform plan, and 'successful' when a plan was generated.

1. When the PR plan is pushed to the queue:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/054e702-screen_shot_2021-04-29_at_14.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=e757b20e6ad98846ea1bb80a6aed77b9" alt="" width="987" height="97" data-path="images/guides/admin-guide/environments/054e702-screen_shot_2021-04-29_at_14.png" />

1. When a PR Plan starts running (this will not happen [until you approve](/guides/admin-guide/environments/#approval-flow) the previous deployment):

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/04c2a82-screen_shot_2021-04-29_at_15.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=0cff7cb8de6a08ae23a7774271a10471" alt="" width="949" height="137" data-path="images/guides/admin-guide/environments/04c2a82-screen_shot_2021-04-29_at_15.png" />

1. When a Terraform plan was generated:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/5c9aaa7-screen_shot_2020-12-30_at_16.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=ee7c9d9af89dfc5c6433d7f9a5ec6f77" alt="" width="1842" height="544" data-path="images/guides/admin-guide/environments/5c9aaa7-screen_shot_2020-12-30_at_16.png" />

1. When the run was not able to generate a proper Terraform plan:

<img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/failed_terraform_plan_generation.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=8b6173b2b90d6321796d740bb82f49b7" alt="" width="1838" height="532" data-path="images/guides/admin-guide/environments/failed_terraform_plan_generation.png" />

1. If you linked your PR to multiple environments you will get the summary of all the *PR Plans*

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/a295a33-multiple_pr_plans.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=b6f9091ba6dd01ad3fa45fb23dc8293d" alt="" width="1838" height="608" data-path="images/guides/admin-guide/environments/a295a33-multiple_pr_plans.png" />

By clicking Details, GitHub will forward you to the Checks tab:

<img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/feac7f5-screen_shot_2020-12-30_at_16.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=72098c1f03bb16d23b8f894ae2cd0e81" alt="" width="1384" height="552" data-path="images/guides/admin-guide/environments/feac7f5-screen_shot_2020-12-30_at_16.png" />

Clicking View more details on env zero will take you to your environment on env zero

## GitLab Pipelines

env zero will run set a GitLab pipeline and job status on the commit you want to merge in the merge request.\
The status will be shown as 'failed' when the run had failed to generate a Terraform plan, and 'successful' when a plan was generated.

<Frame caption="A Merge Request and its associated env zero pipeline run status">
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/gitlab_merge_request_with_env0_pipeline_status.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=b7ff41f8299a0740657e466b473f200e" alt="GitLab merge request with env zero pipeline status" width="1944" height="558" data-path="images/guides/admin-guide/environments/gitlab_merge_request_with_env0_pipeline_status.png" />
</Frame>

Clicking the pipeline on the Merge Request will reveal which env zero environment deployments were  triggered and show their status.

Clicking the status will take you back to env zero, where you can see more details on this automatic plan run.

1. When a PR Plan starts running, the commit will be labeled ‘in progress’:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/75cca25-screen_shot_2021-05-10_at_11.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=4a6452581fca68a3499a4f5049e9c038" alt="" width="1027" height="164" data-path="images/guides/admin-guide/environments/75cca25-screen_shot_2021-05-10_at_11.png" />

1. When a Terraform plan was generated:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/73800e2-screen_shot_2021-05-10_at_11.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=792f10f1183c6dc93d694140e764368a" alt="" width="1078" height="197" data-path="images/guides/admin-guide/environments/73800e2-screen_shot_2021-05-10_at_11.png" />

1. When the run was not able to generate a proper Terraform plan:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/failed_terraform_plan_generation.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=8b6173b2b90d6321796d740bb82f49b7" alt="Failed Terraform plan generation" width="1838" height="532" data-path="images/guides/admin-guide/environments/failed_terraform_plan_generation.png" />
</Frame>

## Bitbucket Commit Build Status

env zero will set a status check on the commit you want to merge in the pull request.

The status will be set to ‘failing’ when the run had failed to generate a Terraform plan, and ‘successful’ when a plan was generated.

1. When the PR Plan starts running, the commit will be labeled as ‘in progress’:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/6af4b03-screen_shot_2021-05-10_at_10.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=378cd2c09cdf2a9fcd4aed30f7fbd9d9" alt="" width="561" height="142" data-path="images/guides/admin-guide/environments/6af4b03-screen_shot_2021-05-10_at_10.png" />

1. When a Terraform plan was generated:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/621c48b-screen_shot_2021-04-08_at_14.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=a70f163cfcd78b98ed1c20016170e49e" alt="" width="532" height="234" data-path="images/guides/admin-guide/environments/621c48b-screen_shot_2021-04-08_at_14.png" />

1. When the run was not able to generate a proper Terraform plan:

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/bf38ff2-screen_shot_2021-04-08_at_14.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=378dfafb86383ea085ef3d80203c025b" alt="" width="656" height="240" data-path="images/guides/admin-guide/environments/bf38ff2-screen_shot_2021-04-08_at_14.png" />

## Azure DevOps PR Status

env zero will set a status check on your pull request.\
The status will be set to 'failing' when the run had failed to generate a Terraform plan, and 'successful' when a plan was generated.

1. When the PR Plan starts running, the PR status will be labeled  ‘pending’.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/1c0d52d-image_6.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=3e3b348988e18eeeda2674e840ceeb52" alt="" width="1246" height="223" data-path="images/guides/admin-guide/environments/1c0d52d-image_6.png" />.png")

1. When a Terraform plan was generated:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/032fcd0-image_7.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=5b90873602e66261e67aaacd3ba0ed23" alt="" width="1231" height="213" data-path="images/guides/admin-guide/environments/032fcd0-image_7.png" />.png")

1. When the run was not able to generate a proper Terraform plan:

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/d26915b-image_10.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=4281990ab754d3a88c8e5f8b892b1b68" alt="" width="1228" height="213" data-path="images/guides/admin-guide/environments/d26915b-image_10.png" />.png")

## Rerun a PR Plan

You can rerun a PR Plan deployment on the deployment page.\
The newly created deployment will be an exact snapshot of the commits and code source of the original PR Plan.\
This will recreate the comment on the PR and the status checks.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/dca11de-screen_shot_2021-12-26_at_10.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=df8159c1f39fbc863c7b799b74061abe" alt="" width="2958" height="684" data-path="images/guides/admin-guide/environments/dca11de-screen_shot_2021-12-26_at_10.png" />

### Deployment Comment

When a PR Plan is triggered, a comment will be added in env zero, linking to the PR.

## Suggested Content

[Do Not Report Skipped Status Check](/guides/policies-governance/do-not-report-skipped-status-check)

[Skip PR Plan on Merge Commits](/guides/policies-governance/skip-pr-plan-on-merge-commits)

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Migrating from Atlantis to env0](https://www.env0.com/blog/video-tutorial-how-to-migrate-from-atlantis-to-env0)

[Alternative to Atlantis](https://www.env0.com/alternatives/atlantis-alternative)

Built with [Mintlify](https://mintlify.com).
