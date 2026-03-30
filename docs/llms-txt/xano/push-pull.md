# Source: https://docs.xano.com/xano-cli/push-pull.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Push & Pull

> Sync XanoScript files between your local filesystem and Xano

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

The Xano CLI lets you pull your entire workspace down as XanoScript files and push local changes back. This enables local development, version control with Git, AI-assisted development, and team collaboration.

## Pull

Pull downloads your workspace as individual `.xs` (XanoScript) files, organized by type.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace pull ./my-workspace
  ```
</BrowserFrame>

This creates a directory structure like:

```
my-workspace/
├── workspace/
│   ├── my_workspace.xs
│   └── trigger/
│       └── on_workspace_event.xs
├── table/
│   ├── user.xs
│   ├── product.xs
│   └── trigger/
│       └── on_user_create.xs
├── function/
│   ├── calculate_shipping.xs
│   └── utils/
│       └── validate_email.xs
├── api/
│   ├── user/
│   │   ├── api_group.xs
│   │   ├── get_user_get.xs
│   │   └── create_user_post.xs
│   └── product/
│       ├── api_group.xs
│       └── list_products_get.xs
├── task/
│   └── cleanup_expired_sessions.xs
├── ai/
│   ├── agent/
│   │   ├── support_bot.xs
│   │   └── trigger/
│   │       └── on_agent_event.xs
│   ├── tool/
│   │   └── search_knowledge_base.xs
│   └── mcp_server/
│       ├── my_mcp_server.xs
│       └── trigger/
│           └── on_mcp_event.xs
├── realtime/
│   ├── channel/
│   │   └── notifications.xs
│   └── trigger/
│       └── on_message.xs
├── middleware/
│   └── auth_check.xs
└── addon/
    └── fetch_related.xs
```

Each resource becomes its own `.xs` file. Key details:

* **API endpoints** are grouped under `api/{group_name}/` directories, with each group containing an `api_group.xs` and endpoint files named `{name}_{verb}.xs`
* **Hierarchical functions** (with `/` in the name) are split into subdirectories
* **AI resources** (agents, tools, MCP servers) are grouped under `ai/`, with triggers in `ai/{type}/trigger/`
* **Realtime** resources are organized under `realtime/channel/` and `realtime/trigger/`
* **Triggers** are placed in `trigger/` subdirectories within their parent type (`table/trigger/`, `ai/agent/trigger/`, etc.)
* All filenames are converted to `snake_case`

### Pull Options

| Flag        | Description                                              |
| ----------- | -------------------------------------------------------- |
| `-b`        | Branch name (overrides profile; defaults to live branch) |
| `-w`        | Workspace ID (overrides profile)                         |
| `--env`     | Include environment variables                            |
| `--records` | Include database records                                 |
| `--draft`   | Include draft versions of resources                      |

#### Include environment variables

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace pull ./my-workspace --env
  ```
</BrowserFrame>

#### Include database records

Pull your table records alongside the schema. This is also a convenient way to create a **local backup** of your data before pushing schema changes.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace pull ./my-workspace --records
  ```
</BrowserFrame>

#### Both

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace pull ./my-workspace --env --records
  ```
</BrowserFrame>

#### Pull a specific branch

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace pull ./my-workspace -b v2-feature
  ```
</BrowserFrame>

If `-b` is not provided, the pull targets the branch stored in your profile. If no branch is set in your profile, it defaults to the live branch.

***

## Push

Push uploads all local `.xs` files back to your Xano workspace, syncing your local changes.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace
  ```
</BrowserFrame>

The CLI recursively collects all `.xs` files from the directory, sorts them alphabetically, combines them into a single payload, and sends them to Xano. After completion, the CLI displays the total execution time.

| Flag              | Description                                                                     |
| ----------------- | ------------------------------------------------------------------------------- |
| `-b`              | Branch name (overrides profile; defaults to live branch)                        |
| `-w`              | Workspace ID (overrides profile)                                                |
| `--partial`       | Push without requiring a workspace block — useful for pushing a subset of files |
| `--delete`        | Delete objects in Xano that are not present in the push                         |
| `--no-records`    | Skip importing table records (push schema only)                                 |
| `--no-env`        | Skip overwriting environment variables                                          |
| `--no-sync-guids` | Skip writing server-assigned GUIDs back to local files                          |
| `--truncate`      | Truncate all table records before importing                                     |

<Warning>
  Push replaces the workspace's XanoScript content with what you send. If your local files include schema changes — such as renamed or removed columns, or changed field types — those changes are applied directly and can affect existing data.

  **Before pushing**, make sure your local files are up to date (`pull` first), review your changes with `git diff`, and consider pulling with `--records` to snapshot your data. Work on a **non-live branch** and test before promoting to live. Use `--partial` if you only need to update specific resources.
</Warning>

### Push Options

#### Push schema only (skip records)

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace --no-records
  ```
</BrowserFrame>

#### Push without overwriting environment variables

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace --no-env
  ```
</BrowserFrame>

#### Partial push (no workspace block required)

Use `--partial` to push a subset of files without needing a complete workspace block. This is useful when you only want to update specific resources.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace --partial
  ```
</BrowserFrame>

#### Delete removed objects

Use `--delete` to remove any objects in Xano that are not present in your local files. This ensures your workspace matches your local directory exactly.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace --delete
  ```
</BrowserFrame>

<Warning>
  The `--delete` flag will permanently remove objects from your Xano workspace that don't exist in the local push. Double-check your local files before using this flag.
</Warning>

#### Truncate table records before importing

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace --truncate
  ```
</BrowserFrame>

#### Skip GUID sync

By default, after a push the CLI writes server-assigned GUIDs back into your local `.xs` files. Use `--no-sync-guids` to skip this step — useful in CI/CD pipelines or when you don't want local files modified.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace --no-sync-guids
  ```
