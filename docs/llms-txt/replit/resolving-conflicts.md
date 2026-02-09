# Source: https://docs.replit.com/teams/projects/resolving-conflicts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Conflict Resolution in Projects

> Learn how to handle and resolve merge conflicts when multiple team members make changes to the same files in a Replit Project.

## Overview

When two teammates make changes to the same files in a Project, it is possible to end up with a [merge conflict](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts).

## Resolving a merge conflict

In this example, the main Replit App has a change to the joke endpoint. In your Replit App, if you also change the joke endpoint and attempt to sync or merge your changes, you'll hit a merge warning:

<Frame>
  <img src="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-on-pull.png?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=18037f38d8bef65992a45cde2fecae7d" alt="Merge Conflict on Pull" data-og-width="1440" width="1440" data-og-height="900" height="900" data-path="images/projects/projects-merge-conflict-on-pull.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-on-pull.png?w=280&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=ab521bdf0060a6010bfda1677166d84e 280w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-on-pull.png?w=560&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=6ee4d659f6d56df7694575505a635af8 560w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-on-pull.png?w=840&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=a1e8d8283b10fa2cf9f3acc265ced851 840w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-on-pull.png?w=1100&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=396485fba4621813eff2707239baed07 1100w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-on-pull.png?w=1650&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=c83ef85fe0af283978628ef8aecabcd5 1650w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-on-pull.png?w=2500&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=02889dadd6803fed0e9aef03f776758d 2500w" />
</Frame>

If you click the "resolve manually" button, the git tool will open up in conflict resolution mode to help you resolve the conflict:

<Frame>
  <img src="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-view-conflict.png?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=1f9c8d304a001a982b53d806fba16754" alt="Merge Conflict View Conflict" data-og-width="1440" width="1440" data-og-height="900" height="900" data-path="images/projects/projects-merge-conflict-view-conflict.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-view-conflict.png?w=280&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=77a951da29e16c652216305a34c8c426 280w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-view-conflict.png?w=560&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=08738e64ee3079419a45aa2c0058bacb 560w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-view-conflict.png?w=840&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=949aa56ea5ff979d0d7606128136dca8 840w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-view-conflict.png?w=1100&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=8558d7f09f01bb6208ebe145c84c187c 1100w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-view-conflict.png?w=1650&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=93c3dca96c433e168b0fdb3b33e0fd62 1650w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-view-conflict.png?w=2500&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=a51705836c7a2332d96ea346592bb526 2500w" />
</Frame>

You will see conflict markers `<<<<<<< HEAD`, `=======` and `>>>>>>> dd936daa...`. This is git's way of showing you the conflict it encountered and the two different version of the code it found. The bit between `<<<<<<< HEAD` and `=======` is the version of the joke endpoint found in the main Replit App (which was merged in between the time when you created your fork and the time you attempted to merge your fork), and the bit between `=======` and `>>>>>>> dd936daa...` is your change to the joke endpoint.

Resolving a merge conflict simply means editing the file to remove the conflict markers. Sometimes this means picking one change or the other. Other times this means picking parts of each version to create a blended version. In this situation, you can pick your version of the change:

<Frame>
  <img src="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-resolve-conflict.png?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=5efb31953aab83be0b374b341566eb30" alt="Merge Conflict Resolve Conflict" data-og-width="1440" width="1440" data-og-height="900" height="900" data-path="images/projects/projects-merge-conflict-resolve-conflict.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-resolve-conflict.png?w=280&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=e426054513686fe37bace2aa5e5d7422 280w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-resolve-conflict.png?w=560&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=b79aa9689405b0570b9bff9e0c9699c6 560w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-resolve-conflict.png?w=840&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=75d4166b3435b5837387392999bb8793 840w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-resolve-conflict.png?w=1100&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=126976b372220c5b2098c4ba0645494c 1100w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-resolve-conflict.png?w=1650&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=66e408aeb5010c61921687c42d4174b4 1650w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-resolve-conflict.png?w=2500&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=8c74bf2dedbc9b905b9ef879b29ee834 2500w" />
</Frame>

The "Complete merge and commit" button will be enabled when you have resolved all the conflicts. When you click it, you'll end up with a new commit that resolves the conflict:

<Frame>
  <img src="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-commit.png?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=387d0b083e9ec0d1cb5e3d3ec6ffeb63" alt="Merge Conflict Commit" data-og-width="1440" width="1440" data-og-height="900" height="900" data-path="images/projects/projects-merge-conflict-commit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-commit.png?w=280&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=c30f286fde281af7d1ee7660baacc23b 280w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-commit.png?w=560&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=7922b07ad3afa163a3b24f0666025f27 560w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-commit.png?w=840&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=b9b7db91c8738beb538c2b286d1b8e62 840w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-commit.png?w=1100&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=22a2a027d524248a62f005632f6a3874 1100w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-commit.png?w=1650&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=b3105a711f9aff1be7b784c6238a4467 1650w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/projects/projects-merge-conflict-commit.png?w=2500&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=ffab488b0afd02b44224ecc48331cde9 2500w" />
</Frame>

You will now be able to merge your changes back into the main Replit App.
