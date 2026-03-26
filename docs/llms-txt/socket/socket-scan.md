# Source: https://docs.socket.dev/docs/socket-scan.md

# socket scan

Scans related commands

A Scan is the core artifact that Socket creates and this command has several sub-commands to work with them.

```
$ socket scan --help

  Scan related commands

  Usage
    $ socket scan <command>

  Commands
    create            Create a scan
    del               Delete a scan
    diff              See what changed between two Scans
    list              List the scans for an organization
    metadata          Get a scan's metadata
    report            Check whether a scan result passes the organizational policies (security, license)
    setup             Start interactive configurator to customize default flag values for `socket scan` in this dir
    view              View the raw results of a scan

  Options
    (none)

  Examples
    $ socket scan --help
```

You can create, delete, view, diff Scans, its meta data, or a report of a Scan. You can see a list of scans in your org. You can also setup defaults for working with these sub-commands.

## `socket scan create`

This is probably the core command for this CLI. As the name suggests it creates a new scan. There's a few ways you can go about doing this;

```
$ socket scan create --help

  Create a new Socket scan and report

  Usage
    $ socket scan create [options] [TARGET...]

  API Token Requirements
    - Quota: 1 unit
    - Permissions: full-scans:create

  Options
    --auto-manifest     Run `socket manifest auto` before collecting manifest files. This is necessary for languages like Scala, Gradle, and Kotlin, See `socket manifest auto --help`.
    --branch            Branch name
    --commit-hash       Commit hash
    --commit-message    Commit message
    --committers        Committers
    --cwd               working directory, defaults to process.cwd()
    --default-branch    Set the default branch of the repository to the branch of this full-scan. Should only need to be done once, for example for the "main" or "master" branch.
    --interactive       Allow for interactive elements, asking for input. Use --no-interactive to prevent any input questions, defaulting them to cancel/no.
    --json              Output result as json
    --markdown          Output result as markdown
    --org               Force override the organization slug, overrides the default org from config
    --pull-request      Pull request number
    --reach             Run tier 1 full application reachability analysis
    --read-only         Similar to --dry-run except it can read from remote, stops before it would create an actual report
    --repo              Repository name
    --report            Wait for the scan creation to complete, then basically run `socket scan report` on it
    --set-as-alerts-page  When true and if this is the "default branch" then this Scan will be the one reflected on your alerts page. See help for details. Defaults to true.
    --tmp               Set the visibility (true/false) of the scan in your dashboard.

  Reachability Options (when --reach is used)
    --reach-analysis-memory-limit  The maximum memory in MB to use for the reachability analysis. The default is 8192MB.
    --reach-analysis-timeout  Set timeout for the reachability analysis. Split analysis runs may cause the total scan time to exceed this timeout significantly.
    --reach-disable-analytics  Disable reachability analytics sharing with Socket. Also disables caching-based optimizations.
    --reach-ecosystems  List of ecosystems to conduct reachability analysis on, as either a comma separated value or as multiple flags. Defaults to all ecosystems.
    --reach-exclude-paths  List of paths to exclude from reachability analysis, as either a comma separated value or as multiple flags.

  Uploads the specified dependency manifest files for Go, Gradle, JavaScript,
  Kotlin, Python, and Scala. Files like "package.json" and "requirements.txt".
  If any folder is specified, the ones found in there recursively are uploaded.

  Details on TARGET:

  - Defaults to the current dir (cwd) if none given
  - Multiple targets can be specified
  - If a target is a file, only that file is checked
  - If it is a dir, the dir is scanned for any supported manifest files
  - Dirs MUST be within the current dir (cwd), you can use --cwd to change it
  - Supports globbing such as "**/package.json", "**/requirements.txt", etc.
  - Ignores any file specified in your project's ".gitignore"
  - Also a sensible set of default ignores from the "ignore-by-default" module

  The --repo and --branch flags tell Socket to associate this Scan with that
  repo/branch. The names will show up on your dashboard on the Socket website.

  Note: for a first run you probably want to set --default-branch to indicate
        the default branch name, like "main" or "master".

  The "alerts page" (https://socket.dev/dashboard/org/YOURORG/alerts) will show
  the results from the last scan designated as the "pending head" on the branch
  configured on Socket to be the "default branch". When creating a scan the
  --set-as-alerts-page flag will default to true to update this. You can prevent
  this by using --no-set-as-alerts-page. This flag is ignored for any branch that
  is not designated as the "default branch". It is disabled when using --tmp.

  You can use `socket scan setup` to configure certain repo flag defaults.

  Examples
    $ socket scan create
    $ socket scan create ./proj --json
    $ socket scan create --repo=test-repo --branch=main ./package.json

```

