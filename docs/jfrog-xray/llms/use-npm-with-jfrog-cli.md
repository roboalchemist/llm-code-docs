# Source: https://docs.jfrog.com/artifactory/docs/use-npm-with-jfrog-cli.md

# Use Npm with Jfrog CLI

Run npm commands with Artifactory integration for dependency resolution and build information collection.

## **When Should You Use `jf npm`?**

Use `jf npm` if your JavaScript or TypeScript project uses npm for dependency management and you want packages resolved from and published to JFrog Artifactory. For Yarn-based projects, use `jf yarn`. For pnpm-based projects, use `jf pnpm`. For more information, see [package managers integration](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli/binaries-management-with-jfrog-artifactory/package-managers-integration) in the JFrog CLI documentation.

## **What Do You Need Before You Start?**

* npm must be installed (version 5.4.0 or above).
* JFrog Artifactory version 5.5.2 or above is required when the CLI obtains npm credentials from the Artifactory `/api/npm/auth` API (for example, typical password-based flows, or when the CLI cannot set authentication via access token for your npm version). If you use an access token with a supported npm client, the CLI may build authentication without calling that API, so that version check may not apply to your setup.
* Configure a server with `jf config add` or `jf c add` (equivalent to the older `jfrog` binary: `jfrog config add` or `jfrog c add`). The built-in `jf npm-config --help` text may still refer to `jfrog c add`. The command is the same.
* Authentication to JFrog Artifactory is required.
* Run `jf npm-config` in the project directory before the first build.

***

## **How Do You Configure `jf npm-config`?**

Generate npm configuration for resolving and deploying packages through JFrog Artifactory. Run this once per project before your first build.

To generate npm configuration for a project:

