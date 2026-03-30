# Source: https://buildkite.com/docs/pipelines/source-control/gitlab.md

# GitLab

You can use Buildkite to run builds on [GitLab](https://about.gitlab.com/) commits.

## GitLab repositories

If you host your repositories on [gitlab.com](https://gitlab.com/) enter your gitlab.com repository URL when you create your pipeline in Buildkite (for example, `git@gitlab.com:your/repo.git`) and follow the instructions provided on that page to set up webhooks.

## GitLab Self-Managed repositories

You can also use repositories from your own self-managed GitLab service but you'll need to connect it to Buildkite first.

>📘
> The earliest supported version of GitLab is <a href=https://about.gitlab.com/releases/2014/10/22/gitlab-7-4-released/>7.4</a>.

1. Open your Buildkite organization's **Settings** and choose [**Repository Providers**](https://buildkite.com/organizations/-/repository-providers).
1. Select **GitLab Self-Managed**.
1. Enter the URL to your GitLab installation (for example, `https://git.example.org`).
1. You can optionally specify a list of IP addresses to restrict where builds can be triggered from. This field accepts a space separated list of networks in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

    <div style="max-width: 872px"><div class="responsive-image-container"><img alt="Screen of Buildkite Organization GitLab Settings" src="/docs/assets/gitlab-org-settings-H2iyuIoB.png" /></div></div>

1. Select **Save Settings** before leaving this page.
1. Create a new pipeline on Buildkite using your GitLab repository's URL (for example, `git@git.mycompany.com:your/repo.git`) and follow the instructions on the pipeline creation page.

> 📘 Verify your GitLab account
> To ensure that the commit author from GitLab is a verified Buildkite account user, a public email must be specified in the user's GitLab account. This public email must match their Buildkite user account email.

## Branch configuration and settings

<p>You can edit the version control provider settings for each pipeline from the pipeline's settings page. Go to <strong>Pipelines</strong> &gt; your specific pipeline &gt; <strong>Settings</strong> &gt; your Git service provider.</p>

<p>If you need more control over your pipeline configuration, add a <a href="/docs/pipelines/configure/defining-steps#adding-steps">pipeline.yml</a> to your repository. Then you can use <a href="/docs/pipelines/configure/conditionals">conditionals</a> and <a href="/docs/pipelines/configure/workflows/branch-configuration">branch filtering</a> to configure your pipeline.</p>

## Using one repository in multiple pipelines and organizations

<p>If you want to use the same repository in multiple pipelines (including pipelines in different Buildkite organizations), you need to configure a separate webhook for each pipeline. Follow the webhook setup instructions in the Buildkite UI. Buildkite shows you these instructions when you create the pipeline, but you can also find them in <strong>Pipeline</strong> &gt; your specific pipeline &gt; <strong>Settings</strong> &gt; your Git service provider &gt; your Git service provider's <strong>Setup Instructions</strong>.</p>

## Build skipping

<p>You may not always want to rebuild on every commit, or branch. You can configure Buildkite to ignore <a href="/docs/pipelines/configure/skipping#ignore-a-commit">individual commits</a> or <a href="/docs/pipelines/configure/workflows/branch-configuration">branches</a>, or to <a href="/docs/pipelines/configure/skipping">skip builds</a> under certain conditions.</p>

## Commit statuses

Buildkite Pipelines can update commit statuses in GitLab. You can then see the status of your builds from your GitLab.com commits and merge requests with direct links back to your Buildkite Pipelines build.

For GitLab.com, connect your Buildkite and GitLab user accounts by going to your Buildkite user account's **Personal Settings** from the global navigation > **Connected Apps** page:

<div style="max-width: 582px"><div class="responsive-image-container"><img alt="Screen of Buildkite User Connected Apps with GitLab.com connected" src="/docs/assets/gitlab-connected-apps-6yU1qf6d.png" /></div></div>

Next, in your Buildkite organization, go to **Pipelines** > your specific pipeline > **Settings** > **GitLab**, and make sure the **Update commit statuses** checkbox is selected:

<div style="max-width: 749px"><div class="responsive-image-container"><img alt="Screen of Buildkite User Connected Apps with GitLab.com connected" src="/docs/assets/gitlab-update-commit-status-CoRCEKa8.png" /></div></div>

For a self-managed GitLab service, ensure you have configured API authentication for your Buildkite organization's GitLab repository provider. To do this, select  **Settings** from the global navigation > **Repository Providers** > **GitLab Self-Managed** page:

<div style="max-width: 584px"><div class="responsive-image-container"><img alt="Screen of Buildkite GitLab repository provider settings page with authentication configured" src="/docs/assets/gitlab-repository-provider-authentication-DICpF_vD.png" /></div></div>

Then update your pipeline's repository settings as above.
