# Source: https://docs.windsurf.com/windsurf/cascade/worktrees.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.windsurf.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Worktrees

> Automatically set up git worktrees for parallel Cascade tasks

Windsurf supports using git worktrees to run Cascade tasks in parallel without interfering with your main workspace.

When using worktrees, each Cascade conversation gets its own session, allowing Cascade to make edits, or build and test code without interfering with your main workspace.

## Basic worktree usage

The simplest way to get started with using worktrees is switch to the "Worktree" mode in the bottom right corner of the Cascade input.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-toggle.png?fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=8bb3e54349d5c84d4db81210a67ee931" data-og-width="873" width="873" data-og-height="224" height="224" data-path="assets/windsurf/worktree-toggle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-toggle.png?w=280&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=ddf585207cf3d250b907271eda2cd108 280w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-toggle.png?w=560&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=635d65a1ca31987bdeeddb3b41dc2a35 560w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-toggle.png?w=840&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=61bb6d69981a39d4384094313a0dec79 840w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-toggle.png?w=1100&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=de84bfd761961e382cfd01fe87f70e98 1100w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-toggle.png?w=1650&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=2a1ffa7ee5b11576dbd284ef1642cc42 1650w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-toggle.png?w=2500&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=46a3198ea0bc5e00a305c3e2fd081b03 2500w" />
</Frame>

<Note>
  Currently, you can only switch to a worktree at the beginning of a Cascade session. Conversations cannot be moved to a different worktree once started.
</Note>

After Cascade makes file changes in the worktree, you have the option of clicking "merge" to incorporate those changes back into your main workspace.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-merge.png?fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=bb47b232dd861f3e37255b9b82fb18bc" data-og-width="724" width="724" data-og-height="98" height="98" data-path="assets/windsurf/worktree-merge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-merge.png?w=280&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=533e20b72c7d8e4619d2cc9e24b8aefb 280w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-merge.png?w=560&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=6aee660c46be478a6a744656100a6126 560w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-merge.png?w=840&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=432454ffca00c711b156cf94551f6453 840w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-merge.png?w=1100&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=fdb5c7889da375e6691e193182632aff 1100w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-merge.png?w=1650&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=d41895fd1e774550bd9d4e4f2c347a3a 1650w, https://mintcdn.com/codeium/U6QOrK-OfUtO4wfJ/assets/windsurf/worktree-merge.png?w=2500&fit=max&auto=format&n=U6QOrK-OfUtO4wfJ&q=85&s=717677273a6747ea668e4b9da2a7b1cd 2500w" />
</Frame>

## Location

Worktrees are organized by repo name inside `~/.windsurf/worktrees/<repo_name>`.

Each worktree is given a unique random name.

To see a list of active worktrees, you can run `git worktree list` from within the repository directory.

## Setup hook

Each worktree contains a copy of your repository files, but does not include `.env` files or other packages that aren't version-controlled.

If you would like to include additional files or packages in each worktree, you can use the `post_setup_worktree` [hook](./hooks#post_setup_worktree) to copy them into the worktree directory.

The `post_setup_worktree` hook runs after each worktree is created and configured. It is executed inside the new **worktree** directory.

The `$ROOT_WORKSPACE_PATH` environment variable points to the original workspace path and can be used to access files or run commands relative to the original repository.

### Example

Copy environment files and install dependencies when a new worktree is created.

**Config** (in `.windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "post_setup_worktree": [
      {
        "command": "bash $ROOT_WORKSPACE_PATH/hooks/setup_worktree.sh",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`hooks/setup_worktree.sh`):

```bash  theme={null}
#!/bin/bash

# Copy environment files from the original workspace
if [ -f "$ROOT_WORKSPACE_PATH/.env" ]; then
    cp "$ROOT_WORKSPACE_PATH/.env" .env
    echo "Copied .env file"
fi

if [ -f "$ROOT_WORKSPACE_PATH/.env.local" ]; then
    cp "$ROOT_WORKSPACE_PATH/.env.local" .env.local
    echo "Copied .env.local file"
fi

# Install dependencies
if [ -f "package.json" ]; then
    npm install
    echo "Installed npm dependencies"
fi

exit 0
```

This hook ensures each worktree has the necessary environment configuration and dependencies installed automatically.

## Cleanup

Windsurf automatically cleans up older worktrees when creating a new worktree to prevent excessive disk usage. Each workspace can have up to **20** worktrees.

Worktrees are cleaned up based on when they were last accessed—the oldest ones are removed first. This cleanup happens on a per-workspace basis, ensuring that worktrees from different repositories remain independent of each other.

Additionally, if you manually delete a Cascade conversation, Windsurf will automatically delete the associated worktree.

## Source Control Panel

By default, Windsurf does not show worktrees created by Cascade in the SCM Panel.
You can set `git.showWindsurfWorktrees` to `true` in your settings to override this and enable visualizing the worktrees in the SCM Panel.