1. Add an JFrog CLI server with `jf config add` (or `jf c add`) if you have not already.
2. Run `jf npm-config` with `--server-id-resolve`, `--repo-resolve`, and optionally `--server-id-deploy` and `--repo-deploy`, as shown in [Configuration Examples](https://markdownlivepreview.com/#configuration-examples).

### **Synopsis**

```
jf npm-config [options]
```

Aliases: `npmc`

### **Configuration Options**

The following table describes `jf npm-config` flags.

| Flag                  | Default | Description                                           |
| --------------------- | ------- | ----------------------------------------------------- |
| `--global`            | `false` | Apply configuration globally for all projects         |
| `--server-id-resolve` | —       | JFrog Artifactory server ID for dependency resolution |
| `--server-id-deploy`  | —       | JFrog Artifactory server ID for deployment            |
| `--repo-resolve`      | —       | Repository for resolving dependencies                 |
| `--repo-deploy`       | —       | Repository for deploying packages                     |

### **Configuration Examples**

#### **View Help**

```shell
jf npm-config --help
```

#### **Non-interactive Configuration**

Configure npm with non-interactive flags:

```shell
jf npm-config --server-id-resolve=<server_id> --repo-resolve=<repository_key> --server-id-deploy=<server_id> --repo-deploy=<repository_key>
```

Where:

* `<server_id>` matches a server from `jf config add`.
* `<repository_key>` is the target npm repository key in JFrog Artifactory.

For example:

```shell
jf npm-config --server-id-resolve=my-server --repo-resolve=npm-virtual --server-id-deploy=my-server --repo-deploy=npm-local
```

Note: `jf npm-config` only writes `.jfrog/projects/npm.yaml` (or the global equivalent). It does not check that the resolve or deploy repository keys exist in JFrog Artifactory or that they are the correct npm repository type. A typo or wrong repository name still produces `npm build config successfully created.` You may only see 404, 401, or 403 on the first `jf npm install`, `jf npm ci`, or `jf npm publish`. Confirm repository names in JFrog Artifactory before relying on the config step.

### **Why Run Config First?**

You must run `jf npm-config` before running `jf npm install` or `jf npm publish`. The config command creates a `.jfrog/projects/npm.yaml` file in your project directory that tells the CLI which JFrog Artifactory repositories to use for resolution and deployment. Without it, `jf npm` does not know where to fetch or publish packages.

In CI/CD, pass all flags non-interactively so the config step is fully automated and reproducible.

### **Configuration Notes**

* Run once per project. The configuration persists in `.jfrog/projects/`. Re-run only when changing repository assignments.
* Global compared to project: Use `--global` to apply to all npm projects on the machine. Without it, configuration is project-specific (recommended).
* Server must exist: The `--server-id-resolve` and `--server-id-deploy` values must match a server added via `jf config add` (or `jf c add`).
* Native mode (`jf npm`, not `jf npm-config`): Native behavior is controlled when you run `jf npm install`, `jf npm ci`, or `jf npm publish`, by setting `JFROG_RUN_NATIVE=true` or using the deprecated `--run-native` flag on those commands. In native mode the CLI does not create a temporary `.npmrc` for those flows. Your existing `.npmrc` is used. `jf npm-config` does not define a `--run-native` option. It only writes project (or global) YAML under `projects/npm.yaml`.

### **Expected Output**

The CLI logs a line like the following (your logger may add a level prefix such as `[Info]`):

```
npm build config successfully created.
```

Example:

```
$ jf npm-config --server-id-resolve=my-server --repo-resolve=npm-virtual --server-id-deploy=my-server --repo-deploy=npm-local
npm build config successfully created.
```

### **How to Verify**

After running without `--global`, confirm the configuration exists under your project (or a parent directory):

```shell
cat .jfrog/projects/npm.yaml
```

If you used `jf npm-config --global`, the file is under the JFrog home directory, for example:

```
cat ~/.jfrog/projects/npm.yaml
```

JFrog CLI normally uses `~/.jfrog` as the home directory. If `JFROG_HOME` is set, global project config lives under `$JFROG_HOME/projects/npm.yaml` instead.

***

## **How Do You Run `jf npm`?**

Run npm commands with JFrog Artifactory integration for dependency resolution and build information collection.

To run an npm command through JFrog CLI:

1. Complete `jf npm-config` for the project (see [How Do You Configure `jf npm-config`?](https://markdownlivepreview.com/#how-do-you-configure-jf-npm-config)).
2. Run `jf npm` followed by the npm subcommand and options you need (see [Subcommands](https://markdownlivepreview.com/#subcommands) and [Build Options](https://markdownlivepreview.com/#build-options)).

### **Synopsis**

```
jf npm <npm_arguments> [options]
```

Aliases: none

### **Arguments**

The following table describes `jf npm` arguments.

| Argument        | Required | Description                                                         |
| --------------- | -------- | ------------------------------------------------------------------- |
| `npm_arguments` | Yes      | npm command and arguments (for example, `install`, `ci`, `publish`) |

### **Subcommands**

The following table lists common `jf npm` subcommands.

| Subcommand                       | Description                                                           |
| -------------------------------- | --------------------------------------------------------------------- |
| `install`, `i`, `isntall`, `add` | Install dependencies                                                  |
| `ci`                             | Install dependencies from package-lock (CI mode)                      |
| `publish`, `p`                   | Pack and deploy the package to the designated artifact repository     |
| `dist-tag`, `dist-tags`          | Manage distribution tags (uses the deployer repository configuration) |

Note: `jf npm --help` may list only `install`, `ci`, `publish`, and `help`. `dist-tag` and `dist-tags` are still supported. Invoke them the same way as with npm, for example `jf npm dist-tag add` `package@version` `tag`. Do not rely on `--help` alone for the full list of wrapped npm subcommands.

### **Build Options**

The following table describes `jf npm` options.

| Flag                 | Default | Description                                                                                                                                                                                                                                                                                                            |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--build-name`       | —       | Build name for build information (requires `--build-number`)                                                                                                                                                                                                                                                           |
| `--build-number`     | —       | Build number for build information (requires `--build-name`)                                                                                                                                                                                                                                                           |
| `--project`          | —       | JFrog Artifactory project key                                                                                                                                                                                                                                                                                          |
| `--module`           | —       | Optional module name for build information                                                                                                                                                                                                                                                                             |
| `--run-native`       | `false` | \[Deprecated] Use the `JFROG_RUN_NATIVE=true` environment variable instead. When set, uses the native npm client and the user's existing `.npmrc` configuration file. JFrog CLI will not create its own temporary `.npmrc`. All configurations, including authentication, must be handled by the user's `.npmrc` file. |
| `--detailed-summary` | `false` | Include a list of affected files in the command output summary (publish only)                                                                                                                                                                                                                                          |
| `--scan`             | `false` | Scan all files with JFrog Xray before upload. Skip upload if vulnerabilities are found (publish only).                                                                                                                                                                                                                 |
| `--format`           | `table` | Output format for the `--scan` option. Accepts `table`, `json`, `simple-json`, `sarif`, or `cyclonedx` (publish only).                                                                                                                                                                                                 |
| `--workspaces`       | `false` | Set to `true` to publish all packages defined in npm workspaces. Each workspace package is packed and deployed to JFrog Artifactory (publish only). Actual support follows your npm CLI version (workspace packing behavior is enforced by npm).                                                                       |

### **Publishing Scripts: Wrapped Compared to Native**

When building npm packages, it is important to understand how the `jf npm publish` command handles publishing scripts:

* Default behavior (without `--run-native`): JFrog CLI runs the `pack` command in the background, followed by an upload action not based on the npm client's native publish command. If your npm package includes `prepublish` or `postpublish` scripts, you must rename them to `prepack` and `postpack` respectively to ensure they are executed.
* Behavior with `--run-native`: The command uses the native npm client's own publish lifecycle. Standard npm script names such as `prepublish`, `publish`, and `postpublish` are handled directly by npm itself, and no renaming is necessary.

Note: The deployment view and details summary features are not supported by the `jf npm install` and `jf npm ci` commands. This limitation applies regardless of whether the `--run-native` flag is used.

### **Build Examples**

#### **Install Dependencies**

```shell
jf npm install
```

Expected output (truncated):

```
npm warn deprecated inflight@1.0.6: This module is not supported...
added 145 packages in 3s
```

#### **Publish With Build Information**

```shell
jf npm publish --build-name=<build_name> --build-number=<build_number>
```

Where:

* `<build_name>` and `<build_number>` identify the build-info record.

For example:

```shell
jf npm publish --build-name=my-app --build-number=42
```

Expected output:

```
npm notice Publishing to https://<server>.jfrog.io/artifactory/api/npm/npm-local/
+ my-package@1.0.0
```

#### **Run npm ci**

```shell
jf npm ci --build-name=my-app --build-number=1
```

#### **Install Using Native Mode**

Install dependencies using the native npm client, based on the `.npmrc` configuration:

```shell
export JFROG_RUN_NATIVE=true

jf npm install

jf npm install --build-name=my-native-build --build-number=1
```

#### **Publish npm Workspaces**

Publish all workspace packages in a monorepo:

```shell
jf npm publish --workspaces --build-name=my-monorepo --build-number=1
```

#### **Publish Using Native Mode**

```shell
export JFROG_RUN_NATIVE=true
jf npm publish
```

Ensure your `package.json` and `.npmrc` are configured for publishing.

***

## **How Does Native Mode Work for npm?**

npm supports native mode, which uses the user's `.npmrc` file instead of JFrog CLI-managed configuration. Unlike other tools, build-info collection still works in npm native mode.

Enable with `export JFROG_RUN_NATIVE=true` (the `--run-native` flag is deprecated).

For full setup instructions, per-tool comparison, and when to use each mode, see [Native mode](https://docs.jfrog.com/artifactory/docs/native-mode) in the JFrog documentation.

## **How Do You Use `jf npm` in GitHub Actions?**

The following workflow snippet shows a typical pattern.

```
# .github/workflows/build.yml
steps:
  - uses: actions/checkout@v4
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}
  - name: Configure npm
    run: jf npm-config --server-id-resolve=setup-jfrog-cli-server --repo-resolve=npm-virtual --server-id-deploy=setup-jfrog-cli-server --repo-deploy=npm-local
  - name: Install dependencies
    run: jf npm ci --build-name=my-app --build-number=${{ github.run_number }}
  - name: Publish build info
    run: jf rt build-publish my-app ${{ github.run_number }}
```

## **How Do You Troubleshoot `jf npm`?**

The following table lists common symptoms, causes, and fixes.

| Symptom                                                                                                                                                                                                      | Cause                                                                                                                                                        | Fix                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Error containing `no config file was found!` (full text continues: *Before running the 'jf npm' command on a project for the first time, the project should be configured with the 'jf npm-config' command*) | `jf npm-config` was not run, or wrong directory, or only global config exists                                                                                | Run `jf npm-config` in the project directory, or use the path under `~/.jfrog/projects/` if you used `--global`                              |
| 404 on `jf npm install`                                                                                                                                                                                      | Resolution repository does not exist, name is wrong, or `npm.yaml` was created with invalid repositories (`jf npm-config` does not validate repository keys) | Confirm repository keys in JFrog Artifactory and in `.jfrog/projects/npm.yaml`. Use an npm virtual repository for resolution where required. |
| `jf npm-config` reported success but the next command fails                                                                                                                                                  | Config step does not verify repositories                                                                                                                     | Fix `--repo-resolve` and `--repo-deploy` and re-run `jf npm-config`, or edit `npm.yaml`                                                      |
| 401 or 403 on install or publish                                                                                                                                                                             | Invalid credentials or insufficient permissions                                                                                                              | Re-run `jf config add` with a valid access token. Check repository permissions.                                                              |
| `jf npm publish` succeeds but package not visible                                                                                                                                                            | Published to wrong repository or repository type mismatch                                                                                                    | Confirm `--repo-deploy` points to an npm local repository                                                                                    |
| `prepublish` scripts not executing                                                                                                                                                                           | Wrapped mode uses `pack`, not `publish` lifecycle                                                                                                            | Rename `prepublish` and `postpublish` scripts to `prepack` and `postpack`, or use `--run-native`                                             |
| Build-info shows 0 dependencies                                                                                                                                                                              | `--build-name` and `--build-number` not passed together to `jf npm install` or `jf npm ci`                                                                   | Pass both flags to the install or `ci` command (they cannot be used separately)                                                              |

Enable debug logging: `export JFROG_CLI_LOG_LEVEL=DEBUG`

## **Frequently Asked Questions**

### **When must I run `jf npm-config`?**

Before the first `jf npm install` or `jf npm publish` on a project, run `jf npm-config` so `.jfrog/projects/npm.yaml` exists. See [How Do You Configure `jf npm-config`?](https://markdownlivepreview.com/#how-do-you-configure-jf-npm-config).

### **What is the difference between wrapped publish and `--run-native`?**

Wrapped mode runs `pack` then upload, so `prepublish` scripts may need to become `prepack`. Native mode uses npm's full publish lifecycle. See [Publishing Scripts: Wrapped Compared to Native](https://markdownlivepreview.com/#publishing-scripts-wrapped-compared-to-native).

### **Why do I see 404 after a successful `jf npm-config`?**

`jf npm-config` does not validate repository keys. Confirm keys in JFrog Artifactory and in `.jfrog/projects/npm.yaml`. See [Configuration Examples](https://markdownlivepreview.com/#configuration-examples).