# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/enterprise-self-hosted.md

# Enterprise (Self Hosted)

Follow this guide to setup, install, and begin using Qodo Context Engine.

{% hint style="success" %}
**Need to deploy** Qodo Context Engine **on-prem?**

Head over to the [**On-Prem** documentation](https://docs.qodo.ai/qodo-documentation/on-prem) for full instructions.
{% endhint %}

{% hint style="info" %}
Qodo Context Engine is currently supported for **Enterprise customers** only.
{% endhint %}

### Models Supported

These models are used by Qodo Context Engine and must be available for Qodo Context Engine to be used:

* `gpt-5`
* `claude-4.1-opus`

{% hint style="warning" %}
Contact Qodo support if **none of these AI models are supported** by your system or if you **don't work with an official model provider**.
{% endhint %}

***

### 1. Set Up Database

Qodo Context Engine requires a database to store its indexing data and metadata. This setup enables fast, reliable retrieval of code context and insights across your repositories.

[Follow this guide to setup your database](#id-1.-set-up-database) before you continue.

***

### 2. Index your Codebase

The second step to set up Qodo Context Engine is to **index your codebase**.

This allows Qodo Context Engine to analyze your repositories, build internal context, and start answering questions intelligently.

Choose your platform to get instructions for indexing your codebase:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h2>GitHub</h2></td><td><a href="https://639808785-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8U6cm8NzMKDuV19vWMfb%2Fuploads%2FRHB8cumjHfdIjNGPoPEP%2FGitHub.png?alt=media&#x26;token=75a65570-745d-4778-8eef-a5629124b1bc">GitHub.png</a></td><td><a href="enterprise-self-hosted/3.-index-your-codebase/github">github</a></td></tr><tr><td><h2>GitLab</h2></td><td><a href="https://639808785-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8U6cm8NzMKDuV19vWMfb%2Fuploads%2FPQ0UbuMBUMHB9AbFsGND%2FGitLab.png?alt=media&#x26;token=cb62723d-685e-41c9-8c88-ab61af6ad0d5">GitLab.png</a></td><td><a href="enterprise-self-hosted/3.-index-your-codebase/gitlab">gitlab</a></td></tr><tr><td><h2>Bitbucket</h2></td><td><a href="https://639808785-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8U6cm8NzMKDuV19vWMfb%2Fuploads%2FD3zNFlJruOafj7xyZyWA%2FBitbucket.png?alt=media&#x26;token=59f3b5bc-3f41-4d40-8f63-1a0bb7774721">Bitbucket.png</a></td><td><a href="enterprise-self-hosted/3.-index-your-codebase/bitbucket-data-center">bitbucket-data-center</a></td></tr><tr><td><h2>On Prem</h2></td><td><a href="https://639808785-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8U6cm8NzMKDuV19vWMfb%2Fuploads%2FjUtwpnFqKt3GnbGdWI5v%2Fqodo%20Management%20Portal.png?alt=media&#x26;token=ce18e4e3-e3b4-4718-ac94-884d35ed2a80">qodo Management Portal.png</a></td><td><a href="https://docs.qodo.ai/qodo-documentation/on-prem/qodo-aware/setup-qodo-aware">https://docs.qodo.ai/qodo-documentation/on-prem/qodo-aware/setup-qodo-aware</a></td></tr><tr><td><h2>Gerrit</h2></td><td><a href="https://639808785-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8U6cm8NzMKDuV19vWMfb%2Fuploads%2FAn7DexaDgn2IbbRC3AYF%2FGerrit.png?alt=media&#x26;token=8d3d5ecb-24ab-40c0-a78b-11b0614b8377">Gerrit.png</a></td><td><a href="enterprise-self-hosted/3.-index-your-codebase/gerrit">gerrit</a></td></tr></tbody></table>
