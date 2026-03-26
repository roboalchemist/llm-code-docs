# Source: https://docs.socket.dev/docs/socket-fix.md

# socket fix

Update dependencies with fixable Socket alerts

The `socket fix` command automatically upgrades vulnerable dependencies in your project to secure versions, using intelligent upgrade planning to minimize the risk of breaking changes.

```text Text
socket fix --help

  Fix CVEs in dependencies

  Usage
    $ socket fix [options] [CWD=.]

  API Token Requirements
    - Quota: 101 units
    - Permissions: full-scans:create and packages:list

  Options
    --autopilot         Enable auto-merge for pull requests that Socket opens.
                        See GitHub documentation (​https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository​) for managing auto-merge for pull requests in your repository.
    --ecosystems        Limit fix analysis to specific ecosystems. Can be provided as comma separated values or as multiple flags. Defaults to all ecosystems.
    --exclude           Exclude workspaces matching these glob patterns. Can be provided as comma separated values or as multiple flags
    --fix-version       Override the version of @coana-tech/cli used for fix analysis. Default: 14.12.113.
    --id                Provide a list of vulnerability identifiers to compute fixes for:
                            - GHSA IDs (​https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-ghsa-ids​) (e.g., GHSA-xxxx-xxxx-xxxx)
                            - CVE IDs (​https://cve.mitre.org/cve/identifiers/​) (e.g., CVE-2025-1234) - automatically converted to GHSA
                            - PURLs (​https://github.com/package-url/purl-spec​) (e.g., pkg:npm/package@1.0.0) - automatically converted to GHSA
                            Can be provided as comma separated values or as multiple flags
    --include           Include workspaces matching these glob patterns. Can be provided as comma separated values or as multiple flags
    --json              Output as JSON
    --markdown          Output as Markdown
    --minimum-release-age  Set a minimum age requirement for suggested upgrade versions (e.g., 1h, 2d, 3w). A higher age requirement reduces the risk of upgrading to malicious versions. For example, setting the value to 1 week (1w) gives ecosystem maintainers one week to remove potentially malicious versions.
    --no-apply-fixes    Compute fixes only, do not apply them. Logs what upgrades would be applied. If combined with --output-file, the output file will contain the upgrades that would be applied.
    --no-major-updates  Do not suggest or apply fixes that require major version updates of direct or transitive dependencies
    --output-file       Path to store upgrades as a JSON file at this path.
    --pr-limit          Maximum number of pull requests to create in CI mode (default 10). Has no effect in local mode.
    --range-style       Define how dependency version ranges are updated in package.json (default 'preserve').
                        Available styles:
                          * pin - Use the exact version (e.g. 1.2.3)
                          * preserve - Retain the existing version range style as-is
    --show-affected-direct-dependencies  List the direct dependencies responsible for introducing transitive vulnerabilities and list the updates required to resolve the vulnerabilities

  Environment Variables (for CI/PR mode)
    CI                          Set to enable CI mode
    SOCKET_CLI_GITHUB_TOKEN     GitHub token for PR creation (or GITHUB_TOKEN)
    SOCKET_CLI_GIT_USER_NAME    Git username for commits
    SOCKET_CLI_GIT_USER_EMAIL   Git email for commits

  Examples
    $ socket fix
    $ socket fix --id CVE-2021-23337
    $ socket fix ./path/to/project --range-style pin
```

## Overview

Socket Fix gives developers a faster, safer way to clear vulnerabilities without endless manual upgrades. With Socket Fix, you can now:

