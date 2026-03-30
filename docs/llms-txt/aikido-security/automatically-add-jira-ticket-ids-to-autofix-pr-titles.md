# Source: https://help.aikido.dev/aikido-autofix/configure/automatically-add-jira-ticket-ids-to-autofix-pr-titles.md

# Automatically Add Jira Ticket IDs to AutoFix PR Titles

## What is it?

Enable autofix PRs in Aikido to automatically include Jira ticket references in the title, with full Jira integration depending on your SCM.

Aikido’s autofix feature can insert Jira ticket IDs into PR titles using `$TASK_REF`, streamlining traceability between security fixes and issue tracking.

{% hint style="info" %}
`$TASK_REF` can be used in **PR titles**, **Branch Prefix** and **Commit Messages**
{% endhint %}

## Use cases

* Improve visibility of security fixes in Jira by auto-linking PRs.
* Ensure each autofix PR is associated with the correct Jira ticket.
* Enable clickable references between PRs and Jira tickets across your SCM

## How to Enable

**GitHub → Jira**

**Step 1:** Install [**GitHub for Jira**](https://github.com/marketplace/jira-software-github) from the GitHub Marketplace.

**Step 2:** Grant access to the repositories you want linked.

**Step 3:** In Jira Cloud:

* Go to **Apps → Manage apps → GitHub for Jira → Configure**.
* Connect to your GitHub organization.

**Step 4:** In Aikido, use `$TASK_REF` in your PR title config.

**Step 5:** Jira ticket keys:

* Show as clickable links in Jira.
* Appear in GitHub’s UI (clickable when viewed in Jira).

***

**GitLab → Jira**

**Step 1:** In GitLab:

* Go to your project → **Settings → Integrations → Jira**.
* Fill in:
  * **Jira URL**: `https://yourcompany.atlassian.net`
  * **Username**: Your Atlassian email
  * **Password/API Token**: Generate from your Atlassian account

**Step 2:** Save the integration.

**Step 3:** In Aikido, use `$TASK_REF` in your PR title config.

**Step 4:** Jira ticket keys:

* Auto-link in GitLab UI.
* Update Jira’s development panel.

***

**Bitbucket → Jira (Cloud)**

**Step 1:** In Bitbucket Cloud:

* Go to **Settings → Linked repositories → Link Jira project**.
* Sign in to your Atlassian account and select the Jira project.

**Step 2:** In Aikido, use `$TASK_REF` in your PR title config.

**Step 3:** Jira ticket keys:

* Auto-link in Bitbucket UI.
* Appear in Jira’s development info panel.

***

**Azure DevOps → Jira**

**Step 1:** Install a connector between Azure DevOps and Jira, such as:

* TFS4JIRA
* [Git Integration for Jira](https://marketplace.atlassian.com/apps/4984/git-integration-for-jira-azure-devops-github-gitlab)
* Exalate

**Step 2:** Authorize both Azure DevOps and Jira accounts in the chosen connector.

**Step 3:** Configure the connector to recognize ticket patterns (e.g. `ABC-\d+`).

**Step 4:** In Aikido, use `$TASK_REF` in your PR title config.

**Step 5:** Jira ticket keys:

* Link PRs to Jira and appear in the Jira development panel.