* Basic scan
  * `socket scan create`
  * It will search your target directory for all manifest files that we support (*that's`requirements.txt`, `package.json`, `pom.xml`, etc.*) and upload them to Socket. No real source code just meta data about which packages your project depends on.
  * The server will respond with a URL for this Scan that you can access while it works on processing the Scan. It may not be done yet when you visit it. When it's ready, this page will tell you the result.
* Report
  * `socket scan create --report`
  * This starts with a basic Scan.
  * The server is then polled for completion.
  * Once completed it downloads the report and holds any alerts that may surface against the security and license policy set by your organization. When any alert violates any of these, the output will tell you with a "healthy" indicator.
  * Additionally, the exit code will reflect whether or not the Scan passed your org policies.
* With generated manifests
  * For certain languages we must generate concrete manifest files because the language itself does not have them. Two current examples are Scala's `sbt` and gradle (leveraged by Java, Kotlin, Scala).
  * These "manifests" are dynamic code that requires an unpredictable amount of files to collect as manifest files so instead we leverage the local build setup to generate the manifest files and scan those.
  * See the [`socket manifest`](socket-manifest) page for details.
* With [Tier 1 full application reachability analysis](full-application-reachability)
  * `socket scan create --reach`
  * This starts with a basic Scan.
  * It then runs a static code analysis on your code and the code of your dependencies to determine the reachability of CVEs. You can filter on 'CVE Reachability' when you view the scan in the dashboard.
  * Additionally, it writes a `.socket.facts.json` file to your project folder that contains the reachability data.

## Repo / Branch names

* `--repo` tells Socket to which repository this Scan belongs (default: `socket-default-repository`)
* `--branch` tells Socket to which branch this Scan belongs (default: `socket-default-branch`)

Repo names are required to follow these rules:

* Only `a-z A-Z 0-9` and `.`, `_`, and `-` are allowed
* Max length is 100

Branch names are required to follow these rules, which should be roughly equal to GitHub's branch names:

* be 1–255 characters long
* cannot be exactly `@` or `0`
* cannot begin or end with `/`, `.`, or `.lock`
* cannot contain `//`, `..`, `@{`, any control characters, spaces, or any of `; ~ ^ : ? * [ .`

### Head Scan

A concept currently called Head Scan is the scan that currently reflects the "dependencies" and "alerts" page in your dashboard. This must be a Scan on the "default" branch in a project.

### Default branch

Very similar to how branches in a git repository have a default branch, so do repositories on Socket have a default branch for each repository.

You can mark a repository as `default branch` by setting a flag. You only need to do this once per repo.

## `socket scan diff`

If you want to know what changed between two commits you can check a scan diff. This will take two Scan ID and compute the delta between the before and after Scan, then tell you exactly what changed in terms of dependencies and alerts.

```
$ socket scan diff --help

  See what changed between two Scans

  Usage
    $ socket scan diff [options] <SCAN_ID1> <SCAN_ID2>

  API Token Requirements
    - Quota: 1 unit
    - Permissions: full-scans:list

  This command displays the package changes between two scans. The full output
  can be pretty large depending on the size of your repo and time range. It is
  best stored to disk (with --json) to be further analyzed by other tools.

  Note: While it will work in any order, the first Scan ID is assumed to be the
        older ID, even if it is a newer Scan. This is only relevant for the
        added/removed list (similar to diffing two files with git).

  Options
    --depth           Max depth of JSON to display before truncating, use zero for no limit (without --json/--file)
    --file            Path to a local file where the output should be saved. Use `-` to force stdout.
    --interactive     Allow for interactive elements, asking for input. Use --no-interactive to prevent any input questions, defaulting them to cancel/no.
    --json            Output result as json
    --markdown        Output result as markdown
    --org             Force override the organization slug, overrides the default org from config

  Examples
    $ socket scan diff aaa0aa0a-aaaa-0000-0a0a-0000000a00a0 aaa1aa1a-aaaa-1111-1a1a-1111111a11a1
    $ socket scan diff aaa0aa0a-aaaa-0000-0a0a-0000000a00a0 aaa1aa1a-aaaa-1111-1a1a-1111111a11a1 --json
```

## `socket report`

This downloads a Scan and the security / license policies set by your organization and checks whether the Scan had any alerts that might violate any rules in those policies.

```
$ socket scan report --help

 Check whether a scan result passes the organizational policies (security, license)

  Usage
    $ socket scan report [options] <SCAN_ID> [OUTPUT_PATH]

  API Token Requirements
    - Quota: 2 units
    - Permissions: full-scans:list security-policy:read

  Options
    --fold            Fold reported alerts to some degree
    --interactive     Allow for interactive elements, asking for input. Use --no-interactive to prevent any input questions, defaulting them to cancel/no.
    --json            Output result as json
    --license         Also report the license policy status. Default: false
    --markdown        Output result as markdown
    --org             Force override the organization slug, overrides the default org from config
    --reportLevel     Which policy level alerts should be reported
    --short           Report only the healthy status

  When no output path is given the contents is sent to stdout.

  By default the result is a nested object that looks like this:
    `{
      [ecosystem]: {
        [pkgName]: {
          [version]: {
            [file]: {
              [line:col]: alert
    }}}}`
  So one alert for each occurrence in every file, version, etc, a huge response.

  You can --fold these up to given level: 'pkg', 'version', 'file', and 'none'.
  For example: `socket scan report --fold=version` will dedupe alerts to only
  show one alert of a particular kind, no matter how often it was foud in a
  file or in how many files it was found. At most one per version that has it.

  By default only the warn and error policy level alerts are reported. You can
  override this and request more ('defer' < 'ignore' < 'monitor' < 'warn' < 'error')

  Short responses look like this:
    --json:     `{healthy:bool}`
    --markdown: `healthy = bool`
    neither:    `OK/ERR`

  Examples
    $ socket scan report 000aaaa1-0000-0a0a-00a0-00a0000000a0 --json --fold=version
    $ socket scan report 000aaaa1-0000-0a0a-00a0-00a0000000a0 --license --markdown --short
```

Here's what that would kind of look like:

```
$ socket scan report 000aaaa1-0000-0a0a-00a0-00a0000000a0

ℹ Scan result: success. Security policy: received policy.
✔ Generated reported in 1 ms
{
  healthy: true,
  orgSlug: 'bearDev',
  scanId: '000aaaa1-0000-0a0a-00a0-00a0000000a0',
  options: { fold: 'none', reportLevel: 'warn' },
  alerts: Map(0) {}
}
```

The report will include the alerts and a simple boolean flag for whether the report passes or not, called "healthy".

## View / Del / Metadata

There are a few commands to organize Scans in your repository. These are fairly straightforward.

## Setup defaults

You can start an interactive prompt to generate a `socket.json` in your target directory with defaults for running scans in this directory. ([More details here](https://docs.socket.dev/docs/socketjson))

```
socket scan setup ./proj
```

This is helpful for setting up defaults for flags like `--repo` (the name of the repo of this directory), `--branch` the name of (presumably default) branch of this directory. And a few more.

This way, you can just do `socket scan create ./proj` and it could prefill `--repo website --branch main` for you.

## Automation

Note that most of these commands support

* `--json` for a raw payload (which you can forward to `jq`)
* `--markdown` for easy sharing

## Automation

While we try to offer simpler ways of combining these commands, like `socket ci` and `socket scan create --report`, we recognize that there may always be desires to customize your chain. And that's totally fine!

Here is an automation example of running it as part of your CI logic

```
socket scan create \
  --report \
  --repo="$CI_PROJECT_NAME" \
  --branch="$CI_COMMIT_REF_NAME" \
  ./proj
```

This will create the scan on the `./proj` directory, wait for the report, and have exit code `0` for success or `1` if the Scan does not pass your security policy or license policy *(or if an error occurred)*.

Make sure you set the env vars to the appropriate values. For example, GitLab should expose the `CI_PROJECT_NAME` variable. Each environment will have their own set of env vars exposed.