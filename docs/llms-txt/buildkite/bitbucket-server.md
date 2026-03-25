# Source: https://buildkite.com/docs/pipelines/source-control/bitbucket-server.md

# Bitbucket Server

Buildkite integrates with Bitbucket Server to provide automated builds based on your source control. This guide shows you how to set up your Bitbucket Server builds with Buildkite. You can run a build every time you push code to Bitbucket Server, using a webhook that you create in your Bitbucket Server.

> 📘 Buildkite plan availability and Bitbucket Server version
> Bitbucket Server is only available to Buildkite customers on [Pro or Enterprise](https://buildkite.com/pricing) plans.
> This guide is based on Bitbucket Server version 7.11.1. Earlier or later versions may have variations in the interface.

## Step 1: connect Bitbucket Server and set up a pipeline

1. Select **Settings** to open the **Organization Settings** page.
1. Navigate to **Repository Providers**.
1. Select **Bitbucket Server**.
1. In **URLs**, enter the address of your Bitbucket Server, including a port if needed. For example, `localhost:8000`. You can also restrict which network addresses are allowed to trigger builds using webhooks in **Allowed IP Addresses** in **Network Settings**.
1. Select **Save Settings**.
1. Set up a pipeline as normal. Refer to [Pipelines](/docs/pipelines) for more information.

## Step 2: confirm your setup

If your configuration worked, Buildkite automatically recognizes your repository URL as a Bitbucket Server repository. To check this, go to **Pipelines** > your specific pipeline > **Settings**. You should see **Bitbucket Server** on the side as a configurable area for your pipeline.

## Step 3: work through the in-app guide to set up your webhook

Buildkite includes built-in instructions on how to set up a Bitbucket Server webhook. This webhook allows Bitbucket Server to trigger Buildkite builds in response to events like code pushes and pull requests.

1. Navigate to **Pipelines** > your specific pipeline > **Settings** > **Bitbucket Server**.
1. Select **Bitbucket Server Setup Instructions**.
1. Follow the on screen instructions to configure your webhook.

## Branch configuration and settings

<p>You can edit the version control provider settings for each pipeline from the pipeline's settings page. Go to <strong>Pipelines</strong> &gt; your specific pipeline &gt; <strong>Settings</strong> &gt; your Git service provider.</p>

<p>If you need more control over your pipeline configuration, add a <a href="/docs/pipelines/configure/defining-steps#adding-steps">pipeline.yml</a> to your repository. Then you can use <a href="/docs/pipelines/configure/conditionals">conditionals</a> and <a href="/docs/pipelines/configure/workflows/branch-configuration">branch filtering</a> to configure your pipeline.</p>

## Using one repository in multiple pipelines and organizations

<p>If you want to use the same repository in multiple pipelines (including pipelines in different Buildkite organizations), you need to configure a separate webhook for each pipeline. Follow the webhook setup instructions in the Buildkite UI. Buildkite shows you these instructions when you create the pipeline, but you can also find them in <strong>Pipeline</strong> &gt; your specific pipeline &gt; <strong>Settings</strong> &gt; your Git service provider &gt; your Git service provider's <strong>Setup Instructions</strong>.</p>

## Build skipping

<p>You may not always want to rebuild on every commit, or branch. You can configure Buildkite to ignore <a href="/docs/pipelines/configure/skipping#ignore-a-commit">individual commits</a> or <a href="/docs/pipelines/configure/workflows/branch-configuration">branches</a>, or to <a href="/docs/pipelines/configure/skipping">skip builds</a> under certain conditions.</p>
