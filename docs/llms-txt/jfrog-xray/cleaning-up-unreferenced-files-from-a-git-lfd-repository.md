# Source: https://docs.jfrog.com/artifactory/docs/cleaning-up-unreferenced-files-from-a-git-lfd-repository.md

# Clean Up Unreferenced Files from a Git LFS Repository

Use this command to clean up a Git LFS repository. This command deletes all files from a Git LFS repository in Artifactory that are no longer referenced in a corresponding Git repository.

**To clean up unreferenced Git LFS objects in Artifactory:**

1. Complete the prerequisites in [Before You Begin](#before-you-begin).
2. Run `jf rt git-lfs-clean` (or `jf rt glc`) starting with `--dry-run` and `--repo` where appropriate, then run without `--dry-run` when you are ready to delete (see [Cleaning Up Unreferenced Files Examples](#cleaning-up-unreferenced-files-examples)).

## Before You Begin

Ensure the following prerequisites are met before running this command:

1. **JFrog CLI configured** — Run `jf config add` to add your Artifactory server if you have not done so already.
2. **Git LFS installed** — Install from [git-lfs.com](https://git-lfs.com) and run `git lfs install` in your repository.
3. **Artifactory LFS URL configured in your Git repository** — The CLI attempts to auto-detect the Artifactory LFS repository from your local Git config. For auto-detection to work, your repository must have one of the following set:

   **Option A — `.lfsconfig` file** (recommended): Create a `.lfsconfig` file in your repository root:

   ```
   [lfs]
       url = https://<your-server>/artifactory/<your-lfs-repo>
   ```

   **Option B — `.git/config`**: Set the `lfs.url` key in your local Git config:

   ```
   git config lfs.url https://<your-server>/artifactory/<your-lfs-repo>
   ```

   If neither is configured, pass `--repo=<repo-name>` explicitly on every command invocation.

## Commands Params

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Command / Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Command name
      </td>

      <td>
        `rt git-lfs-clean`
      </td>
    </tr>

    <tr>
      <td>
        Abbreviation
      </td>

      <td>
        `rt glc`
      </td>
    </tr>

    <tr>
      <td>
        **Command options:**
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `--server-id`
      </td>

      <td>
        \[Optional]

        Server ID configured using the `jf config` command. If not specified, the default configured server is used.
      </td>
    </tr>

    <tr>
      <td>
        `--refs`
      </td>

      <td>
        \[Default: `refs/remotes/*`] List of comma-separated Git references in the form of `"ref1,ref2,..."` which should be preserved.

        **Important:** When using wildcard patterns (for example, `refs/remotes/*`), quote the entire value to prevent shell glob expansion: `--refs='HEAD,refs/remotes/*'`
      </td>
    </tr>

    <tr>
      <td>
        `--repo`
      </td>

      <td>
        \[Required unless Artifactory LFS URL is pre-configured in the Git repository]

        Name of the Git LFS repository in Artifactory to clean. If omitted, the CLI attempts to detect the repository from `.lfsconfig` or the `lfs.url` key in `.git/config`. If neither is configured, this flag is required — the command will fail with a detection error. See [Before You Begin](#before-you-begin) for setup instructions.
      </td>
    </tr>

    <tr>
      <td>
        `--quiet`
      </td>

      <td>
        \[Default: `false`; defaults to `true` when the `$CI` environment variable is set]

        Set to `true` to skip the delete confirmation message. When running in a CI environment (where the `CI` environment variable is set), this defaults to `true`.
      </td>
    </tr>

    <tr>
      <td>
        `--dry-run`
      </td>

      <td>
        \[Default: `false`]

        If `true`, cleanup is only simulated. No files are actually deleted.
      </td>
    </tr>

    <tr>
      <td>
        `--insecure-tls`
      </td>

      <td>
        \[Default: `false`]

        Set to `true` to skip TLS certificates verification.
      </td>
    </tr>

    <tr>
      <td>
        `--retries`
      </td>

      <td>
        \[Default: `3`]

        Number of HTTP retries.
      </td>
    </tr>

    <tr>
      <td>
        `--retry-wait-time`
      </td>

      <td>
        \[Default: `0`]

        Number of seconds or milliseconds to wait between retries. The numeric value should either end with `s` for seconds or `ms` for milliseconds (for example, `10s` or `100ms`).
      </td>
    </tr>

    <tr>
      <td>
        **Authentication flags:**
      </td>

      <td>
        This command also accepts per-invocation authentication flags: `--url`, `--user`, `--password`, `--access-token`, `--ssh-key-path`, `--ssh-passphrase`. These override the configured server credentials for this command only. See [Authentication](/docs/authentication) for details.
      </td>
    </tr>

    <tr>
      <td>
        **Command arguments:**
      </td>

      <td>
        If no arguments are passed in, the command assumes the .git repository is located at current directory.
      </td>
    </tr>

    <tr>
      <td>
        path to .git
      </td>

      <td>
        Path to the directory which includes the .git directory.
      </td>
    </tr>
  </tbody>
</Table>

## Cleaning Up Unreferenced Files Examples

### Example 1: Recommended Starting Point — Dry Run with Explicit Repository

Before deleting any files, use `--dry-run` with `--repo` to preview what would be removed. This is the recommended way to start, especially for first-time use.

```
jf rt glc --dry-run --repo=my-gitlfs-repo
```

**Expected output:**

```
[Info] Searching files from Artifactory repository my-gitlfs-repo ...
[Info] The following 3 files are not referenced in git and will be deleted from Artifactory:
my-gitlfs-repo/objects/ab/cd/abcd1234...
my-gitlfs-repo/objects/ef/gh/efgh5678...
my-gitlfs-repo/objects/ij/kl/ijkl9012...
[Info] Dry run. No files were deleted.
```

If there are no unreferenced files, the output will indicate that nothing was found.

***

### Example 2: Clean Up Using the Current Directory

This example cleans up Git LFS files from Artifactory using the `.git` directory in the current directory. The LFS repository is auto-detected from `.lfsconfig` or `.git/config`. If auto-detection fails, use `--repo` as shown in Examples 4 and 5.

```
jf rt glc
```

**Expected output (when LFS repo is auto-detected):**

```
[Info] Searching files from Artifactory repository <detected-repo> ...
[Info] The following files are not referenced in git and will be deleted from Artifactory:
...
Delete the above files? (y/n): y
[Info] Deleted X files from Artifactory.
```

***

### Example 3: Clean Up Using a Specific Path

This example cleans up Git LFS files from Artifactory using the `.git` directory located inside `path/to/git/config`. The LFS repository is auto-detected from that Git repo's configuration.

```
jf rt glc path/to/git/config
```

***

### Example 4: Dry Run to Preview Deletions

This example simulates the cleanup without actually deleting any files. Always pass `--repo` when the Git repo does not have an Artifactory LFS URL configured.

```
jf rt glc --dry-run --repo=my-gitlfs-repo
```

**Expected output:**

```
[Info] Searching files from Artifactory repository my-gitlfs-repo ...
[Info] Dry run. No files were deleted.
```

***

### Example 5: Clean Up with Specific Repository

This example cleans up a named Git LFS repository in Artifactory. The user is prompted for confirmation before deletion.

```
jf rt glc --repo=my-gitlfs-repo
```

**Expected output:**

```
[Info] Searching files from Artifactory repository my-gitlfs-repo ...
[Info] The following files are not referenced in git and will be deleted from Artifactory:
...
Delete the above files? (y/n): y
[Info] Deleted X files from Artifactory.
```

***

### Example 6: Clean Up with Custom Refs

This example preserves files referenced by HEAD and all remote branches. **Quote the `--refs` value** to prevent shell glob expansion (required on zsh and bash when the path does not match existing files).

```
jf rt glc --repo=my-gitlfs-repo --refs='HEAD,refs/remotes/*'
```

<Callout icon="📘" theme="info">
  Note

  The command `jf rt glc --refs=HEAD,refs/remotes/*` (unquoted) will fail in zsh with `no matches found` because the shell expands `*` before passing the argument to the CLI.
</Callout>

***

### Example 7: Quiet Mode for CI/CD Pipelines

This example runs the cleanup without confirmation prompts, suitable for automated pipelines. The `--quiet` flag is automatically set to `true` when the `$CI` environment variable is present.

```
jf rt glc --quiet --repo=my-gitlfs-repo
```

**Expected output:**

```
[Info] Searching files from Artifactory repository my-gitlfs-repo ...
[Info] Deleted X files from Artifactory.
```

***

### Example 8: With Retry Configuration

This example configures retry behavior for unreliable network connections.

```
jf rt glc --repo=my-gitlfs-repo --retries=5 --retry-wait-time=10s
```