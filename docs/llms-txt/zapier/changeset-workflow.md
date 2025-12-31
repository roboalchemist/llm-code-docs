# Source: https://docs.zapier.com/platform/manage/changeset-workflow.md

# Integration CI Pipelines using Changesets and Snapshot Versions

> Use changesets with snapshot versions to set up an automated pipeline for integration version updates.

<Note>
  Changesets are a third-party npm package and therefore only available to Platform CLI integrations.
</Note>

This guide suggests some ways to automate version management and deployment for Zapier integrations using CI pipelines and changesets. Instead of manually updating version numbers and pushing snapshot versions, you can use automated workflows to handle these tasks consistently and reliably.

## Benefits of Automation

Automating your versioning and deployment workflow provides several advantages:

* **Consistency**: Version bumps follow semantic versioning rules automatically
* **Speed**: Deploy snapshot versions for testing without manual intervention
* **LLM Integration**: Changesets are easier for AI tools to work with, compared to manual version number bumps
* **Reduced Errors**: Eliminate mistakes from manual version number updates
* **Team Collaboration**: Multiple developers can work in parallel without worrying about conflicting version bumps

## What are Changesets?

[Changesets](https://github.com/changesets/changesets) is a tool for managing versioning and changelogs in monorepos and single-package projects. Instead of manually editing `package.json` and `CHANGELOG.md`, developers create small markdown files that describe their changes and specify the version bump type (patch, minor, or major).

When you're ready to release, changesets processes these files to:

* Bump version numbers in `package.json`
* Generate changelog entries
* Remove the processed changeset files

This workflow separates "what changed" from "when to release," making it easier to batch changes and coordinate releases.

## The Complete Workflow

This guide covers four automated jobs we recommend adding, and how they can work together.

<Note>
  We recognize all codebases and CI flows are different. These are the jobs we've found most useful in our integration development, but feel free to pick and choose from these jobs per your workflow needs.
</Note>

1. **Snapshot Deployment**: Deploys labeled snapshot versions to Zapier for testing
2. **Integration Validation**: Validates your integration code, configuration, and optional changelog format as you go
3. **Changeset Validation**: Verifies changeset files are properly formatted and version numbers haven't been manually changed
4. **Changeset Processing**: Processes changesets to update versions and changelogs

## Common Integration Patterns

### Pattern 1: Continuous Snapshot Deployment

Deploy snapshot versions on every commit to a pull request for easy testing:

* Snapshot deployment runs on every PR commit
* Uses branch name as the snapshot label
* Enables immediate testing of changes without waiting for version releases

### Pattern 2: Pull Request Validation

Run validation jobs on pull requests to catch issues early:

* Integration validation runs on any PR to verify code and configuration
* Changeset validation runs only when changeset files are added or modified

### Pattern 3: Pre-Publication Processing

Process changesets before publishing:

* Changeset processing runs before publishing your integration version (when changeset files exist)
* Updates version numbers and changelogs in preparation for release

## Job 1: Snapshot Deployment

### Purpose

Deploys labeled snapshot versions to Zapier using the `zapier push --snapshot` command. This enables testing specific branches or features without creating official version releases. Running this on every PR commit allows for continuous testing of changes.

### What It Does

```yaml  theme={null}
- name: Deploy snapshot version
  script:
    - Extract snapshot label from branch name (max 12 characters)
    - Install dependencies
    - Run `zapier push --snapshot LABEL`
```

The `zapier push --snapshot LABEL` command:

* Creates a version labeled `0.0.0-LABEL`
* Deploys this version to Zapier
* Enables testing without affecting production versions

Please reference [documentation for the `zapier push --snapshot` flag here.](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#push)

### When to Run

* On every commit to a pull request for continuous testing
* On feature branches for testing
* Manually triggered for specific branches
* Based on branch name patterns or labels

Consider allowing this job to fail without blocking the pipeline, as snapshot deployments are often optional.

***

## Job 2: Integration Validation

### Purpose

Validates your integration code and configuration using the `zapier validate` command. This catches common issues with authentication, triggers, actions, and other integration components before deployment. Optionally, you can also validate that your `CHANGELOG.md` format is compatible with changesets.

### What It Does

```yaml  theme={null}
- name: Validate integration
  script:
    - Install dependencies
    - Run `zapier validate`
    - Optionally check CHANGELOG.md format for changesets compatibility
```

Please reference [documentation on the `zapier validate` command here](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#validate).

### When to Run

* On every pull request
* As part of your standard test suite
* Before processing any changesets
* Before publishing your integration version

### Additional Considerations

If you're using changesets, you may also want to validate that your `CHANGELOG.md` format is compatible. Changesets expects the file to start with an H1 header (e.g., `# App Name`) that is not a version number.

```yaml  theme={null}
- name: Validate CHANGELOG format (optional)
  script:
    - Check that CHANGELOG.md starts with an H1 header
    - Verify the H1 header is not a version number (e.g., not "# 1.2.3")
```

***

## Job 3: Changeset Validation

### Purpose

Validates that changesets are properly formatted and ensures developers haven't manually modified version numbers in `package.json`. This prevents double version bumps (one manual, one from changesets).

### What It Does

```yaml  theme={null}
- name: Validate changesets
  script:
    - Compare current package.json version with previous commit
    - Fail if version number has changed manually
    - Run `npx changeset status` to validate changeset format
    - Confirm changeset references the correct app/package
```

The `npx changeset status` command:

* Lists all pending changesets
* Shows which packages will be affected
* Validates changeset file format
* Does not fail if no changesets exist

### When to Run

* On pull requests that add or modify changeset files
* Before publishing your integration version
* Use CI rules to only trigger when `.changeset/*.md` files change

### Additional Considerations

* This job requires access to git history to compare versions
* Ensure the CI checkout isn't in a detached HEAD state

***

## Job 4: Changeset Processing

### Purpose

Processes all pending changesets to update version numbers and changelogs before publishing your integration version. This prepares your integration for release by consolidating all pending changes.

### What It Does

```yaml  theme={null}
- name: Process changesets
  script:
    - Run `npx changeset version`
    - Review updated files (package.json, CHANGELOG.md)
```

The `npx changeset version` command:

* Reads all pending changeset files
* Bumps version numbers in `package.json` based on changeset types
* Updates `CHANGELOG.md` with new entries
* Deletes processed changeset files

### When to Run

* Before publishing your integration version (when changesets exist)
* Manually triggered for release preparation
* As part of your release workflow
* Use CI rules to only trigger when `.changeset/*.md` files exist

### Additional Considerations

* Run this job when you're ready to prepare a new version for publication
* Review the updated version number and changelog entries before publishing
* You can run this locally or as part of a CI workflow
* After processing, use `zapier push` to publish the new version to Zapier

***

## Setting Up Changesets

To use these workflows, follow the instructions in the [Changesets Github repo](https://github.com/changesets/changesets/blob/main/docs/intro-to-using-changesets.md) to set up Changesets in your codebase.

## Creating a Changeset

Developers create changesets using:

```bash  theme={null}
npx changeset add
```

This interactive CLI prompts for:

* Which packages are changing
* The version bump type (patch, minor, major)
* A description of the changes

The tool creates a markdown file in `.changeset/` with this information.

## Example: Complete Workflow in Action

1. Developer creates a feature branch and makes changes
2. Developer pushes the branch and opens a pull request
3. CI runs **snapshot deployment** on every commit, pushing version `0.0.0-LABEL` to Zapier
4. Team can immediately test the snapshot version as development continues
5. Developer runs `npx changeset add` and creates a changeset file describing the changes
6. CI runs **integration validation** and **changeset validation** on the PR
7. After PR approval, changes are merged
8. When ready to publish a new version, team runs **changeset processing**, which:
   * Updates version in `package.json`
   * Adds entry to `CHANGELOG.md`
   * Deletes the changeset file
9. Team reviews the updated version and changelog, then uses `zapier push` to publish the version

***

## Additional Resources

* [Changesets Documentation](https://github.com/changesets/changesets)
* [Changesets CLI Reference](https://github.com/changesets/changesets/blob/main/packages/cli/README.md)
* [Zapier CLI Documentation](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md)
* [Zapier Labeled Versions](https://docs.zapier.com/platform/manage/labeled-versions)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.zapier.com/llms.txt