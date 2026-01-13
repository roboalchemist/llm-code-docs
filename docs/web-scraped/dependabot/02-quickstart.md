# Dependabot Quickstart Guide

Source: https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide

## Overview

Dependabot comprises three integrated features for dependency management:

- **Dependabot alerts**: Inform you about vulnerabilities in the dependencies that you use in your repository
- **Dependabot security updates**: Automatically generates pull requests addressing known security vulnerabilities
- **Dependabot version updates**: Keeps dependencies current through automated pull requests

## Getting Started

### Prerequisites

To follow along with practical examples, you can fork the demonstration repository at:
https://github.com/dependabot/demo

### Step 1: Access Repository Settings

1. Navigate to your repository's main page
2. Click **Settings** (or access via the dropdown menu if unavailable)

### Step 2: Enable Dependabot Features

1. In the sidebar, locate the "Security" section
2. Click **Advanced Security**
3. Under "Dependabot," click **Enable** for each feature you want:
   - Dependabot alerts
   - Dependabot security updates
   - Dependabot version updates

**Note**: The dependency graph activates automatically when enabling Dependabot if not already enabled.

### Step 3: Configure Version Updates

If you've selected Dependabot version updates:

1. A default `dependabot.yml` file will be created in `/.github/`
2. Edit this file to suit your repository's needs
3. Commit your changes

The file uses YAML format with the following basic structure:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
```

## Viewing and Managing Alerts

### Access Dependabot Alerts

1. Click the **Security** tab on your repository (use the dropdown if unavailable)
2. In the "Vulnerability alerts" sidebar, select **Dependabot**
3. The page displays open alerts by default; switch to **Closed** to see dismissed ones

### Review Alert Details

Click any alert to review:

- Affected package information
- Vulnerability severity
- Available patches
- Associated CVE/GHSA identifiers

## Resolving Vulnerabilities

### Merge a Security Fix

1. Click "Review security update" to examine Dependabot's proposed pull request
2. Review the changes and CI results
3. Merge the PR once confirmed

### Dismiss an Alert

If you choose not to upgrade:

1. Click "Dismiss alert" on the details page
2. Select a dismissal reason
3. Optionally add explanatory comments
4. Confirm dismissal (alerts move to the Closed tab)

## Common Dismissal Reasons

- **Not affected**: The vulnerability doesn't apply to your use case
- **Tolerable risk**: You accept the risk of the vulnerability
- **No bandwidth**: You don't have resources to address it now
- **Inaccurate**: The alert is incorrect or misidentified

## Troubleshooting

If Dependabot cannot generate pull requests or detection seems inaccurate, consult the full documentation for troubleshooting guidance.

## Next Steps

After completing the quickstart:

- Explore additional configuration options for security updates
- Learn advanced version management techniques
- Set up organization-wide deployment
- Configure alert notifications
- Implement custom commit messages and labels
