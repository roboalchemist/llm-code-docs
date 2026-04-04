# Source: https://www.mintlify.com/docs/guides/automate-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tutorial: Auto-update documentation when code is changed

> Use the agent API to automatically update your documentation.

## What you will build

An automation that updates your documentation when code is pushed to your main branch. The workflow can be built on multiple platforms, including GitHub Actions and n8n. It watches your code repository and then calls the agent API to update your documentation in a separate documentation repository.

This workflow connects two separate repositories:

* **Code repository**: Where you store application code. You'll set up the automation trigger on this repository. Examples include a backend API, frontend app, SDK, or CLI tool.
* **Documentation repository**: Where you store your documentation and connect to your Mintlify project. The agent creates pull requests with documentation updates in this repository.

This tutorial assumes your documentation is in a separate repository from your application code. If you have a monorepo, modify the workflow to target the directory where you store your documentation.

### Workflow overview

1. Someone pushes code to your main branch.
2. The workflow triggers.
3. The workflow calls the agent API to update your documentation.
4. The agent creates a pull request with documentation updates in your documentation repository.

## Choose your platform

<Tabs>
  <Tab title="GitHub Actions">
    GitHub Actions is the simplest option if your code is already on GitHub. No additional services required.

    ## Prerequisites

    * GitHub Actions enabled on your code and documentation repositories
    * [Mintlify GitHub App](/deploy/github) installed in both your code and documentation repositories
    * [Mintlify admin API key](https://dashboard.mintlify.com/settings/organization/api-keys)
    * [Mintlify project ID](https://dashboard.mintlify.com/settings/organization/api-keys)
    * [Mintlify Enterprise plan](https://mintlify.com/pricing)
    * Admin access to the GitHub repositories for your code and documentation

    ### Install the Mintlify app on your code repository

    The Mintlify app must be installed on your code repository so the agent can fetch context from your codebase. To add the app to new repositories:

    1. Open the agent panel in your Mintlify dashboard.
       <Frame>
         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=56ee8c375606ca4a50b9b889474fc769" alt="The agent panel in light mode." className="block dark:hidden" data-og-width="2056" width="2056" data-og-height="840" height="840" data-path="images/agent/dashboard-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=62e3a171a1923a8afc5e958979c9fa67 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=9b670552f1cd97b14fabef128ae051ee 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=cdf9081b352d9dc74f66b10ea1761333 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=2648dfc256eef274a6b2988da72b64db 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=2c179d8a203d364d04ca1201ce2caa83 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=52eaedba495900766dc706d0bda7e1bf 2500w" />

         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=ad82516ec69eb247ac0475fd3397c338" alt="The agent panel in dark mode." className="hidden dark:block" data-og-width="2056" width="2056" data-og-height="840" height="840" data-path="images/agent/dashboard-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=bd58d31fcf5d51daaa7eec5dd3f565ce 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=98225e13a7b5d9052e7d9cb08d14d08a 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=1e82d5cf5b33c24744db75d4acff5f0e 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=76f753872cb7dca5446e2a98c8c7f6e8 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=50053641543ddeeeb18818da997132ea 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=b1de133975f47c6a4f99eead9069d99e 2500w" />
       </Frame>
    2. Click the **Settings** button.
       <Frame>
         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=ecb555eecfddf7480baaaf7d2fd6bce9" alt="The settings button in light mode." className="block dark:hidden" data-og-width="668" width="668" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=f6663dbc0d65a673d8d40a1a5021c4e6 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=8f16ed84866ed266b6c94ee063504e86 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0f09f59a375b2d0fa1a52e7105b9983a 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=9bd984bb1301430689ca1f80a55949da 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=27abd64a63bcba9de2cb2ca4fea13c76 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0fbcc0de8221607fd1ddddc91ff7299c 2500w" />

         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=a3250fa23cac19e8914b7185ac24c6d0" alt="The settings button in dark mode." className="hidden dark:block" data-og-width="670" width="670" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=e24b9bd26f3ae15ba38467da9e9fd650 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=1dbb09e9fc6d17ab545c6ad46e7e5585 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=05978a332b79eb6ccf7d86ae3c579039 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=38f053dd12cc6197779a368756b5eb34 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=c1d8e1cd78e6a494852b809cbeb1a695 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=508da1702ec011fa336b0fd7738c60c1 2500w" />
       </Frame>
    3. Click **Add to New Organization**. This will take you to the app installation page on GitHub.
    4. Select the repositories you want to grant access to from the list.
    5. Save your changes.

    ### Get your admin API key

    1. Navigate to the [API keys](https://dashboard.mintlify.com/settings/organization/api-keys) page in your dashboard.
    2. Select **Create Admin API Key**.
    3. Copy the key and save it securely.

    ## Build the workflow

    ### Create the workflow file

    1. In your code repository, create a new file: `.github/workflows/update-docs.yml`
    2. Add this workflow:

       ```yaml  theme={null}
       name: Update Docs

       on:
         push:
           branches:
             - main

       jobs:
         update-docs:
           runs-on: ubuntu-latest
           steps:
             - uses: actions/github-script@v8
               env:
                 MINTLIFY_API_KEY: ${{ secrets.MINTLIFY_API_KEY }}
                 PROJECT_ID: ${{ secrets.MINTLIFY_PROJECT_ID }}
               with:
                 script: |
                   const { owner, repo } = context.repo;
                   const projectId = process.env.PROJECT_ID;
                   const apiKey = process.env.MINTLIFY_API_KEY;

                   if (!projectId || !apiKey) {
                     core.setFailed('Missing MINTLIFY_PROJECT_ID or MINTLIFY_API_KEY secrets');
                     return;
                   }

                   const url = `https://api.mintlify.com/v1/agent/${projectId}/job`;
                   const payload = {
                     branch: `mintlify/docs-update-${Date.now()}`,
                     messages: [
                       {
                         role: 'system',
                         content: 'You are an action runner that updates documentation based on code changes. You should never ask questions. If you are not able to access the repository, report the error and exit.'
                       },
                       {
                         role: 'user',
                         content: `Update the documentation for our recent pushes to main:\n\nRepository: ${owner}/${repo}`
                       }
                     ],
                     asDraft: false
                   };

                   try {
                     const response = await fetch(url, {
                       method: 'POST',
                       headers: {
                         'Authorization': `Bearer ${apiKey}`,
                         'Content-Type': 'application/json'
                       },
                       body: JSON.stringify(payload)
                     });

                     if (!response.ok) {
                       throw new Error(`API request failed with status ${response.status}: ${await response.text()}`);
                     }

                     const reader = response.body.getReader();
                     const decoder = new TextDecoder();
                     let buffer = '';

                     while (true) {
                       const { done, value } = await reader.read();
                       if (done) break;
                       buffer += decoder.decode(value, { stream: true });
                       const lines = buffer.split('\n');
                       buffer = lines.pop() || '';
                       for (const line of lines) {
                         if (line.trim()) {
                           console.log(line);
                         }
                       }
                     }
                     if (buffer.trim()) {
                       console.log(buffer);
                     }

                     core.notice(`Documentation update job triggered for ${owner}/${repo}`);
                   } catch (error) {
                     core.setFailed(`Failed to create documentation update job: ${error.message}`);
                   }
       ```

    ### Add secrets

    1. In your code repository, go to **Settings** → **Secrets and variables** → **Actions**.
    2. Click **New repository secret**.
    3. Add the following secrets:
       * Name: `MINTLIFY_API_KEY`, Secret: Your Mintlify admin API key
       * Name: `MINTLIFY_PROJECT_ID`, Secret: Your Mintlify project ID (found on the [API keys](https://dashboard.mintlify.com/settings/organization/api-keys) page of your dashboard)

    For more information, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) in the GitHub documentation.

    ## Test the automation

    1. Make a small change in your code repository and push to main:
       ```bash  theme={null}
       git add .
       git commit -m "Test: trigger docs automation"
       git push origin main
       ```

    2. Check the **Actions** tab in your code repository to see the workflow running.

    3. After the workflow runs, check your documentation repository for a new branch and pull request with documentation updates.

    ## Troubleshooting

    ### Workflow not running

    * Verify GitHub Actions is enabled in your code repository.
    * Check the **Actions** tab for error messages.
    * Ensure the workflow file is in `.github/workflows/` with a `.yml` extension.

    ### 401 error from agent API

    * Verify your API key starts with `mint_`.
    * Check the Authorization header is formatted as `Bearer mint_yourkey`.
    * Confirm the API key is for the correct Mintlify organization.

    ### No documentation updates appearing

    * Check that the documentation repository is connected to your Mintlify project.
    * Verify the agent has write access to the documentation repository.
    * Check the workflow logs for error messages from the agent.
  </Tab>

  <Tab title="n8n">
    n8n provides a visual workflow editor and can integrate with multiple services.

    ## Prerequisites

    * n8n workspace
    * [Mintlify Enterprise plan](https://mintlify.com/pricing)
    * Mintlify app installed on your code repository
    * Mintlify admin API key
    * Admin access to the GitHub repositories for your code and documentation
    * GitHub personal access token

    ### Install the Mintlify app on your code repository

    The Mintlify app must be installed on your code repository so the agent can fetch context from your codebase. To add the app to new repositories:

    1. Open the agent panel in your Mintlify dashboard.
       <Frame>
         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=56ee8c375606ca4a50b9b889474fc769" alt="The agent panel in light mode." className="block dark:hidden" data-og-width="2056" width="2056" data-og-height="840" height="840" data-path="images/agent/dashboard-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=62e3a171a1923a8afc5e958979c9fa67 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=9b670552f1cd97b14fabef128ae051ee 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=cdf9081b352d9dc74f66b10ea1761333 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=2648dfc256eef274a6b2988da72b64db 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=2c179d8a203d364d04ca1201ce2caa83 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=52eaedba495900766dc706d0bda7e1bf 2500w" />

         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=ad82516ec69eb247ac0475fd3397c338" alt="The agent panel in dark mode." className="hidden dark:block" data-og-width="2056" width="2056" data-og-height="840" height="840" data-path="images/agent/dashboard-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=bd58d31fcf5d51daaa7eec5dd3f565ce 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=98225e13a7b5d9052e7d9cb08d14d08a 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=1e82d5cf5b33c24744db75d4acff5f0e 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=76f753872cb7dca5446e2a98c8c7f6e8 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=50053641543ddeeeb18818da997132ea 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=b1de133975f47c6a4f99eead9069d99e 2500w" />
       </Frame>
    2. Click the **Settings** button.
       <Frame>
         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=ecb555eecfddf7480baaaf7d2fd6bce9" alt="The settings button in light mode." className="block dark:hidden" data-og-width="668" width="668" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=f6663dbc0d65a673d8d40a1a5021c4e6 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=8f16ed84866ed266b6c94ee063504e86 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0f09f59a375b2d0fa1a52e7105b9983a 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=9bd984bb1301430689ca1f80a55949da 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=27abd64a63bcba9de2cb2ca4fea13c76 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0fbcc0de8221607fd1ddddc91ff7299c 2500w" />

         <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=a3250fa23cac19e8914b7185ac24c6d0" alt="The settings button in dark mode." className="hidden dark:block" data-og-width="670" width="670" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=e24b9bd26f3ae15ba38467da9e9fd650 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=1dbb09e9fc6d17ab545c6ad46e7e5585 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=05978a332b79eb6ccf7d86ae3c579039 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=38f053dd12cc6197779a368756b5eb34 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=c1d8e1cd78e6a494852b809cbeb1a695 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=508da1702ec011fa336b0fd7738c60c1 2500w" />
       </Frame>
    3. Click **Add to New Organization**. This will take you to the app installation page on GitHub.
    4. Select the repositories you want to grant access to from the list.
    5. Save your changes.

    ### Get your admin API key

    1. Navigate to the [API keys](https://dashboard.mintlify.com/settings/organization/api-keys) page in your dashboard.
    2. Select **Create Admin API Key**.
    3. Copy the key and save it securely.

    ### Get your GitHub personal access token

    1. In GitHub, navigate to **Settings**.
    2. Click **Developer settings**.
    3. Click **Personal access tokens**.
    4. Click **Tokens (classic)**.
    5. Click **Generate new token (classic)**.
    6. Select these scopes:
       * `repo` (full control of private repositories)
       * `admin:repo_hook` (if you want n8n to create webhooks)
    7. Generate and save the token securely.

    For more information, see [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens?versionId=free-pro-team%40latest\&productId=account-and-profile#creating-a-personal-access-token-classic) in the GitHub documentation.

    ## Build the workflow

    ### Create the webhook trigger

    1. In n8n, create a new workflow.
    2. Add a webhook node.
    3. Configure the webhook:
       * HTTP Method: `POST`
       * Path: `auto-update-documentation` (or any unique path)
       * Authentication: None
       * Respond: Immediately
    4. Save the workflow.
    5. Copy the production webhook URL. It looks like: `https://your-n8n-instance.app.n8n.cloud/webhook/auto-update-documentation`

    <Frame>
      <img
        src="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=165a57aed92aa90d90609c5d381d29b7"
        alt="Screenshot of the configurations for the webhook node."
        style={{
    width: 'auto',
    height: '700px',
  }}
        data-og-width="794"
        width="794"
        data-og-height="1290"
        height="1290"
        data-path="images/guides/n8n/webhook-node.png"
        data-optimize="true"
        data-opv="3"
        srcset="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=280&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=efbe9ed332b50e6d3a7d23e72414ee8d 280w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=560&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=77e09994b5055899ccd06694a93d2dea 560w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=840&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=322632ea71fc87c6b8d1efe3fbe0fa03 840w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=1100&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=93c413964016c6fe0f93be7469f16975 1100w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=1650&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=5c7c0fb7641c8696213d039708f0b30c 1650w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/webhook-node.png?w=2500&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=67b2572d4375f958940493affb1028ad 2500w"
      />
    </Frame>

    ### Set up the GitHub webhook

    1. Navigate to your code repository on GitHub.
    2. Click **Settings**.
    3. Click **Webhooks**.
    4. Click **Add webhook**.
    5. Configure the webhook:
       * Payload URL: Paste your n8n webhook URL
       * Content type: `application/json`
       * Which events would you like to trigger this webhook?
         * Select **Let me select individual events.**
         * Select only **Push events**.
       * Select **Active**
    6. Click **Add webhook**.

    ### Filter for main branch pushes

    Add a code node after the webhook to filter for pushes to main and extract the relevant information.

    1. Add a code node.
    2. Name it "Filter main pushes."
    3. Set mode to **Run Once for All Items**.
    4. Add this JavaScript:

    ```javascript  theme={null}
    const webhookData = $input.first().json.body;

    // Only continue if this is a push to main
    if (webhookData.ref !== "refs/heads/main") {
      return [];
    }

    // Extract information
    const repository = webhookData.repository;
    const pusher = webhookData.pusher;

    // Build message for agent
    const agentMessage = `Update documentation for changes pushed to main in ${repository.name}. Always edit files and create a pull request.`;

    return {
      json: {
        codeRepoName: repository.full_name,
        codeRepoShortName: repository.name,
        agentMessage: agentMessage
      }
    };
    ```

    <Frame>
      <img src="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=a7661a96b0a5c6272e8a284edb8eb8f5" alt="Screenshot of the configurations for the filter main pushes node." data-og-width="1520" width="1520" data-og-height="1444" height="1444" data-path="images/guides/n8n/filter-merged-PRs-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=280&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=b4e5cf685a50ebb3833fdff26fed0e6d 280w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=560&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=07228082cde6852f53b1cba514b5b3eb 560w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=840&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=ea22fe443bd29c1a48dd2a839510c7ca 840w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=1100&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=b6abd7a70bba3a54fe80a6ba630e6081 1100w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=1650&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=9c9086087bcd6069b467a8e31ecb8af5 1650w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/filter-merged-PRs-node.png?w=2500&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=ee4742c2dea8acbaac654e75d4c5c803 2500w" />
    </Frame>

    This code stops the workflow if the push wasn't to main, extracts all relevant information from the GitHub webhook, and creates a message for the agent API.

    ### Call the agent API

    Add an HTTP request node to create a documentation job.

    1. Add an HTTP request node.
    2. Name it "Create agent job."
    3. Configure the request:

       * Method: `POST`
       * URL: `https://api.mintlify.com/v1/agent/YOUR_PROJECT_ID/job` (replace `YOUR_PROJECT_ID` with your project ID from the [API keys](https://dashboard.mintlify.com/settings/organization/api-keys) page)
       * Authentication: Generic Credential Type → Header Auth
         * Create a new credential:
           * Name: `Authorization`
           * Value: `Bearer mint_YOUR_API_KEY` (replace with your API key)
       * Send Body: On
       * Body Content Type: JSON
       * Specify Body: Using JSON
       * Add this JSON:

       ```json  theme={null}
       {
       "branch": "docs-update-from-{{ $json.codeRepoShortName }}-{{ $now.toISOString() }}",
       "messages": [
           {
           "role": "system",
           "content": "{{ $json.agentMessage }}"
           }
       ],
       "asDraft": false
       }
       ```

    <Frame>
      <img
        src="https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=2bbb162905564f80a30bb7d75c917815"
        alt="Screenshot of the configurations for the create agent job node."
        style={{
    width: 'auto',
    height: '700px',
  }}
        data-og-width="756"
        width="756"
        data-og-height="1438"
        height="1438"
        data-path="images/guides/n8n/create-agent-job-node.png"
        data-optimize="true"
        data-opv="3"
        srcset="https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=280&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=01faea9302149a974dc9ac3dc68d6f95 280w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=560&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=01fcfb7f35dfaf59afd9e2a626df7ea5 560w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=840&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=ce18f31daf60caec50823650d06cd96d 840w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=1100&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=280fa6219837e89137b31ffc6d458235 1100w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=1650&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=5a2bd3ae4862208ea9aedd0f3a3ed8e0 1650w, https://mintcdn.com/mintlify/jW5VvzJALf7BW1X_/images/guides/n8n/create-agent-job-node.png?w=2500&fit=max&auto=format&n=jW5VvzJALf7BW1X_&q=85&s=c74c496f1085e6cb6f8fb075cba90fa1 2500w"
      />
    </Frame>

    The agent creates a pull request in your documentation repository using a descriptive branch name that includes the source repository name and timestamp.

    ### Activate the workflow

    1. Save your workflow.
    2. Set it to active.

    Your workflow is now monitoring your code repository for pushes to main.

    <Frame>
      <img src="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=55120ad3ffc9b32d56aefe05c6431324" alt="Screenshot of the automation workflow in the n8n editor." data-og-width="1562" width="1562" data-og-height="632" height="632" data-path="images/guides/n8n/workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=280&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=7dbba58e8a86f3998e022cb5174649d7 280w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=560&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=06d69f116911ba3a32980f59c122ff45 560w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=840&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=5fe9e6f99577ba5591874ea0b6c4f9a7 840w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=1100&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=af2b635a1605ca0dd4f7123fe1c122a0 1100w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=1650&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=ef500f88af7377097e4c7a21843cbe6a 1650w, https://mintcdn.com/mintlify/MUT1RZiseS3dwdrU/images/guides/n8n/workflow.png?w=2500&fit=max&auto=format&n=MUT1RZiseS3dwdrU&q=85&s=6a9b10ff9ee6d5da2657ebec2ef12c0e 2500w" />
    </Frame>

    ## Test the automation

    1. Create a test branch in your code repository:
       ```bash  theme={null}
       git checkout -b test-docs-automation
       ```

    2. Make a small change and commit it:
       ```bash  theme={null}
       git add .
       git commit -m "Test: trigger docs automation"
       git push origin test-docs-automation
       ```

    3. Open a pull request on GitHub.

    4. Merge the pull request.

    ### Verify the automation

    You should see a new n8n execution with all nodes completed successfully, and a new branch and pull request in your documentation repository.

    ## Troubleshooting

    ### Webhook not triggering

    * Verify the workflow is active in n8n.
    * Check GitHub repository Settings → Webhooks → Recent Deliveries for the response code.
    * Confirm the webhook URL matches your n8n webhook URL exactly.

    ### 401 error from agent API

    * Verify your API key starts with `mint_`.
    * Check the Authorization header is formatted as `Bearer mint_yourkey`.
    * Confirm the API key is for the correct Mintlify organization.

    ### 401 error from GitHub

    * Verify your token has the `repo` scope.
    * Check that the token hasn't expired.
    * Confirm you included the `User-Agent` header in the GitHub request.
  </Tab>
</Tabs>
