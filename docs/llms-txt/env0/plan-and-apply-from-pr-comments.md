# Source: https://docs.envzero.com/guides/admin-guide/environments/plan-and-apply-from-pr-comments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Plan And Apply via PR Comments

> Trigger env zero plan and apply commands directly from pull request comments in your VCS provider

As software developers, we all use a Version Control System (VCS) as the main tool in our process. With env zero, you can also manage your Infrastructure as Code (IaC) deployments directly from your VCS provider.\
Commenting with env zero commands on a pull request makes it possible to interact with your env zero environments without having to log in to the env zero platform.

#### For an env zero environment to be actionable in a pull request comment, the following prerequisites must be met

1. The environment needs to have originated from a VCS-integrated template, and its configured revision must be the same as the base branch (target) of the pull request
2. The environment has ‘Enable PR Comments Commands for this Environment’ enabled
3. (Optional) The environment has Alias set

## Configuration

In order to configure this feature, you will have to enable the ‘Enable PR Comments Commands for this environment’ checkbox. Go to ‘Environments’, select ‘Settings’ and check ‘Enable PR Comments Commands for this environment’. Optional: Set an alias for each environment in which you would like to run individual commands using an `-e` flag. This alias will be used as a unique environment identifier when running a command from your VCS provider.\
**Environment aliases may only contain letters, numbers, \_, and -.**\
Even without setting an alias, the environment will still be included when using `--all` or `--path` flags.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/c54b143-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=276a8e88be67fb4df87f1293c685b9e2" alt="" width="2390" height="706" data-path="images/guides/admin-guide/environments/c54b143-image.png" />

