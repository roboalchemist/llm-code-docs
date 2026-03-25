# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/github-enterprise.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/github-enterprise.md

# GitHub Enterprise

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

Learn more on how to setup Qodo on GitHub Enterprise.

## Before you start <a href="#github-cloud" id="github-cloud"></a>

When setting up Qodo on GitHub Enterprise, expect a straightforward configuration with an extra focus on secure enterprise environments.

You can install it on one project to start or across multiple repositories for organization-wide adoption.

The setup usually takes a few minutes, depending on your environment.

Once installed, Qodo will automatically process your pull requests and post actionable output—such as reviews, summaries, or improvements—right in your Enterprise PRs.

***

## 1. Log In to Qodo Portal <a href="#github-cloud" id="github-cloud"></a>

Before setting up Qodo, make sure to [create a Qodo account and sign in](https://app.qodo.ai/signin).

Once you've signed in to the Qodo Portal, you can follow the [Qodo Git plugin installation guide](https://app.qodo.ai/qodo-merge/installation) straight from the portal, or continue reading here.

## 2. Setup Qodo

Once you've signed in to your [Qodo account](https://app.qodo.ai/signin), follow the instructions in the [Qodo Portal](https://app.qodo.ai/qodo-merge/installation) or below to setup Qodo on GitHub Enterprise.

### GitHub Enterprise Server <a href="#github-enterprise-server" id="github-enterprise-server"></a>

{% hint style="success" %}
[**Contact Qodo**](https://www.qodo.ai/contact/#pricing) **to use Qodo Git** interface **on your private GitHub Enterprise Server.**

Enterprise server requires single tenant or On Prem registration with Qodo.
{% endhint %}

#### Action for GitHub enterprise server <a href="#action-for-github-enterprise-server" id="action-for-github-enterprise-server"></a>

To use the action with a GitHub enterprise server, add an environment variable `GITHUB.BASE_URL` with the API URL of your GitHub server.

For example, if your GitHub server is at `https://github.mycompany.com`, add the following to your workflow file:

```
      env:
        # ... previous environment values
        GITHUB.BASE_URL: "https://github.mycompany.com/api/v3"
```
