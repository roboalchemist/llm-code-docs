# Source: https://docs.port.io/guides/all/setup-pr-enricher-ai-agent.md

# Set up the Pull Request Enricher AI agent

## Overview[â](#overview "Direct link to Overview")

This guide will walk you through setting up a "Pull Request Enricher" AI agent in Port.<br /><!-- -->By the end of this guide, your developers will receive automated, contextual comments on their pull requests to help streamline the review process.

![PR Enricher AI Agent GitHub comment example](/img/ai-agents/AIAgentPREnrichierGitHubComment.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Automatically comment on new pull requests with assessments based on PR metadata.
* Highlight potential areas of concern.
* Provide context from related Jira tickets directly in the PR comments.
* Suggest relevant reviewers based on code changes.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes you have:

* A Port account with the [AI agents feature enabled](/ai-interfaces/ai-agents/overview.md#access-to-the-feature).
* Appropriate permissions to create and configure AI agents.
* [GitHub integration](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) configured in your Port instance.
* [Jira integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md) configured in your Port instance.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

First, we'll need to create the Pull Request Enricher AI agent in Port.<br /><!-- -->We will need to configure:

* The data sources it will use to analyze pull requests.
* The agent configuration that defines its capabilities.
* An automation to trigger the agent when new pull requests are opened.

### Configure data source access[â](#configure-data-source-access "Direct link to Configure data source access")

For this guide, we will be using **GitHub** as our data source to provide comprehensive pull request analysis capabilities. Make sure you have [Port's GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) installed and configured.

Additional data sources

While this guide uses GitHub, you can enhance the agent's capabilities by adding other data sources like:

* PagerDuty for checking active incidents.
* Your software catalog services for broader context.

### Create the agent configuration[â](#create-the-agent-configuration "Direct link to Create the agent configuration")

1. Go to the [AI Agents](https://app.getport.io/_ai_agents) page of your portal.

2. Click on `+ AI Agent`.

3. Toggle `Json mode` on.

4. Copy and paste the following JSON schema:

   **Pull Request Enricher agent configuration (Click to expand)**

   ```
   {
     "identifier": "pr_assistant_ai_agent",
     "title": "PR Review Assistant",
     "description": "AI agent that analyzes pull requests and provides helpful context for reviewers",
     "icon": "Pipeline",
     "properties": {
       "description": "Comment on open PRs with additional context to assist developers",
       "status": "active",
       "allowed_blueprints": [
         "githubPullRequest",
         "githubRepository",
         "githubUser",
         "jiraIssue",
         "_user",
         "_team"
       ],
       "prompt": "Analyze pull request details and provide a structured review in the following format:\n\nPR Description:\n Summarize the PR description and key properties in one sentence \n\nKey Points:\n{{ List up to 3 key insights about the changes }}\n\nObservations:\nProvide up to 3 observations using ð¢ for low risk, ð¡ for medium risk, and ð´ for high risk\n\nRecommendations:\nList up to 3 optional recommendations for improvement.provide this in markdown form",
       "execution_mode": "Automatic"
     }
   }
   ```

5. Click on `Create` to save the agent.

### Create the automations[â](#create-the-automations "Direct link to Create the automations")

We will need two automations:

1. One to trigger the AI agent when a PR is opened.
2. Another to post the agent's response as a comment.

#### Trigger PR enricher AI agent[â](#trigger-pr-enricher-ai-agent "Direct link to Trigger PR enricher AI agent")

1. Go to the [Automations](https://app.getport.io/automations) page.

2. Click on `+ Automation`.

3. Copy and paste the following JSON schema:

   **PR Enricher agent trigger automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "pr_opened_to_agent",
     "title": "Upon PR opened, trigger PR Assistant",
     "description": "Automation to trigger PR Assistant when a new PR is opened",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_CREATED",
         "blueprintIdentifier": "githubPullRequest"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".diff.after.properties.status == \"open\""
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.port.io/v1/agent/pr_assistant_ai_agent/invoke",
       "synchronized": true,
       "body": {
         "prompt": "Analyze pull request with entity identifier '{{ .event.diff.after.identifier }}'",
         "labels": {
           "source": "Automation",
           "prNumber": "{{ .event.diff.after.properties.prNumber | tostring }}",
           "repo": "{{ (.event.diff.after.properties.link | tostring | split(\"/\"))[3] + \"/\" + ((.event.diff.after.properties.link | tostring | split(\"/\"))[4]) }}"
         }
       }
     },
     "publish": true
   }
   ```

4. Click on `Create` to save the automation.

#### Post PR enricher AI agent response on GitHub[â](#post-pr-enricher-ai-agent-response-on-github "Direct link to Post PR enricher AI agent response on GitHub")

This automation requires a GitHub Personal Access Token (PAT) with `repo` scope to post comments on pull requests.<br /><!-- -->Store this token as a secret in Port.

1. **Create GitHub PAT:**<br /><!-- -->Follow GitHub's guide to [create a fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) with **Read and Write** permissions for **Pull requests** for the repositories you want the agent to comment on.

2. **Add Secret to Port:**

   * Click on the `...` button in the top right corner of your Port application.
   * Click on **Credentials**.
   * Click on the `Secrets` tab.
   * Click on `+ Secret` and add the following secret:
     <!-- -->
     * `GITHUB_TOKEN` - Your GitHub Personal Access Token.

3. Go back to the [Automations](https://app.getport.io/automations) page.

4. Click on `+ Automation`.

5. Copy and paste the following JSON schema:

   **Post PR comment from agent response automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "post_pr_comment",
     "title": "Post PR comment from agent response",
     "description": "Automation to post the agent's response as a PR comment",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_CREATED",
         "blueprintIdentifier": "_ai_invocations"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".event.diff.after.relations.agent == \"pr_assistant_ai_agent\"",
           ".event.diff.after.properties.status == \"Completed\""
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.github.com/repos/<YOUR_GITHUB_ORG>/<YOUR_GITHUB_REPO>/actions/workflows/post-pr-comment.yml/dispatches",
       "method": "POST",
       "headers": {
         "Accept": "application/vnd.github+json",
         "Authorization": "Bearer {{ .secrets.GITHUB_TOKEN }}",
         "Content-Type": "application/json"
       },
       "body": {
         "ref": "main",
         "inputs": {
           "comment": "{{ .event.diff.after.properties.response }}",
           "pr": "{{ .event.diff.after.properties.labels.prNumber }}",
           "repo": "{{ .event.diff.after.properties.labels.repo }}"
         }
       }
     },
     "publish": true
   }
   ```

   Replace placeholders

   Make sure to replace 'YOUR\_GITHUB\_ORG' and 'YOUR\_GITHUB\_REPO' in the `url` field above with the actual organization and repository where your `post-pr-comment.yml` workflow resides.

6. Click on `Create` to save the automation.

### Create the GitHub workflow[â](#create-the-github-workflow "Direct link to Create the GitHub workflow")

Now let's create the workflow file that contains the logic to post the comment.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

Choose the authentication method that best fits your setup:

* Personal access token
* GitHub app

This approach uses your personal GitHub account to comment on pull requests. It's simpler to set up but comments will appear from your personal account.

In your dedicated workflow repository, ensure you have a `.github/workflows` directory.

1. Create a new file named `post-pr-comment.yml`.

2. Copy and paste the following snippet:

   **Post PR comment workflow using PAT (Click to expand)**

   ```
   name: Comment on PR

   on:
     workflow_dispatch:
       inputs:
         comment:
           description: 'The comment text to post'
           required: true
           type: string
         repo:
           description: 'Repository in "owner/repo" format (e.g., port-labs/puddle-integrations)'
           required: true
           type: string
         pr:
           description: 'Pull request number'
           required: true
           type: string

   jobs:
     comment:
       runs-on: ubuntu-latest
       steps:
         - name: Comment on PR using PAT
           env:
             GITHUB_TOKEN: ${{ secrets.COMMENT_ON_PR_TOKEN }}
             COMMENT: ${{ github.event.inputs.comment }}
             REPO: ${{ github.event.inputs.repo }}
             PR_NUMBER: ${{ github.event.inputs.pr }}
           run: |
             # Split repo into owner and name
             OWNER=$(echo "$REPO" | cut -d'/' -f1)
             REPO_NAME=$(echo "$REPO" | cut -d'/' -f2)
             
             # Post comment to PR using GitHub CLI
             echo "$COMMENT" | gh pr comment "$PR_NUMBER" --repo "$OWNER/$REPO_NAME" --body-file -
   ```

   Required GitHub Secrets

   For this workflow to function properly, you need to add the following secret to your GitHub repository:

   * `COMMENT_ON_PR_TOKEN`: Your Personal Access Token with **Read and Write** permissions for **Pull requests**. Follow [GitHub's guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) to create one.

3. Commit and push the changes to your repository.

This approach uses a GitHub App to comment on pull requests. Comments will appear from the app's account, providing a more professional and centralized approach.

In your dedicated workflow repository, ensure you have a `.github/workflows` directory.

1. Create a new file named `post-pr-comment.yml`.

2. Copy and paste the following snippet:

   **Post PR comment workflow using GitHub App (Click to expand)**

   ```
   name: Comment on PR

   on:
     workflow_dispatch:
       inputs:
         comment:
           description: 'The comment text to post'
           required: true
           type: string
         repo:
           description: 'Repository in "owner/repo" format (e.g., port-labs/puddle-integrations)'
           required: true
           type: string
         pr:
           description: 'Pull request number'
           required: true
           type: string

   jobs:
     comment:
       runs-on: ubuntu-latest
       steps:
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.x'

         - name: Install Python dependencies
           run: |
             pip install PyJWT requests cryptography

         - name: Comment on PR using GitHub App
           env:
             PEM: ${{ secrets.PORT_GITHUB_APP_PEM }}
             APP_ID: ${{ secrets.PORT_GITHUB_APP_ID }}
             INSTALLATION_ID: ${{ secrets.PORT_GITHUB_APP_INSTALLATION_ID }}
             COMMENT: ${{ github.event.inputs.comment }}
             REPO: ${{ github.event.inputs.repo }}
             PR_NUMBER: ${{ github.event.inputs.pr }}
           run: |
             python - <<'EOF'
             import os, time, jwt, requests

             # Load environment variables
             pem = os.environ['PEM']
             app_id = os.environ['APP_ID']
             installation_id = os.environ['INSTALLATION_ID']
             comment = os.environ['COMMENT']
             repo = os.environ['REPO']
             pr_number = os.environ['PR_NUMBER']

             # Generate JWT (valid for 10 minutes)
             now = int(time.time())
             payload = {
                 'iat': now - 60,
                 'exp': now + (10 * 60),
                 'iss': app_id
             }
             jwt_token = jwt.encode(payload, pem, algorithm='RS256')

             # Obtain an installation access token
             headers = {
                 'Authorization': f'Bearer {jwt_token}',
                 'Accept': 'application/vnd.github+json'
             }
             token_url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
             resp = requests.post(token_url, headers=headers)
             resp.raise_for_status()
             token = resp.json()['token']

             # Comment on the pull request (PRs are issues in GitHub API)
             owner, repo_name = repo.split('/')
             comment_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{pr_number}/comments"
             comment_payload = {"body": comment}
             headers = {
                 'Authorization': f'Bearer {token}',
                 'Accept': 'application/vnd.github.v3+json',
                 'Content-Type': 'application/json'
             }
             resp = requests.post(comment_url, headers=headers, json=comment_payload)
             resp.raise_for_status()
             print("Comment posted successfully!")
             EOF
   ```

   Required GitHub Secrets

   For this workflow to function properly, you need to add the following secrets to your GitHub repository:

   * `PORT_GITHUB_APP_PEM`: The private key of your GitHub App in PEM format.
   * `PORT_GITHUB_APP_ID`: The App ID of your GitHub App.
   * `PORT_GITHUB_APP_INSTALLATION_ID`: The installation ID of your GitHub App in this repository.

3. Commit and push the changes to your repository.

Choosing the right approach

* **Personal Access Token**: Simpler setup, comments appear from your personal account, suitable for smaller teams or personal projects.
* **GitHub App**: More professional, comments appear from a dedicated app account, better for larger organizations and provides more granular permissions.

## Example response[â](#example-response "Direct link to Example response")

The PR Enricher agent will automatically comment on new pull requests with information like:

```
## Pull Request Review: Feature/Payment Gateway Integration

### PR Details
This PR implements Stripe payment processing with 3D Secure authentication and adds feature flags for gradual rollout. Created by Alex Chen from the payments team.

### PR Description
This pull request introduces a new payment gateway integration with Stripe, enabling secure credit card processing with 3D Secure authentication and compliance with PCI-DSS requirements.

### Key Points
1. Adds a new `PaymentService` that implements the payment gateway interface with Stripe-specific logic.
2. Includes comprehensive error handling for payment failures, network issues, and fraud detection.
3. Adds feature flags to gradually roll out the payment system to different user segments.

### Observations
- **Security Impact**: ð´ Handles sensitive payment information requiring thorough security review and PCI compliance verification.
- **Test Coverage**: ð¡ Integration tests with Stripe's test environment included, but mock tests for failure scenarios need expansion.
- **Performance**: ð¢ Initial load testing shows payment processing completes in <200ms for 99% of transactions.

### Recommendations
- **Security Review**: Request dedicated review from security team to verify proper handling of payment tokens and credentials.
- **Documentation**: Add detailed documentation about the Stripe integration configuration and failure handling for on-call engineers.
- **Monitoring**: Consider adding additional logging and alerting for payment failures to quickly identify issues in production.

*This integration significantly expands our payment capabilities while maintaining our security standards. The feature flags provide a safe rollout strategy.*
```

## Best practices[â](#best-practices "Direct link to Best practices")

To get the most out of your PR Enricher agent:

1. **Ensure PR-Jira Linking**: Verify that your Port setup correctly establishes relations between `githubPullRequest` entities and `jiraIssue` entities.

2. **Start with basic assessment**: Begin with simple risk assessment and gradually add more context as you see how the agent performs.

3. **Monitor responses**: Regularly review the agent's comments to ensure they're helpful and accurate.

4. **Iterate on the prompt**: Refine the prompt based on the quality of responses and specific needs of your team.

5. **Test the workflow**: Create test pull requests to verify the entire flow works as expected.

6. **Troubleshoot**: If you're not getting the expected results, check our [troubleshooting guide](/ai-interfaces/ai-agents/interact-with-ai-agents.md#troubleshooting--faq) for common issues and solutions.

## Possible enhancements[â](#possible-enhancements "Direct link to Possible enhancements")

You can further enhance the PR Enricher setup by:

* **Adding more data sources** like PagerDuty for incident context or [additional Git providers](/ai-interfaces/ai-agents/build-an-ai-agent.md#step-2-configure-data-access-tools) for broader repository visibility.
* **Configuring automated actions** such as [reviewer assignment, PR labeling, or creating follow-up Jira tickets](/ai-interfaces/ai-agents/interact-with-ai-agents.md#interaction-methods).
* **Customizing risk assessment criteria** to align with your organization's specific guidelines and [monitoring usage patterns](/ai-interfaces/ai-agents/interact-with-ai-agents.md#ai-interaction-details).
