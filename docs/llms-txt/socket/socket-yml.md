# Source: https://docs.socket.dev/docs/socket-yml.md

# socket.yml

Optional Socket GitHub App configuration file

You can optionally configure the Socket GitHub app and CLI by adding a `socket.yml` file to the root of your repo.

```yaml
# top level version field is required
version: 2

projectIgnorePaths:
  - "ignored-folder"
  - "foo/bar/package.json"

# only trigger pull request alerts when these files change.
triggerPaths:
  - "package.json"
  - "package-lock.json"

issueRules:
  unresolvedRequire: false

githubApp:
  enabled: true # enable/disable the Socket.dev GitHub app entirely
  dependencyOverviewEnabled: true # enable/disable GitHub app dependency overview comments in pull request alerts.
  ignoreUsers: ["aBotOnGitHub"]
  disableCommentsAndCheckRuns: false
```

> 🚧 Note
>
> The `socket.yml` file is only supported in the root of your repo. The 4 letter extension variant is also supported (`socket.yaml`). If both extensions are present, `socket.yml` wins.

## Fields

All fields listed here are optional, except for the version field.

### `version`

The version field should not be omitted and should be set to 2. If it is missing or a lower number, see below for a migration guide. The `version` field sets the configuration schema used to validate `socket.yml`.

### `projectIgnorePaths`

The `projectIgnorePaths` key is an array of strings that are used to ignore folders or files.

