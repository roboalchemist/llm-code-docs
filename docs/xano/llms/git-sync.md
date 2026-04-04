# Source: https://docs.xano.com/xano-features/workspace-settings/git-sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Git Sync

> Learn how to use Git Sync to sync your Xano workspace to GitHub or GitLab

Xano supports **one-way Git sync** to <Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/GitHub_light.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=7304b7cb9606506e332ca0504388559e" size={16} width="1024" height="1024" data-path="images/icons/GitHub_light.svg" /><Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/GitHub_dark.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=adb0b7079fcba72618143a25d1fafdff" size={16} width="1024" height="1024" data-path="images/icons/GitHub_dark.svg" /> GitHub and <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/gitlab.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=9c4f55426b9ab4cbeabe567578ad364a" size={16} width="32" height="32" data-path="images/icons/gitlab.svg" /> GitLab.

This feature makes your XanoScript a first-class citizen in your development workflow, while keeping Xano as the **source of truth**. Publish your XanoScript to GitHub or GitLab to keep a versioned copy of your code outside of Xano for disaster recovery, compliance, or auditing. Or open source your XanoScript to the world to get feedback, contributions, and help from the community.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R-kwSxRFeU8?si=d2POKdRy-FIOV2R0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

***

## How It Works

* **Write code** in the Xano UI or in your IDE with the XanoScript VS Code extension.
* **Sync to Xano** — all changes flow through Xano first.
* **Push to Git** — Xano can export your latest code to GitHub or GitLab.

***

## Benefits of Git Sync

### 🔐 Version Control

Every sync creates a new commit in your Git repo. Track the history of changes and roll back when needed.

### 🧰 Collaboration

Use branches, pull requests, and code reviews. Non-Xano teammates can review and contribute using familiar Git tools.

### ☁️ Backup & Transparency

Keep a secure, versioned copy of your code outside of Xano for disaster recovery, compliance, or auditing.

### 🔄 Automation & Integration

Plug your XanoScript into CI/CD pipelines, linters, and security scanners. Git sync bridges Xano into your existing engineering ecosystem.

***

## What Git Sync Is *Not*

> ❌ Git sync is **not** a way to deploy code into Xano.\
> ❌ You cannot push changes from GitHub/GitLab into Xano.\
> ✅ All changes must flow through Xano—either via the UI or the XanoScript VS Code extension.

***

## Example Workflow

1. Jamie edits an API function in **VS Code** using the XanoScript extension.
2. The changes sync directly to **Xano**.
3. From Xano, Jamie pushes the latest code to **GitHub**.
4. The team reviews the diff in GitHub, merges a pull request, and maintains a clean version history.

***

## Using Git Sync in Xano

<Steps>
  <Step title="From your workspace dashboard, click the gear icon in the top-right corner, and choose Git Sync.">
        <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/git-sync-20251008-125901.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=5d9800fe8309541beda51c2e5cbd5aac" alt="git-sync-20251008-125901" width="621" height="651" data-path="images/git-sync-20251008-125901.png" />
  </Step>

  <Step title="In GitHub, create a new repository if you haven't already." />

  <Step title="In Xano's Git Sync menu, provide the URL of your GitHub repository.">
        <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/git-sync-20251008-130738.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=6c5eadfee90f4bc2ddd67e3da27add36" alt="git-sync-20251008-130738" width="1353" height="419" data-path="images/git-sync-20251008-130738.png" />

    <Steps>
      <Step title="Have a private repository or want to use SSH? Click the 'Generate Key' option.">
                <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/git-sync-20251008-130657.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=e070cbfffb91e32febf6689ecab59284" alt="git-sync-20251008-130657" width="1345" height="679" data-path="images/git-sync-20251008-130657.png" />
      </Step>

      <Step title="In GitHub, head to your repository settings and add the SSH key you generated in Xano.">
                <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/git-sync-20251008-130218.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=f3702cf9275e1ca5775e6770093838ba" alt="git-sync-20251008-130218" width="2086" height="1241" data-path="images/git-sync-20251008-130218.png" />
      </Step>
    </Steps>
  </Step>
</Steps>

***

## FAQ

**Why can’t I push changes from GitHub into Xano?**\
Xano treats itself as the **single source of truth** for XanoScript.\
Pulling code from Git would create conflicts, dependencies, and merge issues. Instead, use the XanoScript VS Code extension to push changes directly to Xano. Git is your **mirror** for history, backup, and collaboration.


Built with [Mintlify](https://mintlify.com).