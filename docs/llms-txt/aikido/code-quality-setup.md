# Source: https://help.aikido.dev/code-quality/code-quality-setup.md

# Code Quality Setup

{% hint style="info" %}
Code Quality currently works by adding comments on newly introduced PRs.&#x20;
{% endhint %}

Code Quality helps you maintain high standards across your codebase by automatically reviewing pull requests for common issues, best practices, and team-specific guidelines. This guide walks you through setting up Code Quality in your PR / MR Checks.

## Prerequisites

Before you begin, ensure you have:

* An account connected to GitHub, Bitbucket, Gitlab or Azdo. **No support for Local Scanning Accounts.**
* Admin access to your Aikido account
* [Connected repositories to Aikido](https://help.aikido.dev/code-scanning/connect-your-source-code)

## Getting started <a href="#getting-started" id="getting-started"></a>

There are 3 steps in total to setup and run your first code quality steps. The Aikido UI shows clearly which steps to follow on the Code Quality page (accessible from sidebar). Below is a more extensive description.

{% stepper %}
{% step %}

### Enable Code Quality for repositories

Choose which repositories should have Code Quality checks enabled:

1. Click **Configure Repositories** on the Code Quality Page to open the PR checks page. If you haven't configured the CI checks yet, you will be taken through the installation flow.
2. Select the repositories where you want to run code quality checks and enable the Code Quality functionality (on the bottom) in the modal. You can choose whether you just want to add comments or also fail the gate.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FyAFgSyMljg19z8y8Bixw%2Fimage.png?alt=media&#x26;token=1a59e52e-32af-438b-a11a-b84c4c42a54d" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Select quality checks

Configure which code quality rules to enforce on the Code Quality Checks page

1. Browse through the available checks organized by:
   * **Default checks** - Pre-configured best practices for multiple languages
   * **Custom checks** - Rules specific to your team (you can add these later)
2. Toggle checks on/off based on your team’s needs

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fq4mHA6XkYQpZjLqs9TXn%2Fimage.png?alt=media&#x26;token=ae37ff36-0998-4b75-91bc-5c90d1207bfc" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Run your first scan

Once you’ve configured repositories and checks:

1. Create a new pull request, or push a new commit to an existing pull request in one of the configured repositories. This will automatically trigger your first Code Quality scan.
2. Review the results in the **Activity** tab.
   {% endstep %}
   {% endstepper %}
