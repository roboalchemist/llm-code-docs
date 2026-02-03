# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/local-configs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Configuration Branches

> Learn how to create and manage local branches for GenerativeAgent configurations.

# Managing Configuration Branches

## Introduction

Branching allows you to test new ideas, such as adding a new task or function, or changing instructions dramatically, without modifying the main version of GenerativeAgent. Think of a branch as your own “playground” to experiment and make changes freely—knowing the main configuration stays safe. Once you’re happy with your changes, you can bring them into the main setup to share with the rest of your team.

GenerativeAgent allows users to create local branches of configurations. This feature enables experimentation and collaboration without affecting the main configurations. Local branches provide a safe environment for testing changes to tasks, functions, and settings.

## Creating a New Branch

To create a new branch:

1. Navigate to the "Branch Switcher" in the GenerativeAgent interface.
2. Click on "Create branch."
3. Enter a unique branch name. Remember, branch names are case-insensitive and must include only letters, numbers, and dashes.
4. Select the source branch from which you wish to branch: Draft, Sandbox, or Production.
5. Click "Create branch."

> **Note:** You cannot create a branch from another branch; only the main environments can be used as a base.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a314f6eb26503284ac8c7b00e5f9a4b0" data-og-width="2282" width="2282" data-og-height="1116" height="1116" data-path="images/generativeagent/LocalConfig.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=45cc97ffb114e54615947704df7ecdca 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c0cb57489c8f651b954b18c337c7c7ea 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=73329c558e53c5134e36315b6648fd18 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=6b1b06f456194255a1e9a3b34af8245a 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b54db09ce5eb37cf5b80ad25555352b5 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=58a3e47f6d306e80d647a67bef386545 2500w" />
</Frame>

## Editing Configurations in a Branch

Within a local branch, you can edit tasks, functions, and settings:

* Access the configurations you wish to change.
* Make your edits safely, knowing they won't affect the main versions.
* Be aware that changes to the knowledge base, test users, and API connections will be visible across all environments and branches.

> **Note:** Knowledge articles do not support branching yet, so all branches will use the knowledge articles from draft.

## Previewing Configurations

To preview configurations in a local branch:

1. Select the branch you’re working on.
2. Click the "Preview" button.
3. The previewer will display the current state of your configurations within the branch.

> **Limitations:** You cannot switch branches/environments during a conversation. To do so, you must restart the conversation and select a different branch or environment.

## Managing Branches

### Switching Branches

* Use the "Branch Switcher" to select the desired branch for viewing or editing configurations.

### Deleting a Branch

1. Click "Delete branch" button in the header.
2. Confirm the deletion. This action is irreversible, and the system will lose all configurations in the branch.

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeleteLocalBranch.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=98c564241c2a81c7ab5b3fae0e7b8c7e" data-og-width="1548" width="1548" data-og-height="150" height="150" data-path="images/generativeagent/DeleteLocalBranch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeleteLocalBranch.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=cacecc4b856fa4d35768f7215ac41a74 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeleteLocalBranch.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=6852241d81ed8a359c1367c3f137105b 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeleteLocalBranch.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8401122c506737b3feb09757c2e864f3 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeleteLocalBranch.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3fe3cb7adc86b2416182b46d58bec417 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeleteLocalBranch.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=93ce8160d858dc27b981b996beb08eef 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeleteLocalBranch.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=084b3094298e921503f277b2ec114f55 2500w" />
</Frame>

## Promoting Changes to Main Environments

When ready to implement changes:

* Copy adjustments from your local branch to the main environments.
* Review and test thoroughly to ensure seamless integration.

> **Best Practices:** Document changes and collaborate with team members to maintain alignment and ensure successful deployment.

With these steps, you can leverage the full power of configuration branching in GenerativeAgent, fostering a collaborative and flexible development process.
