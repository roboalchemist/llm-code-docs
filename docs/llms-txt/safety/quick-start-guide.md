# Source: https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/quick-start-guide.md

# Quick Start Guide

Running your first scan using Safety CLI takes less than a minute and can be performed via our  [Command Line Interface](#command-line-interface) or through the [GitHub Action](#github-action) .  Below we detail [1. Installation](#id-1.-installation), [2. Authentication](#id-2.-log-in-or-register), and [3. Running your first scan](#id-3.-running-your-first-scan).

To learn more about upgrading from Safety 2.x to Safety CLI please check out our [Migration guide](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/migrating-from-safety-cli-2.x-to-safety-cli-3.x).

## Command Line Interface

## 1. Installation

Begin by installing Safety on your development machine.

1. Open your Terminal
2. Run the following command to install:

```
pip install safety
```

{% hint style="info" %}
If you already have Safety installed, please use `pip install -U safety`&#x20;
{% endhint %}

## 2. Log In or Register

1\. Once installed, try to run your first scan using the following command:&#x20;

```
safety scan
```

2\. If you are already logged in, Safety will perform the scan. If you are not already authenticated, Safety CLI will prompt you to [create an account](https://platform.safetycli.com/register/) or [log in](https://platform.safetycli.com/login/) using existing credentials.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FUfzkaeezbhMsGsBCwzqU%2FAuth%20Step%201.gif?alt=media&#x26;token=26ee156c-5ef6-40ab-8449-f48aef15d88b" alt=""><figcaption></figcaption></figure>

In both cases, a browser window will open with clear instructions on how to log in or create a new account. Once logged in, Safety CLI will show that you are authenticated and can proceed with the next step.

{% hint style="warning" %}
You will be unable to perform vulnerability scans unless you are authenticated. [Create an account and access your free trial here. ](https://platform.safetycli.com/register/)If you require assistance, please email <support@safetycli.com>.
{% endhint %}

{% hint style="info" %}
To check your authentication status, you can run **`safety auth`** at any time.&#x20;
{% endhint %}

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F6hD5zET5qM5jOBO41OX7%2Fimage.png?alt=media&#x26;token=c66aeb22-16aa-4fc7-9a4a-98da66c8857f" alt="" width="563"><figcaption><p>Safety CLI after Successful Authentication</p></figcaption></figure>

## 3. Running Your First Scan

1. Using the Terminal, navigate to a project, e.g. `cd my/project/`. (This root folder would normally contain files such as `composer.lock`, `requirements.txt`, `READMEs`, `Pipfile.lock`,  `pyproject.toml`, `.gitignores` etc.)
2. Run the **`safety scan`** command.
3. Safety will now perform a scan of the current project directory, detecting all Python installations and requirements files. The output of the scan will be presented in the Terminal window.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FH0vrNDq570gOzOTBTt04%2Fsafety_scan_S_white.gif?alt=media&#x26;token=d634310e-1501-4fb7-8b9e-649aa307e050" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Performing scans across entire development machines and in CI/CD**

Detailed documentation on how to integrate Safety with other tools, perform system-wide scans, and more are available via the links to the left.
{% endhint %}

#### Jupyter Notebook Quickstart

For users who prefer a more interactive environment, we also provide a Jupyter Notebook Quickstart guide. This notebook offers step-by-step instructions for running Safety CLI within a Jupyter environment, making it easier to explore the functionality and perform your first scan in a familiar interface.

You can access the quickstart notebook here: [Jupyter Notebook Quickstart](https://github.com/pyupio/safety/blob/main/docs/Safety-CLI-Quickstart.ipynb).

## Basic Commands

The following are the most commonly used commands. [A full glossary of available commands can be found here](https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/available-commands-and-inputs).

* **`safety --help`** accesses Help and displays all available commands, utility commands, and options.
* **`safety auth`** starts the authentication flow if not logged in and displays authentication status if logged in.
* **`safety scan`** performs a vulnerability scan in the current directory.
* **`safety system-scan`** performs a vulnerability scan across the entire development machine.
* `safety scan --apply-fixes` performs a scan and automatically updates vulnerable dependencies to the next secure version.

{% hint style="info" %}
**Enterprise Customers:**

* Your organization may require installation to be performed via approved software bundles.&#x20;
* If your organization leverages SAML-based authentication, you will be prompted to enter your corporate login credentials at the authentication stage.&#x20;

If you are unsure whether your organization uses either of these options, please contact your administrator or email <support@safetycli.com>.
{% endhint %}

## GitHub Action

The quickest way to test Safety CLI in CI/CD is by using our [GitHub Action](https://github.com/pyupio/safety-actions), new in Safety CLI. Full [documentation on the GitHub Action](https://docs.safetycli.com/safety-docs/installation/github-actions) is available here:

[github-actions](https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github/github-actions "mention")

If you require assistance, please email <support@safetycli.com>.
