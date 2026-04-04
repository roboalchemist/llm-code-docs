# Source: https://docs.jit.io/docs/jit-ide-extension-for-visual-studio.md

# Jit IDE Extension

## Overview

The Jit IDE Extension brings real-time security scanning directly into Visual Studio Code, helping you catch and fix vulnerabilities without leaving your editor.

Find us in the [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=JitSecurity.jitsecurity).

### Key Features

**Real-time Vulnerability Detection:** Jit scans your code as you write it, surfacing issues inline so you can fix them before they reach review.

**Prevent Secrets from Being Pushed:** Pre-commit hooks catch accidental secret exposure before it ever leaves your machine.

**Local & Private:** All scans run locally inside Docker containers. Your code never leaves your machine.

![VSCode extension](https://user-images.githubusercontent.com/6392804/202451407-4cf1baf4-7386-44bf-8bda-56455754e138.gif)

## Prerequisites

* **Docker** must be installed and running. The extension uses Docker containers to run its security tools in the background. If Docker isn't detected, the extension will prompt you to install it.

## Features

### Inline Issue Detection

Jit highlights vulnerabilities directly in the editor with quick-fix suggestions, so you can resolve issues without breaking your flow.

![Quick Fix highlights issues in the editor](https://user-images.githubusercontent.com/6392804/200568071-21a029ad-4c18-4d93-ac86-102ce0522ad1.png)

### Manage New and Existing Issues

View, triage, and track all findings from the extension's side panel.

![Manage New and Existing Issues](https://user-images.githubusercontent.com/6392804/200842469-37787d1c-a27d-4719-b019-e1d58759a48d.png)

### Pre-Commit Hook

Jit can block insecure code at commit time using the [pre-commit](https://pre-commit.com/) framework.

#### Enable

Open the Command Palette and run **"Jit: Install Pre Commit Hook"**, or click **Activate** in the pre-commit section of the extension's side panel. This adds the Jit hook to your `.pre-commit-config.yaml`. If the hook detects issues, it will block the commit and show diagnostic details to help you fix them.

#### Configure

1. Open Settings and search for `jitsecurity.pre-commit`
2. Choose which issue types the hook checks for and adjust other preferences as needed

## Using the Extension with Cursor

The Jit extension can be used with [Cursor](https://cursor.sh/), the AI-powered editor built on VSCode. Since Cursor uses its own application bundle, you need to redirect the `vscode://` URL scheme to Cursor on macOS so that extension links open correctly.

> ⚠️ **Warning:**
>
> This reassigns the `vscode://` URL scheme system-wide - links will open in Cursor instead of VSCode. If you actively use both editors, be aware of this trade-off.

> **macOS only.**

**Step 1:** Check whether a handler is already registered:

```bash
defaults read com.apple.LaunchServices/com.apple.launchservices.secure LSHandlers | grep -i vscode
```

If the output is empty, you're safe to continue. If you see a result, a handler is already registered - the steps below will add a new entry rather than replace it.

**Step 2:** Get Cursor's bundle identifier:

```bash
mdls -name kMDItemCFBundleIdentifier /Applications/Cursor.app
```

Expected output: `kMDItemCFBundleIdentifier = "com.todesktop.230313mzl4w4u92"`

**Step 3:** Register Cursor as the `vscode://` handler using the bundle ID from Step 2:

```bash
defaults write com.apple.LaunchServices/com.apple.launchservices.secure LSHandlers -array-add \
  '{LSHandlerURLScheme = vscode; LSHandlerRoleAll = com.todesktop.230313mzl4w4u92;}'
```

**Step 4:** Apply the change:

```bash
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -r -domain local -domain system -domain user
```

> **Note:** If the change doesn't take effect immediately, a full logout or system restart is required.

## Coverage

| Language/File Type         | Objective                       |
| -------------------------- | ------------------------------- |
| Python                     | Code scanning, Dependency check |
| JavaScript & TypeScript    | Code scanning, Dependency check |
| GoLang                     | Code scanning, Dependency check |
| Java                       | Code scanning                   |
| Kotlin                     | Code scanning                   |
| C#                         | Code scanning                   |
| Swift                      | Code scanning                   |
| Rust                       | Code scanning                   |
| PHP                        | Dependency check                |
| Text Files                 | Secret detection                |
| Terraform / CloudFormation | Infrastructure-as-code scanning |
| Kubernetes                 | Infrastructure-as-code scanning |
| Dockerfile                 | Infrastructure-as-code scanning |

## FAQ

* **Does the extension send my code anywhere?**

  No. All scans run locally inside Docker containers. Your code never leaves your machine.

* **What are the system requirements?**

  Docker must be installed and running. The extension will prompt you if it's not detected.

* **Can I use Jit with Cursor?**

  Yes - see [Using the Extension with Cursor](#using-the-extension-with-cursor) above.

* **What happens when the pre-commit hook finds an issue?**

  The commit is blocked and diagnostic details are shown so you can fix the problem before retrying.