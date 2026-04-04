# Source: https://docs.xano.com/xano-cli/workspaces-and-branches.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspaces & Branches

> Manage your Xano workspaces and branches from the CLI

export const BrowserFrame = props => {
  const {url = "xano.run", maxWidth = 820, className = "", lightSrc, darkSrc, alt = "", children} = props || ({});
  const style = typeof maxWidth === "number" ? {
    maxWidth: `${maxWidth}px`,
    margin: "16px 0"
  } : {
    maxWidth,
    margin: "16px 0"
  };
  const hasSwapImages = Boolean(lightSrc && darkSrc);
  return <div className={`browser-frame ${className}`.trim()} style={style}>
      <div className="browser-frame__top">
        <div className="browser-frame__controls" aria-hidden="true">
          <span className="browser-frame__dot browser-frame__dot--red" />
          <span className="browser-frame__dot browser-frame__dot--yellow" />
          <span className="browser-frame__dot browser-frame__dot--green" />
        </div>
        <div className="browser-frame__address">{url}</div>
      </div>

      <div className="browser-frame__body">
        {hasSwapImages ? <>
            <img className="browser-frame__img--light" src={lightSrc} alt={alt} />
            <img className="browser-frame__img--dark" src={darkSrc} alt={alt} />
          </> : children}
      </div>
    </div>;
};

## Workspaces

A workspace is an isolated backend environment in Xano containing your database tables, APIs, functions, tasks, and more. The CLI provides full workspace management.

<Note>
  Most workspace commands use the workspace ID stored in your profile. You can override it per-command with `-w WORKSPACE_ID`.
</Note>

### List Workspaces

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace list
  ```
</BrowserFrame>

Use `-o json` for the full JSON response.

### Get Workspace Details

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace get
  ```
</BrowserFrame>

This returns details for the workspace in your current profile. To get a specific workspace:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace get WORKSPACE_ID
  ```
</BrowserFrame>

### Create a Workspace

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace create "My New Workspace"
  ```
</BrowserFrame>

| Argument / Flag | Description                           |
| --------------- | ------------------------------------- |
| `name`          | Workspace name (required, positional) |
| `-d`            | Description                           |
| `-o`            | Output format: `summary` or `json`    |

### Edit a Workspace

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace edit WORKSPACE_ID -n "Updated Name" -d "New description"
  ```
</BrowserFrame>

You can also toggle settings:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace edit WORKSPACE_ID --swagger --require-token
  ```
</BrowserFrame>

Use `--no-swagger` or `--no-require-token` to disable those options.

### Delete a Workspace

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace delete WORKSPACE_ID
  ```
</BrowserFrame>

Add `-f` to skip the confirmation prompt.

<Warning>
  Workspaces with active tenants cannot be deleted.
</Warning>

***

## Branches

Branches are versions of a workspace's business logic. They let you develop and test changes without affecting the live environment. Every workspace starts with a `v1` branch.

### List Branches

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch list
  ```
</BrowserFrame>

The output indicates which branch is `(live)` and which are `(backup)`:

```
Branches for workspace 12345:
  v1 (live)
  v2-feature
  v3-backup (backup)
```

You can specify a workspace ID directly:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch list WORKSPACE_ID
  ```
</BrowserFrame>

### Get Branch Details

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch get v2-feature
  ```
</BrowserFrame>

### Create a Branch

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch create -l v2-feature
  ```
</BrowserFrame>

By default, new branches are cloned from `v1`. To clone from a different source:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch create -l v3-hotfix -s v2-feature
  ```
</BrowserFrame>

| Flag | Description                                 |
| ---- | ------------------------------------------- |
| `-l` | Branch label (required)                     |
| `-s` | Source branch to clone from (default: `v1`) |
| `-d` | Description                                 |
| `-c` | Color hex code (e.g., `#FF5733`)            |
| `-w` | Workspace ID                                |

### Edit a Branch

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch edit v2-feature -l v2-ready -d "Ready for review" -c "#00FF00"
  ```
</BrowserFrame>

<Note>
  The `v1` branch cannot be renamed.
</Note>

### Set a Branch Live

Promote a branch so that it serves all live API traffic:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch set_live v2-feature
  ```
</BrowserFrame>

You'll be asked to confirm before the switch takes effect. Use `-f` to skip confirmation.

<Warning>
  Setting a branch live immediately affects all API consumers. Make sure you've tested the branch thoroughly before promoting it.
</Warning>

### Delete a Branch

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano branch delete v2-feature
  ```
</BrowserFrame>

Add `-f` to skip confirmation.

<Note>
  The `v1` branch and the currently live branch cannot be deleted. To delete a branch that is currently live, first set a different branch live with `xano branch set_live <other-branch>`, then delete the original branch.
</Note>

***

## Working with Profiles and Branches

Your profile can store a default branch, so you don't need to specify it on every command. To update which branch your profile targets:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano profile edit -b BRANCH_LABEL
  ```
</BrowserFrame>

To clear the branch (use the live branch by default):

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano profile edit --remove-branch
  ```
</BrowserFrame>

This is especially useful when you want [push and pull](/xano-cli/push-pull) operations to target a specific branch.


Built with [Mintlify](https://mintlify.com).