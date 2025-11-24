# Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-review-customization.md

# Customization

> Tailor AI reviews to your team's specific needs and coding standards

## Making AI reviews work for your team

While Graphite Agent will catch bugs out of the box, you can customize its behavior to better match your team's specific needs and coding standards. AI reviews offer two primary customization options: **Exclusions** and **Custom rules**.

<Frame caption="AI reviews customization interface">
  <img src="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=4ecc00cdba3cb276a28cf7f02348d6ba" data-og-width="2336" width="2336" data-og-height="1584" height="1584" data-path="images/ai-reviewer-customizations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=280&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=801b12656fd7f31e18412c9dc5b41525 280w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=560&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=cbd77ac882797e04572734fff53a077e 560w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=840&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=f42ac19ca3a0b722c40cc72dc20162e8 840w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=1100&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=2ea41cddd6dabc78c98826e82e2cf481 1100w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=1650&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=24c4692118a0bee9f6824f717560a0ac 1650w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=2500&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=8c238155ecd08f82f0d274e228c43d40 2500w" />
</Frame>

## Exclusions: Specifying what to ignore

Comment exclusions allow you to specify situations where Graphite Agent should **not** leave comments. This reduces noise and focuses AI reviews on what matters most to your team.

Common exclusion use cases:

* **Ignore generated code**: Prevent extraneous comments on generated code from build artifacts, schemas, and other generated files.
* **Skip specific types of comments**: Turn off categories of feedback that aren't relevant to your team
* **Ignore certain repositories or directories**: Focus AI reviews where they matter most
* **Exclude specific patterns**: Define patterns that shouldn't be flagged (e.g., team-specific style conventions)

### Best practices for writing exclusions

Make the language as targeted as possible by specifying the exact scope where the exclusion should apply. If an exclusion is written too broadly, then Graphite Agent may not leave valid comments.

Bad example:

```
### Bad example: Overly broad exclusion

Don't suggest performance improvements.
```

Why is this bad?

* This is too broad and would miss legitimate performance issues. The rule could be rewritten instead as:

```
Do not suggest performance optimizations for code in the /scripts directory - these are one-time utility scripts.
```

Good example:

```
### Good example: Language-specific syntax exclusion

Do not comment on missing "return" keywords in Kotlin single-expression functions. This is valid Kotlin syntax.
```

To set up exclusions:

1. Go to the [AI reviews settings page](https://app.graphite.com/ai-reviews)
2. Click on Workspace Settings
3. Create and save your exclusions

## Custom rules: Teaching Graphite Agent your standards

Custom rules allow you to define explicit guidelines for Graphite Agent to follow when reviewing your code. This is especially powerful for enforcing team-specific best practices.

With custom rules, you can:

* Define coding standards specific to your codebase
* Implement architectural guidelines for your team
* Enforce security or performance best practices
* Ensure consistent patterns across your repositories

<Frame caption="Custom rule interface">
  <img src="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=486fb3d8b71cb571c13843ee506a2cda" data-og-width="2346" width="2346" data-og-height="1584" height="1584" data-path="images/ai-reviewer-add-custom-rule-with-templates.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=280&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=d075d556af1aaf5f8c9106bc8ac854ca 280w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=560&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=91b9cfdceb5c39b6cf1ced7de0f17158 560w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=840&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=0a06f64d47bb0d71a1d70f55af3149c7 840w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=1100&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=582be71ba4a7bb46ed9e0c7ddaa20f42 1100w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=1650&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=afd8e66e884d0e0cba09f40e1c743cbd 1650w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=2500&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=7e7057c9ce2e38a414455d96d1e1a8bf 2500w" />
</Frame>

There are two ways to configure custom rules: custom prompts and file-based rules. Below is our recommendation for when each option is most appropriate.

### Custom prompts (Recommended)

Custom prompts are rules written directly in the Graphite UI. They're the recommended approach for most teams.

**Why custom prompts work best:**

* **Focused**: Each rule addresses one specific concern
* **Fast to iterate**: Test and refine rules based on their effectiveness
* **Better performance**: No file processing overhead
* **Easy to manage**: All rules across all repos visible in a single interface

**Getting started:**

1. Use built-in templates for common scenarios:

   * Language-specific style guides (JavaScript, Python, Go, etc.)
   * Security best practices
   * Accessibility standards

2. **Start small**: Create focused rules that address specific concerns

   * Example: "JavaScript error handling patterns"
   * Example: "API response formatting standards"

3. **Quick start**: Copy relevant sections from your existing coding guidelines and refine them into focused rules

### File-based rules

File-based rules reference existing documentation in your repository using glob patterns. Use these sparingly when you have living documentation that changes frequently.

**When to use file-based rules:**

* Documentation maintained by other teams that changes regularly
* Shared architectural decision records across repositories
* Style guides that are actively updated

**How they work:**

1. Specify a glob pattern (e.g., `docs/coding-style.md`)
2. Graphite Agent reads the file content from your repository
3. Uses that content as context during code review

**Example patterns:**

```
docs/coding-standards.md    # Specific documentation file
CONTRIBUTING.md             # Contributing guidelines
docs/architecture/*.md      # Architecture documentation
```

**Limitations:**

* Large files are truncated for performance
* Too many files can reduce review quality
* Glob patterns are case-sensitive

### Best practices for writing custom rules

**Structure your rules clearly:**

* **Format**: Rule → Bad example → Good example → Reasoning
* **Focus**: One specific concern per rule
* **Examples**: Provide 2-3 clear, contrasting examples
* **Test**: Try your rule on recent PRs to verify it adds value

**What works best:**

* Language-specific conventions (naming, imports, error handling)
* Security guidelines (authentication, data validation)
* Framework-specific patterns (React hooks, API design)

**What to avoid:**

* Overly broad rules ("write good code")
* Subjective preferences without clear reasoning
* Complex architectural patterns that only sometimes apply

Bad examples:

```
### Bad example 1: Vague database rule

Rule: Don't make breaking changes to database fields. When dropping or adding fields could cause issues, flag them in review.
```

Why is this bad?

* Too vague. The rule needs to specify what types of field drops or additions would be considered breaking.
* Not actionable. The rule should be specific, like: "Never drop a required field directly. Always make it nullable first and stop writing to it so that it is no longer used by the entity."
* No examples provided.

```
### Bad example 2: Unclear CSS class naming rule

Always comment on color values like #FF0000 being used in stylesheets. Don't comment on utility classes like bg-red-500 or text-primary.
```

Why is this bad?

* More context is needed. The rule should specify which files or frameworks this applies to (CSS files, styled-components, etc.).
* This isn't phrased as a rule. The rule should be stated clearly as "Never use hex color values directly, always use design system tokens instead."
* This prompt mixes custom rules and exclusions. The latter sentence is not necessary.

Good examples:

````
### Good example 1: Security rule with clear structure

## Security Rules

### Rule: Never expose detailed error messages

**Rule:**
Never expose detailed error messages that reveal stack traces or internal system details. In production environments, always return generic error messages to protect the system while logging full details internally for debugging.

**Bad example:**
```js
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.stack });
});
```

**Good example:**
```js
app.use((err, req, res, next) => {
  res.status(500).json({ error: "Internal Server Error" });
});
```

**Reasoning:**
Revealing stack traces or internal error details can leak sensitive implementation information, making it easier for attackers to exploit vulnerabilities.
````

````
### Good example 2: Database rule with specific context

## Database Rules

### Rule: Use `text` instead of `varchar(n)` for new PostgreSQL columns

**Rule:**
When adding new string columns to TypeORM entities, always use `text` type instead of `varchar(n)` unless there's a specific business requirement for length constraints.

**Good example:**
```ts
@Column({ type: 'text' })
description: string;
```

**Bad example:**
```ts
@Column({ type: 'varchar', length: 255 })
description: string;
```

**Reasoning:**
PostgreSQL handles `text` and `varchar` identically in terms of performance, but `text` avoids arbitrary length limits that can cause issues as data grows.
````

For additional recommendations, see [Anthropic's suggestions for prompt engineering best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#be-explicit-with-your-instructions).

To set up custom rules:

1. Go to the [AI reviews settings page](https://app.graphite.com/ai-reviews?view=settings)
2. Scroll to the "Custom rules" section and click on "Create custom rule"
3. Choose a template or add a custom prompt for your new rule
4. Save your configuration

## Excluding files from AI review

For large repositories, you may want to exclude certain files from AI review analysis. This is useful for:

* Data files that don't need to be reviewed
* Generated code that is automatically created by tools
* Any files that would make a PR too big for Graphite Agent to analyze

You can exclude files by marking them as generated files in your repository's `.gitattributes` file:

```
# Exclude specific files
docs/data.txt linguist-generated=true

# Exclude file types
*.csv linguist-generated=true
*.pb.go linguist-generated=true

# Exclude entire directories
data/** linguist-generated=true
generated/** linguist-generated=true
```

Files marked as `linguist-generated` will be:

* Automatically collapsed in GitHub pull request views
* Excluded from AI review when determining if a PR is too large
* Skipped during the AI review process

For more information, see GitHub's documentation on [customizing how changed files appear on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/customizing-how-changed-files-appear-on-github).

## PR-level filtering

Advanced PR-level filtering provides granular control over where AI reviews run. You can configure AI reviews to run on specific pull requests based on defined criteria.

With PR-level filtering, you can control AI reviews based on:

* **PR author**: Run reviews only for specific team members or external contributors
* **File paths**: Analyze PRs only when certain files or directories are modified
* **PR labels**: Trigger reviews based on GitHub labels applied to pull requests
* **PR title and description**: Filter based on text content in PR titles or descriptions
* **Parent branch**: Run analysis based on target branch naming conventions

PR-level filtering provides flexibility to:

* **Control usage and costs**: Optimize AI review usage by focusing on the most important PRs
* **Focus analysis on critical PRs**: Ensure reviews target high-impact changes while skipping routine updates
* **Implement organization-specific review policies**: Align AI review behavior with your team's development workflows and governance requirements

Once saved, AI reviews will only run on new and updated pull requests that match the configured settings in enabled repositories. You can configure these settings through the AI reviews settings page, and organization admin permissions are required to modify them.
