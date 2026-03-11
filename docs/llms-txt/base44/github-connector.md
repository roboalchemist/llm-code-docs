# Source: https://docs.base44.com/Integrations/github-connector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the GitHub connector

> Connect your Base44 app to GitHub and manage repositories, list issues, review pull requests, and automate workflows connected to your codebase.

## About the GitHub connector

The GitHub connector lets your Base44 app securely access GitHub data using OAuth. Use it to build pull request and issue dashboards, automate issue creation, generate release notes, and sync repository activity into your app.

The GitHub connection is shared at the app level. When you connect GitHub, you authorize one GitHub account for that app. Everyone who can edit the app uses the same GitHub connection and sees the same GitHub-powered data inside the app.

<Frame caption="GitHub connector in Base44">
    <img src="https://mintcdn.com/base44/2T5G78XL6Ji4Hnz5/images/basegithubconnector.png?fit=max&auto=format&n=2T5G78XL6Ji4Hnz5&q=85&s=f84c8c2d4fbc1f0d73b77b14d5ec6c2c" alt="Basegithubconnector" width="684" height="393" data-path="images/basegithubconnector.png" />
</Frame>

<Warning>
  **Important:** Connectors are app-level, shared connections. Do not use the GitHub connector if each person using your app needs to connect their own GitHub account. For per-person GitHub login, build a custom OAuth flow with backend functions.
</Warning>

