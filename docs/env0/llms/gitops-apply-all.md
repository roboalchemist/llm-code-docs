# Source: https://docs.envzero.com/changelogs/2024/07/gitops-apply-all.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🏝️ GitOps Apply All

> From now on, env0 gives you more control over deploying your environments directly from the VCS using the new feature: **GitOps Apply All**. PR will have a new comment, listing the affected environments. Affected environments can be easily applied before merging using the new `env0 apply --all` command. Visit [our docs](/guides/admin-guide/environments/plan-and-apply-from-pr-comments) for more information.

You asked for it, and it's finally here! From now on, env0 gives you more control over deploying your environments directly from the VCS using the new feature: **GitOps Apply All**

Enabling this feature is very simple, all you need to do is go to environment settings and click Continuous Deployment. You can also enable this feature on the project level, by going to Project Settings, clicking Policies and selecting Continuous Deployment. Your changes will be applied to every new environment created in that project.\
See [Configuration docs](/guides/admin-guide/environments/plan-and-apply-from-pr-comments#configuration) for more details.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/07/bcdfca3-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=461f5fe84198e1c626f8e4bcc3f4593b" alt="Feature demonstration screenshot showing new functionality" width="2382" height="702" data-path="images/changelogs/2024/07/bcdfca3-image.png" />
</Frame>

Once it is enabled, every PR commit will have a comment listing the affected environments by the latest commit to the PR:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/07/4129ed4-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=62062aefa5a9622ad55e29046c32eef7" alt="Feature demonstration screenshot showing new functionality" width="2288" height="1352" data-path="images/changelogs/2024/07/4129ed4-image.png" />
</Frame>

The affected environments can be applied (or planned) by running one of the following PR comments:

* `env0 apply --all`
* `env0 apply --path "<glob path>"`

Read more about the different commands in [our docs](/guides/admin-guide/environments/plan-and-apply-from-pr-comments#supported-env0-commands)

Finally, upon first deployment, a new `env0/Apply` commit check will be added (on top of the individual deployment commit checks). The commit check will be `in progress`and will be in `success` status once all affected environments have been deployed successfully, or `failure` status if one of the deployments failed.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/07/5f2e948-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=7cca068d2aa1bbeaf9e8c2cac9082643" alt="Feature demonstration screenshot showing new functionality" width="2281" height="797" data-path="images/changelogs/2024/07/5f2e948-image.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
