# Source: https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/ignore-issues/consistent-ignores-for-snyk-code/snyk-ide.md

# Consistent Ignores for Snyk Code IDE

When you run tests in any of the [four supported Snyk IDE plugins](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions), the plugins will take into account your ignores.

## Minimum version required

Snyk Code Consistent Ignores works best with the latest IDE plugin versions.

| IDE           | Minimum version required |
| ------------- | ------------------------ |
| VS Code       | 2.22.0                   |
| IntelliJ      | 2.13.1                   |
| Visual Studio | 2.2.1                    |
| Eclipse       | v20250516.122216         |

## Setup

To take ignores into account, specify the Organization where the ignores reside. [Group-level policies also cascade down to all Organizations](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/ignore-issues/consistent-ignores-for-snyk-code/..#manage-ignores-at-the-group-level-through-snyk-code-security-policies). See [How to select the Organization to use in IDE plugins (Visual Studio Code example)](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/how-to-select-the-organization-to-use-in-the-cli).

## Snyk IDE default ignore behavior

The IDE display output hides ignored results by default to maintain developer focus.

## View ignores in Snyk IDE

You can apply filters in the plugin settings to show ignored results alongside open results or in isolation. When you set ignored issues to display, the issues and their details appear in the plugin.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-bacd5ebd04ef4e57c42cf7c2066286a37855c100%2Fsnyk-code-ignored-issue-ide.png?alt=media" alt=""><figcaption><p>View ignores in Snyk IDE</p></figcaption></figure>
