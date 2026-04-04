# Source: https://docs.port.io/guides/all/auto-approve-and-merge-dependabot-prs.md

# Auto approve and merge Dependabot PRs

This guide demonstrates how to set up an automation in Port that approves GitHub pull requests created by Dependabot. By doing so, engineering teams can effortlessly keep dependencies up to date and quickly apply security patches without manual overhead.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) is installed in your account.

## Set up automation[â](#set-up-automation "Direct link to Set up automation")

Once the GitHub pull request entities are synced to your catalog, you can configure an automation in Port that triggers a GitHub workflow to approve and merge the pull request.

This setup involves two parts:

1. Adding a GitHub PAT as a Port secret.

2. Defining the automation in Port.

### Add Port secrets[â](#add-port-secrets "Direct link to Add Port secrets")

To add a secret to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secrets:

   * `GITHUB_TOKEN` - A [GitHub Personal Access Token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) with **repo** and **workflow** scopes.

### Define automation backend[â](#define-automation-backend "Direct link to Define automation backend")

1. Go to the [Automations](https://app.getport.io/settings/automations) page in your portal.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration into the editor:

   **Auto merge and approve PR automation (Click to expand)**

   Replace placeholders

   Make sure to replace `<YOUR_GITHUB_ORG>` and `<YOUR_GITHUB_REPO>` in the url field below with the actual organization and repository where your `approve-and-merge-dependabot-pr.yaml` workflow resides.

   Create in Port

   ```
   {
       "identifier": "approveAndMergeDependabotPR",
       "title": "Approve and Merge Dependabot PR",
       "description": "Automation to approve and merge dependabot pull requests",
       "trigger": {
           "type": "automation",
           "event": {
           "type": "ENTITY_UPDATED",
           "blueprintIdentifier": "githubPullRequest"
           },
           "condition": {
           "type": "JQ",
           "expressions": [
               ".diff.after.properties.creator | test(\"dependabot\") == true",
               ".diff.after.properties.status != \"merged\""
           ],
           "combinator": "and"
           }
       },
       "invocationMethod": {
           "type": "WEBHOOK",
           "url": "https://api.github.com/repos/<YOUR_GITHUB_ORG>/<YOUR_GITHUB_REPO>/actions/workflows/approve-and-merge-dependabot-pr.yaml/dispatches",
           "method": "POST",
           "headers": {
           "Accept": "application/vnd.github+json",
           "Authorization": "Bearer {{ .secrets.GITHUB_TOKEN }}",
           "Content-Type": "application/json"
           },
           "body": {
           "ref": "main",
           "inputs": {
               "prNumber": "{{ .event.diff.after.properties.prNumber | tostring }}",
               "repository": "{{ .event.diff.after.relations.repository }}",
               "runID": "{{ .run.id }}"
           }
           }
       },
       "publish": true
   }
   ```

4. Click `Save`.

### Create the GitHub workflow[â](#create-the-github-workflow "Direct link to Create the GitHub workflow")

We will now define the GitHub Actions workflow that processes the input and executes the necessary steps to achieve the desired outcome.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

In your dedicated workflow repository, ensure you have a `.github/workflows` directory.

1. Create a new file named `approve-and-merge-dependabot-pr.yaml`

2. Copy and paste the following workflow configuration:

   **Approve and merge Dependabot PR workflow (Click to expand)**

   ```

   name: Auto-Approve & Merge Dependabot PR

   on:
     workflow_dispatch:
       inputs:
         prNumber:
           required: true
           type: string
         repository:
           required: true
           type: string
         runID:
           required: true
           type: string

   jobs:
     approve_and_merge:
       runs-on: ubuntu-latest
       env:
         GH_TOKEN: ${{ secrets.MY_GITHUB_TOKEN }}

       steps:
         - name: Checkout
           uses: actions/checkout@v4

         - name: Fetch Port Access Token
           id: fetch_port_token
           run: |
             PORT_ACCESS_TOKEN=$(curl -s -L 'https://api.port.io/v1/auth/access_token' \
               -H 'Content-Type: application/json' \
               -H 'Accept: application/json' \
               -d '{
                 "clientId": "${{ secrets.PORT_CLIENT_ID }}",
                 "clientSecret": "${{ secrets.PORT_CLIENT_SECRET }}"
               }' | jq -r '.accessToken')
             echo "PORT_ACCESS_TOKEN=$PORT_ACCESS_TOKEN" >> "$GITHUB_ENV"
             
         - name: Extract PR Info
           id: pr_info
           run: |
             repo="${{ github.event.inputs.repository }}"
             pr_number=$(echo "${{ github.event.inputs.prNumber }}" | grep -o '[0-9]\+$')
             echo "repo=$repo" >> $GITHUB_ENV
             echo "pr_number=$pr_number" >> $GITHUB_ENV

         - name: Approve Pull Request
           run: |
             echo "â Approving PR #$pr_number in $repo"
             curl -s -X POST \
               -H "Authorization: Bearer $GH_TOKEN" \
               -H "Accept: application/vnd.github+json" \
               https://api.github.com/repos/${{ github.repository_owner }}/$repo/pulls/$pr_number/reviews \
               -d '{"event":"APPROVE"}'

         - name: Ensure "approved-dependabot" label exists
           run: |
             label_name="approved-dependabot"
             label_color="2cbe4e"
             echo "ð·ï¸ Ensuring label '$label_name' exists..."
             curl -s -o /dev/null -w "%{http_code}" -X POST \
               https://api.github.com/repos/${{ github.repository_owner }}/$repo/labels \
               -H "Authorization: Bearer $GH_TOKEN" \
               -H "Accept: application/vnd.github+json" \
               -d "{\"name\": \"$label_name\", \"color\": \"$label_color\"}" | grep -qE "201|422"

         - name: Apply Label to PR
           run: |
             echo "ð·ï¸ Applying label to PR #$pr_number..."
             curl -s -X POST \
               https://api.github.com/repos/${{ github.repository_owner }}/$repo/issues/$pr_number/labels \
               -H "Authorization: Bearer $GH_TOKEN" \
               -H "Accept: application/vnd.github+json" \
               -d '{"labels": ["approved-dependabot"]}'

         - name: Check PR Mergeability
           id: check_merge
           run: |
             echo "ð Checking mergeability for PR #$pr_number"
             pr_response=$(curl -s -H "Authorization: Bearer $GH_TOKEN" \
               https://api.github.com/repos/${{ github.repository_owner }}/$repo/pulls/$pr_number)
             
             mergeable_state=$(echo "$pr_response" | jq -r '.mergeable_state')
             echo "mergeable_state=$mergeable_state" >> $GITHUB_ENV

         - name: Merge PR (if mergeable)
           if: env.mergeable_state == 'clean'
           id: merge_pr
           run: |
             echo "ð Merging PR #$pr_number"
             curl -s -X PUT \
               -H "Authorization: Bearer $GH_TOKEN" \
               -H "Accept: application/vnd.github+json" \
               https://api.github.com/repos/${{ github.repository_owner }}/$repo/pulls/$pr_number/merge \
               -d '{"merge_method":"squash"}'

         - name: Update Port action status
           if: always()
           run: |
             if [ "${{ steps.merge_pr.outcome }}" == "failure" ]; then
               STATUS="FAILURE"
             else
               STATUS="SUCCESS"
             fi
         
             curl -L -X PATCH "https://api.port.io/v1/actions/runs/${{ github.event.inputs.runID }}" \
             -H "Content-Type: application/json" \
             -H "Accept: application/json" \
             -H "Authorization: Bearer ${{ env.PORT_ACCESS_TOKEN }}" \
             -d '{
               "status": "'"$STATUS"'",
               "statusLabel": "'"$STATUS"'",
               "link": "'"${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}"'",
               "summary": "Dependabot pull request approval and merge completed with status: '"$STATUS"'"
             }'
   ```

   Required GitHub Secrets

   For this workflow to function properly, you need to add the following secrets to your GitHub repository:

   * `PORT_CLIENT_ID`: The client ID of your Port account.
   * `PORT_CLIENT_SECRET`: The client ID of your Port account.
   * `MY_GITHUB_TOKEN`: The fine grained GitHub personal access token with `Read and Write` access to **issues**, **pull requests** across all repositories in your organization.

3. Commit and push the changes to your repository.

When a pull request created by Dependabot is updated, the automation is triggered automatically to approve and merge the PRâensuring a seamless and secure update process.
