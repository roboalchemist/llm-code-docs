# Source: https://docs.infrahub.app/topics/branch-synchronization.md

# Selective branch synchronization

Infrahub automatically creates all branches from a connected Git repository by default. While this ensures full visibility, it can create unnecessary noise when many Git branches are unrelated to Infrahub data or workflows. Selective branch synchronization introduces an optional configuration that allows teams to control which Git branches are imported and synchronized into Infrahub based on custom naming patterns.

## Why selective synchronization matters[​](#why-selective-synchronization-matters "Direct link to Why selective synchronization matters")

In real-world Git repositories, teams often maintain many branches for different purposes:

* Development branches for features unrelated to infrastructure
* Documentation-only branches
* Experimental work that doesn't involve Infrahub data
* Personal development branches
* Archive branches kept for historical reference

When all these branches automatically sync to Infrahub, it creates:

* **Visual clutter**: Branch lists become difficult to navigate with irrelevant entries
* **Performance overhead**: Unnecessary synchronization consumes system resources
* **Workflow confusion**: Team members may struggle to identify which branches contain infrastructure changes

Selective synchronization addresses these challenges by allowing administrators to define explicit rules for which branches should be imported and maintained in Infrahub.

## How selective synchronization works[​](#how-selective-synchronization-works "Direct link to How selective synchronization works")

The feature operates through a set of branch naming rules that determine which Git branches Infrahub will track and synchronize.

### Default behavior[​](#default-behavior "Direct link to Default behavior")

By default, every branch created in your Git repository continues to be automatically imported and synchronized into Infrahub. No configuration changes are required for teams who want to maintain the current behavior.

This default ensures backward compatibility and zero-configuration operation for existing deployments.

### Enabling selective synchronization[​](#enabling-selective-synchronization "Direct link to Enabling selective synchronization")

When you enable selective branch synchronization, Infrahub will only import branches whose names match a set of user-defined rules. Each rule is a regular expression that defines a pattern for matching branch names.

Setup guide

To configure selective branch synchronization in your Infrahub instance, see [Configure selective branch synchronization](/guides/selective-branch-sync.md).

info

Selective synchronization only affects the Git to Infrahub direction. Branches created in Infrahub with the "sync to Git" option enabled will still synchronize to Git normally.

## Rule processing[​](#rule-processing "Direct link to Rule processing")

Infrahub processes the rules in the order they appear in the configuration. The first matching expression determines whether a branch is synchronized.

**Processing logic:**

1. When Infrahub discovers a branch in the Git repository, it evaluates the branch name against each rule in sequence
2. The first rule that matches the branch name determines the outcome
3. If a match is found, the branch will be created and synchronized in Infrahub
4. If no match is found after checking all rules, the branch will be ignored

This top-to-bottom evaluation allows for fine-grained control over branch synchronization behavior.

### Rule evaluation during updates[​](#rule-evaluation-during-updates "Direct link to Rule evaluation during updates")

When you modify the synchronization rules after a repository has been imported, Infrahub evaluates branches differently depending on their current state:

**For new Git branches that now match the updated rules:**

If a Git branch exists but was not previously imported because it didn't match the old rules, and it now matches the updated rules, Infrahub will import that branch during the next synchronization cycle. This allows you to expand your synchronization scope by adding new patterns.

**For existing Infrahub branches that no longer match the updated rules:**

If a branch was already imported into Infrahub and has the "sync with Git" flag enabled, it will continue to synchronize even if it no longer matches the updated rules. This preserves existing work and prevents unexpected data loss. Once a branch exists in Infrahub with Git synchronization enabled, the branch naming rules no longer apply to it.

info

The synchronization rules only control initial import of branches from Git to Infrahub. Once a branch exists in Infrahub with Git synchronization enabled, it continues syncing regardless of rule changes.

## Regular expression patterns[​](#regular-expression-patterns "Direct link to Regular expression patterns")

Each rule uses standard regular expression syntax to define matching patterns. This approach provides maximum flexibility without enforcing a specific naming convention.

Common pattern elements you can use:

