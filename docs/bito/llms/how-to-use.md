# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/how-to-use.md

# Source: https://docs.bito.ai/ai-code-reviews-in-cli/how-to-use.md

# How to use?

Get up and running in minutes. This guide walks you through running your first code review from the terminal and shows common workflows you can adopt right away.

## Prerequisites

Before you begin, make sure you have:

* ✅ Installed the CLI ([Installation guide](https://docs.bito.ai/ai-code-reviews-in-cli/installation-guide))
* ✅ Configured your [Bito API key (aka Bito Access Key)](https://docs.bito.ai/help/account-and-settings/access-key)
* ✅ A Git repository with code changes (committed or uncommitted)

## Run your first code review

#### Review all changes (default)

From your project's root directory, run:

```shellscript
bitoreview review
```

**Command format:**

```shellscript
bitoreview review [files...] [options]
```

**Options:**

|           Flag           |                    Description                   |
| :----------------------: | :----------------------------------------------: |
|    `-t, --type <type>`   |  Review scope: `all`, `uncommitted`, `committed` |
|    `-i, --interactive`   |        Enable interactive fix application        |
|         `--plain`        |           Plain text output (no colors)          |
|      `--prompt-only`     |      Minimal output optimized for AI agents      |
|     `--focus <area>`     |           Focus area (see Focus Areas)           |
|      `--mode <mode>`     | `essential` (HIGH only) or `comprehensive` (all) |
|   `--severity <level>`   |    Filter by severity: `high`, `medium`, `low`   |
|     `--base <branch>`    |            Base branch for comparison            |
| `--base-commit <commit>` |          Specific commit for comparison          |
|      `--scm <type>`      |  Override SCM: `git`, `svn`, `hg`, `p4`, `plain` |
|   `-c, --config <path>`  |              Custom config file path             |
|     `--api-key <key>`    |               Pass API key directly              |
|      `--cwd <path>`      |               Set working directory              |
|       `-d, --debug`      |                Enable debug output               |
|      `-v, --verbose`     |              Enable verbose logging              |
|   `--max-retries <num>`  |            Retry attempts (default: 2)           |
|       `--no-color`       |              Disable colored output              |

{% hint style="info" %}
For complete reference of CLI commands, refer to [Available commands](https://docs.bito.ai/ai-code-reviews-in-cli/available-commands).
{% endhint %}

#### Review only uncommitted changes

Use this while actively coding, before committing:

```shellscript
bitoreview review --type uncommitted
```

#### Review only committed changes

Review commits that haven't been pushed yet:

```shellscript
bitoreview review --type committed
```

#### Review specific files

Limit the review scope to specific files:

```shellscript
bitoreview review src/api/*.js src/utils/helper.js
```

#### Review changes against a specific branch

Compare your current branch with another branch (for example, `main`):

```shellscript
bitoreview review --base main
```

#### Review changes against a specific commit

Compare your current code with a specific commit by providing its hash:

```shellscript
bitoreview review --base-commit abc123
```

{% hint style="info" %}
**Note:** replace `abc123` with your actual commit hash.
{% endhint %}

#### Short alias for `bitoreview` command

You can use `br` as a shortcut:

```shellscript
br review
```

```shellscript
br review --type uncommitted
```

## Review modes

{% stepper %}
{% step %}

### Essential mode (fast, critical issues only)

* Only shows HIGH severity issues
* Ideal for CI/CD pipelines and pre-commit hooks
* Quick, focused feedback

```shellscript
bitoreview review --mode essential
```

{% endstep %}

{% step %}

### Comprehensive mode (full analysis)

* Shows all severity levels (HIGH, MEDIUM, LOW)
* Thorough analysis for pull requests and code audits
* This is the **default mode**.

```shellscript
bitoreview review --mode comprehensive
```

{% endstep %}
{% endstepper %}

## Focus areas

Use `--focus <area>` to concentrate the review on specific aspects:

|    Focus area    |                      Description                      |
| :--------------: | :---------------------------------------------------: |
|    `security`    |  SQL injection, authentication, data validation, XSS  |
|   `performance`  | Bottlenecks, memory leaks, optimization opportunities |
|      `bugs`      |        Logic errors, edge cases, runtime errors       |
| `best-practices` |      Code style, design patterns, maintainability     |
|      `tests`     |        Test coverage, test quality, testability       |
|  `documentation` |         Comments, documentation, code clarity         |

**Example:**

```shellscript
bitoreview review --focus security --mode essential
```

## Severity levels

|   Level  |                          Description                          |
| :------: | :-----------------------------------------------------------: |
|  `high`  | Must-fix: crashes, security vulnerabilities, breaking changes |
| `medium` |     Should-fix: best practice violations, moderate issues     |
|   `low`  |    Nice-to-have: formatting, minor refactoring suggestions    |

Filter by minimum severity:

```shellscript
bitoreview review --severity high
```

## Output formats

{% stepper %}
{% step %}

### Interactive mode (default)

Rich terminal UI with:

* Colored output
* Tables for metrics and issues
* Real-time progress spinners

```shellscript
bitoreview review
```

{% endstep %}

{% step %}

### Plain text mode

No colors, suitable for logs and CI/CD:

```shellscript
bitoreview review --plain
```

Save to file:

```shellscript
bitoreview review --plain > review-report.txt
```

{% endstep %}

{% step %}

### Prompt-only mode

Minimal output optimized for AI agents:

```shellscript
bitoreview review --prompt-only
```

{% endstep %}
{% endstepper %}

## Interactive fix application

Enable interactive mode to review and apply suggested fixes one by one:

```shellscript
bitoreview review --interactive
# or
bitoreview review -i
```

#### Interactive prompts

For each fixable issue, you'll see:

| Option     | Action                                      |
| ---------- | ------------------------------------------- |
| `y` (yes)  | Apply this fix                              |
| `n` (no)   | Skip this fix                               |
| `s` (skip) | Same as 'no'                                |
| `a` (all)  | Apply all remaining fixes without prompting |
| `q` (quit) | Exit interactive mode                       |

#### Backup files

When fixes are applied, backup files are automatically created with the `.bitoreview-backup` extension.

## Multi-SCM support

The CLI automatically detects your version control system:

|     SCM     |     Detection    |
| :---------: | :--------------: |
|     Git     | `.git` directory |
|     SVN     | `.svn` directory |
|  Mercurial  |  `.hg` directory |
|   Perforce  | `.p4config` file |
| Plain files |  No VCS required |

#### Override SCM detection

```shellscript
bitoreview review --scm git
bitoreview review --scm svn
bitoreview review --scm hg
bitoreview review --scm p4
bitoreview review --scm plain
```

#### Review types across SCMs

|  Review type  |      Git     |      SVN     |  Mercurial  |     Perforce    |
| :-----------: | :----------: | :----------: | :---------: | :-------------: |
| `uncommitted` | Working tree | Working copy | Working dir | Pending changes |
|  `committed`  |   Committed  |   Revisions  |  Changesets |    Submitted    |
|     `all`     |     Both     |     Both     |     Both    |       Both      |

## Combine review options for precision

You can mix options to match your workflow:

```shellscript
# Quick security check before commit
bitoreview review --type uncommitted --focus security --mode essential

# High-severity performance issues vs main branch
bitoreview review --base main --focus performance --severity high

# Full review of selected files
bitoreview review src/auth/*.js --mode comprehensive
```

## Configuration

Customize settings to match your project's needs and workflow preferences.

#### Configuration methods

AI Code Reviews in CLI can be configured in three ways, with each method overriding the previous:

1. **Built-in defaults** - Sensible defaults that work for most projects
2. **Configuration file** - Project-specific settings in `.bitoreview.yaml`&#x20;
3. **CLI flags** - Per-command overrides (highest priority)

#### Configuration file

Create a `.bitoreview.yaml` file in your project root to set default options:

```shellscript
# Review scope: all, uncommitted, committed
type: all

# Review mode: essential (HIGH only) or comprehensive (all severities)
mode: comprehensive

# Focus area: security, performance, bugs, best-practices, tests, documentation
focus: best-practices

# Minimum severity: high, medium, low
severity: medium

# Custom instructions for the AI reviewer
customInstructions: |
  - Pay special attention to error handling
  - Check for proper input validation
  - Ensure consistent coding style
```

{% hint style="info" %}
For complete reference of review options, refer to [Available commands](https://docs.bito.ai/ai-code-reviews-in-cli/available-commands).
{% endhint %}

#### Environment variables

| Variable       | Description                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| `BITO_API_KEY` | [Bito API key (aka Bito Access key)](https://docs.bito.ai/help/account-and-settings/access-key) for authentication |

## Getting help

View help directly from the CLI:

```shellscript
# Show help
bitoreview --help
bitoreview review --help
bitoreview config --help

# Show version
bitoreview --version
```

**Still running into issues?**\
👉 Visit the [**Troubleshooting guide**](https://docs.bito.ai/ai-code-reviews-in-cli/troubleshooting) to find solutions for common installation, configuration, and runtime problems, along with tips for resolving frequent errors quickly.