<Warning>
  **Role Based Access**

  Note that when enabling this feature, anyone who can comment on the pull request can trigger a plan or an apply command, regardless of their role and access level in env zero, making your VCS provider determine the RBAC in this case.

  If you want to enforce PR commenter permissions based on env zero user permissions, jump to the [Enforce PR commenter permissions section](/guides/admin-guide/environments/plan-and-apply-from-pr-comments/#enforce-pr-commenter-permissions-on-env-zero).
</Warning>

<Note>
  **Self-hosted VCS provider support**

  To enable this feature for GitHub Enterprise, Bitbucket Server and GitLab Enterprise, make sure your VCS Webhook is configured to send PR comments events.
</Note>

## List of Affected Environments

Every PR push will generate a PR comment, indicating which environments are affected by changes to this PR. An environment must enable the 'Enable PR Comments Commands for this environment' to be detected as affected, as described in the [Configuration](/guides/admin-guide/environments/plan-and-apply-from-pr-comments/#configuration) above. Below is an example of a comment which lists three affected environments and their full paths:

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/d12a257-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=e6314e151a5d475461d7e589ccf82a31" alt="" width="2288" height="1352" data-path="images/guides/admin-guide/environments/d12a257-image.png" />

This comment is updated (edited) on every PR commit, so only a single comment will be shown in the PR.

## Supported env zero commands

### env0 help command

ℹ️    `env0 help` - Lists all available commands.

<img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/f8599b6-screenshot_2023-07-06_at_12.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=6666ac1c373d72db87792de213a6daea" alt="" width="907" height="453" data-path="images/guides/admin-guide/environments/f8599b6-screenshot_2023-07-06_at_12.png" />

### env0 list command

🔢    `env0 list` - Returns a list of all available environments and their aliases to plan and apply in env zero.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/93bebff-env0_list_command.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=86cdbf61df09d847d4be0ee558a619b0" alt="" width="1638" height="452" data-path="images/guides/admin-guide/environments/93bebff-env0_list_command.png" />

### env0 plan command

🔂    `env0 plan --all [-v {name=value}]` - Runs `plan` on all the affected environments listed in the `affected environments` comment above.

🔂    `env0 plan --path "<path glob pattern>" [-v {name=value}]` - Runs `plan` on all the environments listed in the `affected environments` comment above whose full path matches the given [glob pattern path](https://en.wikipedia.org/wiki/Glob_\(programming\)). Use quotes `"` around the glob pattern if it contains spaces.

🔂    `env0 plan -e {environments aliases} [-v {name=value}]` - Runs `plan` on a set of provided env zero environment aliases (comma-separated).

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/de7be33-env0_plan_command.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=fff8b395685ce5e82ee9523d231a36d2" alt="" width="1652" height="442" data-path="images/guides/admin-guide/environments/de7be33-env0_plan_command.png" />

### env0 apply command

⏯️  `env0 apply --all [-v {name=value}]` - Runs `apply` on all the affected environments listed in the `affected environments`comment above.

⏯️  `env0 apply --path "<path glob pattern>" [-v {name=value}]` - Runs `apply` on all the environments listed in the `affected environments` comment above whose full path matches the given [glob pattern path](https://en.wikipedia.org/wiki/Glob_\(programming\)) . Use quotes `"` around the glob pattern if it contains spaces.

⏯️  `env0 apply -e {environments aliases} [-v {name=value}]` - Runs `apply` on a set of provided env zero environment aliases (comma-separated).

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/27d28e9-env0_apply_command.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=a5e49358841d2f48140d75f3ee33756d" alt="" width="1652" height="438" data-path="images/guides/admin-guide/environments/27d28e9-env0_apply_command.png" />

<Info>
  **Requires Approval Behavior in env zero Apply**

  By default, applies triggered from PR comments are approved automatically.

  **Why?**
  When using apply via PR comments, we assume that users rely on their existing VCS governance methods, such as:

  1. Status checks
  2. PR approvals
  3. Branch protection rules

  You can override this behavior by enabling "Require approval for PR comment applies" in the `Organization Settings → Policies page`.

  Learn more about it [here](/guides/admin-guide/environments/plan-and-apply-from-pr-comments#require-approval-for-pr-comment-applies)
</Info>

<Info>
  **Specifying Environment Variables in plan and apply**

  To include multiple variables, use the following format:

  ```bash  theme={null}
  -v {name=value} -v {name=value}
  ```

#### Use Case: Terraform Environment Variables

  This approach is especially useful for setting [Terraform environment variables](https://developer.hashicorp.com/terraform/cli/config/environment-variables#environment-variables).

  For example, you can utilize the `ENV0_TERRAFORM_TARGET` variable to perform [Target Resources](https://developer.hashicorp.com/terraform/tutorials/state/resource-targeting) deployments, as explained in the [Additional Controls](/guides/admin-guide/additional-controls/#terraform-partial-apply):

  ```bash  theme={null}
  -v ENV0_TERRAFORM_TARGET=module.example_resource
  ```

</Info>

<Warning>
  **Important Note on Persistent Variables**

  When setting a variable using:

  ```bash  theme={null}
  -v {name=value}
  ```

  This value will persist in the next deployment.

  For example, if you set `ENV0_TERRAFORM_TARGET`, subsequent deployments will continue to use the same target, which may be opaque to users and could lead to unexpected behavior.
</Warning>

## Apply Requirements

The apply command also verifies that the pull request has the following requirements:

1. **GitHub** - We won't run the apply command if you have a protected branch in place and all the requirements are not met. You can read more about [protected branches here](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches).
2. **Bitbucket / Bitbucket Server** - We verify that at least one person who isn't the author of the PR approved the pull request, and that none of the participants requested changes. You can learn more about [reviewing a pull request](https://support.atlassian.com/bitbucket-cloud/docs/review-code-in-a-pull-request/) in Bitbucket and [declining a pull request](https://support.atlassian.com/bitbucket-cloud/docs/decline-a-pull-request/).
3. **Azure DevOps** - We won't run the apply command if you have required [branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies) checks that failed.

<Warning>
  **GitHub: Circular dependency with required `env0/Apply` status check**

  If you set the `env0/Apply` status check as a required check in GitHub branch protection, the PR will appear non-mergeable before apply runs, preventing the apply from executing. To resolve this, enable the [Bypass Apply Mergeability Check](/guides/policies-governance/bypass-apply-mergeability-check) policy.
</Warning>

## env0/Apply Commit Check

When running `env0 apply --all` or `env0 apply --path <path>`, a new `env0/Apply` commit check will be added on top of the individual deployment checks that you have per environment deployed.

<Tip>
  If you want to make `env0/Apply` a required status check in GitHub branch protection, see [Bypass Apply Mergeability Check](/guides/policies-governance/bypass-apply-mergeability-check) to avoid a circular dependency with the apply mergeability requirement.
</Tip>

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/ed776ba-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=51493ed9295672b4efceaaeca0d349fd" alt="" width="2264" height="606" data-path="images/guides/admin-guide/environments/ed776ba-image.png" />

This commit check will show a `success` status once all the environments listed in the [affected environments comment](/guides/admin-guide/environments/plan-and-apply-from-pr-comments/#list-of-affected-environments) have been applied successfully. In case of failure in any of the deployments, the check's status will be set to `failure`.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/7320e29-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=86fc82eb29b4743312292a84be0764ce" alt="" width="2281" height="797" data-path="images/guides/admin-guide/environments/7320e29-image.png" />

The check's status is calculated after every deployment of an environment listed in the affected environments comment.

## Enforce PR commenter permissions on env zero

With env zero, you can restrict your users' permissions through [role-based access controls](/guides/admin-guide/user-role-and-team-management/rbac). One drawback of using PR Comment Plan and Apply is that the VCS provider determines your users' permissions. By default, anyone with comment permission on your repository can run a Plan or an Apply on your environments.

Enforce PR commenter permissions on env zero is an organizational policy that lets you apply your env zero permissions to your VCS provider users. When turned on, env zero will validate that a user trying to run PR Comment Commands have adequate permissions.

### Turning on the policy for your organization

Navigate to 'Organization Settings' then go to 'Policies' and check 'Enforce commenter permissions on env zero'.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/85b7ab9-pr_plan_policy.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=f5ffeff25200a7d6d0ccdd91fb5dbb3c" alt="Interface screenshot showing configuration options" width="2880" height="1558" data-path="images/guides/admin-guide/environments/85b7ab9-pr_plan_policy.png" />
</Frame>

### Map VCS provider user

Now that the feature is turned on, every user across the organization who wishes to use the PR comments flow must set up a mapping of their VCS provider user.\
First you will need to get your VCS provider user ID from one of the supported VCS providers.

### Setting your VCS user in env zero

Now that you have your VCS provider user ID, head over to your env zero account, click on the avatar image in the top right corner, and click on 'Personal Settings' to enter your profile page.\
In the VCS user ids tab, enter the ID from the previous step in the VSC Provider User ID textbox and click on the ‘Save’ button.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/efd62d423af68ffe01e1dbc13946cfbbf0916df9e011169df0644c621086a25d-image_6.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=f3a60190b0094d0b627a359ba2c0529a" alt="Interface screenshot showing configuration options" width="3431" height="1513" data-path="images/guides/admin-guide/environments/efd62d423af68ffe01e1dbc13946cfbbf0916df9e011169df0644c621086a25d-image_6.png" />
</Frame>

### GitHub

While logged in to your GitHub account, click on your profile image in the right top corner of the page and copy your username.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/d7cae97-screen_shot_2023-02-23_at_14.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=a0bc082b0df4f890bd4abd320492aaff" alt="Interface screenshot showing configuration options" width="398" height="324" data-path="images/guides/admin-guide/environments/d7cae97-screen_shot_2023-02-23_at_14.png" />
</Frame>

### Bitbucket

While logged in to your Bitbucket user, visit [this URL](https://bitbucket.org/!api/2.0/user) from your browser. you will receive a JSON from which you will need to extract the `accound_id` field.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/ed5026d-screen_shot_2023-02-23_at_16.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=820345ed7187a27a586009127cf25bc6" alt="" width="1165" height="781" data-path="images/guides/admin-guide/environments/ed5026d-screen_shot_2023-02-23_at_16.png" />

### Bitbucket Server

While logged into your Bitbucket Server account, go to your profile and locate the username by your avatar.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/480e929-screen_shot_2023-02-23_at_14.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=9bfcdeac7c870de8958c14b3ef9eb3fa" alt="" width="2414" height="640" data-path="images/guides/admin-guide/environments/480e929-screen_shot_2023-02-23_at_14.png" />

### GitLab / GitLab Enterprise Edition

While logged into your GitLab account, navigate to the ‘Profile’ tab and ‘Edit Profile’ or "kebab" menu to find and copy your user ID.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/87b05a73e0b321414b32c6271f2c45aa9dd434a6ab9b61b5c449479cbe0abdc6-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=9db0e060d576c4af1d22a230b929fd82" alt="" width="700" height="470" data-path="images/guides/admin-guide/environments/87b05a73e0b321414b32c6271f2c45aa9dd434a6ab9b61b5c449479cbe0abdc6-image.png" />

### Azure DevOps

While logged in to your Azure DevOps account, click on your profile image in the right top corner of the page and copy your unique user ID.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/109df60-screenshot_2023-07-02_at_16.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=3a5279b09176044822e5800307cd7d71" alt="Interface screenshot showing configuration options" width="838" height="726" data-path="images/guides/admin-guide/environments/109df60-screenshot_2023-07-02_at_16.png" />
</Frame>

<Info>
  **Additional Content**

* [Alternative to Atlantis](https://www.env0.com/alternatives/atlantis-alternative)
* [Migrating from Atlantis to env zero](https://www.env0.com/blog/video-tutorial-how-to-migrate-from-atlantis-to-env0)
</Info>

## Status Checks for PR Comments

env zero offers the convenience of tracking the deployment status of your PRs directly from your Git provider's interface. By integrating this feature into the familiar UI, you not only gain visibility into deployment statuses, but also leverage it to enhance your CI pipeline, using checks to enforce successful infrastructure deployments.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/d0360f5-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=c5a1369206aaa945379708507623bf62" alt="" width="920" height="666" data-path="images/guides/admin-guide/environments/d0360f5-image.png" />

## Require approval for PR comment applies

To require approval for applies triggered by PR comments, you must enable the "Require approval for PR comment applies" policy in Organization Settings → Policies.

With this policy enabled, running env zero apply will trigger a deployment that will wait for manual approval.\
Once the plan step finishes, the plan results will be posted as a comment on the PR:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/2b0fa90d8c9af8629a430672a6ebca9ed03fe066c74232776afaebb897685531-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=306d094a056ed533f4fb3311103a7510" alt="" width="1710" height="806" data-path="images/guides/admin-guide/environments/2b0fa90d8c9af8629a430672a6ebca9ed03fe066c74232776afaebb897685531-image.png" />

The environment’s Apply Commit Check and the Apply All Commit Check will remain “In Progress” until the deployment is either approved or canceled.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/841a24810f3b06dbd75ccf50c79b095efaaa988b25bdf60e8f079c7f1f6aceb9-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=24f9ef11ecdca9d13b12ddad92b7c378" alt="" width="1710" height="404" data-path="images/guides/admin-guide/environments/841a24810f3b06dbd75ccf50c79b095efaaa988b25bdf60e8f079c7f1f6aceb9-image.png" />

Note: When running an apply that requires approval, we will not check if the PR is mergeable at this stage - that check happens when approving the apply.

Additional Supported Commands (when the policy is enabled):

### env0 approve command

🔂    `env0 approve --all [-v {name=value}]` - Runs `approve` on all the affected environments listed in the `affected environments` comment above.

🔂    `env0 approve --path "<path glob pattern>" [-v {name=value}]` - Runs `approve` on all the environments listed in the `affected environments` comment above whose full path matches the given [glob pattern path](https://en.wikipedia.org/wiki/Glob_\(programming\)). Use quotes `"` around the glob pattern if it contains spaces.

🔂    `env0 approve -e {environments aliases} [-v {name=value}]` - Runs `approve` on a set of provided env zero environment aliases (comma-separated).

### env0 cancel command

🔂    `env0 cancel --all [-v {name=value}]` - Runs `cancel` on all the affected environments listed in the `affected environments` comment above.

🔂    `env0 cancel --path "<path glob pattern>" [-v {name=value}]` - Runs `cancel` on all the environments listed in the `affected environments` comment above whose full path matches the given [glob pattern path](https://en.wikipedia.org/wiki/Glob_\(programming\)). Use quotes `"` around the glob pattern if it contains spaces.

🔂    `env0 cancel -e {environments aliases} [-v {name=value}]` - Runs `cancel` on a set of provided env zero environment aliases (comma-separated).

Both commands will only run for environments where the deployment awaiting approval was triggered from the same PR.

When approving, a deployment summary will be posted back to the PR, and commit checks will be marked as successful.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/566e32313b6e11190d53b1f2ea83520010c93cc04e1dc3339af8d7b076779846-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=484de2c0ae87e4f5b6324b9cd7ba58ec" alt="" width="1710" height="670" data-path="images/guides/admin-guide/environments/566e32313b6e11190d53b1f2ea83520010c93cc04e1dc3339af8d7b076779846-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/966609a60004ba80c0fea82cad58b7bc7ea9db73960b959872a11d6f643f7f31-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=462ea7092fa3a6503db4a0287692db98" alt="" width="1710" height="498" data-path="images/guides/admin-guide/environments/966609a60004ba80c0fea82cad58b7bc7ea9db73960b959872a11d6f643f7f31-image.png" />

Attempting to approve a deployment triggered from another PR will fail and post an error comment to the PR.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/64c9065e88398060f1bbac1b8f60459270b731cadd9be5bddf7addccca8e8c71-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=bd3ff28f0d3769fdf3ed9c40dd23ceef" alt="" width="1710" height="316" data-path="images/guides/admin-guide/environments/64c9065e88398060f1bbac1b8f60459270b731cadd9be5bddf7addccca8e8c71-image.png" />

When canceling, commit checks will fail, and a Deployment Canceled comment will be added to the PR.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/8020b6d588598170a428947e35a092b9a9f1d1339248211eb3f0c7c1c449f996-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=ad8c2547b0825f87bf214fc20f489300" alt="" width="1710" height="600" data-path="images/guides/admin-guide/environments/8020b6d588598170a428947e35a092b9a9f1d1339248211eb3f0c7c1c449f996-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/6dd172eba168b9d2a6e33458581a3fd00cb90a27cb89fc609bfca9a6c2d89481-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=d83b92d334504818adf7b77573bd7161" alt="" width="1710" height="400" data-path="images/guides/admin-guide/environments/6dd172eba168b9d2a6e33458581a3fd00cb90a27cb89fc609bfca9a6c2d89481-image.png" />

If you try to run an apply while another apply is already waiting for approval, the new deployment will be queued, and a PR comment will indicate this.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/e03e2002678c1e38a853b911add7401618916c9de2653241e29ae0c9625224c5-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=e6a1e9abca232edfaf186cffa350194b" alt="" width="1710" height="594" data-path="images/guides/admin-guide/environments/e03e2002678c1e38a853b911add7401618916c9de2653241e29ae0c9625224c5-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/0331158be031de5c87f307ace49d347052c34c37c525e5be3e0e477d50076d92-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=d29e18b7b49eb0ccb8824189f0b1f56a" alt="" width="1710" height="316" data-path="images/guides/admin-guide/environments/0331158be031de5c87f307ace49d347052c34c37c525e5be3e0e477d50076d92-image.png" />

Built with [Mintlify](https://mintlify.com).
