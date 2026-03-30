# Source: https://docs.xano.com/xano-cli/DOC_ACCURACY_REPORT.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Xano CLI Documentation Accuracy Report

**Date:** 2026-02-12
**CLI Version:** @xano/cli/0.0.25
**Environment:** app.dev.xano.com (darwin-arm64, node v24.1.0)

***

## Summary

All 5 doc pages were tested end-to-end: `get-started.mdx`, `guide-from-existing.mdx`, `guide-from-scratch.mdx`, `push-pull.mdx`, and `workspaces-and-branches.mdx`. Every documented command was executed against the dev environment. Below are the issues found, grouped by severity.

***

## CRITICAL Issues

### 1. Pulled directory structure does not match docs (all pages)

**Affected files:** `push-pull.mdx`, `guide-from-existing.mdx`, `guide-from-scratch.mdx`

All three pages show this directory structure after a pull:

```
my-workspace/
├── table/
├── function/
├── api/
├── task/
└── ...
```

**Actual structure** (pulled from a populated workspace):

```
my-workspace/
├── addon/
├── api_group/
├── query/
├── table/
├── task/
└── workspace/
```

Specific problems:

* **`api/` does not exist** — API endpoints are stored in **`query/`**, not `api/`. Every reference to the `api/` directory is wrong.
* **`function/` does not exist** — No `function/` directory was produced. The docs reference it as a top-level directory in the pull output, but it was never created. (Untested whether standalone functions produce a `function/` directory or use a different name.)
* **`addon/` directory is undocumented** — Addons are pulled into their own directory.
* **`api_group/` directory is undocumented** — API group definitions appear here.
* **`workspace/` directory is undocumented** — Contains a workspace-level `.xs` file with metadata.

### 2. `-b` flag documented as `BRANCH_ID` but actually accepts branch labels

**Affected files:** `workspaces-and-branches.mdx`, `get-started.mdx`

`workspaces-and-branches.mdx` (line 169):

```bash  theme={null}
xano profile edit -b BRANCH_ID
```

`get-started.mdx` (line 170, profile create table):

```
-b  Branch ID
```

But `guide-from-existing.mdx` (line 141) correctly uses:

```bash  theme={null}
xano profile edit -b dev
```

**Actual behavior:** `-b` accepts a branch **label** (e.g., `dev`, `v1`), not a numeric ID. The profile stores the label, not an ID. The docs in `workspaces-and-branches.mdx` and `get-started.mdx` are misleading. `guide-from-existing.mdx` gets it right.

***

## MODERATE Issues

### 3. `xano auth` step order lists Branch and Project as separate numbered steps

**Affected file:** `get-started.mdx` (lines 31-37)

The docs list the auth flow as 5 discrete steps:

1. Instance
2. Workspace (optional)
3. Branch (optional)
4. Project (optional)
5. Profile name

**Actual behavior:** When workspace is skipped, steps 3 and 4 are silently skipped entirely — the user jumps directly from workspace to profile name. This isn't necessarily wrong, but listing them as 5 numbered steps implies the user will always see all 5 prompts. Clarifying that steps 3-4 only appear when a workspace is selected would be more accurate.

### 4. Profile wizard step order differs from documented order

**Affected file:** `get-started.mdx` (lines 74-125)

The docs present the wizard steps as:

1. Enter access token
2. Select instance
3. Name your profile
4. Select workspace
5. Select branch
6. Select project

**Actual behavior:** The same order was observed, but:

* Workspace prompt says **"Select a workspace (or skip to use default)"** — the docs show `"Select a workspace:"` with `(skip)` as the last list item. The actual skip mechanism is different: "(Skip workspace)" appears as the **first** option, not the last.
* After skipping workspace, the CLI outputs "Fetching available run projects..." but no project selection prompt appeared (possibly because no run projects exist, or they are auto-selected). The docs call this step "Select a project" but the actual concept seems to be "run projects", not generic projects.

### 5. `workspace push` outputs `null` before the success message

**Affected file:** `push-pull.mdx`

Running `xano workspace push ./dir` produces:

```
null
Pushed 1 documents from /tmp/xano-cli-test
```

The `null` on the first line appears to be a stray API response being logged. Not a documentation issue per se, but if users follow the docs and see `null`, they may think something went wrong.

### 6. `workspace get` error when no workspace in profile is not documented