The individual strings in the `projectIgnorePaths` array work like [`.gitignore`](https://git-scm.com/docs/gitignore) patterns.

The following patterns are always included in the ignore array by default:

* `node_modules`
* `.yarn`

> 🚧 Mind the YAML
>
> When using gitignore directives like `!` and `*`, be sure that you wrap your selector rules in `"` (double quotes). YAML supports some unquoted strings, however some characters break this feature so its safer to wrap your strings in `"`.

#### Advanced `projectIgnorePaths` example

If you prefer to ignore ingesting all package manifest files by default, and instead only ingest specific files, you could utilize the following ignore string patterns to achieve that:

```Text yaml
projectIgnorePaths:
  - "/*"
  - "!/package.json"
  - "!/package-lock.json"
  - "!/workspaces"
  - "/workspaces/*"
  - "!/workspaces/foo"
  - "!/workspaces/bar"

```

In this example, we ignore everything in the root of the repo, unignore the workspaces directory and top level dependency manifests, ignore everything in the workspaces directory, then unignore the `foo` and `bar` subfolders. Any other folders in the `workspaces` directory will be ignored.

### `triggerPaths`

The `triggerPaths` key is an array of strings that are used to match against files modified in pull requests and determine if a Pull Request alert scan should be performed.

The individual strings in the `triggerPaths` array work like [`.gitignore`](https://git-scm.com/docs/gitignore) patterns, except instead of matching files to ignore, match files that will trigger reports. When `triggerPaths` is omitted, the default rule set of `["*"]` is used. The `triggerPath` rules are matched against all modified files inside of a pull request. If any of the rules match a file in a pull request, a Pull Request alert report is run and a check run indicator is displayed.

This is a useful setting if you have a large monorepo and only want to roll socket out to a few sub-projects at a given time. It also separates out the report ingestion rules from the trigger rules so you can continue to ingest top level dependency manifest files that are common in monorepos but change frequently in shared contexts.

`triggerPaths` determines when to run Pull Request alert reports, and `projectIgnorePaths` determines which paths are included when ingesting package manifest files for the report. Socket Security only ever ingests package manifest files and never any other source code.

#### `triggerPaths` example

If you only wanted to roll out the Socket Security GitHub app on the following directories in your repo:

* `/workspaces/foo`
* `/workspaces/bar`

You could implement the following `triggerPaths` rule.

```yaml
triggerPaths:
  - "/workspaces/foo"
  - "/workspaces/bar"

```

If you combined this `triggerPaths` with the above `projectIgnorePaths` example above, Pull request alerts from Socket would only run when the pull request contained modified files inside of the `foo` and `bar` workspaces folder.

### `issueRules`

> 🚧 issueRules are deprecated
>
> While currently supported, we intend to replace `socket.yml`'s `issueRules` with [repository labels](https://socket.dev/blog/introducing-repository-labels-and-security-policies). Repository labels provide the same functionality as `issueRules`, but with additional flexibility to apply the same rules to multiple repositories.

`issueRules` is a map of issue names from Socket's [Issues](https://socket.dev/npm/issue) page that allows you to enable or disable issue alerts in your pull requests. Issues are identified by the url slug of the corresponding issue page. The default issues map looks like this:

```yaml
issueRules:
  didYouMean: true
  installScripts: true
  telemetry: true
  troll: true
  malware: true
  hasNativeCode: true
  shellScriptOverride: true
  gitDependency: true
  httpDependency: true
  invalidPackageJSON: true
  unresolvedRequire: true
```

You can disable issue by setting it's value to false. You can also enable alerts for any other issue that isn't enabled by default by setting the issue slug value to true in the issues map.

If any issue keys are omitted (having no entry at all in `socket.yml`) they will use the values from the relevant Socket dashboard settings page.

### `githubApp`

The `githubApp` is a map of settings that correspond to the [Socket GitHub app](/docs/socket-for-github-installation). The contained settings are described below.

### `githubApp.enabled`

Default: `true`.

If you want the Socket GitHub app to never run on a repo and do not have org permissions to disable GitHub access to that repo, you can add a `socket.yml` file to your repo and set `enabled` to false.

Setting `enabled` to `false` will override other settings in the `socket.yml` associated with the GitHub app.

### `githubApp.pullRequestAlertsEnabled`

Default: `true`.

The `pullRequestAlertsEnabled` field can be used to individually disable pull request alerts check runs and pull request comments generated by the Socket.dev GitHub app.

The `enabled` field must be set to `true` for this field to have any effect.

### `githubApp.dependencyOverviewEnabled`

Default: `true`.

The `dependencyOverviewEnabled` field can be used to individually disable dependency overview comments in pull requests.

The `enabled` and  `pullRequestAlertsEnabled` field must be set to `true` for this field to have any effect.

### `githubApp.projectReportsEnabled`

Default: `true`.

The `projectReportsEnabled` field can be used to individually disable project reports check runs for commits from being generated.

The `enabled` field must be set to `true` for this field to have any effect.

### `githubApp.ignoreUsers`

Default: `[]`

The `ignoreUsers` is an optional array of strings that let you specify GitHub usernames that will prevent Pull Request Alerts from running on Pull Requests that are opened by anyone specified in this array. This can be useful in merge queues or other bot related circumstances.

### `githubApp.disableCommentsAndCheckRuns`

Default: `false`

If you set "Disable Comments and Check Runs" to true in your organization settings, the GitHub app will continue to ingest and create reports on the repos that are installed in your Socket GitHub App installation, but will not post any comments or create check run status indicators in pull requests and commits. You can use this setting to override the organization setting for a specific repo.

If "Disable Comments and Check Runs" is set to `true` in org settings, and `githubApp.disableCommentsAndCheckRuns` is set to `false` in `socket.yml`, the repo will continue getting comments and check run status indicators.

If "Disable Comments and Check Runs" is set to `false` in org settings, and `githubApp.disableCommentsAndCheckRuns` is set to `true` in `socket.yml`, the repo will continue creating reports that populate in your Socket org dashboard, but will not receive any check run status indicators or comments in pull requests.

## Version 1 to Version 2 migration

To migrate a Version 1 `socket.yml` to version 2, perform the following changes:

* Add the top level `version` key set to the value `2`
* Rename the `ignore` key to `projectIgnorePaths`
* Rename the `issues` key to `issueRules`
* Move the `enabled`, `projectReportsEnabled` and `pullRequestAlertsEnabled` keys under a top level `githubApp` key.
* Remove the `beta` key

Existing v1 configuration files will continue to work, however newly added settings may not be accessible until you migrate your configuration to version 2. Internal details on configuration parsing can be found in the [SocketDev/socket-config-js repo](https://github.com/SocketDev/socket-config-js).