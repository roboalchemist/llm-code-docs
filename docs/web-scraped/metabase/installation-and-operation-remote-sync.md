# Source: https://www.metabase.com/docs/latest/installation-and-operation/remote-sync

<div>

1.  [Home](/docs/latest/)
2.  [Installation and Operation](/docs/latest/installation-and-operation/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Remote sync

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Remote sync is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

## Overview

Remote Sync lets you develop analytics content in a collection in a development Metabase and automatically deploy it to a read-only production Metabase through Git.

**Remote Sync only syncs your dashboards, questions, and models---not your data or query results.** What gets stored in Git are [YAML files](./serialization#example-of-a-serialized-question) describing your analytics content. Your actual data stays in your databases and never goes to GitHub.

### How Remote Sync works

Here's a basic remote-sync workflow:

1.  Create a dashboard in a **Metabase configured in Read-write mode**.
2.  Push it to a Git branch.
3.  Open a pull request for review.
4.  Merge the PR to production.
5.  Your **Metabase configured in Read-only mode** automatically pulls in the changes.

We'll cover [setting up Remote Sync](#setting-up-remote-sync), an [example dev-to-production workflow](#an-example-dev-to-production-workflow), [branch management](#branch-management), and some other odds and ends.

### Key concepts

**Remote sync has two modes for different roles**:

-   **Read-write mode**: Create and edit content. You can [push](#pushing-changes-to-git) and [pull](#pulling-changes-from-git) changes to and from your repository. Multiple Metabase instances can connect in Read-write mode, each working on [different branches](#branch-management).
-   **Read-only mode**: Serves read-only content to users. Read-only instances only [pull](#pulling-changes-from-git) changes (typically from your main branch) and don't allow direct editing of synced content. You can set up [auto-sync](#pulling-changes-automatically) to automatically pull approved changes every five minutes.

**Only the synced collection is tracked**: Each Metabase connected to Remote Sync has one special [collection that syncs with Git](#how-the-synced-collection-works-in-read-write-mode). When you connect in Read-write mode, Metabase creates a collection called "Synced Collection" (you can rename it). Everything inside this collection (including sub-collections) is versioned and synchronized with your repository.

**The synced collection must be self-contained**: Everything a dashboard or question needs must be [inside the synced collection](#items-in-the-synced-collection-cant-depend-on-items-outside-of-it). Content outside the synced collection won't sync to your repository or appear in other Metabase instances.

**Content is stored as [YAML files](./serialization#example-of-a-serialized-question)**: Remote Sync stores your content as YAML files in your Git repository. Each dashboard, question, model, and document becomes a YAML file that can be reviewed in pull requests and versioned like code.

**Remote Sync excludes table metadata**: Column types, descriptions, and visibility settings don't sync. If you need to version table metadata, use [serialization](./serialization) instead.

## Setting up Remote Sync

You'll need to be an admin to set up Remote Sync.

1.  [Set up a repository to store your content](#1-set-up-a-repository-to-store-your-content)
2.  [Create a personal access token for development](#2-create-a-personal-access-token-for-development)
3.  [Connect your development Metabase to your repository](#3-connect-your-development-metabase-to-your-repository)
4.  [Add an item to your synced collection](#4-add-an-item-to-your-synced-collection)
5.  [Push your changes to your repository](#5-push-your-changes-to-your-repository)
6.  [Create a personal access token for production](#6-create-a-personal-access-token-for-production)
7.  [Connect your production Metabase to your repository](#7-connect-your-production-metabase-to-your-repository)

### 1. Set up a repository to store your content 

Before you connect Metabase to your Git repository, create a [new GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository). Initialize the repo with a README.md.

### 2. Create a personal access token for development 

Create a [Github fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for your repository with these permissions:

-   **Contents:** Read and write
-   **Metadata:** Read-only (required)

Copy the token immediately after generating it.

### 3. Connect your development Metabase to your repository 

![Development settings](./images/read-write-settings.png)

You can put any Metabase into Read-write mode. We also offer [Development instances](./development-instance) that you can use for Remote Sync or any other kind of development.

In the Metabase instance that you use for development:

1.  Go to **Admin settings** \> **Settings** \> **Remote sync**.

2.  Enter your repository URL:

    -   For example, `https://github.com/your-org/your-repo`. The repository must already exist and be initialized with at least one commit.

3.  Select **Read-write mode**.

4.  Add your access token:

    -   Paste the personal access token (PAT) you created earlier. Make sure the token has [read and write permissions](#2-create-a-personal-access-token-for-development). Metabase encrypts your token before storing it.

5.  Save and test the connection:

    -   Click "Save changes". Metabase will check whether it can reach your repository. If the connection fails, make sure your token has the appropriate permissions and hasn't expired. If you copied the token incorrectly, generate a new one.

### 4. Add an item to your synced collection 

When you first connect in Read-write mode, Metabase automatically creates a **synced collection** called "Synced Collection"---any content you add to it will be tracked in Git and can be pushed to your repository.

You can rename the Synced Collection if you want, and you can add sub-collections within it to organize your content.

1.  Navigate to the "Synced Collection" in your Synced Collections section (look for it in the left sidebar).

2.  Create or move content into the Synced Collection:

    -   **Create new content:** Click "New" and choose a dashboard, question, or document. Save it to the Synced Collection.
    -   **Move existing content:** Drag and drop items from other collections into the Synced Collection, or use the move option in the item's menu.

Remember that the synced collection must be [self-contained](#items-in-the-synced-collection-cant-depend-on-items-outside-of-it).

### 5. Push your changes to your repository 

![Push your changes](./images/push-changes.png)

Once you've added content, you'll see a yellow dot on your Synced Collection indicating uncommitted changes.

1.  Click the up arrow (push) icon next to the Synced Collection in the left sidebar.

2.  Enter a commit message describing your changes (e.g., "Added dashboard on mammoth populations").

3.  Click "Continue" to commit and push your changes to your repository.

Check your repository --- you should see the collection.

**About branches:** By default, you're pushing to your repository's main branch. However, you can choose which branch to push your development work to, allowing you to open pull requests for review before merging to the branch that your production Metabase pulls from. See [Branch management](#branch-management) for details on creating and switching branches.

### 6. Create a personal access token for production 

Create a [GitHub fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for your repository with these permissions:

-   **Contents:** Read-only
-   **Metadata:** Read-only (required)

Copy the token immediately after generating it --- you'll need to paste it into your production Metabase.

### 7. Connect your production Metabase to your repository 

![Production settings](./images/read-only-settings.png)

In your production Metabase instance:

1.  Go to **Admin settings** \> **Settings** \> **Remote sync**.

2.  Enter your repository URL:

    -   Use the same repository as your development Metabase, for example, `https://github.com/your-org/your-repo`.

3.  Select **Read-only mode**.

4.  Add your access token:

    -   Paste the read-only personal access token you created for this production Metabase.

5.  Save and test the connection:

    -   Click "Save changes". Metabase will verify it can reach your repository. If the connection fails, verify your token has the appropriate permissions and hasn't expired.

6.  Sync your content:

    -   Click "Pull changes" to immediately sync content from your repository.
    -   To keep your production instance automatically updated, toggle on "Auto-sync with Git". Metabase will pull changes from your main branch every five minutes.

In Read-only mode, the synced collection appears in the regular collections list with a special icon to indicate it's versioned and read-only.

![Production Metabase](./images/read-only-view.png)

At this point, you should be all set up. Exit Admin settings, then reload your browser. You should see your synced collection in your production Metabase.

## An example dev-to-production workflow

Let's say your team wants to build a new analytics dashboard. Here's a workflow that ensures that all production content goes through a review process.

### Step 1: Create a new branch

In your development Metabase, click the branch dropdown in the synced collections section and [create a new branch](#branch-management) for your work, like `feature/megafauna-dashboard`.

### Step 2: Create content in your development Metabase

Create a dashboard called "Megafauna Analytics" and add some questions. Save the questions either to the dashboard itself or to the synced collection. Save the dashboard to the synced collection.

### Step 3: Push to your development branch

1.  You should see a yellow dot on your synced collection (indicating local changes).
2.  Click the up arrow (push) icon next to your synced collection.
3.  Enter a commit message: "Add Megafauna Analytics dashboard".
4.  Metabase commits your changes to the branch you're working on and pushes them to your repo.

### Step 4: Create a pull request

In your Git repository:

1.  Create a pull request from your branch, `feature/megafauna-dashboard`, to the main branch `main`.
2.  Review the changes to the YAML files representing your dashboards and questions.
3.  Someone who knows what they're doing approves and merges the PR.

### Step 5: Production automatically updates

On your production Metabase instance:

1.  Within five minutes, Auto-sync detects the new commits on `main` (you can also manually import the changes).
2.  The "Megafauna Analytics" dashboard appears in production with all its questions.
3.  The content is read-only for users (they can view and use it, but can't edit it).

## How the synced collection works in Read-write mode

-   [The synced collection in the UI](#the-synced-collection-in-the-ui)
-   [Moving and deleting content in the synced collection](#moving-and-deleting-content-in-the-synced-collection)
-   [Items in the synced collection can't depend on items outside of it](#items-in-the-synced-collection-cant-depend-on-items-outside-of-it)

### The synced collection in the UI

When you first connect in Read-write mode, Metabase creates a synced collection called "Synced Collection". You can add items and sub-collections to it. The synced collection shows its current state with visual indicators: a yellow dot indicates unsynced local changes that need to be committed, and up/down arrows provide sync controls for pulling and pushing changes.

In Read-only mode, the synced collection appears in the regular collections list (not in a separate "Synced Collections" section) with a special icon to indicate it's versioned and read-only.

### Moving and deleting content in the synced collection

**Deletions sync to production:** When you remove content from the synced collection in Read-write mode and push that change, the content will also be removed from your Production instance when it syncs. This applies to moving content out of the synced collection or deleting it entirely.

Content in other Metabases that depended on this item may break since the dependency will no longer be in the synced collection.

### Items in the synced collection can't depend on items outside of it

For Remote Sync to work properly, the synced collection must be self-contained. Everything a dashboard or question needs must be inside the synced collection. This includes:

-   Questions that reference models
-   Dashboards with questions
-   Click behaviors linking to other content
-   Filters that pick values from other questions or models
-   @ mentions in documents

Exception: questions that reference snippets can't be synced, since snippets live outside collections.

If you try to add a question that references a model, make sure the model is also in the synced collection.

### Making sub-collections appear at the top level

If you're using Metabase for embedding, you might want synced content to appear at the top level of your navigation rather than nested under the Synced Collection. Since all synced content must be in sub-collections of the Synced Collection, you can use permissions to control how the collection hierarchy appears to different groups.

1.  In your development Metabase, **Organize content in sub-collections of your Synced Collection**. For example, you might have `Synced Collection/Mammoth Statistics` and `Synced Collection/Giant Sloth Statistics`.

2.  In your production Metabase, **Set up permissions for embedded groups:** Groups should have:

    -   **No view access** to the Synced Collection itself
    -   **View access** to specific sub-collections within the Synced Collection

For groups with these permissions, the sub-collections they can access will appear at the top level of navigation, as if they were root-level collections. They won't see the top-level Synced Collection that you have in your development Metabase.

What you see in Read-write mode:

``` highlight
Collections
└── Synced Collection
    ├── Mammoth Statistics
    ├── Giant Sloth Statistics
```

What embedding groups see in Read-only mode (with no access to Synced Collection, but access to Mammoth Statistics and Giant Sloth Statistics):

``` highlight
Collections
├── Mammoth Statistics
└── Giant Sloth Statistics
```

## What Metabase syncs

Remote Sync uses the same serialization format as the [Metabase CLI serialization feature](./serialization), storing your content as YAML files in your Git repository.

**What syncs:**

-   Dashboards and their cards
-   Questions (saved queries and models)
-   Model metadata (column descriptions, display settings, etc.)
-   Documents
-   Timelines and events
-   Collection structure and metadata

**What doesn't sync:**

-   Users, groups, and permissions
-   Alerts and subscriptions
-   Snippets
-   Database connections
-   Personal collections
-   Table metadata (column types, descriptions, visibility settings, etc.)

## Branch management

Branching is only available in Read-write mode.

### Creating a branch

You can create branches in Metabase or directly in your Git repository. Branches created in Git will appear in the Metabase branch dropdown once Metabase syncs with your repository.

Before creating branches, push an initial commit to your main branch.

To create a new branch in Metabase:

1.  Click the branch dropdown in the synced collections section.
2.  Type a name for the new branch in the search box.
3.  Press Enter to create the branch.

The new branch is created from your current commit (not the latest commit from the remote).

### Switching branches

In the left sidebar under "SYNCED COLLECTIONS", you'll see a branch dropdown next to the synced collection name:

1.  Click the branch dropdown to see available branches.
2.  Select a different branch to switch to it.

If the branch doesn't appear, ensure it exists in your Git repository and that the name matches exactly (branch names are case-sensitive).

If you have unsynced changes, Metabase will show a dialog asking what you want to do:

-   **Push changes to the current branch:** Commits your changes to the current branch before switching.
-   **Create a new branch and push changes there:** Saves your work to a new branch, keeping the original branch clean.
-   **Discard these changes:** Throws away your uncommitted changes (can't be undone).

The dialog shows you exactly which items have changed, so you can make an informed decision.

If you switch modes (from Read-write to Read-only or vice versa) with unpushed changes, you'll be prompted to save or discard them. You cannot switch to Read-only mode with uncommitted changes.

If changes don't appear after switching modes: Hard refresh your browser (Cmd/Ctrl + Shift + R).

## Pushing changes to Git

You can only push changes in a Metabase with Remote Sync set to Read-write mode.

### Committing and pushing your changes

When you make changes to items in the synced collection, a yellow dot appears on your synced collection (indicating uncommitted changes). To commit and push your changes:

1.  Click the up arrow (push) icon next to the synced collection name in the left sidebar.
2.  Enter a descriptive commit message explaining your changes.
3.  Click "Continue" to push your changes to Git.

If you see a message that "Remote is ahead of local", that means someone else pushed to the branch from another Metabase in Read-write mode. Pull the latest changes before pushing again.

## Pulling changes from Git

You can pull changes when in Read-write or Read-only mode.

In Read-write mode, you can get the latest changes from your Git repository:

1.  Click the down arrow (pull) icon next to your synced collection in the left sidebar.
2.  Review any summary of incoming changes if shown.
3.  Confirm the import.
4.  Metabase updates your collections with the latest content from Git.

If changes don't appear after pulling:

-   Verify you're on the correct branch.
-   Hard refresh your browser (Cmd/Ctrl + Shift + R).
-   If you encounter sync errors, review error messages in the sync dialog, manually resolve conflicts in your Git repository, then pull again.

In Read-only mode, go to **Admin settings** \> **Settings** \> **Remote sync** and click **Pull changes**.

### Handling unsynced changes

If you have local uncommitted changes when trying to pull or switch branches, Metabase will prompt you with options:

-   **Push changes to the current branch:** Commit your changes first, then proceed.
-   **Create a new branch and push changes there:** Preserve your work on a new branch.
-   **Discard these changes:** Throw away your uncommitted changes to accept what's in Git.

When in doubt, create a new branch and push changes to that branch. That way you won't lose any work.

### Pulling changes automatically

In Read-only mode, you can set Metabase to auto-sync changes from your main branch.

1.  Navigate to **Admin settings** \> **Settings** \> **Remote sync**.
2.  Enable Auto-sync with Git.

By default, Metabase will pull any changes (if any) from the branch you specify every five minutes. You can also manually sync as needed.

## Disabling Remote Sync

To disable Remote Sync, go to the Remote Sync settings page in Admin settings.

To disable Remote Sync:

1.  Go to **Admin settings** \> **Settings** \> **Remote sync**.
2.  Click **Disable Remote Sync**.
3.  In the confirmation dialog, click **Disable**.

-   All remote sync settings are cleared, including the repository URL, access token, and branch information.
-   Your synced collection and its content remain in your Metabase (they're not deleted).
-   The synced collection becomes a regular collection that you can edit like any other collection.
-   You can re-enable Remote Sync later by reconnecting to a repository, but any changes you made to the collection after disabling can be overwritten if you enable sync again.

## Migrating existing content to Remote Sync

If you already have content in your Metabase, you can gradually adopt Remote Sync. Content that lives outside the synced collection remains unaffected---you can continue working with it normally while you migrate content into the synced collection over time.

Make sure you move any dependencies (like models referenced by questions) into the synced collection, since [synced content must be self-contained](#key-concepts).

### If you already have a repo with serialized Metabase data

Keep doing what you're doing.

If you want to switch fully to Remote Sync, we recommend starting with a new repo:

1.  Check out a new branch in your Metabase instance in Read-write mode.
2.  Import your data to your Metabase instance with the serialization command as you normally would.
3.  Move the content you want to sync into the synced collection.
4.  Push up your changes to the new repo.

Remote Sync does NOT sync table metadata, so if you're importing and exporting your [table metadata](../data-modeling/metadata-editing), you should stick with serialization.

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/installation-and-operation/remote-sync.md) ]