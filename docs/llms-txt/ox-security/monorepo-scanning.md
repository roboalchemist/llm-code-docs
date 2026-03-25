# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/monorepo-scanning.md

# Monorepo Scanning

OX supports monorepo scanning, which is scanning repositories that contain multiple services or applications under a single root directory.

In OX, a monorepo can be managed either as a single OX application or divided into multiple OX applications using Monorepos Segmented Scanning. This setting controls how the repository is structured in the platform and how risk, policies, and workflows are applied. It does not affect scan depth or detection accuracy.

## When Monorepos Segmented Scanning Is Enabled

When enabled, OX divides a single repository into smaller OX applications based on the file names you define in the connector configuration.

Each folder that contains at least one of the specified file names is designated as a separate OX application. OX builds a separate dependency graph per segment, evaluates policies per segment, and calculates risk and prioritization at segment level. Each segment appears as an independent OX application in the platform and can follow its own workflow and ticketing configuration.

Findings remain mapped to their exact file paths. The segmentation affects organizational structure and risk calculation, not file-level visibility.

**To enable and define segmented scanning:**

1. Go to **Settings > Applications**.
2. Enable **Monorepos Segmented Scanning** (Default: enabled).
3. In the **File List** field, enter one or more file names that define application boundaries. File names are case-insensitive.
4. Click **Update**.

After saving the configuration, OX designates any folder that contains at least one of the specified files as a separate OX application during subsequent scans.

If you modify the file list and click Update, OX applies the updated segmentation rules to future scans.

## When Monorepos Segmented Scanning Is Disabled

When segmented scanning is disabled, OX treats the repository root as a single OX application.

All detected manifests are analyzed together under one repository context. A unified dependency graph is built, policies apply at repository scope, and findings are aggregated under one application.

Findings are still associated with their specific file paths, and full analysis is preserved. Ownership, prioritization, reporting, and workflows are calculated at repository level rather than per service.