* **Target specific vulnerabilities** - Fix the CVEs that matter most to your team
* **Apply fixes locally** - Test changes before committing
* **Support multiple ecosystems** - Works with npm, pnpm, Yarn, Maven [and many more](#supported-ecosystems)
* **Use intelligent upgrade planning** - Finds the least disruptive upgrade path

## How Socket Fix Works

Socket Fix uses an advanced compute-and-apply fix engine to intelligently resolve vulnerabilities:

1. **Scans your dependencies** - Identifies all vulnerable packages in your project
2. **Computes upgrade paths** - Determines the minimal set of changes needed to fix vulnerabilities
3. **Applies updates** - Modifies your manifest and lock files with the secure versions

### Example Fix Scenario

Suppose your application depends on `remark-reading-time@2.0.1\`:

* This version has a dependency constraint of `^1.3.0` on `estree-util-value-to-estree` ([link](https://socket.dev/npm/package/remark-reading-time/files/2.0.1/package.json))
* A vulnerability ([GHSA-f7f6-9jq7-3rqj](https://github.com/advisories/GHSA-f7f6-9jq7-3rqj)) affects all versions of `estree-util-value-to-estree` below 3.3.3
* The patched `remark-reading-time@2.0.2` updates its constraint to `^3.3.3` ([link](https://socket.dev/npm/package/remark-reading-time/files/2.0.2/package.json))
* Socket Fix automatically upgrades:
  * `estree-util-value-to-estree` to version `3.3.3` to fix the vulnerability
  * `remark-reading-time` to version `2.0.2` to ensure it's compatible with the new `estree-util-value-to-estree` version

## Usage

### Target Specific Vulnerabilities

Fix only specific CVEs or GHSA advisories using the `--id` flag:

```bash
# Fix a specific GHSA
$ socket fix --id GHSA-hhq3-ff78-jv3g

# Fix multiple vulnerabilities
$ socket fix --id GHSA-xxxx-xxxx-xxxx,GHSA-yyyy-yyyy-yyyy

# Using multiple flags
$ socket fix --id GHSA-xxxx-xxxx-xxxx --id GHSA-yyyy-yyyy-yyyy
```

### Fix all CVEs

Run `socket fix --all` in your project directory to automatically fix all fixable vulnerabilities:

```bash
$ socket fix --all
```

**Notice:** Use this mode with care. Upgrading many dependencies simultaneously makes it difficult to uncover the culprit if something breaks.

### Developer Workflow (Local Mode)

The developer-friendly workflow makes it easy to apply fixes locally:

1. **Run Socket Fix** in your project directory
2. **Review the changes** to your manifest and lock files
3. **Test your application** to ensure everything still works
4. **Open a pull request** with the changes

This workflow allows you to:

* Apply fixes locally before committing
* Test changes thoroughly
* Maintain control over what gets merged
* Document security updates in your commit history

### Create and Merge PRs (Autopilot Mode)

Run `socket fix --autopilot` in a GitHub action to automatically create PRs with the fixes that merge automatically if all checks pass.

Below is an example of how to set up the autopilot fix to run twice a day for a pnpm project:

```yaml
name: Socket Fix
on:
  schedule:
    - cron: '0 0 * * *'
    - cron: '0 12 * * *'
permissions:
  contents: write
  pull-requests: write
jobs:
  socket-fix:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8

      - name: Setup pnpm
        uses: pnpm/action-setup@a7487c7e89a18df4991f7f222e4898a00d66ddda
        with:
          version: '^10.16.0'

      - name: Setup Node.js with pnpm cache
        uses: actions/setup-node@a0853c24544627f65ddf259abe73b1d18a591444
        with:
          node-version: "22"
          cache: 'pnpm'

      - name: Install dependencies
        shell: bash
        run: >
          pnpm dlx @socketsecurity/cli pnpm install --config '{"issueRules":{"malware":true}}'

      - name: Run Socket Fix CLI
        env:
          SOCKET_CLI_GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SOCKET_CLI_GIT_USER_EMAIL: socket-fix[bot]@users.noreply.github.com
          SOCKET_CLI_GIT_USER_NAME: socket-fix[bot]
          SOCKET_CLI_API_TOKEN: ${{ secrets.SOCKET_CLI_API_TOKEN }}
        run: pnpm dlx @socketsecurity/cli fix --autopilot

```

## Options

### --id

Target specific vulnerabilities by their identifiers:

* **GHSA IDs**: GitHub Security Advisory Database identifiers

```bash
# Target a specific vulnerability
$ socket fix --id GHSA-f7f6-9jq7-3rqj
```

### --include / --exclude

Include folders matching these glob patterns. Can be provided as comma separated values or as multiple flags:

```Text Text
# Fix GHSA-f7f6-9jq7-3rqj in workspaces/utils
socket fix --id GHSA-f7f6-9jq7-3rqj --include "workspaces/utils"

# Fix GHSA-f7f6-9jq7-3rqj in all subprojects locates in workspaces
socket fix --id GHSA-f7f6-9jq7-3rqj --include "workspaces/*"

# Fix GHSA-f7f6-9jq7-3rqj in all folders workspaces/utils
socket fix --id GHSA-f7f6-9jq7-3rqj --exclude "workspaces/utils"
```

Notice that `socket fix` may make changes to manifest files outside the included folders if necessary to fix the vulnerability. For example, if fixing a vulnerability in folder `workspaces/utils` requires making updates to the `package-lock.json` in the root project.

### --pr-limit

Control the maximum number of PRs to open when running in a GitHub Actions workflow (default: 10). For example, if you set the limit to 10 and already have 6 open Socket Fix PRs, at most 4 new PRs will be opened:

```bash
# Fix and open PRs for at most 5 vulnerabilities
$ socket fix --pr-limit 5

# Fix and open PRs for at most 10 vulnerabilities
$ socket fix
```

### --range-style

Define how dependency version ranges are updated:

* **preserve** (default): Retains existing version range style
* **pin**: Uses exact versions (e.g., `1.2.3` instead of `^1.2.3`)

```bash
# Keep existing range style
$ socket fix --range-style preserve

# Pin to exact versions
$ socket fix --range-style pin
```

### --no-major-updates

Do not suggest or apply fixes that require changing the major version number in direct or transitive dependencies. This option reduces the probability that a fix breaks the application, but it also increases the probability that Socket is unable to find a valid fix for a CVE.

```shell
socket fix --no-major-updates
```

### --minimum-release-age

Set a minimum age requirement for suggested upgrade versions (e.g., 1h, 2d, 3w). A higher age requirement reduces the risk of updating to malicious package versions. For example, setting the value to 1 week (1w) gives ecosystem maintainers one week to remove potentially malicious versions from the ecosystem registry.

```shell
# Only update to package versions that are at least 3 days old
socket fix --minimum-release-age 3d

# Only update to package versions that are at least 2 weeks old
socket fix --minimum-release-age 2w
```

### Output Formats

#### --json

Output results in JSON format for programmatic processing:

```bash
$ socket fix --json
```

#### --markdown

Output results in Markdown format for documentation:

```bash
$ socket fix --markdown
```

### Getting Suggested Fixes

#### --no-apply-fixes

Computes the dependency upgrades necessary to fix the CVE, but does **not** apply the upgrades to the project. The suggested upgrades are printed to the console.

```shell bash
socket fix --no-apply-fixes
```

#### --output-file

Specify the file path where upgrades should be stored. The path must point to a file with a .json extension.

```shell
socket fix --output-file suggested-fixes.json
```

#### --show-affected-direct-dependencies

Shows you which direct dependencies introduced CVEs in transitive or direct dependencies.

```shell
# Show affected direct dependencies
socket fix --show-affected-direct-dependencies --id GHSA-6chw-6frg-f759,GHSA-v6h2-p8h4-qcjw --output-file fixes.json

# Upgrade the direct dependency, acorn, to version 5.7.4 to fix vulnerability GHSA-6chw-6frg-f759.
# Upgrade transitive dependency, brace-expansion, to version 1.1.12 to fix GHSA-v6h2-p8h4-qcjw. No direct dependency upgrades are required.
cat fixes.json
{
  "type": "only-direct-dependency-upgrades",
  "fixes": {
    "GHSA-6chw-6frg-f759": {
      "directDependencies": [
        {
          "purl": "pkg:npm/acorn@5.5.0",
          "fixedVersion": "5.7.4"
        }
      ]
    },
    "GHSA-v6h2-p8h4-qcjw": {
      "directDependencies": [
        {
          "purl": "pkg:npm/minimatch@3.0.4",
          "transitiveFixes": [
            {
              "purl": "pkg:npm/brace-expansion@1.1.11",
              "fixedVersion": "1.1.12"
            }
          ]
        }
      ]
    }
  }
}
```

## Supported Ecosystems

Socket Fix supports:

* **C#** (Nuget - packages.lock.json support is coming later)

* **Golang** (go.sum/go.mod)

* **Java** (Maven, Gradle with gradle.lockfile)

* **JavaScript/TypeScript** (npm, pnpm v6 or newer, Yarn classic and berry)

* **Python** (uv with uv.lock and requirements.txt)

* **Ruby** (RubyGems)

* **Rust** (Cargo)

**Coming Soon:**

* **Scala** (SBT)

## API Token Requirements

To use `socket fix`, your API token needs:

* **Quota**: 101 units per execution
* **Permissions**:
  * `full-scans:create` - to scan your dependencies
  * `packages:list` - to retrieve package information

## Examples

### Fix all vulnerabilities in current directory

```bash
$ socket fix --all
```

### Fix vulnerabilities in a specific project

```bash
$ socket fix ./proj/tree
```

### Target high-priority CVEs

```bash
$ socket fix --id GHSA-hhq3-ff78-jv3g
```

### Generate a fix report

```bash
$ socket fix --markdown > security-fixes.md
```

### Conservative approach with exact versions

```bash
$ socket fix --pr-limit 1 --range-style pin
```

## Best Practices

1. **Test locally first** - Run Socket Fix locally and test before pushing changes
2. **Use version control** - Commit before running Socket Fix for easy rollback
3. **Review changes** - Always review what Socket Fix changed in your dependencies
4. **Incremental updates** - Use `--pr-limit` or `--id` for gradual updates in large projects

## Notes

* Socket Fix respects your project's `.gitignore` file
* Only dependencies with known safe fixes are updated
* The command will not downgrade packages
* The fix engine uses sophisticated upgrade planning to minimize breaking changes