* `^` - Match the beginning of the branch name
* `$` - Match the end of the branch name
* `.*` - Match any characters (zero or more)
* `[a-z]` - Match any lowercase letter
* `[0-9]+` - Match one or more digits
* `(feature|fix)` - Match either "feature" or "fix"

### Example 1: infrastructure-only branches[​](#example-1-infrastructure-only-branches "Direct link to Example 1: infrastructure-only branches")

Your team uses a naming convention where all infrastructure-related branches start with `infra/`.

**Rule:**

```
["^infra/.*$"]
```

**Results:**

| Git Branch Name        | Matches Rule? | Imported to Infrahub?  |
| ---------------------- | ------------- | ---------------------- |
| `infra/network-update` | ✅ Yes        | ✅ Created in Infrahub |
| `infra/add-devices`    | ✅ Yes        | ✅ Created in Infrahub |
| `docs/update-readme`   | ❌ No         | 🚫 Not imported        |
| `feature/new-api`      | ❌ No         | 🚫 Not imported        |

### Example 2: multiple team prefixes[​](#example-2-multiple-team-prefixes "Direct link to Example 2: multiple team prefixes")

Different teams use different prefixes for their infrastructure work.

**Rules:**

```
[
  "^infra/.*$",
  "^network/.*$",
  "^config/.*$"
]
```

**Results:**

| Git Branch Name     | Matches Rule? | Imported to Infrahub?  |
| ------------------- | ------------- | ---------------------- |
| `infra/devices`     | ✅ Yes        | ✅ Created in Infrahub |
| `network/topology`  | ✅ Yes        | ✅ Created in Infrahub |
| `config/templates`  | ✅ Yes        | ✅ Created in Infrahub |
| `docs/architecture` | ❌ No         | 🚫 Not imported        |

### Example 3: feature branches with issue numbers[​](#example-3-feature-branches-with-issue-numbers "Direct link to Example 3: feature branches with issue numbers")

Your workflow includes Infrahub-related feature branches that reference issue numbers.

**Rule:**

```
["^feature/infrahub-[0-9]+.*$"]
```

**Results:**

| Git Branch Name                | Matches Rule? | Imported to Infrahub?  |
| ------------------------------ | ------------- | ---------------------- |
| `feature/infrahub-321`         | ✅ Yes        | ✅ Created in Infrahub |
| `feature/infrahub-123-network` | ✅ Yes        | ✅ Created in Infrahub |
| `feature/api-update`           | ❌ No         | 🚫 Not imported        |
| `feature/device-backup`        | ❌ No         | 🚫 Not imported        |

## Current scope and limitations[​](#current-scope-and-limitations "Direct link to Current scope and limitations")

### Directional behavior[​](#directional-behavior "Direct link to Directional behavior")

Selective branch synchronization only affects the **Git → Infrahub** direction:

* Git branches that don't match the rules will not be imported into Infrahub
* Branches created in Infrahub with the "sync to Git" option enabled will still synchronize to Git normally
* This asymmetric behavior allows teams to use Infrahub as the source of truth while filtering incoming Git branches

### Dynamic updates[​](#dynamic-updates "Direct link to Dynamic updates")

When you modify the `sync_branch_names` configuration:

* New Git branches will be evaluated against the updated rules during the next synchronization
* Git branches that now match the rules will be automatically imported
* Existing Infrahub branches with Git synchronization enabled continue syncing regardless of rule changes
* Branches no longer matching the rules will **not** be automatically removed from Infrahub
* You must manually delete branches in Infrahub if they no longer align with your synchronization policy

### Repository types[​](#repository-types "Direct link to Repository types")

Selective branch synchronization applies to standard read-write repositories that support full bidirectional integration. Read-only repositories track a single reference and are not affected by this configuration.

## Further reading[​](#further-reading "Direct link to Further reading")

* [Configure selective branch synchronization](/guides/selective-branch-sync.md) - Step-by-step setup guide
* [Understanding Git repositories in Infrahub](/topics/repository.md) - Repository integration concepts and architecture
* [How to connect external Git repositories](/guides/repository.md) - Step-by-step repository setup guide
* [Understanding branching in Infrahub](/topics/branching.md) - Branch isolation, hierarchy, and workflows
* [Configuration reference](/reference/configuration.md) - Complete configuration options including Git settings