</BrowserFrame>

#### Combine flags

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace --no-records --no-env
  ```
</BrowserFrame>

***

## Pull from Git

You can pull XanoScript files directly from a Git repository (GitHub, GitLab, or any git URL) into a local directory — without needing to clone the repo yourself.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace git pull ./output -r https://github.com/owner/repo
  ```
</BrowserFrame>

This fetches all `.xs` files from the repository and organizes them into the same directory structure as a workspace pull.

### Git Pull Options

| Flag     | Description                                                                    |
| -------- | ------------------------------------------------------------------------------ |
| `-r`     | Git repository URL (required) — supports HTTPS, SSH, GitHub, and GitLab URLs   |
| `-b`     | Branch, tag, or ref to fetch (defaults to the repository's default branch)     |
| `-t`     | Personal access token for private repos (falls back to `GITHUB_TOKEN` env var) |
| `--path` | Subdirectory within the repo to import from                                    |

### URL Formats

You can pass a variety of URL formats — the CLI extracts the owner, repo, branch, and path automatically:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  # Repository root
  xano workspace git pull ./output -r https://github.com/owner/repo

  # Specific branch
  xano workspace git pull ./output -r https://github.com/owner/repo -b main

  # Subdirectory via URL path
  xano workspace git pull ./output -r https://github.com/owner/repo/tree/main/path/to/dir

  # Single file URL (imports the containing directory)
  xano workspace git pull ./output -r https://github.com/owner/repo/blob/main/file.xs

  # SSH URL
  xano workspace git pull ./output -r git@github.com:owner/repo.git

  # GitLab
  xano workspace git pull ./output -r https://gitlab.com/owner/repo/-/tree/master/path

  # Private repo with token
  xano workspace git pull ./output -r https://github.com/owner/private-repo -t ghp_xxx
  ```
</BrowserFrame>

<Tip>
  For GitHub repos, the CLI uses the tarball API for fast downloads without requiring `git` to be installed. For GitLab and other hosts, it falls back to a shallow `git clone`.
</Tip>

### Workflow: Import from Git, Push to Xano

A common use case is pulling XanoScript from a shared Git repository and pushing it to a workspace. For example, you can pull the **Hello World** sample from the [XanoScript examples repo](https://github.com/xano-inc/xanoscript-examples) and push it to your workspace:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace git pull ./helloworld \
    -r https://github.com/xano-inc/xanoscript-examples \
    --path helloworld
  xano workspace push ./helloworld
  ```
</BrowserFrame>

***

## Typical Workflow

A common development cycle looks like this:

<Steps>
  <Step title="Pull the latest">
    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace pull ./my-workspace
      ```
    </BrowserFrame>
  </Step>

  <Step title="Make changes locally">
    Edit `.xs` files in your editor of choice. Use the [XanoScript VS Code Extension](https://marketplace.visualstudio.com/items?itemName=xano.xanoscript) for syntax highlighting and autocomplete.
  </Step>

  <Step title="Push changes back">
    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace push ./my-workspace
      ```
    </BrowserFrame>
  </Step>

  <Step title="Test in Xano">
    Verify your changes in the Xano dashboard or via API calls.
  </Step>
</Steps>

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/GitHub_light.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=7304b7cb9606506e332ca0504388559e" size={24} width="1024" height="1024" data-path="images/icons/GitHub_light.svg" /><Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/GitHub_dark.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=adb0b7079fcba72618143a25d1fafdff" size={24} width="1024" height="1024" data-path="images/icons/GitHub_dark.svg" /> <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/gitlab.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=9c4f55426b9ab4cbeabe567578ad364a" size={24} width="32" height="32" data-path="images/icons/gitlab.svg" /> Git works like it always has

Your workspace is plain files on disk — `git init`, commit, branch, and open PRs exactly like any other project. Xano's push/pull fits into your Git workflow, not the other way around.

## Working with Git

Since pull outputs standard files to your filesystem, you can version control your XanoScript with Git:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  cd my-workspace
  git init
  git add .
  git commit -m "Initial pull from Xano"
  ```
</BrowserFrame>

This gives you full commit history, diffs, branching, and collaboration through Git — on top of Xano's own branching system.

***

## Tips

* **Pull before you push** to avoid overwriting changes made by teammates in the Xano dashboard.
* **Use branches** for development work. Create a branch with `xano branch create -l dev`, then use `-b dev` on push and pull commands to target it without affecting the live branch.
* **Snapshot your data** by pulling with `--records` before pushing schema changes. This gives you a local copy of your database records you can restore from if needed.
* **Use `--partial`** when you only need to push a few specific resources instead of the entire workspace.
* **Combine with AI tools** like Claude Code or Cursor to generate and edit XanoScript locally, then push the results. See the [Start from Scratch](/xano-cli/guide-from-scratch) and [Work from Existing](/xano-cli/guide-from-existing) guides for full walkthroughs.

***

## Troubleshooting

If a push or pull isn't working as expected, use the `-v` (verbose) flag to see the full request and response details:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace push ./my-workspace -v
  ```
</BrowserFrame>

Verbose mode shows:

* The HTTP method and full URL being called
* Request headers (with the authorization token partially masked)
* The request body (truncated to 500 characters for readability)
* The response status code and elapsed time

This works on **all** CLI commands, not just push and pull. You can also enable it globally by setting the `XANO_VERBOSE` environment variable:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  export XANO_VERBOSE=true
  xano workspace pull ./my-workspace
  ```
</BrowserFrame>


Built with [Mintlify](https://mintlify.com).