# Source: https://docs.replit.com/getting-started/quickstarts/import-from-github.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Import from GitHub

> Learn how to import GitHub repositories into Replit using rapid import or guided import methods.

## Import your GitHub repository

⏰ *Estimated time: two minutes*

You can import your GitHub repositories and turn them into Replit Apps to
run, test, and publish your code. This quickstart covers the fastest methods to get your GitHub projects running on Replit.

For comprehensive import options including other platforms like Figma, Bolt, and Lovable, see the [Import feature documentation](/replit-app/import-to-replit).

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/github.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=e85b1dcc9dd85b1c5f4f74c44406b48e" alt="Preview of GitHub repository import in Replit" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/import/github.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/github.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=5ce1d724e65bf66deaea53c1ab2426b2 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/github.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=9db2400a02e13072b66307d2a574191a 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/github.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=a8df4438cc9164c276be33182a137540 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/github.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=e85775ebc74208719a508375a4a2291e 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/github.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=72eb7ce6e318c6a141efc3fae7068698 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/github.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=80d6c8daaf7befe5e3affb85a60de1f8 2500w" />
</Frame>

## Rapid import

Rapid import works instantly with public repositories.
Combine the Replit import URL with your GitHub repository URL to start the import process.

<Accordion title="Import using rapid import" defaultOpen={true}>
  1. Copy the repository GitHub URL, starting with `github.com`.

  2. Type `https://replit.com/` in the browser address bar and paste your copied GitHub URL at the end (no spaces).

     **Example**:

     GitHub repository URL: `https://github.com/exampleUser/my-app`

     Import URL: `https://replit.com/github.com/exampleUser/my-app`

  3. Press Enter to start the automatic import process.
</Accordion>

## Guided import

Guided import steps you through the process of selecting a repository to import
and supports public and private repositories.

<Accordion title="Import using guided import" defaultOpen={false}>
  1. Navigate to <a href="https://replit.com/import" target="_blank">[https://replit.com/import](https://replit.com/import)</a>.

  2. Select **GitHub** from the available import sources.

  3. **Connect your GitHub account** to authorize access to your repositories.

  4. **Select the repository** you want to import.

  5. Select **Import** to start the conversion process.

  6. Configure your privacy settings and click **Import** to start the automatic import process.
</Accordion>

## Configure and run your app

During the import process, Replit attempts to set your app's language, dependencies, and workflow.
If your app doesn't run as expected, Replit offers the following workspace tools to help you resolve the issues:

* **[Agent](/replitai/agent)**: Diagnose and fix setup issues using AI-powered assistance.
* **[Configure Repl](/replit-app/configuration)**: Configure your app's language, dependencies, and workflow.
* **[Secrets](/replit-workspace/workspace-features/secrets)**: Securely add environment variables your app depends on.
* **[Workflows](/replit-workspace/workflows)**: Configure the Run button to your preferred command.

## Continue your journey

Now that you've set up your app, learn more about what you can do with your Replit App from the following resources:

* [Using the Git interface](/replit-workspace/workspace-features/git-interface): Learn how to manage your Git repositories in Replit
* [Make your Replit App Public](/replit-app/collaborate#make-your-replit-app-public): Share your Replit App as a Template for others to remix
* [Replit Deployments](https://docs.replit.com/category/replit-deployments): Publish your Replit App to the cloud with a few clicks
* [Secrets](/replit-workspace/workspace-features/secrets): Securely store sensitive information, including API keys and database credentials
* [Collaborate](/replit-app/collaborate): Work with others on your GitHub-imported projects