<Check>
  **Before you begin:** You need a [Builder plan](https://base44.com/pricing) or higher to use connectors in your app.
</Check>

***

## GitHub use cases and prompts

Use the GitHub connector to track engineering work, keep stakeholders updated, and connect code workflows to the rest of your tools.

<AccordionGroup>
  <Accordion title="Review pull requests and code activity">
    Build dashboards that list pull requests, show their status, and surface what needs review. You can also create views for recent commits, contributors, and repository activity.

    **Example prompts:**

    ```text  theme={null}
    Connect to GitHub and show all open pull requests across my repositories that are waiting for review.
    ```

    ```text  theme={null}
    Build a dashboard for one repository showing open pull requests, status checks, reviewers, and last update time.
    ```

    ```text  theme={null}
    Create a page that shows the latest commits for this repository with author, message, and timestamp.
    ```

    ```text  theme={null}
    Add a widget that highlights pull requests marked as "changes requested" and still open.
    ```

    ```text  theme={null}
    Show a list of pull requests merged in the last 7 days, grouped by repository.
    ```
  </Accordion>

  <Accordion title="Track issues and bugs">
    Turn GitHub issues into structured queues inside your app. Track priorities, assignees, labels, and aging issues, and keep a clear view of what is blocked or overdue.

    **Example prompts:**

    ```text  theme={null}
    Show open issues from my repository in a table with labels, assignee, priority, and created date.
    ```

    ```text  theme={null}
    Create a page that lists issues labeled "bug" and "p0" and sort them by oldest first.
    ```

    ```text  theme={null}
    Build a weekly report that summarizes new issues created this week and the top labels.
    ```

    ```text  theme={null}
    Add a view that shows issues that have not been updated in 14 days.
    ```

    ```text  theme={null}
    Create a dashboard that counts open issues by label and assignee.
    ```
  </Accordion>

  <Accordion title="Automate issue creation and workflows">
    Trigger GitHub actions from events in your app, such as creating an issue when a bug is reported, or opening a tracking issue when an incident is created.

    **Example prompts:**

    ```text  theme={null}
    When a new bug report is created in this app, create a GitHub issue in repo org/repo with the title and steps to reproduce.
    ```

    ```text  theme={null}
    Create a GitHub issue automatically when a critical incident is created, including severity, owner, and incident link.
    ```

    ```text  theme={null}
    When a feature request is marked Approved, open a GitHub issue with acceptance criteria and priority label.
    ```

    ```text  theme={null}
    When a customer ticket is escalated, create a GitHub issue and link back to the ticket.
    ```

    ```text  theme={null}
    Add a button that lets an admin create a GitHub issue from a record in this app.
    ```
  </Accordion>

  <Accordion title="Create changelogs and release notes">
    Sync merged pull requests and commits into a changelog, or generate release notes automatically from GitHub activity.

    **Example prompts:**

    ```text  theme={null}
    Sync merged pull requests from org/repo into a changelog page with title, author, and link.
    ```

    ```text  theme={null}
    Generate release notes for the last 2 weeks based on merged pull requests, grouped by label.
    ```

    ```text  theme={null}
    Create a weekly digest summarizing what shipped, including links to pull requests and issues closed.
    ```

    ```text  theme={null}
    Show a list of releases and their notes for this repository.
    ```

    ```text  theme={null}
    Create a "What's new" page that updates every Friday with this week's merged pull requests.
    ```
  </Accordion>

  <Accordion title="Combine GitHub with other tools">
    Connect GitHub to Slack, Gmail, BigQuery, Notion, or CRMs to route engineering updates where teams work.

    **Example prompts:**

    ```text  theme={null}
    Post a message in Slack when a pull request is merged, including title, author, and link.
    ```

    ```text  theme={null}
    Send a weekly Gmail digest with merged pull requests and closed issues, grouped by repository.
    ```

    ```text  theme={null}
    When a GitHub issue labeled "customer" is created, add it to a Notion database and notify #support in Slack.
    ```

    ```text  theme={null}
    Mirror issues labeled "docs" into a documentation backlog table inside my app.
    ```

    ```text  theme={null}
    Create a dashboard that joins GitHub deployment activity with BigQuery performance metrics.
    ```

    <Tip>
      When describing multi-tool flows in the AI chat, be explicit about which GitHub event should trigger the action and what details to include (repo, issue/PR number, title, labels, link).
    </Tip>
  </Accordion>
</AccordionGroup>

***

## Connecting GitHub to your app

Use the AI chat to connect to GitHub, or connect using a pre-made prompt from your app dashboard.

### Using the AI chat

1. Go to your app editor.
2. Describe what you want to do with GitHub in the AI chat, for example:
   * `Connect to GitHub and show all open pull requests for org/repo that are waiting for review.`
   * `Create a GitHub issue when a new bug is reported in this app.`
3. Review the **Action required** and **Required permissions** in the side panel.
4. Click **Connect to GitHub**.
5. In the GitHub window that opens:
   1. Sign in to the GitHub account you want to connect.
   2. Review the requested permissions and click **Authorize**.
6. Return to the editor and let the AI finish creating the GitHub-powered pages, tables, and flows.

<Frame caption="Connecting GitHub using the AI chat">
    <img src="https://mintcdn.com/base44/3C_67yjYIDEbv8rz/images/connectinggithub.png?fit=max&auto=format&n=3C_67yjYIDEbv8rz&q=85&s=4334fc8bb7b9c7ef60a8fdf0792b703a" alt="Connectinggithub" width="581" height="789" data-path="images/connectinggithub.png" />
</Frame>

### From the app dashboard

1. Click **Dashboard** in your app editor.
2. Click **Integrations**.
3. Click the **Browse** tab.
4. Find **GitHub** and click **Use**.
5. Select the pre-made prompt you want to add to the AI chat.
6. In the AI chat, review the **Action required** and **Required permissions**.
7. Click **Connect to GitHub** and complete the authorization flow.
8. Return to the editor and let the AI finish creating the GitHub-powered flows.

<Frame caption="Connecting GitHub from your app's dashboard">
    <img src="https://mintcdn.com/base44/k5k5XOsKyb1Fmny1/images/githubindashboard.png?fit=max&auto=format&n=k5k5XOsKyb1Fmny1&q=85&s=c860925947e8d79ca64618ef90ee38b4" alt="Githubindashboard" width="1260" height="968" data-path="images/githubindashboard.png" />
</Frame>

<Tip>
  Start with a simple read-only flow (like listing open pull requests) to confirm the connection works. Then add write actions like creating issues.
</Tip>

<Note>
  If you click **Reject** or close the authorization window, the connector is not added. You can run the connection flow again from the AI chat or from **Integrations → Browse**.
</Note>

***

## Managing your GitHub connection

You can review and manage the GitHub connector for each app from the app dashboard.

**To view or update your GitHub connector:**

1. Go to your app dashboard.
2. Click **Integrations**.
3. Click the **My integrations** tab.
4. Find **GitHub**, then choose what you want to do:
   * **View access**: See which permissions GitHub currently has in this app.
   * Click the **More Actions** icon <Icon icon="ellipsis" /> and select an option:
     * **Switch account**
     * **Disconnect account**
     * **Remove**

<Frame caption="Managing your GitHub connection in your app">
    <img src="https://mintcdn.com/base44/-ME_-awv5pBjXmIX/images/managegithubconnector.png?fit=max&auto=format&n=-ME_-awv5pBjXmIX&q=85&s=e45b3d9d70a608f3ef13ef529ffebc79" alt="Managegithubconnector" width="1257" height="890" data-path="images/managegithubconnector.png" />
</Frame>

***

## GitHub scopes and permissions

When you connect GitHub, the connector requests permissions through GitHub’s OAuth authorization flow. The exact permissions you see depend on what your app is trying to build or run.

<Card icon="shield" title="GitHub permissions">
  Always review the permissions shown in the GitHub authorization window before approving access.

  **Example permissions you may see:**

  * `repo`: Full access to repositories the connected account can access.
  * `read:user`: Read basic profile information for the connected account.
  * `user:email`: Read email addresses for the connected account.
</Card>

<Note>
  GitHub permissions may change depending on the flows you build. The authorization window always shows the current access being requested.
</Note>

***

## FAQs

<AccordionGroup>
  <Accordion title="Can I connect more than one GitHub account to the same app?">
    No. Each app uses one shared GitHub account. To use multiple GitHub accounts, create separate apps or build a custom OAuth flow with backend functions.
  </Accordion>

  <Accordion title="Can each person using my app connect their own GitHub account?">
    No. Connectors are app-level. When you connect GitHub, you connect a single GitHub account that all flows in the app use.

    To let each person using your app connect their own GitHub account, you need to build a custom OAuth flow with backend functions and the GitHub API, including per-user token storage and refresh.
  </Accordion>

  <Accordion title="How do I change which GitHub account is connected?">
    1. Go to your app dashboard and click **Integrations**.
    2. Click the **My integrations** tab.
    3. Find **GitHub** and click the **More Actions** icon <Icon icon="ellipsis" />, then **Switch account**.
    4. Complete the GitHub authorization flow for the new account.
  </Accordion>

  <Accordion title="Why can't my app access a private repository?">
    Access to private repositories depends on what you approved during authorization and which repositories your connected GitHub account can access.

    Reconnect GitHub and review the permissions shown in the authorization window to ensure the connector is authorized for the repositories you need.
  </Accordion>

  <Accordion title="Can I create issues or update content in GitHub from my app?">
    Yes, if the flow you build requires write permissions and you approve them during authorization. Always review the permissions shown in the connection flow before approving access.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).