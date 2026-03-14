# Source: https://buildkite.com/docs/pipelines/source-control/bitbucket.md

# Bitbucket

Buildkite integrates with [Bitbucket](https://bitbucket.org/) to provide automated builds based on your source control. You can run a build every time you push code to Bitbucket, and pull requests can have their build status live-updated as builds progress.

This guide shows you how to set up your Bitbucket builds with Buildkite.

## Set up the Bitbucket webhook

Once you've created a pipeline in Buildkite and copied in your Bitbucket repository URL, Buildkite shows you setup instructions for configuring your Bitbucket webhooks.

You can also find these instructions by following the **Bitbucket Setup Instructions** link on your Buildkite pipeline's **Settings** page:

<div style="max-width: 296px"><div class="responsive-image-container"><img alt="Screenshot of Bitbucket setup instructions link" src="/docs/assets/setup-instructions-uEVDf6PW.png" /></div></div>

The setup instructions give you:

- A direct link to your Bitbucket repository's **Webhooks** settings
- Instructions
- A custom webhook URL for the pipeline

<div style="max-width: 869px"><div class="responsive-image-container"><img alt="Screenshot of Bitbucket setup instructions on Buildkite" src="/docs/assets/setup-CDsL9ekN.png" /></div></div>

Once you've followed the link you can add a new webhook:

<div style="max-width: 698px"><div class="responsive-image-container"><img alt="Screenshot of a Bitbucket webhook settings" src="/docs/assets/bitbucket-webhook-add-wPZbPjKc.png" /></div></div>

After filling out the webhook details using the instructions from your Buildkite pipeline settings, select **Save**, and you're ready to trigger a build.

## Enable commit status updates

If you want your Bitbucket pull request's build status icons to update as builds progress, you need to connect your Bitbucket account with Buildkite. You only need to do this once, and if you don't need build status updates you can skip this step altogether.

To connect your Bitbucket account:

1. Open Buildkite's **Personal Settings**.
2. Choose **Connected Apps**.
3. Select **Connect** next to **Bitbucket**.

<div style="max-width: 1161px"><div class="responsive-image-container"><img alt="Screenshot of the Buildkite Connected Apps screen" src="/docs/assets/personal-settings-Dec2cCPC.png" /></div></div>

Buildkite prompts you to give permission for Buildkite to post status updates, then redirects back to your **Connected Apps** page.

## Branch configuration and settings

<p>You can edit the version control provider settings for each pipeline from the pipeline's settings page. Go to <strong>Pipelines</strong> &gt; your specific pipeline &gt; <strong>Settings</strong> &gt; your Git service provider.</p>

<p>If you need more control over your pipeline configuration, add a <a href="/docs/pipelines/configure/defining-steps#adding-steps">pipeline.yml</a> to your repository. Then you can use <a href="/docs/pipelines/configure/conditionals">conditionals</a> and <a href="/docs/pipelines/configure/workflows/branch-configuration">branch filtering</a> to configure your pipeline.</p>

## Using one repository in multiple pipelines and organizations

<p>If you want to use the same repository in multiple pipelines (including pipelines in different Buildkite organizations), you need to configure a separate webhook for each pipeline. Follow the webhook setup instructions in the Buildkite UI. Buildkite shows you these instructions when you create the pipeline, but you can also find them in <strong>Pipeline</strong> &gt; your specific pipeline &gt; <strong>Settings</strong> &gt; your Git service provider &gt; your Git service provider's <strong>Setup Instructions</strong>.</p>

## Build skipping

<p>You may not always want to rebuild on every commit, or branch. You can configure Buildkite to ignore <a href="/docs/pipelines/configure/skipping#ignore-a-commit">individual commits</a> or <a href="/docs/pipelines/configure/workflows/branch-configuration">branches</a>, or to <a href="/docs/pipelines/configure/skipping">skip builds</a> under certain conditions.</p>
