# Dependabot Configuration Reference

Source: https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference

## File Location

The `dependabot.yml` file must be stored in the `.github` directory of your repository:

```
.github/dependabot.yml
```

## Basic Structure

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
```

All values are case-sensitive.

## Required Fields

### version

Always set to `2` for the latest Dependabot configuration format.

```yaml
version: 2
```

### updates

Array of package managers to monitor. Each entry requires:
- `package-ecosystem`
- `directory` or `directories`
- `schedule.interval`

## Configuration Options

### package-ecosystem

Specifies the package manager to monitor.

**Supported values:**
- `bundler` (Ruby)
- `pip` (Python)
- `npm` (Node.js)
- `yarn` (Node.js, alternative)
- `pnpm` (Node.js, alternative)
- `composer` (PHP)
- `cargo` (Rust)
- `hex` (Erlang)
- `nuget` (.NET)
- `maven` (Java)
- `gradle` (Java)
- `docker` (Docker)
- `terraform` (Terraform)
- `helm` (Kubernetes)
- `go` (Go modules)
- `pub` (Dart)
- `elm` (Elm)
- `deno` (Deno)
- `mix` (Elixir)
- `rebar3` (Erlang)
- And others

```yaml
updates:
  - package-ecosystem: "npm"
```

### directory

Single directory containing dependency manifests.

```yaml
directory: "/"
directory: "/src"
directory: "/packages/app"
```

### directories (alternative)

Update multiple directories with the same configuration.

```yaml
directories:
  - "/"
  - "/app"
  - "/utils"
```

### schedule

Defines when Dependabot checks for updates.

#### schedule.interval

**Required**. Update frequency.

**Values:**
- `daily`
- `weekly` (default)
- `monthly`
- `quarterly`
- `semiannually`
- `yearly`

```yaml
schedule:
  interval: "weekly"
```

#### schedule.day

Day of the week for weekly updates (Monday-Sunday).

```yaml
schedule:
  interval: "weekly"
  day: "monday"
```

#### schedule.time

Time of day for updates (00:00-23:59 UTC).

```yaml
schedule:
  interval: "daily"
  time: "03:00"
```

#### schedule.timezone

Timezone for the `time` setting. Use IANA timezone identifiers.

```yaml
schedule:
  interval: "daily"
  time: "09:00"
  timezone: "America/Los_Angeles"
```

#### schedule.cron

Custom cron expression for advanced scheduling (overrides interval/day/time).

```yaml
schedule:
  cron: "0 3 * * 1"  # 3 AM every Monday UTC
```

### allow

Specify which dependencies to update.

```yaml
allow:
  - dependency-name: "express"
  - dependency-name: "lodash*"
```

### ignore

Exclude specific dependencies from updates.

```yaml
ignore:
  - dependency-name: "express"
    versions: ["4.0.0", "5.0.0"]
  - dependency-name: "lodash*"
```

### dependency-type

Filter dependencies by type.

**Values:**
- `direct`
- `indirect`
- `all` (default)
- `production`
- `development`

```yaml
dependency-type: "direct"
dependency-type: "production"
```

### assignees

Automatically assign reviewers to pull requests.

```yaml
assignees:
  - "alice"
  - "bob"
```

### labels

Add labels to pull requests.

```yaml
labels:
  - "dependencies"
  - "automated"
```

### milestone

Associate PRs with a milestone.

```yaml
milestone: 1
```

### commit-message

Customize commit message formatting.

```yaml
commit-message:
  prefix: "chore(deps):"
  include: "scope"
```

### pull-request-branch-name.separator

Customize branch naming convention.

```yaml
pull-request-branch-name:
  separator: "-"  # "dependabot-npm-express-4.0.0"
  separator: "/"  # "dependabot/npm/express-4.0.0"
```

### open-pull-requests-limit

Maximum concurrent Dependabot pull requests.

**Default:** 5
**Range:** 1-99

```yaml
open-pull-requests-limit: 10
```

### rebase-strategy

How to handle conflicts.

**Values:**
- `auto` (default) - Automatically rebase and force-push
- `disabled` - Don't rebase automatically

```yaml
rebase-strategy: "disabled"
```

By default, Dependabot automatically rebases pull requests to resolve conflicts. After 30 days without merging, Dependabot stops automatic rebasing.

### target-branch

Specify a non-default branch for updates.

```yaml
target-branch: "develop"
```

### versioning-strategy

Control how version changes are applied.

**Values:**
- `auto` (default) - Detect best strategy
- `increase` - Always increase versions
- `increase-if-necessary` - Only increase if required
- `lockfile-only` - Only update lock files
- `widen` - Widen version ranges

```yaml
versioning-strategy: "increase-if-necessary"
```

### groups

Consolidate multiple dependency updates into single pull requests.

```yaml
groups:
  production-dependencies:
    dependency-type: "production"
  development-dependencies:
    dependency-type: "development"
    exclude-patterns:
      - "eslint*"
```

### multi-ecosystem-groups

Span groups across multiple package managers.

```yaml
multi-ecosystem-groups:
  all-dependencies:
    package-ecosystems:
      - "npm"
      - "pip"
```

### cooldown

Delay updates with customizable periods.

```yaml
cooldown:
  default-days: 3
  semver-patch-days: 0
  semver-minor-days: 3
  semver-major-days: 7
```

### registries

Configure access to private package registries.

```yaml
registries:
  npm-registry:
    type: "npm-registry"
    url: "https://registry.npmjs.org"
    username: "my-username"
    password: "${{ secrets.NPM_TOKEN }}"
```

### vendor

Update vendored dependencies (cached in repository).

```yaml
vendor: true
```

### exclude-paths

Ignore specific directories or files.

```yaml
exclude-paths:
  - "vendor/"
  - "node_modules/"
```

### insecure-external-code-execution

Allow code execution during dependency updates (required for some ecosystems).

```yaml
insecure-external-code-execution: "allow"
```

## Complete Example

```yaml
version: 2
updates:
  # Python
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "03:00"
      timezone: "America/Los_Angeles"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "python"
    assignees:
      - "alice"
    dependency-type: "production"

  # Node.js
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    groups:
      production:
        dependency-type: "production"
      development:
        dependency-type: "development"
    rebase-strategy: "auto"

  # Docker
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
```

## Variable Substitution

Use GitHub Actions secrets in registry credentials:

```yaml
registries:
  custom-registry:
    type: "npm-registry"
    username: "my-user"
    password: "${{ secrets.REGISTRY_TOKEN }}"
```

## Notes

- All configuration is case-sensitive
- File must be valid YAML (use a YAML validator)
- Comments starting with `#` are allowed
- Empty values must be quoted: `directory: ""`
