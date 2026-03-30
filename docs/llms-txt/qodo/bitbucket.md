# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/bitbucket.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/bitbucket.md

# Bitbucket

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

Learn more on how to setup Qodo on Bitbucket.

## Before you start <a href="#github-cloud" id="github-cloud"></a>

Integrating Qodo with Bitbucket is a simple process that can be applied to one repository or scaled to multiple workspaces.

Setup usually takes a few minutes, including authentication and pipeline configuration.

Once connected, Qodo will process your pull requests automatically and provide reviews, summaries, or improvement suggestions as part of your Bitbucket workflow.

***

## 1. Log In to Qodo Portal <a href="#github-cloud" id="github-cloud"></a>

Before setting up Qodo, make sure to [create a Qodo account and sign in](https://app.qodo.ai/signin).

Once you've signed in to the Qodo Portal, you can follow the [Qodo Merge installation guide](https://app.qodo.ai/qodo-merge/installation) straight from the portal, or continue reading here.

## 2. Setup Qodo

Once you've signed in to your [Qodo account](https://app.qodo.ai/signin), follow the instructions in the [Qodo Portal](https://app.qodo.ai/qodo-merge/installation) or below to setup Qodo on Bitbucket.

### Bitbucket App <a href="#run-as-a-bitbucket-pipeline" id="run-as-a-bitbucket-pipeline"></a>

{% hint style="success" %}
**This installation method is available to subscribed users only.**

Visit [Qodo's Plans page](https://www.qodo.ai/pricing/) to learn more.
{% endhint %}

1. Go to Go to the [Qodo Git plugin Pro app page](https://bitbucket.org/site/addons/authorize?addon_key=d6df813252c37258).
2. Choose which workspace Qodo should have access to, then click **Grant access**.

### Bitbucket Server <a href="#bitbucket-server" id="bitbucket-server"></a>

{% hint style="success" %}
[**Contact Qodo**](https://www.qodo.ai/contact/#pricing) **to use Qodo Git interface on your private Bitbucket Server.**
{% endhint %}

### Bitbucket Pipeline <a href="#run-as-a-bitbucket-pipeline" id="run-as-a-bitbucket-pipeline"></a>

1. **Create a pipelines file:** Create a new file named `bitbucket-pipelines.yml` with the content below:&#x20;

```yaml
pipelines:
    pull-requests:
      '**':
        - step:
            name: PR Agent Review
            image: codiumai/pr-agent:latest
            script:
              - pr-agent --pr_url=https://bitbucket.org/$BITBUCKET_WORKSPACE/$BITBUCKET_REPO_SLUG/pull-requests/$BITBUCKET_PR_ID review
```

2. **Choose your authentication type:** You could choose either `basic` or `bearer`.&#x20;
   * `bearer` = just a token (more secure, no username/password exposure).
   * `basic` = username + password (or app password) combined and encoded.
3. **Create a token:** Based on your authentication type, create a token.
   * **If your authentication type is `bearer`**, generate an access token for your Bitbucket repository:
     1. Go to your repository's settings.
     2. Choose **Secutiry** then **Access Tokens**.
     3. Generate an access token and save it somewhere safe.
   * **If your authentication type is `basic`**, generate a `base64` encoded token from your `username:password` combination and save it somewhere safe.
4. **Add secure variables:** Go to your repository's settings. Choose **Pipelines**. Under **Repository variables**, add the following variables:
   * &#x20;**OPENAI\_API\_KEY:** `<your key>`
   * **BITBUCKET.AUTH\_TYPE:** `basic` or `bearer` (default is `bearer`)
   * **BITBUCKET\_\_BEARER\_TOKEN** or **BITBUCKET.BASIC\_TOKEN:** `<your token>` (obtained from step 3)

**You’re all set!** Start using Qodo

{% hint style="info" %}
[Visit our usage guide](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide) for next steps.
{% endhint %}

{% hint style="warning" %}
**Note:** Comments on a PR **are not supported** in Bitbucket Pipeline.
{% endhint %}
