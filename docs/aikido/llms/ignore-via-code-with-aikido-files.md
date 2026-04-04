# Source: https://help.aikido.dev/code-scanning/scanning-practices/ignore-via-code-with-aikido-files.md

# Ignore with .aikido Files

The `.aikido` file (YAML-formatted) allows you to ignore certain CVE's and exclude certain paths from being scanned by Aikido. These are read automatically whenever a scan is initiated.

## Default behavior and customization

Aikido already excludes a large number of irrelevant files and directories by default in order to reduce noise as much as possible. This includes files and paths that are commonly non-actionable or not meaningful for security analysis.

The `.aikido` file is **not required for standard usage**. Instead, it is intended for **organization-specific customization**, allowing you to further tailor scanning behavior to your codebase, risk appetite, and internal policies. Use it when you need to ignore highly specific files, paths, or CVEs that are known to be irrelevant or intentionally accepted within your organization.

## Setting up the .aikido file <a href="#setting-up-the-aikido-file" id="setting-up-the-aikido-file"></a>

Create the `.aikido` file **within the root of your repository**.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-02d3975853e1de4cf9b0eaa4d153ca996db6fdc5%2Fignore-via-code-with-aikido-files_9b2a4a59-3404-4012-be7a-dd43a6374104.png?alt=media" alt="Project directory with .aikido config file." width="375"></div>

### Exclude specific paths or files <a href="#exclude-specific-paths" id="exclude-specific-paths"></a>

The `exclude` key and `paths` subkey allow you to hide specific files and directories from being scanned by Aikido code scanning. This will automatically **exclude scans for secrets, SAST issues, lockfiles and code quality.**

{% hint style="info" %}
**Note:** Path matching in `.aikido` is based on **simple string inclusion**.

If a configured value appears anywhere in the full file path, it will be excluded.\
Wildcards and regular expressions are **not supported**.
{% endhint %}

```yaml
exclude:
  paths:
    - src/useless-folder
    - docs/example.js
    - .gen.ts
```

### Ignore CVEs <a href="#ignore-cves" id="ignore-cves"></a>

To ignore CVE's, add them to the `.aikido` yaml file with a reason. The Aikido UI will also show that these specific CVEs are ignored with reference to the `.aikido` file.

```yaml
ignore:
  cves:
    CVE-2020-8203:
      reason: We do not care about this CVE
    CVE-2025-22869:
      reason: We handle this
```

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fd067a83d3161a9cbc5fa6dda3a852c84dbe8729%2Fignore-via-code-with-aikido-files_97662102-7431-4590-b26a-53572f1ae18e.png?alt=media" alt="High severity CVE downgraded via .aikido  config file." width="375"></div>

## Additional options <a href="#excluding-sast-findings-using-comments" id="excluding-sast-findings-using-comments"></a>

It's also possible to ignore [SAST findings using comments within your code.](https://help.aikido.dev/code-scanning/scanning-practices/excluding-sast-findings-using-comments)
