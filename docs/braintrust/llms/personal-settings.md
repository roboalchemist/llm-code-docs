# Source: https://braintrust.dev/docs/admin/personal-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Personal settings

> Configure your individual user preferences

Personal settings control your individual user experience across all projects in your organization. Access personal settings by going to any project and selecting <Icon icon="settings-2" /> **Settings** > **Personal** > <Icon icon="square-user-round" /> **Profile**.

## Profile

Update your name and avatar to help team members identify you in comments, reviews, and activity logs.

## Appearance

Choose between light, dark, or system appearance modes.

## Default data display format

Set your preferred format for viewing data in span fields across all traces:

* **Pretty** - Parses objects deeply and renders values as Markdown (optimized for readability)
* **JSON** - JSON highlighting and folding
* **YAML** - YAML highlighting and folding
* **Tree** - Hierarchical tree view for nested data structures

When viewing individual span fields, additional format-specific views become available for certain data types, including LLM (formatted AI messages), LLM Raw (unformatted AI messages), and HTML (rendered HTML content).

You can override this default for individual span fields when viewing traces. These overrides are remembered per field type.

To clear all overrides and restore your default preferences across all fields, use the <Icon icon="refresh-ccw" /> reset button.

## Next steps

* [View your logs](/observe/view-logs) to see how data views work in practice
* [Manage organizations](/admin/organizations) to configure organization-wide settings
