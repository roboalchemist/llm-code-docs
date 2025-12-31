# Source: https://docs.replit.com/replit-workspace/workspace-features/git-interface.md

# Using the Git pane

> The Git pane streamlines version control directly in your workspace, making code tracking, branch management, and collaboration seamless.

The Git pane in Replit provides a visual interface for Git operations, eliminating the need to use command-line Git commands. This feature makes version control accessible for beginners while remaining powerful for experienced developers.

## Features

The Git pane offers comprehensive version control capabilities directly in your workspace, with a user-friendly interface that simplifies complex Git operations.

* **Repository management**: Initialize, connect, and manage Git repositories with GitHub integration
* **Commit tracking**: Stage, commit, and view changes across all your files
* **Branch operations**: Create, switch between, and merge branches visually
* **Conflict resolution**: Identify and resolve merge conflicts with visual assistance
* **Shell integration**: Synchronization between Git commands run in Shell and the Git pane

## Usage

### Repository setup

<Accordion title="How to access the Git pane">
  1. Navigate to the Tools section in your Replit App
  2. Select the **+** sign to add new tools
  3. Select **Git** from the list of available tools
</Accordion>

The Git pane helps you set up and connect your repository:

* **Initialize repository**: Create a new Git repository for your Replit App
* **Connect to GitHub**: Link your repository to GitHub for backup and collaboration
* **Configure remote**: Set up and manage the connection to your GitHub repository

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/01-git-pane.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=8173abb36daae9b8f60646cf259bf0dc" alt="Git pane showing the initialize repository button" data-og-width="230" width="230" data-og-height="314" height="314" data-path="images/gh/pane/01-git-pane.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/01-git-pane.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=c086175d67e99d5ef4339bda0c60e2d3 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/01-git-pane.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=76b597fd2f153d32e36853ed464a09c1 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/01-git-pane.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f66d5a713e54661be07ed6a91842ab2f 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/01-git-pane.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=9e48a40174a334f3de0466f8117c7369 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/01-git-pane.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bcd5460490c6927f699dfc4c7b908eab 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/01-git-pane.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e8f552f798c90b9b0cb2279fdc928a01 2500w" />
</Frame>

### Change management

<Accordion title="How to view changes">
  1. Make changes to any files in your Replit App
  2. Open the Git pane from the Tools section
  3. Review changes in the **Review Changes** section
</Accordion>

The Git pane provides tools to manage your code changes:

* **Review changes**: See modified files with additions and deletions highlighted
* **Stage files**: Select specific files to include in your next commit
* **Commit changes**: Save your changes with descriptive messages
* **Push updates**: Send your commits to GitHub with a single click

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/06-stage-commit-changes.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bf166d48de3a57be08343b79ea5ff900" alt="Git pane showing commit message field and stage options" data-og-width="526" width="526" data-og-height="211" height="211" data-path="images/gh/pane/06-stage-commit-changes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/06-stage-commit-changes.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=24aa6ba201889e4cfc63daafa1fbf335 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/06-stage-commit-changes.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f89e0f2fb929e965e3410d00dd45d0fa 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/06-stage-commit-changes.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=156f9c4d9dd668f2148feaf4a12bf4b0 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/06-stage-commit-changes.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=5081d7e7d4f58bcec1809f05607e0358 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/06-stage-commit-changes.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=dd0a0a5d2991fd26b00c9ed269ff422a 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/06-stage-commit-changes.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=360445bccd484b6508e8a8b686ea0a1d 2500w" />
</Frame>

<Note>
  You can use Replit AI to help generate commit messages that accurately describe your changes.
</Note>

### Branch management

<Accordion title="How to manage branches">
  1. Open the Git pane from the Tools section
  2. Select the branch dropdown next to the branch name
  3. Create a new branch or select an existing one
</Accordion>

The Git pane simplifies working with multiple versions of your code:

