# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-permission-target-template.md

# Generate a permission target template with jf rt permission-target-template

Create a JSON template for permission target creation or replacement through an interactive process.

## Synopsis

```
jf rt permission-target-template <template-path>
```

**Aliases:** `rt ptt`

## Arguments

| Argument          | Required | Description                                  |
| ----------------- | -------- | -------------------------------------------- |
| `<template-path>` | Yes      | Local file system path for the template file |

## Options

This command accepts no flags. It uses the server configured as default by `jf config`.
To target a non-default server, run `jf config use <server-id>` before executing this command.

<Callout icon="📘" theme="info">
  Note

  Connection flags such as `--server-id`, `--url`, and `--access-token` are accepted by
  [`jf rt ptc`](/docs/jf-rt-permission-target-create) and [`jf rt ptu`](/docs/jf-rt-permission-target-update)
  when applying a template — not by `jf rt ptt`.
</Callout>

## Examples

### Create a Permission Target Template

**To generate a permission target template interactively:**

1. Run:

```bash
jf rt permission-target-template <template-path>
```

**Where:**

* `<template-path>` — path where the new JSON template file should be written (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt permission-target-template ./my-permission-target.json
```

The CLI guides you through an interactive wizard. On success, you will see:

```
HH:MM:SS [Info] Permission target configuration template successfully created at ./my-permission-target.json.
```

The output file is standard JSON and is suitable for use with `permission-target-create` or `permission-target-update`.

## When to Use

Use `jf rt ptt` to create a JSON template interactively before creating or updating permission targets. The template approach is recommended because:

* **Complex structure**: Permission targets involve repositories, users, groups, and action permissions — the template guides you through all the fields
* **Reusability**: Save the template and reuse it across environments. Use `${variableName}` placeholders in the template, then inject real values with `--vars` when running `jf rt ptc` or `jf rt ptu`
* **Version control**: Commit templates to source control for auditable access control changes

**Typical workflow:**

**To create a template and apply it, then update with variables:**

1. Create the template interactively (writes the file to the path you provide):

```bash
jf rt ptt ./team-access.json
```

2. (Optional) Edit the JSON to add `${variable}` tokens for parameterization (for example change `"repositories":"my-repo"` to `"repositories":"${repoName}"`).

3. Create the permission target from the template:

```bash
jf rt ptc ./team-access.json
```

4. Later, update it and inject variables with `--vars` (semicolon-separated `key=value` pairs):

```bash
jf rt ptu ./team-access.json --vars "groupName=new-team;repoName=my-libs-repo"
```

<Callout icon="📘" theme="info">
  Coming from the UI?

  In the Artifactory UI, you manage permission targets under **Administration > Identity and Access > Permissions**. The template corresponds to the JSON payload you would see if you clicked "Export" on a permission target. The CLI's interactive prompts walk you through the same fields.
</Callout>

<br />

## Before You Begin

Have the following information ready before starting the wizard:

* **Permission target name** — a unique identifier for this permission target
* **Repository names** — the repos to apply permissions to, or one of the special values `ANY`, `ANY REMOTE`, or `ANY LOCAL`
* **Usernames and/or group names** — principals to grant permissions to (you can press Enter with no value to skip users or groups)

<br />

## Wizard Walkthrough

The wizard runs a multi-step questionnaire. Here is the full prompt sequence:

| Step | Prompt                                                                                                                | Input type             | Notes                                                                                                 |
| ---- | --------------------------------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------- |
| 1    | `Insert the permission target name >`                                                                                 | Free text              | Required. Name of the permission target.                                                              |
| —    | `You can type ":x" at any time to save and exit.`                                                                     | *(hint)*               | See [Saving and exiting](#important-notes).                                                           |
| 2    | `Select the permission target section to configure (press Tab for options):`                                          | Tab-select             | Options: **`repo`**, **`build`**, **`releaseBundle`**, **`:x`** (save and exit). Press Tab to reveal. |
| 3    | `Insert the section's repositories value.` / `The value should be a comma separated list >`                           | Comma-separated        | *(repo section only)* Accepts repo names, `ANY`, `ANY REMOTE`, or `ANY LOCAL`.                        |
| 4    | `Insert a value for include-patterns:` / `The value should be a comma separated list (press enter for default) [**]:` | Comma-separated        | *(repo section only)* Default is `**` (all files). Press Enter to accept.                             |
| 5    | `Insert value for exclude-patterns:` / `The value should be a comma separated list (press enter for default) []:`     | Comma-separated        | *(repo section only)* Default is empty (no exclusions). Press Enter to accept.                        |
| 6    | `Configure actions for users? (press Tab for options): [yes]:`                                                        | Tab-select             | Options: `yes`, `no`. Default is `yes`.                                                               |
| 7    | `Insert user name (press enter to finish) >`                                                                          | Free text (repeatable) | Enter one username per line. Press Enter with no value to finish the user list.                       |
| 8    | `Configure actions for groups? [yes]:`                                                                                | Tab-select             | Options: `yes`, `no`. Default is `yes`.                                                               |
| 9    | `Insert group name (press enter to finish) >`                                                                         | Free text (repeatable) | Enter one group name per line. Press Enter with no value to finish.                                   |
| 10   | Returns to step 2                                                                                                     | —                      | Add another section (`build`, `releaseBundle`) or type `:x` to save and exit.                         |

<Callout icon="👍" theme="okay">
  Tip

  You can configure multiple sections in one session. After completing a section, the wizard returns to the section selector. Type `:x` when you are done adding sections.
</Callout>

<br />

## Important Notes

* **Requires a real terminal (TTY).** This command uses an interactive prompt library that requires a live terminal session. Running it without a TTY — for example, from a script, CI pipeline, or with piped stdin — causes the command to exit immediately with an error. If you need to create a template in a non-interactive environment, write the JSON file manually using the format documented in [jf rt permission-target-create](/docs/jf-rt-permission-target-create) or [jf rt permission-target-update](/docs/jf-rt-permission-target-update).
* **Saving and exiting the wizard:** At any section selection prompt, type `:x` and press Enter to save the template and exit. This is the only way to complete and save the wizard session.
* **Dropdown prompts require Tab:** Prompts marked `(press Tab for options)` require you to press `Tab` to reveal the list of valid choices. Pressing Enter without a valid selection prints `Invalid answer. Please select value from the suggestions list.` You can either press `Tab` and then Enter, or type the option name exactly (for example, `repo`) and press Enter.
* The command is interactive — it prompts for the permission target name, section type, repository assignments, user/group principals, and action permissions.
* The wizard writes **literal values** to the template JSON exactly as you typed them. To enable variable substitution, manually edit the JSON after generation and replace any value with a `${variableName}` token. Then pass real values at apply time using `--vars` with `jf rt ptc` or `jf rt ptu`. For example:
  ```json
  { "name": "team-target", "repo": { "repositories": "${repoName}" } }
  ```
  ```bash
  jf rt ptc ./team-access.json --vars "repoName=my-libs-repo"
  ```
  The `--vars` flag is not accepted by `jf rt ptt` itself.
* Template files are standard JSON and can be edited manually after generation.

<br />