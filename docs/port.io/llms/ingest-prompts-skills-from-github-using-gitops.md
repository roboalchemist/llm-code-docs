# Source: https://docs.port.io/guides/all/ingest-prompts-skills-from-github-using-gitops.md

# Ingest prompts and skills from GitHub using GitOps

Teams that manage AI prompts and skills as code need a reliable way to sync those assets into Port. This guide shows you how to structure prompt and skill files in your GitHub repositories and map them to Port blueprints using the GitHub app integration. This gives you a GitOps workflow where GitHub is the source of truth and Port stays in sync automatically.

![Skill entity view synced from GitHub](/img/guides/ingest-github-skill-example.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Keep AI prompts and skills version-controlled with clear audit trails.
* Avoid manual entity creation and drift across systems.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* [Port's GitHub integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/) is installed in your account.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

Let's create two blueprints to manage AI prompts and skills.

### Create the prompt blueprint[â](#create-the-prompt-blueprint "Direct link to Create the prompt blueprint")

Follow the steps in the [Set up the data model](https://docs.port.io/ai-interfaces/port-mcp-server/prompts#set-up-the-data-model) section of the prompts documentation to create the prompt blueprint.

### Create the skill blueprint[â](#create-the-skill-blueprint "Direct link to Create the skill blueprint")

Follow the steps in the [Step 1: Create the skill blueprint](https://docs.port.io/ai-interfaces/port-mcp-server/skills#step-1-create-the-skill-blueprint) section of the skills documentation to create the skill blueprint.

## Recommended file structure[â](#recommended-file-structure "Direct link to Recommended file structure")

You can map GitHub files and folders to Port entities. The structure below keeps prompts and skills consistent and predictable.

### Prompt files[â](#prompt-files "Direct link to Prompt files")

Store prompts as YAML files under `.github/prompts` using the `.prompt.yaml` suffix. This is consistent with [GitHub's prompt storage standard](https://docs.github.com/en/github-models/use-github-models/storing-prompts-in-github-repositories).

Example file: `.github/prompts/code-review.prompt.yaml`.

**Example prompt file (click to expand)**

```
name: code-review
description: Review code changes for correctness, security, performance, and test coverage following repo conventions.
arguments:
  - name: change_scope
    description: Summary of the changes or files to review.
    required: false
  - name: focus_areas
    description: Specific concerns to prioritize (e.g., security, performance).
    required: false
message: |-
  # Code review

  Review code changes for this repository.

  Inputs:
  - change_scope: {{change_scope}}
  - focus_areas: {{focus_areas}}

  ## Instructions

  Focus on:
  - correctness and edge cases.
  - security risks and input validation.
  - performance regressions.
  - missing tests or insufficient coverage.
  - adherence to repo conventions in `AGENTS.md`.

  Output format:
  1. Findings (ordered by severity).
  2. Questions and assumptions.
  3. Suggested fixes.

  ## Examples
  - Review changes in {{change_scope}} with focus on {{focus_areas}}.
  - If {{change_scope}} is empty, review the full diff and infer key risks.

  ## Guidelines
  - Be specific and cite affected areas.
  - Prioritize actionable feedback.
```

### Skill folders[â](#skill-folders "Direct link to Skill folders")

Store each [Anthropics skill](https://github.com/anthropics/skills) in its own folder under `skills/`. Each folder should include a `SKILL.md` file with YAML frontmatter and instructions. You can add supporting files under `references/` and `assets/` as needed.

Example file: `skills/my-skill/SKILL.md`.

**Example skill file (click to expand)**

```
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My skill name

Add your instructions here that the AI should follow when this skill is active.

## Examples
- Example usage 1.
- Example usage 2.

## Guidelines
- Guideline 1.
- Guideline 2.
```

File content validation

Make sure your prompt and skill files contain only the fields you intend to expose in Port, and avoid including secrets or credentials in any file content that will be ingested.

## Update integration mapping[â](#update-integration-mapping "Direct link to Update integration mapping")

Now you will configure the GitHub integration to ingest prompts and skills from your repositories.

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Find your GitHub integration and click on it.

3. Go to the `Mapping` tab.

4. Update the mapping configuration:

   **GitHub integration mapping configuration (click to expand)**

   ```
   deleteDependentEntities: false
   createMissingRelatedEntities: true
   enableMergeEntity: true
   resources:
     - kind: repository
       selector:
         query: 'true'
         teams: true
       port:
         entity:
           mappings:
             identifier: .full_name
             title: .name
             blueprint: '"githubRepo"'
             properties:
               readme: file://README.md
               url: .html_url
               defaultBranch: .default_branch
             relations:
               githubTeams: '[.teams[].id | tostring]'

     - kind: folder
       selector:
         query: 'true'
         folders:
           - path: '**/skills/*'
       port:
         entity:
           mappings:
             identifier: .repo.name + "-" + .folder.name
             title: .repo.name + "-" + .folder.name
             blueprint: '"skill"'
             properties:
               instructions: file://SKILL.md
               description: .folder.name

     - kind: file
       selector:
         query: 'true'
         files:
           - path: .github/prompts/*.prompt.yaml
             skipParsing: false
       port:
         entity:
           mappings:
             identifier: .repo.name + "/" + .file.name
             title: .file.name | split(".") | .[0]
             blueprint: '"prompt"'
             properties:
               description: .file.content.description
               arguments: .file.content.arguments
               template: .file.content.message
   ```

5. Click **Save** to update the integration configuration.

## Test the configuration[â](#test-the-configuration "Direct link to Test the configuration")

Now you can validate the full workflow and confirm that changes in GitHub appear in the Port catalog.

1. Update a `.prompt.yaml` or `SKILL.md` file in your repository and merge the change.
2. Go to your [software catalog](https://app.getport.io/organization/catalog) page.
3. Find the corresponding `Prompt` or `Skill` entity and confirm the content is updated.

## Related guides[â](#related-guides "Direct link to Related guides")

* [Centralize AI coding rules with Port](https://docs.port.io/guides/all/centralize-ai-coding-rules-with-port/).
* [Manage AI instructions with Port](https://docs.port.io/guides/all/manage-ai-instructions/).