* **Create branches**: Make new branches to develop features separately
* **Switch branches**: Move between different versions of your code
* **Publish branches**: Share your branches to GitHub
* **Pull changes**: Sync with remote updates from collaborators

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/08-new-branch.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a9cab3e787687b8fbbf11103b8b86b20" alt="Git pane showing branch creation interface" data-og-width="526" width="526" data-og-height="83" height="83" data-path="images/gh/pane/08-new-branch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/08-new-branch.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e10469bd61c5cc9ab63083a439eec829 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/08-new-branch.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=84cf48a02fe3cfb657028c9f55a80274 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/08-new-branch.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=1fdab2ef6fe6e9aae40d240989d219bc 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/08-new-branch.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6740573a20b72b246daea2ff500ff46a 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/08-new-branch.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=071d16571c8ce00b9d645fcd15313562 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/08-new-branch.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=25c716f6b5d69d771110e7f987681e5f 2500w" />
</Frame>

### Merge conflict resolution

<Accordion title="How to resolve merge conflicts">
  1. Attempt to pull changes when conflicts exist
  2. The Git pane will highlight conflicting files
  3. Open each conflicted file to see and resolve the conflicts
  4. Save the files after resolving conflicts
  5. Complete the merge by selecting **Pull**
</Accordion>

When code from different sources conflicts, the Git pane helps you:

* **Identify conflicts**: See exactly which files contain conflicts
* **Visualize differences**: Review both versions of the conflicting code
* **Resolve issues**: Choose which code to keep or manually edit conflicts
* **Finalize merges**: Complete the merge process after resolving conflicts

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/11-merge-conflict.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f02773231068c03053c9c80d75ded53f" alt="Code editor showing merge conflict markers" data-og-width="526" width="526" data-og-height="108" height="108" data-path="images/gh/pane/11-merge-conflict.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/11-merge-conflict.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=2ff3c6f9de2c231be43f9357898747b7 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/11-merge-conflict.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=fc5ce34526e0f4d1c7e53a030bf3e513 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/11-merge-conflict.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=48427e257548024e84fa2376186d10a9 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/11-merge-conflict.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a3c586ac1259619acb32e494195338dc 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/11-merge-conflict.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=de2d29b7321e5c56fd8b841c96ddf911 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/gh/pane/11-merge-conflict.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=c7256e93a0299f810dde2a4a70d4bbed 2500w" />
</Frame>

After resolving a conflicted file, you can remove the conflict markers by removing the lines starting with conflict symbols and save the file.

### Using Git commands in Shell

<Accordion title="How to access Shell">
  1. Select **All tools** from the left Tool dock
  2. Select **Shell** from the available tools
</Accordion>

<Tip>
  While the Git pane provides a user-friendly interface, power users can use standard Git commands in the Shell for more complex operations. Changes made through either method will be reflected in both places.
</Tip>

If you prefer using Git through the command line:

* **Command synchronization**: Any Git commands executed in the Shell will automatically sync with the Git pane
* **Full Git functionality**: Access advanced Git features not available in the Git pane
* **Seamless switching**: Switch between using Shell commands and Git pane as needed

<Info>
  **GitHub and GitLab CLI Support**: In addition to standard Git commands, you can also use the [GitHub CLI](https://docs.github.com/en/github-cli) (`gh`) and [GitLab CLI](https://docs.gitlab.com/ee/editor_extensions/gitlab_cli/) (`glab`) in the Shell to manage and connect to external Git repositories. These tools provide enhanced functionality for working with GitHub and GitLab repositories, including pull requests, issues, and other platform-specific features.
</Info>

#### Repository operations

* **Clone repository**: `git clone <url-to-repository>`
* **Initialize repository**: `git init`
* **Add remote**: `git remote add origin <url-to-repository>`

#### Making changes

* **Check status**: `git status` (shows modified, added, and deleted files)
* **Stage files**: `git add <filename>` or `git add .` (for all files)
* **Commit changes**: `git commit -m "your commit message"`
* **Push changes**: `git push origin <branch-name>`
* **Pull changes**: `git pull origin <branch-name>`

#### Authentication

When working with private repositories, you'll need to authenticate:

* For GitHub repositories, use a personal access token instead of your password
* To avoid re-entering credentials, you can store them using Replit Secrets:
  1. Create a new secret with key `GIT_URL`
  2. Set the value to `https://<username>:<token>@github.com/<user-or-org>/<repository>`
  3. Use `git push $GIT_URL` to push without typing credentials

<Note>
  When using credential secrets, anyone with access to your Replit App can potentially access your Git credentials. For sensitive repositories, consider manually entering credentials each time.
</Note>
