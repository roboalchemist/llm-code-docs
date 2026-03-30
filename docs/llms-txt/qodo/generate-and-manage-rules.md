# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/rule-enforcement/generate-and-manage-rules.md

# Generate and Manage Rules

This page explains how to generate and manage rules in the Qodo portal, including rule lifecycle operations such as editing, disabling, and deletion.

**Admins** can create, edit, enable, approve, and delete rules.\
**Members** can generate rules in the portal; however, these rules appear in the **Suggestions** tab and require admin approval before becoming active. Members can also view active rules, suggested rules, and review rule outcomes during code reviews.

### Anatomy of a rule

A rule consists of the following fields:

<table><thead><tr><th width="148.8515625">Field</th><th width="247.87109375">Description</th><th width="341.9140625">Details</th></tr></thead><tbody><tr><td><strong>Rule name</strong></td><td>Short, descriptive title summarizing the rule’s intent.</td><td>Shown in the Rules table and in code review findings.</td></tr><tr><td><strong>Rule content</strong></td><td>Enforcement description used during reviews.</td><td>Explains what to check and what behavior is expected.</td></tr><tr><td><strong>Examples</strong></td><td>Compliant and non-compliant code examples.</td><td>Displayed to developers when violations occur.</td></tr><tr><td><strong>Category</strong></td><td>Type of issue the rule addresses.</td><td>Security, Correctness, Quality, Reliability, Performance, Testability, Compliance, Accessibility, Observability, Architecture.</td></tr><tr><td><strong>Severity</strong></td><td>Priority level of a violation.</td><td>Error (action required), Warning (recommended), Recommendation (informational).</td></tr><tr><td><strong>Scope</strong></td><td>Where the rule is enforced.</td><td>Can be left empty to apply organization-wide, or limited to specific Git organizations, repositories, and optional path patterns.</td></tr></tbody></table>

**Rule scope**

Scope defines where the rule is enforced.

By default, a rule applies organization-wide. You can narrow the scope to limit enforcement:

* **Organization** — leave the scope empty to apply the rule to all repositories across all Git organizations.
* **Git organization** — applies the rule to selected Git organizations.
* **Repository** — applies only to selected repositories.
* **Path patterns** — applies to specific directories or files within a repository. Path patterns are optional and can only be added after selecting a repository, and are especially useful for monorepos where different projects or services live under the same repository.

### Generate a rule

Use this flow to describe a rule in natural language and let Qodo agent generate a structured draft.

#### Step 1: Start rule generation

1. From **Rules**, click **Generate.**
2. Enter a short description of the rule’s intent.
3. Click **Generate rule.**

Example prompts:

* “Disallow `console.log` in production builds”
* “Avoid SQL string concatenation with user input”

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FWHvRencF4fdgPQfbEEHF%2FGenerate.png?alt=media&#x26;token=905c6f92-1120-4451-9c0d-c7ca99567ac6" alt="" width="560"><figcaption></figcaption></figure>

#### Step 2: Review the generated rule draft

Qodo generates a complete rule draft that can be edited before activation.

#### Step 3: Related rules check

Before activation, Qodo checks for:

* Conflicts
* Duplicates
* Overlapping scope

You can review related rules or revise the draft.

#### Step 4: Accept and activate

1. Click **Accept & activate** to enable enforcement.

The rule is added to the Rules table and enforced automatically according to its defined scope (repositories and optional path patterns).

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2Fh8ir6ylpQ2zfLY13HLNd%2FGenerate%20edit.png?alt=media&#x26;token=01c18ae1-4094-42da-9e2b-9347e39f257a" alt=""><figcaption></figcaption></figure>

### Manage existing rules

Management actions for existing rules are available from the **actions menu (⋮)** in the Rules table.\
These actions are optional and can be performed at any time by admins or team admins.

**Editing a rule** - Editing an existing rule.&#x20;

**Enabling or disabling a rule** - Disabling pauses enforcement while retaining history.

**Deleting a rule** - Deletion is permanent and irreversible.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FQsvpavuuzEUs16txSWmv%2FActions.png?alt=media&#x26;token=59057f4b-b31f-456e-a2ae-de0f0dc12958" alt=""><figcaption></figcaption></figure>

### Best practices for maintenance

* Edit instead of duplicating
* Disable before deleting
* Keep scopes narrow
* Periodically review low-signal rules

### Fetch rules using `get-qodo-rules` skill

Supported AI coding agents can access your Rule System directly using the `get-qodo-rules` skill.

The skill fetches repository specific rules from the Qodo platform API, including organization, repository, and path level rules, and loads them into the agent context. This allows the agent to reference the same rules that are defined in Qodo.

This capability is optional and does not replace Qodo’s rule enforcement. It enables agents to use the rules already configured for the repository. Using the skill requires a Qodo API key and rules configured in the Qodo platform.

For more details go to the [open source installation instructions](https://github.com/qodo-ai/qodo-skills).