**Affected file:** `workspaces-and-branches.mdx` (lines 27-29)

The docs say:

```bash  theme={null}
xano workspace get
```

> "This returns details for the workspace in your current profile."

But if no workspace is set in the profile, it throws:

```
Error: No workspace ID provided. Either pass a workspace ID as an argument
 or set one in your profile.
```

The docs don't mention this error case or that a workspace must be set in the profile first.

***

## MINOR Issues

### 7. Token mask format in `profile list -d` is not described

**Affected file:** `get-started.mdx` (line 157)

The docs say `-d` shows "masked tokens" but don't describe the format. Actual format: `eyJ...QJA` (first 3 chars + `...` + last 3 chars).

### 8. Deleting live branch returns a raw 500 error

**Affected file:** `workspaces-and-branches.mdx` (lines 157-159)

The docs correctly state "the currently live branch cannot be deleted" but the actual error is a raw server error:

```
Error: Failed to delete branch: API request failed with status 500: Internal Server Error
{"code":"ERROR_FATAL","message":"Cannot delete live branch"}
```

Compared to deleting `v1` which gives a clean client-side error:

```
Error: Cannot delete the "v1" branch. This is the default branch and cannot be removed.
```

This is more of a CLI bug than a doc issue, but worth noting since the docs imply both cases are handled equivalently.

### 9. `--require-token` flag for workspace edit produces no visible confirmation

**Affected file:** `workspaces-and-branches.mdx` (line 57)

Running `xano workspace edit 23 --require-token` succeeds but the output doesn't confirm the token requirement was enabled (no "Require Token: enabled" line). Only "Swagger: disabled" is shown in the edit confirmation. Not necessarily a doc error, but could confuse users trying to verify the setting took effect.

### 10. Docs link to `https://app.xano.com` dashboard — no mention of other environments

**Affected files:** `guide-from-existing.mdx` (line 114), `guide-from-scratch.mdx` (line 101)

Both guides tell users to "Check the Xano dashboard" and link to `https://app.xano.com`. Users on self-hosted or dev environments would need to use their own URL. Minor, but could confuse dev/self-hosted users following the guides.

***

## What Worked Correctly

| Feature                                                        | Status                  |
| -------------------------------------------------------------- | ----------------------- |
| `npm install -g @xano/cli`                                     | OK                      |
| `xano --version`                                               | OK                      |
| `xano auth -o <url>` (browser flow)                            | OK                      |
| `xano profile wizard -o <url>` (token flow)                    | OK                      |
| `xano profile list` / `list -d`                                | OK                      |
| `xano profile create` (manual)                                 | OK                      |
| `xano profile edit` (set/remove fields)                        | OK                      |
| `xano profile set-default`                                     | OK                      |
| `xano profile delete` / `delete -f`                            | OK                      |
| `xano profile me` / `me -o json`                               | OK                      |
| `-p` profile override flag                                     | OK                      |
| `XANO_PROFILE` env var override                                | OK                      |
| `xano workspace list` / `list -o json`                         | OK                      |
| `xano workspace get <id>`                                      | OK                      |
| `xano workspace create -n` / `-d`                              | OK                      |
| `xano workspace edit` (name, desc, swagger, no-swagger)        | OK                      |
| `xano workspace delete` / `delete -f`                          | OK                      |
| `xano branch list` / `list <workspace_id>`                     | OK                      |
| `xano branch get <label>`                                      | OK                      |
| `xano branch create -l` / `-s` / `-d` / `-c`                   | OK                      |
| `xano branch edit` (label, desc, color)                        | OK                      |
| `xano branch set-live` / `set-live -f`                         | OK                      |
| `xano branch delete` / `delete -f`                             | OK                      |
| v1 branch delete protection                                    | OK                      |
| Live branch delete protection                                  | OK (but error is ugly)  |
| `xano workspace pull <dir>`                                    | OK                      |
| `xano workspace pull --env`                                    | OK                      |
| `xano workspace pull --records`                                | OK                      |
| `xano workspace pull --env --records`                          | OK                      |
| `xano workspace push <dir>`                                    | OK (but outputs `null`) |
| `-w` workspace override on commands                            | OK                      |
| API filenames include HTTP method (e.g., `auth_login_POST.xs`) | OK                      |
| Credentials saved to `~/.xano/credentials.yaml`                | OK                      |


Built with [Mintlify](https://mintlify.com).